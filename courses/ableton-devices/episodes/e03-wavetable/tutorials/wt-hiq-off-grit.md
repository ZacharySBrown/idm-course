# Patch: Hi-Q-Off-Grit (the Hamburg grit)  (preset: presets/wt-hiq-off-grit.adv)

Concept demonstrated: **Hi-Q OFF + Modern → Fold + fast sweep → the PPG/Hamburg grit, on purpose.**

> ⚠ **PARTIAL HAND-BUILD — Effect Mode, Hi-Q, and the table are NOT settable over our headless path.**
> Set **Osc 1 Effect Mode = Modern** (Fold lives on Effect 2). **Leave Hi-Q OFF** — Hi-Q is not LOM-exposed, but it **defaults OFF in Wavetable**, so the default state IS the grit; **do NOT enable Hi-Q.** Pre-load a **bright/Distortion-category table** by hand. The fast Pos sweep + Fold + high register supply the aliasing regardless.

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note (Hi-Q already OFF by default) |
| 1 | Osc 1 | **Table / Category** | **Distortion (bright/harsh)** | ⚠ **Set in Live by hand (not settable over our headless path).** A harmonic-rich, harsh timbre. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.0 (swept) | The first frame |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 1 | **Osc 1 Effect Mode** | **Modern** | ⚠ **Set in Live by hand.** Enables Warp + Fold. |
| 7 | Osc 1 | Osc 1 Effect 1 (Warp) | 0.0 | No warp |
| 8 | Osc 1 | **Osc 1 Effect 2 (Fold)** | **0.7 (up)** | Buzzy wavefold grit |
| 9 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 10 | Sub | Sub On | Off (0) | No sub |
| 11 | Filter 1 | Flt 1 On / Type | On / 1 (OSR) | Characterful lowpass |
| 12 | Filter 1 | Flt 1 LP/HP / Freq / Res | 0 / 0.85 / 0.15 | Mostly open, a little bite |
| 13 | Filter 1 | **Flt 1 Drive** | 0.4 | ADDED dirt — pushes the grit further |
| 14 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 15 | Amp Env | Amp Attack / Sustain / Release | 0.02 / 1.0 / 0.1 | Fast attack, full hold |
| 16 | Global | **Hi-Q** | **OFF (default — leave it)** | ⚠ **Do NOT enable (not settable over our headless path; defaults OFF = the grit).** |

**The demonstrative move (single):**
Hold a **high** note (**C4**) for ~4.7 s and sweep **Osc 1 Pos 0.0 → 1.0** fast (~1.5 s). Deliberately gritty, aliased, lo-fi — the harsh PPG sound Palm kept.

Final check: strong inharmonic / non-integer partials and a raised inter-harmonic noise floor throughout. A clean harmonic comb ⇒ Hi-Q was on / Fold didn't engage ⇒ reject.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-hiq-off-grit.adv`. **Set Effect Mode = Modern, pre-load the Distortion table, and confirm Hi-Q is OFF in Live before saving.**
