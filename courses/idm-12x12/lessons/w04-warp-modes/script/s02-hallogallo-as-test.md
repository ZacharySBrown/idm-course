Hallogallo. [pause 200ms] NEU, 1972 — stylized with a trailing bang on the record sleeve, which we will omit in conversation. Track one, side one of their self-titled debut. Ten minutes and six seconds. Klaus Dinger on drums, Michael Rother on guitar, Conny Plank engineering. The guitar drifts; the drums do not.

The drum pattern is what Germans call *motorik* — "the motor beat." Four-on-the-floor kick. Closed hi-hat on every eighth note. Snare on two and four. Nothing else. No fills. No accents. No dynamics. It is the pattern you would write if a robot asked you to demonstrate rock rhythm.

That lack of variety is *exactly* why it is useful to us. [pause 200ms]

Three reasons I picked this clip.

First — repetition. If the warp algorithm introduces an artifact, say Complex Pro rounding the leading edge of the kick — that artifact repeats every beat. You hear it within two bars. You can A/B it. A clip with lots of fills and ghost notes hides artifacts inside the performance. Hallogallo has nowhere to hide.

Second — transient content. Every kick and every snare is a distinct event. If Beats mode preserves them, you will hear that. If Complex Pro smears them, you will hear that too. Sparse, percussive, consistent.

Third — the *other* stem. The guitar is effectively a drone. Long sustained tones, no discrete attacks. That is exactly the material Texture mode is built for. When we get to Flux and Grain Size, we will swap from the drum stem to the other stem and watch Texture mode do its job.

The stemforge recipe is `w04-hallogallo-warp-ab`. It runs Demucs on the source file — Hallogallo-NEU-dot-wav — with the default pipeline and *no slicing*. We want the full stems, unchopped. You get `hallogallo_drums.wav` and `hallogallo_other.wav`. [pause 200ms] Check the build directory, drag the drums stem into a new set, and we'll meet on the next slide.

Cite — stemforge repo, at `zacharysbrown/stemforge`. [pause 300ms]
