# Patch tutorial — `op-ratio-1-sqrt2`

**Preset:** `presets/op-ratio-1-sqrt2.adv`  ·  **Concept:** Ratio → spectrum — **1 : √2 irrational** (bell/gong)  ·  **Used in slide:** `03c-ratios`

> Identical to `op-ratio-1to1` except the modulator is detuned to an **irrational** ratio:
> **B Coarse = 1, B Fine = 414**, which pushes B to ≈ 1.414× the carrier (√2). Sidebands now
> fall *off* the harmonic grid — the ear stops hearing a note and hears an *object*.
>
> **You should hear:** a held C3 that no longer reads as a pitch but as a struck **bell/gong**
> — metallic, detuned, inharmonic partials.

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
| 10 | Osc B | On | On | A metallic edge appears |
| 11 | Osc B | Wave | Sine | Clean sidebands |
| 12 | Osc B | **Coarse** | **1** | Base ratio 1:1 before the fine detune |
| 13 | Osc B | **Fine** | **414** | **≈ ×1.414 (√2) — irrational; inharmonic bell/gong** |
| 14 | Osc B | Level | 0.8 (≈ 80%, fixed index) | Steady brightness (the controlled constant) |
| 15 | Osc B | Feedback | 0 | No self-modulation |
| 16 | Osc B | Env Mode | None | Inharmonic ring holds for the whole note |
| 17 | Osc B | Env Attack / Decay / Sustain / Release | 0.0 / 1.0 / 1.0 / 0.30 | Constant index, no sweep |
| 18 | Osc C | On | Off | (unused) |
| 19 | Osc D | On | Off | (unused) |

**Final check:** a sustained, metallic, bell/gong-like tone with no clear pitch center.
Spectrum: partials at **non-integer** spacing (off the harmonic comb).

**Verification (Gate 7):** `ratio` — this segment's peaks do **not** correlate with an integer
harmonic comb of f0 (irregular spacing). If it reads pitched, the Fine detune didn't take ⇒ reject.

_To persist: right-click the Operator title bar → **Save Preset** → save as `op-ratio-1-sqrt2`
into the episode's `presets/` folder._
