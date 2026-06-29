# Warp Recipe: walk-tones-warble

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Walkthrough step 3 — Tones stretched 300% with large grains → brittle jungle-vocal warble.
**What you should hear:** the same "ah" in Tones, stretched to 300% with a large Grain Size: a metallic flutter — the brittle Akai-era timestretch wobble early-90s jungle producers kept.
**Structure:** single. **Isolates:** Tones **large Grain Size** at 300% stretch (the monophonic-stretch breakage).
**Source audio:** `src_vox-ah.wav` — the walkthrough source.

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_vox-ah.wav` onto an audio track | — | The dry "ah" |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Tones** | Pitch-aware granular — here it CAN track (the vowel is pitched) |
| 3 | Clip view | **Grain Size** | **0.8** (large) | Large grains → audible grain repetition / flutter |
| 4 | Transport | Stretch to **~300%** — project tempo **~33%** | ~300% | A pitched but metallic, fluttery warble — the jungle-vocal artifact |

**The abuse extreme here:** unlike `tones-warble` (wrong-source), this is Tones doing its *intended* job (a pitched vowel) but pushed — **large Grain Size at 300%** makes the grain repetition audible as the brittle Akai-era wobble. Same artifact family, right source, exaggerated.

## Verify
- **Audible:** a pitched but metallic, fluttery warble (grain repetition) on the stretched vowel — the jungle-vocal artifact. Clean stretch ⇒ grains too small / stretch too mild ⇒ reject.
- **Spectral:** periodic grain-repetition modulation (amplitude/centroid flutter at the grain rate) over the held pitch. Smooth, unmodulated stretch ⇒ reject.

## Make it reusable (resample / freeze)
Resample/freeze→flatten to `walk-tones-warble.wav`.
