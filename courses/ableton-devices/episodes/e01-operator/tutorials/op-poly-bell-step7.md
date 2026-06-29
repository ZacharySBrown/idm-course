# Patch tutorial — `op-poly-bell-step7`  (Polynomial-Bell, Step 7 of 8)

**Preset:** `presets/op-poly-bell-step7.adv`  ·  **Concept:** Velocity → modulator level (= modulation index = brightness)  ·  **Used in slide:** `05g-velocity`

> Step 7 — the difference between a static patch and a playable one. Route **velocity to the
> modulator's level** on B: harder notes raise B's level → higher modulation index → brighter,
> more metallic timbre. Same patch, different velocity, different *color* — the FM equivalent of
> an embouchure response, no external automation.
>
> **You should hear:** two C3s — a **soft** note (vel 30, nearly pure sine) then a **hard** note
> (vel 110, metallic, bright). The bite on the loud note is velocity hitting modulation depth.

> ⚠️ **Velocity panel note:** this is **Osc-B Lev < Vel** (modulator *level* per velocity), which
> changes *brightness/index* — it lives in B's oscillator panel and is distinct from
> **Freq < Vel** (which changes *pitch*). Do not conflate them.
>
> 📝 **Gate 4 reconciliation:** the `05g-velocity` script also says "set **Time-less-than-Vel**
> +30 on B" (harder = shorter, brighter ring). The rendered demo / manifest sets only
> **Osc-B Lev < Vel = +50**. Before SCRIPT LOCK, either add the velocity→envelope-time routing
> to the patch or trim that line — the table below matches the **rendered** patch.

Build from a **freshly loaded Operator** (init). One parameter per step. (Operators A–C and the
Global block repeat Step 6; the new work is the single velocity routing on B.)

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack) | Routing only |
| 2 | Osc A | On / Wave / Coarse / Fine / Level | On / Sine / 1 / 0 / −12 dB | Carrier |
| 3 | Osc A | Env A / D / S / R | 1 ms / 400 ms / −inf / 200 ms | Pure-sine pluck |
| 4 | Osc B | On / Wave / Coarse / Fine / Level | On / Sine / 1 / 414 (√2) / 0.8 | Bell shimmer |
| 5 | Osc B | Env A / D / S / R | 1 ms / 120 ms / −inf / 80 ms | Short metallic attack |
| 6 | Osc B | **Lev < Vel** | **+50** | **Velocity now drives brightness:** soft = dull, hard = metallic |
| 7 | Osc C | On / Wave / Coarse / Level / Feedback | On / Sine / 7 / 0.5 / 30% | Gritty high shimmer |
| 8 | Osc C | Env A / D / S / R | 1 ms / 60 ms / −inf / 60 ms | Front-of-attack sparkle |
| 9 | Osc D | On | Off | (unused) |
| 10 | Global | Spread | 12 | Stereo width |
| 11 | Global | Filter On / Type / Slope / Circuit | On / Lowpass / 24 dB / OSR | Analog-warm lowpass |
| 12 | Global | Filter Freq / Drive | ~8 kHz (norm 0.85) / +3 dB | Top rounded, slight warmth |

**Final check:** play soft → the bell is nearly a pure sine; play hard → it opens into a bright
metallic strike. The change is in modulation depth, not a filter. Spectrum: the hard note has
measurably more sideband energy than the soft note at the same pitch.

**Verification (Gate 7):** `velocity` — high-velocity segment has more sideband energy than low
at identical pitch. Equal ⇒ reject.

_To persist: right-click the Operator title bar → **Save Preset** → save as
`op-poly-bell-step7` into the episode's `presets/` folder._
