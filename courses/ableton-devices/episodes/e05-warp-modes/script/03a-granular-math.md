Stop two. The physics of how it breaks. We just spent forty years on the grain — so what is the grain actually doing, by ear?

[pause 400ms]

Granular stretching tiles the output with overlapping grains — short windowed segments pulled out of the input — and the trick is that the read rate and the write rate are decoupled. The write pointer marches forward at one speed; the read pointer marches at another. For a stretch, the read pointer moves slower than the write pointer, which means the engine runs out of fresh material and has to repeat what it already has. To compress, it moves faster, and skips. That is exactly the manual's phrasing: Live's granular modes "manipulate time by repeating or omitting segments of the audio." Slow down equals repeat. Speed up equals omit.

[pause 500ms]

And the character — whether it sounds clean or buzzy — comes from one relationship: the size of the grain against the signal. If the grain lines up with the pitch period, the stretch stays clean. If the grain ignores the signal and falls at arbitrary phases, every seam between grains is a little discontinuity, and you hear those seams as a tone.

[pause 500ms]

Listen. This is one sustained note, warped to four hundred percent in Texture — the signal-blind mode — with a small grain. Then I drag the Grain Size up. Listen to the buzz move.

[cue: granular-seam-grainsize]

That buzz is the seam between grains. When the grain got bigger, the seams came less often, so the buzz dropped in pitch — the grain rate fell. That is the entire mechanism, audible in one drag. Grain size sets grain rate, grain rate is a pitch, and that pitch is the sound of the algorithm tiling.
