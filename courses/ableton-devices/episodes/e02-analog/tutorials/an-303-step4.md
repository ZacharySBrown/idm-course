# Patch tutorial — `an-303-step4`

**Preset:** `presets/an-303-step4.adv`  ·  **Concept:** 303 build step 4 — resonance up toward self-oscillation (the squelch)

> Same line, the resonance pushed to ~80%: the per-note sweep sharpens into the singing squelch that defines acid. **Step 4 of the 6-step 303 ladder** — the ONE change from step3 is `F1 Resonance` 0.4 → 0.8.
>
> **You should hear:** A sharper, more vocal/squelchy resonant peak on each note vs step3.

Build from a **freshly loaded default Analog** (or continue from `an-303-step3`). Filter Freq is NORMALIZED 0–1 (NOT Hz).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | Global / Voices | Voices | Mono |  |
| 2 | Global / Glide | Glide On/Off | On |  |
| 3 | Global / Glide | Glide Mode | Const |  |
| 4 | Global / Glide | Glide Time | 0.15 |  |
| 5 | Global / Glide | Glide Legato | On |  |
| 6 | OSC 1 | OSC1 On/Off | On |  |
| 7 | OSC 1 | OSC1 Shape | Saw |  |
| 8 | OSC 1 | O1 Sub/Sync | 0.0 |  |
| 9 | OSC 1 | OSC1 Balance | 1.0 |  |
| 10 | OSC 2 | OSC2 On/Off | Off |  |
| 11 | Noise | Noise On/Off | Off |  |
| 12 | Filter 1 | F1 On/Off | On |  |
| 13 | Filter 2 | F2 On/Off | Off |  |
| 14 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 15 | Filter 1 | F1 Freq | 0.417 (≈ 400 Hz) |  |
| 16 | **Filter 1** | **F1 Resonance** | **0.8 (the ONE change from step3)** | **A sharp, vocal squelch per note** |
| 17 | Filter 1 | F1 Drive | Off |  |
| 18 | Filter 1 | F1 Freq < Env | 0.75 |  |
| 19 | Filter Env 1 | FEG1 Attack | 0.01 (≈ 2 ms) |  |
| 20 | Filter Env 1 | FEG1 Decay | 0.25 (≈ 180 ms) |  |
| 21 | Filter Env 1 | FEG1 Sustain | 0.0 |  |
| 22 | Amp Env 1 | AEG1 Attack | 0.01 (≈ 2 ms) |  |
| 23 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 24 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 25 | Amp Env 1 | AEG1 Rel | 0.15 (≈ 80 ms) |  |
| 26 | Global | Key Error | 0.0 |  |

**Play:** the same 16th line. The wow is now a squelch.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-303-step4` into `presets/`._
