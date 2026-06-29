# Patch tutorial — `an-error-drift`

**Preset:** `presets/an-error-drift.adv`  ·  **Concept:** Error → re-injected per-voice tuning drift ("make it analog")

> The same sustained chord twice: Error = 0 (dead-stable, clinical) then Error dialed up (each voice drifts slightly out of tune — the model "comes alive"). **A/B demo: only `Key Error` changes.** Detune is held at 0 so Error is the only drift source.
>
> **You should hear:** A perfectly still; B has slow beating/chorusing between voices.

Build from a **freshly loaded default Analog**. One parameter per step. `Key Error` is the spec's global "Error" (random per-voice tuning drift); needs polyphony to be audible.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | Global / Voices | Voices | 4 (polyphony for the chord) |  |
| 2 | OSC 1 | OSC1 On/Off | On |  |
| 3 | OSC 1 | OSC1 Shape | Saw |  |
| 4 | OSC 1 | OSC1 Balance | 1.0 |  |
| 5 | OSC 2 | OSC2 On/Off | On |  |
| 6 | OSC 2 | OSC2 Shape | Saw | Two saws per voice |
| 7 | OSC 2 | OSC2 Detune | 0.5 (= 0 cents — Error is the ONLY drift) |  |
| 8 | OSC 2 | OSC2 Balance | 1.0 |  |
| 9 | Noise | Noise On/Off | Off |  |
| 10 | Filter 1 | F1 On/Off | On |  |
| 11 | Filter 2 | F2 On/Off | Off |  |
| 12 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 13 | Filter 1 | F1 Freq | 0.741 (≈ 3000 Hz; open-ish) |  |
| 14 | Filter 1 | F1 Resonance | 0.1 |  |
| 15 | Filter 1 | F1 Drive | Off |  |
| 16 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 17 | Amp Env 1 | AEG1 Attack | 0.15 (≈ 80 ms) |  |
| 18 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 19 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 20 | Amp Env 1 | AEG1 Rel | 0.42 (≈ 400 ms) |  |
| 21 | **Global** | **Key Error** | **A: 0.0  ·  B: 0.35** | **The ONE variable — B drifts/chorus** |

**A/B:** render segment A (chord C3/E3/G3) with **Key Error = 0.0**, then B with **Key Error = 0.35**, everything else held. A is dead-stable; B comes alive with per-voice beating.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-error-drift` into `presets/`._
