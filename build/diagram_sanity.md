# Diagram sanity review — Wave 10.3

Reviewed 52 diagrams (mermaid + svg_content) across w01–w12 lesson.yaml files.
Cross-checked against the two compass_artifact specs and cited references.

**Totals:** 8 issues — 1 high, 5 medium, 2 low. Most diagrams pass.

---

## w07-squarepusher-chops (2 issues — 1 high, 1 medium)

### [HIGH] gd-s950-06 — Akai S950 sample rate is wrong
Diagram states "12-bit linear quantize at 48 kHz". The S950 samples at a
user-selectable 7.5–40 kHz — **not 48 kHz**. The lesson's own narrative
(aliased repitch as signature) depends on this ceiling.

**Fix:** "12-bit linear quantize at 7.5–40 kHz (user-selectable)". Also
soften "µ-law companding" to "µ-law-style (Akai/E-mu 12→8-bit
proprietary)".

### [MEDIUM] gd-s950-02 — pitch shift aliasing asymmetry
Callout says "aliases above ±2 semitones". Aliasing only happens on
upward shifts (foldover above Nyquist); downward shifts produce
decimation artefacts, not aliasing. Practical threshold is closer to
+4 semitones.

**Fix:** "Aliases on upward shifts (typically audible by +4st).
Downward shifts thicken via decimation."

---

## w05-aphex-tuning (1 issue — medium)

### [MEDIUM] gd-mnlg-04 — Monologue DAC bit-depth math
Diagram claims "12-bit DAC ~0.24¢ step". A 12-bit DAC over 1 octave =
0.29¢/step; over 5 octaves = 1.47¢/step. Neither matches 0.24¢. Korg's
own spec describes 16-bit pitch resolution; microtuning edit page
exposes 1¢ offsets.

**Fix:** Either drop the bit-depth node or update to "16-bit pitch
resolution, 1¢ user-facing microtuning offsets". Cite Korg Monologue
owner's manual instead of Roads 1996 for this specific claim.

---

## w09-vocal-chopping (2 issues — both medium)

### [MEDIUM] gd-sp1200-06 — SP-1200 companding is not µ-law
Curve labelled "µ-law-style" but drawn as a µ-law shape. SP-1200 uses
E-mu's proprietary 12→8-bit floating-point-scale encoding. The slide
body acknowledges the caveat; diagram label should too.

**Fix:** Relabel as "E-mu proprietary 12→8-bit (µ-law-like shape)".
Add note: "Not the ITU G.711 µ-law function."

### [MEDIUM] gd-sp1200-07 — 'no anti-alias filter' is overstated
SP-1200's input path does have a gentle analog roll-off (per service
manual); it's not brick-wall but also not absent. Students replicating
with a plain 26 kHz downsampler will over-emphasise HF aliasing.

**Fix:** Add third spectral line showing "gentle ~1-pole roll-off
from ~10 kHz". Caption: "Famously permissive — not truly 'no filter'."

---

## w04-warp-modes (1 issue — medium)

### [MEDIUM] wm03 — Complex Pro phase vocoder block diagram
Labels "Hann window, hop = N/4" as if spec. These are textbook defaults
(Roads 1996) but Ableton does not publish Complex Pro internals.
Diagram also omits the two artefact sources students actually hear:
vertical phase coherence and transient smearing.

**Fix:** Reframe window/hop as "Hann typical, hop ~N/4 — Complex Pro
internals not published". Add annotation after IFFT: "Phase-only
propagation → phasiness on polyphonic transients. Complex Pro adds
formant preservation + phase-locking heuristics not shown."

---

## w08-autechre-feedback (1 issue — low)

### [LOW] gd-maxmsp-03 — sample rate assumption
"64 samples = 1.45ms" is correct at 44.1 kHz but not declared. At
48 kHz = 1.33 ms. Scheduler "1ms resolution" is typical but
user-configurable.

**Fix:** "64 samples @ 44.1 kHz ≈ 1.45 ms (1.33 ms @ 48 kHz)".
Scheduler: "1–2 ms (user-configurable)".

---

## w11-beat-switch (1 issue — low)

### [LOW] d01 — "power-of-two" label vs bar 33
Diagram labels switch candidates at bars 8, 16, 33 and footer asserts
"power-of-two bar boundaries only". Bar 33 is the downbeat after a
32-bar (2⁵) period, not itself a power of two.

**Fix:** Either relabel as "bar 32 → new section at bar 33" or adjust
footer to "power-of-two period boundaries (8 = 2³, 16 = 2⁴, 32 = 2⁵)".

---

## Lessons that passed clean

- w01-listen-subtract (4 diagrams — Demucs hybrid description correct; Berklee loop flow OK; stem-occupancy Hz ranges reasonable as approximations; room-acoustics sketch correctly labelled as simplification)
- w02-subtraction (2 diagrams — density curve and Subtraction/Bounce/Skeleton decision graph both conceptual, no numeric claims to audit)
- w03-simpler-basics (~11 diagrams — Simpler mode dispatch, slicing decision tree, drum-rack signal path, MPC2000XL 44.1 kHz 16-bit claim correct per Akai spec, velocity curve illustration reasonable)
- w06-fourtet-layering (6 diagrams — kick-stack frequency bands labelled as "Zak estimate" in the caption itself; Skater doubling octave math correct; Omnisphere signal chain matches Spectrasonics docs; AudioMulch paradigm diagram conceptual)
- w10-variation-generation (3 diagrams — Follow Actions state machine, resample-mutate pipeline, variation tree — all conceptual, no numeric claims)
- w12-ship-two-tracks (4 diagrams — LUFS scale (-14 Spotify, -1 dBTP ceiling) matches ITU-R BS.1770 and streaming platform docs; mastering chain flow correct; playback-chain translation matrix is subjective/experiential, no factual claims to audit)
- Most of w07, w08, w09 (the ones not listed above — AWM voice block, Metallurgist sidechain fan-out, Dilla 96-PPQN swing math at 90 BPM was double-checked and arithmetic is correct: 1 tick = 6.94 ms, -3 ticks ≈ -20 ms)

---

## Summary for Zak

The diagrams are generally solid. The one genuinely problematic number
is the **S950 48 kHz sample rate** in w07 — that's factually wrong and
undermines the aliasing narrative the same lesson builds. Worth fixing
before ship.

The other medium items (SP-1200 µ-law label, Monologue 12-bit DAC
math, Complex Pro FFT internals, SP-1200 anti-alias filter wording) are
cases where the diagram is approximately right but missing a caveat
that the slide body already carries. A label tightening pass would
close them.

The two low items (Max scheduler rate, power-of-two bar labelling) are
presentational nitpicks.
