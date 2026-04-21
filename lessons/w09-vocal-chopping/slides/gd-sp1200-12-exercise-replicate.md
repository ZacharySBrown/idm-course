# Exercise A — process a modern sample into SP-1200 territory

Goal: take a modern 44.1 kHz vocal sample and reduce it through the three-device chain until the aliasing and companding artifacts are audible. Then A/B.

Steps:

1. Load the `hp_vocals.wav` bounce from the stemforge recipe onto an audio track (`bib:stemforge_repo`).
2. Freeze and flatten the track. The bounce is the source-of-truth.
3. Add the chain, in series: **Redux** (SR 13 kHz, Bit depth 12, anti-alias off) → **TAL-Bitcrusher** (12-bit, slight drive) → **EQ Eight** (LPF 13 kHz, 12 dB/oct). See bib references s01's slide-08.
4. Set up a second track, identical but with the chain bypassed. Solo both in turn.
5. Bounce both as `hp_sp1200.wav` and `hp_clean.wav`.
6. Drop both into a DAW session. A/B at matched loudness.

Deliverable: two bounces, plus one paragraph noting what the chain *removed* (top-end air, sibilance detail) and what it *added* (aliased mid-range artifacts, companded quantization noise at transient attacks). The point is not "it sounds old" — the point is specifically which artifacts are doing the work (`bib:roads_computer_music_tutorial`).
