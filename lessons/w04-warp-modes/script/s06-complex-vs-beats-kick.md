Now the pitfall. [pause 200ms] This is the single biggest mistake people make with Complex Pro, and it is the reason beginners' drums sound soft.

Put the Hallogallo drums stem on a track. Set the warp mode to Complex Pro. Defaults — Formants one hundred, Envelope one-twenty-eight. Play it against the unwarped source, same tempo, A/B.

Listen to the kick. [pause 300ms] Something is off. The leading edge is rounded. The *click* is gone. What was a punchy four-on-the-floor now reads more like a wet floor tom. The snare also — there's a softness on the stick that was not there in the source.

This is not a bug in Complex Pro. It is how phase vocoders work. The algorithm reconstructs audio by averaging spectral frames across its Envelope window. A transient is, by definition, a fast change in the signal — so it gets spread across adjacent frames and loses its bite. Per the research compendium, quote — "Complex Pro softens kick transients." End quote. It is a documented cost.

Two fixes. Both useful. [pause 200ms]

**Fix number one — nudge the warp markers.** For every kick hit, drag the warp marker on the timeline a few milliseconds *before* the transient. Three, five, seven milliseconds — tune by ear. What this does is give the phase vocoder a head-start, so by the time the grid position arrives the attack has already materialized. The kick lands on the beat instead of just behind it.

**Fix number two — layer Beats mode underneath.** Duplicate the track. Set the duplicate to Beats mode, Preserve Transients, Transient Envelope one hundred. High-pass it around eighty hertz — you only need the click. Sum the duplicate at minus-six decibels under the Complex Pro track. The original carries the body; the Beats layer restores the punch. [pause 150ms] This is the classic fix. It works every time. It costs you one extra track.

Pick per source. Do not default to Complex Pro on drum material.

Cite — Ableton manual; compass research notes.
