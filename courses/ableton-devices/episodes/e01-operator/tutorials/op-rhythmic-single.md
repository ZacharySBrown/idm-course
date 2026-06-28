# Patch tutorial — `op-rhythmic-single`

**Preset:** `presets/op-rhythmic-single.adv`  ·  **Concept:** _(add concept)_

> Algorithm 1, A=Trigger envelope (decay 200ms), B=Beat envelope at 1/16 (Be Retrig=2), B Coarse=11. Hold C3 4 bars at 100 BPM.


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
| 6 | Osc A | Level | 0.8  *(0–1 ≈ 80%)* |  |
| 7 | Osc A | Feedback | 0 |  |
| 8 | Osc A | Env Mode | Beat |  |
| 9 | Osc A | Env Retrig | 2 |  |
| 10 | Osc A | Env Attack | 0  *(norm 0–1; set by ear)* |  |
| 11 | Osc A | Env Decay | 0.12  *(norm 0–1; set by ear)* |  |
| 12 | Osc A | Env Sustain | 0  *(norm 0–1; set by ear)* |  |
| 13 | Osc A | Env Release | 0  *(norm 0–1; set by ear)* |  |
| 14 | Osc B | On/Off | On |  |
| 15 | Osc B | Wave | Sine |  |
| 16 | Osc B | Coarse | 11 |  |
| 17 | Osc B | Fine | 0 |  |
| 18 | Osc B | Level | 0.7  *(0–1 ≈ 70%)* |  |
| 19 | Osc B | Feedback | 0 |  |
| 20 | Osc B | Env Mode | None |  |
| 21 | Osc B | Env Attack | 0  *(norm 0–1; set by ear)* |  |
| 22 | Osc B | Env Decay | 1  *(norm 0–1; set by ear)* |  |
| 23 | Osc B | Env Sustain | 1  *(norm 0–1; set by ear)* |  |
| 24 | Osc B | Env Release | 0  *(norm 0–1; set by ear)* |  |
| 25 | Osc C | On/Off | Off |  |
| 26 | Osc D | On/Off | Off |  |

_Final check: it should match the preset and the demo render._
_To persist: in Live, right-click the Operator title bar → **Save Preset** → save as `op-rhythmic-single` into the episode's `presets/` folder._
