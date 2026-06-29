# Warp Recipe: granular-seam-grainsize

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Texture **Grain Size** → grain rate → the pitch of the seam-buzz between grains.
**What you should hear:** one sustained note warped to 400% in signal-blind Texture, buzzing at the grain rate; as Grain Size is dragged UP, the buzz **drops in pitch** because the seams come less often.
**Structure:** sweep. **Isolates:** Texture **Grain Size** (small → large), Flux **held at 0** so only the seam-rate moves.
**Source audio:** `src_synth-note.wav` — one sustained note (needs a steady spectrum).

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_synth-note.wav` onto an audio track | — | The held note at native pitch |
| 1 | Clip view | **Warp** | ON | Clip follows project tempo |
| 2 | Clip view | **Warp Mode** | **Texture** | Granular engine engaged |
| 3 | Clip view | **Flux** | **0** (HELD) | The periodic seam-buzz is **exposed**, not smoothed |
| 4 | Transport | Stretch to **~400%** — project tempo **~25%** of analyzed | ~400% | A held note with an audible buzz at the grain rate |
| 5 | Clip view | **Grain Size automation** | ramp **0.1 → 0.85** over ~5 s | The buzz **pitch falls** as Grain Size rises; the note's own pitch stays fixed |

**The abuse extreme here:** **Flux = 0** is deliberate — it removes the smoothing so the grain SEAM becomes a pitched buzz you can hear move. This is the demo that exposes the mechanism the cold open hides.

## Verify
- **Audible:** held-note pitch constant; a buzz present throughout whose PITCH falls as Grain Size rises. Flat buzz pitch ⇒ Grain Size didn't move the rate ⇒ reject.
- **Spectral:** a comb whose spacing (grain rate) **decreases monotonically** as Grain Size rises; source fundamental fixed. Flat comb spacing ⇒ reject.

## Make it reusable (resample / freeze)
1. Render with the Grain Size automation in place (so the sweep is baked).
2. Resample/freeze→flatten to a new audio clip → `granular-seam-grainsize.wav`.
3. To reuse a single grain-rate, freeze at one Grain Size value (e.g. 0.4) instead of the ramp.
