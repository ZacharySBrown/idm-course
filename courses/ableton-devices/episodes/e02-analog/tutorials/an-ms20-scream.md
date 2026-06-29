# Patch tutorial — `an-ms20-scream`

**Preset:** `presets/an-ms20-scream.adv`  ·  **Concept:** The MS-20 dual filter pushed past polite (HP→LP series, both screaming)

> A saw through a resonant HP into a resonant LP in series, both cutoffs swept hard against each other into a vocal, screaming, semi-broken sweep — the Autechre move before the lo-fi degrade. Distinct from `an-ms20-series-filter` (04d): here **BOTH cutoffs sweep in OPPOSITION** and the resonances are pushed extreme. The mix adds bitcrush + short reverb after this render.
>
> **You should hear:** An aggressive, vocal, resonant sweep with a moving narrow pass-band; no clean/full moment.

Build from a **freshly loaded default Analog**. F1/F2 Freq are NORMALIZED 0–1 (NOT Hz).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | OSC 1 | OSC1 On/Off | On |  |
| 2 | OSC 1 | OSC1 Shape | Saw |  |
| 3 | OSC 1 | OSC1 Balance | 1.0 |  |
| 4 | OSC 2 | OSC2 On/Off | Off |  |
| 5 | Noise | Noise On/Off | Off |  |
| 6 | Filter 1 | F1 On/Off | On |  |
| 7 | Filter 1 | F1 To F2 | 1.0 (full series amount) | F1 feeds F2 |
| 8 | Filter 1 | F1 Type | High-pass 24dB/oct |  |
| 9 | Filter 1 | F1 Freq | 0.259 (≈ 150 Hz; HP sweeps UP) |  |
| 10 | Filter 1 | F1 Resonance | 0.85 (pushed) | A screaming HP edge |
| 11 | Filter 1 | F1 Drive | Asym2 |  |
| 12 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 13 | Filter 2 | F2 On/Off | On |  |
| 14 | Filter 2 | F2 Type | Low-pass 24dB/oct |  |
| 15 | Filter 2 | F2 Freq | 0.741 (≈ 3000 Hz; LP sweeps DOWN) |  |
| 16 | Filter 2 | F2 Resonance | 0.85 (pushed) | A screaming LP edge |
| 17 | Filter 2 | F2 Slave | Off (independent edges) |  |
| 18 | Amp Env 1 | AEG1 Attack | 0.05 (≈ 10 ms) |  |
| 19 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 20 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 21 | Amp Env 1 | AEG1 Rel | 0.24 (≈ 150 ms) |  |
| 22 | Global | Key Error | 0.05 (a touch of instability) |  |

**Sweep (the ONE move, in opposition):** hold C2 and automate **F1 Freq 0.259 → 0.659** (≈ 150 → 1800 Hz, HP UP) while automating **F2 Freq 0.741 → 0.507** (≈ 3000 → 700 Hz, LP DOWN). The two resonant peaks converge then cross — the scream.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-ms20-scream` into `presets/`._
