# Patch tutorial — `an-reese-detune-sweep`

**Preset:** `presets/an-reese-detune-sweep.adv`  ·  **Concept:** Detuning two saws → beating / phase-cancellation ("fat" = interference)

> A held low note: two saws starting in unison (static), then OSC2 detuned 0 → 20 cents — the static tone blooms into a slow, accelerating "wub" with no LFO anywhere.
>
> **You should hear:** Pitch and loudness steady; an amplitude beating emerges and speeds up as the detune widens.

Build from a **freshly loaded default Analog**. One parameter per step. Detune is NORMALIZED: 0.5 = 0 cents, ±300 c full (norm = 0.5 + cents/600).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | OSC 1 | OSC1 On/Off | On |  |
| 2 | OSC 1 | OSC1 Shape | Saw |  |
| 3 | OSC 1 | OSC1 Detune | 0.5 (= 0 cents) |  |
| 4 | OSC 1 | OSC1 Balance | 1.0 |  |
| 5 | OSC 2 | OSC2 On/Off | On | A second saw |
| 6 | OSC 2 | OSC2 Shape | Saw | Two saws in unison (static) |
| 7 | OSC 2 | OSC2 Detune | 0.5 (= 0 cents; swept to +20 c below) |  |
| 8 | OSC 2 | OSC2 Balance | 1.0 |  |
| 9 | Noise | Noise On/Off | Off |  |
| 10 | Filter 1 | F1 On/Off | On |  |
| 11 | Filter 2 | F2 On/Off | Off |  |
| 12 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 13 | Filter 1 | F1 Freq | 0.594 (≈ 1200 Hz; tames the saws, lets the beat through) |  |
| 14 | Filter 1 | F1 Resonance | 0.1 |  |
| 15 | Filter 1 | F1 Drive | Sym1 (touch of body) |  |
| 16 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 17 | Amp Env 1 | AEG1 Attack | 0.05 (≈ 10 ms) |  |
| 18 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 19 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 20 | Amp Env 1 | AEG1 Rel | 0.24 (≈ 150 ms) |  |
| 21 | Global | Key Error | 0.0 (beating must come from Detune, not drift) |  |

**Sweep (the ONE variable):** hold C1 and automate **OSC2 Detune** from **0.5 → 0.533** (0 → +20 cents) over ~5.5 s. A slow beat emerges and accelerates as detune widens.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-reese-detune-sweep` into `presets/`._
