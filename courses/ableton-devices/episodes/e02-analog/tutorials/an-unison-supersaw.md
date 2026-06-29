# Patch tutorial — `an-unison-supersaw`

**Preset:** `presets/an-unison-supersaw.adv`  ·  **Concept:** Unison voices + Detune → the JP-8000 Supersaw (fat = many copies that almost agree)

> A held chord played twice: Unison off (thin, single saw per note) then Unison On with 4 voices + Detune (a wide, shimmering supersaw wall). Same notes, four detuned copies each. **A/B demo: only `Unison On/Off` changes** (Analog's 4 unison voices approximate the JP-8000's 7-saw Super Saw).
>
> **You should hear:** B is wider, thicker, chorusing vs the thin A; same pitches.

Build from a **freshly loaded default Analog**. One parameter per step. Filter Freq is NORMALIZED 0–1 (NOT Hz).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | Global / Voices | Voices | 8 (headroom for the chord) |  |
| 2 | OSC 1 | OSC1 On/Off | On |  |
| 3 | OSC 1 | OSC1 Shape | Saw |  |
| 4 | OSC 1 | OSC1 Balance | 1.0 |  |
| 5 | OSC 2 | OSC2 On/Off | Off |  |
| 6 | Noise | Noise On/Off | Off |  |
| 7 | Filter 1 | F1 On/Off | On |  |
| 8 | Filter 2 | F2 On/Off | Off |  |
| 9 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 10 | Filter 1 | F1 Freq | 0.853 (≈ 6000 Hz; bright so the shimmer shows) |  |
| 11 | Filter 1 | F1 Resonance | 0.05 |  |
| 12 | Filter 1 | F1 Drive | Off |  |
| 13 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 14 | Amp Env 1 | AEG1 Attack | 0.12 (≈ 60 ms) |  |
| 15 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 16 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 17 | Amp Env 1 | AEG1 Rel | 0.35 (≈ 300 ms) |  |
| 18 | **Global / Unison** | **Unison On/Off** | **A: Off  ·  B: On** | **The ONE variable — B = supersaw wall** |
| 19 | Global / Unison | Unison Voices | 4 (detuned copies when unison engages) |  |
| 20 | Global / Unison | Unison Detune | 0.3 (spread; audible only when Unison on) |  |

**A/B:** render segment A (chord C3/G3) with **Unison On/Off = Off**, then B with **Unison On/Off = On**, everything else held. B fans each saw into four detuned copies.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-unison-supersaw` into `presets/`._
