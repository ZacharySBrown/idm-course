# Warp Recipe: walk-repitch-tape

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Walkthrough step 5 — Re-Pitch down then up → tape drop and chipmunk, the honest mode.
**What you should hear:** the same "ah" in Re-Pitch: first half speed (dark, pitched down, lo-fi grain, no aliasing), then double speed (bright, chipmunked, with fizz on top where partials cross Nyquist). No smear either way.
**Structure:** ab. **Isolates:** Re-Pitch **tempo ratio** (down 50% vs up 200%); Transpose disabled — ratio is the pitch.
**Source audio:** `src_vox-ah.wav` — the walkthrough source.

## Steps — Segment A (tape down)

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_vox-ah.wav` onto an audio track | — | The dry "ah" |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Re-Pitch** | Varispeed; **Transpose/Detune greyed out** (confirm) |
| 3 | Transport | **Half speed** — project tempo **50%** | 50% | Pitched down ~1 octave, longer, dark + lo-fi grain, **no fizz, no smear** |

## Steps — Segment B (chipmunk up), then concat A · silence · B

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 4 | Duplicate the clip | **Double speed** — project tempo **200%** | 200% | Pitched up ~1 octave, shorter, bright + **HF fizz** (aliasing), no smear |

Render A, insert ~0.4 s silence, render B, concatenate.

**The abuse extreme here:** both directions of varispeed in one A/B. **No smear or buzz in either** is the correctness check — Re-Pitch resamples, so the only artifacts are lo-fi grain (down) and aliasing fizz (up). Don't claim a measured resampler spec on-mic.

## Verify
- **Audible:** A pitched down an octave and longer (dark, grainy, no fizz); B pitched up an octave and shorter (chipmunk, with HF fizz). No smear/buzz in either ⇒ correct (Re-Pitch). Smear present ⇒ wrong mode ⇒ reject.
- **Spectral:** A scaled down ~2× (no aliasing); B scaled up ~2× WITH folded-back inharmonic components on top. No scaling / added smear bands ⇒ reject.

## Make it reusable (resample / freeze)
Resample each direction to its own clip, or bounce the A·silence·B concat to `walk-repitch-tape.wav`.
