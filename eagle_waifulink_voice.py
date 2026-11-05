"""
WaifuLink JP Voice Engine v1.0 for Project Eagle (`gta sa gameplay-lab`).

Asynchronous Japanese Seiyuu Voice-Over playback engine powered by Windows Multimedia API
(`winmm.dll` -> `mciSendStringW` / `PlaySoundW`) running inside the `EagleCompanion.py` sidecar.
Zero ASI injection, zero GTA SA `GENRL`/`SFX` archive modification, zero crash risk.

Covers 6 WaifuLink v4.0 heroines (`hutao`, `furina`, `citlali`, `columbina`, `kirara`, `vesna`)
across 8 contextual emotion buckets:
  1. `greet_doorstep`      — Approaching Waifu's doorstep (<= 22m) or opening `[F9]` House Menu
  2. `vn_sweet_happy`      — VN / Chat happy, sweet, delighted, `BEST` choice, gift reaction
  3. `vn_shy_blush`        — VN / Chat blushing, flustered, shy, tsundere
  4. `vn_playful_tease`    — VN / Chat playful, teasing, mischievous, sassy
  5. `vn_tender_love`      — VN `Scene 4/4` romantic ending / deep heartfelt confession
  6. `outing_cruise`       — Boarding `575 Broadway` convertible & smooth 40s cruise chatter
  7. `outing_bump_rescue`  — Free-Roam vehicle collision HP drop or `< 250 HP` burning-car rescue
  8. `outing_arrive_photo` — S/A-Rank destination arrival or Time-Apart Milestone Photo Drop
"""
from __future__ import annotations

import ctypes
import datetime
import json
import os
import queue
import random
import threading
import time
import wave
from collections import deque
from pathlib import Path
from typing import Any, Callable, Optional

ADDR_MENU_ACTIVE = 0x00BA67A4  # CMenuManager::m_bMenuActive (uint8: != 0 when GTA SA Pause Menu is open)

SUPPORTED_CHARS: tuple[str, ...] = (
    "hutao",
    "furina",
    "citlali",
    "columbina",
    "kirara",
    "vesna",
)

VOICE_BUCKETS: tuple[str, ...] = (
    "greet_doorstep",
    "vn_sweet_happy",
    "vn_shy_blush",
    "vn_playful_tease",
    "vn_tender_love",
    "outing_cruise",
    "outing_bump_rescue",
    "outing_arrive_photo",
)

DEFAULT_COOLDOWNS: dict[str, float] = {
    "greet_doorstep": 25.0,
    "outing_cruise": 40.0,
    "outing_bump_rescue": 3.5,
    "outing_arrive_photo": 1.2,
    "vn_sweet_happy": 0.0,
    "vn_shy_blush": 0.0,
    "vn_playful_tease": 0.0,
    "vn_tender_love": 0.0,
}

SEIYUU_CREDITS: dict[str, str] = {
    "hutao": "Rie Takahashi (高橋李依)",
    "furina": "Inori Minase (水瀬いのり)",
    "citlali": "Asami Tano (田野アサミ)",
    "columbina": "Lynn (りん)",
    "kirara": "Sayumi Suzushiro (鈴代紗弓)",
    "vesna": "Aya Endo (遠藤綾)",
}

SND_SYNC = 0x0000
SND_ASYNC = 0x0001
SND_NODEFAULT = 0x0002
SND_PURGE = 0x0040
SND_FILENAME = 0x00020000


def classify_mood_to_vn_bucket(
    mood: str = "",
    scene_num: int = 1,
    grade: str = "",
    passed: Optional[bool] = None,
    text_hint: str = "",
) -> str:
    """Maps a WaifuLink mood label, choice grade, or VN scene context to one of the 4 `vn_*` buckets."""
    m = (mood or "").strip().lower()
    g = (grade or "").strip().upper()
    h = (text_hint or "").strip().lower()

    if scene_num >= 4 and passed is True:
        return "vn_tender_love"

    # 1. Explicit mood keyword matching
    shy_kw = (
        "blush",
        "fluster",
        "shy",
        "tsundere",
        "embarrass",
        "pout",
        "nervous",
        "stam",
        "bashful",
        "awkward",
        "hmph",
    )
    tender_kw = (
        "tender",
        "love",
        "touch",
        "serene",
        "soulmate",
        "dreamy",
        "devot",
        "intimate",
        "affectionate",
        "eternal",
        "cherish",
        "gentle",
        "warm",
    )
    tease_kw = (
        "playful",
        "teas",
        "mischiev",
        "sassy",
        "smug",
        "wink",
        "prank",
        "cheeky",
        "confident",
        "sly",
    )
    happy_kw = (
        "happy",
        "delight",
        "sweet",
        "cheer",
        "excit",
        "overjoy",
        "joy",
        "charm",
        "proud",
        "cozy",
        "sparkl",
    )

    if any(k in m for k in shy_kw):
        return "vn_shy_blush"
    if any(k in m for k in tender_kw):
        return "vn_tender_love"
    if any(k in m for k in tease_kw):
        return "vn_playful_tease"
    if any(k in m for k in happy_kw):
        return "vn_sweet_happy"

    # 2. Grade-based fallback
    if g == "REASK_OFF_TOPIC":
        return "vn_playful_tease"
    if g == "AWKWARD":
        return "vn_shy_blush"
    if g == "BEST":
        return "vn_tender_love" if scene_num >= 3 else "vn_sweet_happy"

    # 3. Text cue fallback (from scene narration / inner thought / dialogue)
    if any(k in h for k in ("blush", "cheeks flush", "stammer", "looks away", "flustered", "h-hey", "w-what")):
        return "vn_shy_blush"
    if any(k in h for k in ("tease", "wink", "giggle", "prank", "hehe", "mischievous", "smirk")):
        return "vn_playful_tease"
    if scene_num >= 3 or any(k in h for k in ("heartbeat", "moonlight", "forever", "hold hands", "embrace", "whisper")):
        return "vn_tender_love"

    return "vn_sweet_happy"


class WaifuLinkVoiceEngine:
    """
    Thread-safe asynchronous Japanese voice playback & telemetry engine for WaifuLink v4.0.
    All `mciSendStringW` commands execute on a single dedicated worker thread to guarantee
    Win32 MCI alias thread-affinity (`wl_voice`).
    """

    MCI_ALIAS = "wl_voice"

    def __init__(
        self,
        voices_dir: Optional[Path] = None,
        settings_path: Optional[Path] = None,
        pause_checker: Optional[Callable[[], bool]] = None,
        cooldown_overrides: Optional[dict[str, float]] = None,
    ) -> None:
        repo_root = Path(__file__).resolve().parent.parent.parent
        default_dating_dir = repo_root / "data" / "project-eagle" / "dating-sim"
        self.voices_dir = Path(voices_dir) if voices_dir else (default_dating_dir / "voices")
        self.settings_path = Path(settings_path) if settings_path else (default_dating_dir / "voice_settings.json")
        self.manifest_path = self.voices_dir / "manifest.json"
        self._pause_checker = pause_checker
        self._state_listener: Optional[Callable[[bool], None]] = None

        self._lock = threading.RLock()
        self.cooldowns: dict[str, float] = dict(DEFAULT_COOLDOWNS)
        if cooldown_overrides:
            self.cooldowns.update(cooldown_overrides)

        # Persisted user settings
        self.voice_enabled: bool = True
        self.voice_volume: int = 80  # 0..100
        self._load_settings()

        # Catalog & round-robin state
        self.manifest_meta: dict[str, Any] = {}
        self.catalog: dict[str, dict[str, list[Path]]] = {}
        self.clip_meta_by_rel: dict[str, dict[str, Any]] = {}
        self._rr_queues: dict[tuple[str, str], list[Path]] = {}
        self._last_picked_file: dict[tuple[str, str], str] = {}
        self._last_bucket_play_ts: dict[tuple[str, str], float] = {}
        self._global_last_bucket_ts: dict[str, float] = {}
        self.reload_catalog()

        # Live playback & telemetry state
        self._is_playing: bool = False
        self._paused_by_menu: bool = False
        self._active_end_estimate: float = 0.0
        self._active_driver: str = "mci_mpegvideo"
        self._play_count: int = 0
        self._per_char_counts: dict[str, int] = {c: 0 for c in SUPPORTED_CHARS}
        self._per_bucket_counts: dict[str, int] = {b: 0 for b in VOICE_BUCKETS}
        self._last_voice_played: Optional[dict[str, Any]] = None
        self._recent_history: deque[dict[str, Any]] = deque(maxlen=25)

        # Dedicated Win32 MCI command thread
        self._cmd_queue: queue.Queue[tuple[str, dict[str, Any]]] = queue.Queue()
        self._closed = False
        self._winmm = ctypes.windll.winmm if os.name == "nt" else None
        self._worker_thread = threading.Thread(
            target=self._mci_worker_loop,
            name="WaifuLinkJPVoiceWorker",
            daemon=True,
        )
        self._worker_thread.start()

    # ------------------------------------------------------------------
    # Settings & Catalog Loading
    # ------------------------------------------------------------------
    def _load_settings(self) -> None:
        if not self.settings_path.exists():
            self._save_settings()
            return
        try:
            raw = json.loads(self.settings_path.read_text(encoding="utf-8-sig"))
            if "voice_enabled" in raw:
                self.voice_enabled = bool(raw["voice_enabled"])
            if "voice_volume" in raw:
                self.voice_volume = max(0, min(100, int(raw["voice_volume"])))
        except Exception:
            pass

    def _save_settings(self) -> None:
        try:
            self.settings_path.parent.mkdir(parents=True, exist_ok=True)
            payload = {
                "voice_enabled": bool(self.voice_enabled),
                "voice_volume": int(self.voice_volume),
                "updated_at": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(),
            }
            self.settings_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        except Exception:
            pass

    def update_settings(
        self,
        voice_enabled: Optional[bool] = None,
        voice_volume: Optional[int] = None,
    ) -> dict[str, Any]:
        with self._lock:
            if voice_enabled is not None:
                self.voice_enabled = bool(voice_enabled)
            if voice_volume is not None:
                self.voice_volume = max(0, min(100, int(voice_volume)))
            self._save_settings()
            enabled_now = self.voice_enabled
            vol_now = self.voice_volume

        if not enabled_now:
            self.stop()
        else:
            self._cmd_queue.put(("set_volume", {"volume": vol_now}))
        return self.get_settings()

    def get_settings(self) -> dict[str, Any]:
        with self._lock:
            return {
                "ok": True,
                "voice_enabled": self.voice_enabled,
                "voice_volume": self.voice_volume,
                "settings_path": str(self.settings_path),
            }

    def set_pause_checker(self, checker: Optional[Callable[[], bool]]) -> None:
        self._pause_checker = checker

    def set_state_listener(self, listener: Optional[Callable[[bool], None]]) -> None:
        self._state_listener = listener

    def _emit_voice_state(self, active: bool) -> None:
        cb = self._state_listener
        if cb is not None:
            try:
                cb(bool(active))
            except Exception:
                pass

    def reload_catalog(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        new_catalog: dict[str, dict[str, list[Path]]] = {
            cid: {b: [] for b in VOICE_BUCKETS} for cid in SUPPORTED_CHARS
        }
        clip_meta: dict[str, dict[str, Any]] = {}

        if self.manifest_path.exists():
            try:
                mdata = json.loads(self.manifest_path.read_text(encoding="utf-8-sig"))
                self.manifest_meta = mdata
                for item in mdata.get("files", []):
                    rel = str(item.get("rel_path") or "").replace("\\", "/")
                    if rel:
                        clip_meta[rel] = item
            except Exception:
                pass

        if self.voices_dir.exists():
            for cid in SUPPORTED_CHARS:
                cdir = self.voices_dir / cid
                if not cdir.is_dir():
                    counts[cid] = 0
                    continue
                files = sorted(
                    p for p in cdir.iterdir()
                    if p.is_file() and p.suffix.lower() in (".wav", ".mp3") and p.stat().st_size > 1024
                )
                for p in files:
                    stem_low = p.stem.lower()
                    matched_b = next((b for b in VOICE_BUCKETS if stem_low.startswith(b)), None)
                    if matched_b:
                        new_catalog[cid][matched_b].append(p)
                counts[cid] = sum(len(v) for v in new_catalog[cid].values())
        else:
            for cid in SUPPORTED_CHARS:
                counts[cid] = 0

        with self._lock:
            self.catalog = new_catalog
            self.clip_meta_by_rel = clip_meta
            self._rr_queues.clear()
        return counts

    # ------------------------------------------------------------------
    # Pause Menu Check (`0x00BA67A4 != 0`)
    # ------------------------------------------------------------------
    def is_game_paused(self) -> bool:
        if self._pause_checker is not None:
            try:
                return bool(self._pause_checker())
            except Exception:
                return False
        return False

    @staticmethod
    def read_pause_flag_from_bridge(bridge: Any) -> bool:
        """Reads `CMenuManager::m_bMenuActive` (`0x00BA67A4`) safely when attached to `gta_pe.exe`."""
        if bridge is None:
            return False
        try:
            if hasattr(bridge, "try_attach") and not bridge.try_attach():
                return False
            val = bridge.read_u8(ADDR_MENU_ACTIVE)
            return bool(val is not None and int(val) != 0)
        except Exception:
            return False

    # ------------------------------------------------------------------
    # Clip Selection & Duration Helper
    # ------------------------------------------------------------------
    def _estimate_duration_sec(self, path: Path) -> float:
        rel = f"{path.parent.name}/{path.name}"
        meta = self.clip_meta_by_rel.get(rel)
        if meta and meta.get("duration_sec"):
            return float(meta["duration_sec"])
        if path.suffix.lower() == ".wav":
            try:
                with wave.open(str(path), "rb") as wf:
                    rate = wf.getframerate()
                    frames = wf.getnframes()
                    if rate > 0:
                        return round(frames / float(rate), 3)
            except Exception:
                pass
        return 2.8

    def _pick_clip(self, char_id: str, bucket: str) -> Optional[Path]:
        with self._lock:
            char_buckets = self.catalog.get(char_id) or {}
            candidates = list(char_buckets.get(bucket) or [])
            if not candidates:
                # Fallback to another VN bucket of the same character if needed
                for alt_b in ("vn_sweet_happy", "vn_playful_tease", "vn_tender_love", "greet_doorstep"):
                    if char_buckets.get(alt_b):
                        candidates = list(char_buckets[alt_b])
                        break
            if not candidates:
                return None

            key = (char_id, bucket)
            q = self._rr_queues.get(key)
            if not q:
                shuffled = list(candidates)
                if len(shuffled) > 1:
                    random.shuffle(shuffled)
                    last_name = self._last_picked_file.get(key, "")
                    if last_name and shuffled[0].name == last_name:
                        shuffled.append(shuffled.pop(0))
                q = shuffled
                self._rr_queues[key] = q

            picked = q.pop(0)
            self._last_picked_file[key] = picked.name
            return picked

    def is_currently_playing(self) -> bool:
        with self._lock:
            if not self._is_playing:
                return False
            if self._paused_by_menu:
                return True
            return time.time() < self._active_end_estimate

    def reset_bucket_cooldown(self, char_id: str = "", bucket: str = "") -> None:
        with self._lock:
            if not char_id and not bucket:
                self._last_bucket_play_ts.clear()
                self._global_last_bucket_ts.clear()
                return
            keys = [
                k for k in self._last_bucket_play_ts
                if (not char_id or k[0] == char_id) and (not bucket or k[1] == bucket)
            ]
            for k in keys:
                self._last_bucket_play_ts.pop(k, None)
            if bucket:
                self._global_last_bucket_ts.pop(bucket, None)

    # ------------------------------------------------------------------
    # Primary Playback Entry Point
    # ------------------------------------------------------------------
    def play_event(
        self,
        char_id: str,
        bucket: str,
        mood: str = "",
        interrupt: bool = True,
        force_cooldown: bool = False,
    ) -> dict[str, Any]:
        """
        Triggers a Japanese voice line asynchronously for `char_id` in `bucket`.
        - VN scene transitions (`interrupt=True`): immediately stops the previous clip and plays
          the new line matching the scene's mood.
        - Ambient / Outing events (`interrupt=False`): respects per-bucket cooldowns
          (`greet_doorstep=25s`, `outing_cruise=40s`, `outing_bump_rescue=3.5s`) and never overlaps
          an active line unless `bucket == "outing_bump_rescue"` (emergency override).
        """
        cid = (char_id or "hutao").strip().lower()
        if cid not in SUPPORTED_CHARS:
            cid = "hutao"

        raw_bucket = (bucket or "").strip().lower()
        if raw_bucket in ("vn", "vn_auto", "vn_scene", "chat", "chat_auto", "auto", ""):
            resolved_bucket = classify_mood_to_vn_bucket(mood=mood)
        elif raw_bucket in VOICE_BUCKETS:
            resolved_bucket = raw_bucket
        else:
            resolved_bucket = classify_mood_to_vn_bucket(mood=mood or raw_bucket)

        # Emergency collision / burning-car rescue ALWAYS overrides ongoing cruise voice lines
        effective_interrupt = True if resolved_bucket == "outing_bump_rescue" else bool(interrupt)

        with self._lock:
            if not self.voice_enabled:
                return {"ok": False, "skipped": "voice_disabled", "char_id": cid, "bucket": resolved_bucket}

        if self.is_game_paused():
            return {"ok": False, "skipped": "game_paused", "char_id": cid, "bucket": resolved_bucket}

        now = time.time()
        with self._lock:
            # Non-overlap guard for ambient events
            if not effective_interrupt and self.is_currently_playing():
                return {"ok": False, "skipped": "busy_playing", "char_id": cid, "bucket": resolved_bucket}

            # Cooldown check
            cd_sec = 0.0 if force_cooldown else float(self.cooldowns.get(resolved_bucket, 0.0))
            if cd_sec > 0.0:
                last_ts = self._last_bucket_play_ts.get((cid, resolved_bucket), 0.0)
                if (now - last_ts) < cd_sec:
                    return {
                        "ok": False,
                        "skipped": "cooldown",
                        "char_id": cid,
                        "bucket": resolved_bucket,
                        "cooldown_remaining_sec": round(cd_sec - (now - last_ts), 2),
                    }

            clip_path = self._pick_clip(cid, resolved_bucket)
            if clip_path is None or not clip_path.exists():
                return {"ok": False, "skipped": "no_audio_file", "char_id": cid, "bucket": resolved_bucket}

            dur_sec = self._estimate_duration_sec(clip_path)
            rel_path = f"{cid}/{clip_path.name}"
            clip_info = self.clip_meta_by_rel.get(rel_path, {})

            self._last_bucket_play_ts[(cid, resolved_bucket)] = now
            self._global_last_bucket_ts[resolved_bucket] = now
            self._play_count += 1
            self._per_char_counts[cid] = self._per_char_counts.get(cid, 0) + 1
            self._per_bucket_counts[resolved_bucket] = self._per_bucket_counts.get(resolved_bucket, 0) + 1
            self._is_playing = True
            self._paused_by_menu = False
            self._active_end_estimate = now + dur_sec + 0.12

            event_record = {
                "char_id": cid,
                "bucket": resolved_bucket,
                "mood": str(mood or ""),
                "file": clip_path.name,
                "rel_path": rel_path,
                "seiyuu": clip_info.get("seiyuu") or SEIYUU_CREDITS.get(cid, ""),
                "jp_text": clip_info.get("jp_text", ""),
                "source_title": clip_info.get("source_title", ""),
                "duration_sec": round(dur_sec, 3),
                "interrupt": effective_interrupt,
                "volume": int(self.voice_volume),
                "timestamp": round(now, 3),
                "iso_time": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(),
                "play_count": self._play_count,
                "mci_ok": True,
            }
            self._last_voice_played = event_record
            self._recent_history.append(dict(event_record))
            vol_now = int(self.voice_volume)

        self._emit_voice_state(True)
        self._cmd_queue.put(
            (
                "play",
                {
                    "path": str(clip_path.resolve()),
                    "volume": vol_now,
                    "duration_sec": dur_sec,
                    "record": event_record,
                },
            )
        )
        return {"ok": True, "played": dict(event_record)}

    def stop(self) -> None:
        with self._lock:
            self._is_playing = False
            self._paused_by_menu = False
            self._active_end_estimate = 0.0
        self._emit_voice_state(False)
        self._cmd_queue.put(("stop", {}))

    def shutdown(self) -> None:
        self._closed = True
        self._cmd_queue.put(("shutdown", {}))

    # ------------------------------------------------------------------
    # Telemetry Snapshot for `/api/state` (`dating_sim.voice_telemetry`)
    # ------------------------------------------------------------------
    def get_telemetry(self) -> dict[str, Any]:
        with self._lock:
            playing = self.is_currently_playing()
            return {
                "engine": "WaifuLink JP Voice Engine v1.0",
                "backend": self._active_driver,
                "voice_enabled": self.voice_enabled,
                "voice_volume": self.voice_volume,
                "is_playing": playing,
                "paused_by_menu": self._paused_by_menu,
                "play_count": self._play_count,
                "per_char_counts": dict(self._per_char_counts),
                "per_bucket_counts": dict(self._per_bucket_counts),
                "last_voice_played": dict(self._last_voice_played) if self._last_voice_played else None,
                "recent_history": list(self._recent_history)[-10:],
            }

    # ------------------------------------------------------------------
    # Dedicated Win32 `winmm.dll` (`mciSendStringW` / `PlaySoundW`) Thread
    # ------------------------------------------------------------------
    def _mci_send(self, cmd: str) -> tuple[int, str]:
        if self._winmm is None:
            return (0, "")
        buf = ctypes.create_unicode_buffer(256)
        err = int(self._winmm.mciSendStringW(cmd, buf, 255, None))
        return (err, buf.value.strip())

    def _mci_close_current(self) -> None:
        if self._winmm is None:
            return
        self._mci_send(f"stop {self.MCI_ALIAS}")
        self._mci_send(f"close {self.MCI_ALIAS}")
        try:
            self._winmm.PlaySoundW(None, None, SND_PURGE)
        except Exception:
            pass

    def _mci_start_file(self, file_path: str, volume: int, record: dict[str, Any]) -> None:
        self._mci_close_current()
        if self._winmm is None:
            return

        mci_vol = max(0, min(1000, int(round(volume * 10))))
        # 1. Try DirectShow MCI (`type mpegvideo`) first so `setaudio volume to 0..1000` works on `.wav` & `.mp3`
        err_open, _ = self._mci_send(f'open "{file_path}" type mpegvideo alias {self.MCI_ALIAS}')
        if err_open == 0:
            self._mci_send(f"setaudio {self.MCI_ALIAS} volume to {mci_vol}")
            err_play, _ = self._mci_send(f"play {self.MCI_ALIAS} from 0")
            if err_play == 0:
                with self._lock:
                    self._active_driver = "mci_mpegvideo"
                    record["mci_ok"] = True
                return
            self._mci_send(f"close {self.MCI_ALIAS}")

        # 2. Fallback to `type waveaudio`
        err_wopen, _ = self._mci_send(f'open "{file_path}" type waveaudio alias {self.MCI_ALIAS}')
        if err_wopen == 0:
            err_wplay, _ = self._mci_send(f"play {self.MCI_ALIAS} from 0")
            if err_wplay == 0:
                with self._lock:
                    self._active_driver = "mci_waveaudio"
                    record["mci_ok"] = True
                return
            self._mci_send(f"close {self.MCI_ALIAS}")

        # 3. Last-resort fallback to `PlaySoundW` async
        try:
            if volume > 0:
                ok_ps = bool(self._winmm.PlaySoundW(file_path, None, SND_FILENAME | SND_ASYNC | SND_NODEFAULT))
            else:
                ok_ps = True
            with self._lock:
                self._active_driver = "playsound_async"
                record["mci_ok"] = ok_ps
        except Exception:
            with self._lock:
                record["mci_ok"] = False

    def _mci_poll_playback_and_pause(self) -> None:
        if self._winmm is None:
            return
        with self._lock:
            currently_active = self._is_playing
            was_paused = self._paused_by_menu
        if not currently_active:
            return

        err_mode, mode_str = self._mci_send(f"status {self.MCI_ALIAS} mode")
        mode_low = mode_str.lower()
        if err_mode == 0 and mode_low in ("stopped", "not ready"):
            self._mci_close_current()
            with self._lock:
                self._is_playing = False
                self._paused_by_menu = False
                self._active_end_estimate = 0.0
            self._emit_voice_state(False)
            return

        game_paused = self.is_game_paused()
        if game_paused and not was_paused:
            self._mci_send(f"pause {self.MCI_ALIAS}")
            with self._lock:
                self._paused_by_menu = True
        elif (not game_paused) and was_paused:
            self._mci_send(f"resume {self.MCI_ALIAS}")
            with self._lock:
                self._paused_by_menu = False
                self._active_end_estimate = max(self._active_end_estimate, time.time() + 1.5)
        elif not was_paused and time.time() > (self._active_end_estimate + 0.6):
            self._mci_close_current()
            with self._lock:
                self._is_playing = False
                self._active_end_estimate = 0.0
            self._emit_voice_state(False)

    def _mci_worker_loop(self) -> None:
        while not self._closed:
            try:
                cmd, payload = self._cmd_queue.get(timeout=0.10)
            except queue.Empty:
                try:
                    self._mci_poll_playback_and_pause()
                except Exception:
                    pass
                continue

            try:
                if cmd == "shutdown":
                    self._mci_close_current()
                    break
                elif cmd == "stop":
                    self._mci_close_current()
                elif cmd == "set_volume":
                    vol = max(0, min(100, int(payload.get("volume", 80))))
                    self._mci_send(f"setaudio {self.MCI_ALIAS} volume to {vol * 10}")
                elif cmd == "play":
                    # Drain any stale queued 'play' commands if multiple arrived within the same millisecond
                    latest_payload = payload
                    while True:
                        try:
                            nxt_cmd, nxt_pl = self._cmd_queue.get_nowait()
                            if nxt_cmd == "play":
                                latest_payload = nxt_pl
                            elif nxt_cmd == "stop":
                                latest_payload = None
                            elif nxt_cmd == "shutdown":
                                self._mci_close_current()
                                return
                        except queue.Empty:
                            break
                    if latest_payload is not None:
                        self._mci_start_file(
                            latest_payload["path"],
                            int(latest_payload["volume"]),
                            latest_payload["record"],
                        )
            except Exception:
                pass


def verify_mci_file_open_and_play(file_path: Path, play_ms: int = 80, muted: bool = True) -> dict[str, Any]:
    """
    Standalone verification helper that tests opening, querying length, setting volume,
    starting playback, and closing a voice file through `winmm.dll` `mciSendStringW`.
    """
    if os.name != "nt":
        return {"ok": True, "driver": "non_nt_skip"}
    winmm = ctypes.windll.winmm
    alias = f"wl_chk_{os.getpid()}_{random.randint(1000, 9999)}"
    buf = ctypes.create_unicode_buffer(256)

    def _call(c: str) -> tuple[int, str]:
        rc = int(winmm.mciSendStringW(c, buf, 255, None))
        return rc, buf.value.strip()

    abs_p = str(file_path.resolve())
    rc_open, _ = _call(f'open "{abs_p}" type mpegvideo alias {alias}')
    driver = "mpegvideo"
    if rc_open != 0:
        rc_open, _ = _call(f'open "{abs_p}" type waveaudio alias {alias}')
        driver = "waveaudio"
    if rc_open != 0:
        return {"ok": False, "error": f"mci open failed rc={rc_open}", "file": abs_p}

    try:
        _call(f"set {alias} time format milliseconds")
        rc_len, len_str = _call(f"status {alias} length")
        if driver == "mpegvideo":
            _call(f"setaudio {alias} volume to {0 if muted else 300}")
        rc_play, _ = _call(f"play {alias} from 0")
        if play_ms > 0:
            time.sleep(play_ms / 1000.0)
        rc_mode, mode_str = _call(f"status {alias} mode")
        _call(f"stop {alias}")
        return {
            "ok": rc_play == 0,
            "driver": driver,
            "mci_length_ms": int(len_str) if (rc_len == 0 and len_str.isdigit()) else -1,
            "mode_sampled": mode_str if rc_mode == 0 else "",
        }
    finally:
        _call(f"close {alias}")
