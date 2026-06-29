# Patch: Two-Hands — Step 2: Engine B FM + Plate Resonator  (preset: presets/meld-twohands-step2.adv)

**Demo:** `meld-twohands-step2`  ·  **Slide:** `05b-engine-b-fm-resonator`  ·  **Structure:** single (build-step)
**Concept demonstrated:** Step 2 — add Engine B: Harmonic FM an octave up → Plate Resonator (the one filter that's "physical modelling"). "It's a filter, not the oscillator."
**Render status:** RENDERABLE headless. No matrix, no MPE.
**⚠ PLACEHOLDER ENUM INDEX — NEEDS LIVE CONFIRMATION:** `B Filter Type` Plate Resonator is a **PLACEHOLDER = 15** (EMPTY value_items, no doc ordering). Confirm the live index before render/save. This same index carries into steps 3/4/5/6/final.

Continue from Step 1 (Engine A unchanged). Re-state Engine A explicitly (the renderer does not carry forward), then add Engine B.

### Engine A — unchanged from Step 1
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 1 | Engine A | `A On` | On (1) | Engine A body present |
| 2 | Engine A | `A Osc Type` | **19 = Swarm Saw** | The in-key saw swarm |
| 3 | Engine A | `A Osc Shape` (Motion) | 0.30 | Gentle motion |
| 4 | Engine A | `A Osc Tone` (Spacing) | 0.40 | Medium spread |
| 5 | Engine A | `A Osc Scale Aware` | On (1) | In-key |
| 6 | Engine A | `A Filter On` / `A Filter Type` / `A Filter L-B-H-N` | On / **0 = Analog** / 0.0 (lowpass) | Warm analog low-pass |
| 7 | Engine A | `A Filter Freq` / `A Filter Q` | 0.55 / 0.10 | Gentle low-pass with a little body |
| 8 | Engine A | `A Volume` | 0.65 | Chord-level body |

### Engine B — the added element
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 9 | Engine B | `B On` | On (1) | A second engine joins |
| 10 | Engine B | `B Osc Type` | **9 = Harmonic FM** | A glassy FM overtone layer |
| 11 | Engine B | `B Osc Shape` (macro 1 = FM Amount) | 0.50 | A bright FM amount |
| 12 | Engine B | `B Osc Tone` (macro 2 = FM Ratio) | 0.40 | A metallic ratio |
| 13 | Engine B | `B Octave` | **1** (octave up; `B Transpose` maxes ±12 semitones, so use Octave) | The FM layer sits an octave above the body |
| 14 | Engine B | `B Filter On` | On (1) | (routing) |
| 15 | Engine B | `B Filter Type` | **Plate Resonator (PLACEHOLDER idx 15 — CONFIRM LIVE)** | A struck, body-resonant, metallic shimmer on the FM layer |
| 16 | Engine B | `B Filter Filter Scale Aware` | On (1) | The plate modes snap into key |
| 17 | Engine B | `B Filter Freq` | 0.50 (resonator pitch) | Sets the resonator's tuning |
| 18 | Engine B | `B Filter Q` | 0.55 (resonator decay) | A ringing, sustained shimmer |
| 19 | Engine B | `B Amp Attack` | 0.02 | A struck attack on the layer |
| 20 | Engine B | `B Amp Decay` | 0.50 | A decaying ring |
| 21 | Engine B | `B Amp Sustain` | 0.40 | Low sustain — a layer, not the lead |
| 22 | Engine B | `B Amp Release` | 0.40 | A short ring-out |
| 23 | Engine B | `B Volume` | 0.40 | Low level — sits under the body |
| 24 | Global | `Scale Aware` | On (1) | Master scale-snap on |

**Play:** hold `C3 + G3` for ~3.6 s.

**Final check:** Step 1's saw body PLUS a new high glassy resonant layer; differs from Step 1 by exactly the Engine B layer.
**Analyzer:** Step 1 spectrum + added discrete modal peaks an octave up (Plate Resonator).

**Save:** with the confirmed Plate index set, right-click Meld → **Save Preset** → `presets/meld-twohands-step2.adv`.
