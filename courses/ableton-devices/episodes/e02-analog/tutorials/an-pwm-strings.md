# Patch tutorial — `an-pwm-strings`

**Preset:** `presets/an-pwm-strings.adv`  ·  **Concept:** LFO → Pulse Width = one oscillator behaving like two (PWM strings)

> A single rectangular oscillator on a held chord, an LFO slowly sweeping the pulse width: a lush, chorusing string-ensemble shimmer from one oscillator and no chorus effect.
>
> **You should hear:** A steady chord with a slow chorusing/phasing movement; no second oscillator, no chorus device.

Build from a **freshly loaded default Analog**. One parameter per step. Filter Freq is NORMALIZED 0–1 (NOT Hz); `O1 PW < LFO` is the LFO→pulse-width depth (−1..1).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | OSC 1 | OSC1 On/Off | On |  |
| 2 | OSC 1 | OSC1 Shape | Rect | A hollow square |
| 3 | OSC 1 | OSC1 PW | 0.5 (LFO modulates around this center) |  |
| 4 | OSC 1 | OSC1 Balance | 1.0 |  |
| 5 | OSC 1 | O1 PW < LFO | 0.35 (LFO1 → OSC1 pulse-width depth) | The pulse width begins to move |
| 6 | OSC 2 | OSC2 On/Off | Off | One oscillator only |
| 7 | Noise | Noise On/Off | Off |  |
| 8 | LFO 1 | LFO1 On/Off | On |  |
| 9 | LFO 1 | LFO1 Shape | Sine |  |
| 10 | LFO 1 | LFO1 Sync | Hertz (free-running) |  |
| 11 | LFO 1 | LFO1 Speed | 0.15 (slow chorus rate) | A slow chorusing shimmer |
| 12 | Filter 1 | F1 On/Off | On |  |
| 13 | Filter 2 | F2 On/Off | Off |  |
| 14 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 15 | Filter 1 | F1 Freq | 0.787 (≈ 4000 Hz; gentle top-end taming) |  |
| 16 | Filter 1 | F1 Resonance | 0.05 |  |
| 17 | Filter 1 | F1 Drive | Off |  |
| 18 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 19 | Amp Env 1 | AEG1 Attack | 0.35 (≈ 300 ms — slow string swell) | A soft swell-in |
| 20 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 21 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 22 | Amp Env 1 | AEG1 Rel | 0.5 (≈ 600 ms) |  |
| 23 | Global | Key Error | 0.08 (small drift adds ensemble width) | A wider ensemble |

**Play:** hold a chord (C3 / Eb3 / G3). The single rect osc widens into a chorusing string ensemble from the LFO→PW motion alone.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-pwm-strings` into `presets/`._
