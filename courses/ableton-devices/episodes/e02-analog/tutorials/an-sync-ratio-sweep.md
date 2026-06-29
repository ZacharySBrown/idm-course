# Patch tutorial — `an-sync-ratio-sweep`

**Preset:** `presets/an-sync-ratio-sweep.adv`  ·  **Concept:** Hard-sync Ratio → tearing/formant sweep (the screaming sync lead)

> One held note, the sync Ratio swept up: the waveform is hard-restarted faster and faster, the harmonics tearing upward into the classic screaming sync lead. With **OSC1 Mode = Sync**, the Sub/Sync slider (`O1 Sub/Sync`) acts as the sync-ratio depth.
>
> **You should hear:** Constant fundamental pitch; a formant/harmonic peak sweeps upward as the sync ratio rises.

Build from a **freshly loaded default Analog**. One parameter per step. Filter Freq is NORMALIZED 0–1 (NOT Hz).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | OSC 1 | OSC1 On/Off | On |  |
| 2 | OSC 1 | OSC1 Shape | Saw |  |
| 3 | OSC 1 | OSC1 Mode | Sync (Sub/Sync slider now = sync ratio) |  |
| 4 | OSC 1 | O1 Sub/Sync | 0.0 (sync ratio depth; swept below) | No sync tearing yet |
| 5 | OSC 1 | OSC1 Balance | 1.0 |  |
| 6 | OSC 2 | OSC2 On/Off | Off |  |
| 7 | Noise | Noise On/Off | Off |  |
| 8 | Filter 1 | F1 On/Off | On |  |
| 9 | Filter 2 | F2 On/Off | Off |  |
| 10 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 11 | Filter 1 | F1 Freq | 1.0 (wide open so sync content is unmasked) |  |
| 12 | Filter 1 | F1 Resonance | 0.0 |  |
| 13 | Filter 1 | F1 Drive | Off |  |
| 14 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 15 | Amp Env 1 | AEG1 Attack | 0.03 (≈ 5 ms) |  |
| 16 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 17 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 18 | Amp Env 1 | AEG1 Rel | 0.2 (≈ 120 ms) |  |
| 19 | Global | Key Error | 0.0 |  |

**Sweep (the ONE variable):** hold C3 and automate **O1 Sub/Sync** from **0.0 → 1.0** over ~4.5 s. The fundamental stays fixed while a formant peak tears upward — the screaming sync lead.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-sync-ratio-sweep` into `presets/`._
