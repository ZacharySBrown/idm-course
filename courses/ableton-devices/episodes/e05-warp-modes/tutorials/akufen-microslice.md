# Warp Recipe: akufen-microslice

> **No `.adv` preset** — warp lives in the clip, and here the composition is the **marker placement**, not a knob. Reusable artifact = the resampled bounce (last section).
> Section-6 rebuild (06b): Akufen's hand-cut radio grains, automated via transient placement.

**Concept:** Beats with Warp Markers dragged onto un-transient material + short Loop Forward segments → rhythmic vocal-fragment percussion. The microsample is a grain you cut by hand; transient PLACEMENT is the composition.
**What you should hear:** a spoken-radio voice turned into micro-sliced rhythmic percussion — words and breaths short-looped into a microhouse groove.
**Structure:** rebuild (single). **Isolates:** **Warp Marker placement** (markers moved OFF the real onsets).
**Source audio:** `src_radio-vox.wav` — a spoken-word / radio-style voice (words + breaths).

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_radio-vox.wav` onto an audio track | — | The spoken voice at native tempo |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Beats** | Transient-locked granular |
| 3 | Clip view | **Preserve** | **Transients** (start honest) | Markers sit on the real onsets |
| 4 | Sample editor | **Drag Warp Markers** onto **un-transient material** (mid-word, mid-breath) | placement is the move | Slices now start on arbitrary slivers, not onsets |
| 5 | Clip view | **Transient Loop Mode** | **Loop Forward** | Short segments loop into rhythmic percussion |
| 6 | Clip view | **Transient Envelope** | **100** | Hard, clicky grain edges |
| 7 | Transport | Project tempo | **100%** (placement, not stretch, is the lever) | Hand-cut radio grains sequenced into a groove |

**The abuse extreme here:** the teaching point is **marker placement** — the render MUST move markers **off** the real onsets onto mid-word/breath material and short-loop them. If markers stay on the transients you just get the source slowed; the composition is the off-onset placement.

## Verify
- **Audible:** rhythmic vocal-fragment percussion built from sub-second slivers — the Akufen microhouse character. If it reads as the source merely chopped on its own onsets ⇒ markers weren't moved ⇒ reject.
- **Spectral:** onset grid mismatched to the source's natural onsets (markers on non-transient material), short repeated loop segments.

## Make it reusable (resample / freeze)
Resample/freeze→flatten to `akufen-microslice.wav`. This is the 06b rebuild that follows the real `akufen-clip`.
