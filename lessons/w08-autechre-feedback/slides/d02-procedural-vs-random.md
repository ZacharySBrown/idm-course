# Procedural vs random — same generator, two runs

Imagine the same 16-step rhythm generator, run twice.

**Run A — random.** Each step's probability rolls a fresh `Math.random()` at playback. Render 1 gives you hits at 1, 4, 7, 9, 13. Render 2 gives you hits at 2, 5, 8, 10, 11, 15. The pattern is different every render. Booth's complaint lives here: you cannot play this system, you can only wait for a take you like.

**Run B — procedural.** Steps are chosen by a <term key="rule_based">rule-based modulator</term> — a counter, an LFO quantized to step positions, a <term key="markov_chain">Markov chain</term> with fixed transition weights. Render 1 and render 2 produce the *same* pattern. Change the seed or the weights — the pattern changes predictably. You can play this system.

The Autechre rule: **if the render isn't reproducible, it isn't finished.** Commit the run. The run is the piece.

`bib:sos_autechre_april_2004` · `bib:watmm_forum_general`
