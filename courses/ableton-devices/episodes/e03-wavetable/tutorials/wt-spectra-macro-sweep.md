# Patch: Spectra-Morph — Step 6/7 (One Macro: Pad → Growl)  (preset: presets/wt-spectra-macro-sweep.adv)

Concept demonstrated: **walkthrough step 6 of 7 — ONE macro turns the pad into a growl (the payoff).** Same oscillators, same table, one decision apart.

> ⚠ **PARTIAL HAND-BUILD — Macros and the matrix are NOT settable over our headless path.**
> Build the **"Pad ↔ Growl" Macro 1** in Live by hand (step 18). At 0 = slow pad LFO; at 127 = LFO 2 fast wobble engaged + filter tightens + mono/glide on. Also pre-load **Formants/bell tables**, **Effect Mode = FM**, **Unison = Position Spread**. Headless renders the IDENTICAL audible payoff by automating `Osc 1 Pos` (slow drift → fast 1/8 wobble) and `Flt 1 Freq` (tightens 0.8 → 0.5) on ONE held note.

Builds on **Step 5** (the saved preset). Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load step-5 preset (or default) | init | The armed pad |
| 1 | Osc 1 | Table / Pos / Detune / Gain | **Formants** ⚠ / 0.35 / 0.5 / 1.0 | The morphing pad base |
| 2 | Osc 1 | **Osc 1 Effect Mode + Effect 1** | **FM** ⚠ / 0.2 | FM metallic edge |
| 3 | Osc 2 | Osc 2 On / table / Pos / Transp / Gain | On / **Harmonics-bell** ⚠ / 0.6 / +12 st / 0.25 | Bell layer |
| 4 | Sub | Sub On / Transpose / Tone / Gain | On / **idx 0** ⚠ / 0.15 / **0.4** | Weight (a touch louder for the bass payoff) |
| 5 | Filter 1 | Flt 1 On / Type | On / 1 (OSR) | Characterful lowpass |
| 6 | Filter 1 | Flt 1 LP/HP / Freq / Res | 0 / 0.8 (automated down) / 0.2 | Filter that tightens as the growl engages |
| 7 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 8 | Unison | **Unison Mode / Amount** | **Position Spread** ⚠ / 0.25 | Spread width |
| 9 | Global | Glide | 0.0 (macro raises it for mono growl) | No glide at the pad end |
| 10 | Amp Env | Amp Attack / Sustain / Release | 0.3 / 1.0 / 0.4 | Medium swell, full hold |
| 11 | LFO 1 | LFO 1 → Osc 1 Pos (slow) | matrix **30 → 0** under the macro | ⚠ **Set in Live by hand.** Slow pad scan, crossfaded OUT by the macro. |
| 12 | LFO 2 | LFO 2 → Osc 1 Pos (fast 1/8) | matrix **0 → 50** under the macro | ⚠ **Set in Live by hand.** Fast wobble, crossfaded IN by the macro. |
| 18 | Macros | **Macro 1 "Pad ↔ Growl"** | maps: LFO1→Pos 30→0 · LFO2→Pos 0→50 · Flt 1 Freq 0.8→0.5 · Mono Off→On · Glide 0.0→0.1 | ⚠ **Build in Live by hand (not settable over our headless path).** The single knob that does the whole transform. |

**The demonstrative move (sweep):**
Hold **C2** for ~7.5 s and sweep **Macro 1 = 0 → 127**: at 0 it's the slow PPG pad; by 127 the fast 1/8 wobble engages, the filter tightens, and mono/glide kicks in — a dubstep growl. (Headless proxy: `Osc 1 Pos` slow drift for ~3.5 s then a fast ~1/8 wobble; `Flt 1 Freq` ramps 0.8 → 0.5.)

Final check: starts as a slow morphing pad; ends as a fast rhythmic growl on the SAME note, continuous. Centroid modulation rate rises from sub-1 Hz to ~1/8 across the clip. No change in modulation rate ⇒ reject.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-spectra-macro-sweep.adv`. **Build the Macro 1 mappings, both LFO→Pos matrix rows, Effect Mode = FM, both tables, and Unison = Position Spread in Live before saving** (save with Macro 1 = 0, the pad end).
