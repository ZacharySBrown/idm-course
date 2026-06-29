# Patch tutorial — `an-reso-to-self-osc`

**Preset:** `presets/an-reso-to-self-osc.adv`  ·  **Concept:** Resonance → self-oscillation (the filter becomes a sine oscillator)

> A held saw with Resonance climbing 0 → max: a peak emerges at the cutoff, sharpens, then the filter sings its own near-pure sine — the Barkhausen unity-gain condition, by ear.
>
> **You should hear:** Loudness roughly constant; a tuned peak emerges and turns into a sustained sine at the (fixed) cutoff.

Build from a **freshly loaded default Analog**. One parameter per step. Filter Freq is NORMALIZED 0–1 (NOT Hz).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | OSC 1 | OSC1 On/Off | On |  |
| 2 | OSC 1 | OSC1 Shape | Saw | A bright saw |
| 3 | OSC 1 | OSC1 Balance | 1.0 |  |
| 4 | OSC 2 | OSC2 On/Off | Off |  |
| 5 | Noise | Noise On/Off | Off |  |
| 6 | Filter 1 | F1 On/Off | On |  |
| 7 | Filter 2 | F2 On/Off | Off |  |
| 8 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 9 | Filter 1 | F1 Freq | 0.482 (≈ 600 Hz; fixed = the sung pitch) | A darkened saw |
| 10 | Filter 1 | F1 Resonance | 0.0 (the ONE variable, swept below) |  |
| 11 | Filter 1 | F1 Drive | Off |  |
| 12 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 13 | Amp Env 1 | AEG1 Attack | 0.05 (≈ 10 ms) |  |
| 14 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 15 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 16 | Amp Env 1 | AEG1 Rel | 0.24 (≈ 150 ms) |  |
| 17 | Global | Key Error | 0.0 |  |

**Sweep (the ONE variable):** hold C3 and automate **F1 Resonance** from **0.0 → 1.0** over ~5.5 s. A peak at the cutoff emerges, sharpens, and by clip end the filter rings a near-pure sine.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-reso-to-self-osc` into `presets/`._
