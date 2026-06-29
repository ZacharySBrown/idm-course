# Harness Contribution Report — Fact-Checker (Gate 6, isolated/adversarial)

**Role:** independent verification of every on-air claim — including spoken claims that never
hit the page — against source material before the irreversible publish. I check the **tape**, not
just the script. When a fact collides with the narrative, the fact wins.

**Honesty note up front:** I report what the *record* shows, not what would make the pipeline look
finished. Two things below differ from the common framing: (1) ep2 did, in fact, run a fact-check
gate (the produce-episode commit `aab420d` says so explicitly), so "ep1/ep2 predate the gate" is
only true for ep1's *original* cut; and (2) **no `factcheck-report.md` or `source-map.json` exists
in any episode directory** — the only structured source map in the repo is
`specs/ableton_course_ep4_meld_source_map.json`. The fact-check work is real and is recorded in
commit messages and `SUMMARY.md`/`clip_manifest.yaml` notes, but the Gate-6 artifact my own spec
calls for has not been written per episode. That is a process gap, flagged in Concerns.

---

## 1. Readiness (Gate 6) per episode

| Ep | Device | Tape rendered? | Fact-check actually ran? | Verdict |
|----|--------|----------------|--------------------------|---------|
| e01 | Operator | **Yes** (`e01-operator.mp3`; `.before.mp3` = pre-recut tape) | **Yes — twice.** Original cut predates this gate; the **re-cut** (`7657989`) ran story-editor→writer→lock→fact-check and the isolated fact-checker caught 8 errors. | **Cleared-with-corrections** (re-cut). Tape was re-rendered after correction. |
| e02 | Analog | **Yes** (`e02-analog.mp3`) | **Yes.** produce-episode commit `aab420d`: "Fact-check corrections applied: Aphex/Digeridoo age softened (2x); TB-303 diode-ladder wording fixed." | **Cleared-with-corrections.** Tape rendered after editorial; spot tape-vs-script audit not separately logged. |
| e03 | Wavetable | **Yes** (`e03-wavetable.mp3`, all stems `ok` in `_render_status.json`) | **Yes.** Plaid "CLOCK"/*Polymer* label corrected in `clip_manifest.yaml`; Skrillex-not-Serum and Serum-rationale-to-Duda traps caught in dossier→script. | **Cleared-with-corrections.** |
| e04 | Meld | **No — not rendered.** No `narration/e04*` or `episodes/e04*.mp3`. | **Yes, on the script** (source-map exists; 4 named corrections applied). **Tape check impossible — there is no tape.** | **Cleared-with-corrections (script only).** Gate 6 cannot fully pass: the "check the tape" clause is unmet because no tape exists yet. |
| e05 | Warp Modes | **No — not rendered.** | **Partial.** Research dossier only; **no structured `source-map.json`**; several claims self-flagged for verification (e.g. Jon Hopkins quote "verify exact wording before quoting"). | **NOT fully checked.** Editorial-locked, but open claims remain and no tape. **Gate 6 = FAIL until rendered + source-mapped.** |

---

## 2. What I'm proud of — the most consequential catch

The **ep1 *Black Refraction* attribution**, caught in the re-cut and inherited straight from the
dossier: the script had it on *Ravedeath, 1972* (2011). It is on **Tim Hecker's *Virgins* (2013)**.
That is the class of error that earns a public correction and erodes trust with exactly the
crate-digging audience this show courts — a wrong record title under a named artist, stated as
fact, in the cold tape. It was structural-adjacent (the dossier was wrong, so every downstream beat
inherited it), which is precisely the failure the *isolated* net exists to catch: the authors were
too close to the dossier to doubt it. Honorable mention: forcing the FM-patent claim from "second
most lucrative in Stanford history" down to "one of the most lucrative (behind recombinant DNA and
Google)" — the source supported the weaker statement, so the claim was softened to it.

## 3. What I actually did — evidenced corrections

**ep1 re-cut (8, commit `7657989`)** — *Black Refraction* → *Virgins (2013)*; Xtal teardown
credited to SynaMax 2022 (not Reverb Machine); FM patent "second" → "one of the most lucrative";
Chowning/CCRMA chronology decoupled from *Stria* + funding claim softened; patent dates made
internally consistent (filed 1974, granted 1977); DX7 "50k transistors" → "two custom Yamaha LSI
chips"; Aphex *Lannerlog* year softened to "as a teenager." (Commit lists 7 lines; header says 8.)

**ep2 (commit `aab420d`)** — Aphex/Didgeridoo age softened (×2); TB-303 diode-ladder wording fixed.

**ep3** — Plaid clip relabeled: there is **no title track "Polymer"**; the acquired cut is
**"CLOCK"** from the album *Polymer* (2019). The narration was left referencing the album/method
(not a track), so the on-air claim is correct and the manifest now carries the honest label
(`clip_manifest.yaml` lines 25–28). Also held: Skrillex 2010–11 growls are Massive+FM8 (not Serum,
shipped 2014); Serum editor rationale to Steve Duda, not deadmau5.

**ep4 (4 corrections, `source_map.json` + scripts verified)** — all confirmed present in the locked
scripts and **independently re-verified by web search today**:
- Poly cap = **12 voices** ("the voice drop-down goes up to twelve"), not "a few dozen." Dossier
  flagged this UNCERTAIN (12 vs 32 conflict); independent check resolves it to **12**. Fact won.
- **"Granulator III"** (not "Granulator") — confirmed as a Live 12.0 launch device.
- Meld reframed from "physical-modelling hybrid" to **bi-timbral macro-oscillator**; the only
  physical-modelling DSP is the Plate/Membrane *resonator filters* — the narration now states this
  plainly and turns the correction into a payoff beat (`03c`, `06d`).
- **Shipped Live 12.0, 5 March 2024** (not 12.1) — independently confirmed; Chord osc added 12.2.

## 4. Concerns (open before publish)

1. **ep4 and ep5 have no tape.** Gate 6's "check the rendered narration, not only the script"
   clause is structurally unmet for both. Every spoken number/name/date must be re-audited against
   the tape **after render** — TTS and any ad-libs can drift from the page. Do not treat ep4/ep5 as
   fact-cleared on the script alone.
2. **ep5 has no structured source-map and carries self-flagged open claims** — e.g. the Jon Hopkins
   destructive-resample ethos is marked "verify exact wording before quoting." Per my rubric, a
   claim with no source in a map cannot be cleared. ep5 is a **FAIL** until it has a `source-map.json`
   and a post-render tape audit. Route to Researcher (source map) then back to me.
3. **The Gate-6 artifact itself is missing.** My spec says I emit `episodes/<ep>/factcheck-report.md`
   per episode; none exist. The verification happened (commits prove it) but is not captured in the
   per-episode auditable form. Recommend back-filling one per shipped episode (e01–e03) so the
   "series of nets" is inspectable, not just asserted.
4. **ep1 feedback demo is a known unresolved item** (`FEEDBACK_FIX.md`): the shipped feedback demo
   is "weak but audible" and the headless render could not make Operator feedback buzz. Not a
   *factual* error in the narration, but the script's "sine → saw → broadband" causal claim is not
   currently proven by the tape it points at. Flag for a tape-vs-claim recheck once the demo is
   re-cut by ear.
