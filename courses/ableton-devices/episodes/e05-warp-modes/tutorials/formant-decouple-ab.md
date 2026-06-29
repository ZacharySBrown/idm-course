# Warp Recipe: formant-decouple-ab

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Complex Pro **Formants** → excitation vs spectral envelope: keep the body human, or drag it up into a chipmunk.
**What you should hear:** the same vocal transposed up 12 semitones, twice — first Formants 100% (a person singing higher, body intact), a beat of silence, then Formants 0% (the chipmunk — envelope dragged up with the pitch).
**Structure:** ab. **Isolates:** Complex Pro **Formants** (100% vs 0%); same vocal, same **+12** transpose in both segments.
**Source audio:** `src_vox-ah.wav` — a dry sung "ah".

## Steps — Segment A (Formants 100%)

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_vox-ah.wav` onto an audio track | — | The dry "ah" at native pitch |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Complex Pro** | Phase-vocoder / élastique; Formants + Envelope appear |
| 3 | Clip view | **Transpose** | **+12** st | The "ah" up an octave |
| 4 | Clip view | **Envelope** | **128** (default, HELD) | No extra coloration |
| 5 | Clip view | **Formants** | **100%** | Same voice, just higher — **body intact** |

## Steps — Segment B (Formants 0%), then concat A · silence · B

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 6 | Duplicate the clip | **Formants** | **0%** (Transpose still +12, Envelope still 128) | Chipmunk — envelope dragged up with the pitch |

Render A, insert ~0.4 s silence, render B, concatenate.

**The abuse extreme here:** **Formants 0%** under **+12** is the destroy extreme. At 100% Complex Pro is "transparent transpose"; at 0% it is the chipmunk — same dial, opposite ends.

## Verify
- **Audible:** both segments same pitch (up an octave); A sounds like the SAME voice higher, B sounds chipmunked/thin. A ≈ B ⇒ Formants didn't move ⇒ reject.
- **Spectral:** both share the transposed harmonic comb (same f0); B's spectral-envelope/formant peaks shifted UP relative to A while A's envelope sits near the original. Equal envelope position ⇒ reject.

## Make it reusable (resample / freeze)
Resample each segment to its own clip, or bounce the A·silence·B concat to `formant-decouple-ab.wav`.
