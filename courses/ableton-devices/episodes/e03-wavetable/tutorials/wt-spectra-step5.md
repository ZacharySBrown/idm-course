# Patch: Spectra-Morph — Step 5/7 (Arm the Growl)  (preset: presets/wt-spectra-step5.adv)

Concept demonstrated: **walkthrough step 5 of 7 (halfway — arm the growl) — fast LFO 2 → Position (bypassed), Env → Filter, Osc 1 FM.** The pad, unchanged at the surface, now armed for the transform.

> ⚠ **PARTIAL HAND-BUILD — several pieces are NOT settable over our headless path.**
> Pre-load **Formants (Osc 1) + Harmonics/bell (Osc 2)** tables; set **Osc 1 Effect Mode = FM** (the metallic edge); set **Unison = Position Spread (4 voices)**; and build three matrix rows by hand: **LFO 1 → Osc 1 Pos (30)**, **LFO 2 → Osc 1 Pos (0, bypassed)**, **Env 2 → Flt 1 Freq (35)**. `Sub Transpose` index 0 — verify by ear. Headless renders only the FM edge (`Osc 1 Effect 1 = 0.2`) + the Env 2 shape + the preserved slow Pos drift.

Builds on **Step 4**. Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | **Formants** | ⚠ **Set in Live by hand.** Vowel timbre. |
| 2 | Osc 1 | Osc 1 On / Pos / Detune / Gain | On / 0.35 (drifts) / 0.5 / 1.0 | The morphing vowel pad |
| 3 | Osc 1 | **Osc 1 Effect Mode** | **FM** | ⚠ **Set in Live by hand (not settable over our headless path).** Enables the hidden FM modulator. |
| 4 | Osc 1 | **Osc 1 Effect 1 (FM Amount)** | **0.2 (~20%)** | ADDED a faint metallic edge |
| 5 | Osc 1 | Osc 1 Effect 2 (FM Tune) | 0.0 | Modulator at osc pitch |
| 6 | Osc 2 | Osc 2 On / table / Pos / Transp / Gain | On / **Harmonics-bell** ⚠ / 0.6 / +12 st / 0.25 | Glassy bell layer (table set by hand) |
| 7 | Sub | Sub On / Transpose / Tone / Gain | On / **idx 0** ⚠ / 0.15 / 0.35 | Low-end weight (octave by ear) |
| 8 | Filter 1 | Flt 1 On / Type | On / 1 (OSR) | Characterful lowpass |
| 9 | Filter 1 | Flt 1 LP/HP / Freq / Res | 0 / 0.8 / 0.15 | Gentle low-pass |
| 10 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 11 | Env 2 | Env 2 Attack / Decay / Sustain / Release | 0.05 / 0.4 / 0.3 / 0.3 | A snappy contour (will drive the filter) |
| 12 | Matrix | **Env 2 → Flt 1 Freq** | amount **35** | ⚠ **Set in Live by hand.** ADDED — armed filter movement. |
| 13 | LFO 1 | LFO 1 Attack Time | 0.6 (~2 s) | Slow bloom preserved |
| 14 | Matrix | **LFO 1 → Osc 1 Pos** | amount **30** | ⚠ **Set in Live by hand.** Slow pad scan. |
| 15 | LFO 2 | LFO 2 Shape / Sync + S. Rate | Saw / Sync, **1/8** | (sets the fast wobble — bypassed for now) |
| 16 | Matrix | **LFO 2 → Osc 1 Pos** | amount **0 (ARMED, bypassed)** | ⚠ **Set in Live by hand.** ADDED but silent — the growl is armed, not engaged. |
| 17 | Amp Env | Amp Attack / Sustain / Release | 0.45 / 1.0 / 0.55 | Soft swell, full hold, long tail |
| 18 | Unison | **Unison Mode / Voices / Amount** | **Position Spread, 4 voices** ⚠ / 0.25 | Chord of timbres (mode by hand) |

**The sound (single):**
Hold the **C3 / Eb3 / G3** triad ~5.5 s. Still recognizably the pad, with a faint metallic edge from the FM; the fast 1/8 wobble is armed but bypassed (silent).

Final check: a slight rise in upper/inharmonic content vs step 4 (the FM edge). The fast wobble should NOT be audible yet.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-spectra-step5.adv`. **Set Effect Mode = FM, all three matrix rows, both tables, and Unison = Position Spread in Live before saving.**
