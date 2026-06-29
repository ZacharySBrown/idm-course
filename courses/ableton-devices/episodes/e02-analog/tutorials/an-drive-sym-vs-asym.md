# Patch tutorial — `an-drive-sym-vs-asym`

**Preset:** `presets/an-drive-sym-vs-asym.adv`  ·  **Concept:** Filter Drive — symmetric (odd harmonics) vs asymmetric (even harmonics)

> The same resonant note played twice at the same cutoff: Drive = Sym2 (fuzzy, odd-harmonic, square-ward) then Drive = Asym2 (warmer, even-harmonic, tube-ish). Same sweep, different grit. **A/B demo: only `F1 Drive` changes.**
>
> **You should hear:** Same pitch/cutoff; A reads as harder/buzzier, B as warmer/rounder.

Build from a **freshly loaded default Analog**. One parameter per step. Filter Freq is NORMALIZED 0–1 (NOT Hz).

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
| 9 | Filter 1 | F1 Freq | 0.453 (≈ 500 Hz; identical both takes) |  |
| 10 | Filter 1 | F1 Resonance | 0.4 (enough drive into saturation) |  |
| 11 | **Filter 1** | **F1 Drive** | **A: Sym2  ·  B: Asym2** | **The ONE variable — A buzzy, B warm** |
| 12 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 13 | Amp Env 1 | AEG1 Attack | 0.03 (≈ 5 ms) |  |
| 14 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 15 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 16 | Amp Env 1 | AEG1 Rel | 0.2 (≈ 120 ms) |  |
| 17 | Global | Key Error | 0.0 |  |

**A/B:** render segment A with **F1 Drive = Sym2**, then B with **F1 Drive = Asym2**, everything else held. Play C2 both times. A adds odd harmonics; B adds the even 2nd.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-drive-sym-vs-asym` into `presets/`._
