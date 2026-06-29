# Patch: LFO → Macro (The Timbre Breathes)  (preset: presets/meld-lfo-to-macro.adv)

**Demo:** `meld-lfo-to-macro`  ·  **Slide:** `04b-macros-and-matrix`  ·  **Structure:** single
**Concept demonstrated:** the oscillator macro is a first-class matrix target — modulate it and the whole timbre breathes without touching pitch ("the macro is the new Position").

> ## ⚠ THIS DEMO IS BUILT BY HAND — IT CANNOT BE RENDERED OVER OUR HEADLESS PATH.
> The cyclic morph comes from a **modulation-matrix route** (`A LFO 1 → A Osc Shape`). The matrix
> is **NOT in Meld's LOM param map**, so the route cannot be set headless. Setting the `A LFO 1 *`
> params alone does nothing audible without the matrix amount. The manifest's single-ramp
> `automation:` FALLBACK is a stand-in that will NOT pass the cyclic `macro-mod-sweep` assertion.
> **Hand-build the matrix route in the live device.**

Build from a **freshly loaded default Meld**. One parameter per step.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine B | `B On` | Off (0) | Engine B silent |
| 2 | Engine A | `A On` | On (1) | Engine A only |
| 3 | Engine A | `A Osc Type` | **0 = Basic Shapes** | A clean shape — the macro target |
| 4 | Engine A | `A Osc Shape` (macro 1) | 0.50 (center the LFO modulates around) | A mid-bright shape — the LFO's center |
| 5 | Engine A | `A Osc Tone` (macro 2) | 0.50 | A neutral tone |
| 6 | Engine A | `A Transpose` | 0 | (no offset) |
| 7 | Engine A | `A Detune` | 0.50 (0 cents) | Centered tuning |
| 8 | Engine A | `A Filter On` | On (1) | (routing) |
| 9 | Engine A | `A Filter Type` | **0 = Analog** | Transparent filter |
| 10 | Engine A | `A Filter L-B-H-N` | 0.0 (lowpass) | Lowpass response |
| 11 | Engine A | `A Filter Freq` | 1.0 (open) | Uncolored — the macro morph is the only audible change |
| 12 | Engine A | `A Filter Q` | 0.0 | No resonance |
| 13 | Engine A (LFO 1) | `A LFO 1 Type` | **0 = first waveform (sine-ish)** (waveform selector, numeric 0–5) | (sets the LFO shape; not the wave-shaping macro `A LFO 1 Shape`) |
| 14 | Engine A (LFO 1) | `A LFO 1 Rate` | 0.25 (NORMALIZED 0–1, NOT Hz — a slow breathe) | (sets the breathe period; no audible motion until routed) |
| 15 | Engine A | `A Amp Attack` | 0.05 | Fast note start |
| 16 | Engine A | `A Amp Sustain` | 1.0 | Holds at full level |
| 17 | Engine A | `A Amp Release` | 0.30 | Short tail |
| 18 | Engine A | `A Volume` | 0.70 | Solid level |

### HAND-BUILD: the matrix route (this is what makes the demo work)
In the live device's **Matrix** tab, add ONE route:

| Source | Destination | Amount |
|---|---|---|
| `A LFO 1` | `A Osc Shape` (macro 1) | **+0.8 (bipolar)** |

With LFO 1 driving `A Osc Shape` at the slow rate, the held note's timbre slowly opens and closes, cycling — pitch unchanged.

**Play:** one held note `C3` for ~6.7 s.

**Final check:** pitch and loudness constant; timbre cyclically brightens and darkens at the LFO rate.
**Analyzer:** f0 fixed; spectral centroid oscillates at the LFO period while pitch stays flat.

**Save:** with the matrix route built, right-click Meld → **Save Preset** → `presets/meld-lfo-to-macro.adv`.
