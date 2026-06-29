# Warp Recipe: cold-open-texture-wash

> **There is no `.adv` preset for a warp setting.** A warp mode + its controls live in the clip, not in a saved device. The reusable artifact is the **resampled bounce** (last section).

**Concept:** Texture + high Flux at extreme stretch → a finished pop song broken into a de-pitched ambient cloud.
**What you should hear:** ~12 s of a smooth, slowly-evolving wash — no clear pitch, no beat. A Justin Bieber song stretched past recognition; the pop is buried but unfindable.
**Structure:** single. **Isolates:** Texture **Flux** (high) at extreme stretch — the marquee cloud control.
**Source audio:** `04_u-smile.wav` — a ~4 s vocal/hook excerpt.

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `04_u-smile.wav` onto an **audio track** | — | The clip plays at its native tempo/pitch |
| 1 | Clip view | **Warp** | ON | Clip now follows project tempo (no audible change yet at native tempo) |
| 2 | Clip view | **Warp Mode** | **Texture** | Signal-blind granular engaged; still near-native until you stretch |
| 3 | Clip view | **Grain Size** | **0.35** (small–mid) | Fine grains — feeds a smooth wash once stretched |
| 4 | Clip view | **Flux** | **90** (high) | Grains decorrelate; the metallic seam-buzz is suppressed |
| 5 | Transport / clip | Stretch to **~800%** — set project tempo to **~12.5%** of the clip's analyzed tempo (or set the clip's seg-BPM so 4 s plays over ~32 s) | ~800% | A smooth de-pitched ambient cloud; the pop is gone |

**The abuse extreme here:** Flux pinned to **90** at **~800%** stretch is the whole point — this is the PaulStretch "U Smile 800% Slower" cousin built *inside a clip*, not in PaulStretch. Flux is what turns the repeating grain-loop into a stationary cloud.

## Verify (Gate-7 pass condition)
- **Audible:** no beat, no recognizable melody; a smooth wash evolving over ~12 s. Recognizable pop ⇒ stretch/Flux didn't take ⇒ reject.
- **Spectral:** stationary, smeared spectrum; no periodic onset peaks; low/continuous spectral flux. A strong periodic buzz at the grain rate ⇒ Flux too low ⇒ reject.

## Make it reusable (resample / freeze)
A warp setting can't be saved as a preset, so **commit it**:
1. Set the loop brace over the 12 s you want.
2. Route the warped track to a new audio track's input (or **right-click clip → Freeze**, then **Flatten**), arm, and **resample** the playback to a new clip.
3. The bounce is now a plain audio file at the wash you designed — drag it anywhere, no warp settings required. Export to `build/.../e05-warp-modes/cold-open-texture-wash.wav`.
