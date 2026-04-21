# Complex Pro — Formants and Envelope

Two controls do the heavy lifting.

**Formants (0–100).** Formants are the resonant bumps in a signal's spectrum — for a voice, the vowel frequencies. Set to 100%, Complex Pro preserves them across pitch shifts. Pitch a vocal up an octave with Formants 100 and it still says "ah," not "eeeeh." Set to 0 and you get the aliased-chipmunk character — cheap and sometimes exactly right.

**Envelope (16 / 32 / 64 / 128 / 256).** Window size, in samples. Smaller windows = better time resolution, worse frequency resolution; larger = the inverse. Defaults:

- **Envelope 64** — hi-hats, cymbals, anything with fast transients
- **Envelope 128** — most full mixes and mid-range content
- **Envelope 256** — bass, kick sustain, sub-heavy material

If the clip is smeary on the top end, drop to 64. If the bass is chattering, raise to 256.

Cite: `bib:ableton_live_12_manual`.
