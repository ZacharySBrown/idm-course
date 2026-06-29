# Warp Recipe: walk-texture-cloud

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section). **Reused by `05d-texture-cloud` and `05h-save-instrument`.**

**Concept:** Walkthrough step 4 (and step 8 reuse) — Texture 800% + Flux 60 → the ambient granular cloud (the cold-open sound, built live).
**What you should hear:** the same "ah" in Texture warped to 800%, Grain Size mid, Flux ~60: two seconds of voice become a slowly-evolving pad with no clear pitch — the "U Smile" move and the Truax cloud, in a clip.
**Structure:** single. **Isolates:** Texture **Flux (~60)** at 800% stretch — the cloud breakage (the hero mangler).
**Source audio:** `src_vox-ah.wav` — the walkthrough source.

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_vox-ah.wav` onto an audio track | — | The dry "ah" |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Texture** | Signal-blind granular |
| 3 | Clip view | **Grain Size** | **0.5** (mid) | Mid grains |
| 4 | Clip view | **Flux** | **60** | Decorrelates grains → stationary cloud, no metallic loop |
| 5 | Transport | Stretch to **~800%** — project tempo **~12.5%** | ~800% | A smooth, slowly-evolving, de-pitched pad/cloud |

**The abuse extreme here:** **800% stretch with Flux 60** is the hero move — the in-the-box "U Smile"/Truax cloud. Flux 60 is enough to kill the metallic grain-loop without fully erasing motion. This is the sound the cold open opens on, built live from a 2-second vowel.

## Verify
- **Audible:** a smooth, slowly-evolving, de-pitched pad/cloud — no beat, no clear pitch, no metallic looping buzz. A repeating metallic loop ⇒ Flux too low ⇒ reject.
- **Spectral:** stationary smeared spectrum, low periodic-buzz energy (Flux decorrelation), evolving slowly. Strong grain-rate comb ⇒ reject.

## Make it reusable (resample / freeze)
1. Resample/freeze→flatten to `walk-texture-cloud.wav`.
2. **This is the "save as instrument" payoff (05h):** the bounced cloud is now an original instrument — drag it into Simpler, or keep as a drone bed. It is also pass-1 of the Hopkins loop (`walk-resample-pass3`).
