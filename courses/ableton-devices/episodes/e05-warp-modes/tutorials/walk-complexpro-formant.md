# Warp Recipe: walk-complexpro-formant

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section). **Mirrors `complexpro-formant-monster` — same recipe, walkthrough framing; keep in sync.**

**Concept:** Walkthrough step 6 — Complex Pro: goblin (+12, Formants 0) then giant (−7, Formants 0).
**What you should hear:** the same "ah" in Complex Pro: up 12 with Formants 0 (goblin — envelope dragged up), then down 7 with Formants 0 (giant — envelope hauled down). Two monsters from one dial; nudge Envelope off-default for hollow coloration.
**Structure:** ab. **Isolates:** **Transpose direction** with Formants pinned to **0** (goblin vs giant).
**Source audio:** `src_vox-ah.wav` — the walkthrough source.

## Steps — Segment A (goblin)

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_vox-ah.wav` onto an audio track | — | The dry "ah" |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Complex Pro** | Formants + Envelope appear |
| 3 | Clip view | **Envelope** | **128** (default; optionally nudge for hollow color — calibrate) | Default coloration |
| 4 | Clip view | **Formants** | **0** (constant in BOTH segments) | Envelope tracks the pitch — destroyed |
| 5 | Clip view | **Transpose** | **+12** st | A thin high **goblin** |

## Steps — Segment B (giant), then concat A · silence · B

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 6 | Duplicate the clip | **Transpose** | **−7** st (Formants still 0, Envelope still 128) | A low hollow **giant** |

Render A, insert ~0.4 s silence, render B, concatenate.

**The abuse extreme here:** **Formants 0 in both directions** — same voice, formants destroyed both ways. Optional: nudge **Envelope** off 128 on the giant for extra hollow color.

## Verify
- **Audible:** A a thin high goblin; B a low hollow giant — same voice, formants destroyed both ways. Either still human ⇒ Formants not at 0 ⇒ reject.
- **Spectral:** envelope/formant peaks shifted UP in A (+12) and DOWN in B (−7), tracking the transpose. Envelope peaks fixed ⇒ reject.

## Make it reusable (resample / freeze)
Resample each segment, or bounce the concat to `walk-complexpro-formant.wav`.
