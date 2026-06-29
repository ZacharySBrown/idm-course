# Patch: Type-Switch Live  (preset: presets/meld-type-switch-live.adv)

**Demo:** `meld-type-switch-live`  ·  **Slide:** `03a-the-osc-families`  ·  **Structure:** ab (A/B/C)
**Concept demonstrated:** two knobs hide a whole instrument — same note, change the oscillator type, get a new instrument.
**Render status:** RENDERABLE headless (A/B/C split render across `A Osc Type` = 0 / 9 / 12). No matrix, no MPE.

Build from a **freshly loaded default Meld**. One parameter per step. The base state is segment A (Basic Shapes); the demo re-renders the same patch at three `A Osc Type` values separated by a beat of silence.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine B | `B On` | Off (0) | Engine B silent |
| 2 | Engine A | `A On` | On (1) | Engine A only |
| 3 | Engine A | `A Osc Type` | **0 = Basic Shapes** (segment A) | A clean analog shape |
| 4 | Engine A | `A Osc Shape` (macro 1) | 0.50 | Mid-shape; meaning re-maps per type but the macro is held fixed |
| 5 | Engine A | `A Osc Tone` (macro 2) | 0.50 | Mid-tone; held fixed across all three |
| 6 | Engine A | `A Transpose` | 0 | (no offset) |
| 7 | Engine A | `A Detune` | 0.50 (0 cents) | Centered tuning |
| 8 | Engine A | `A Filter On` | On (1) | (routing) |
| 9 | Engine A | `A Filter Type` | **0 = Analog** | Transparent filter in line |
| 10 | Engine A | `A Filter L-B-H-N` | 0.0 (lowpass) | Lowpass response |
| 11 | Engine A | `A Filter Freq` | 1.0 (open) | Uncolored — must NOT color the type contrast |
| 12 | Engine A | `A Filter Q` | 0.0 | No resonance |
| 13 | Engine A | `A Amp Attack` | 0.05 | Fast note start |
| 14 | Engine A | `A Amp Sustain` | 1.0 | Holds at full level |
| 15 | Engine A | `A Amp Release` | 0.20 | Short tail |
| 16 | Engine A | `A Volume` | 0.70 | Solid level |

**A/B/C (hold `C3` each, beat of silence between):**
- **A:** `A Osc Type` = **0 = Basic Shapes** — a clean shape.
- **B:** `A Osc Type` = **9 = Harmonic FM** — a metallic FM instrument.
- **C:** `A Osc Type` = **12 = Rain** — a noisy synthesized-weather instrument.

**Final check:** same pitch and loudness all three; each segment is an audibly different instrument (clean shape → metallic FM → noisy weather).
**Analyzer:** the three segments have measurably distinct spectra (centroid / harmonicity) at identical f0.

**Save:** save segment A (Type 0) → right-click Meld → **Save Preset** → `presets/meld-type-switch-live.adv`.
