# Why Hallogallo is the test clip

NEU — "Hallogallo" (1972). Klaus Dinger on drums, Michael Rother on guitar, Conny Plank at the desk. Ten minutes and six seconds of motorik: four-on-the-floor kick, closed hat on every eighth, snare on the two and the four, zero fills.

For our purposes it is almost ideal material:

- **Repetitive** — a warp artifact repeats too, so you can hear it clearly
- **Transient-rich** — every kick and snare is a separate event to smear or not smear
- **Drone-adjacent** — the guitar layer is effectively a static texture, which is what Texture mode eats

Recipe: `stemforge:w04-hallogallo-warp-ab`. The source WAV for the Hallogallo track (see `stemforge-demo-material/recipes.yaml`) gets split with the default pipeline, no slicing — you end up with a clean `drums` stem and an `other` stem (guitar plus drift). We work off the drums stem for the warp A/B; we keep the `other` stem in the back pocket for Texture mode later.

Cite: `bib:stemforge_repo`.
