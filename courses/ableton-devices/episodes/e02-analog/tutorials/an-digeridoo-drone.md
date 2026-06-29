# Patch tutorial — `an-digeridoo-drone`

**Preset:** `presets/an-digeridoo-drone.adv`  ·  **Concept:** Play the self-oscillating filter as an instrument (the Digeridoo rebuild)

> Oscillators off, Reso near max, a 24 dB LP ringing at its cutoff, **noise-excited** and **key-tracked** so the keyboard plays it — then an LFO sweeps the cutoff for the drone. The filter IS the oscillator (reedy/breathy, didgeridoo-like). Aphex's "Digeridoo" (1992) — there is no real didgeridoo.
>
> **You should hear:** A reedy pitched drone (dominant near-pure ring over a faint breath of noise) whose pitch follows the played note, with a slow LFO wobble.

> **Why noise, not a sine:** Analog's filter will NOT self-oscillate from bare resonance with the oscillators off (you get silence). A low continuous NOISE feed excites the high-Q key-tracked filter so it rings at its cutoff — making the pitched drone provably the *filter*, not an oscillator.

Build from a **freshly loaded default Analog**. F1 Freq is NORMALIZED 0–1 (NOT Hz); `F1 Freq < Key` (−1..1, 1.0 = full key-track), `F1 Freq < LFO` (−1..1).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | OSC 1 | OSC1 On/Off | Off (the filter is the only pitched source) | Near silence (no osc) |
| 2 | OSC 2 | OSC2 On/Off | Off |  |
| 3 | Noise | Noise On/Off | On (broadband noise EXCITES the filter) | A breath of noise |
| 4 | Noise | Noise Level | 0.35 (low feed — rings, doesn't swamp) |  |
| 5 | Noise | Noise Balance | 1.0 (noise routed fully into F1) |  |
| 6 | Filter 1 | F1 On/Off | On |  |
| 7 | Filter 2 | F2 On/Off | Off |  |
| 8 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 9 | Filter 1 | F1 Freq | 0.36 (≈ 330 Hz base; key-track + LFO move it) |  |
| 10 | Filter 1 | F1 Resonance | 0.95 (very high Q — the filter rings/sings) | A near-pure ring emerges |
| 11 | Filter 1 | F1 Drive | Sym1 (a little body/reed buzz) |  |
| 12 | Filter 1 | F1 Freq < Key | 1.0 (cutoff tracks MIDI pitch ⇒ it's an oscillator) | The ring follows the keyboard |
| 13 | Filter 1 | F1 Freq < LFO | 0.25 (LFO1 → cutoff = the drone wobble) | A slow wobble on the ring |
| 14 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 15 | LFO 1 | LFO1 On/Off | On |  |
| 16 | LFO 1 | LFO1 Shape | Sine |  |
| 17 | LFO 1 | LFO1 Sync | Hertz (free-running) |  |
| 18 | LFO 1 | LFO1 Speed | 0.5 (≈ mid free rate — the drone wobble) |  |
| 19 | Amp Env 1 | AEG1 Attack | 0.1 (≈ 50 ms) |  |
| 20 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 21 | Amp 1 | AMP1 Level | 0.9 (a ringing-filter drone is quiet; lift it) | A solid drone level |
| 22 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 23 | Amp Env 1 | AEG1 Rel | 0.3 (≈ 200 ms) |  |
| 24 | Global | Key Error | 0.0 |  |

**Play:** C1 then G1 — the pitched ring should track the played note (proving it's the filter), with the LFO wobble on top.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-digeridoo-drone` into `presets/`._
