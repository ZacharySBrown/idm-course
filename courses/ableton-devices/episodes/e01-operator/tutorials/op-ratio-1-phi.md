# Patch tutorial — `op-ratio-1-phi`

**Preset:** `presets/op-ratio-1-phi.adv`  ·  **Concept:** Ratio → spectrum — **1 : φ irrational** (Stria cloud)  ·  **Used in slide:** `03c-ratios`

> Identical to `op-ratio-1to1` except the modulator is detuned to the **golden ratio**:
> **B Coarse = 1, B Fine = 618**, pushing B to ≈ 1.618× the carrier (φ). This is the exact
> inharmonic territory Chowning used in *Stria* (1977).
>
> **You should hear:** a held C3 as a shimmering, glassy inharmonic cloud — more diffuse than
> the √2 bell, no pitch center.

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
| 10 | Osc B | On | On | A shimmering edge appears |
| 11 | Osc B | Wave | Sine | Clean sidebands |
| 12 | Osc B | **Coarse** | **1** | Base ratio 1:1 before the fine detune |
| 13 | Osc B | **Fine** | **618** | **≈ ×1.618 (φ, golden ratio) — irrational; *Stria*-cloud inharmonic** |
| 14 | Osc B | Level | 0.8 (≈ 80%, fixed index) | Steady brightness (the controlled constant) |
| 15 | Osc B | Feedback | 0 | No self-modulation |
| 16 | Osc B | Env Mode | None | Inharmonic cloud holds for the whole note |
| 17 | Osc B | Env Attack / Decay / Sustain / Release | 0.0 / 1.0 / 1.0 / 0.30 | Constant index, no sweep |
| 18 | Osc C | On | Off | (unused) |
| 19 | Osc D | On | Off | (unused) |

**Final check:** a sustained, glassy, inharmonic shimmer with no pitch center — *Stria*
territory. Spectrum: partials at **non-integer** (golden-ratio) spacing.

**Verification (Gate 7):** `ratio` — peaks do **not** correlate with an integer harmonic comb
of f0; spacing should also differ measurably from the √2 demo.

_To persist: right-click the Operator title bar → **Save Preset** → save as `op-ratio-1-phi`
into the episode's `presets/` folder._
