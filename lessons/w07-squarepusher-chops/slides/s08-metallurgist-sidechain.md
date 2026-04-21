# The Metallurgist — sidechain as composition

Jenkinson, on "The Metallurgist": *"The bass drum is the sidechain source, and each time it drops, the dynamics for other instruments are being changed to permit a sense of fluidity."* <Citation bib="tape_op_89" />

Read that again. **All** other instruments. The kick does not just duck the bass. It modulates the dynamics of the pads, the leads, the vocal, the noise — the entire mix becomes one rhythmic envelope.

Sidechain stops being a mix-bus trick and becomes the composition.

## Ableton recipe — Metallurgist bus

1. Route the kick to a return track named **kick-trigger**, pre-fader, no audio output.
2. On every other instrument track, insert **Compressor** → Sidechain ON → Source: **kick-trigger**. <Citation bib="ableton_live_12_manual" />
3. Depth varies per track. Kick → sub: 6 dB ducking, 5 ms attack, 80 ms release. Kick → pad: 3 dB, 20 ms attack, 200 ms release (breathing). Kick → lead: 1 dB, 50 ms attack, 30 ms release (pumping glint).
4. Optional: **Glue Compressor** on the master with sidechain from kick, 1 dB of grab — the whole mix moves together.

The result is a mix that breathes on the one. Nothing in it is mixed; everything in it is composed.
