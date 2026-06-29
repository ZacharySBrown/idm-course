# Patch tutorial — `op-poly-bell-step2`  (Polynomial-Bell, Step 2 of 8)

**Preset:** `presets/op-poly-bell-step2.adv`  ·  **Concept:** The carrier (A) — give it a pluck envelope  ·  **Used in slide:** `05b-carrier`

> Step 2. Configure the carrier (A) with a standard pluck shape: fast attack, ~400 ms decay
> to silence, short release. Level is pulled down to leave headroom for the modulators to come.
>
> **You should hear:** a pure-sine **pluck** — instant onset, decays to silence in under half a
> second. Still no FM character; just a shaped sine.

Build from a **freshly loaded Operator** (init). One parameter per step.
Envelope columns use the script's by-ear ms targets (Operator's 0–1 normalized fields are
non-linear; the manifest stores the normalized equivalent in parentheses).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack) | No change yet — routing only |
| 2 | Osc A | On | On | Default sine carrier |
| 3 | Osc A | Wave | Sine | Pure sine |
| 4 | Osc A | Coarse | 1 | Carrier at the played pitch |
| 5 | Osc A | Fine | 0 | No detune |
| 6 | Osc A | Level | −12 dB (manifest norm 0.75) | Quieter sine — headroom for later operators |
| 7 | Osc A | Env Attack | 1 ms (norm 0.01) | Instant onset |
| 8 | Osc A | Env Decay | 400 ms (norm 0.40) | Sine falls away over ~0.4 s |
| 9 | Osc A | Env Sustain | −inf (0.0) | Goes fully silent after the decay |
| 10 | Osc A | Env Release | 200 ms (norm 0.30) | Short tail on note-off |
| 11 | Osc B | On | Off | Still a pure-sine pluck |
| 12 | Osc C | On | Off | (unused) |
| 13 | Osc D | On | Off | (unused) |

**Final check:** a clean sine **pluck** — fast in, decays to silence in ~0.4 s. No bell yet.

_To persist: right-click the Operator title bar → **Save Preset** → save as
`op-poly-bell-step2` into the episode's `presets/` folder._
