# The Metallurgist — sidechain bus graph

Jenkinson on "The Metallurgist": *"The bass drum is the sidechain source, and each time it drops, the dynamics for other instruments are being changed to permit a sense of fluidity."* <Citation bib="tape_op_89" />

The key word is *dynamics for other instruments* — plural, comprehensive. The sidechain graph is not a single duck on a bass track. It is a fan-out.

```
[KICK trigger bus — pre-fader, no audio out]
            │
            ├─► Compressor on SUB track       — 6 dB, 5 ms atk, 80 ms rel
            ├─► Compressor on PAD track       — 3 dB, 20 ms atk, 200 ms rel
            ├─► Compressor on LEAD track      — 1 dB, 50 ms atk, 30 ms rel
            ├─► Compressor on VOX track       — 2 dB, 10 ms atk, 120 ms rel
            ├─► Compressor on NOISE track     — 4 dB, 2 ms atk, 40 ms rel
            └─► Glue Compressor on MASTER     — 1 dB grab (whole mix breathes)
```

Every non-kick track in the mix receives a gain-reduction envelope triggered by the kick. The mix is **composed** by the envelope, not just mixed.

Receipt caveat: the specific threshold/release values above are Ableton-translated reconstructions, not Jenkinson's own numbers. The principle — every bus gets the sidechain — is the quote. See `needs_bib` for the source-of-quote flag.
