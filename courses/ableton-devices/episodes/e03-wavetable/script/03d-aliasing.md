There is one more DSP fight, and it is the one that decides whether your patch sounds like nineteen-eighty-two or twenty-fourteen.

[pause 500ms]

A single-cycle frame — especially a saw or a square — is stuffed with high harmonics. Play it at a high pitch and the harmonics above Nyquist, half the sample rate, fold back down into the audible band as inharmonic alias tones. Tones that aren't integer multiples of anything. Grit.

[pause 500ms]

Two ways to fight it. One — band-limited mip-mapping: pre-compute several copies of the table, each with fewer harmonics, and at playback pick the copy whose top harmonic still sits below Nyquist for the note you're holding. Two — oversampling: run the oscillator at a higher internal rate, then decimate. Oversampling doesn't remove aliasing; it reduces it. Ableton's Hi-Q mode is the oversampling switch, and it costs you CPU.

[pause 600ms]

Now the punchline. The PPG grit — the thing Palm tried to filter out — is uncorrected aliasing. Eight-bit playback, no interpolation, control updates only about twenty-six times a second. Serum and Wavetable spend their whole DSP budget removing exactly what made the PPG iconic. So listen to one fast sweep, twice: Hi-Q off first, then Hi-Q on.

[cue: wt-hiq-on-vs-off]

Hi-Q off was a PPG. Hi-Q on was a Serum. The entire forty-year argument, in one switch — and later we'll flip it off on purpose.
