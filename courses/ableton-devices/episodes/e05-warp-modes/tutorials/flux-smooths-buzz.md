# Warp Recipe: flux-smooths-buzz

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Texture **Flux 0 → 100** → randomizing grain phase trades a periodic metallic buzz for a smooth cloud (the PaulStretch insight).
**What you should hear:** a held note in Texture: Flux at 0 gives the periodic seam-buzz; pushing Flux to 100 dissolves it into a smooth, stationary wash.
**Structure:** sweep. **Isolates:** Texture **Flux** (0 → 100); grain size & stretch held constant.
**Source audio:** `src_synth-note.wav` — the same sustained note as `granular-seam-grainsize`.

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_synth-note.wav` onto an audio track | — | The held note at native pitch |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Texture** | Granular engine engaged |
| 3 | Clip view | **Grain Size** | **0.3** (small–mid, HELD) | Grain size fixed for the whole demo |
| 4 | Transport | Stretch to **~500%** — project tempo **~20%** | ~500% | A held note with an obvious periodic buzz (Flux still 0) |
| 5 | Clip view | **Flux automation** | ramp **0 → 100** over ~5 s | The buzz dissolves into a smooth wash by the end |

**The abuse extreme here:** sweeping Flux to **100** is the marquee move — this is the granular-domain version of PaulStretch randomizing STFT phase. The "adding randomness makes it *smoother*" paradox is the entire demo.

## Verify
- **Audible:** starts as an obvious periodic buzz; ends as a smooth wash with the buzz gone. Buzz still present at the end ⇒ Flux didn't engage ⇒ reject.
- **Spectral:** periodic-buzz energy at the grain rate **drops monotonically** as Flux rises; spectrum becomes stationary/decorrelated. Buzz energy flat or rising ⇒ reject.

## Make it reusable (resample / freeze)
1. Render with the Flux ramp baked in.
2. Resample/freeze→flatten to `flux-smooths-buzz.wav`.
3. To reuse the end-state cloud, freeze at Flux 100 instead of the ramp.
