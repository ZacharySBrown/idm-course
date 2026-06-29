# Patch tutorial — `an-303-step2`

**Preset:** `presets/an-303-step2.adv`  ·  **Concept:** 303 build step 2 — add the resonant 24 dB low-pass

> The same line, now darkened and slightly peaky as a 24 dB low-pass closes over it with light resonance. The carve begins. **Step 2 of the 6-step 303 ladder** — the ONE change from step1 is the filter (open → LP 24 at a mid cutoff with ~40% reso).
>
> **You should hear:** Same line as step1, audibly darker with a slight resonant edge.

Build from a **freshly loaded default Analog** (or continue from `an-303-step1`). Filter Freq is NORMALIZED 0–1 (NOT Hz).

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
| 9 | OSC 1 | OSC1 Balance | 1.0 (full to F1) |  |
| 10 | OSC 2 | OSC2 On/Off | Off |  |
| 11 | Noise | Noise On/Off | Off |  |
| 12 | Filter 1 | F1 On/Off | On |  |
| 13 | Filter 2 | F2 On/Off | Off |  |
| 14 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 15 | **Filter 1** | **F1 Freq** | **0.507 (≈ 700 Hz; mid — the carve)** | **Darker than step1** |
| 16 | **Filter 1** | **F1 Resonance** | **0.4** | **A slight resonant edge** |
| 17 | Filter 1 | F1 Drive | Off |  |
| 18 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 19 | Amp Env 1 | AEG1 Attack | 0.01 (≈ 2 ms) |  |
| 20 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 21 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 22 | Amp Env 1 | AEG1 Rel | 0.15 (≈ 80 ms) |  |
| 23 | Global | Key Error | 0.0 |  |

**Play:** the same 16th line as step1.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-303-step2` into `presets/`._
