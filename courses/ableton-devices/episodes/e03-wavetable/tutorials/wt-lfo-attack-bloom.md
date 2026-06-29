# Patch: LFO-Attack-Bloom  (preset: presets/wt-lfo-attack-bloom.adv)

Concept demonstrated: **LFO Attack (fade-in) → modulation that blooms only after a sustained note** — the "comes alive on long notes" pad trick.

> ⚠ **PARTIAL HAND-BUILD — the mod-matrix routing is NOT settable over our headless path.**
> The **LFO 1 → Osc 1 Pos** connection is not LOM-creatable. `LFO 1 Attack Time` IS settable, but its routing to Position is not. Build the real **LFO 1 → Osc 1 Pos** row by hand (step 20). Our headless render reproduces the result by automating `Osc 1 Pos` (flat ~2 s, then growing-amplitude wobble).

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | default (Basic Shapes) | ⚠ Table not settable headless — confirm by hand. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.35 (center) | A steady mid-table tone |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 7 | Sub | Sub On | Off (0) | No sub |
| 8 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 9 | Filter 1 | Flt 1 Type | 1 (OSR — OSCar circuit) | Slightly characterful lowpass |
| 10 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 11 | Filter 1 | Flt 1 Freq | 0.9 | Gently shaded top end |
| 12 | Filter 1 | Flt 1 Res | 0.1 | A touch of resonance |
| 13 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 14 | Amp Env | Amp Attack | 0.2 (slow) | Note eases in, sustains into the bloom |
| 15 | Amp Env | Amp Sustain | 1.0 | Holds full level |
| 16 | Amp Env | Amp Release | 0.3 | Soft tail |
| 17 | LFO 1 | LFO 1 Shape | Triangle | (sets the morph shape) |
| 18 | LFO 1 | LFO 1 Rate | slow (sub-1 Hz) | (sets a slow drift) |
| 19 | LFO 1 | **LFO 1 Attack Time** | 0.6 (~2 s fade-in) | The LFO fades in over ~2 s |
| 20 | Matrix | **LFO 1 → Osc 1 Pos** | amount **35** | ⚠ **Set in Live by hand (not creatable over our headless path).** Tweak Osc 1 Pos into the matrix, assign LFO 1. Movement now blooms ~2 s after the note. |

**The demonstrative move (single):**
Hold **C3** for ~6.7 s. First ~2 s static; then the timbre begins to morph and breathe as the LFO fades in. (Headless proxy: flat ~2 s, then a growing-amplitude triangle wobble on `Osc 1 Pos`.)

Final check: centroid oscillation near zero for the first ~2 s, then grows. Movement from t=0 ⇒ the fade-in didn't take ⇒ reject.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-lfo-attack-bloom.adv`. **Build the LFO 1 → Osc 1 Pos matrix row in Live before saving.**
