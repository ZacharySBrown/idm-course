# Classic mode — chromatic play, warp on

Classic is Simpler's <term key="chromatic_chopping">chromatic playback</term> mode. The sample is pitched up or down by the incoming MIDI note, interpolating with the warp engine so that timing and pitch can be decoupled.

What actually happens under the hood:

- Incoming note number sets the ratio against the **root key** (C3 by default).
- If **Warp** is off, Simpler does straight varispeed — pitch and time move together, like pulling tape faster. A vocal chunk an octave up is half as long.
- If **Warp** is on — Beats, Tones, Texture, Re-Pitch, or Complex Pro — the warp engine time-stretches so the sample stays locked to project tempo while pitch tracks the keyboard.
- **Amp envelope**, **filter**, **LFO**, **voicing** (Mono / Poly / Legato) — standard subtractive front-end.

Use Classic for one-shot melodic sources — vocal chops, flute stabs, pitched hits — any time you want chromatic keyboard play over a pitched fragment.

[ref: bib:ableton_live_12_manual]
