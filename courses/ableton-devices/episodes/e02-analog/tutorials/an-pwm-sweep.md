# Patch tutorial — `an-pwm-sweep`

**Preset:** `presets/an-pwm-sweep.adv`  ·  **Concept:** Pulse width → harmonic content (even harmonics appear)

> One rectangular oscillator, filter wide open, the duty cycle swept from 50% (square, odd-harmonic) down to a narrow pulse. Even harmonics fade in and the spectrum spreads upward — no filter touched.
>
> **You should hear:** One held note (C3), constant pitch and loudness, the tone thinning and nasalizing as the pulse narrows.

Build from a **freshly loaded default Analog**. One parameter per step; the right column is your self-check. Filter Freq values are NORMALIZED 0–1 (NOT Hz).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note (default) |
| 1 | OSC 1 | OSC1 On/Off | On | The oscillator sounding |
| 2 | OSC 1 | OSC1 Shape | Rect | A hollow square tone |
| 3 | OSC 1 | OSC1 PW | 0.5 (= 50%, a symmetric square) | An odd-harmonic-only square |
| 4 | OSC 1 | OSC1 Octave | 0 |  |
| 5 | OSC 1 | OSC1 Detune | 0.5 (= 0 cents) |  |
| 6 | OSC 1 | O1 Sub/Sync | 0.0 (sub off) |  |
| 7 | OSC 1 | OSC1 Balance | 1.0 (full to F1) |  |
| 8 | OSC 2 | OSC2 On/Off | Off | Single oscillator |
| 9 | Noise | Noise On/Off | Off |  |
| 10 | Filter 1 | F1 On/Off | On |  |
| 11 | Filter 2 | F2 On/Off | Off | Only F1 in the chain |
| 12 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 13 | Filter 1 | F1 Freq | 1.0 (≈ max — effectively bypassed) | Filter does NOT color the tone |
| 14 | Filter 1 | F1 Resonance | 0.0 |  |
| 15 | Filter 1 | F1 Drive | Off |  |
| 16 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 17 | Amp Env 1 | AEG1 Attack | 0.03 (≈ 5 ms) | A near-instant start |
| 18 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 19 | Amp Env 1 | AEG1 Sustain | 1.0 (full) | Steady held level |
| 20 | Amp Env 1 | AEG1 Rel | 0.15 (≈ 80 ms) |  |
| 21 | Global | Key Error | 0.0 (clean spectrum) | A stable square |

**Sweep (the ONE variable):** automate **OSC1 PW** from **0.5 → 0.08** over ~4 s while holding C3. Even harmonics rise and the tone thins/nasalizes as the pulse narrows.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-pwm-sweep` into `presets/`._
