# Exercise B — nested LFOs modulating each other

The Navier-Stokes territory Booth and Brown were chasing — slow, continuous, non-repeating modulation — is achievable today with one Max for Live device and an afternoon.

Build it:

1. New MIDI track, Wavetable or Meld instrument, one sustained note held by a 64-bar MIDI clip.
2. Insert Max for Live **LFO** device #1 on the track. Routing: LFO1 output → LFO2 **Rate** parameter.
3. Insert Max for Live **LFO** device #2 on the same track. Routing: LFO2 output → Wavetable filter cutoff.
4. Now insert Max for Live **LFO** device #3. Routing: LFO3 output → LFO1 Rate. **The three LFOs modulate each other's rates in a cycle.**
5. Set all three to different base rates (LFO1: 1/4, LFO2: 1/3, LFO3: 1/8) and different depths.
6. Play. The filter cutoff will move in a way that is fully deterministic (no random) but non-periodic at any listenable timescale.

**Deliverable.** A 32-bar recording of the sustained note with the self-modulating filter. The render is reproducible — same clip, same automation, same output. Procedural, not random.

This is the poor-person's Lorenz attractor. The next deep-dive slide (d02 / gd-maxmsp-13) gives you the real thing.

`bib:cycling74_max_msp_docs` · `bib:ableton_cv_tools`
