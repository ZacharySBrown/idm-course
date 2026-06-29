# Patch tutorial — `an-loop-env-pulse`

**Preset:** `presets/an-loop-env-pulse.adv`  ·  **Concept:** Looping filter envelope (AD-R) = rhythm from one held note (no LFO, no sequencer)

> A single held note; the filter envelope set to loop (AD-R) at a tempo-ish rate cycles the cutoff open and shut — an evolving rhythmic filter pulse with nothing sequencing it. The Attack + Decay together set the loop period.
>
> **You should hear:** A regular, repeating filter open/close pulse from a single sustained note.

Build from a **freshly loaded default Analog**. F1 Freq is NORMALIZED 0–1 (NOT Hz); `FEG1 Loop` ∈ {Off, AD-R, ADR-R, ADS-AR}.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | OSC 1 | OSC1 On/Off | On |  |
| 2 | OSC 1 | OSC1 Shape | Saw |  |
| 3 | OSC 1 | OSC1 Balance | 1.0 |  |
| 4 | OSC 2 | OSC2 On/Off | Off |  |
| 5 | Noise | Noise On/Off | Off |  |
| 6 | Filter 1 | F1 On/Off | On |  |
| 7 | Filter 2 | F2 On/Off | Off |  |
| 8 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 9 | Filter 1 | F1 Freq | 0.395 (≈ 350 Hz base; the loop opens it) | A dark resting tone |
| 10 | Filter 1 | F1 Resonance | 0.55 |  |
| 11 | Filter 1 | F1 Drive | Off |  |
| 12 | Filter 1 | F1 Freq < Env | 0.8 |  |
| 13 | **Filter Env 1** | **FEG1 Loop** | **AD-R (the ONE variable that makes this rhythmic)** | **A repeating open/close pulse** |
| 14 | Filter Env 1 | FEG1 Attack | 0.07 (≈ 40 ms — the pulse rise) |  |
| 15 | Filter Env 1 | FEG1 Decay | 0.3 (≈ 220 ms — the pulse fall; A+D = loop period) | The pulse rate |
| 16 | Filter Env 1 | FEG1 Sustain | 0.0 |  |
| 17 | Amp Env 1 | AEG1 Attack | 0.05 (≈ 10 ms) |  |
| 18 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 19 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 20 | Amp Env 1 | AEG1 Rel | 0.24 (≈ 150 ms) |  |
| 21 | Global | Key Error | 0.0 |  |

**Play:** hold ONE note (C2). The looping filter envelope does the rhythm — no LFO, no sequencer.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-loop-env-pulse` into `presets/`._
