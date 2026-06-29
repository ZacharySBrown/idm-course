# Patch: One Knob, Three Worlds  (preset: presets/meld-one-knob-three-worlds.adv)

**Demo:** `meld-one-knob-three-worlds`  ·  **Slide:** `02a-what-a-macro-osc-is`  ·  **Structure:** ladder
**Concept demonstrated:** the macro-oscillator promise — ONE macro knob sweeps a whole behavior, and switching the TYPE hands you a whole new instrument. Breadth from two knobs.
**Render status:** RENDERABLE headless (rendered as a split render: one segment per `A Osc Type` value, with `A Osc Shape` automated across segment 1). No matrix, no MPE.

Build from a **freshly loaded default Meld**. One parameter per step. This patch is the **base state**; the demo then (a) sweeps `A Osc Shape` 0→1 across segment 1, and (b) switches `A Osc Type` to 9, then 12 for segments 2 and 3.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine B | `B On` | Off (0) | Engine B silent |
| 2 | Engine A | `A On` | On (1) | Engine A is the only voice |
| 3 | Engine A | `A Osc Type` | **0 = Basic Shapes** | A clean analog shape — the segment-1 starting world |
| 4 | Engine A | `A Osc Shape` (macro 1 = Shape) | 0.0 (base; swept 0→1 in seg 1) | Sine at 0.0 → saw → square as it sweeps up |
| 5 | Engine A | `A Osc Tone` (macro 2 = Tone) | 0.50 | A neutral tone setting held across all three worlds |
| 6 | Engine A | `A Transpose` | 0 | (no offset) |
| 7 | Engine A | `A Detune` | 0.50 (0 cents) | Centered tuning |
| 8 | Engine A | `A Filter On` | On (1) | (routing) |
| 9 | Engine A | `A Filter Type` | **0 = Analog** | Transparent analog filter in line |
| 10 | Engine A | `A Filter L-B-H-N` | 0.0 (lowpass) | Lowpass response |
| 11 | Engine A | `A Filter Freq` | 1.0 (open) | Uncolored — the filter must NOT mask the type contrast |
| 12 | Engine A | `A Filter Q` | 0.0 | No resonance |
| 13 | Engine A | `A Amp Attack` | 0.05 | Fast, clean note start |
| 14 | Engine A | `A Amp Sustain` | 1.0 | Note holds at full level |
| 15 | Engine A | `A Amp Release` | 0.20 | Short tail |
| 16 | Engine A | `A Volume` | 0.70 | Solid audible level |

**Ladder / automation:**
- **World 1 (Basic Shapes):** hold `C3`; sweep `A Osc Shape` 0.0 → 1.0 over ~2.5 s. *Sine opens into saw into square.*
- **World 2 (Harmonic FM):** set `A Osc Type` = **9 = Harmonic FM**; hold `C3`. *A metallic FM instrument — different world, same key.*
- **World 3 (Rain):** set `A Osc Type` = **12 = Rain**; hold `C3`. *A noisy synthesized-weather instrument.*

**Final check:** constant pitch and loudness; segment 1 morphs continuously, then two discrete new instruments. Three audibly different worlds.
**Analyzer:** segment-1 centroid rises during the sweep; segments 2 and 3 are measurably distinct spectra at the same f0.

**Save:** save the **base state** (Type 0, Shape 0.0) → right-click Meld → **Save Preset** → `presets/meld-one-knob-three-worlds.adv`.
