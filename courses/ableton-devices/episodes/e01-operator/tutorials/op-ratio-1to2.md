# Patch tutorial — `op-ratio-1to2`

**Preset:** `presets/op-ratio-1to2.adv`  ·  **Concept:** Ratio → spectrum — **1:2 integer** (hollow/clarinet)  ·  **Used in slide:** `03c-ratios`

> Identical to `op-ratio-1to1` except **B Coarse = 2** (modulator an octave above the
> carrier). Ratio is the ONLY change. A 1:2 ratio emphasises octave-spaced sidebands — a
> hollow, clarinet-like color.
>
> **You should hear:** a held C3, still clearly pitched but *hollow* — clarinet-like, the
> energy sitting in widely-spaced harmonics.

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
| 10 | Osc B | On | On | A hollow edge appears |
| 11 | Osc B | Wave | Sine | Clean sidebands |
| 12 | Osc B | **Coarse** | **2** | **1:2 ratio — hollow, clarinet-like** |
| 13 | Osc B | Fine | 0 | Exact integer ratio |
| 14 | Osc B | Level | 0.8 (≈ 80%, fixed index) | Steady brightness (the controlled constant) |
| 15 | Osc B | Feedback | 0 | No self-modulation |
| 16 | Osc B | Env Mode | None | Brightness holds for the whole note |
| 17 | Osc B | Env Attack / Decay / Sustain / Release | 0.0 / 1.0 / 1.0 / 0.30 | Constant index, no sweep |
| 18 | Osc C | On | Off | (unused) |
| 19 | Osc D | On | Off | (unused) |

**Final check:** a sustained, hollow, clarinet-like tone — still pitched. Spectrum: integer
harmonic comb, weighted toward octave-spaced partials.

**Verification (Gate 7):** `ratio` — peaks fall on an integer harmonic comb of f0 (pitched).

_To persist: right-click the Operator title bar → **Save Preset** → save as `op-ratio-1to2`
into the episode's `presets/` folder._
