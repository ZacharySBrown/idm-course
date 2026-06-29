# Patch tutorial — `op-poly-bell-step6`  (Polynomial-Bell, Step 6 of 8)

**Preset:** `presets/op-poly-bell-step6.adv`  ·  **Concept:** Spread + Filter — stereo width and analog warmth  ·  **Used in slide:** `05f-spread-filter`

> Step 6 — global polish. **Spread 12%** runs two detuned, hard-panned voice instances for
> stereo width. **Filter on**: a 24 dB/oct lowpass on the **OSR** circuit (Oxford OScar model,
> diode-clipped resonance) at ~8 kHz, with +3 dB drive for gentle warmth.
>
> **You should hear:** the Step-5 bell now **wider** (stereo) and a touch **warmer/rounder** at
> the top — the OSR drive adds analog character without dulling the bell.

Build from a **freshly loaded Operator** (init). One parameter per step. (Operators A–C repeat
Step 5; the new work is the Global block.)

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack) | Routing only |
| 2 | Osc A | On / Wave / Coarse / Fine / Level | On / Sine / 1 / 0 / −12 dB | Carrier |
| 3 | Osc A | Env A / D / S / R | 1 ms / 400 ms / −inf / 200 ms | Pure-sine pluck |
| 4 | Osc B | On / Wave / Coarse / Fine / Level | On / Sine / 1 / 414 (√2) / 0.8 | Bell shimmer |
| 5 | Osc B | Env A / D / S / R | 1 ms / 120 ms / −inf / 80 ms | Short metallic attack |
| 6 | Osc C | On / Wave / Coarse / Level / Feedback | On / Sine / 7 / 0.5 / 30% | Gritty high shimmer |
| 7 | Osc C | Env A / D / S / R | 1 ms / 60 ms / −inf / 60 ms | Front-of-attack sparkle |
| 8 | Osc D | On | Off | (unused) |
| 9 | Global | **Spread** | **12** | Bell widens noticeably (stereo), no phasing |
| 10 | Global | **Filter On** | On | Filter now in circuit |
| 11 | Global | **Filter Type** | Lowpass | Top end under control |
| 12 | Global | **Filter Slope** | 24 dB | Steeper rolloff |
| 13 | Global | **Filter Circuit - LP/HP** | OSR | Oxford OScar model — diode-clipped resonance, analog grit |
| 14 | Global | **Filter Freq** | ~8 kHz (manifest norm 0.85) | Tames the very top while keeping the bell bright |
| 15 | Global | **Filter Drive** | +3 dB | Subtle warmth/saturation |

**Final check:** the same bell, wider and warmer — stereo spread audible, top end rounded by
the OSR filter without losing the metallic attack.

_To persist: right-click the Operator title bar → **Save Preset** → save as
`op-poly-bell-step6` into the episode's `presets/` folder._
