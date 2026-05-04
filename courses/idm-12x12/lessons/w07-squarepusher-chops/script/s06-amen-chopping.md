# s06 — Amen chopping

The Amen break. [pause 400ms]

Six seconds of drumming by Gregory Coleman on "Amen, Brother" by The Winstons, the B-side of their 1969 single "Color Him Father." Four bars. Seven kicks, seven snares, one crash break. The most sampled drum loop in recorded music.

Jenkinson's introduction to it, per Sound on Sound: *"I first heard it being used in the Mantronix track 'King Of The Beats'… the way that the drummer does the ghosting, the timing of the ghosting, the sound of his kit, the way it is recorded, the vinyl — everything works. You can pitch it up, down, stretch it, reverse it, it does everything. The Amen break is very sonically rich, very spectrally dense."* [pause 500ms]

On *Big Loada*'s "Come On My Selector," 1997, the Amen lives inside an Akai S950 sampler, and gets triggered from a Boss DR-660 drum machine. The S950's pitch-shift aliases — when you repitch a sample in the S950, it sounds crude and digital in a specific way that the more expensive Akai samplers do not. That aliasing is part of the drum-and-bass aesthetic. It is a feature of the cheap hardware, not a defect, and Jenkinson leans into it. [pause 400ms]

Ableton translation.

Step one. Drop `build/audio/stemforge-renders/w07/ff_drums.wav` onto an audio track. This is the `idm_crushed`-pipeline render of Funky Fanfare — not literally the Amen, but functionally equivalent source material. Four bars of funk drums. Spectrally dense. Rich in transients. [pause 200ms]

Step two. Right-click the clip. Choose **Slice to New MIDI Track**. In the dialog, Slice to: **one-sixteenth**, Slicing Preset: **Built-In**. Hit Create.

Ableton does three things at once. It detects where the sixteenth-note grid sits. It creates a Drum Rack with one chain per slice, each chain holding a Simpler pointed at a tiny fragment of the source audio. And it drops a MIDI clip into the new track with every slice triggered on its original beat.

You can now play that MIDI clip and get the original loop back. [pause 200ms] That is the boring outcome.

Step three. Re-pitch individual pads. Click a pad, open the Simpler tab, nudge Transpose by minus-seven or plus-seven semitones. That is the S950-alias flavor, approximately. Ableton's pitch-shift is cleaner than the S950's, so you will not get the exact crunch. For that we want to add bit-reduction. Insert a **Pedal** or **Redux** on the Drum Rack chain, crush to 8-bit or 12-bit. Now the pad aliases.

Step four. Arm a new MIDI clip. Finger-drum a new pattern. Or keyboard-play one.

~This is the whole move.~ Every technique later in the course — Prefuse vocal chopping, Dilla micro-grid shifts, Death Grips kick layering — is a variation on *slice, remap, resample*. Jenkinson was doing it in 1997 on twelve-bit hardware. [pause 300ms]

One more thing. Save that Drum Rack as a preset. Do not rebuild it every session.
