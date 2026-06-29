# Patch tutorial — `an-303-step5`

**Preset:** `presets/an-303-step5.adv`  ·  **Concept:** 303 build step 5 — Asym Drive for dirt + Env<Vel for the accent

> Asymmetric drive adds 303-style grit; high-velocity (accented) notes now open brighter than soft ones — that's the accent button, as velocity → filter-envelope depth. **Step 5 of the 6-step 303 ladder** — the additions are `F1 Drive = Asym2` and `FEG1 < Vel = 0.6`.
>
> **You should hear:** A gritty tone; accented (loud-velocity) notes audibly brighter/more open than soft ones.

Build from a **freshly loaded default Analog** (or continue from `an-303-step4`). Filter Freq is NORMALIZED 0–1 (NOT Hz).

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
| 16 | Filter 1 | F1 Resonance | 0.8 |  |
| 17 | **Filter 1** | **F1 Drive** | **Asym2 (the dirt)** | **A gritty, overdriven squelch** |
| 18 | Filter 1 | F1 Freq < Env | 0.75 |  |
| 19 | Filter Env 1 | FEG1 Attack | 0.01 (≈ 2 ms) |  |
| 20 | Filter Env 1 | FEG1 Decay | 0.25 (≈ 180 ms) |  |
| 21 | Filter Env 1 | FEG1 Sustain | 0.0 |  |
| 22 | **Filter Env 1** | **FEG1 < Vel** | **0.6 (velocity → filter-env depth = the accent)** | **Loud notes open brighter** |
| 23 | Amp Env 1 | AEG1 Attack | 0.01 (≈ 2 ms) |  |
| 24 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 25 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 26 | Amp Env 1 | AEG1 Rel | 0.15 (≈ 80 ms) |  |
| 27 | Global | Key Error | 0.0 |  |

**Play:** the 16th line with alternating velocities (e.g. vel 60 / vel 120) so the accent is audible inside the clip.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-303-step5` into `presets/`._
