# Technique — Confield-era patches

SOS April 2004, Booth: the *Confield* compositional move was **nested analogue sequencers emulated in Max**, with fluid-math modulation routed to filter, pan, pitch.

Reconstructed patch shape (community consensus, not a leaked .maxpat):

- **Sequencer 1** — `counter` + `coll` (a data store), outputs a CV-like value per step. Step period 1/16.
- **Sequencer 2** — identical structure, but its *rate* is set by the output of Sequencer 1. When Sequencer 1 outputs a low value, Sequencer 2 runs slow. When high, fast.
- **Sequencer 3** — gates Sequencer 2's output. When Sequencer 3 is low, Sequencer 2's notes are muted. Sequencer 3's rate is set by an LFO driven by a Navier-Stokes fluid simulation rendered in Jitter.
- **Final stage** — a gen~ drum synth, triggered by the Sequencer 2 output. The kick pitch is p-locked to Sequencer 1's current value.

Output: a drum pattern that evolves over minutes, never repeats in the first 20, is *fully deterministic*. Record 20 minutes to disk. Edit down. Ship.

"That is the patch." is an oversimplification — the real patches have dozens more objects — but this is the compositional skeleton.

`bib:sos_autechre_april_2004` · `bib:watmm_forum_general` · `bib:cycling74_max_msp_docs`
