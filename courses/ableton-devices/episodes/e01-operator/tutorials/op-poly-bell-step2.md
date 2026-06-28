# Patch tutorial — `op-poly-bell-step2`

**Preset:** `presets/op-poly-bell-step2.adv`  ·  **Concept:** _(add concept)_

> Step 1 + carrier (A) ADSR shape: A=1ms, D=400ms, S=-inf, R=200ms. Coarse 1, Fine 0, Level -12dB. Pure sine pluck.


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
| 6 | Osc A | Level | 0.75  *(0–1 ≈ 75%)* |  |
| 7 | Osc A | Feedback | 0 |  |
| 8 | Osc A | Env Attack | 0.01  *(norm 0–1; set by ear)* |  |
| 9 | Osc A | Env Decay | 0.4  *(norm 0–1; set by ear)* |  |
| 10 | Osc A | Env Sustain | 0  *(norm 0–1; set by ear)* |  |
| 11 | Osc A | Env Release | 0.3  *(norm 0–1; set by ear)* |  |
| 12 | Osc B | On/Off | Off |  |
| 13 | Osc C | On/Off | Off |  |
| 14 | Osc D | On/Off | Off |  |

_Final check: it should match the preset and the demo render._
_To persist: in Live, right-click the Operator title bar → **Save Preset** → save as `op-poly-bell-step2` into the episode's `presets/` folder._
