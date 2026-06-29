Pitch-shift a voice the naive way and it turns into a chipmunk. There is a reason, and the reason is one control on Complex Pro.

[pause 400ms]

A voiced sound has two separable parts. The excitation — the glottal pulse train, the buzz of the vocal folds, which sets the pitch and the comb of harmonics. And the vocal tract on top of it — the resonances of throat and mouth, the formants, the spectral envelope that sets the vowel. The pitch is the comb; the vowel is the shape the comb sits under. They are independent: sing the same vowel at any pitch and the formant shape barely moves.

[pause 500ms]

Naive pitch-shift moves both at once. Slide the harmonics up an octave and the formant peaks slide up with them — the resonances that say "adult human" climb into "chipmunk." Formant-preserving transpose fixes this in three steps: estimate the spectral envelope, divide it out to leave just the fine structure, shift the fine structure to the new pitch, then re-apply the original envelope. Pitch moves; body stays. That estimation is usually cepstral or LPC — standard DSP — and it is exactly Complex Pro's Formants control. The manual: at a hundred percent, "the original formants will be preserved, even if the pitch is changed significantly."

[pause 500ms]

Hear the decouple. Same vocal, Complex Pro, transposed up twelve semitones. First with Formants at a hundred percent — the envelope held in place. Then Formants at zero — the envelope dragged up with the pitch.

[cue: formant-decouple-ab]

The first one is a person singing higher. The second one is the chipmunk. Same transpose, same engine — the only thing that moved was whether you kept the spectral envelope. One honest note, because it trips people up: Live's Formants is a preserve-versus-destroy dial, zero to a hundred percent. It is not a free formant shifter — you cannot move formants by a named number of semitones. That preserve-only framing is repeated across secondary coverage; the manual itself only documents the percentage.
