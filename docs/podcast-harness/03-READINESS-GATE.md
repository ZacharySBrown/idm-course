# Readiness Gate — the harness's receipt-emitting, build-blocking consistency check

**Why this exists.** The 9 agent self-reports converged on one weakness: the quality
gates *ran* but emitted no **receipts**, and consistency was enforced only on the
**narrative** — not on background music, audio-editing style, the demo clips, or the
preset build books. "Passed" was *asserted, not evidenced*, and silent-skips let
episodes ship with missing content nobody saw. This layer fixes that.

## The gate: `shared/tools/episode_readiness.py`

One deterministic, re-runnable command that emits a structured receipt per episode
(`episodes/<ep>/gate-report.json` + `.md`) and returns a non-zero exit code on any hard
FAIL — so a build/CI can block on it, and you can **iterate** (fix → re-run → diff).

```
python3 shared/tools/episode_readiness.py --course-root courses/ableton-devices --all
python3 shared/tools/episode_readiness.py --course-root courses/ableton-devices --episode e02-analog
#   --strict   promotes warnings to failures
```

### The seven checks (consistency, not just narrative)

| Check | Enforces | Hard-fails when |
|---|---|---|
| `narration`    | every slide in `episode.yaml` is actually narrated | a slide has a script but **no narration WAV** (build would silently drop it) |
| `preset_books` | **EVERY described preset** (a demo with a `params:` block) has a build book | a `tutorials/<id>.md` is missing, or it isn't listed in `presets/SAVE_CHECKLIST.md` |
| `demo_clips`   | every `[cue:]` resolves; built demos are rendered | a cue points at no manifest id (warn: a demo with no clip + no `headless:false`) |
| `beds`         | background music is real, not placeholder | any bed/transition `clip_id` is `TBD` or has no rendered clip (warn: an act with no bed) |
| `audio_style`  | demo levels sit near the voice | a demo is **>12 dB** off the voice (warn: 6–12 dB). Runs `sound_design_qa` per-episode. |
| `loudness`     | delivered loudness is on-spec | integrated outside −16 ±1 LUFS, or true-peak **> −1 dBTP** (measured on the mp3) |
| `lexicon`      | house voice | any banned phrase / exclamation / emoji (single source of truth: `shared/style/lexicon.md`) |

Severity is split deliberately: **placeholders / missing content = hard FAIL**;
intentional-but-imperfect things (a demo-dense act with no bed, a slightly-hot demo)
= **warn** (surfaced, not blocking) unless `--strict`.

## Build-engine fixes that the gate's findings forced (`shared/tools/build_episode.py`)

1. **Beds no longer silent-skip.** `build_bed_track` returned `None` and `continue`d past
   any `TBD`/missing/mis-ranged bed — so an episode could build **bed-less with no signal**.
   It now returns a list of dropped-bed WARNINGS, printed at build time (`[bed] DROPPED — …`)
   and recorded in the build status. *This immediately exposed that e02's act-06 bed had
   never been placed* (its slide range pointed at un-narrated slides).
2. **True-peak honored.** The final `alimiter` defaulted to `level=true`, which
   **re-normalizes back toward 0 dB after limiting** — undoing the ceiling and pushing
   inter-sample peaks over target (this is what put e02 at −0.5 dBTP). Fixed with
   `level=disabled` and a `limit=0.75` (~−2.5 dBFS) ceiling that leaves headroom for the
   ~0.85 dB of overshoot MP3 lossy encoding adds, so the **delivered mp3 lands ≤ −1 dBTP**.

## Preset build books for ANY device (`courses/ableton-devices/tools/build_tutorials.py`)

Rewritten from Operator-only to **device-generic**: it orders each demo's params by their
**index in the device's dumped param map** (`device_render/param_maps/<device>.json`) —
the device's own natural order — and labels enum values from the map's `value_items`. So a
missing build book can be generated/refreshed for Operator, Analog, Wavetable, Meld, or any
future device, and `preset_books` coverage is **guaranteeable**, not hand-maintained.
`--only-missing` refreshes gaps without clobbering richer hand-written books.

## What the hardened harness CAUGHT and FIXED this pass

- **e02 shipped missing its last 4 slides** (the entire MS-20-abuse / loop-envelope / payoff /
  exercise tail of act 6 — scripts existed, narration was never rendered). The new
  `narration` check would have blocked it; rendered + rebuilt → **33 chapters / 51:15** (was 29 / 45:23).
- **e02 true-peak −0.5 dBTP** (over spec) → root-caused to `alimiter level=true` → fixed → **−1.15 dBTP**.
- **e02 act-06 bed had never placed** (mis-ranged, silently dropped) → now placed.
- **e01 poly-bell demos are −17 to −32 dB below the voice** (effectively inaudible) — a real,
  long-standing defect now **machine-blocking** (`audio_style` FAIL); fix needs a louder re-render.
- **e04 is correctly NOT ready** (TBD beds + unrendered narration) instead of falsely "locked."

## The iteration loop this enables
`build_episode` → `episode_readiness` (read the receipt) → fix the one red line →
re-run → diff the receipt. Consistency across **narrative, background music, audio-editing
style, demo clips, and preset books** is now a check you can run, not a hope.
