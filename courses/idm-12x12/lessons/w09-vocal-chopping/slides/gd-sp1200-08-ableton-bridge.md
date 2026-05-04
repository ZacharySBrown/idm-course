# Ableton bridge — Redux + TAL-Bitcrusher + 13 kHz LPF

The closest in-the-box approximation of SP-1200 character is a **three-device serial chain on Simpler in One-Shot mode**:

1. **Redux** (native Live sample-rate/bit-depth reducer) — set **Sample Rate ≈ 13 kHz** (or 13.02 kHz if the device permits fine setting) to simulate the Nyquist bandwidth limit. Bit depth **12**. Redux's default anti-alias setting is *cleaner* than the SP-1200 — for authenticity, turn anti-aliasing *off* or reduce it (`bib:ableton_live_12_manual`).
2. **TAL-Bitcrusher** (`bib:tal_bitcrusher`) — set bit depth 12, add a slight non-linear drive curve to approximate companding asymmetry. Alternate: Decimort 2 (`bib:decimort_2`) has a specific "SP-1200" preset that matches the companding curve closely.
3. **EQ Eight, 12 dB/oct LPF at 13 kHz** — enforces the bandwidth limit as a hard cliff. Some producers prefer 16 kHz LPF as more forgiving.
4. **Simpler in One-Shot mode, Warp Re-Pitch** on the input sample — preserves varispeed coupling.

Parameter table:

| SP-1200 | Ableton chain |
| --- | --- |
| 26.04 kHz sample rate (no AA filter) | Redux SR 13 kHz, anti-alias off |
| 12-bit companded PCM | TAL-Bitcrusher 12-bit + drive OR Decimort 2 "SP-1200" preset |
| 2.5 s per pad RAM | Discipline — do not exceed (see Exercise B) |
| No per-voice filter | Chain's LPF is global, not per-voice — constraint preserved |
| Varispeed playback | Simpler Classic / Warp Re-Pitch |

This is the closest you get without a $4,000 hardware unit. It is not identical. It is close enough that a blind A/B requires careful listening on mids.
