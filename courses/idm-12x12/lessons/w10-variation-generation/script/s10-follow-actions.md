[pause 300ms] Follow Actions 2.0.

Live 12 shipped this — per-scene probability, per-clip probability, legato triggering, and an *Any* option that lets a deck of clips play in a non-repeating order. The Ableton Live 12 manual documents the feature cleanly in the Session View chapter.

Here is the recipe, from Spec A section 5.7.

[pause 300ms]

Step one. Build eight to sixteen one-bar MIDI variants of your drum pattern in a single Session track. Each clip is a small hand-edit of the original — a hat drop on beat 2 of bar 1. A ghost snare on the *and* of 4. An open hi-hat on beat 3. Nothing dramatic. Small deltas.

Step two. For every clip, set the Follow Action to *Any*. Chance — twenty percent Play Again. Sixty percent Other. Twenty percent Any. Trigger length one bar.

Step three. Hit play. Live deals variants.

Step four — this is where the committing happens. In Arrangement View, arm the track and use Capture MIDI with Cmd-Shift-C. You now have a *committed*, non-repeating drum take for that section. The pool itself was the instrument. The capture is the bounce.

[pause 400ms]

Stacking the unlinked-envelope trick on top of this is the next layer, from Spec A section 5.7 again. Four-bar audio clip. Seven-bar clip envelope on the filter cutoff. Autechre have been doing the polymeter-through-envelope move since *Confield* — Booth and Brown described the idea in the *Sound on Sound* April 2004 feature, in a section about how their sequencers stopped obeying the bar line. Live 12 makes this one checkbox.

[pause 300ms]

The commit path. When the Session pool sounds right, use Bounce in Place. Bounce Groups shipped in 12.3 as part of the 12.x feature set — group your generative chain, hit Bounce Group, Live prints a fixed audio stem. The generative chain is frozen. Your arrangement now references one file instead of a clip pool plus a plugin chain plus a MIDI effect chain.

Frozen audio is psychologically expensive to un-freeze. That expense is the feature.

[pause 300ms] Bounce. Move on.
