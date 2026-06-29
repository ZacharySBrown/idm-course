# Ableton Expert / Patch Director — Harness Contribution Report

Role: demo-correctness owner. Gates I own: **Gate 3** (demo design), **Gate 4** (demo↔script
reconciliation), **Gate 7** (demonstration-verification after render). Mandate: every demo
provably demonstrates ONE concept, the script's parameter claims match the patch, and each patch
ships as a reusable preset + click-by-click tutorial that round-trip.

**Honesty caveat up front:** I worked headless via AbletonOSC. Demo design (Gate 3) and reconciliation
against the dumped param maps (Gate 4) are done across ep1–ep5. **Gate 7 was NOT closed end-to-end:**
no `demo-verification.json` was emitted, no `.adv` was actually saved and committed (0 `.adv` files in
the repo — the presets exist only as build-and-save procedures in each `presets/SAVE_CHECKLIST.md`),
and the librosa/ffmpeg `verify_demo.py` assertions were run on only a handful of demos. So "readiness"
below means **design-complete and param-reconciled, predicted-renderable** — not "rendered and
machine-verified." Where I actually measured a render, I say so.

---

## 1. Readiness (Gate 3 / Gate 7) per episode

Device-demo counts are the real `device_demos:` rows in each `clip_manifest.yaml`.

| Ep | Device | Demos | Provably demonstrative (design + reconcile) | Needs hand-build / cannot render headless | Readiness |
|---|---|---|---|---|---|
| e01 | Operator | 18 | ~16 design-clean, param-reconciled | **feedback demo inert** + rhythmic-pair needs onset check | **AMBER** |
| e02 | Analog | 23 | **23/23** names+ranges verified vs `analog.json` (172 params); reference-correct | 0 hard blockers; ~3 "watch on first render" | **GREEN (design)** |
| e03 | Wavetable | 20 | 18/20 renderable | **2 cannot render** (Hi-Q toggle); ~6 need device pre-set | **AMBER** |
| e04 | Meld | 19 | **~8/19** fully renderable | 5 need matrix hand-build, 4 MPE play-it-yourself, 2 unconfirmed filter idx | **RED for headless** |
| e05 | Warp modes | 18 | recipe+source-clip complete | **no `.adv` possible** (warp = clip property, not a device) | **AMBER (different contract)** |

Per-episode honest split:

- **e01 (AMBER).** 18 Operator demos. The index→brightness, ratio (1:1/1:2/1:3/√2/φ), and the 8-step
  Polynomial-Bell walkthrough are clean. **Two known problems I did NOT paper over:**
  `op-feedback-bifurcation` is **inert** — I rendered both candidate recipes (lone-carrier and
  modulator self-feedback) and **measured** flat sine: centroid ≈133 Hz, **0.0% energy >2 kHz at every
  rung including Feedb=100**. Feedback does not take audible effect over the OSC write here. Shipped ep1
  was left unchanged; the fix is hands-on in Live (see `FEEDBACK_FIX.md`). The rhythmic pair
  (`op-rhythmic-single` / `op-rhythmic-instance2`) is the exact ep1 bug that motivated the onset-rate
  assertion — designed-correct now, but **not re-verified** with distinct onset rates.
- **e02 (GREEN at design).** 23/23 demos audited against `analog.json`: **0 missing param names, 0 value
  violations** after edits. Reference-correct rebuilds (Reese = two detuned saws not saw+sub; Digeridoo =
  noise-excited self-oscillating filter). This is the strongest episode. Caveat: still **pre-render** —
  the MS-20 series-filter demos and `an-reese-detune-sweep` loudness are flagged "watch on first render."
- **e03 (AMBER).** 20/20 param-reconciled vs `wavetable.json` (93 params); fixed a genuinely silent bug
  (`Osc 1 Gain: 0.0 dB` is 0.0 on a 0–1 scale = silence). **2 cannot demonstrate headless** —
  `wt-zipper-vs-smooth` and `wt-hiq-on-vs-off` both hinge on the **Hi-Q toggle, not LOM-exposed**; they
  render one valid reference segment so the build doesn't break but they do **not** prove their A/B.
  ~6 more need an orchestrator pre-set (Effect Mode / table / Position-Spread). Two are reduced-fidelity:
  `wt-position-spread-chord` proves width not spread; `wt-mpe-pressure-position` proves a brightness
  ladder not MPE per-voice independence.
- **e04 (RED for headless).** 19 demos reconciled vs `meld.json` (129 params), but Meld's
  **modulation matrix and MPE are not in the LOM map.** Honest split: **~8 fully renderable**, **5 need
  matrix hand-build** to satisfy the cyclic/recurrence assertion (the NO-MATRIX-FALLBACK single ramp is
  audible motion but is **not** an LFO/loop and **fails Gate 7 as-is**), **4 are MPE play-it-yourself**
  (static render proves layering, not per-voice behavior), and the **Plate Resonator filter index (15) is
  an unconfirmed placeholder** carried into 7 demos. This episode is the most over-claimable; I have
  flagged every fallback inline.
- **e05 (AMBER, different contract).** 18 warp recipes. There is **no `.adv`** — warp settings are clip
  properties, so the reusable artifact is a **resampled bounce**, and the reproducibility contract is
  recipe-card + named source clip → WAV. Several demos depend on copyrighted source songs (cite-don't-
  commit), so they can't be auto-rendered in CI without the user supplying audio.

---

## 2. What I'm proud of

**Root-causing the ep2 "silent demos" as a renderer/param bug, not a design bug.** The failure
listeners would have heard as dead air traced to wrong LOM names and out-of-scale values silently
no-op'ing the write (a wrong param name renders silently; `Osc 1 Gain 0.0 dB` reads as 0.0 = silence on
a 0–1 scale). I dumped the real param maps (`operator/analog/wavetable/meld.json`), then audited **every**
`params`/`automation`/`ab_*` key verbatim against them — e02 came out 0 missing names / 0 value
violations. That audit is the difference between "renders" and "renders the right thing."

**The reference-correct rebuilds in e02.** Reese bass redesigned to its canonical form — **two detuned
saws** (Saunderson, 1988), dropping the un-canonical sub osc that was also the measured root cause of the
−47 dB render (energy at ~33 Hz, inaudible on phones, eating normalization headroom). Digeridoo rebuilt
as a **noise-excited high-Q key-tracked filter** (filter-as-oscillator) so the pitched ring is *provably
the filter*, not an ambiguous filtered sine. These fix demonstrativeness, not just levels.

**The honest LOM-limit findings (e03/e04), refusing to fake them.** Where the matrix/MPE/Hi-Q isn't
LOM-addressable I said so per demo rather than shipping a single ramp dressed as an LFO. The
NO-MATRIX-FALLBACK convention is explicitly labelled "audible stand-in, FAILS Gate 7 as-is, hand-build
to pass." That keeps the harness honest about what proves its concept.

---

## 3. What I actually did (evidenced)

- **Dumped 4 param maps** over LOM: `param_maps/{operator,analog,wavetable,meld}.json`
  (172 / 93 / 129 params for analog/wavetable/meld respectively) — the authoritative name+range source.
- **Designed & reconciled all device demos** ep1–ep5: 18 + 23 + 20 + 19 + 18 = **98 device-demo rows**,
  each with concept / isolates-one-variable / structure / verification, and reconciled against the maps.
- **Wrote per-episode verification dossiers:** `e02/DEMO_VERIFICATION.md`, `e03/DEMO_VERIFICATION.md`,
  `e04/DEMO_VERIFICATION.md` (full per-demo tables: names-OK?, isolates-one-var?, reference, confidence,
  LOM limitation), and `e01/FEEDBACK_FIX.md` (the measured feedback-inert diagnostic).
- **Generated tutorials:** 17 (e01) / 23 (e02) / 20 (e03) / 19 (e04) / 20 (e05) click-by-click rebuild
  cards; and a `presets/SAVE_CHECKLIST.md` per episode (incl. e05's "warp is not a preset" contract).
- **Measured real renders** for the feedback diagnostic (centroid / >2 kHz band energy across 5 rungs,
  two configurations) and the e02 Reese loudness (−47 dB mean), and applied level/concept fixes from
  those measurements.

---

## 4. Concerns — demos I would NOT claim are demonstrative

Gate-7-blocking, by episode:

- **e01 — `op-feedback-bifurcation`: NOT demonstrative.** Measured flat sine at every feedback rung; the
  concept (sine→saw→broadband) does not render headless. Needs ear-verification in Live before it ships
  as anything but the original weak demo. **e01 — rhythmic pair:** designed-correct but **not re-verified**
  for distinct onset rates — this is the original ep1 failure, so it must pass the onset-rate assertion
  before I'll vouch for it.
- **e02 — pre-render, not machine-verified.** I'd back the *design* with high confidence, but the MS-20
  **F1→F2 series-filter** demos (`an-ms20-series-filter`, `an-ms20-scream`) depend on the series route
  actually engaging in the pipeline, and `an-digeridoo-drone` is my one substantive redesign — both need
  a first-render listen. Don't claim "verified" until `verify_demo.py` has run.
- **e03 — `wt-zipper-vs-smooth` and `wt-hiq-on-vs-off`: CANNOT demonstrate headless** (Hi-Q not exposed).
  They render a single reference segment only — that is **not** the A/B the concept needs. Hand-render or
  fold into narration. Reduced-fidelity: `wt-position-spread-chord` (width ≠ spread) and
  `wt-mpe-pressure-position` (ladder ≠ MPE independence) — proving a *neighboring* fact, not the claim.
- **e04 — the most over-claimable episode.** I would NOT claim demonstrative without hand-build:
  the 5 matrix demos (`meld-modenv-loop-macro`, `meld-lfo-to-macro`, `meld-twohands-step3/4`,
  `meld-self-sequence-onenote`) — their single-ramp fallback **fails the cyclic/recurrence assertion**;
  and the 4 MPE demos (`meld-mpe-per-note`, `meld-twohands-step5/final`) prove layering, not per-voice
  expression. Also the **Plate Resonator filter index (15) is an unconfirmed placeholder** in 7 demos —
  if the live ordering differs, those render the wrong filter.
- **e05 — reproducibility gap by nature.** No `.adv` round-trip is possible; the contract is recipe +
  source clip → bounce. Demos that need copyrighted songs cannot be auto-verified in CI without the user
  supplying audio, and song timestamps need re-cutting by ear per pressing.

**Cross-cutting gap:** Gate 7's machine pass is **not yet closed** — `verify_demo.py` / round-trip diffs
were not run across the board, no `demo-verification.json` was emitted, and **no `.adv` is committed**.
Until presets are saved-and-committed and the assertions run on the actual renders, treat all "GREEN"
marks as *design-readiness*, not *demonstration-verified*.

---

## Relevant file paths

- Persona: `/Users/zak/zacharysbrown/idm-course/.claude/agents/ableton-expert.md`
- Gates: `/Users/zak/zacharysbrown/idm-course/docs/podcast-harness/02-QUALITY-GATES.md`
- Param maps: `/Users/zak/zacharysbrown/idm-course/courses/ableton-devices/tools/device_render/param_maps/{operator,analog,wavetable,meld}.json`
- e01: `/Users/zak/zacharysbrown/idm-course/courses/ableton-devices/episodes/e01-operator/FEEDBACK_FIX.md`, `.../e01-operator/{clip_manifest.yaml,tutorials/,presets/SAVE_CHECKLIST.md}`
- e02: `/Users/zak/zacharysbrown/idm-course/courses/ableton-devices/episodes/e02-analog/DEMO_VERIFICATION.md`
- e03: `/Users/zak/zacharysbrown/idm-course/courses/ableton-devices/episodes/e03-wavetable/DEMO_VERIFICATION.md`
- e04: `/Users/zak/zacharysbrown/idm-course/courses/ableton-devices/episodes/e04-meld/DEMO_VERIFICATION.md`
- e05: `/Users/zak/zacharysbrown/idm-course/courses/ableton-devices/episodes/e05-warp-modes/presets/SAVE_CHECKLIST.md`
