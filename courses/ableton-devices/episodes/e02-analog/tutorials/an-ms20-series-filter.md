# Patch tutorial — `an-ms20-series-filter`

**Preset:** `presets/an-ms20-series-filter.adv`  ·  **Concept:** Two filters in series — resonant HP → resonant LP (the MS-20 band)

> A saw through a resonant high-pass into a resonant low-pass, the two cutoffs swept against each other: a vocal, hollow, band-limited sweep — the MS-20's HP→LP architecture rebuilt in Analog. `F1 To F2 = 1.0` routes F1 into F2 (series); `F2 Slave = Off` keeps the two edges independent.
>
> **You should hear:** A pass-band that narrows/moves; resonant peaks on both edges; no all-pass "full" moment.

Build from a **freshly loaded default Analog**. One parameter per step. F1/F2 Freq are NORMALIZED 0–1 (NOT Hz).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | OSC 1 | OSC1 On/Off | On |  |
| 2 | OSC 1 | OSC1 Shape | Saw |  |
| 3 | OSC 1 | OSC1 Balance | 1.0 (OSC1 fully into F1 first) |  |
| 4 | OSC 2 | OSC2 On/Off | Off |  |
| 5 | Noise | Noise On/Off | Off |  |
| 6 | Filter 1 | F1 On/Off | On |  |
| 7 | Filter 1 | F1 To F2 | 1.0 (full series amount, F1 → F2) | F1 feeds F2 |
| 8 | Filter 1 | F1 Type | High-pass 24dB/oct (resonant HP) |  |
| 9 | Filter 1 | F1 Freq | 0.305 (≈ 200 Hz start; HP edge sweeps up) |  |
| 10 | Filter 1 | F1 Resonance | 0.65 |  |
| 11 | Filter 1 | F1 Drive | Off |  |
| 12 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 13 | Filter 2 | F2 On/Off | On |  |
| 14 | Filter 2 | F2 Type | Low-pass 24dB/oct (resonant LP) | A hollow band-pass |
| 15 | Filter 2 | F2 Freq | 0.705 (≈ 2400 Hz; held — the upper band edge) |  |
| 16 | Filter 2 | F2 Resonance | 0.65 |  |
| 17 | Filter 2 | F2 Slave | Off (F2 does NOT follow F1 — independent edge) |  |
| 18 | Amp Env 1 | AEG1 Attack | 0.05 (≈ 10 ms) |  |
| 19 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 20 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 21 | Amp Env 1 | AEG1 Rel | 0.24 (≈ 150 ms) |  |
| 22 | Global | Key Error | 0.0 |  |

**Sweep (the ONE variable):** hold C2 and automate **F1 Freq** from **0.305 → 0.676** (≈ 200 → 2000 Hz) while F2 holds. The lower band edge sweeps up against the fixed upper edge.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-ms20-series-filter` into `presets/`._
