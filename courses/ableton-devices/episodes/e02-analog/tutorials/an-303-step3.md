# Patch tutorial — `an-303-step3`

**Preset:** `presets/an-303-step3.adv`  ·  **Concept:** 303 build step 3 — filter envelope → Freq (the per-note "wow")

> Each note now blips open and shut: a fast filter-envelope decay sweeps the cutoff per note while the volume stays constant — the acid "wow." **Step 3 of the 6-step 303 ladder** — the ONE addition is `F1 Freq < Env` + a short `FEG1 Decay`; base cutoff dropped so the env opens it upward.
>
> **You should hear:** A per-note brightness blip (open→shut) at constant loudness.

Build from a **freshly loaded default Analog** (or continue from `an-303-step2`). Filter Freq is NORMALIZED 0–1 (NOT Hz); `F1 Freq < Env` is the filter-env amount (−1..1).

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
| 15 | **Filter 1** | **F1 Freq** | **0.417 (≈ 400 Hz lower base; env opens it up)** | **Darker resting tone** |
| 16 | Filter 1 | F1 Resonance | 0.4 |  |
| 17 | Filter 1 | F1 Drive | Off |  |
| 18 | **Filter 1** | **F1 Freq < Env** | **0.75 (filter env → cutoff, high)** | **The cutoff now moves per note** |
| 19 | **Filter Env 1** | **FEG1 Attack** | **0.01 (≈ 2 ms)** | **Instant open** |
| 20 | **Filter Env 1** | **FEG1 Decay** | **0.25 (≈ 180 ms — the per-note wow)** | **A fast open→shut blip** |
| 21 | **Filter Env 1** | **FEG1 Sustain** | **0.0 (falls back to base cutoff)** |  |
| 22 | Amp Env 1 | AEG1 Attack | 0.01 (≈ 2 ms) |  |
| 23 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 24 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 25 | Amp Env 1 | AEG1 Rel | 0.15 (≈ 80 ms) |  |
| 26 | Global | Key Error | 0.0 |  |

**Play:** the same 16th line as step1/2. Each note now "wows."

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-303-step3` into `presets/`._
