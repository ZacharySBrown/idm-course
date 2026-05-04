# Underlying algorithm — 12-bit companded ADC

The SP-1200 uses a **12-bit companded PCM** format. "Companded" means the amplitude range is non-linear — small values are finely resolved, large values are coarsely resolved. It's closer to <term key="mu_law">µ-law companding</term> than to plain 12-bit linear PCM.

Why companding matters sonically:
- **Loud transients** (snares, kick clicks) hit the coarse end of the curve → visible quantization noise at the attack. This is the "crunch" at the front of every SP-1200 snare.
- **Quiet content** (reverb tails, vocal sustain) sits on the fine end → cleaner than a pure 12-bit linear would give.
- The resulting quantization noise floor is **signal-dependent**, not constant. Linear 12-bit PCM at the same bit depth sounds noticeably different — flatter, less characterful.

Bit-depth math: 12 bits = 4096 levels, theoretical SNR ≈ 72 dB. But with companding, effective dynamic range is pushed into the usable range where content lives, at the cost of top-end detail. Roads 1996 covers companding curves in Ch. 1 (`bib:roads_computer_music_tutorial`).

Manufacturer documentation for the exact E-mu companding curve is thin — the SP-1200 service manual is the primary source, flagged in `needs_bib:`.
