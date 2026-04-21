Third case study. The one you can deploy tomorrow on any existing project. `Tape Notes #140`, the KH-labeled track "Looking At Your Pager," and Hebden's admission that he uses the same trick on *"pretty much everything"* on *Three*.

[pause 400ms]

Here is the quote, verbatim from the episode. *"Get some sort of midi pattern together and then put some sort of randomization on the velocity of the midi notes. So I've put the velocity, and I've made it random fifteen percent. And then I'm asking it also to fifteen percent of the time to pick one of the notes and play either an octave up or an octave below. And it stops the pattern being totally repetitive. You just get these little sparkles and twinkles."*

[pause 500ms]

Two parameters. That is the whole trick.

[pause 300ms]

Parameter one — velocity variance of plus-or-minus fifteen percent around whatever the note's current velocity is. Every trigger, Live picks a random value inside that band.

[pause 300ms]

Parameter two — per-note probability of fifteen percent that the note transposes by one octave, up *or* down.

[pause 400ms]

The consequence he flags himself in the interview is structural and worth dwelling on. He says — *"the version on the vinyl will be different probably to the version that's digitally available."* Because the master was rendered off a probabilistic source, and he rendered the vinyl master on a different day from the digital master, the two objects have *different notes* in them. Both are legitimate. Neither is the canonical version.

[pause 500ms]

That is a huge philosophical move dressed up as a casual workflow tweak. The album is not a fixed artifact. It is a *slice* of a generative system. Two slices exist, commercially. Many more were rendered during the session and never shipped.

[pause 400ms]

We are going to wire this up in Ableton on the next slide. Two mechanisms, both native to Live 12 — the Velocity Range handle in the clip editor, and the Chance field plus a duplicated octave-shifted layer. No third-party devices required. `Ableton Live 12 Reference Manual`.
