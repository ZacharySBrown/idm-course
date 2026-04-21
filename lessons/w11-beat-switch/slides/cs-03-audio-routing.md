# How the Rack routes audio — the mental model

- MIDI enters the Rack at the top. It fans out to every chain whose zone contains the current Chain Selector value. Chains outside the selector value do not receive MIDI — they stop producing sound.
- Audio from each active chain is summed internally and exits the Rack as one stereo output. The Rack itself is a bus.
- **Key mental-model fact:** switching chains does not re-trigger envelopes on the destination chain. If chain 2 has an 800 ms attack pad and you flip to it on a downbeat, you will hear the attack starting from zero. Plan for this or commit the destination chain first.
- **Zone fades matter.** A zone with a 4-unit fade region will crossfade in over four selector values — so if you automate the macro from 40 to 60 over one bar, you get a 1-bar crossfade. Set fades to 0 for a hard cut; set fades wide for a DJ blend.
- `bib:ableton_live_12_manual` diagrams this in the *Chains* section. See d03 in this lesson for a simplified flow.
