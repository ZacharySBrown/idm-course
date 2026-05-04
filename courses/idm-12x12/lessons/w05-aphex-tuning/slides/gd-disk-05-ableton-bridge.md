# The Ableton bridge — Collision, piano VST, parallel click bus

Simulate the Disklavier in Live 12 without owning one. <Citation bib="ableton_live_12_manual" />

Signal flow:

```
MIDI clip ─┬─> Piano VST (NI Noire or Ableton Grand Piano)  ─┐
           │                                                  ├──> Master
           └─> Collision (tuned for solenoid click)  ─> HPF ──┘
                    + Drum Rack of piano-mechanism samples
```

Device breakdown:

- **Collision** — Live's built-in physical-modelling instrument. Set Mallet layer ON, Mallet Stiffness 95%, Mallet Noise 40%. Resonator type: Plate, Decay 200ms, Material 80%. This is the solenoid click — short, metallic, velocity-scaled. <Citation bib="ableton_live_12_manual" />
- **Piano VST** — NI Noire or any felted-piano patch carries the tone; Collision carries the mechanism. <Citation bib="ni_noire_docs" />
- **Parallel click bus** — route Collision to its own audio return. HPF at 600 Hz so it reads as click, not pitched note. Sidechain the return's compressor off the kick if needed.
- **Velocity mapping** — duplicate the MIDI clip onto both tracks so Collision and the piano always fire together. Use Velocity Shaper (Max for Live) to send low velocities to Collision-only — the simulated "soft-pedal click without full hammer strike."

What this will not capture: the body-cavity ~70 Hz woof. Add a Drum Rack with low-velocity kick samples pitched to ~70 Hz on a parallel send to fake it. Not identical. Close enough.

Budget-$0 Disklavier. The tradeoff: no physical strings, no Helmholtz, no Nagra tape saturation. All three matter; none are showstoppers for a demo.
