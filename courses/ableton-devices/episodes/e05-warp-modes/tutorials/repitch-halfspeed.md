# Warp Recipe: repitch-halfspeed

> **No `.adv` preset** — warp lives in the clip. Reusable artifact = the resampled bounce (last section).

**Concept:** Re-Pitch at half speed → dark, pitched-down, lo-fi grain — varispeed and nothing else (no smear).
**What you should hear:** a loop in Re-Pitch dropped to half speed: darker, pitched down an octave, with audible lo-fi grain — the samples spaced out like a sampler dropped two octaves. No granular buzz, no phase smear.
**Structure:** single. **Isolates:** Re-Pitch **tempo ratio (50% / half speed)**; Transpose disabled — the ratio is the pitch.
**Source audio:** `src_drumbreak.wav` — a clean break loop.

## Steps

| # | Where | Setting | Value | You should now hear |
|---|---|---|---|---|
| 0 | Track | Drop `src_drumbreak.wav` onto an audio track | — | The break at native tempo |
| 1 | Clip view | **Warp** | ON | Follows project tempo |
| 2 | Clip view | **Warp Mode** | **Re-Pitch** | Varispeed; **Transpose/Detune greyed out** (confirm) |
| 3 | Transport | Stretch to **half speed** — project tempo **50%** | 50% | Pitched down ~1 octave AND twice as long (turntable law); dark + lo-fi grain, **no buzz, no smear** |

**The abuse extreme here:** the honest mode. Half speed is the "tape drop" — pitch and tempo move **together** because Re-Pitch resamples rather than time-stretching. The only artifact is HF roll-off + interpolation grain. If you hear a granular seam-buzz or watery smear, the wrong mode rendered.

## Verify
- **Audible:** pitched down ~1 octave and duration doubled **together** (turntable law); darker with lo-fi grain, NO granular seam-buzz and NO watery phase smear. Smear/buzz present ⇒ wrong mode rendered ⇒ reject.
- **Spectral:** whole spectrum scaled DOWN by ~2× (pitch and tempo locked); no added inharmonic/smear components — only HF roll-off and interpolation grain. Added smear bands ⇒ reject.

## Make it reusable (resample / freeze)
Resample/freeze→flatten to `repitch-halfspeed.wav`. Pairs with `aliasing-on-speedup` (the up direction) as the two halves of the varispeed story.
