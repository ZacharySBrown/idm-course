# Ableton bridge — Max for Live is Max embedded

Max for Live is literally the same Max runtime running inside Ableton. A .amxd file is a Max patch plus a small wrapper that exposes Live API objects.

Three kinds of M4L device:

- **Max MIDI Effect** — between a MIDI input and an instrument. For generative MIDI (Markov, Euclidean, probability).
- **Max Audio Effect** — inserts in the audio chain. For custom DSP (gen~-based saturators, grain engines, filters).
- **Max Instrument** — a synth. Receives MIDI, outputs audio.

The Live API exposes the session tree: tracks, clips, devices, parameters, transport. A M4L device can read and write any Live parameter by walking the tree. This is how Dillon Bastan's data.mod writes modulation into any mapped parameter — it opens a Live API connection and pushes values.

Upshot: every Max patch you can think of can be ported to M4L. The Confield sequencer skeleton above (5 Max-rate objects + gen~ drum synth) becomes a single .amxd instrument. Drop it into a MIDI track, done.

`bib:ableton_live_12_manual` · `bib:cycling74_max_msp_docs`
