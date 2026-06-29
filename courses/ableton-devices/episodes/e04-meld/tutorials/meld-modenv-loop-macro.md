# Patch: Mod-Env Loop → Macro (Self-Cycling Timbre)  (preset: presets/meld-modenv-loop-macro.adv)

**Demo:** `meld-modenv-loop-macro`  ·  **Slide:** `03e-lfo-loop-env`  ·  **Structure:** single
**Concept demonstrated:** a Mod Env in AD-Loop routed to an oscillator macro is a self-cycling timbral sequencer on ONE held note — a sustained key turns into a repeating timbral figure, no new notes.

> ## ⚠ THIS DEMO IS BUILT BY HAND — IT CANNOT BE RENDERED OVER OUR HEADLESS PATH.
> The audible motion comes from a **modulation-matrix route** (`A Mod Env → A Osc Shape`). The
> matrix is **NOT exposed in Meld's LOM param map**, so the route cannot be set headless. Setting
> `A Mod Loop Mode` alone produces NO motion without the matrix amount. The manifest carries a
> single-ramp `automation:` FALLBACK so *something* renders, but a single ramp is not a loop — it
> will NOT pass the `self-sequence` recurrence assertion. **Hand-build the matrix route in the live
> device** for the real demo and the saved `.adv`.

**⚠ PLACEHOLDER ENUM INDEX — NEEDS LIVE CONFIRMATION:** `A Mod Loop Mode` is quantized 0–3 with EMPTY value_items. The Meld set is {Trigger / Loop / AD Loop / + one more}; **AD Loop is set to PLACEHOLDER index 2** — confirm the 0–3 ordering live.

Build from a **freshly loaded default Meld**. One parameter per step.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine B | `B On` | Off (0) | Engine B silent |
| 2 | Engine A | `A On` | On (1) | Engine A only |
| 3 | Engine A | `A Osc Type` | **0 = Basic Shapes** | A clean shape — the macro target |
| 4 | Engine A | `A Osc Shape` (macro 1) | 0.30 (center the loop sweeps around) | A mid-bright shape — the loop's starting point |
| 5 | Engine A | `A Osc Tone` (macro 2) | 0.50 | A neutral tone |
| 6 | Engine A | `A Filter On` | On (1) | (routing) |
| 7 | Engine A | `A Filter Type` | **0 = Analog** | Transparent filter |
| 8 | Engine A | `A Filter L-B-H-N` | 0.0 (lowpass) | Lowpass response |
| 9 | Engine A | `A Filter Freq` | 0.80 | A gentle low-pass, slightly tamed top |
| 10 | Engine A | `A Filter Q` | 0.10 | A touch of resonant edge |
| 11 | Engine A (Mod Env) | `A Mod Loop Mode` | **2 = AD Loop (PLACEHOLDER — CONFIRM)** | The Mod Env now cycles (no audible change yet — needs the matrix route) |
| 12 | Engine A (Mod Env) | `A Mod Attack` | 0.15 | (sets the rise of each loop cycle) |
| 13 | Engine A (Mod Env) | `A Mod Decay` | 0.40 | (sets the self-sequence period) |
| 14 | Engine A | `A Amp Attack` | 0.05 | Fast note start |
| 15 | Engine A | `A Amp Sustain` | 1.0 | Holds at full level |
| 16 | Engine A | `A Amp Release` | 0.30 | Short tail |
| 17 | Engine A | `A Volume` | 0.70 | Solid level |

### HAND-BUILD: the matrix route (this is what makes the demo work)
In the live device's **Matrix** tab, add ONE route:

| Source | Destination | Amount |
|---|---|---|
| `A Mod Env` | `A Osc Shape` (macro 1) | **+0.85** |

With the AD-Loop Mod Env (steps 11–13) driving `A Osc Shape` at +0.85, the held note's timbre now cycles on its own on a steady period.

**Play:** one held note `C3` for ~6.7 s — do not play another note.

**Final check:** constant pitch; the timbre cyclically morphs on a steady period from a single held note. No new note onsets.
**Analyzer:** spectral centroid follows a repeating AD-Loop contour from one held note; f0 fixed.

**Save:** with the matrix route built, right-click Meld → **Save Preset** → `presets/meld-modenv-loop-macro.adv` (the `.adv` preserves the matrix route even though the param path cannot set it).
