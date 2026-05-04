# Combining Follow Actions with Clip Envelopes

Follow Actions gives you *which clip plays next*. Clip Envelopes give you *what the clip sounds like while it plays*. Stacked, you get generative arrangement from a small source.

**Clip Envelopes unlinked from clip loop** — set the envelope's loop length to a value different from the audio/MIDI loop. Live 12 manual §13. <Citation bib="ableton_live_12_manual" />

Example — 4-bar audio clip. Filter-cutoff envelope set to 7-bar loop. The filter sweep never lands in the same place across four plays of the clip. Now stack this under Follow Actions: on each bar-1 trigger, FA may advance to a *different* 4-bar clip, at which point the 7-bar envelope continues from wherever it was.

That is <term key="polymeter">polymeter</term> on two axes — clip rotation on axis one, envelope phase on axis two. Autechre spent albums on this. <Citation bib="sos_autechre_april_2004" /> Live does it with two checkboxes.

Sample Offset envelope on the printed loop is the same trick for drum playback — see ram-04.
