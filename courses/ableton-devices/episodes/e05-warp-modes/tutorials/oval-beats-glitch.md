# Warp Recipe: oval-beats-glitch

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).
> Section-6 rebuild (06a): Oval's skipping CD, automated. Lives in `song_clips` because the source is a song-adjacent loop, but it is a warp recipe.

**Concept:** Beats with deliberately wrong-grid Preserve + Loop Forward → hard-edged stutters/skips you didn't play — Markus Popp's damaged-CD glitch, in the box.
**What you should hear:** a melodic loop whose transients DON'T land on 1/16 forced onto a 1/16 grid at ~70% tempo → manufactured skips and stutters.
**Structure:** rebuild (single). **Isolates:** Beats **Preserve = 1/16** fighting the real transients.
**Source audio:** `src_melodic-loop.wav` — a loop whose transients are **off** the 1/16 grid (essential — that's where the glitch comes from).

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_melodic-loop.wav` onto an audio track | — | The melodic loop at native tempo |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Beats** | Transient-locked granular |
| 3 | Clip view | **Preserve** | **1/16** | **Wrong-grid on purpose** — cuts mid-transient, not on the hits |
| 4 | Clip view | **Transient Loop Mode** | **Loop Forward** | Each 1/16 cell loops → stutter |
| 5 | Clip view | **Transient Envelope** | **100** | Hard, clicky edges |
| 6 | Transport | Stretch to **~70% tempo** (dossier Recipe 1) | 70% | Hard-edged stutters/skips the source never performed |

**The abuse extreme here:** the recipe **only works if the source transients are off the 1/16 grid** — that mismatch is what manufactures the glitch. A loop already quantized to 1/16 will just slow down cleanly. Pick or build an off-grid loop.

## Verify
- **Audible:** hard-edged stutter/skip artifacts not present in the source — Oval's CD-skip, automated. A clean slow-down ⇒ the source was on-grid or Loop Forward didn't engage ⇒ reject.
- **Spectral:** periodic 1/16 onset peaks (an imposed grid) with hard segment edges, mismatched to the source's real onset positions.

## Make it reusable (resample / freeze)
Resample/freeze→flatten to `oval-beats-glitch.wav`. This is the 06a rebuild that A/Bs against the real `systemisch-clip`.
