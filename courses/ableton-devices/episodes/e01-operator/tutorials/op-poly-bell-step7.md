# Patch tutorial — `op-poly-bell-step7`

**Preset:** `presets/op-poly-bell-step7.adv`  ·  **Concept:** _(add concept)_

> Step 6 + velocity routing: Osc-B Lev < Vel = +50 (LOM scale). Two notes: soft (vel 30) at t=0, hard (vel 110) at t=3.


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
| 18 | Osc B | Level<Vel | 50 |  |
| 19 | Osc B | Env Attack | 0.01  *(norm 0–1; set by ear)* |  |
| 20 | Osc B | Env Decay | 0.15  *(norm 0–1; set by ear)* |  |
| 21 | Osc B | Env Sustain | 0  *(norm 0–1; set by ear)* |  |
| 22 | Osc B | Env Release | 0.1  *(norm 0–1; set by ear)* |  |
| 23 | Osc C | On/Off | On |  |
| 24 | Osc C | Wave | Sine |  |
| 25 | Osc C | Coarse | 7 |  |
| 26 | Osc C | Fine | 0 |  |
| 27 | Osc C | Level | 0.5  *(0–1 ≈ 50%)* |  |
| 28 | Osc C | Feedback | 30 |  |
| 29 | Osc C | Env Attack | 0.01  *(norm 0–1; set by ear)* |  |
| 30 | Osc C | Env Decay | 0.08  *(norm 0–1; set by ear)* |  |
| 31 | Osc C | Env Sustain | 0  *(norm 0–1; set by ear)* |  |
| 32 | Osc C | Env Release | 0.08  *(norm 0–1; set by ear)* |  |
| 33 | Osc D | On/Off | Off |  |
| 34 | Global | Spread | 12 |  |
| 35 | Global | Filter On | On |  |
| 36 | Global | Filter Type | Lowpass |  |
| 37 | Global | Filter Slope | 24 dB |  |
| 38 | Global | Filter Circuit | OSR |  |
| 39 | Global | Filter Freq | 0.85 |  |
| 40 | Global | Filter Drive | 3 |  |

_Final check: it should match the preset and the demo render._
_To persist: in Live, right-click the Operator title bar → **Save Preset** → save as `op-poly-bell-step7` into the episode's `presets/` folder._
