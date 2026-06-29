# Patch: Spectra-Morph — Step 7/7 (The Saved Patch, Demonstrated)  (preset: presets/wt-spectra-morph-final.adv)

Concept demonstrated: **walkthrough step 7 of 7 — the saved "Spectra-Morph" patch, demonstrated.** A held pad chord, then the macro pushed up to growl on a low note — the PPG and Skrillex, one patch.

> ⚠ **PARTIAL HAND-BUILD — same device-state as step 6.**
> This is the **finished, saved preset.** It carries the full hand-set state: **Formants (Osc 1) + Harmonics/bell (Osc 2)** tables, **Osc 1 Effect Mode = FM**, **Unison = Position Spread (4 voices)**, the **Macro 1 "Pad ↔ Growl"** mappings, and the three matrix rows (LFO 1 → Pos, LFO 2 → Pos, Env 2 → Flt 1 Freq). Headless renders the pad→growl move by automating `Osc 1 Pos` + `Flt 1 Freq` across the phrase.

Identical patch to **Step 6** (the saved preset). Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load step-6 preset | init | The full Spectra-Morph patch |
| 1 | Osc 1 | Table / Pos / Detune / Gain | **Formants** ⚠ / 0.35 / 0.5 / 1.0 | Morphing pad base |
| 2 | Osc 1 | **Osc 1 Effect Mode + Effect 1** | **FM** ⚠ / 0.2 | FM edge |
| 3 | Osc 2 | Osc 2 On / table / Pos / Transp / Gain | On / **Harmonics-bell** ⚠ / 0.6 / +12 st / 0.25 | Bell layer |
| 4 | Sub | Sub On / Transpose / Tone / Gain | On / **idx 0** ⚠ / 0.15 / 0.4 | Weight |
| 5 | Filter 1 | Flt 1 On / Type / LP-HP / Freq / Res | On / 1 (OSR) / 0 / 0.8 (automated) / 0.2 | Filter that tightens for the growl half |
| 6 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 7 | Unison | **Unison Mode / Amount** | **Position Spread** ⚠ / 0.25 | Spread width |
| 8 | Amp Env | Amp Attack / Sustain / Release | 0.3 / 1.0 / 0.4 | Medium swell, full hold |
| 9 | Matrix | **LFO 1 → Pos (30), LFO 2 → Pos (0→50), Env 2 → Flt 1 Freq (35)** | as listed | ⚠ **Set in Live by hand.** The pad/growl routings. |
| 10 | Macros | **Macro 1 "Pad ↔ Growl"** | full mappings (see step 6) | ⚠ **Build in Live by hand.** The one-knob transform. |

**The demonstrative phrase (single):**
- Hold the **C3 / Eb3 / G3** triad ~4 s (Macro low) — a morphing pad.
- Then play **C2** (~4 s) with the Macro pushed up — a growl on the low note.
Recognizably the same instrument: the PPG choir and the Skrillex growl, one patch. (Headless proxy: `Osc 1 Pos` slow drift during the chord, fast wobble during the C2 note; `Flt 1 Freq` tightens 0.85 → 0.5 on the second half.)

Final check: first half slow Position-scan motion; second half fast wobble + tighter filter. Both halves clearly the same patch.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-spectra-morph-final.adv` (the canonical **"Spectra-Morph"** patch). **All hand-set device state from step 6 must be in place before saving.**
