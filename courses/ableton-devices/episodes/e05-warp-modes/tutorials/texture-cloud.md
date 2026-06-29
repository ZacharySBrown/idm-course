# Warp Recipe: texture-cloud

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Texture on the same source → signal-blind granular gives a de-pitched cloud (no pitch hunting).
**What you should hear:** the SAME source as `tones-warble`, now in Texture: no pitch hunting, just a de-pitched granular cloud — the hero mangler, a granular cloud generator hiding in a clip.
**Structure:** single. **Isolates:** **Warp Mode = Texture** (signal-blind) on the same source — contrast partner to `tones-warble`.
**Source audio:** `src_drumbreak.wav` — same source as `tones-warble`.

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_drumbreak.wav` onto an audio track | — | The break at native tempo |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Texture** | Signal-blind granular — no pitch tracking |
| 3 | Clip view | **Grain Size** | **0.4** (mid) | Mid grains |
| 4 | Clip view | **Flux** | **60** | Enough randomization to de-pitch into a cloud |
| 5 | Transport | Stretch to **~300%** — project tempo **~33%** (SAME as `tones-warble`) | ~300% | A smooth de-pitched cloud — **no warble**, no pitch-hunt |

**The abuse extreme here:** the point is the **fair A/B** against `tones-warble`: identical source, identical 300% stretch, only the mode (and Flux) changed. Texture's signal-blindness is the feature — it never hunts a pitch, so the same un-pitchable source becomes a clean cloud instead of a warble.

## Verify
- **Audible:** a smooth de-pitched cloud with NO warbling pitch-hunt (contrast vs `tones-warble`). Audible pitch-tracking warble ⇒ this rendered as Tones, not Texture ⇒ reject.
- **Spectral:** stationary, smeared spectrum with no tracked pseudo-pitch; lower periodic-pitch energy than the Tones render of the same source. Tracked pitch present ⇒ reject.

## Make it reusable (resample / freeze)
Resample/freeze→flatten to `texture-cloud.wav`. Keep next to `tones-warble.wav` for the slide A/B.
