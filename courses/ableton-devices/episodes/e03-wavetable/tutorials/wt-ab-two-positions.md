# Patch: A/B Two Positions  (preset: presets/wt-ab-two-positions.adv)

Concept demonstrated: **a wavetable IS a collection of spectra** — two positions of ONE table are two distinct timbres. Same note, played at a low Position then a high Position.

Build from a **freshly loaded default Wavetable.** One parameter per step. Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | **Basic Shapes** (default) | Same tone. ⚠ Table not settable headless — confirm Basic Shapes by hand. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.1 (segment A, low) | A dark, near-sine tone |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 7 | Sub | Sub On | Off (0) | No sub |
| 8 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 9 | Filter 1 | Flt 1 Type | 0 (Clean) | Transparent circuit |
| 10 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 11 | Filter 1 | Flt 1 Freq | 1.0 (open) | Full brightness — identical both segments |
| 12 | Filter 1 | Flt 1 Res | 0.0 | No resonance |
| 13 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 14 | Amp Env | Amp Attack | 0.05 | Fast attack |
| 15 | Amp Env | Amp Decay | 0.0 | No decay |
| 16 | Amp Env | Amp Sustain | 1.0 | Holds full level |
| 17 | Amp Env | Amp Release | 0.15 | Short tail |

**The demonstrative move (A/B, discrete):**
- **Segment A:** play **C3** (~2 s) with **Osc 1 Pos = 0.1** — a dark tone.
- Beat of silence.
- **Segment B:** play **C3** again (~2 s) with **Osc 1 Pos = 0.85** — a brighter, richer tone.

Final check: same pitch both segments; B is audibly brighter/more harmonics than A. A ≈ B ⇒ reject.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-ab-two-positions.adv` (save with **Osc 1 Pos = 0.1**, the segment-A value; B is re-rendered by the A/B pass).
