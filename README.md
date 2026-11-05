# eagle-waifulink

> **Project Eagle** | WaifuLink Dating Sim System | v4.0

Complete dating simulation system for Project Eagle — 6 Genshin Impact heroines with Visual Novel scenarios, JP voice, and Genshin BGM.

## Repository Contents

```
eagle_dating_sim.py           ← Core dating sim engine
eagle_waifulink_bgm.py        ← Genshin BGM engine (48 tracks, 5 moods)
eagle_waifulink_voice.py      ← JP voice playback engine
eagle_waifulink_v4_pilot.py   ← WaifuLink v4 pilot/registry
eagle_waifulink_v4_hutao.py   ← Hu Tao character pack
eagle_waifulink_v4_furina.py  ← Furina character pack
eagle_waifulink_v4_citlali.py ← Citlali character pack
eagle_waifulink_v4_columbina.py ← Columbina character pack
eagle_waifulink_v4_kirara.py  ← Kirara character pack
eagle_waifulink_v4_vesna.py   ← Vesna Strivozha character pack
README-waifulink-bgm.md       ← BGM engine documentation
```

## 6 Heroines

| # | Character | Ped ID | Home | CV (JP) | CG | Status |
|---|-----------|--------|------|---------|-----|--------|
| 1 | Hu Tao | 49428 | Idlewood LS | Rie Takahashi | 135/135 | ✅ |
| 2 | Furina | 49429 | Richman Hills LS | Inori Minase | 135/135 | ✅ |
| 3 | Citlali | 49430 | Verona Beach LS | Asami Tano | 135/135 | ✅ |
| 4 | Columbina | 49431 | Prickle Pine LV | Lynn | 135/135 | ✅ |
| 5 | Kirara | 49432 | Marina Canal LS | Sayumi Suzushiro | 135/135 | ✅ |
| 6 | Vesna Strivozha | 49433 | Palisades Bayfront Villa, SF | Aya Endo | 135/135 | ✅ |

**Total: 810 CGs** | 90 Milestones | 180 VN Scenarios

## BGM Engine v1.1

48 HOYO-MiX / Yu-Peng Chen tracks across 5 mood tiers:

| Mood | Tracks | Trigger |
|------|--------|---------|
| `hub_cozy` | 14 | Hub screen (6 signature tracks per heroine) |
| `vn_daily_sweet` | 9 | Daily VN scenarios |
| `vn_tender_romance` | 9 | Romance scenarios |
| `vn_melancholy_memory` | 8 | Sad / memory scenarios |
| `vn_mystic_tension` | 8 | Tense / mystery scenarios |

**v1.1**: WASAPI GTA Muter — auto-mutes `gta_pe.exe` during VN/Story Quest mode.

## JP Voice Engine v1.0

- 24 `.wav` files per character — 8 emotion buckets
- Triggers: Ambient Map Encounter, Free-Roam Outing, VN scenarios, Milestone Photo Drop
- Engine: `winmm.dll` MCI stream

## CG Specification

- Resolution: 1376×768 (16:9) JPEG
- SHA-256 unique per file, no duplicates or placeholders
- Path: `data/project-eagle/dating-sim/media/{char_id}/`

## Jira
- [SCRUM-141](https://nguyennguyenle997.atlassian.net/browse/SCRUM-141) — WaifuLink v4.0 System
- [SCRUM-155-159](https://nguyennguyenle997.atlassian.net/browse/SCRUM-155) — Individual QA passes
- [SCRUM-160](https://nguyennguyenle997.atlassian.net/browse/SCRUM-160) — JP Voice Engine
- [SCRUM-173](https://nguyennguyenle997.atlassian.net/browse/SCRUM-173) — BGM Engine v1.1
