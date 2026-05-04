# Drum Rack signal path — from MIDI to audio out

A Drum Rack is MIDI-in, audio-out, with 128 parallel chains inside. Read the diagram left-to-right.

- MIDI enters the rack. Every chain receives every note.
- Each chain has a **Receive Note** — a single MIDI note (or note range). Only notes matching the receive pass through to that chain's devices.
- Inside a chain: the instrument (usually <term key="simpler">Simpler</term>), optional insert effects (EQ Eight, Saturator, a Utility), optional <term key="send">sends</term> to the Return chains.
- Return chains (the rack's own, not the project's) are shared across all pads — one reverb, one delay, fed by the S-knobs on each pad.
- **Choke groups** operate at the MIDI layer, not the audio layer — when pad A fires, any pad in the same choke group receives a note-off. Closed-hat chokes open-hat by muting the source of its sound.
- Audio sums to the rack's output, or each pad can route to its own Live audio output for multi-out processing.

The rack is not a sampler. The sampler is on the pad. The rack is the router.

[ref: bib:ableton_live_12_manual]
