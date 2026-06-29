# Patch: Spectra-Morph — Step 3/7 (Position Spread + OSR filter)  (preset: presets/wt-spectra-step3.adv)

Concept demonstrated: **walkthrough step 3 of 7 — Position Spread unison: a chord of timbres + gentle OSR filter.** The morphing pad now spread wider and richer.

> ⚠ **PARTIAL HAND-BUILD — Formants table, LFO→Pos matrix, and Unison MODE are NOT settable over our headless path.**
> Pre-load the **Formants table**, build the **LFO 1 → Osc 1 Pos** row, and **set Unison = Position Spread (4 voices)** in Live by hand. Only `Unison Amount` and the OSR filter render headless.

Builds on **Step 2**. Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | **Formants (vocal/choir)** | ⚠ **Set in Live by hand.** Vowel timbre. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.35 (drifts) | A vowel frame |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 7 | Sub | Sub On | Off (0) | No sub |
| 8 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 9 | Filter 1 | **Flt 1 Type** | **1 (OSR — OSCar circuit)** | ADDED character — a warmer, slightly resonant lowpass |
| 10 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 11 | Filter 1 | Flt 1 Freq | 0.8 | More shaded top — gentle low-pass |
| 12 | Filter 1 | Flt 1 Res | 0.12 | A touch more resonance |
| 13 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 14 | LFO 1 | LFO 1 Attack Time | 0.6 (~2 s) | Slow bloom preserved |
| 15 | Matrix | **LFO 1 → Osc 1 Pos** | amount **30** | ⚠ **Set in Live by hand.** Slow scan from step 2, preserved. |
| 16 | Amp Env | Amp Attack | 0.45 | Soft swell |
| 17 | Amp Env | Amp Sustain | 1.0 | Holds full level |
| 18 | Amp Env | Amp Release | 0.55 | Long tail |
| 19 | Unison | **Unison Mode / Voices** | **Position Spread, 4 voices** | ⚠ **Set in Live by hand (not settable over our headless path).** ADDED — each voice at a different position. |
| 20 | Unison | Unison Amount | 0.25 | ADDED width — a chord of timbres |

**The sound (single):**
Hold the **C3 / Eb3 / G3** triad ~5.5 s. The same morphing pad, now noticeably wider and with more simultaneous timbres. (Headless proxy: same `Osc 1 Pos` drift + OSR filter + Unison Amount render the added width.)

Final check: broader spread and more distinct partials than step 2; the Position-scan motion preserved.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-spectra-step3.adv`. **Pre-load Formants + LFO→Pos row + Unison = Position Spread in Live before saving.**
