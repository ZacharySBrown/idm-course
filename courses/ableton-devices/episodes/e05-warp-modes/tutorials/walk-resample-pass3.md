# Warp Recipe: walk-resample-pass3

> **No `.adv` preset** — and here the *method* is the point: each pass MUST be resampled to a new clip before the next warp. This is the Jon Hopkins destructive loop.

**Concept:** Walkthrough step 7 — the Hopkins resample loop: warp → resample → warp → resample; the source gone by pass 3.
**What you should hear:** the third pass of a commit-and-mangle chain: the Texture cloud resampled, re-warped in Complex Pro, resampled again — the "ah" has been granulated, phase-smeared, granulated again. You can't find the voice anymore.
**Structure:** single. **Isolates:** iterated warp+resample (the method, not one control) — pass 3 of the destructive loop.
**Source audio:** `src_vox-ah.wav` → (pass1) Texture cloud → resample → (pass2) Complex Pro stretch → resample → (pass3 render).

## Steps — the pipeline (resample/PRINT between every pass)

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_vox-ah.wav` | — | The dry "ah" |
| **Pass 1** | Clip view | **Warp Mode = Texture**, Grain Size **0.5**, Flux **60**, stretch **~800%** (tempo 12.5%) | — | A de-pitched granular cloud (= `walk-texture-cloud`) |
| | **PRINT** | **Resample** the cloud to a new audio clip | — | Pass-1 committed as plain audio; discard the source warp |
| **Pass 2** | Clip view (on the pass-1 clip) | **Warp Mode = Complex Pro**, Transpose **+5**, Formants **30**, stretch **~400%** (tempo 25%) | — | The cloud phase-smeared and pitch-shifted — watery, ghosted |
| | **PRINT** | **Resample** to a new audio clip | — | Pass-2 committed |
| **Pass 3** | Clip view (on the pass-2 clip) | **Warp Mode = Texture**, Grain Size **0.35**, Flux **80**, stretch **~400%** (tempo 25%) | — | An evolving, source-less texture — **render this** |

**The abuse extreme here:** the destruction is *iterative*. Each pass must be **PRINTED (resampled to a new clip)** before the next warp — that's what commits the change and discards the source (the Hopkins method). Skip a print and the warp just replaces the previous warp instead of stacking on its output.

## Verify
- **Audible:** an evolving, source-less texture — no recognizable "ah", no clear pitch, layered granular + spectral character. If the original vowel is still identifiable ⇒ the passes didn't commit/print ⇒ reject.
- **Spectral:** spectrum unrecognizable vs `src_vox-ah.wav`: smeared + granulated, low correlation with the source's harmonic structure. High correlation with the source ⇒ reject.

## Make it reusable (resample / freeze)
The whole recipe **is** a resample chain. The pass-3 render `walk-resample-pass3.wav` is the reusable instrument; keep the pass-1 and pass-2 bounces too, since the method (not one setting) is the deliverable.
