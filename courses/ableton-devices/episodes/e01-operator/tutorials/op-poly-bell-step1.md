# Patch tutorial — `op-poly-bell-step1`  (Polynomial-Bell, Step 1 of 8)

**Preset:** `presets/op-poly-bell-step1.adv`  ·  **Concept:** Algorithm 1, all sines — the blank canvas  ·  **Used in slide:** `05a-algo1`

> Step 1 of the Polynomial-Bell build. Open Operator, pick Algorithm 1 (the linear stack
> D→C→B→A), every operator a sine, defaults otherwise. Nothing is modulating anything yet.
>
> **You should hear:** a pure, unmodulated sine — a held C3 with no FM character at all. This
> is the reference the next seven steps build on.

Build from a **freshly loaded Operator** (init). One parameter per step.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack D→C→B→A) | No change yet — routing only |
| 2 | Osc A | On | On | Default sine carrier |
| 3 | Osc A | Wave | Sine | Pure sine |
| 4 | Osc A | Coarse | 1 | Carrier at the played pitch (C3) |
| 5 | Osc A | Fine | 0 | No detune |
| 6 | Osc A | Level | 1.0 (0 dB) | Full-level sine |
| 7 | Osc A | Env Mode | None | Sustains while held |
| 8 | Osc A | Env Attack / Decay / Sustain / Release | 0.0 / 1.0 / 1.0 / 0.30 | Held, steady sine |
| 9 | Osc B | On | Off | Still just the sine (no modulator) |
| 10 | Osc C | On | Off | (unused) |
| 11 | Osc D | On | Off | (unused) |

**Final check:** a clean, held sine on C3 — no buzz, no bell, nothing inharmonic. If you hear
any edge, an operator other than A is still on.

_To persist: right-click the Operator title bar → **Save Preset** → save as
`op-poly-bell-step1` into the episode's `presets/` folder._
