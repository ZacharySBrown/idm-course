# Patch tutorial — `an-filter-env-vs-amp-env`

**Preset:** `presets/an-filter-env-vs-amp-env.adv`  ·  **Concept:** Same envelope shape, two destinations — filter env = brightness, amp env = loudness

> One decay shape played twice. **A:** on the FILTER envelope — the note "plucks" brighter→darker at constant volume. **B:** on the AMP envelope — loudness drops while the timbre stays put. Same shape, opposite result. **A/B demo: the decay TIME is identical; only its destination moves.**
>
> **You should hear:** A = constant loudness, brightness collapses (a wah/pluck). B = loudness collapses, brightness constant.

Build from a **freshly loaded default Analog**. One parameter per step. Filter Freq is NORMALIZED 0–1 (NOT Hz); `F1 Freq < Env` is the filter-env amount (−1..1).

| # | Panel | Parameter | Value (A → B) | You should now hear |
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
| 9 | Filter 1 | F1 Freq | 0.507 (≈ 700 Hz base cutoff) |  |
| 10 | Filter 1 | F1 Resonance | 0.25 |  |
| 11 | Filter 1 | F1 Drive | Off |  |
| 12 | **Filter 1** | **F1 Freq < Env** | **A: 0.7  ·  B: 0.0** | **A/B — A: filter env drives cutoff; B: off** |
| 13 | Filter Env 1 | FEG1 Attack | 0.03 (≈ 5 ms) |  |
| 14 | Filter Env 1 | FEG1 Decay | 0.5 (≈ 600 ms — the shared decay shape) |  |
| 15 | Filter Env 1 | FEG1 Sustain | 0.0 |  |
| 16 | Amp Env 1 | AEG1 Attack | 0.03 (≈ 5 ms) |  |
| 17 | **Amp Env 1** | **AEG1 Decay** | **A: 0.0  ·  B: 0.5 (≈ 600 ms)** | **A/B — A: sustained; B: amp decays** |
| 18 | **Amp Env 1** | **AEG1 Sustain** | **A: 1.0  ·  B: 0.0** | **A/B — A: full sustain; B: decays to silence** |
| 19 | Amp Env 1 | AEG1 Rel | 0.2 (≈ 120 ms) |  |
| 20 | Global | Key Error | 0.0 |  |

**A/B:** segment A is the table's "A" column (filter env drives the cutoff, amp sustained). Segment B flips the three A/B rows (filter env off; the identical decay now lives on the amp env). Play C3 both times.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-filter-env-vs-amp-env` into `presets/`._
