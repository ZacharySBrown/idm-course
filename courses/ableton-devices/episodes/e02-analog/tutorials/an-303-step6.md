# Patch tutorial — `an-303-step6`

**Preset:** `presets/an-303-step6.adv`  ·  **Concept:** 303 build step 6 — the full acid line with cutoff automated

> The finished 303: a 16th-note line with slides, F1 Freq swept by automation across the loop — saw, resonant low-pass, and a hand on the cutoff. **Final step (6 of 6) of the 303 ladder.** Adds `AMP1 Level = 0.85` (level-matches the Reese for the `an-303-reese-final` A/B) and the performed cutoff sweep.
>
> **You should hear:** A complete acid line whose cutoff visibly opens and closes across the loop.

Build from a **freshly loaded default Analog** (or continue from `an-303-step5`). Filter Freq is NORMALIZED 0–1 (NOT Hz).

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
| 15 | Filter 1 | F1 Freq | 0.371 (≈ 300 Hz start; automation sweeps it) |  |
| 16 | Filter 1 | F1 Resonance | 0.8 |  |
| 17 | Filter 1 | F1 Drive | Asym2 |  |
| 18 | Filter 1 | F1 Freq < Env | 0.75 |  |
| 19 | Filter Env 1 | FEG1 Attack | 0.01 (≈ 2 ms) |  |
| 20 | Filter Env 1 | FEG1 Decay | 0.25 (≈ 180 ms) |  |
| 21 | Filter Env 1 | FEG1 Sustain | 0.0 |  |
| 22 | Filter Env 1 | FEG1 < Vel | 0.6 |  |
| 23 | Amp Env 1 | AEG1 Attack | 0.01 (≈ 2 ms) |  |
| 24 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 25 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 26 | **Amp 1** | **AMP1 Level** | **0.85 (level-match the Reese for the A/B)** | **A healthy line level** |
| 27 | Amp Env 1 | AEG1 Rel | 0.15 (≈ 80 ms) |  |
| 28 | Global | Key Error | 0.0 |  |

**Play + automate (the performed move):** program a 4-bar 16th line (e.g. C2-C2-C3-C2-Eb2-C2-G2-Bb2 at 130 BPM with offbeat accents), then automate **F1 Freq** from **0.371 → 0.691** (≈ 300 → 2200 Hz) across the loop. The cutoff opens across the bars.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-303-step6` into `presets/`._
