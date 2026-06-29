# Patch tutorial — `op-poly-bell-final`  (Polynomial-Bell, Step 8 of 8 — SAVE)

**Preset:** `presets/op-poly-bell-final.adv`  ·  **Concept:** The complete Polynomial-Bell — inharmonic FM bell-pluck (√2 modulator + C-shimmer + feedback + filter)  ·  **Used in slide:** `05h-save`

> Step 8 — the finished patch, played as a demonstration arpeggio (C3–Eb3–G3–C4 sixteenths,
> 4 bars @ 100 BPM). This is the full parameter set from Step 7; the only "step" here is to
> **Save Preset** and name it *Polynomial-Bell*. (Step 7 added velocity→level; this final patch
> is the same patch auditioned across a melodic pattern rather than two held notes.)
>
> **You should hear:** a metallic, detuned bell-pluck arpeggio with a bright gritty attack and a
> sine-like tail — something you could drop into a *Drukqs*-era track.

This is the **single source of truth** patch for the build section. Building it from default
should round-trip with `presets/op-poly-bell-final.adv` (gzip-diff the XML clean).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack D→C→B→A) | Routing only |
| 2 | Osc A | On / Wave | On / Sine | Pure sine carrier |
| 3 | Osc A | Coarse / Fine / Level | 1 / 0 / −12 dB (norm 0.75) | Carrier with headroom |
| 4 | Osc A | Env A / D / S / R | 1 ms / 400 ms / −inf / 200 ms (0.01 / 0.40 / 0.0 / 0.30) | Pure-sine pluck |
| 5 | Osc B | On / Wave | On / Sine | Modulator in |
| 6 | Osc B | Coarse / **Fine** / Level | 1 / **414 (√2)** / 0.8 | Inharmonic bell shimmer |
| 7 | Osc B | Lev < Vel | +50 | Velocity → brightness |
| 8 | Osc B | Env A / D / S / R | 1 ms / 120 ms / −inf / 80 ms (0.01 / 0.15 / 0.0 / 0.10) | Short metallic attack |
| 9 | Osc C | On / Wave | On / Sine | Shimmer modulator (feeds B) |
| 10 | Osc C | Coarse / Level / **Feedback** | 7 / 0.5 / **30%** | High gritty sparkle on the onset |
| 11 | Osc C | Env A / D / S / R | 1 ms / 60 ms / −inf / 60 ms (0.01 / 0.08 / 0.0 / 0.08) | Front-of-attack only |
| 12 | Osc D | On | Off | (unused) |
| 13 | Global | Spread | 12 | Stereo width |
| 14 | Global | Filter On / Type / Slope / Circuit | On / Lowpass / 24 dB / OSR | Analog-warm lowpass |
| 15 | Global | Filter Freq / Drive | ~8 kHz (norm 0.85) / +3 dB | Top rounded, slight warmth |
| 16 | **SAVE** | Right-click title bar → **Save Preset** | name: **Polynomial-Bell** | Patch saved to `presets/op-poly-bell-final.adv` |

**Final check:** a metallic, inharmonic bell-pluck with grit on the attack and a clean tail.
Across the arpeggio each note rings detuned and bell-like. Analyzer: irregular (non-integer)
partial spacing on every onset.

**Round-trip (Gate 7):** `gzip -cd presets/op-poly-bell-final.adv` and confirm the `<Manual
Value>` entries match this table; a fresh build from default must produce an identical sound +
analyzer image.

_To persist: right-click the Operator title bar → **Save Preset** → save as
`op-poly-bell-final` (display name *Polynomial-Bell*) into the episode's `presets/` folder._
