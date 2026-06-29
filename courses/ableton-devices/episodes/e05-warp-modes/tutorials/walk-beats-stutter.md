# Warp Recipe: walk-beats-stutter

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Walkthrough step 2 — Beats turns the held vowel into a stutter it never performed.
**What you should hear:** the sung "ah" in Beats: Preserve 1/16 (gridding a vowel that has no transients), Loop Forward, Envelope 100, half tempo — the smooth voice becomes a chopped, stuttering machine rhythm.
**Structure:** single. **Isolates:** Beats on a transient-less vowel with **wrong-grid Preserve 1/16** + Loop Forward.
**Source audio:** `src_vox-ah.wav` — the walkthrough source.

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_vox-ah.wav` onto an audio track | — | The dry "ah" |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Beats** | Transient-locked granular |
| 3 | Clip view | **Preserve** | **1/16** | **Wrong-grid on purpose** — grids a vowel that has no real transients |
| 4 | Clip view | **Transient Loop Mode** | **Loop Forward** | Each 1/16 segment will loop to fill time |
| 5 | Clip view | **Transient Envelope** | **100** | Hard, clicky segment edges |
| 6 | Transport | Stretch to **half tempo** — project tempo **50%** | 50% | A clear sixteenth-grid **stutter** from one long sustain |

**The abuse extreme here:** **Preserve = 1/16 on a transient-less vowel** is the manufactured-glitch move — you impose a rhythm grid the source never had. Loop Forward + Envelope 100 turn each grid cell into a hard-edged micro-loop.

## Verify
- **Audible:** a clear sixteenth-grid stutter/rhythm from a source that was one long sustain. Smooth stretch ⇒ Loop Forward / grid didn't take ⇒ reject.
- **Spectral:** periodic onset peaks at the imposed 1/16 grid (a rhythm the source never had) with hard segment edges. No periodic onsets ⇒ reject.

## Make it reusable (resample / freeze)
Resample/freeze→flatten to `walk-beats-stutter.wav`.
