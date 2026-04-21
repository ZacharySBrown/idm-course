[pause 300ms] The source pool, this week. *Heather*.

Billy Cobham, *Spectrum*, 1973. We run the track through stemforge with the section-stratified strategy, two-bar length. The recipe is `w10-heather-variation-source`, and it lives in recipes.yaml if you want to re-run.

The command: stemforge forge, input `grooves/Heather.wav`, strategy section-stratified, n-bars equals two. The output is a directory called `heather_loops/`, and every file in it is tagged by arrangement region. `intro_` prefix for candidates the classifier thinks belong in an intro. `a_` for A-section candidates. `b_`, `peak_`, `outro_`.

[pause 400ms]

Why this material. Cobham's early-seventies drumming has long phrased sections that survive chopping. His timing sits wide of the grid — the kick is pushed, the snare pulls, the hats float. When you chop at two bars, you are capturing a full rhythmic phrase, not a sixteenth-note loop. The chop keeps Cobham's swing without locking you into his specific kit.

It is also — and this is a craft argument, not a critical one — one of the last long-form fusion grooves before fusion became a genre label that meant *uncool*. The recordings are punchy. The stereo image is usable. The bass is loud.

[pause 300ms]

How to use it, practically. Two paths.

Path A — drop the `a_*.wav` candidates into a Simpler, set to Slicing mode. Now every slice is a pad. Trigger from the Drum Rack grid. You have a hand-playable version of Cobham.

Path B — drop the two-bar files directly onto an audio clip slot with Follow Actions 2.0 enabled. Build a pool. Let Live deal variants. That is the next slide, and it is where this material really pays off.

[pause 400ms]

Caveat. Section-stratified curation is a classifier. It guesses at arrangement role from energy profile and spectral features. It is not a composer. Re-audition the `a_` tagged files before you commit — some of them are mis-tagged, and some are mis-tagged in a way that is actually correct for your track. The tag is a hint, not a contract.
