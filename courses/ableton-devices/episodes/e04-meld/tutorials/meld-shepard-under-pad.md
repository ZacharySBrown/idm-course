# Patch: Shepard Under Pad (the Cold-Open Trick, Put to Work)  (preset: presets/meld-shepard-under-pad.adv)

**Demo:** `meld-shepard-under-pad`  ·  **Slide:** `06c-shepard-trick`  ·  **Structure:** single
**Concept demonstrated:** the cold-open Shepard's Pi oscillator, put to work — an endless build for IDM tension under a sustained pad.
**Render status:** FULLY RENDERABLE headless. No matrix needed — the Shepard rise is intrinsic to the oscillator; Engine B is a static pad.

Build from a **freshly loaded default Meld**. One parameter per step. Engine A = the Shepard build, Engine B = the pad.

### Engine A — Shepard's Pi (the build)
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine A | `A On` | On (1) | Engine A present |
| 2 | Engine A | `A Osc Type` | **13 = Shepard's Pi** | A tone that seems to climb forever |
| 3 | Engine A | `A Osc Shape` (macro 1 = Rate) | 0.25 | A slow, steady rate of endless rise |
| 4 | Engine A | `A Osc Tone` (macro 2 = Width) | 0.50 | A balanced band of partials |
| 5 | Engine A | `A Filter On` / `A Filter Type` / `A Filter L-B-H-N` | On / **0 = Analog** / 0.0 | Transparent lowpass |
| 6 | Engine A | `A Filter Freq` | 0.80 | A gently tamed top on the build |
| 7 | Engine A | `A Amp Attack` | 0.30 | A gentle fade-in |
| 8 | Engine A | `A Amp Sustain` | 1.0 | Holds at full level |
| 9 | Engine A | `A Amp Release` | 0.60 | A soft tail |
| 10 | Engine A | `A Volume` | 0.50 | The build sits under the pad |

### Engine B — Basic Shapes pad (the bed)
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 11 | Engine B | `B On` | On (1) | A warm pad joins under the rise |
| 12 | Engine B | `B Osc Type` | **0 = Basic Shapes** | A warm analog pad |
| 13 | Engine B | `B Osc Shape` (macro 1) | 0.40 | A soft shape |
| 14 | Engine B | `B Osc Tone` (macro 2) | 0.50 | A neutral tone |
| 15 | Engine B | `B Filter On` / `B Filter Type` / `B Filter L-B-H-N` | On / **0 = Analog** / 0.0 | Lowpass on the pad |
| 16 | Engine B | `B Filter Freq` | 0.50 | A warm, rounded pad |
| 17 | Engine B | `B Amp Attack` | 0.50 | A slow pad swell |
| 18 | Engine B | `B Amp Sustain` | 1.0 | Holds at full level |
| 19 | Engine B | `B Amp Release` | 0.80 | A long pad tail |
| 20 | Engine B | `B Volume` | 0.60 | A steady pad bed |
| 21 | Global | `Limiter On` | On (1) | Peaks caught |

**Play:** hold `C2` (Engine A build) and `C3` (Engine B pad) together for ~8.5 s.

**Final check:** a continuous sense of rising tension under a steady pad; the rise never lands.
**Analyzer:** Engine A centroid drifts upward continuously with no octave reset, over Engine B's steady pad spectrum.

**Save:** right-click Meld → **Save Preset** → `presets/meld-shepard-under-pad.adv`.
