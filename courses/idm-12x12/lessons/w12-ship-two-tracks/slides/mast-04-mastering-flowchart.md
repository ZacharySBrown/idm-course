# The mastering chain — signal order that survives contact with reality

Six stages, in this order, on the master bus. Deviate and you will regret it.

1. **Pre-master check** — mix bounce imported on a new Live set, one stereo track, no plugins. Reference tracks on parallel tracks, Utility-gain-matched to the same integrated LUFS. This is the starting point. If the mix is broken here, mastering will not save it.
2. **Master EQ** — broad strokes only. Low-shelf below 30 Hz if there is sub-mud. High-shelf at 12 kHz if the top is dull. No narrow cuts. If you need surgery, the mix is not finished.
3. **Master compression (optional)** — 1.5:1 to 2:1 ratio, slow attack, auto release, 1–2 dB gain reduction max. Glue, not squash. Skip this if the mix already feels cohesive.
4. **Limiter** — Pro-L 2, stock Limiter, Ozone Maximizer, bx_XL. Ceiling at −1.0 dBTP. Threshold pulled down until integrated LUFS hits the target. <Citation bib="fabfilter_prol2_docs" />
5. **Metering** — Youlean (LUFS + TP) and SPAN (spectrum) at the end of the chain. Measurement only, zero effect on signal.
6. **Export** — 24-bit / 44.1 kHz WAV. Dither is automatic in Live on 16-bit export; skip for 24-bit.

The order matters because EQ before limiter changes *what the limiter is limiting*. Limiter before EQ means the EQ is re-lifting content you already clamped. <Citation bib="ableton_live_12_manual" />
