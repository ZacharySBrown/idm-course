# Warp Recipe: walk-source-dry

> **No `.adv` preset** — warp lives in the clip. This is the unwarped reference, not a sound-design move.

**Concept:** Walkthrough step 1 — the dry source, the reference for every destruction.
**What you should hear:** two seconds of a dry sung "ah" — no plugins, no reverb, no chain. The raw material to hold in your ear for the next six steps.
**Structure:** single. **Isolates:** nothing — the unwarped reference (Warp engine effectively transparent).
**Source audio:** `src_vox-ah.wav` — a dry sung "ah".

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_vox-ah.wav` onto an audio track | — | The dry "ah" at native pitch/length |
| 1 | Clip view | **Warp** | ON | Clip follows project tempo |
| 2 | Clip view | **Warp Mode** | **Beats** (any mode is fine; nothing is stretched) | No change yet |
| 3 | Transport | Project tempo = clip's analyzed tempo | **100%** (no stretch) | The clean, unprocessed "ah" — effectively dry |

**Why warp at 100%:** rendering through the engine at original tempo means **nothing is processed** — this is the A in every subsequent A-against-the-source comparison. If you hear any warp artifact, the render stretched it.

## Verify
- **Audible:** a clean, unprocessed sung "ah", ~2 s, no artifacts. Any audible warp artifact ⇒ the render stretched it ⇒ reject.
- **Spectral:** spectrum identical to the source file (no smear, no scaling). Any deviation ⇒ reject.

## Make it reusable (resample / freeze)
None needed — this **is** the source. Keep `src_vox-ah.wav` as the canonical reference; the six destruction cards all start from it.
