# Patch: Position-By-Hand  (preset: presets/wt-position-by-hand.adv)

Concept demonstrated: **Position → which waveform you play (timbre), with pitch held constant.** Hold one note, drag Position 0→100, and only the harmonic content moves.

Build from a **freshly loaded default Wavetable.** One parameter per step. The "hear" column is your self-check. Position values use Wavetable's **0–1 LOM scale** (the UI shows 0–100% — 0.0 = 0%, 1.0 = 100%).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | A neutral saw on each note (default Basic Shapes table) |
| 1 | Osc 1 | Table / Category | **Basic Shapes** (default — already loaded) | Same neutral tone. ⚠ Table selection is **not settable over our headless path** — confirm Basic Shapes is the loaded table by hand. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding (already on by default) |
| 3 | Osc 1 | Osc 1 Pos | 0.0 (0%) | The first frame of Basic Shapes — a near-pure sine |
| 4 | Osc 1 | Osc 1 Transp | 0 st | Pitch at the played note, no transpose |
| 5 | Osc 1 | Osc 1 Detune | 0.5 (= 0 cents) | No detune — single clean voice |
| 6 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level (NOTE: 0.0 here = silence) |
| 7 | Osc 2 | Osc 2 On | Off (0) | Osc 2 muted — Osc 1 only |
| 8 | Sub | Sub On | Off (0) | No sub layer |
| 9 | Filter 1 | Flt 1 On | On (1) | Filter in the path |
| 10 | Filter 1 | Flt 1 Type | 0 (Clean) | Transparent Cytomic circuit — no colour added |
| 11 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 12 | Filter 1 | Flt 1 Freq | 1.0 (wide open) | Nothing filtered — full brightness passes |
| 13 | Filter 1 | Flt 1 Res | 0.0 | No resonance |
| 14 | Filter 2 | Flt 2 On | Off (0) | Single filter only |
| 15 | Amp Env | Amp Attack | 0.05 (~fast) | Note speaks immediately |
| 16 | Amp Env | Amp Decay | 0.0 | No decay stage |
| 17 | Amp Env | Amp Sustain | 1.0 (full) | Note holds at full level the whole time |
| 18 | Amp Env | Amp Release | 0.15 (short) | Clean tail on key-up |

**The demonstrative move (automation, by hand or recorded):**
Hold **C3** for ~4.7 s and drag **Osc 1 Pos** smoothly **0.0 → 1.0** over ~4.5 s.
You should hear the timbre walk **sine → triangle → saw → square** while pitch and loudness stay dead constant.

Final check: one held pitch, constant loudness, brightness rising monotonically as Position scans. Flat brightness ⇒ the Position scan didn't take.

**Save:** right-click the Wavetable title bar → **Save Preset** → `presets/wt-position-by-hand.adv`.
