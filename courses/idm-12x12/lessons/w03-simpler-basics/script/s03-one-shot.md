One-Shot mode. The parameter list. In the order you actually touch them.

[pause 400ms]

First — **Snap**. Leave it on. Always. Snap forces the start and end markers to the nearest zero crossing in the waveform. A zero crossing is the point where the sample value passes through zero. If your sample start is not on a zero crossing, the first output sample is a non-zero number preceded by silence — that step function produces a click. Snap eliminates it. One toggle. On. Forever.

[pause 300ms]

**Fade In.** Measured in milliseconds. Zero to two milliseconds for a raw drum hit that was captured cleanly. If the sample front-end is brittle — if it was sliced out of a wet mix and has a residual pre-transient — push Fade In to five or six milliseconds. You are smoothing the attack without softening the hit. Anything above fifteen milliseconds on a drum one-shot is a mistake.

[pause 300ms]

**Fade Out.** Five to fifteen milliseconds is the normal range. Its job is to prevent a click at the other end of the sample — specifically, when a long kick is cut off by the next MIDI note on the same pad, or by a choke group firing. A twenty-millisecond fade-out sounds like a fade-out. A seven-millisecond fade-out just stops cleanly.

[pause 400ms]

**Trigger versus Gate.** *Trigger* plays the full sample regardless of how long the MIDI note is. A thirty-second kick will finish playing even if the note was a thirty-second-note at 120 BPM. *Gate* stops on note-off. For drum hits, Trigger is almost always right, because a drum hit has a natural decay and you want it to finish. Gate is for sustained material — a synth one-shot you want to chop with note length.

[pause 300ms]

**Transpose** in semitones. **Detune** in cents. Transpose is the pitch-tune-to-root move we cover in depth in Week 5 on Aphex — every kick gets tuned to the root of the track. Detune at plus or minus five cents is the layering trick — duplicate a hit, detune one copy, pan them ten degrees apart, instant width.

[pause 400ms]

One more note — Warp is available in One-Shot mode. Leave it off unless you are deliberately time-locking a hit to project tempo. A one-shot warped to tempo is not a one-shot anymore; it is a time-stretched sample that happens to be short. If you want time-locking, use Slicing mode. If you want a drum hit, leave Warp off.

[pause 200ms]

That is the whole tab. Five controls you will change. Four you will not.
