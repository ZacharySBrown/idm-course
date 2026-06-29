# Patch tutorial — `an-slope-12-vs-24`

**Preset:** `presets/an-slope-12-vs-24.adv`  ·  **Concept:** Filter slope (poles) → darkness above cutoff

> The same held saw at the same cutoff, played twice: 12 dB/oct then 24 dB/oct. The 24 dB version is audibly darker above the cutoff — twice the roll-off. **A/B demo: only `F1 Type` changes between segments.**
>
> **You should hear:** Same pitch and cutoff both takes; segment B (24 dB) has less high-frequency content.

Build from a **freshly loaded default Analog**. One parameter per step. Filter Freq is NORMALIZED 0–1 (NOT Hz).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | OSC 1 | OSC1 On/Off | On |  |
| 2 | OSC 1 | OSC1 Shape | Saw | A bright buzzy saw |
| 3 | OSC 1 | OSC1 Balance | 1.0 (full to F1) |  |
| 4 | OSC 2 | OSC2 On/Off | Off |  |
| 5 | Noise | Noise On/Off | Off |  |
| 6 | Filter 1 | F1 On/Off | On |  |
| 7 | Filter 2 | F2 On/Off | Off |  |
| 8 | **Filter 1** | **F1 Type** | **A: Low-pass 12dB/oct  ·  B: Low-pass 24dB/oct** | **The ONE variable — B is darker** |
| 9 | Filter 1 | F1 Freq | 0.528 (≈ 800 Hz; same both takes) | A darkened saw |
| 10 | Filter 1 | F1 Resonance | 0.15 (slight, identical both) |  |
| 11 | Filter 1 | F1 Drive | Off |  |
| 12 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 13 | Amp Env 1 | AEG1 Attack | 0.03 (≈ 5 ms) |  |
| 14 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 15 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 16 | Amp Env 1 | AEG1 Rel | 0.2 (≈ 120 ms) |  |
| 17 | Global | Key Error | 0.0 |  |

**A/B:** render segment A with **F1 Type = Low-pass 12dB/oct**, then segment B with **F1 Type = Low-pass 24dB/oct**, everything else held. Play C3 both times. B is the darker take.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-slope-12-vs-24` into `presets/`._
