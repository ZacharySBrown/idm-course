# Warp Recipe: beats-stutter-freeze

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Beats **Loop Forward** + Transient Envelope 100 at half tempo → each slice freezes into a hard-edged loop (the Ableton stutter-freeze).
**What you should hear:** a drum/melodic loop dropped to half tempo in Beats: instead of smoothly stretching, every segment freezes into a tiny held loop with sharp, clicky seams — a stutter-glitch.
**Structure:** single. **Isolates:** Beats **Transient Loop Mode = Loop Forward** (with Envelope 100), at half tempo.
**Source audio:** `src_drumbreak.wav` — a clean break loop.

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_drumbreak.wav` onto an audio track | — | The break at native tempo |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Beats** | Transient-locked granular |
| 3 | Clip view | **Preserve** | **Transients** | Slice boundaries on the real hits |
| 4 | Clip view | **Transient Loop Mode** | **Loop Forward** | The stutter-freeze lever — each slice will loop to fill time |
| 5 | Clip view | **Transient Envelope** | **100** | Hard, clicky segment edges |
| 6 | Transport | Stretch to **half tempo** — project tempo **50%** | 50% | Each slice **freezes into a tiny held loop** with hard seams — a stutter |

**The abuse extreme here:** **Loop Forward + Envelope 100** at half tempo is the canonical Ableton "robot/granular freeze." At slow tempos Loop Forward turns each transient-to-transient slice into a sustained micro-loop instead of a smooth stretch.

## Verify
- **Audible:** clearly rhythmic stutter/freeze — repeated tiny loops with hard seams — not a smooth slow-down. A smooth stretch ⇒ Loop Forward didn't engage ⇒ reject.
- **Spectral:** strong periodic onset/segment-repeat peaks (a stutter rate) and sharp segment-edge transients (Envelope 100). Smooth, low-onset envelope ⇒ reject.

## Make it reusable (resample / freeze)
1. Render at half tempo with the loop/envelope settings.
2. Resample/freeze→flatten to `beats-stutter-freeze.wav` — the stutter is now a plain audio clip you can re-pitch and chop.
