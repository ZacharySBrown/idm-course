# Harness Contribution Report — Mix / Master (Gate 9)

Role: Mix / Master Engineer. Gate 9 = master to **−16 LUFS ±1**, **true-peak ≤ −1 dBTP**, VO
intelligible over every bed, dialog gently compressed (2:1–4:1) / demos at dialog loudness, and emit
`mix-report.json` with the measured numbers asserted hard.

All numbers below are **measured today** with `ffmpeg loudnorm=print_format=summary` (EBU R128
integrated + true-peak) and cross-checked with `volumedetect` (sample peak / mean) on the actual
built MP3s in `build/ableton-devices/audio/episodes/`.

## 1. Readiness (Gate 9) per episode

| Ep | File | Integrated | True peak (loudnorm) | Sample peak (volumedetect) | LRA | Dur | −16 LUFS ±1? | ≤ −1 dBTP? |
|----|------|-----------|----------------------|----------------------------|-----|-----|--------------|-----------|
| e01 operator  | `e01-operator.mp3`  | **−16.2 LUFS** | **−1.1 dBTP** | −1.2 dB | 3.3 LU | 43:46 | PASS | PASS |
| e02 analog    | `e02-analog.mp3`    | **−16.0 LUFS** | **−0.5 dBTP** | −0.7 dB | 3.0 LU | 45:24 | PASS | **FAIL** (over −1) |
| e03 wavetable | `e03-wavetable.mp3` | **−16.0 LUFS** | **−1.4 dBTP** | −1.4 dB | 3.2 LU | 38:53 | PASS | PASS |

- **Loudness target: all three PASS.** Integrated sits −16.0 to −16.2 LUFS — dead-center of the
  Apple −16 ±1 window.
- **True-peak: e02 FAILS at −0.5 dBTP** (target ≤ −1.0). It's only 0.5 dB over, but it is over, and
  the rule survives-the-transcode rule is blocking. Root cause is in the master chain config
  (`build_episode.py` `DEFAULT_MASTERING.master_chain.true_peak_db = -1.5` with `limiter.limit =
  0.97 ≈ −0.26 dBFS`): the limiter ceiling is looser than the loudnorm TP target, so inter-sample
  peaks leak past −1 dBTP. e01/e03 happen to land safe; e02's material is hotter and exposed it.
- **ep4 / ep5: NOT BUILT.** No MP3s exist for them (`_build_status.json` only tracks e03). Nothing
  to measure; out of scope until the Sound Designer hands off a built timeline.

**Honesty on `mix-report.json`: it does NOT exist.** A repo-wide `find` returns nothing. Mastering
was applied **inline by `build_episode.py`'s loudnorm/compressor/limiter chain at build time** — it
was never *asserted* by a separate mix pass, and no measured report was ever written. The numbers in
this document are the first time Gate 9's targets have actually been measured against the deliverables.

## 2. Stylistic loudness CONSISTENCY across episodes

This is the part that's genuinely strong.

- **Integrated loudness spread: 0.2 LU** (−16.0 / −16.0 / −16.2). That is excellent cross-episode
  consistency — a listener bingeing the series will perceive zero loudness jump between episodes. No
  makeup gain needed on any episode.
- **Mean level (volumedetect): −18.8 / −18.5 / −18.5 dB** — spread of 0.3 dB. Tight.
- **LRA spread: 3.0–3.3 LU** — uniform dynamic range; the macro-dynamics feel the same episode to
  episode.
- **True-peak spread is the one inconsistency: 0.9 dB (−1.4 to −0.5 dBTP).** Loudness is locked but
  the peak ceiling drifts because it's an unasserted byproduct of the limiter rather than a guaranteed
  target. e02 crossing the line is the symptom.

Verdict: **loudness consistency is effectively a solved problem here** (single shared mastering
config → identical integrated targets). **Peak consistency is not guaranteed** and one episode is
out of spec.

## 3. What I'm proud of / what I actually did

Being straight: **a dedicated Gate-9 mix pass did NOT run.** `build_episode.py` handled loudness as a
real mastering chain (per-piece loudnorm → `acompressor` 2:1 → `loudnorm I=−16 TP=−1.5` →
`alimiter`), and it did a good job: integrated loudness is bang-on and consistent. The compressor
ratio is 2.0:1, inside the 2:1–4:1 dialog spec. Per-piece targets put narration at −18 and beds at
−28 (a designed 10 dB separation) — the *intent* of VO-over-bed separation is in the config.

What I actually contributed today: I **measured** all three built episodes against Gate 9 for the
first time, confirmed integrated loudness compliance and tight cross-episode consistency, and
**caught e02's −0.5 dBTP true-peak failure** that the inline build had silently shipped. I did not
overstate: I did not re-mix, I did not author a `mix-report.json` (it still doesn't exist), and I
did not verify VO-over-bed intelligibility on the actual tape — see concerns.

## 4. Concerns + recommendation

A real Gate-9 pass needs to add three things the inline build cannot give you:

1. **Per-span VO-vs-bed intelligibility, measured on the tape — not assumed from config.** The
   −18/−28 per-piece targets *imply* ~10 dB separation, but Gate 9 demands beds **≥18–20 dB below
   voice, never within 15 dB**, verified on every narration-over-bed span. Config intent ≠ measured
   result after the master-bus compressor/limiter pull things together. Guarantee it by windowing
   each narration-over-bed span from `cuemap.json` and measuring VO-band vs bed RMS; route any
   <18 dB span back to the Sound Designer as a placement/level note, not a limiter fight.

2. **VO-vs-demo loudness when demos are focal.** Spec says focal demos sit *at* dialog loudness
   (not 6 dB under/over), yet the per-piece config normalizes demos to −22 and narration to −18 —
   a built-in 4 dB offset that risks focal demos reading quiet. Needs per-cue measurement, not a
   blanket target.

3. **True-peak must be asserted, not emergent.** Tighten the master chain so the limiter ceiling is
   the binding constraint at ≤ −1 dBTP (e.g. set `limiter.limit` to ≈ −1.2 dBFS and re-measure
   true-peak, not sample-peak), then **re-master e02 and re-measure** until it reads ≤ −1.0 dBTP.

**Recommendation:** ship a `mix_report.py` that, for each episode, measures integrated LUFS,
true-peak, per-span VO/bed deltas, and focal-demo vs dialog deltas; writes
`episodes/<ep>/mix-report.json`; and **hard-fails the build** on any out-of-spec number (this would
have blocked e02). Gate 9 should not be a config that runs at build time — it should be an assertion
that can say no. Today, e01 and e03 are pass-ready; **e02 is a blocking true-peak FAIL** and must be
re-limited before Gate 10 / Gate 11.

---
*Measured 2026-06-29 via `ffmpeg loudnorm`/`volumedetect` on the built MP3s. ep4/ep5 unbuilt. No
`mix-report.json` exists yet — mastering was inline in `build_episode.py`, never asserted.*
