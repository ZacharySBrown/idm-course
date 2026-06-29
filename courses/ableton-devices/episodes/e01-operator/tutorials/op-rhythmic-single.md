# Patch tutorial — `op-rhythmic-single`  (Rhythmic FM, layer 1 of 2)

**Preset:** `presets/op-rhythmic-single.adv`  ·  **Concept:** Rhythmic FM via envelope **Beat** mode — the synthesis topology *is* the rhythm  ·  **Used in slide:** `06a-rhythmic-fm`

> A single held C3 becomes a self-rhythmic metallic percussion line. The carrier's amplitude
> envelope is in **Beat** mode, re-triggering on the grid (≈ 1/16 @ 100 BPM) so the note pulses
> without a sequencer; B modulates continuously at an inharmonic **11:1** ratio for the metal.
>
> **You should hear:** a held note that *pulses* on a sixteenth-note grid, each hit a short
> metallic click — no MIDI sequence, one note in.

> 📝 **Gate 4 reconciliation (rendered patch vs script):** the `06a` script narrates "set **B's**
> envelope to Beat mode at 1/16; set **A** to Trigger, decay 200 ms." The **rendered** patch
> (manifest / this table) instead puts **Beat mode on the carrier A** (Ae Mode = Beat, decay
> ~120 ms) with **B = None** (continuous modulator). Both produce beat-locked metallic hits, but
> the operator carrying the Beat envelope differs. Reconcile before SCRIPT LOCK — this table
> matches the WAV that ships.
>
> ⚙️ **Be / Ae Retrig calibration:** Retrig is 0–14 (continuous in LOM, an enum of note values in
> the UI). `2` is the first guess for 1/16; **verify the rate by ear in Live** and adjust
> (0≈1/32, 2≈1/16, 4≈1/8 …). The Gate 7 onset check measures the actual rate.

Build from a **freshly loaded Operator** (init). One parameter per step.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack) | Routing only |
| 2 | Osc A | On / Wave | On / Sine | Pure sine carrier |
| 3 | Osc A | Coarse / Fine | 1 / 0 | Carrier at C3 |
| 4 | Osc A | Level | 0.8 (≈ 80%) | Carrier level |
| 5 | Osc A | **Env Mode** | **Beat** | Carrier amplitude now **pulses on the grid** |
| 6 | Osc A | **Env Retrig** | **2** (≈ 1/16 — verify by ear) | Pulse rate = sixteenth notes @ song tempo |
| 7 | Osc A | Env Attack / Decay / Sustain / Release | 0.0 / 120 ms (0.12) / −inf (0.0) / 0.0 | Each hit a short percussive click |
| 8 | Osc B | On / Wave | On / Sine | Modulator in |
| 9 | Osc B | **Coarse** | **11** (prime, inharmonic) | **11:1 ratio → metallic, no musical-interval character** |
| 10 | Osc B | Fine | 0 | Exact integer ratio |
| 11 | Osc B | Level | 0.7 (≈ 70%) | Modulation depth (the metal) |
| 12 | Osc B | Env Mode | None | B modulates **continuously** under each hit |
| 13 | Osc B | Env Attack / Decay / Sustain / Release | 0.0 / 1.0 / 1.0 / 0.0 | Constant metallic timbre |
| 14 | Osc C | On | Off | (unused) |
| 15 | Osc D | On | Off | (unused) |

**Final check:** hold one note → a steady stream of short metallic clicks locked to a 1/16
grid. The pulse is A's Beat envelope; the metal is the 11:1 ratio. Like the FM percussion that
opens Autechre's *Bike* (*Incunabula*, 1993).

**Verification (Gate 7):** `rhythmic` — onset rate matches the intended grid (≈ 8 onsets/s for
1/16 @ 120; scale for 100 BPM) AND this layer's onset rate is **distinct** from
`op-rhythmic-instance2`. (This is the exact check that caught `single == instance2` in ep1.)

_To persist: right-click the Operator title bar → **Save Preset** → save as
`op-rhythmic-single` into the episode's `presets/` folder._
