# How the stems got made — Demucs, briefly

<term key="demucs">Demucs</term> is a U-Net-shaped neural separator. In the hybrid version, one branch processes the waveform directly, one branch processes a time-frequency representation, and the outputs fuse into four masks — drums, bass, vocals, other.

You do not need to train it. stemforge wraps the pretrained weights and runs a single command: `stemforge default --no-slice benjamins.wav`. <Citation bib="stemforge_repo" />

The separator is not clean. Sibilance leaks into `other`. Kick sub-harmonics smear into `bass`. Noticing the artifacts is itself a listening exercise — where the separator fails tells you what was tangled in the mix.
