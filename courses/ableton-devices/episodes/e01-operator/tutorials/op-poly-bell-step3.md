# Patch tutorial — `op-poly-bell-step3`  (Polynomial-Bell, Step 3 of 8)

**Preset:** `presets/op-poly-bell-step3.adv`  ·  **Concept:** First modulator B at a √2 (irrational) ratio — bell appears  ·  **Used in slide:** `05c-modulator-b`

> Step 3 — the move that makes it a bell. Bring in modulator B at **Coarse 1, Fine 414**
> (≈ ×1.414, √2) so its sidebands fall off the harmonic grid. B's envelope is *shorter* than
> the carrier's, so the spectrum is bright on the attack then fades back toward sine.
>
> **You should hear:** a metallic, inharmonic **shimmer in the attack** that decays into a near-
> pure sine — the first recognizable bell-pluck.

Build from a **freshly loaded Operator** (init). One parameter per step. (Steps 0–10 repeat
Step 2's carrier; the new work is the Osc B block.)

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack D→C→B→A) | Routing only |
| 2 | Osc A | On / Wave | On / Sine | Pure sine carrier |
| 3 | Osc A | Coarse / Fine | 1 / 0 | Carrier at C3 |
| 4 | Osc A | Level | −12 dB (norm 0.75) | Headroom retained |
| 5 | Osc A | Env A / D / S / R | 1 ms / 400 ms / −inf / 200 ms (0.01 / 0.40 / 0.0 / 0.30) | Pure-sine pluck |
| 6 | Osc B | On | On | A metallic edge enters the attack |
| 7 | Osc B | Wave | Sine | Clean inharmonic sidebands |
| 8 | Osc B | Coarse | 1 | Base ratio before the fine detune |
| 9 | Osc B | **Fine** | **414** | **≈ ×1.414 (√2) — irrational; bell territory** |
| 10 | Osc B | Level | 0.8 (≈ 80%) | Strong metallic shimmer on the attack |
| 11 | Osc B | Feedback | 0 | No self-modulation |
| 12 | Osc B | Env Attack | 1 ms (norm 0.01) | Instant bright onset |
| 13 | Osc B | Env Decay | 120 ms (norm 0.15) | Shimmer fades faster than the carrier → spectrum collapses toward sine |
| 14 | Osc B | Env Sustain | −inf (0.0) | Modulation gone after the decay |
| 15 | Osc B | Env Release | 80 ms (norm 0.10) | Short bright tail |
| 16 | Osc C | On | Off | (added next step) |
| 17 | Osc D | On | Off | (unused) |

**Final check:** a struck **bell-pluck** — metallic, detuned attack that settles into a pure
sine. Spectrum: non-integer partial spacing on the transient. This is the same trick James
used on *Drukqs*-era bells.

_To persist: right-click the Operator title bar → **Save Preset** → save as
`op-poly-bell-step3` into the episode's `presets/` folder._
