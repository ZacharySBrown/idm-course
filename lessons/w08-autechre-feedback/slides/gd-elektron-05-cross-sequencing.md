# Technique continued — cross-sequencing Machinedrum and Monomachine

Autechre did not run the two boxes as two independent sequencers. They cross-sequenced them. The receipts for the exact routing are community consensus on Elektronauts and WATMM (flag: not an officially documented patch — forum-reconstructed from live-set video analysis), but the general move is well documented:

- **Machinedrum LFO → Monomachine CC input.** Use the Machinedrum's per-track LFO (shape, rate, depth) as a modulator routed via MIDI CC to a Monomachine filter cutoff. The drum track "plays" the synth filter.
- **Monomachine MIDI sequencer tracks → Machinedrum trigger input.** Monomachine has two MIDI-out tracks; route one to a Machinedrum drum track's trigger. The synth pattern triggers the kick.
- **Nord G2 as glue.** The G2 takes in CC data from both, applies chaotic modulation (built-in Lorenz-style oscillators), and routes back.

Booth in SOS April 2004 on the broader studio philosophy: *"Stuff can go back in and back out as many times as we want it to."* The same routing mindset, implemented in a MIDI mixer box.

`bib:sos_autechre_april_2004` · `bib:elektronauts_autechre_threads` · `bib:watmm_forum_general`
