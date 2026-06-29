# Harness Contribution Reports — ableton-devices podcast

Each of the 9 production-harness personas wrote a self-report on its own contribution:
a **readiness assessment** (from its gate's standpoint), **what it's proud of**, and a
**brief, evidenced summary of what it actually did** — under a hard honesty mandate
(report only evidenced work; if a gate didn't run, say so). Generated 2026-06-29.

## The reports

| Persona | Gate(s) | Report |
|---|---|---|
| Researcher | 1 — cited dossier | [researcher.md](researcher.md) |
| Story Editor | 2 outline · 5 lock | [story-editor.md](story-editor.md) |
| Writer | 4 — in-voice prose + cue choreography | [writer.md](writer.md) |
| Ableton Expert | 3 demo design · 7 demonstration-verify | [ableton-expert.md](ableton-expert.md) |
| Fact-Checker | 6 — isolated adversarial verify | [fact-checker.md](fact-checker.md) |
| Sound Designer | 8 — timeline + demo/bed placement | [sound-designer.md](sound-designer.md) |
| Mix / Master | 9 — loudness + intelligibility | [mix-master.md](mix-master.md) |
| Fresh-Ears | 5 table-read · 10 cold listen | [fresh-ears.md](fresh-ears.md) |
| Showrunner / EP | 0 greenlight · 11 sign-off | [showrunner.md](showrunner.md) |

---

## What the orchestration did WELL (cross-cutting, multiple agents independently)

1. **Editorial consistency is genuinely strong and is the voice bible working.** Showrunner,
   fresh-ears, and story-editor independently confirm the same locked signatures across all
   five episodes: a **cold-open confession** (never "welcome to week N"), a planted **N-stop
   map**, a **seeded→echoed→landed refrain** that closes on an exercise (zero motivational
   kickers), **receipt-first / caveat-inline** honesty, and an **Act-4 device tour held by one
   driving question** (the deliberate fix for the "Section-4 flatline" first named in ep1).
2. **The harness caught real defects this session** — not cosmetic ones:
   - ep2's 8 "silent demos" root-caused as a **renderer/param bug**, not the handoff's param-value theory.
   - **Meld** reframed (bi-timbral macro-osc MPE, *not* physical modelling) and re-dated (Live **12.0**, not 12.1) *before* anything was built on it.
   - **Black Refraction** corrected (Tim Hecker, *Virgins* 2013 — not *Ravedeath*).
   - Reference-correct **Reese / digeridoo** rebuilds; the **jumpy-narrative** diagnosis → re-cut.
3. **Loudness consistency across episodes is effectively solved** — measured spread **0.2 LU**
   (e01 −16.2, e02 −16.0, e03 −16.0 LUFS), because all three share one mastering config.
4. **The agents were honest about their own gaps** — they corrected the orchestrator (ep2 *did*
   run fact-check), refused to fake demonstrativeness, and labelled retrospective assessments as
   such. Credible self-reporting is itself a signal the orchestration is working.

## What the reports converge on as WEAK (the real backlog)

1. **Gate *receipts* aren't being written.** Independently flagged by ableton-expert, fact-checker,
   sound-designer, mix-master, showrunner: **no per-episode `factcheck-report.md`, `source-map.json`
   (except ep4), `demo-verification.json`, `mix-report.json`**, no green `sound-design-qa` run, and
   **0 `.adv` presets committed**. The gates happen *informally* (in the produce-episode run or by
   hand) but don't emit the structured artifacts the spec mandates — so "passed" is **asserted, not
   evidenced**. This is the #1 theme.
2. **The evidentiary standard weakens across the series.** ep1–ep3 demos are mostly machine-verifiable;
   ep4 (~9/19) and ep5 (effectively all) **cannot be proven over the headless path** (Meld mod-matrix
   + MPE not LOM-exposed; warp = clip property). The *voice* stays consistent; the *proof* does not.
   The fix is to render+verify or to **downgrade those demos on-mic to "tutorial, not proven render."**
3. **Concrete, actionable bugs surfaced (do these):**
   - **ep2 true-peak FAIL: −0.5 dBTP** (over the −1.0 ceiling). Cause: `build_episode.py` limiter
     `limit=0.97` is looser than the loudnorm TP target. *Re-master e02.*
   - **Beds silently dropped:** `build_episode.py build_bed_track` does `if not src: continue`, so a
     `TBD`/missing bed clip yields a **bed-less episode with no error**. ep4/ep5 would build dry.
   - **`validate.ts` lexicon linter has a broken `yaml` import** — voice-clean is currently grep-asserted, not linted.
   - **ep1 script↔patch mismatches:** `06a-rhythmic-fm` (Beat-envelope on carrier A, script says modulator B);
     `05g-velocity` (script names a Time<Vel routing the patch lacks).
   - **ep1 `op-feedback-bifurcation` is inert** over OSC (measured flat sine); needs hands-on.

## Per-episode readiness, reconciled across all 9 reports

| Ep | Status | Editorial | Demos | Loudness | Beds | Net |
|----|--------|-----------|-------|----------|------|-----|
| e01 Operator | published | LOCKED (re-cut fixed the "jumpy mess") | feedback inert; 2 script↔patch flags | −16.2 / −1.1 ✓ | real | **published, narrative-clean, demo flags open** |
| e02 Analog | published | strongest; reference build | 23/23 render | −16.0 / **−0.5 ✗** | real | **re-master for true-peak, else clean** |
| e03 Wavetable | published | clean | 18/20 (2 Hi-Q can't) | −16.0 / −1.4 ✓ | real | **published; 2 demos need hand-render or narration** |
| e04 Meld | editorial-locked | most disciplined script pkg | ~8/19 headless | not built | **TBD** | **ready-pending-render; matrix/MPE = tutorials** |
| e05 Warp | editorial-locked | strong angle | warp = bounce, not render | not built | partial TBD | **ready-pending-render + source audio** |

**On the showrunner's open question** (did e01 publish dirty, or were flags fixed post-summary?):
the **narrative** mess was fixed and shipped clean (the re-cut — four-stop map, signposts, 8 fact
corrections, verified in the published scripts). The **demo** flags (feedback inert, 2 script↔patch
mismatches, empty `presets/`) are **genuinely still open** — the SUMMARY is accurate, not stale. e01
is narrative-clean and demo-flagged.

## Recommended next actions (in priority order)
1. **Re-master e02** (tighten the limiter ceiling to honor −1 dBTP) and re-push.
2. **Make unresolved `clip_id`s build-blocking** + add a deterministic bed-planner so every episode
   gets beds (closes the silent-skip).
3. **Emit the gate receipts**: `demo-verification.json`, per-episode `factcheck-report.md` +
   `source-map.json`, `mix-report.json`, and a green `sound-design-qa` run — so "passed" is provable.
4. **Fix the `validate.ts` yaml import** and run a real line-level lexicon pass on all five scripts.
5. **ep1 reconciliations**: fix the two script↔patch mismatches; commit `.adv` presets.
6. **ep4/ep5**: render what's renderable; downgrade the non-headless demos on-mic to "tutorial."
