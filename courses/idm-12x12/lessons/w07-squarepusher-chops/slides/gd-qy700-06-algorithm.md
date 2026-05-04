# Underlying algorithm — AWM tone generation

The QY700's internal voice is <term key="awm_synthesis">AWM (Advanced Wave Memory)</term>: PCM sample playback followed by a per-voice envelope + filter stage. Roads 1996 covers the same architecture as generic sample-playback synthesis; Yamaha's twist is the ROM library and the low-cost filter. <Citation bib="roads_computer_music_tutorial" />

Signal flow inside one AWM voice:

```
PCM ROM sample → pitch shifter → LPF → VCA (envelope) → output bus
```

It is not why you care about the QY700 — Jenkinson routed the interesting voices (TX81Z, FS1R, S6000) externally. You care about the **sequencer** side:

- **480 PPQN resolution.** Every 1/16 is subdivided into 120 ticks. Per-step timing offsets are quantized to this grid — the finest groove shift available is ~1 ms at 125 BPM.
- **32 tracks at 48-voice polyphony.** Hard ceiling; dropped notes at peak load are a period signature.
- **Step entry is the native mode.** Real-time record exists; nobody in Jenkinson's camp used it.
