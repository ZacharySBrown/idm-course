# Warp Recipe: tones-warble

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Tones on pitch-less material → the pitch tracker chases a fundamental that isn't there → warbling / underwater artifacts.
**What you should hear:** a source with no clear pitch (a drum loop) stretched in Tones: a fluttery, metallic, "underwater" warble as the mode hunts a pitch that does not exist.
**Structure:** single. **Isolates:** **Warp Mode = Tones** on a deliberately pitch-less source (wrong-mode-on-purpose).
**Source audio:** `src_drumbreak.wav` — pitch-less to Tones; a loop it can't track. *(Contrast partner: `texture-cloud`, same source.)*

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_drumbreak.wav` onto an audio track | — | The break at native tempo |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Tones** | Pitch-aware granular — it will try to track a fundamental |
| 3 | Clip view | **Grain Size** | **0.7** (large) | Larger grains exaggerate grain repetition / warble |
| 4 | Transport | Stretch to **~300%** — project tempo **~33%** | ~300% | A fluttery, metallic, underwater warble — the tracker chasing a pitch that isn't there |

**The abuse extreme here:** feeding **Tones** a **pitch-less drum loop** is the wrong-mode-on-purpose. Tones is for vocals/monophonic instruments; on un-pitchable material it manufactures a wandering pseudo-pitch. Large Grain Size makes the flutter audible. The artifact is gentle/pitched, not clicky — that's the diagnostic vs Beats.

## Verify
- **Audible:** a pitched-but-wobbly, fluttery metallic warble (tracker chasing a nonexistent pitch) — gentle, not clicky. Clean stretch with no warble ⇒ Tones found a stable pitch ⇒ use a more pitch-less source / larger grain ⇒ reject.
- **Spectral:** wandering, unstable pseudo-pitch with grain-repetition flutter (periodic amplitude/centroid modulation) rather than a stable harmonic comb. Stable comb ⇒ reject.

## Make it reusable (resample / freeze)
Resample/freeze→flatten to `tones-warble.wav`. Pairs A/B with `texture-cloud.wav` (same source, Texture) — keep them side by side.
