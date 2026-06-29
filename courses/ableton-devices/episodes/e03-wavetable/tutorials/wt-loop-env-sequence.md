# Patch: Loop-Env-Sequence  (preset: presets/wt-loop-env-sequence.adv)

Concept demonstrated: **a free envelope in Loop → Position → a self-sequencing timbral pattern from ONE held note.**

> ⚠ **PARTIAL HAND-BUILD — Effect Mode, Env→Position routing, and LFO→Effect routing are NOT settable over our headless path.**
> Set **Osc 1 Effect Mode = FM** (for the base grit). `Env 2 Loop Mode` IS settable (index 2 = Loop), but its **routing to Position** is not LOM-creatable, so Loop mode alone produces no Position cycling headless — build the **Env 2 → Osc 1 Pos** row by hand (step 16). Optionally add **LFO 1 → Osc 1 Effect 1** (1/16 grit) by hand. Headless renders the rhythm by automating `Osc 1 Pos` with a repeating 1/8 step pattern.

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | default (Basic Shapes) | ⚠ Table not settable headless — confirm by hand. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.0 (cycled by the loop env) | The first frame |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 1 | **Osc 1 Effect Mode + Effect 1** | **FM** ⚠ / 0.1 (base FM) | ⚠ **Set Effect Mode = FM in Live by hand.** A faint metallic grit. |
| 7 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 8 | Sub | Sub On | Off (0) | No sub |
| 9 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 10 | Filter 1 | **Flt 1 Type** | **2 (MS2 — MS-20 circuit)** | A gritty, characterful lowpass |
| 11 | Filter 1 | Flt 1 LP/HP / Freq / Res | 0 / 0.7 / 0.2 | A tighter low-pass with some bite |
| 12 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 13 | Amp Env | Amp Attack / Sustain / Release | 0.02 / 1.0 / 0.1 | Fast attack, full hold |
| 14 | Env 2 | **Env 2 Loop Mode** | **2 (Loop)** | The envelope now cycles on the grid |
| 15 | Env 2 | Env 2 Attack / Decay / Sustain | 0.1 / 0.4 / 0.0 | A repeating per-cycle contour |
| 16 | Matrix | **Env 2 → Osc 1 Pos** | amount **90** | ⚠ **Set in Live by hand (not creatable over our headless path).** The loop env now cycles Position = a timbral sequence. |
| 17 | Matrix | **LFO 1 → Osc 1 Effect 1** (optional) | amount **30**, LFO 1/16 | ⚠ **Set in Live by hand.** Adds 1/16 FM grit. |

**The demonstrative move (single):**
Hold ONE note (**C3**) for the whole ~7.7 s clip. A single held key becomes a repeating rhythmic timbre pattern at a clear 1/8 grid, because the loop envelope cycles Position. No new notes. (Headless proxy: `Osc 1 Pos` repeating 1/8 step pattern [0.1, 0.5, 0.2, 0.8 …] at 0.25 s/step ≈ 1/8 @120.)

Final check: onset/spectral-flux peaks recur at a fixed ~1/8 grid rate. No periodic recurrence ⇒ reject.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-loop-env-sequence.adv`. **Set Effect Mode = FM, Env 2 Loop Mode = Loop, and build the Env 2 → Osc 1 Pos row in Live before saving.**
