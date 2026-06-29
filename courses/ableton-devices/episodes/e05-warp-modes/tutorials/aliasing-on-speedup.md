# Warp Recipe: aliasing-on-speedup

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Re-Pitch (varispeed) sped up → partials cross Nyquist and fold back as inharmonic fizz — sampling theory by ear.
**What you should hear:** a bright cymbal loop in Re-Pitch pushed to double speed: brighter and chipmunked, with an inharmonic "fizz" on the very top that does **not** belong to the cymbal — partials folding back under Nyquist.
**Structure:** single. **Isolates:** Re-Pitch **tempo ratio (2×)** — the only lever; Transpose is **disabled** in Re-Pitch.
**Source audio:** `src_cymbals.wav` — a bright cymbal/ride loop (lots of HF energy).

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_cymbals.wav` onto an audio track | — | The cymbal loop at native pitch |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Re-Pitch** | Varispeed; **Transpose/Detune greyed out** — confirm they're disabled |
| 3 | Transport | Stretch to **double speed** — project tempo **200%** | 200% | Brighter, chipmunked, half as long, with **fizz on top** that isn't a clean octave-up |

**The abuse extreme here:** push the ratio — **2×**, and if the resampler is too clean to show it, **2.5–3×** or a brighter source. The fizz is the artifact: HF partials crossing **Nyquist (f_s/2)** and folding back as inharmonic tones. **Do not claim a measured resampler spec on-mic** — Live's resampler quality is unpublished; phrase it as "the artifact of sample-rate conversion."

## Verify
- **Audible:** an inharmonic fizz/whistle on the top that is NOT a clean octave-up — aliasing. Clean octave-up with no fizz ⇒ no audible aliasing on this rip ⇒ try a brighter source / steeper push, else reject.
- **Spectral:** inharmonic energy at frequencies that are NOT integer images of the source partials (folded under Nyquist), distinct from a simple frequency-scaled spectrum. Pure scaled spectrum, no fold-back ⇒ reject.

## Make it reusable (resample / freeze)
1. Render at the chosen ratio.
2. Resample/freeze→flatten to `aliasing-on-speedup.wav`.
3. The aliased fizz is now baked in — drag the bounce in as a found lo-fi top-end texture.
