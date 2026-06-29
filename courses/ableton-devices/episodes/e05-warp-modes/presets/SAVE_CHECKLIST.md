# e05-warp-modes — SAVE CHECKLIST (warp settings are NOT presets)

**There is no `.adv` preset for a warp setting.** A Warp Mode and its controls (Preserve, Loop
Mode, Transient Envelope, Grain Size, Flux, Formants, Envelope, transpose, tempo ratio) are
**clip properties**, not a saved device. You cannot drag a "Texture-Flux-90" preset onto a track
the way you drag an Operator `.adv`.

So the reusable artifact for every recipe is the **resampled bounce**: warp the clip, then
**resample / Freeze → Flatten** the result to a plain audio file. That WAV carries the designed
sound with no warp settings attached — drop it anywhere. This file lists, per recipe, the **source
clip** needed and the **resample-to-bounce** step, plus the **source audio to acquire/record**.

This `presets/` directory therefore holds **no `.adv` files** — only this checklist. Bounces land in
`build/ableton-devices/audio/clips/e05-warp-modes/<id>.wav`.

---

## SOURCE AUDIO TO ACQUIRE / RECORD (from the manifest required-sources header)

Drop these in `songs/ableton-ep05/` (git-ignored; copyrighted songs are cited, **not committed**).
Acquire songs as 44.1k/16-or-24-bit stereo WAV; record/source the `src_*` the same.

### Foreground artist references (Section 6 + cold open) — copyrighted, cite don't commit
| File | Track | Used by |
|---|---|---|
| `01_systemisch.wav` | Oval — *Systemisch* (1994, Mille Plateaux) — CD-skip glitch | `systemisch-clip`, `trans-warp-seam-3` |
| `02_akufen-my-way.wav` | Akufen — *My Way* (2002, Force Inc.) — radio microsamples | `akufen-clip`, `trans-warp-seam-4` |
| `03_riverrun.wav` | Barry Truax — *Riverrun* (1986) — first real-time granular cloud | `truax-texture-cloud`, `trans-warp-seam-1` |
| `04_u-smile.wav` | Justin Bieber — *U Smile* (2010) — the cold-open Texture/Flux wash source | `cold-open-texture-wash`, `trans-warp-seam-2`, `bed-warp-cloud` |

### Warp-demo source material — royalty-free / self-recorded, NOT copyrighted
| File | What to record/source | Used by |
|---|---|---|
| `src_vox-ah.wav` | Dry sung "ah", ~2 s, no reverb/no chain — THE walkthrough source | `walk-source-dry`, `walk-beats-stutter`, `walk-tones-warble`, `walk-texture-cloud`, `walk-repitch-tape`, `walk-complexpro-formant`, `walk-resample-pass3`, `formant-decouple-ab`, `complexpro-formant-monster` |
| `src_drumbreak.wav` | Clean kick+snare+hat break, ~2 bars | `transient-survival-ab`, `beats-stutter-freeze`, `tones-warble`, `texture-cloud`, `repitch-halfspeed` |
| `src_cymbals.wav` | Bright cymbal/ride/hat loop (lots of HF energy) | `aliasing-on-speedup` |
| `src_synth-note.wav` | One sustained synth note (held pad/sine-ish), ~2 s, steady spectrum | `granular-seam-grainsize`, `flux-smooths-buzz` |
| `src_pad-chord.wav` | Sustained polyphonic chord / pad, ~2 s | *(texture/cloud beds where a de-pitched wash is wanted; no dedicated demo card — keep for variants)* |
| `src_melodic-loop.wav` | Short melodic loop whose transients DON'T fall on 1/16 | `oval-beats-glitch` |
| `src_radio-vox.wav` | Spoken-word / radio-style voice clip (words + breaths) | `akufen-microslice` |

> Filenames above are the `source:` values in `clip_manifest.yaml`; rename to match or edit
> `source:` per entry. Song timestamps are from dossier §3 — **re-cut by ear** if your rip differs.
> Verify entry points on the actual pressings before stating anything on-mic.

---

## PER-RECIPE: source clip + resample-to-bounce step

Generic bounce procedure (referenced as **[RESAMPLE]** below):
1. Set the loop brace over the demo length (the recipe's `duration_s`).
2. Either **right-click the clip → Freeze**, then **Flatten** — or route the warped track to a new
   audio track's input, arm it, and **Resample** the playback.
3. The new clip is plain audio at the designed sound — no warp settings. Export to
   `build/.../e05-warp-modes/<id>.wav`.

### Device demos (18)
| id | source clip | bounce step |
|---|---|---|
| `cold-open-texture-wash` | `04_u-smile.wav` (~4 s excerpt) | [RESAMPLE] 12 s of the wash |
| `granular-seam-grainsize` | `src_synth-note.wav` | [RESAMPLE] with Grain Size ramp baked; or freeze at one value |
| `transient-survival-ab` | `src_drumbreak.wav` | [RESAMPLE] A (Beats) and B (Complex) separately, or the A·silence·B concat |
| `flux-smooths-buzz` | `src_synth-note.wav` | [RESAMPLE] with Flux ramp baked; or freeze at Flux 100 |
| `formant-decouple-ab` | `src_vox-ah.wav` | [RESAMPLE] A (Formants 100) + B (Formants 0), or concat |
| `aliasing-on-speedup` | `src_cymbals.wav` | [RESAMPLE] the 2× render (fizz baked in) |
| `beats-stutter-freeze` | `src_drumbreak.wav` | [RESAMPLE] the half-tempo stutter |
| `tones-warble` | `src_drumbreak.wav` | [RESAMPLE]; keep next to `texture-cloud.wav` |
| `texture-cloud` | `src_drumbreak.wav` | [RESAMPLE]; keep next to `tones-warble.wav` |
| `repitch-halfspeed` | `src_drumbreak.wav` | [RESAMPLE] the half-speed render |
| `complexpro-formant-monster` | `src_vox-ah.wav` | [RESAMPLE] goblin + giant, or concat |
| `walk-source-dry` | `src_vox-ah.wav` | none — this IS the dry reference source |
| `walk-beats-stutter` | `src_vox-ah.wav` | [RESAMPLE] the 1/16 stutter |
| `walk-tones-warble` | `src_vox-ah.wav` | [RESAMPLE] the 300% warble |
| `walk-texture-cloud` | `src_vox-ah.wav` | [RESAMPLE]; this bounce is the "save as instrument" payoff + pass-1 of the Hopkins loop |
| `walk-repitch-tape` | `src_vox-ah.wav` | [RESAMPLE] down + up, or concat |
| `walk-complexpro-formant` | `src_vox-ah.wav` | [RESAMPLE] goblin + giant, or concat |
| `walk-resample-pass3` | `src_vox-ah.wav` → Texture → resample → Complex Pro → resample → Texture | **PRINT (resample) between every pass** — the method IS the bounce; keep pass-1/2/3 |

### Section-6 warp rebuilds (2)
| id | source clip | bounce step |
|---|---|---|
| `oval-beats-glitch` | `src_melodic-loop.wav` (off-grid transients) | [RESAMPLE] the 70%-tempo glitch |
| `akufen-microslice` | `src_radio-vox.wav` | move markers off onsets first, then [RESAMPLE] |

### Transition / bed warp clips (warp-flavored seams — bounce like the demos)
| id | source clip | warp + bounce |
|---|---|---|
| `trans-warp-seam-2` | `04_u-smile.wav` | Texture, Grain 0.35, Flux 90, ~800% → [RESAMPLE] |
| `bed-warp-cloud` | `04_u-smile.wav` | Texture, Grain 0.4, Flux 95, ~1000% → [RESAMPLE] (long bed) |

> `trans-warp-seam-1/3/4` and the song clips (`systemisch-clip`, `akufen-clip`,
> `truax-texture-cloud`) are plain extractions (no warp block) — cut via `extract_clips.py`, no
> resample step needed.

---

## Round-trip / reproducibility note
Since there is no `.adv` to diff, the reproducibility contract for ep5 is:
**the recipe card (tutorials/<id>.md) + the named source clip → the bounced WAV.** Anyone with the
source file and the step table reproduces the bounce. Keep the card and the manifest `warp:` block
in sync; if a value changes on first render (calibrate-by-ear), update **both** the card and the
manifest.
