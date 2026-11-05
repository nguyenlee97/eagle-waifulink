"""
WaifuLink Genshin BGM Engine v1.1 (`eagle_waifulink_bgm.py`)
============================================================
Dedicated background music engine for Project Eagle's Dating Sim & Pure Visual Novel
ecosystem (`Girlfriend Hub`, `Scenario Mode`, and `Story Quest 5-Chapter Mode`).

Key Engineering Guarantees:
1. Dual-MCI Thread Isolation:
   - Owns a dedicated OS worker thread (`WaifuLinkBGMWorker`) exclusively driving Win32
     `mciSendStringW` with `alias wl_bgm` (`type mpegvideo`), 100% isolated from
     `alias wl_voice` in `eagle_waifulink_voice.py`.
2. Short-Path & Clean ASCII Cache Guard:
   - Resolves `bgm_cache/<id>.mp3` or Win32 `GetShortPathNameW`, automatically materializing
     clean ASCII `.mp3` cache files (`trk_<hash>.mp3`) if `D:\\` disables 8.3 short names or
     source paths contain Unicode / `.m4a` / ID3 cover-art headers (`err 275/277/292`).
   - Strictly read-only with respect to `D:\\Music` and `tools/eagle-radio-studio`.
3. Smart Mixing & Lifecycle:
   - Per-track dBFS loudness-normalized bed volume (`~192..238 / 1000`, centered at `220 / 1000`).
   - Voice Auto-Ducking: ramps smoothly to `~85 / 1000` over `150ms` when Japanese Seiyuu
     voice plays, holds `300ms` after voice finishes, then restores smoothly over `260ms`.
   - Mood Crossfading (`350ms` fade-out -> switch -> `350ms` fade-in) & `EOF Auto-Next`
     (`position >= length - 250` or `mode == stopped`) without repeating the previous track.
   - GTA SA Pause Menu guard (`0x00BA67A4` `CMenuManager::m_bMenuActive`) & immediate
     fade-out + close on Free Roam convertible driving or 3D open-world return (zero RadioEx clash).
4. Per-Process GTA SA Ambient Noise Isolation (`GTAPerProcessAudioMuter`, v1.1):
   - Automatically mutes ONLY `gta_pe.exe`'s Windows CoreAudio WASAPI sessions (`DirectSound8`
     street traffic/horns/pedestrian shouts + CLEO `BASS.dll` ambient audio) during fullscreen
     `vn_scenario` and `story_quest` modes, leaving `EagleCompanion.py` (`wl_bgm` + `wl_voice`)
     100% audible and restoring `gta_pe.exe` immediately on exit (`atexit` + crash guard).
"""

from __future__ import annotations

import atexit
import ctypes
from ctypes import wintypes
import datetime
import hashlib
import json
import os
import queue
import random
import shutil
import subprocess
import threading
import time
from pathlib import Path
from typing import Any, Callable, Optional

# GTA SA 1.0 US `CMenuManager::m_bMenuActive` (`FrontEndMenuManager + 0x32`)
GTA_PAUSE_MENU_ADDR = 0x00BA67A4

DEFAULT_GTA_MUTE_MODES: tuple[str, ...] = (
    "vn_scenario",
    "story_quest",
)

DEFAULT_GTA_EXE_NAMES: tuple[str, ...] = (
    "gta_pe.exe",
    "gta_sa.exe",
)

BGM_MOOD_BUCKETS: tuple[str, ...] = (
    "hub_cozy",
    "vn_daily_sweet",
    "vn_tender_romance",
    "vn_melancholy_memory",
    "vn_mystic_tension",
)

SUPPORTED_CHARS: tuple[str, ...] = (
    "hutao",
    "furina",
    "citlali",
    "columbina",
    "kirara",
    "vesna",
)

FFMPEG_CANDIDATES: tuple[str, ...] = (
    r"C:\PATH_Program\ffmpeg.EXE",
    "ffmpeg",
)


def sanitize_hud_ascii(text: Any, max_len: int = 64) -> str:
    """Clean string to strict GTA SA CFont-safe printable ASCII."""
    raw = (
        str(text or "")
        .replace("~", "-")
        .replace("*", "")
        .replace("•", "-")
        .replace("|", "-")
        .replace("—", " - ")
        .replace("–", "-")
        .replace("…", "...")
        .replace("’", "'")
        .replace("‘", "'")
        .replace("“", '"')
        .replace("”", '"')
    )
    cleaned = "".join(ch for ch in raw if 32 <= ord(ch) <= 126)
    compact = " ".join(cleaned.split()).strip()
    if max_len > 3 and len(compact) > max_len:
        return compact[: max_len - 3].rstrip() + "..."
    return compact


def get_win32_short_path(path_str: str) -> str:
    """Attempt to resolve Win32 8.3 short path (`GetShortPathNameW`) on Windows."""
    if os.name != "nt" or not path_str:
        return path_str
    try:
        kernel32 = ctypes.windll.kernel32
        buf_len = max(512, len(path_str) + 64)
        buf = ctypes.create_unicode_buffer(buf_len)
        res = int(kernel32.GetShortPathNameW(str(path_str), buf, buf_len))
        if 0 < res < buf_len and buf.value:
            return buf.value
    except Exception:
        pass
    return path_str


# ----------------------------------------------------------------------
# Windows CoreAudio WASAPI Per-Process Audio Muter (`gta_pe.exe` only)
# ----------------------------------------------------------------------
class _COMGUID(ctypes.Structure):
    _fields_ = [
        ("Data1", wintypes.DWORD),
        ("Data2", wintypes.WORD),
        ("Data3", wintypes.WORD),
        ("Data4", ctypes.c_ubyte * 8),
    ]

    @classmethod
    def from_str(cls, guid_str: str) -> "_COMGUID":
        g = cls()
        if os.name == "nt":
            ctypes.windll.ole32.IIDFromString(ctypes.c_wchar_p(guid_str), ctypes.byref(g))
        return g


def _com_vtable_fn(ptr: ctypes.c_void_p, idx: int, restype: Any, *argtypes: Any) -> Any:
    vtbl = ctypes.cast(ptr, ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p))).contents
    fn_type = ctypes.WINFUNCTYPE(restype, ctypes.c_void_p, *argtypes)
    return fn_type(vtbl[idx])


def _com_release(ptr: Optional[ctypes.c_void_p]) -> None:
    if ptr is not None and bool(ptr.value):
        try:
            _com_vtable_fn(ptr, 2, wintypes.ULONG)(ptr)
        except Exception:
            pass
        ptr.value = None


class GTAPerProcessAudioMuter:
    """
    Silences ONLY `gta_pe.exe` (DirectSound8 traffic/horns/peds + CLEO BASS.dll street sounds)
    via Windows CoreAudio WASAPI `ISimpleAudioVolume::SetMute`, leaving `EagleCompanion.py`
    (`alias wl_bgm` + `alias wl_voice`) 100% audible and never modifying `gta_sa.set`.

    Includes crash-recovery guard (`gta_audio_guard.json`) + `atexit` unmute so `gta_pe.exe`
    can never remain stuck muted even after an unclean exit or `Alt+F4`.
    """

    PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
    CLSCTX_ALL = 23
    COINIT_MULTITHREADED = 0x0
    RPC_E_CHANGED_MODE = -2147417850  # 0x80010106

    def __init__(
        self,
        guard_path: Optional[Path] = None,
        enabled: bool = True,
        target_exe_names: Optional[tuple[str, ...]] = None,
        target_pids: Optional[set[int]] = None,
    ) -> None:
        self.enabled: bool = bool(enabled and os.name == "nt")
        self.guard_path: Optional[Path] = Path(guard_path) if guard_path else None
        self.target_exe_names: tuple[str, ...] = tuple(
            str(x).strip().lower()
            for x in (target_exe_names if target_exe_names is not None else DEFAULT_GTA_EXE_NAMES)
            if str(x).strip()
        )
        self.target_pids: set[int] = set(int(p) for p in (target_pids or set()) if int(p) > 0)

        self._lock = threading.RLock()
        self._own_pid: int = os.getpid()
        self._pid_exe_cache: dict[int, tuple[float, str]] = {}

        self._want_muted: bool = False
        self._we_muted_gta: bool = False
        self._user_pre_muted: bool = False
        self._pending_crash_unmute: bool = False
        self._active_muted_sessions: int = 0
        self._last_scan_ts: float = 0.0
        self._last_error: str = ""

        if self.enabled:
            self._clsid_enumerator = _COMGUID.from_str("{BCDE0395-E52F-467C-8E3D-C4579291692E}")
            self._iid_enumerator = _COMGUID.from_str("{A95664D2-9614-4F35-A746-DE8DB63617E6}")
            self._iid_session_mgr2 = _COMGUID.from_str("{77AA99A0-1BD6-484F-8BC7-2C654C9A9B6F}")
            self._iid_session_ctrl2 = _COMGUID.from_str("{BFB7FF88-7239-4FC9-8FA2-07C950BE9C6D}")
            self._iid_simple_vol = _COMGUID.from_str("{87CE5498-68D6-44E5-9215-6DA47EF883D8}")
            self._load_crash_guard()
            atexit.register(self.force_restore)

    @property
    def is_currently_muted(self) -> bool:
        with self._lock:
            return bool(self._we_muted_gta and self._want_muted)

    @property
    def muted_session_count(self) -> int:
        with self._lock:
            return int(self._active_muted_sessions) if (self._we_muted_gta and self._want_muted) else 0

    def needs_poll(self) -> bool:
        with self._lock:
            return bool(self.enabled and (self._want_muted or self._we_muted_gta or self._pending_crash_unmute))

    def _load_crash_guard(self) -> None:
        if self.guard_path is None or not self.guard_path.is_file():
            return
        try:
            raw = json.loads(self.guard_path.read_text(encoding="utf-8-sig"))
            if bool(raw.get("we_muted_gta", False)):
                self._pending_crash_unmute = True
        except Exception:
            pass

    def _write_crash_guard(self, we_muted: bool) -> None:
        if self.guard_path is None:
            return
        try:
            self.guard_path.parent.mkdir(parents=True, exist_ok=True)
            payload = {
                "we_muted_gta": bool(we_muted),
                "updated_at": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(),
            }
            self.guard_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        except Exception:
            pass

    def _resolve_pid_exe_name(self, pid: int, now: float) -> str:
        if pid <= 0:
            return ""
        cached = self._pid_exe_cache.get(pid)
        if cached is not None and (now - cached[0]) < 3.0:
            return cached[1]
        exe_name = ""
        if os.name == "nt":
            k32 = ctypes.windll.kernel32
            h_proc = k32.OpenProcess(self.PROCESS_QUERY_LIMITED_INFORMATION, False, wintypes.DWORD(pid))
            if h_proc:
                try:
                    buf = ctypes.create_unicode_buffer(520)
                    sz = wintypes.DWORD(520)
                    if k32.QueryFullProcessImageNameW(h_proc, 0, buf, ctypes.byref(sz)) and buf.value:
                        exe_name = os.path.basename(buf.value).strip().lower()
                finally:
                    k32.CloseHandle(h_proc)
        self._pid_exe_cache[pid] = (now, exe_name)
        return exe_name

    def _matches_target_session(self, pid: int, session_id_str: str, now: float) -> bool:
        if pid == self._own_pid:
            return False
        if self.target_pids and pid in self.target_pids:
            return True
        if pid > 0 and self.target_exe_names and not self.target_pids:
            exe_name = self._resolve_pid_exe_name(pid, now)
            if exe_name and exe_name in self.target_exe_names:
                return True
        if session_id_str and self.target_exe_names and not self.target_pids:
            sid_low = session_id_str.lower()
            for t_exe in self.target_exe_names:
                if f"\\{t_exe}" in sid_low or f"/{t_exe}" in sid_low:
                    return True
        return False

    def _enumerate_and_apply(self, action: str, now: float) -> tuple[int, int, bool]:
        """
        Enumerate all active WASAPI render endpoints and inspect/update matching target sessions.
        `action`: `'mute'` | `'unmute'` | `'inspect'`
        Returns `(matched_count, applied_count, all_already_muted)`.
        """
        if not self.enabled or os.name != "nt":
            return (0, 0, False)

        ole32 = ctypes.windll.ole32
        hr_init = int(ole32.CoInitializeEx(None, self.COINIT_MULTITHREADED))
        need_uninit = hr_init in (0, 1)  # S_OK or S_FALSE
        if hr_init < 0 and hr_init != self.RPC_E_CHANGED_MODE:
            return (0, 0, False)

        matched = 0
        applied = 0
        unmuted_seen = 0

        enum_ptr = ctypes.c_void_p()
        coll_ptr = ctypes.c_void_p()
        try:
            hr = int(
                ole32.CoCreateInstance(
                    ctypes.byref(self._clsid_enumerator),
                    None,
                    self.CLSCTX_ALL,
                    ctypes.byref(self._iid_enumerator),
                    ctypes.byref(enum_ptr),
                )
            )
            if hr != 0 or not enum_ptr.value:
                return (0, 0, False)

            # IMMDeviceEnumerator::EnumAudioEndpoints(eRender=0, DEVICE_STATE_ACTIVE=1)
            hr_e = int(
                _com_vtable_fn(
                    enum_ptr,
                    3,
                    ctypes.c_long,
                    ctypes.c_int,
                    wintypes.DWORD,
                    ctypes.POINTER(ctypes.c_void_p),
                )(enum_ptr, 0, 1, ctypes.byref(coll_ptr))
            )
            if hr_e != 0 or not coll_ptr.value:
                return (0, 0, False)

            dev_count = wintypes.UINT(0)
            _com_vtable_fn(coll_ptr, 3, ctypes.c_long, ctypes.POINTER(wintypes.UINT))(
                coll_ptr, ctypes.byref(dev_count)
            )

            for i in range(int(dev_count.value)):
                dev_ptr = ctypes.c_void_p()
                mgr_ptr = ctypes.c_void_p()
                sess_enum = ctypes.c_void_p()
                try:
                    if (
                        int(
                            _com_vtable_fn(
                                coll_ptr, 4, ctypes.c_long, wintypes.UINT, ctypes.POINTER(ctypes.c_void_p)
                            )(coll_ptr, i, ctypes.byref(dev_ptr))
                        )
                        != 0
                        or not dev_ptr.value
                    ):
                        continue

                    if (
                        int(
                            _com_vtable_fn(
                                dev_ptr,
                                3,
                                ctypes.c_long,
                                ctypes.POINTER(_COMGUID),
                                wintypes.DWORD,
                                ctypes.c_void_p,
                                ctypes.POINTER(ctypes.c_void_p),
                            )(dev_ptr, ctypes.byref(self._iid_session_mgr2), self.CLSCTX_ALL, None, ctypes.byref(mgr_ptr))
                        )
                        != 0
                        or not mgr_ptr.value
                    ):
                        continue

                    if (
                        int(
                            _com_vtable_fn(mgr_ptr, 5, ctypes.c_long, ctypes.POINTER(ctypes.c_void_p))(
                                mgr_ptr, ctypes.byref(sess_enum)
                            )
                        )
                        != 0
                        or not sess_enum.value
                    ):
                        continue

                    sess_count = ctypes.c_int(0)
                    _com_vtable_fn(sess_enum, 3, ctypes.c_long, ctypes.POINTER(ctypes.c_int))(
                        sess_enum, ctypes.byref(sess_count)
                    )

                    for j in range(int(sess_count.value)):
                        sctrl = ctypes.c_void_p()
                        sctrl2 = ctypes.c_void_p()
                        sav = ctypes.c_void_p()
                        try:
                            if (
                                int(
                                    _com_vtable_fn(
                                        sess_enum, 4, ctypes.c_long, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p)
                                    )(sess_enum, j, ctypes.byref(sctrl))
                                )
                                != 0
                                or not sctrl.value
                            ):
                                continue

                            if (
                                int(
                                    _com_vtable_fn(
                                        sctrl,
                                        0,
                                        ctypes.c_long,
                                        ctypes.POINTER(_COMGUID),
                                        ctypes.POINTER(ctypes.c_void_p),
                                    )(sctrl, ctypes.byref(self._iid_session_ctrl2), ctypes.byref(sctrl2))
                                )
                                != 0
                                or not sctrl2.value
                            ):
                                continue

                            pid_dw = wintypes.DWORD(0)
                            _com_vtable_fn(sctrl2, 14, ctypes.c_long, ctypes.POINTER(wintypes.DWORD))(
                                sctrl2, ctypes.byref(pid_dw)
                            )

                            sid_str = ""
                            pwsz_sid = ctypes.c_void_p()
                            try:
                                if (
                                    int(
                                        _com_vtable_fn(sctrl2, 12, ctypes.c_long, ctypes.POINTER(ctypes.c_void_p))(
                                            sctrl2, ctypes.byref(pwsz_sid)
                                        )
                                    )
                                    == 0
                                    and pwsz_sid.value
                                ):
                                    sid_str = ctypes.wstring_at(pwsz_sid.value)
                            finally:
                                if pwsz_sid.value:
                                    ole32.CoTaskMemFree(pwsz_sid)

                            if not self._matches_target_session(int(pid_dw.value), sid_str, now):
                                continue

                            if (
                                int(
                                    _com_vtable_fn(
                                        sctrl,
                                        0,
                                        ctypes.c_long,
                                        ctypes.POINTER(_COMGUID),
                                        ctypes.POINTER(ctypes.c_void_p),
                                    )(sctrl, ctypes.byref(self._iid_simple_vol), ctypes.byref(sav))
                                )
                                != 0
                                or not sav.value
                            ):
                                continue

                            matched += 1
                            cur_mute = wintypes.BOOL(0)
                            _com_vtable_fn(sav, 6, ctypes.c_long, ctypes.POINTER(wintypes.BOOL))(
                                sav, ctypes.byref(cur_mute)
                            )
                            if not bool(cur_mute.value):
                                unmuted_seen += 1

                            if action == "mute":
                                hr_set = int(
                                    _com_vtable_fn(sav, 5, ctypes.c_long, wintypes.BOOL, ctypes.c_void_p)(sav, 1, None)
                                )
                                if hr_set == 0:
                                    applied += 1
                            elif action == "unmute":
                                hr_set = int(
                                    _com_vtable_fn(sav, 5, ctypes.c_long, wintypes.BOOL, ctypes.c_void_p)(sav, 0, None)
                                )
                                if hr_set == 0:
                                    applied += 1
                        finally:
                            _com_release(sav)
                            _com_release(sctrl2)
                            _com_release(sctrl)
                finally:
                    _com_release(sess_enum)
                    _com_release(mgr_ptr)
                    _com_release(dev_ptr)
        except Exception as exc:
            with self._lock:
                self._last_error = f"wasapi_err:{exc}"
        finally:
            _com_release(coll_ptr)
            _com_release(enum_ptr)
            if need_uninit:
                try:
                    ole32.CoUninitialize()
                except Exception:
                    pass

        all_already_muted = (matched > 0) and (unmuted_seen == 0)
        return (matched, applied, all_already_muted)

    def inspect_sessions_muted(self) -> tuple[int, bool]:
        """Helper for diagnostics/tests: returns `(matched_count, all_muted)`."""
        matched, _, all_muted = self._enumerate_and_apply("inspect", time.monotonic())
        return (matched, all_muted)

    def sync(self, want_mute: bool, now: Optional[float] = None, force: bool = False) -> None:
        if not self.enabled:
            return
        ts = time.monotonic() if now is None else float(now)

        with self._lock:
            state_changed = bool(want_mute) != self._want_muted
            self._want_muted = bool(want_mute)

            if want_mute:
                if not state_changed and not force and (ts - self._last_scan_ts) < 0.45:
                    return
                self._last_scan_ts = ts

                # On first transition False -> True, check if user had ALREADY manually muted GTA in Windows Mixer
                if state_changed and not self._we_muted_gta and not self._pending_crash_unmute:
                    matched_0, _, all_muted_0 = self._enumerate_and_apply("inspect", ts)
                    if matched_0 > 0 and all_muted_0:
                        self._user_pre_muted = True
                        self._active_muted_sessions = 0
                        return
                    self._user_pre_muted = False

                if self._user_pre_muted:
                    return

                if not self._we_muted_gta:
                    self._write_crash_guard(True)
                    self._we_muted_gta = True
                    self._pending_crash_unmute = False

                _matched, applied, _ = self._enumerate_and_apply("mute", ts)
                self._active_muted_sessions = applied
            else:
                self._user_pre_muted = False
                if not self._we_muted_gta and not self._pending_crash_unmute:
                    self._active_muted_sessions = 0
                    return

                if not state_changed and not force and (ts - self._last_scan_ts) < 1.25:
                    return
                self._last_scan_ts = ts

                matched, applied, _ = self._enumerate_and_apply("unmute", ts)
                self._active_muted_sessions = 0
                if matched > 0 and applied > 0:
                    self._we_muted_gta = False
                    self._pending_crash_unmute = False
                    self._write_crash_guard(False)
                else:
                    # Target process exited before unmuting; keep crash guard armed so next GTA launch auto-unmutes
                    self._we_muted_gta = False
                    self._pending_crash_unmute = True

    def force_restore(self) -> None:
        """Immediate synchronous unmute invoked on `shutdown()` and `atexit`."""
        if not self.enabled:
            return
        try:
            self.sync(False, now=time.monotonic(), force=True)
        except Exception:
            pass


def infer_vn_bgm_bucket(
    mode: str = "hub",
    char_id: str = "",
    stage: int = 1,
    scene_idx: int = 1,
    mood: str = "",
    vn_session: Optional[dict[str, Any]] = None,
    story_session: Optional[dict[str, Any]] = None,
    story_campaign: Optional[dict[str, Any]] = None,
    explicit_bucket: str = "",
) -> str:
    """
    Zero-script-edit mood classifier for Girlfriend Hub, 4-Scene Scenario Mode, and
    5-Chapter Story Quest Mode.

    Guarantees node-level stability in Story Quest Mode so BGM never flip-flops on every beat.
    """
    exp = str(explicit_bucket or "").strip().lower()
    if exp in BGM_MOOD_BUCKETS:
        return exp

    m_norm = str(mode or "").strip().lower()
    if m_norm in ("hub", "house_menu", "phone_hub", "menu"):
        return "hub_cozy"

    # ------------------------------------------------------------------
    # Mode 1: Story Quest 5-Chapter Pure Visual Novel (`eagle_story_quest.py`)
    # ------------------------------------------------------------------
    if m_norm == "story_quest" or story_session is not None:
        sess = story_session or {}
        camp = story_campaign or {}
        nodes = camp.get("nodes") or {}
        nid = str(sess.get("node_id") or "")
        node = nodes.get(nid) or {}

        # 1. Explicit optional `bgm_bucket` on current beat (if author forced a mid-node shift) or node
        beat_override = ""
        beats_list = node.get("beats") or []
        b_idx = int(sess.get("beat_idx") or 0)
        if 0 <= b_idx < len(beats_list) and isinstance(beats_list[b_idx], dict):
            beat_override = str(beats_list[b_idx].get("bgm_bucket") or "").strip().lower()
        if beat_override in BGM_MOOD_BUCKETS:
            return beat_override

        node_override = str(node.get("bgm_bucket") or "").strip().lower()
        if node_override in BGM_MOOD_BUCKETS:
            return node_override

        # 2. Ending Screen / Terminal Ending Node classification
        end_id = str(sess.get("ending_id") or node.get("ending_id") or "").strip().upper()
        if end_id:
            if "TRUE" in end_id or "GOOD" in end_id:
                return "vn_tender_romance"
            if "BAD_2" in end_id or "BAD2" in end_id or "ABYSS" in end_id or "TRAGIC" in end_id:
                return "vn_mystic_tension"
            if "NEUTRAL" in end_id or "BAD_1" in end_id or "BAD1" in end_id or "BAD" in end_id:
                return "vn_melancholy_memory"

        # 3. Node-stabilized semantic analysis (uses node title, chapter, gate metadata & aggregate node beats)
        chapter_id = str(node.get("chapter_id") or "").strip().upper()
        title_low = str(node.get("title") or "").strip().lower()
        ch_obj = node.get("choice") or {}
        is_combo_gate = bool(
            ch_obj.get("combination_gate")
            or ch_obj.get("exclusive_rescue_gate")
            or "deduct" in str(ch_obj.get("prompt") or "").lower()
            or "clue" in str(ch_obj.get("prompt") or "").lower()
        )
        if is_combo_gate:
            return "vn_mystic_tension"

        sfx_tokens: list[str] = []
        ve_counts: dict[str, int] = {}
        sample_text_parts: list[str] = [title_low]
        for b in beats_list[:8]:
            if not isinstance(b, dict):
                continue
            sc = str(b.get("sfx_cue") or "").strip().lower()
            if sc:
                sfx_tokens.append(sc)
            ve = str(b.get("voice_emotion") or "").strip().lower()
            if ve:
                ve_counts[ve] = ve_counts.get(ve, 0) + 1
            sample_text_parts.append(str(b.get("text") or "").lower()[:160])

        sfx_blob = " ".join(sfx_tokens)
        node_blob = " ".join(sample_text_parts)

        mystic_title_kw = (
            "border",
            "ritual",
            "spirit",
            "soul",
            "lantern",
            "phantom",
            "shadow",
            "omen",
            "trial",
            "verdict",
            "testimony",
            "gate",
            "threshold",
            "abyss",
            "curse",
            "echo",
            "fog",
            "mist",
            "midnight",
            "vigil",
            "sanctuary",
            "altar",
            "prophecy",
            "unseen",
            "wuwang",
            "night-wind",
        )
        melancholy_title_kw = (
            "rain",
            "grief",
            "sorrow",
            "lonely",
            "solitude",
            "ashes",
            "regret",
            "farewell",
            "parting",
            "wound",
            "scar",
            "tears",
            "empty",
            "hollow",
            "forgotten",
            "fading",
            "mask",
            "burden",
            "confession in the rain",
            "drift",
            "silence",
        )
        romance_title_kw = (
            "dawn",
            "sunrise",
            "starlight",
            "promise",
            "vow",
            "hand in hand",
            "hearth",
            "home",
            "warmth",
            "embrace",
            "together",
            "oath",
            "rooftop",
            "moonlight",
            "bloom",
            "reunion",
            "epilogue",
            "heart",
        )
        daily_title_kw = (
            "morning",
            "tea",
            "snack",
            "market",
            "walk",
            "stroll",
            "coupon",
            "prank",
            "cafe",
            "bakery",
            "shop",
            "breeze",
            "sunshine",
            "delivery",
            "invite",
            "parlor",
        )

        if any(k in title_low for k in mystic_title_kw) or any(
            k in sfx_blob for k in ("bell", "chime_spirit", "thunder", "heartbeat", "howl", "whisper", "ritual")
        ):
            return "vn_mystic_tension"

        if any(k in title_low for k in melancholy_title_kw) or "rain" in sfx_blob:
            return "vn_melancholy_memory"

        if any(k in title_low for k in romance_title_kw):
            return "vn_tender_romance"

        if any(k in title_low for k in daily_title_kw) and chapter_id in ("CH1", "CH2", ""):
            return "vn_daily_sweet"

        # Content & voice-emotion secondary cues
        mystic_hits = sum(
            1
            for k in ("ritual", "lantern", "spirit", "departed", "trial", "verdict", "omen", "curse", "threshold", "boundary")
            if k in node_blob
        )
        mel_hits = sum(
            1
            for k in ("rain", "grief", "lonely", "tears", "regret", "mourn", "abandoned", "solitude", "trembl")
            if k in node_blob
        )
        rom_hits = sum(
            1
            for k in ("hold your hand", "intertwine", "moonlight", "promise", "stay by", "warmth", "heartbeat", "forever")
            if k in node_blob
        )

        if chapter_id in ("CH4",):
            if mel_hits >= 3 and mystic_hits == 0:
                return "vn_melancholy_memory"
            return "vn_mystic_tension"

        if chapter_id in ("CH5", "EPILOGUE"):
            if mystic_hits >= 2 and rom_hits == 0:
                return "vn_mystic_tension"
            if mel_hits >= 3 and rom_hits == 0:
                return "vn_melancholy_memory"
            return "vn_tender_romance"

        if chapter_id == "CH3":
            if mystic_hits >= 2:
                return "vn_mystic_tension"
            if rom_hits >= 2 and mel_hits == 0:
                return "vn_tender_romance"
            return "vn_melancholy_memory"

        # CH1 / CH2 default with gentle overrides if overtly mystic or melancholic
        if mystic_hits >= 3:
            return "vn_mystic_tension"
        if mel_hits >= 3:
            return "vn_melancholy_memory"
        if ve_counts.get("vn_tender_love", 0) >= 2 and rom_hits >= 2:
            return "vn_tender_romance"
        return "vn_daily_sweet"

    # ------------------------------------------------------------------
    # Mode 2: 4-Scene Branching Scenario Mode (`eagle_dating_sim.py`)
    # ------------------------------------------------------------------
    vn = vn_session or {}
    eff_stage = int(vn.get("stage") or stage or 1)
    eff_scene = int(vn.get("scene_num") or scene_idx or 1)
    is_finished = bool(vn.get("finished", False))
    is_passed = bool(vn.get("passed", True)) if is_finished else True
    cnode = vn.get("current_node") or {}

    sc_override = str(cnode.get("bgm_bucket") or vn.get("bgm_bucket") or "").strip().lower()
    if sc_override in BGM_MOOD_BUCKETS:
        return sc_override

    if is_finished:
        return "vn_tender_romance" if is_passed else "vn_melancholy_memory"

    if eff_scene >= 4:
        return "vn_tender_romance"

    eff_mood = str(mood or cnode.get("mood") or "").strip().lower()
    title_blob = f"{vn.get('title', '')} {vn.get('subtitle', '')} {vn.get('location', '')}".lower()
    node_text = f"{cnode.get('action_cue', '')} {cnode.get('inner_thought', '')} {cnode.get('speaker_line', '')}".lower()

    if any(k in eff_mood for k in ("melanchol", "sad", "vulnerab", "lonely", "tear", "wistful", "sorrow", "hurt")):
        return "vn_melancholy_memory"
    if any(k in eff_mood for k in ("mystic", "solemn", "eerie", "mysterious", "ritual", "serious")):
        return "vn_mystic_tension"
    if any(k in title_blob for k in ("rainy", "midnight rain", "confession in the rain", "past scar")):
        return "vn_melancholy_memory"
    if any(k in title_blob for k in ("wuwang", "ghost", "spirit", "ritual", "opera trial", "divination", "prophecy")):
        return "vn_mystic_tension"

    if eff_stage >= 4 and (
        eff_scene >= 3
        or any(k in eff_mood for k in ("tender", "romant", "intimat", "affection", "devot", "lov", "blush"))
        or any(k in node_text for k in ("moonlight", "hold hands", "embrace", "kiss", "heartbeat", "forever"))
    ):
        return "vn_tender_romance"

    if eff_scene == 3 and any(k in eff_mood for k in ("tender", "romant", "intimat", "devot", "soulmate")):
        return "vn_tender_romance"

    return "vn_daily_sweet"


class WaifuLinkBGMEngine:
    """
    Thread-safe Genshin Impact HOYO-MiX BGM Engine for WaifuLink (`alias wl_bgm`).
    """

    MCI_ALIAS = "wl_bgm"

    def __init__(
        self,
        catalog_path: Optional[Path] = None,
        cache_dir: Optional[Path] = None,
        settings_path: Optional[Path] = None,
        voice_playing_checker: Optional[Callable[[], bool]] = None,
        pause_checker: Optional[Callable[[], bool]] = None,
        enable_gta_process_mute: bool = True,
        gta_target_exe_names: Optional[tuple[str, ...]] = None,
        gta_target_pids: Optional[set[int]] = None,
    ) -> None:
        repo_root = Path(__file__).resolve().parent.parent.parent
        default_dating_dir = repo_root / "data" / "project-eagle" / "dating-sim"

        self.repo_root = repo_root
        self.catalog_path = Path(catalog_path) if catalog_path else (default_dating_dir / "bgm_catalog.json")
        self.cache_dir = Path(cache_dir) if cache_dir else (default_dating_dir / "bgm_cache")
        self.settings_path = Path(settings_path) if settings_path else (default_dating_dir / "bgm_settings.json")
        self.gta_guard_path = self.settings_path.parent / "gta_audio_guard.json"

        self._voice_playing_checker = voice_playing_checker
        self._pause_checker = pause_checker
        self._lock = threading.RLock()

        # Persisted user preferences
        self.muted: bool = False
        self.master_volume_pct: int = 100  # 0..100 (scales normalized ~220/1000 bed & 85/1000 ducked)
        self.mute_gta_sfx_in_vn: bool = True  # Auto-mute gta_pe.exe street/ped noise during Scenario & Story Quest
        self.mute_gta_in_modes: list[str] = list(DEFAULT_GTA_MUTE_MODES)
        self._load_settings()

        self._gta_muter = GTAPerProcessAudioMuter(
            guard_path=self.gta_guard_path,
            enabled=bool(enable_gta_process_mute),
            target_exe_names=gta_target_exe_names,
            target_pids=gta_target_pids,
        )

        # Mixing constants (loaded from catalog defaults if present)
        self.bed_mci_default: int = 220
        self.ducked_mci_default: int = 85
        self.duck_attack_ms: int = 150
        self.duck_release_hold_ms: int = 300
        self.duck_release_ramp_ms: int = 260
        self.crossfade_out_ms: int = 350
        self.crossfade_in_ms: int = 350
        self.eof_guard_ms: int = 250

        # Catalog state
        self.tracks_by_id: dict[str, dict[str, Any]] = {}
        self.buckets: dict[str, list[str]] = {b: [] for b in BGM_MOOD_BUCKETS}
        self.char_hub_signatures: dict[str, list[str]] = {c: [] for c in SUPPORTED_CHARS}
        self._shuffle_bags: dict[str, list[str]] = {b: [] for b in BGM_MOOD_BUCKETS}
        self.reload_catalog()

        # Desired high-level context (written by main/HTTP threads, consumed by worker thread)
        self._ctx_active: bool = False
        self._ctx_mode: str = ""
        self._ctx_char_id: str = ""
        self._ctx_bucket: str = "hub_cozy"

        # Instant voice notification state (optional fast-path alongside polling)
        self._notified_voice_playing: Optional[bool] = None
        self._last_voice_active_ts: float = 0.0

        # Live worker/MCI telemetry state
        self._playing: bool = False
        self._paused_by_menu: bool = False
        self._ducked: bool = False
        self._mci_ok: bool = True
        self._play_count: int = 0
        self._current_track_id: str = ""
        self._current_track_title: str = ""
        self._current_ascii_title: str = ""
        self._current_region: str = ""
        self._current_origin: str = ""
        self._current_bucket: str = ""
        self._current_char_context: str = ""
        self._current_base_vol: int = 220
        self._current_applied_vol: int = 0
        self._current_length_ms: int = 0
        self._current_pos_ms: int = 0
        self._last_played_track_id: str = ""
        self._last_error: str = ""

        # Dedicated Win32 MCI worker thread (`alias wl_bgm`)
        self._cmd_queue: queue.Queue[tuple[str, dict[str, Any]]] = queue.Queue()
        self._closed: bool = False
        self._winmm = ctypes.windll.winmm if os.name == "nt" else None
        self._worker_thread = threading.Thread(
            target=self._mci_worker_loop,
            name="WaifuLinkBGMWorker",
            daemon=True,
        )
        self._worker_thread.start()

    # ------------------------------------------------------------------
    # Settings & Catalog Management
    # ------------------------------------------------------------------
    def _load_settings(self) -> None:
        if not self.settings_path.exists():
            self._save_settings()
            return
        try:
            raw = json.loads(self.settings_path.read_text(encoding="utf-8-sig"))
            if "muted" in raw:
                self.muted = bool(raw["muted"])
            if "master_volume_pct" in raw:
                self.master_volume_pct = max(0, min(100, int(raw["master_volume_pct"])))
            if "mute_gta_sfx_in_vn" in raw:
                self.mute_gta_sfx_in_vn = bool(raw["mute_gta_sfx_in_vn"])
            if isinstance(raw.get("mute_gta_in_modes"), list) and raw["mute_gta_in_modes"]:
                self.mute_gta_in_modes = [
                    str(m).strip().lower() for m in raw["mute_gta_in_modes"] if str(m).strip()
                ]
            if "mute_gta_sfx_in_vn" not in raw or "mute_gta_in_modes" not in raw:
                self._save_settings()
        except Exception:
            pass

    def _save_settings(self) -> None:
        try:
            self.settings_path.parent.mkdir(parents=True, exist_ok=True)
            payload = {
                "muted": bool(self.muted),
                "master_volume_pct": int(self.master_volume_pct),
                "mute_gta_sfx_in_vn": bool(self.mute_gta_sfx_in_vn),
                "mute_gta_in_modes": list(self.mute_gta_in_modes),
                "updated_at": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(),
            }
            self.settings_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        except Exception:
            pass

    def reload_catalog(self) -> dict[str, int]:
        if not self.catalog_path.exists():
            return {}
        try:
            raw = json.loads(self.catalog_path.read_text(encoding="utf-8-sig"))
            defs = raw.get("defaults") or {}
            self.bed_mci_default = int(defs.get("bed_mci_volume", 220))
            self.ducked_mci_default = int(defs.get("ducked_mci_volume", 85))
            self.duck_attack_ms = int(defs.get("duck_attack_ms", 150))
            self.duck_release_hold_ms = int(defs.get("duck_release_hold_ms", 300))
            self.duck_release_ramp_ms = int(defs.get("duck_release_ramp_ms", 260))
            self.crossfade_out_ms = int(defs.get("crossfade_out_ms", 350))
            self.crossfade_in_ms = int(defs.get("crossfade_in_ms", 350))
            self.eof_guard_ms = int(defs.get("eof_guard_ms", 250))

            new_tracks: dict[str, dict[str, Any]] = {}
            new_buckets: dict[str, list[str]] = {b: [] for b in BGM_MOOD_BUCKETS}
            new_sigs: dict[str, list[str]] = {c: [] for c in SUPPORTED_CHARS}

            for item in raw.get("tracks") or []:
                tid = str(item.get("id") or "").strip()
                bkt = str(item.get("mood_bucket") or "hub_cozy").strip()
                if not tid:
                    continue
                if bkt not in new_buckets:
                    new_buckets[bkt] = []
                new_tracks[tid] = dict(item)
                new_buckets[bkt].append(tid)
                if bkt == "hub_cozy":
                    for ch in item.get("signature_chars") or []:
                        ch_l = str(ch).strip().lower()
                        if ch_l in new_sigs and tid not in new_sigs[ch_l]:
                            new_sigs[ch_l].append(tid)

            raw_sigs = raw.get("character_hub_signatures") or {}
            for ch_l, t_list in raw_sigs.items():
                if ch_l in new_sigs:
                    for tid in t_list or []:
                        if tid in new_tracks and tid not in new_sigs[ch_l]:
                            new_sigs[ch_l].append(tid)

            with self._lock:
                self.tracks_by_id = new_tracks
                self.buckets = new_buckets
                self.char_hub_signatures = new_sigs
                self._shuffle_bags = {b: [] for b in new_buckets}
            return {b: len(v) for b, v in new_buckets.items()}
        except Exception as exc:
            with self._lock:
                self._last_error = f"catalog_load_error: {exc}"
            return {}

    # ------------------------------------------------------------------
    # Pause Menu & Voice Ducking Hooks
    # ------------------------------------------------------------------
    @staticmethod
    def read_pause_flag_from_bridge(bridge: Any) -> bool:
        """Read GTA SA 1.0 US `0x00BA67A4` (`CMenuManager::m_bMenuActive`) safely."""
        if bridge is None:
            return False
        try:
            if hasattr(bridge, "try_attach"):
                if not bridge.try_attach():
                    return False
            elif hasattr(bridge, "attached") and not getattr(bridge, "attached", False):
                return False
            val = bridge.read_u8(GTA_PAUSE_MENU_ADDR)
            return bool(val is not None and int(val) != 0)
        except Exception:
            return False

    def set_pause_checker(self, checker: Optional[Callable[[], bool]]) -> None:
        self._pause_checker = checker

    def set_voice_playing_checker(self, checker: Optional[Callable[[], bool]]) -> None:
        self._voice_playing_checker = checker

    def notify_voice_state(self, is_playing: bool) -> None:
        """Optional zero-latency callback hook invoked by `WaifuLinkVoiceEngine`."""
        with self._lock:
            self._notified_voice_playing = bool(is_playing)
            if is_playing:
                self._last_voice_active_ts = time.monotonic()
        self._cmd_queue.put(("wake", {}))

    def _is_voice_currently_active(self) -> bool:
        if self._voice_playing_checker is not None:
            try:
                return bool(self._voice_playing_checker())
            except Exception:
                pass
        with self._lock:
            return bool(self._notified_voice_playing)

    def _is_game_paused(self) -> bool:
        if self._pause_checker is None:
            return False
        try:
            return bool(self._pause_checker())
        except Exception:
            return False

    # ------------------------------------------------------------------
    # Public Control API (Ready for `WaifuLink Card Hub v2.0` & HTTP `/api/dating/bgm`)
    # ------------------------------------------------------------------
    def sync_context(
        self,
        active: bool,
        mode: str = "",
        char_id: str = "",
        mood_bucket: str = "",
    ) -> dict[str, Any]:
        """
        Synchronize BGM lifecycle with current UI/gameplay state.
        - `active=False` (Free Roam convertible driving or 3D open world): fades out & closes `wl_bgm`.
        - `active=True`: starts or smoothly crossfades `wl_bgm` when `mood_bucket` changes
          (or when switching heroine in `hub_cozy` so her regional Signature Track plays).
        """
        cid = str(char_id or "").strip().lower()
        m_str = str(mode or "").strip().lower()
        b_str = str(mood_bucket or "").strip().lower()
        if active and b_str not in BGM_MOOD_BUCKETS:
            b_str = infer_vn_bgm_bucket(mode=m_str or "hub", char_id=cid)

        changed = False
        with self._lock:
            if (
                bool(active) != self._ctx_active
                or m_str != self._ctx_mode
                or cid != self._ctx_char_id
                or (active and b_str != self._ctx_bucket)
            ):
                self._ctx_active = bool(active)
                self._ctx_mode = m_str
                self._ctx_char_id = cid
                if active:
                    self._ctx_bucket = b_str
                changed = True

        if changed:
            self._cmd_queue.put(("sync", {}))
        return self.get_bgm_telemetry()

    def next_track(self) -> dict[str, Any]:
        """Manually skip to another random track in the active mood bucket (`♪ Next` button)."""
        self._cmd_queue.put(("next_track", {}))
        return self.get_bgm_telemetry()

    def toggle_mute(self, muted: Optional[bool] = None) -> dict[str, Any]:
        """Toggle or explicitly set BGM mute state (`♪ Mute` button on Hub Header)."""
        with self._lock:
            self.muted = (not self.muted) if muted is None else bool(muted)
            self._save_settings()
        self._cmd_queue.put(("wake", {}))
        return self.get_bgm_telemetry()

    def set_master_volume(self, pct: int) -> dict[str, Any]:
        """Set user master BGM volume percentage (`0..100`)."""
        with self._lock:
            self.master_volume_pct = max(0, min(100, int(pct)))
            self._save_settings()
        self._cmd_queue.put(("wake", {}))
        return self.get_bgm_telemetry()

    def set_gta_sfx_mute_enabled(self, enabled: Optional[bool] = None) -> dict[str, Any]:
        """Toggle or explicitly set automatic `gta_pe.exe` WASAPI ambient mute during Scenario & Story Quest."""
        with self._lock:
            self.mute_gta_sfx_in_vn = (not self.mute_gta_sfx_in_vn) if enabled is None else bool(enabled)
            self._save_settings()
        self._cmd_queue.put(("wake", {}))
        return self.get_bgm_telemetry()

    def shutdown(self) -> None:
        self._closed = True
        self._cmd_queue.put(("shutdown", {}))
        self._gta_muter.force_restore()

    def get_bgm_telemetry(self) -> dict[str, Any]:
        """
        Return full BGM telemetry for `/api/state` and ASCII-clean strings for `WaifuLink Card Hub v2.0`.
        """
        with self._lock:
            playing = bool(self._playing and self._ctx_active)
            ascii_title = self._current_ascii_title or sanitize_hud_ascii(self._current_track_title, 48)
            if self.muted:
                hud_bar = f"BGM: MUTED ({ascii_title})" if ascii_title else "BGM: MUTED"
            elif playing and ascii_title:
                hud_bar = f"BGM: {ascii_title}"
            else:
                hud_bar = "BGM: OFF"
            return {
                "playing": playing,
                "muted": bool(self.muted),
                "track_id": self._current_track_id if playing else "",
                "track_title": self._current_track_title if playing else "",
                "ascii_title": ascii_title if playing else "",
                "ascii_now_playing": sanitize_hud_ascii(hud_bar, 62),
                "mood_bucket": self._current_bucket if playing else (self._ctx_bucket if self._ctx_active else ""),
                "volume": int(self._current_applied_vol) if playing else 0,
                "base_volume": int(self._current_base_vol) if playing else self.bed_mci_default,
                "master_volume_pct": int(self.master_volume_pct),
                "ducked": bool(self._ducked and playing),
                "paused_by_menu": bool(self._paused_by_menu and playing),
                "mci_ok": bool(self._mci_ok),
                "play_count": int(self._play_count),
                "active_context": bool(self._ctx_active),
                "mode": self._ctx_mode,
                "char_id": self._ctx_char_id,
                "region": self._current_region if playing else "",
                "origin": self._current_origin if playing else "",
                "position_ms": int(self._current_pos_ms) if playing else 0,
                "length_ms": int(self._current_length_ms) if playing else 0,
                "gta_sfx_muted": bool(self._gta_muter.is_currently_muted),
                "gta_muted_sessions": int(self._gta_muter.muted_session_count),
                "mute_gta_sfx_in_vn": bool(self.mute_gta_sfx_in_vn),
                "last_error": self._last_error,
            }

    # ------------------------------------------------------------------
    # Short-Path & ASCII Cache Resolution (`bgm_cache/trk_<id>.mp3`)
    # ------------------------------------------------------------------
    def resolve_mci_playable_path(self, track: dict[str, Any], probe_mci_fn: Optional[Callable[[str], bool]] = None) -> str:
        """
        Ensure a track path is 100% safe for Win32 `mciSendStringW`:
        1. If pre-built ASCII cache (`cache_abs_path` or `cache_rel_path` or `bgm_cache/trk_<id>.mp3`)
           already exists on disk, inspect `GetShortPathNameW(source_path)` first when `probe_mci_fn` is
           not needed or prefer clean cover-art-free cache if source is `.m4a` / Unicode / long path.
        2. If cache does not exist yet:
           - Try `GetShortPathNameW(source_path)` on `.mp3` files first (if ASCII, `<= 118` chars, and
             `probe_mci_fn` succeeds).
           - Otherwise auto-generate `data/project-eagle/dating-sim/bgm_cache/trk_<hash>.mp3` via
             `ffmpeg -vn` (stripping APIC cover art / converting `.m4a`) or ASCII copy without ever
             modifying `D:\\Music`.
        """
        tid = str(track.get("id") or "").strip()
        src_str = str(track.get("source_path") or "").strip()
        src_path = Path(src_str) if src_str else None

        # Candidate cache paths
        explicit_cache = track.get("cache_abs_path") or (
            str(self.repo_root / track["cache_rel_path"]) if track.get("cache_rel_path") else ""
        )
        if explicit_cache and Path(explicit_cache).is_file() and Path(explicit_cache).stat().st_size >= 8192:
            return str(Path(explicit_cache).resolve())

        safe_slug = tid if (tid and tid.isascii()) else ("trk_" + hashlib.sha1(src_str.encode("utf-8", "ignore")).hexdigest()[:8])
        if not safe_slug.startswith(("trk_", "sup_")):
            safe_slug = f"trk_{safe_slug}"
        auto_cache_file = self.cache_dir / f"{safe_slug}.mp3"
        if auto_cache_file.is_file() and auto_cache_file.stat().st_size >= 8192:
            return str(auto_cache_file.resolve())

        if src_path is None or not src_path.is_file():
            return explicit_cache or src_str

        # Step 1: Try Win32 8.3 Short Path (`GetShortPathNameW`) if already `.mp3`
        if src_path.suffix.lower() == ".mp3":
            short_p = get_win32_short_path(str(src_path))
            if short_p and short_p.isascii() and len(short_p) <= 118:
                if probe_mci_fn is None or probe_mci_fn(short_p):
                    return short_p

        # Step 2: Materialize clean ASCII cache `bgm_cache/trk_<id>.mp3` (read-only on source)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        ffmpeg_bin = next((c for c in FFMPEG_CANDIDATES if Path(c).is_file() or shutil.which(c)), None)
        if ffmpeg_bin:
            try:
                if src_path.suffix.lower() == ".mp3":
                    cmd = [
                        ffmpeg_bin,
                        "-y",
                        "-v",
                        "error",
                        "-nostdin",
                        "-i",
                        str(src_path),
                        "-map",
                        "0:a:0",
                        "-vn",
                        "-map_metadata",
                        "-1",
                        "-c:a",
                        "copy",
                        "-id3v2_version",
                        "0",
                        str(auto_cache_file),
                    ]
                else:
                    cmd = [
                        ffmpeg_bin,
                        "-y",
                        "-v",
                        "error",
                        "-nostdin",
                        "-i",
                        str(src_path),
                        "-vn",
                        "-map_metadata",
                        "-1",
                        "-ar",
                        "44100",
                        "-ac",
                        "2",
                        "-c:a",
                        "libmp3lame",
                        "-b:a",
                        "192k",
                        "-id3v2_version",
                        "0",
                        str(auto_cache_file),
                    ]
                subprocess.run(
                    cmd,
                    capture_output=True,
                    timeout=45,
                    creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
                )
                if auto_cache_file.is_file() and auto_cache_file.stat().st_size >= 8192:
                    return str(auto_cache_file.resolve())
            except Exception:
                pass

        # Step 3: Pure Python ASCII copy fallback if ffmpeg unavailable
        if src_path.suffix.lower() == ".mp3":
            try:
                shutil.copy2(str(src_path), str(auto_cache_file))
                if auto_cache_file.is_file():
                    return str(auto_cache_file.resolve())
            except Exception:
                pass

        return get_win32_short_path(str(src_path))

    # ------------------------------------------------------------------
    # Track Selection (Signature-Aware + Non-Repeating Shuffle)
    # ------------------------------------------------------------------
    def _pick_next_track(self, bucket: str, char_id: str, prefer_signature: bool = False) -> Optional[dict[str, Any]]:
        with self._lock:
            b_key = bucket if bucket in self.buckets and self.buckets[bucket] else "hub_cozy"
            pool = list(self.buckets.get(b_key) or [])
            if not pool:
                if not self.tracks_by_id:
                    return None
                first_id = next(iter(self.tracks_by_id))
                return dict(self.tracks_by_id[first_id])

            last_id = self._last_played_track_id or self._current_track_id

            # In `hub_cozy` (or on initial bucket entry when character has tagged tracks), prioritize heroine's signature tracks
            if prefer_signature and char_id:
                if b_key == "hub_cozy":
                    sig_ids = [tid for tid in (self.char_hub_signatures.get(char_id) or []) if tid in self.tracks_by_id]
                else:
                    sig_ids = [
                        tid
                        for tid in pool
                        if char_id in (self.tracks_by_id[tid].get("signature_chars") or [])
                    ]
                if sig_ids:
                    non_rep = [tid for tid in sig_ids if tid != last_id]
                    chosen_id = random.choice(non_rep if non_rep else sig_ids)
                    return dict(self.tracks_by_id[chosen_id])

            bag = self._shuffle_bags.get(b_key) or []
            bag = [tid for tid in bag if tid in self.tracks_by_id]
            if not bag:
                bag = list(pool)
                random.shuffle(bag)
                if len(bag) > 1 and bag[0] == last_id:
                    bag.append(bag.pop(0))

            chosen_id = bag.pop(0)
            if chosen_id == last_id and bag:
                alt_id = bag.pop(0)
                bag.append(chosen_id)
                chosen_id = alt_id
            self._shuffle_bags[b_key] = bag
            return dict(self.tracks_by_id[chosen_id])

    # ------------------------------------------------------------------
    # Dedicated Win32 `mciSendStringW` Worker Thread (`alias wl_bgm`)
    # ------------------------------------------------------------------
    def _mci_send(self, cmd: str) -> tuple[int, str]:
        if self._winmm is None:
            return (0, "")
        buf = ctypes.create_unicode_buffer(256)
        err = int(self._winmm.mciSendStringW(cmd, buf, 255, None))
        return (err, buf.value.strip())

    def _mci_set_vol(self, vol: int) -> None:
        clamped = max(0, min(1000, int(round(vol))))
        self._mci_send(f"setaudio {self.MCI_ALIAS} volume to {clamped}")
        with self._lock:
            self._current_applied_vol = clamped

    def _mci_fade_to(self, target_vol: int, duration_ms: int, abort_on_new_cmd: bool = False) -> None:
        if self._winmm is None:
            return
        with self._lock:
            start_vol = int(self._current_applied_vol)
            is_open = bool(self._playing)
        if not is_open:
            return
        target_vol = max(0, min(1000, int(target_vol)))
        if duration_ms <= 20 or abs(target_vol - start_vol) <= 6:
            self._mci_set_vol(target_vol)
            return
        steps = max(3, min(12, duration_ms // 28))
        sleep_s = (duration_ms / 1000.0) / float(steps)
        for i in range(1, steps + 1):
            if self._closed or (abort_on_new_cmd and not self._cmd_queue.empty()):
                self._mci_set_vol(target_vol)
                return
            v = int(round(start_vol + (target_vol - start_vol) * (i / float(steps))))
            self._mci_set_vol(v)
            time.sleep(sleep_s)

    def _mci_close(self, fade_ms: int = 0) -> None:
        with self._lock:
            was_playing = self._playing
        if was_playing and fade_ms > 0 and not self._paused_by_menu:
            self._mci_fade_to(0, fade_ms, abort_on_new_cmd=True)
        self._mci_send(f"stop {self.MCI_ALIAS}")
        self._mci_send(f"close {self.MCI_ALIAS}")
        with self._lock:
            self._playing = False
            self._paused_by_menu = False
            self._ducked = False
            self._current_applied_vol = 0
            self._current_pos_ms = 0
            self._current_length_ms = 0
            self._current_track_id = ""
            self._current_track_title = ""
            self._current_ascii_title = ""
            self._current_region = ""
            self._current_origin = ""
            self._current_bucket = ""

    def _compute_desired_steady_volume(self, duck_now: bool) -> int:
        with self._lock:
            if self.muted or self.master_volume_pct <= 0:
                return 0
            scale = self.master_volume_pct / 100.0
            raw = self.ducked_mci_default if duck_now else self._current_base_vol
            return max(0, min(1000, int(round(raw * scale))))

    def _mci_open_and_start_track(
        self,
        track: dict[str, Any],
        bucket: str,
        char_id: str,
        fade_in_ms: int = 350,
    ) -> bool:
        self._mci_close(fade_ms=0)
        play_path = self.resolve_mci_playable_path(track)
        if not play_path or not Path(play_path).is_file():
            with self._lock:
                self._mci_ok = False
                self._last_error = f"missing_file:{play_path}"
            return False

        if self._winmm is None:
            return False

        err_open, _ = self._mci_send(f'open "{play_path}" type mpegvideo alias {self.MCI_ALIAS}')
        if err_open != 0:
            short_p = get_win32_short_path(play_path)
            if short_p != play_path:
                err_open, _ = self._mci_send(f'open "{short_p}" type mpegvideo alias {self.MCI_ALIAS}')
        if err_open != 0:
            with self._lock:
                self._mci_ok = False
                self._last_error = f"mci_open_err_{err_open}:{Path(play_path).name}"
            return False

        self._mci_send(f"set {self.MCI_ALIAS} time format milliseconds")
        err_len, len_s = self._mci_send(f"status {self.MCI_ALIAS} length")
        length_ms = int(len_s) if (err_len == 0 and len_s.isdigit()) else int(float(track.get("duration_sec", 90.0)) * 1000)

        base_vol = int(track.get("base_mci_volume") or self.bed_mci_default)
        voice_now = self._is_voice_currently_active()
        if voice_now:
            self._last_voice_active_ts = time.monotonic()

        with self._lock:
            self._current_base_vol = base_vol
            self._ducked = voice_now

        target_vol = self._compute_desired_steady_volume(duck_now=voice_now)
        init_vol = min(target_vol, 24) if (fade_in_ms > 0 and target_vol > 0) else target_vol
        self._mci_set_vol(init_vol)

        err_play, _ = self._mci_send(f"play {self.MCI_ALIAS} from 0")
        if err_play != 0:
            self._mci_send(f"close {self.MCI_ALIAS}")
            with self._lock:
                self._mci_ok = False
                self._last_error = f"mci_play_err_{err_play}:{Path(play_path).name}"
            return False

        with self._lock:
            self._playing = True
            self._mci_ok = True
            self._paused_by_menu = False
            self._play_count += 1
            self._current_track_id = str(track.get("id") or "")
            self._last_played_track_id = self._current_track_id
            self._current_track_title = str(track.get("title") or "")
            self._current_ascii_title = sanitize_hud_ascii(track.get("ascii_title") or track.get("title") or "", 48)
            self._current_region = str(track.get("region") or "")
            self._current_origin = str(track.get("origin") or "")
            self._current_bucket = bucket
            self._current_char_context = char_id
            self._current_length_ms = length_ms
            self._current_pos_ms = 0
            self._last_error = ""

        # If GTA SA Pause Menu is currently open at the exact instant of opening, pause immediately;
        # otherwise the non-blocking 30ms worker tick loop smoothly fades volume up over `crossfade_in_ms`!
        if self._is_game_paused():
            self._mci_send(f"pause {self.MCI_ALIAS}")
            with self._lock:
                self._paused_by_menu = True

        return True

    def _compute_want_gta_mute(self) -> bool:
        with self._lock:
            return bool(
                self.mute_gta_sfx_in_vn
                and self._ctx_active
                and (self._ctx_mode in self.mute_gta_in_modes)
            )

    def _mci_worker_loop(self) -> None:
        last_status_poll_ts = 0.0
        last_tick_ts = time.monotonic()

        while not self._closed:
            with self._lock:
                is_active = self._ctx_active or self._playing
            wait_s = 0.030 if is_active else (0.250 if self._gta_muter.needs_poll() else 0.100)

            try:
                cmd, _payload = self._cmd_queue.get(timeout=wait_s)
            except queue.Empty:
                cmd = "tick"

            if cmd == "shutdown":
                self._gta_muter.force_restore()
                self._mci_close(fade_ms=0)
                break

            # Drain bursts of wake/sync commands while preserving explicit `next_track` or `shutdown`
            force_next = cmd == "next_track"
            while True:
                try:
                    nxt_cmd, _ = self._cmd_queue.get_nowait()
                    if nxt_cmd == "shutdown":
                        self._gta_muter.force_restore()
                        self._mci_close(fade_ms=0)
                        return
                    if nxt_cmd == "next_track":
                        force_next = True
                except queue.Empty:
                    break

            now = time.monotonic()
            dt_ms = max(1.0, min(150.0, (now - last_tick_ts) * 1000.0))
            last_tick_ts = now

            try:
                # 0. Synchronize per-process WASAPI mute on `gta_pe.exe` immediately (`t = 0ms` before any fade)
                self._gta_muter.sync(self._compute_want_gta_mute(), now=now)

                with self._lock:
                    want_active = self._ctx_active
                    want_bucket = self._ctx_bucket
                    want_char = self._ctx_char_id
                    cur_playing = self._playing
                    cur_bucket = self._current_bucket
                    cur_char = self._current_char_context

                # 1. Context deactivated (Free Roam convertible driving or 3D gameplay) -> fade out & close completely
                if not want_active:
                    if cur_playing:
                        self._mci_close(fade_ms=280)
                    continue

                # 2. Context active: check if we need initial open, mood crossfade, character hub switch, or manual skip
                char_hub_switched = (
                    cur_playing
                    and want_bucket == "hub_cozy"
                    and cur_bucket == "hub_cozy"
                    and bool(want_char)
                    and want_char != cur_char
                )
                need_switch = (not cur_playing) or (want_bucket != cur_bucket) or char_hub_switched or force_next

                if need_switch:
                    if cur_playing:
                        self._mci_close(fade_ms=self.crossfade_out_ms)
                    # Re-read latest target context & re-sync GTA mute in case user exited during fade-out
                    self._gta_muter.sync(self._compute_want_gta_mute(), now=time.monotonic())
                    with self._lock:
                        want_active = self._ctx_active
                        want_bucket = self._ctx_bucket
                        want_char = self._ctx_char_id
                    if not want_active:
                        continue
                    prefer_sig = (not force_next) and (want_bucket == "hub_cozy" or not cur_playing or want_bucket != cur_bucket)
                    nxt_trk = self._pick_next_track(want_bucket, want_char, prefer_signature=prefer_sig)
                    if nxt_trk is not None:
                        self._mci_open_and_start_track(
                            nxt_trk,
                            bucket=want_bucket,
                            char_id=want_char,
                            fade_in_ms=self.crossfade_in_ms,
                        )
                    last_tick_ts = time.monotonic()
                    continue

                # 3. GTA SA Pause Menu (`0x00BA67A4`) auto pause / resume
                game_paused = self._is_game_paused()
                with self._lock:
                    was_paused = self._paused_by_menu
                if game_paused and not was_paused:
                    self._mci_send(f"pause {self.MCI_ALIAS}")
                    with self._lock:
                        self._paused_by_menu = True
                    continue
                elif (not game_paused) and was_paused:
                    self._mci_send(f"resume {self.MCI_ALIAS}")
                    with self._lock:
                        self._paused_by_menu = False

                if game_paused:
                    continue

                # 4. Smooth Auto-Ducking ramp (`150ms` down to `85/1000`, `300ms` post-voice hold, `260ms` restore)
                voice_now = self._is_voice_currently_active()
                if voice_now:
                    self._last_voice_active_ts = now
                    should_duck = True
                else:
                    should_duck = (now - self._last_voice_active_ts) * 1000.0 < float(self.duck_release_hold_ms)

                desired_vol = self._compute_desired_steady_volume(duck_now=should_duck)
                with self._lock:
                    cur_vol = self._current_applied_vol
                    self._ducked = bool(should_duck and not self.muted)

                if cur_vol != desired_vol:
                    if desired_vol < cur_vol:
                        ramp_ms = max(40.0, float(self.duck_attack_ms))
                        max_step = max(8, int(round(abs(cur_vol - desired_vol) * (dt_ms / ramp_ms) + 12)))
                        new_vol = max(desired_vol, cur_vol - max_step)
                    else:
                        ramp_ms = max(60.0, float(self.duck_release_ramp_ms))
                        max_step = max(6, int(round(abs(desired_vol - cur_vol) * (dt_ms / ramp_ms) + 8)))
                        new_vol = min(desired_vol, cur_vol + max_step)
                    self._mci_set_vol(new_vol)

                # 5. EOF Auto-Next check (`position >= length - 250` or `mode == stopped`) every ~200ms
                if (now - last_status_poll_ts) >= 0.20:
                    last_status_poll_ts = now
                    err_m, mode_str = self._mci_send(f"status {self.MCI_ALIAS} mode")
                    err_p, pos_str = self._mci_send(f"status {self.MCI_ALIAS} position")
                    pos_ms = int(pos_str) if (err_p == 0 and pos_str.isdigit()) else 0
                    with self._lock:
                        self._current_pos_ms = pos_ms
                        len_ms = self._current_length_ms

                    eof_reached = False
                    if err_m == 0 and mode_str.lower() in ("stopped", "not ready"):
                        eof_reached = True
                    elif len_ms > 1000 and pos_ms >= max(500, len_ms - self.eof_guard_ms):
                        eof_reached = True

                    if eof_reached:
                        self._mci_close(fade_ms=120)
                        nxt_trk = self._pick_next_track(want_bucket, want_char, prefer_signature=False)
                        if nxt_trk is not None:
                            self._mci_open_and_start_track(
                                nxt_trk,
                                bucket=want_bucket,
                                char_id=want_char,
                                fade_in_ms=self.crossfade_in_ms,
                            )
            except Exception as exc:
                with self._lock:
                    self._last_error = f"worker_err:{exc}"


def verify_catalog_mci_open_all(
    catalog_path: Optional[Path] = None,
    play_sample_ms: int = 0,
    muted: bool = True,
) -> dict[str, Any]:
    """
    Automated offline verification opening 100% (`N/N`) tracks in `bgm_catalog.json`
    via real Win32 `mciSendStringW` (`type mpegvideo`), verifying `err == 0` and
    `status <alias> length > 0` for every single track.
    """
    repo_root = Path(__file__).resolve().parent.parent.parent
    cat_p = Path(catalog_path) if catalog_path else (repo_root / "data" / "project-eagle" / "dating-sim" / "bgm_catalog.json")
    raw = json.loads(cat_p.read_text(encoding="utf-8-sig"))
    tracks = raw.get("tracks") or []

    # Temporary non-playing helper instance only for `resolve_mci_playable_path`
    helper = WaifuLinkBGMEngine(catalog_path=cat_p, enable_gta_process_mute=False)
    helper.shutdown()

    winmm = ctypes.windll.winmm
    buf = ctypes.create_unicode_buffer(256)
    alias = f"wl_bgm_chk_{os.getpid()}"

    def _call(c: str) -> tuple[int, str]:
        rc = int(winmm.mciSendStringW(c, buf, 255, None))
        return rc, buf.value.strip()

    passed = 0
    failures: list[dict[str, Any]] = []
    details: list[dict[str, Any]] = []

    for idx, trk in enumerate(tracks, 1):
        resolved = helper.resolve_mci_playable_path(trk)
        _call(f"close {alias}")
        rc_open, _ = _call(f'open "{resolved}" type mpegvideo alias {alias}')
        if rc_open != 0:
            failures.append({"id": trk.get("id"), "title": trk.get("title"), "path": resolved, "err": rc_open})
            continue
        _call(f"set {alias} time format milliseconds")
        rc_len, len_s = _call(f"status {alias} length")
        length_ms = int(len_s) if (rc_len == 0 and len_s.isdigit()) else 0
        rc_vol, _ = _call(f"setaudio {alias} volume to {0 if muted else 180}")
        rc_play = 0
        if play_sample_ms > 0:
            rc_play, _ = _call(f"play {alias} from 0")
            time.sleep(play_sample_ms / 1000.0)
            _call(f"stop {alias}")
        _call(f"close {alias}")

        ok = (rc_open == 0) and (rc_len == 0) and (length_ms > 0) and (rc_vol == 0) and (rc_play == 0)
        if ok:
            passed += 1
            details.append(
                {
                    "idx": idx,
                    "id": trk.get("id"),
                    "title": trk.get("title"),
                    "mood_bucket": trk.get("mood_bucket"),
                    "mci_length_ms": length_ms,
                    "resolved_path": resolved,
                }
            )
        else:
            failures.append(
                {
                    "id": trk.get("id"),
                    "title": trk.get("title"),
                    "path": resolved,
                    "rc_open": rc_open,
                    "rc_len": rc_len,
                    "length_ms": length_ms,
                    "rc_vol": rc_vol,
                    "rc_play": rc_play,
                }
            )

    return {
        "ok": len(failures) == 0 and passed == len(tracks) and len(tracks) > 0,
        "total": len(tracks),
        "passed": passed,
        "failed": len(failures),
        "failures": failures,
        "details": details,
    }
