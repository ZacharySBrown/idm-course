# Patch tutorial — `op-ratio-1to1`

**Preset:** `presets/op-ratio-1to1.adv`  ·  **Concept:** Ratio → spectrum — **1:1 integer** (reedy/sawtooth)  ·  **Used in slide:** `03c-ratios`

> Algorithm 1, A and B both sine, B Level fixed at ~80% (constant index). Ratio is the ONLY
> variable across the five `op-ratio-*` demos — carrier, depth, note, and envelopes are held.
> Here B Coarse = 1: the modulator sits at the carrier pitch.
>
> **You should hear:** a held C3 that is clearly *pitched* — reedy, sawtooth-like, full
> harmonic series (sidebands land on integer harmonics of the fundamental).

Build from a **freshly loaded Operator** (init). One parameter per step.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack) | No change yet — routing only |
| 2 | Osc A | On | On | Default sine |
| 3 | Osc A | Wave | Sine | Pure sine carrier |
| 4 | Osc A | Coarse | 1 | Carrier at the played pitch |
| 5 | Osc A | Fine | 0 | No detune |
| 6 | Osc A | Level | 1.0 (0 dB) | Carrier full |
| 7 | Osc A | Feedback | 0 | Clean sine |
| 8 | Osc A | Env Mode | None | Sustains while held |
| 9 | Osc A | Env Attack / Decay / Sustain / Release | 0.0 / 1.0 / 1.0 / 0.30 | Instant, steady, ~200 ms tail |
| 10 | Osc B | On | On | A reedy edge appears over the sine |
| 11 | Osc B | Wave | Sine | Clean sidebands |
| 12 | Osc B | **Coarse** | **1** | **1:1 ratio — pitched, reedy/sawtooth-like** |
| 13 | Osc B | Fine | 0 | Exact integer ratio (no detune) |
| 14 | Osc B | Level | 0.8 (≈ 80%, fixed index) | Steady brightness (the controlled constant) |
| 15 | Osc B | Feedback | 0 | No self-modulation |
| 16 | Osc B | Env Mode | None | Brightness holds for the whole note |
| 17 | Osc B | Env Attack / Decay / Sustain / Release | 0.0 / 1.0 / 1.0 / 0.30 | Constant index, no sweep |
| 18 | Osc C | On | Off | (unused) |
| 19 | Osc D | On | Off | (unused) |

**Final check:** a sustained, clearly-pitched reedy tone. Spectrum: a full integer harmonic
comb on the C3 fundamental.

**Verification (Gate 7):** `ratio` (ab vs the inharmonic members of the set) — integer
members (1to1/1to2/1to3) show peaks on an integer harmonic comb of f0; √2 and φ do not.

_To persist: right-click the Operator title bar → **Save Preset** → save as `op-ratio-1to1`
into the episode's `presets/` folder._
