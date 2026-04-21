Texture mode. [pause 200ms] This is the mode that does not get written about enough, and the one that, in practice, separates producers who treat Warp as a utility from producers who treat it as an instrument.

Under the hood: polyphonic granular. The clip is chopped into tiny overlapping grains, each grain is played at the rate that matches the target tempo, and there are two creative controls.

**Grain Size.** In milliseconds. [pause 150ms] Fifty milliseconds is the default-ish sweet spot — grains blend into each other, the result feels smooth and pad-like. Drop to ten milliseconds and you get glitchy, chattering, broken-CD character. Anywhere in between is a legitimate creative choice. Go above a hundred milliseconds and the grains start to be audible as discrete events; useful for rhythmic stutter.

**Flux.** Zero to one hundred percent. [pause 150ms] This is the fun one. Flux controls the amount of *random variation* in where each grain samples the source. Flux zero: grains are perfectly aligned, playback is stable, locked-phase, almost Complex-Pro-like. Flux at sixty percent: the grains start to drift — each pass through the clip samples slightly different material. Flux at one hundred: the playhead is effectively a cloud, continuously evolving, and the clip never repeats identically. [pause 200ms] That last behavior is what you want. Source material you can't afford to get bored with.

Practical move — take the `hallogallo_other` stem, the guitar-plus-drift layer. Stretch it two-x by halving the segment BPM. Mode Texture. Grain fifty milliseconds. Flux sixty. [pause 200ms] You now have a sixteen-bar pad that tracks the original harmonic content but never loops. Drop it on a return, filter it, send a reverb to it. Free texture bed.

At the other extreme — Flux one hundred with Grain ten milliseconds applied to a drum stem produces a noise wash. It stops sounding like drums and starts sounding like a handful of gravel thrown against glass. [pause 100ms] Which is useful. *Not-the-source* is often the point.

One warning. With Flux above zero, the output never prints identically twice. If you need the render stable — bounce to audio before you commit to an arrangement.

Cite — Live 12 manual; stemforge repo.
