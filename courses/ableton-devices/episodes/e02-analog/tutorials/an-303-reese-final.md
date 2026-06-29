# Patch tutorial — `an-303-reese-final`

**Preset:** `presets/an-303-reese-final.adv`  ·  **Concept:** The saved "Subtractive-303-Reese" patch — both sounds from one device

> A short A/B: four bars of the acid 303 line, then four bars of the Reese on a held low note — two of the most influential bass sounds in electronic music from one default Analog patch.
>
> **You should hear:** Segment A = resonant per-note acid squelch. Segment B = sustained detuned-saw Reese growl. Clearly two different sounds from one chain.

**This demo is NOT a fresh build — it is a sequence (`concat_from`) of two already-saved steps:**

| Order | Source preset / tutorial | What it contributes |
|---|---|---|
| A (bars 1–4) | `an-303-step6` (the finished acid 303 config) | The resonant per-note acid squelch with automated cutoff |
| — | (a beat of silence) | The A/B gap |
| B (held low note) | `an-reese-final` (the Reese config) | The sustained detuned-saw growl |

Both sub-patches are level-matched (`AMP1 Level = 0.85`). Render `an-303-step6` and `an-reese-final` from their own tutorials/presets, then concatenate A → silence → B. The saved preset is the source of truth — it is the single "Subtractive-303-Reese" patch the walkthrough lands on.

_No new parameters to set. To persist the umbrella patch: save the morphed device (the `an-reese-final` / `an-303` shared chain) as `an-303-reese-final` into `presets/`._
