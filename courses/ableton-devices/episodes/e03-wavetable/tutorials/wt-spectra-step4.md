# Patch: Spectra-Morph — Step 4/7 (Sub + Osc 2 bell)  (preset: presets/wt-spectra-step4.adv)

Concept demonstrated: **walkthrough step 4 of 7 — Sub for weight, Osc 2 for glassy bell overtones** (the Depeche Mode bell layer).

> ⚠ **PARTIAL HAND-BUILD — Formants/bell tables, LFO→Pos matrix, and Unison MODE are NOT settable over our headless path.**
> Pre-load the **Formants table on Osc 1** and a **Harmonics/bell table on Osc 2**, build the **LFO 1 → Osc 1 Pos** row, and **set Unison = Position Spread (4 voices)** in Live by hand. **Sub Transpose** is quantized 0/1/2 (default 1); index **0** = the lowest (octave-down) setting — **verify by ear.**

Builds on **Step 3**. Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | **Formants (vocal/choir)** | ⚠ **Set in Live by hand.** Vowel timbre. |
| 2 | Osc 1 | Osc 1 On / Pos / Gain | On / 0.35 (drifts) / 1.0 | The morphing vowel pad |
| 3 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 4 | Osc 2 | **Osc 2 On** | **On (1)** | ADDED a second oscillator |
| 5 | Osc 2 | Table / Category | **Harmonics / bell** | ⚠ **Set in Live by hand (not settable over our headless path).** A glassy bell timbre. |
| 6 | Osc 2 | Osc 2 Pos | 0.6 | A bright bell frame |
| 7 | Osc 2 | **Osc 2 Transp** | **+12 st (+1 octave)** | ADDED glassy shimmer one octave up |
| 8 | Osc 2 | Osc 2 Gain | 0.25 (low) | Bell sits as overtones, not body |
| 9 | Sub | **Sub On** | **On (1)** | ADDED low-end weight |
| 10 | Sub | **Sub Transpose** | **index 0 (lowest octave)** | ⚠ Quantized 0/1/2 — **verify octave-down by ear.** |
| 11 | Sub | Sub Tone | 0.15 (~15%) | Mostly clean sine weight |
| 12 | Sub | Sub Gain | 0.35 | Present but supporting |
| 13 | Filter 1 | Flt 1 On / Type | On / 1 (OSR) | Characterful lowpass (from step 3) |
| 14 | Filter 1 | Flt 1 LP/HP / Freq / Res | 0 / 0.8 / 0.12 | Gentle low-pass |
| 15 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 16 | LFO 1 | LFO 1 Attack Time | 0.6 (~2 s) | Slow bloom preserved |
| 17 | Matrix | **LFO 1 → Osc 1 Pos** | amount **30** | ⚠ **Set in Live by hand.** Slow scan preserved. |
| 18 | Amp Env | Amp Attack / Sustain / Release | 0.45 / 1.0 / 0.55 | Soft swell, full hold, long tail |
| 19 | Unison | **Unison Mode / Voices** | **Position Spread, 4 voices** | ⚠ **Set in Live by hand.** Chord of timbres. |
| 20 | Unison | Unison Amount | 0.25 | Spread width |

**The sound (single):**
Hold the **C3 / Eb3 / G3** triad ~5.5 s. The same morphing pad with added low-end weight (Sub) and a high glassy bell shimmer (Osc 2) — the Depeche Mode bell layer.

Final check: more energy below the fundamental (Sub) AND added high partials (Osc 2 bell) vs step 3.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-spectra-step4.adv`. **Pre-load Osc 1 Formants + Osc 2 Harmonics/bell tables, LFO→Pos row, Unison = Position Spread, and confirm Sub Transpose by ear before saving.**
