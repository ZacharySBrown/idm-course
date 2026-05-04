## Diagram — "same preset, three layers" doubling for Skater

Signal flow of the Hebden Skater-bass doubling move. Single MIDI part, three instrument tracks, no counter-melody logic. `Tape Notes #140`.

```
MIDI clip (bass line, F minor walk, root-fifth)
   │
   ├──► Track 1: Omnisphere "Plectra Sub"  ──► bass register (F1-F2)
   │          └─► ~0 dB, center
   │
   ├──► Track 2: same MIDI, transposed +24  ──► bell register (F3-F4)
   │          └─► ~−20 dB, center, no EQ, no bright-ifying
   │
   └──► Track 3: same MIDI, transposed +36  ──► upper register (F4-F5)
              └─► ~−24 dB, light shimmer reverb
```

All three tracks trigger off one MIDI clip via MIDI routing (or duplicate clips locked in sync). No counter-melody, no voicing changes. The doubling is *pure* — identical line, three octaves of the same notes.

The effect is a <term key="brightness_halo">brightness halo</term> on the fundamental, not a melodic stack. Mute track 2 + 3 and the bass "buries." Unmute and it reads as a single, fatter instrument.
