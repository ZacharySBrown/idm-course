Beats mode is a slicer wearing a warp costume. [pause 200ms] That is the mental model. Once you hold it, every control on the panel makes sense.

Under the hood — the algorithm detects transients, cuts the audio at every detected hit or at every grid division, plays each slice at its original unmodified speed, and handles the empty space between slices by either truncating or looping.

Three controls that matter.

**Preserve.** Dropdown. Options are one-half, one-quarter, one-eighth, one-sixteenth, one-thirty-second, or Transients. [pause 150ms] This sets the slice grid. Preserve one-sixteenth means the audio gets cut into sixteenth-note slices regardless of where the actual hits are. Preserve Transients means the algorithm detects real onsets and slices *there*. For drums, Transients is almost always correct.

**Transient Loop Mode.** Three values — Loop, Loop Off, Loop Forward. Loop Off is cleanest. If a slice's audio ends before the next grid mark, you get silence. Loop fills that silence by re-playing the slice's tail — which, on a held note or a snare with a long tail, creates a machine-gun effect. Use Loop Off as the default; switch to Loop only when you *want* the stutter.

**Transient Envelope.** Zero to one hundred. [pause 150ms] Each slice gets a short amplitude envelope on its tail. Value one hundred means *no* envelope — clicks audible at every slice edge. Value zero means fast fade — zipper artifacts on sustained material. For breakbeats and drum loops, set it to one hundred and crop the source to zero-crossings if you get clicks.

[pause 200ms] Hard rule. Beats mode is for transient material only. Drums, percussion, short one-shots, rhythm guitars if they are chunky. Do *not* put a pad, a vocal, or a held chord through Beats. You will get a glitch mess. Which might be what you want — ~but rarely is.~

Cite — Live 12 manual.
