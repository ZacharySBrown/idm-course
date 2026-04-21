# Technique — p-locks as live-programmed variation

The move is: **program a static pattern, then lock a single parameter to a different value on every step.**

Example — classic Machinedrum snare variation:

1. Track 2 (SD), machine type E12, sample slot 17 (a rimshot).
2. Program trigs on steps 4, 8, 12, 16 — the backbeat.
3. FUNC + step 4 → SYN/Pitch encoder → +0. Step 8 → +5. Step 12 → +2. Step 16 → –3.
4. Hit play. The snare backbeat is now a four-pitch melodic fragment. No randomness. Every step deterministic, every step different.

The Autechre extension, per Elektronauts forum analysis of live sets: **p-lock every knob on every step, then vary sequencer length per track** (track 1 plays 16 steps, track 2 plays 15 steps, track 3 plays 13 steps). The pattern repeats only at the LCM — 16×15×13 = 3120 steps, or about 13 minutes at 120 BPM.

That is "procedural, not random" implemented in an interface. The variation is composed.

`bib:elektron_machinedrum_manual` · `bib:elektronauts_autechre_threads`
