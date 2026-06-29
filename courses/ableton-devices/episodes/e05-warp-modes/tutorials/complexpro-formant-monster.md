# Warp Recipe: complexpro-formant-monster

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Complex Pro Formants pulled out under a big transpose → goblin (up) and giant (down) from one dial.
**What you should hear:** the same vocal twice — up 12 semitones with Formants 0% (the envelope dragged up into a goblin), then down 7 with Formants 0% (the envelope hauled down into a giant).
**Structure:** ab. **Isolates:** **Transpose direction** with Formants pinned to **0%** (goblin vs giant) — the destroy-the-envelope lever.
**Source audio:** `src_vox-ah.wav` — a dry sung "ah".

## Steps — Segment A (goblin)

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_vox-ah.wav` onto an audio track | — | The dry "ah" at native pitch |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Complex Pro** | Formants + Envelope appear |
| 3 | Clip view | **Envelope** | **128** (default, HELD) | No extra coloration |
| 4 | Clip view | **Formants** | **0%** (constant in BOTH segments) | Envelope will track the pitch — destroyed |
| 5 | Clip view | **Transpose** | **+12** st | A high, thin **goblin** — envelope dragged up |

## Steps — Segment B (giant), then concat A · silence · B

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 6 | Duplicate the clip | **Transpose** | **−7** st (Formants still 0%, Envelope still 128) | A low, hollow **giant** — envelope hauled down |

Render A, insert ~0.4 s silence, render B, concatenate.

**The abuse extreme here:** **Formants pinned to 0%** in both directions is the destroy extreme — two monsters from one dial. Up = goblin, down = giant. Optionally nudge **Envelope** off 128 for hollow coloration (calibrate by ear).

## Verify
- **Audible:** A is a high, thin goblin; B is a low, hollow giant — same voice, two monsters, one dial. A ≈ B (or either still "human") ⇒ Formants weren't at 0% ⇒ reject.
- **Spectral:** A's formant/spectral-envelope peaks shifted UP with +12; B's shifted DOWN with −7 (envelope tracks the pitch, not preserved). Envelope peaks staying put ⇒ Formants not destroyed ⇒ reject.

## Make it reusable (resample / freeze)
Resample each segment to its own clip, or bounce the A·silence·B concat to `complexpro-formant-monster.wav`. *(Same recipe as the walkthrough card `walk-complexpro-formant` — keep both in sync.)*
