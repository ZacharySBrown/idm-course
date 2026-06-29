# Warp Recipe: transient-survival-ab

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** transient-locked granular (Beats) vs phase-vocoder smear (Complex) → the kick **survives** vs the kick **blurs**.
**What you should hear:** the same break loop at half tempo, played twice — first in **Beats** (kick stays punchy), a beat of silence, then in **Complex** (kick smears into a watery, blurred thwip).
**Structure:** ab. **Isolates:** **Warp Mode** (Beats vs Complex); same source, same half-tempo stretch in both segments.
**Source audio:** `src_drumbreak.wav` — a clean kick+snare+hat break.

## Steps — Segment A (Beats)

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_drumbreak.wav` onto an audio track | — | The break at native tempo |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Beats** | Transient-locked granular |
| 3 | Clip view | **Preserve** | **Transients** | Grain boundaries snap to the real hits |
| 4 | Clip view | **Transient Loop Mode** | **Loop Off** | Each slice plays to its end, no looping |
| 5 | Clip view | **Transient Envelope** | **100** | Hard slice edges — punchy |
| 6 | Transport | Stretch to **half tempo** — project tempo **50%** | 50% | Slow break with kick/snare still **sharp** |

## Steps — Segment B (Complex), then concat A · silence · B

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 7 | Duplicate the clip | **Warp Mode** | **Complex** | Phase-vocoder engine (no per-mode controls) |
| 8 | Transport | Same stretch | **50%** (identical to A) | Slow break with kick/snare **smeared, watery** |

Render A, insert ~0.4 s silence, render B, concatenate.

**The abuse extreme here:** Complex on a **drum** loop is the wrong-mode-on-purpose — Complex is for songs/pads, so a break run through it shows the phase-vocoder transient-smear at its most obvious. Beats is the honest counterpart.

## Verify
- **Audible:** A's kick/snare stay sharp; B's hits soften/smear and go "watery." A ≈ B ⇒ the mode switch did nothing ⇒ reject.
- **Spectral:** A preserves sharp broadband onset transients (high onset-strength peaks); B shows time-smeared onsets (lower, wider peaks) and raised inter-onset energy. Equal transient sharpness ⇒ reject.

## Make it reusable (resample / freeze)
Resample each segment separately (Beats render and Complex render) to two clips, or bounce the full A·silence·B concat to `transient-survival-ab.wav`.
