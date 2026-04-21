# Algorithm continued — varispeed playback and the DAC

Sample playback on the MPC3000 is <term key="varispeed">varispeed</term> — pitch and duration are coupled. Raise a pad's pitch by +5 semitones and the sample plays 1.335× faster (ratio = 2^(5/12)). There is no time-stretching algorithm involved — this is literally "read the sample at a different rate."

Why this is load-bearing for <term key="chipmunk_soul">chipmunk soul</term> (taught in s06):
- **Pitch up = faster = chipmunk artifact preserved.**
- **Pitch down = slower = tape-slow dusty artifact preserved.**
- A phase-vocoder or Complex Pro would *fix* this coupling — and kill the character.

The 18-bit Burr-Brown PCM61P-K DAC and the summing bus give the MPC3000 a specific sound producers call "weight" or "punch." It is not quantifiable in a spec sheet. Roads 1996 (`bib:roads_computer_music_tutorial`, Ch. 2) covers why coupled-pitch-time sample playback and simple-DAC summing have characteristic artifacts — <term key="intermodulation">intermodulation distortion</term> in the bus, quantization noise floor, aperture error at the DAC — that together constitute "the sound of the box."

Constraint note: 32 MB RAM ceiling bounded sample lengths and forced the chop-and-rearrange workflow. Memory pressure is compositional pressure.
