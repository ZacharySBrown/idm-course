# Patch tutorial — `op-poly-bell-step4`  (Polynomial-Bell, Step 4 of 8)

**Preset:** `presets/op-poly-bell-step4.adv`  ·  **Concept:** Modulator C feeding B — high shimmer on the front of the attack  ·  **Used in slide:** `05d-modulator-c`

> Step 4. In Algorithm 1's linear stack (D→C→B→A), **C already modulates B**. Configure C at
> **Coarse 7** (seven times the carrier) with an even shorter envelope — a high-frequency
> shimmer painted across the very front of B's envelope.
>
> **You should hear:** the bell from Step 3 plus a brief, bright high-frequency **sparkle** at
> the onset.

> ⚠️ **Topology check:** Algorithm 1 is the linear stack, so C → B is correct. If, on audition,
> C audibly hits the carrier (A) instead of B, you are on the wrong algorithm — reselect
> Alg. 1 from the algorithm diagram (C must sit *above* B in the stack).

Build from a **freshly loaded Operator** (init). One parameter per step. (Carrier + B repeat
Step 3; the new work is the Osc C block.)

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack D→C→B→A) | Routing — C sits above B |
| 2 | Osc A | On / Wave / Coarse / Fine / Level | On / Sine / 1 / 0 / −12 dB | Carrier ready |
| 3 | Osc A | Env A / D / S / R | 1 ms / 400 ms / −inf / 200 ms | Pure-sine pluck |
| 4 | Osc B | On / Wave / Coarse / Fine / Level | On / Sine / 1 / 414 (√2) / 0.8 | Bell shimmer (Step 3) |
| 5 | Osc B | Env A / D / S / R | 1 ms / 120 ms / −inf / 80 ms | Short metallic attack |
| 6 | Osc C | On | On | A bright sparkle joins the onset |
| 7 | Osc C | Wave | Sine | Clean high sidebands |
| 8 | Osc C | **Coarse** | **7** | C at ×7 the carrier — high shimmer feeding B |
| 9 | Osc C | Fine | 0 | No detune on C |
| 10 | Osc C | Level | 0.5 (≈ 50%) | Adds high-frequency shimmer to B's attack |
| 11 | Osc C | Feedback | 0 | (added next step) |
| 12 | Osc C | Env Attack | 1 ms (norm 0.01) | Instant sparkle |
| 13 | Osc C | Env Decay | 60 ms (norm 0.08) | Sparkle gone fastest of the three — front-of-attack only |
| 14 | Osc C | Env Sustain | −inf (0.0) | No sustained shimmer |
| 15 | Osc C | Env Release | 60 ms (norm 0.08) | Very short tail |
| 16 | Osc D | On | Off | (unused) |

**Final check:** the Step-3 bell plus a brief high sparkle right at the onset. The sparkle
should be gone well before the bell body decays.

_To persist: right-click the Operator title bar → **Save Preset** → save as
`op-poly-bell-step4` into the episode's `presets/` folder._
