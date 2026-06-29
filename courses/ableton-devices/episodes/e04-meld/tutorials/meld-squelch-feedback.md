# Patch: Squelch Feedback  (preset: presets/meld-squelch-feedback.adv)

**Demo:** `meld-squelch-feedback`  ·  **Slide:** `03b-fm-the-macro-way`  ·  **Structure:** sweep
**Concept demonstrated:** FM operator feedback → harmonic complexity, exposed as one macro — the Ep1 (Operator) feedback physics, collapsed into a single knob.
**Render status:** FULLY RENDERABLE headless — the sweep moves a real device param (`A Osc Tone` = Feedback). No matrix, no MPE.

Build from a **freshly loaded default Meld**. One parameter per step. The ONE swept variable is `A Osc Tone` (the FM Bass Feedback macro); everything else is held.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine B | `B On` | Off (0) | Engine B silent |
| 2 | Engine A | `A On` | On (1) | Engine A only |
| 3 | Engine A | `A Osc Type` | **17 = FM Bass (Squelch)** | A pure-ish FM sine bass on the held note |
| 4 | Engine A | `A Osc Shape` (macro 1 = FM Amount) | 0.65 (held fixed) | A fixed amount of FM brightness |
| 5 | Engine A | `A Osc Tone` (macro 2 = Feedback) | 0.0 (start of sweep — THE variable) | A clean sine at the start |
| 6 | Engine A | `A Transpose` | 0 | (no offset) |
| 7 | Engine A | `A Detune` | 0.50 (0 cents) | Centered tuning |
| 8 | Engine A | `A Filter On` | On (1) | (routing) |
| 9 | Engine A | `A Filter Type` | **0 = Analog** | Transparent filter |
| 10 | Engine A | `A Filter L-B-H-N` | 0.0 (lowpass) | Lowpass response |
| 11 | Engine A | `A Filter Freq` | 1.0 (open) | Open so the feedback harmonics are audible |
| 12 | Engine A | `A Filter Q` | 0.0 | No resonance |
| 13 | Engine A | `A Amp Attack` | 0.05 | Fast note start |
| 14 | Engine A | `A Amp Sustain` | 1.0 | Holds at full level |
| 15 | Engine A | `A Amp Release` | 0.20 | Short tail |
| 16 | Engine A | `A Volume` | 0.70 | Solid level |
| 17 | Global | `Drive` | 0.10 | A touch of squelch grit |

**Sweep:** hold `C2`; ramp `A Osc Tone` (Feedback) 0.0 → 1.0 over ~4.5 s.

**Final check:** pitch and loudness roughly constant; the tone roughens sine → saw → noise-edge as the feedback rises.
**Analyzer:** RMS roughly flat (±2 dB); spectral spread / harmonic count rises monotonically start→end.

**Save:** save at the start of the sweep (Feedback = 0.0) → right-click Meld → **Save Preset** → `presets/meld-squelch-feedback.adv`.
