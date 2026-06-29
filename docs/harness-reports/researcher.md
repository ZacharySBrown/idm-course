# Researcher — Harness Contribution Report

**Role:** Gate 1 owner. I build the cited fact dossier + `source-map` that every downstream
agent (Story Editor, Writer, Fact-Checker) stands on. Nothing reaches the script that isn't first
in my dossier, and a claim that isn't in my map cannot be cleared at Gate 6.

**Scope of this report:** my real outputs only — the five `specs/ableton_course_ep*_research.md`
dossiers and the one `..._source_map.json` I produced. Reported honestly; where coverage is thin I
say so.

---

## 1. Readiness (Gate 1) per episode

| Ep | Device | Status | One-line |
|----|--------|--------|----------|
| 1 | Operator / FM | **Ready** | Deepest dossier (~6,500 words, 6 sections); XY frame, full Chowning→DX7→IDM timeline, verbatim Henke/Chowning/RDJ quotes, Bessel/feedback math; domain anchors correct (11 algorithms, Coarse=integer/Fine=fraction, feedback only on un-modulated ops, loop modes None/Loop/Beat/Sync/Trigger, modulator Level ≈ index). |
| 2 | Analog / subtractive | **Ready** | Leads with the right framing fact (AAS physical-modeled VA, **shipped Live 7 / 2007 — not Live 4/5**), every nontrivial claim carries a full URL inline, conflicts flagged (`[FLAG]`/`[VA vs HW]`), Reese-is-Casio-CZ and "I Feel Love" engineer=Wedel corrections landed. |
| 3 | Wavetable | **Ready** | Confidence flags throughout ([CONFIRMED]/[LIKELY]/[UNCERTAIN]); PPG→Waldorf→Serum lineage sourced; soundcard-"wavetable" myth-buster; Cytomic filter circuit map; distinctive-feature table vs Serum/Massive. |
| 4 | Meld | **Ready (caveated by design)** | Strongest evidence discipline of the set: a dedicated `source_map.json`, two up-front framing **corrections** (see §2), oscillator table pulled **verbatim from the primary DSP reference**, and an explicit honesty preamble that there is **no confirmed Meld artist track**. Caveats are the point here, not a weakness. Two values left deliberately unverified (voice cap 12 vs 32; exact macro ranges) and flagged "verify in live device before mic." |
| 5 | Warp Modes | **Ready** | Explicit XY framing block written for Gate 1; manual quoted verbatim on the granular-vs-spectral split and "never neutral"; per-mode control tables with verbatim manual descriptions and a "lever type" column; élastique attribution honestly marked PLAUSIBLE (Ableton doesn't name the vendor in-manual). |

All five pass the Gate 1 rubric: each has a writeable X/Y, primary sources on technical claims, and
correct domain facts. **Only ep4 has a standalone machine-readable `source-map.json`**; ep1–3 and
ep5 carry citations inline in the dossier but were not split into the JSON contract (see §4).

## 2. What I'm proud of

The **Meld dossier's two framing corrections, made before a single feature claim.** The brief
called Meld a "Physical Modelling Hybrid" introduced in "Live 12.1." Both are wrong, and either
error would have propagated through structure, script, and demos before the Fact-Checker caught it.
I corrected them at the source: Meld is a **bi-timbral macro-oscillator synth** (only its
Plate/Membrane *filters* are physical-modelling-flavoured), and it shipped in **Live 12.0 on 5 March
2024**, with only the **Chord oscillator added in 12.2**. I also rewrote the subtitle the rest of
the pipeline would inherit. That is the job working as designed — the evidence layer catching a bad
premise so nobody downstream builds on it.

## 3. What I actually did

- **Five full research dossiers** (`specs/ableton_course_ep{1..5}_*_research.md`), each ~6 sections:
  annotated device parameter reference, history/theory narrative, artist deep-dives, song-curation +
  demo mapping, technical-synthesis depth, and a script-feeding outline.
- **Operator (ep1):** got the domain anchors exactly right and load-bearing — 11 algorithms enumerated,
  Coarse-integer/Fine-fraction asymmetry, feedback-only-on-unmodulated, modulator Level ≈ modulation
  index — plus the Jacobi–Anger/Bessel spectrum math and the Chowning "discovery of the ear" timeline
  with verbatim quotes.
- **Analog (ep2):** corrected the ship-version (Live 7/2007, AAS-licensed — not in-house, not Live 4),
  and ran the running "famous correction" thread: the original Reese is a **Casio CZ phase-distortion**
  synth (Saunderson's own hedged quote captured), "I Feel Love" engineer is **Wedel not Wootton**,
  TB-303 slope flagged as genuinely contested (18 vs 24 dB).
- **Wavetable (ep3):** sourced the PPG/Palm origin vs the Max-Mathews table-lookup distinction and
  busted the "wavetable soundcard" misnomer.
- **Meld (ep4):** the version + physical-modelling corrections (§2); the **verbatim oscillator-type
  table from `docs.cycling74.com/.../abl.dsp.meldosc~`**; the precise, restrained Plaits-lineage framing
  ("acknowledged influence, NOT Plaits code inside Meld"); and the honest **"no confirmed Meld artist
  track"** flag with named-artist connections explicitly marked as *thematic kinship, not credit*.
  Shipped the only standalone `source_map.json`.
- **Warp Modes (ep5):** reframed "invisible tempo plumbing" into a sound-design story with an explicit
  Gate-1 XY block, and tied each mode to its characteristic, reproducible failure mode.

## 4. Concerns before publish

- **Source-map coverage is uneven.** Only ep4 has a machine-readable `source_map.json`. The
  Fact-Checker's Gate 6 contract is the JSON map — for **ep1, ep2, ep3, ep5 the citations live inline
  in the dossier prose, not in a `claim_id → {source,url,quote}` file.** Before those episodes go to
  Gate 6, someone must extract their inline citations into source-maps, or the Fact-Checker has no
  exact contract to audit against. **Do not treat ep1/2/3/5 as having a complete source-map.**
- **Known-unverified values (ep4), flagged in-dossier, must not be stated on-mic as written:**
  Meld's Poly voice cap (manual read gave 12 vs 32 — conflict), and the exact normalized ranges of the
  oscillator macros. I marked these "verify in the live device"; that verification has not happened.
- **Forum/consensus claims are flagged but not all independently confirmed.** e.g. the Operator
  pitch-env/LFO-rate "bug-or-feature" (single forum thread), TB-303 filter slope, "six 303s" for
  Hardfloor. These are caveated inline ("forum consensus, not a confirmed interview") — keep the caveat
  in the script; don't let the Writer harden them into flat assertions.
- **One quote needs re-fetch:** the Josh Wink/Mixmag page returned a 403 during research (noted in the
  ep2 dossier). Verify that verbatim quote against a live page before it's read on tape.
- **Live-12 version drift:** dossiers are scoped to the user's stated build at research time. Re-confirm
  any "added in 12.x" feature claim (esp. Meld's Chord osc) against the current release notes at publish.

---

**Files (all absolute):**
- `/Users/zak/zacharysbrown/idm-course/specs/ableton_course_ep1_research.md`
- `/Users/zak/zacharysbrown/idm-course/specs/ableton_course_ep2_analog_research.md`
- `/Users/zak/zacharysbrown/idm-course/specs/ableton_course_ep3_wavetable_research.md`
- `/Users/zak/zacharysbrown/idm-course/specs/ableton_course_ep4_meld_research.md`
- `/Users/zak/zacharysbrown/idm-course/specs/ableton_course_ep4_meld_source_map.json`
- `/Users/zak/zacharysbrown/idm-course/specs/ableton_course_ep5_warp_modes_research.md`
