# Patch: LFO-to-Position (the wub)  (preset: presets/wt-lfo-to-position.adv)

Concept demonstrated: **LFO → Position in the matrix → timbral wobble with NO pitch change** (the dubstep "wub").

> ⚠ **PARTIAL HAND-BUILD — the mod-matrix routing is NOT settable over our headless path.**
> The **LFO 1 → Osc 1 Pos** matrix connection is not LOM-creatable. In Live, build the real routing by hand (steps 17–19 below). Our headless render reproduces the *identical audible result* by automating `Osc 1 Pos` directly with a triangle wobble — but the **shipping preset must contain the real LFO→Position matrix row.**

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | default (Basic Shapes) | ⚠ Table not settable headless — confirm by hand. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.4 (center; wobble scans around it) | A steady mid-table tone |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 7 | Sub | Sub On | Off (0) | No sub |
| 8 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 9 | Filter 1 | Flt 1 Type | 0 (Clean) | Transparent circuit |
| 10 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 11 | Filter 1 | Flt 1 Freq | 1.0 (open) | Full brightness |
| 12 | Filter 1 | Flt 1 Res | 0.0 | No resonance |
| 13 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 14 | Amp Env | Amp Attack | 0.05 | Fast attack |
| 15 | Amp Env | Amp Sustain | 1.0 | Holds full level |
| 16 | Amp Env | Amp Release | 0.15 | Short tail |
| 17 | LFO 1 | LFO 1 Shape | Triangle (or Saw) | (no change yet — sets the wobble shape) |
| 18 | LFO 1 | LFO 1 Sync + S. Rate | Sync On, **1/8** | (sets the wobble rate to the grid) |
| 19 | Matrix | **LFO 1 → Osc 1 Pos** | amount **40** | ⚠ **Set in Live by hand (not creatable over our headless path).** Tweak Osc 1 Pos so it enters the matrix, then assign LFO 1 as its source. The timbre now wobbles at 1/8 with NO pitch change. |

**The demonstrative move (single, with the real matrix routing):**
Hold **C3** for ~4.7 s. The tone scans back and forth through the table at a steady ~1/8 while the pitch never moves. (Headless proxy: triangle wobble on `Osc 1 Pos` around 0.4 ±0.3, ~0.26 s/step.)

Final check: pitch dead constant; centroid oscillates periodically. f0 wobbling ⇒ routed to pitch by mistake ⇒ reject. Static centroid ⇒ wobble didn't take ⇒ reject.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-lfo-to-position.adv`. **Build the LFO 1 → Osc 1 Pos matrix row in Live before saving** so the preset is the real patch, not the automation proxy.
