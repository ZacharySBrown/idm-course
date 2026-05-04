Wiring the Hebden randomization in Live 12. `Ableton Live 12 Reference Manual` for both features.

[pause 400ms]

Start with the velocity piece. Select your MIDI clip. Open the clip view. Each note has two handles in the velocity lane — the velocity itself, and a *range* handle above or below it. The range handle sets the maximum random deviation applied every time that note plays.

[pause 400ms]

For Hebden's fifteen-percent target, you want the range to equal roughly fifteen percent of the note's current velocity. Easiest path — select all notes, grab any range handle, drag it. Live scales the range proportionally across the selection. Set it to roughly one-seventh of the velocity value for the fifteen-percent target.

[pause 300ms]

Now every trigger Live draws a uniform random velocity inside that band. Re-trigger the clip five times and listen. If every hit is identical, the range handle did not take. Common mistake is clicking the velocity handle instead of the range handle above it.

[pause 500ms]

Second piece — the fifteen-percent octave shift. This is where most students overthink it. The cleanest path is *duplicate the notes up an octave and put Chance fifteen on the duplicates*.

[pause 400ms]

Steps. Select all notes in your clip. Duplicate in place — Command-D on Mac. Select the duplicates. Shift plus arrow-up twelve times to move them up an octave. With those duplicates still selected, open the Chance field in the note editor. Set it to fifteen percent. Leave the originals at one hundred percent chance.

[pause 400ms]

Now, fifteen percent of the time, the duplicated note fires *instead of* — actually, *in addition to* — the original. Which means at that probability you are playing both the note and its octave. Which is not exactly Hebden's wording of *"either an octave up or an octave below"* — he is doing instead-of, not in-addition-to. If you want strict instead-of, delete the originals at the same beat positions where you placed duplicates. Or use the MIDI Pitch Transformer — Transform menu, Pitch — with a probabilistic setting and bake.

[pause 500ms]

Either path. The duplicated-layer one is inspectable. I prefer inspectable. Run it. Bounce. You will hear the sparkle.
