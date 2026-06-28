# Patch tutorial — `op-ratio-1to2`

**Preset:** `presets/op-ratio-1to2.adv`  ·  **Concept:** _(add concept)_

> Same as 1to1 but B Coarse=2. Hollow-clarinet odd-harmonic spectrum.


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
| 13 | Osc B | On/Off | On |  |
| 14 | Osc B | Wave | Sine |  |
| 15 | Osc B | Coarse | 2 |  |
| 16 | Osc B | Fine | 0 |  |
| 17 | Osc B | Level | 0.8  *(0–1 ≈ 80%)* |  |
| 18 | Osc B | Feedback | 0 |  |
| 19 | Osc B | Env Mode | None |  |
| 20 | Osc B | Env Attack | 0  *(norm 0–1; set by ear)* |  |
| 21 | Osc B | Env Decay | 1  *(norm 0–1; set by ear)* |  |
| 22 | Osc B | Env Sustain | 1  *(norm 0–1; set by ear)* |  |
| 23 | Osc B | Env Release | 0.3  *(norm 0–1; set by ear)* |  |
| 24 | Osc C | On/Off | Off |  |
| 25 | Osc D | On/Off | Off |  |

_Final check: it should match the preset and the demo render._
_To persist: in Live, right-click the Operator title bar → **Save Preset** → save as `op-ratio-1to2` into the episode's `presets/` folder._
