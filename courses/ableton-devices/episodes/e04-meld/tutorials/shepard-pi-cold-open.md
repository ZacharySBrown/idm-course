# Patch: Shepard's Pi Cold Open  (preset: presets/shepard-pi-cold-open.adv)

**Demo:** `shepard-pi-cold-open`  ·  **Slide:** `01-cold-open`  ·  **Structure:** single
**Concept demonstrated:** a whole psychoacoustic illusion (endless-rising barberpole) is ONE oscillator type, one knob — the cold-open hook.
**Render status:** FULLY RENDERABLE headless. No matrix, no MPE. The rise is intrinsic to the oscillator.

Build from a **freshly loaded default Meld** (Engine A on, Engine B on, both Basic Shapes). One parameter per step. The "you should now hear" column is your self-check.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain saw/analog tone on each note (Engine A + B both Basic Shapes) |
| 1 | Engine B | `B On` | Off (0) | Engine B silent — we work in Engine A alone |
| 2 | Engine A | `A On` | On (1) | Engine A is the only voice |
| 3 | Engine A | `A Osc Type` | **13 = Shepard's Pi** (numeric index; enum string does not resolve over LOM) | The held note now seems to climb forever and never arrives |
| 4 | Engine A | `A Osc Shape` (macro 1 = Rate) | 0.20 | A slow, gentle rate of endless rise |
| 5 | Engine A | `A Osc Tone` (macro 2 = Width) | 0.50 | A balanced band of partials in the barberpole |
| 6 | Engine A | `A Transpose` | 0 | (no pitch offset) |
| 7 | Engine A | `A Detune` | 0.50 (= 0 cents) | Unchanged — centered tuning |
| 8 | Engine A | `A Filter On` | On (1) | (routing only) |
| 9 | Engine A | `A Filter Type` | **0 = Analog** | A transparent analog filter in line |
| 10 | Engine A | `A Filter L-B-H-N` | 0.0 (lowpass end of morph) | Lowpass response selected |
| 11 | Engine A | `A Filter Freq` | 1.0 (fully open) | Bright, uncolored — filter not shaping the rise |
| 12 | Engine A | `A Filter Q` | 0.0 | No resonant emphasis |
| 13 | Engine A | `A Amp Attack` | 0.30 | A gentle fade-in on each note |
| 14 | Engine A | `A Amp Sustain` | 1.0 | The note holds at full level |
| 15 | Engine A | `A Amp Release` | 0.50 | A soft tail when the key lifts |
| 16 | Engine A | `A Volume` | 0.70 | Solid audible level |
| 17 | Global | `Drive` | 0.0 | Clean, no saturation |
| 18 | Global | `Limiter On` | On (1) | Peaks caught; safe output for the cold-open hook |

**Play:** one held note `C2` for ~8.5 s.

**Final check:** a continuous sense of upward motion with no audible octave reset — the pitch class never "lands."
**Analyzer:** spectral centroid drifts upward continuously/cyclically with NO discrete octave jump.

**Save:** right-click the Meld title bar → **Save Preset** → `presets/shepard-pi-cold-open.adv`.
