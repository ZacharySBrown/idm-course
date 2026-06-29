# Patch tutorial — `op-rhythmic-instance2`  (Rhythmic FM, layer 2 of 2)

**Preset:** `presets/op-rhythmic-instance2.adv`  ·  **Concept:** The second polyrhythm layer — a *distinct* rate and ratio  ·  **Used in slide:** `06b-layer` (summed into `op-rhythmic-layered`)

> The second Operator instance for the layered polyrhythm. Identical to `op-rhythmic-single`
> **except two values change** so the layer is audibly different: a **slower** Beat rate
> (Ae Retrig = 4, ≈ 1/8 dotted) and a **different inharmonic ratio** (B Coarse = 13). Summing
> the two instances (`op-rhythmic-layered`) gives the interlocking metallic polyrhythm.
>
> **You should hear:** the same self-rhythmic metallic pulse, but at a **slower grid** and a
> **different metallic color** than layer 1 — so the two interlock rather than double.

> ⚠️ **Must be distinct from layer 1 (Gate 7):** the ep1 failure was `op-rhythmic-single ==
> instance2` (identical onset rate). The two changed parameters below (Retrig 2→4, Coarse
> 11→13) are what make the onset rates and timbres measurably different. **Verify both rates by
> ear in Live** and confirm the onset-rate check separates them before shipping.
>
> 📝 Same Gate 4 reconciliation as layer 1: the rendered patch carries the **Beat** envelope on
> carrier **A** (script narrates B). This table matches the WAV.

Build from a **freshly loaded Operator** (init). One parameter per step. (Differences from
`op-rhythmic-single` are marked **★**.)

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack) | Routing only |
| 2 | Osc A | On / Wave | On / Sine | Pure sine carrier |
| 3 | Osc A | Coarse / Fine | 1 / 0 | Carrier at C3 |
| 4 | Osc A | Level | 0.8 (≈ 80%) | Carrier level |
| 5 | Osc A | **Env Mode** | **Beat** | Carrier pulses on the grid |
| 6 | Osc A | **★ Env Retrig** | **4** (≈ 1/8 dotted — verify by ear; distinct from layer 1's 2) | **Slower** pulse than layer 1 |
| 7 | Osc A | Env Attack / Decay / Sustain / Release | 0.0 / 180 ms (0.18) / −inf (0.0) / 0.0 | Slightly longer hit than layer 1 |
| 8 | Osc B | On / Wave | On / Sine | Modulator in |
| 9 | Osc B | **★ Coarse** | **13** (prime, inharmonic — distinct from layer 1's 11) | **Different** metallic color |
| 10 | Osc B | Fine | 0 | Exact integer ratio |
| 11 | Osc B | Level | 0.7 (≈ 70%) | Modulation depth |
| 12 | Osc B | Env Mode | None | B modulates continuously |
| 13 | Osc B | Env Attack / Decay / Sustain / Release | 0.0 / 1.0 / 1.0 / 0.0 | Constant metallic timbre |
| 14 | Osc C | On | Off | (unused) |
| 15 | Osc D | On | Off | (unused) |

**Final check:** hold one note → metallic clicks at a **slower** grid and a **different** pitch
character than layer 1. Played together, the two grids interlock into a polyrhythm.

**Verification (Gate 7):** `rhythmic` — onset rate is **distinct** from `op-rhythmic-single`;
the layered mix shows two separable onset rates. Equal rates ⇒ reject (the ep1 failure).

_To persist: right-click the Operator title bar → **Save Preset** → save as
`op-rhythmic-instance2` into the episode's `presets/` folder._
