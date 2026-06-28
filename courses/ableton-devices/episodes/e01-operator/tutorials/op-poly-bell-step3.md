# Patch tutorial — `op-poly-bell-step3`

**Preset:** `presets/op-poly-bell-step3.adv`  ·  **Concept:** _(add concept)_

> Step 2 + modulator B: Coarse 1, Fine 414 (≈√2), Level 80%. Envelope A=1ms D=120ms S=-inf R=80ms. Bell-like inharmonic ringing emerges.


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
| 12 | Osc B | On/Off | On |  |
| 13 | Osc B | Wave | Sine |  |
| 14 | Osc B | Coarse | 1 |  |
| 15 | Osc B | Fine | 414 |  |
| 16 | Osc B | Level | 0.8  *(0–1 ≈ 80%)* |  |
| 17 | Osc B | Feedback | 0 |  |
| 18 | Osc B | Env Attack | 0.01  *(norm 0–1; set by ear)* |  |
| 19 | Osc B | Env Decay | 0.15  *(norm 0–1; set by ear)* |  |
| 20 | Osc B | Env Sustain | 0  *(norm 0–1; set by ear)* |  |
| 21 | Osc B | Env Release | 0.1  *(norm 0–1; set by ear)* |  |
| 22 | Osc C | On/Off | Off |  |
| 23 | Osc D | On/Off | Off |  |

_Final check: it should match the preset and the demo render._
_To persist: in Live, right-click the Operator title bar → **Save Preset** → save as `op-poly-bell-step3` into the episode's `presets/` folder._
