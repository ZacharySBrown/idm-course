That is one family — the grain. There is a second one, running on completely different math, and it matters because three of the six Warp modes belong to it.

[pause 400ms]

The grain family works in time — cut the waveform into chunks, re-arrange the chunks. The other family works in frequency. It is the phase vocoder, introduced by James Flanagan and Robert Golden at Bell Labs in nineteen-sixty-six, in the *Bell System Technical Journal*. Their idea: represent speech not as a waveform but as its short-time spectrum — the amplitude and the phase in each frequency band, frame by frame. And that representation, they noted, "leads to a means for time compression and expansion of speech signals."

[pause 500ms]

The mechanism is worth saying slowly, because the artifact comes straight out of it. Slice the recording into overlapping frames. Run an FFT on each — a short-time Fourier transform. To stretch time, you do not touch the audio; you just space the frames further apart on output than they were on input. More frames, same content, longer sound. Michael Portnoff made this efficient with the FFT in nineteen-seventy-six; Mark Dolson's tutorial carried it into computer music.

[pause 500ms]

But there is a catch, and it is the whole story of how this family breaks. Re-space the frames and the phase no longer lines up. Each band's phase has to be re-derived so the partials stay continuous across the wider gaps. That is the hard part, and when it is even slightly wrong, you hear it. That re-derivation, and its failures, is the Complex and Complex Pro modes. Different math from the grain, different breakage — and we come back to exactly how it breaks in the next stop.
