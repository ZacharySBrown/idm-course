Open Simpler. Drop any sample onto the waveform. Look at the top of the device view.

[pause 300ms]

Three tabs. *Classic.* *One-Shot.* *Slicing.* Same device, three jobs.

[pause 400ms]

**Classic** is melodic play. The sample is pitched by the incoming MIDI note. Middle C plays the sample at its recorded speed; octave up plays it at double speed, double pitch. Warp is available, and when Warp is on, pitch and time decouple — you can transpose up two octaves and the sample stays the same length. Classic mode is where chromatic chopping lives. One vocal chunk mapped across sixteen keys, played as a melodic instrument. This is the Dilla move. We come back to it in Week 9.

[pause 300ms]

**One-Shot** is the drum-hit mode. A single sample, fires start-to-end, no pitch tracking across the keyboard, no envelope release. Snare on C1 sounds the same as snare on G3. There is a Fade In slider, a Fade Out slider, a Trigger-versus-Gate switch, and a Snap button that moves start and end markers to zero crossings. This is where every pad in the Drum Rack we build today lives.

[pause 300ms]

**Slicing** mode is the chopper. You feed it a drum loop, tell it *where* to cut — transient detection, beat grid, equal regions, or manual placement — and Simpler generates a numbered list of slices, each one mapped to its own MIDI note. The playback mode decides how slices overlap. Mono chokes the previous slice; Poly lets them ring; Thru plays the current slice until a new one fires.

[pause 400ms]

The mistake you make exactly once — and only once, because the result is so wrong you never do it again — is loading a drum hit into Classic mode and triggering it from middle C. The sample plays at a wrong speed. The pitch is off by whatever the difference is between the root key and the incoming note. The hit ~sounds like it was recorded underwater.~

[pause 200ms]

This is not a bug. Classic mode is *designed* to pitch. It is doing its job. You asked the wrong mode.

The fix is to click One-Shot, reload the sample, and move on. Or — as we will do today — load the drum hit into a Drum Rack, which instantiates Simpler in One-Shot mode automatically, with pitch tracking disabled and Snap on.

[pause 300ms]

This is the single most important thing to internalize about Simpler: the mode tab decides the contract. Get it right first; tune second.
