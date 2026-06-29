# Patch: Two-Hands — Step 1: Engine A Swarm Saw  (preset: presets/meld-twohands-step1.adv)

**Demo:** `meld-twohands-step1`  ·  **Slide:** `05a-engine-a-swarm`  ·  **Structure:** single (build-step)
**Concept demonstrated:** Step 1 of the "Two-Hands" patch — Engine A: Swarm Saw, scale-locked — the anthemic body. Nothing else on yet.
**Render status:** FULLY RENDERABLE headless. No matrix, no MPE.
**Orchestrator note:** set the Live Set's Scale (e.g. C Minor) before render so the scale-aware swarm snaps in key.

Build from a **freshly loaded default Meld**. One parameter per step.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine B | `B On` | Off (0) | Engine B silent — Engine A is the only layer |
| 2 | Engine A | `A On` | On (1) | Engine A only |
| 3 | Engine A | `A Osc Type` | **19 = Swarm Saw** (scale-aware ♭♯) | A wide supersaw-style swarm |
| 4 | Engine A | `A Osc Shape` (macro 1 = Motion) | 0.30 | A gentle internal motion in the swarm |
| 5 | Engine A | `A Osc Tone` (macro 2 = Spacing) | 0.40 | A medium spread across the swarm |
| 6 | Engine A | `A Osc Scale Aware` | On (1) | The swarm's partials lock to the scale — in-key |
| 7 | Engine A | `A Filter On` | On (1) | (routing) |
| 8 | Engine A | `A Filter Type` | **0 = Analog** | A musical analog filter in line |
| 9 | Engine A | `A Filter L-B-H-N` | 0.0 (lowpass) | Lowpass response |
| 10 | Engine A | `A Filter Freq` | 0.55 | A gentle low-pass — warm, not harsh |
| 11 | Engine A | `A Filter Q` | 0.10 | A touch of resonant body |
| 12 | Engine A | `A Amp Attack` | 0.05 | Fast note start |
| 13 | Engine A | `A Amp Sustain` | 0.90 | Holds near full |
| 14 | Engine A | `A Amp Release` | 0.40 | A soft tail |
| 15 | Engine A | `A Volume` | 0.65 | Solid chord level with headroom |
| 16 | Global | `Scale Aware` (device master enable) | On (1) | Master scale-snap on (set Set Scale to C Minor) |

**Play:** hold the chord `C3 + G3` for ~3.6 s.

**Final check:** a wide in-key saw body; no FM layer, no resonator, no modulation yet.
**Analyzer:** dense saw-swarm comb quantized to scale degrees; single engine only.

**Save:** right-click Meld → **Save Preset** → `presets/meld-twohands-step1.adv`.
