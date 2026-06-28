# Patch tutorial — `op-feedback-bifurcation`

**Preset:** `presets/op-feedback-bifurcation.adv`  ·  **Concept:** Feedback → progressive harmonic complexity

> Single operator A, sine, full sustain. Feedback should sweep 0→high.
>
> **You should hear:** A pure sine roughening into a saw-like buzz as self-feedback increases.

Build from a **freshly loaded Operator** (init). One parameter per step;
the right column is your self-check.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 |  |
| 2 | Osc A | On/Off | On |  |
| 3 | Osc A | Wave | Sine |  |
| 4 | Osc A | Coarse | 1 |  |
| 5 | Osc A | Fine | 0 |  |
| 6 | Osc A | Level | 1  *(0–1 ≈ 100%)* |  |
| 7 | Osc A | Feedback | 0 |  |
| 8 | Osc A | Env Mode | None |  |
| 9 | Osc A | Env Attack | 0  *(norm 0–1; set by ear)* |  |
| 10 | Osc A | Env Decay | 1  *(norm 0–1; set by ear)* |  |
| 11 | Osc A | Env Sustain | 1  *(norm 0–1; set by ear)* |  |
| 12 | Osc A | Env Release | 0.3  *(norm 0–1; set by ear)* |  |
| 13 | Osc B | On/Off | Off |  |
| 14 | Osc C | On/Off | Off |  |
| 15 | Osc D | On/Off | Off |  |

_Final check: it should match the preset and the demo render._
_To persist: in Live, right-click the Operator title bar → **Save Preset** → save as `op-feedback-bifurcation` into the episode's `presets/` folder._
