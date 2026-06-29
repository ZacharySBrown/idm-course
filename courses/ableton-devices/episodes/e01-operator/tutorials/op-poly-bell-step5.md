# Patch tutorial — `op-poly-bell-step5`  (Polynomial-Bell, Step 5 of 8)

**Preset:** `presets/op-poly-bell-step5.adv`  ·  **Concept:** Feedback on C — grit in the attack ("Aphex's bell")  ·  **Used in slide:** `05e-feedback`

> Step 5 — halfway; this is what makes it *Aphex's* bell, not a clean Eno bell. C sits at the
> top of the Alg. 1 stack (nothing modulates it), so **feedback is enabled there**. At 30% C
> self-modulates lightly, leaning its waveform off sine and dropping a little grit into the
> attack transient.
>
> **You should hear:** the Step-4 bell with an added **gritty edge** on the attack — a touch of
> dirt, not a wholesale saw.

> ⚠️ **Feedback caveat:** feedback only takes on an operator that is *not* being modulated by
> another. C is at the top of the stack here, so this is valid. (Our headless renderer
> under-reads feedback — see `FEEDBACK_FIX.md`; confirm the grit by ear in Live.)

Build from a **freshly loaded Operator** (init). One parameter per step. (Everything repeats
Step 4 except the single new Feedback value on C.)

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack D→C→B→A) | Routing — C above B |
| 2 | Osc A | On / Wave / Coarse / Fine / Level | On / Sine / 1 / 0 / −12 dB | Carrier ready |
| 3 | Osc A | Env A / D / S / R | 1 ms / 400 ms / −inf / 200 ms | Pure-sine pluck |
| 4 | Osc B | On / Wave / Coarse / Fine / Level | On / Sine / 1 / 414 (√2) / 0.8 | Bell shimmer |
| 5 | Osc B | Env A / D / S / R | 1 ms / 120 ms / −inf / 80 ms | Short metallic attack |
| 6 | Osc C | On / Wave / Coarse / Level | On / Sine / 7 / 0.5 | High shimmer on the onset |
| 7 | Osc C | Env A / D / S / R | 1 ms / 60 ms / −inf / 60 ms | Front-of-attack sparkle |
| 8 | Osc C | **Feedback** | **30%** | **Gritty edge appears in the attack — C leans off sine** |
| 9 | Osc D | On | Off | (unused) |

**Final check:** same bell, now with a little grit/dirt on the attack — enough to stop it
sounding like a clean Eno bell. Spectrum: a slightly richer, less symmetric transient.

_To persist: right-click the Operator title bar → **Save Preset** → save as
`op-poly-bell-step5` into the episode's `presets/` folder._
