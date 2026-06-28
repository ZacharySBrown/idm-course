# The Production Harness — A Multi-Agent Pipeline for Instructional Synthesis Podcasts

> Goal: produce episodes the way a commercial narrative/music-education show does — with
> specialized roles, hard phase gates, and objective pass/fail criteria — so the result is
> coherent, the examples land, and every patch is reproducible.

This document is the architecture. See [`01-PERSONAS.md`](01-PERSONAS.md) for the agent roster
and [`02-QUALITY-GATES.md`](02-QUALITY-GATES.md) for the concrete rubrics each gate enforces.

---

## 0. Why — the first pass proved ad-hoc production yields an ad-hoc result

Episode 1 (Operator) shipped, but the listener (you) named four failure modes. Every one of
them traces to a *missing role* or a *missing gate*:

| Observed failure | Root cause | The role/gate that prevents it |
|---|---|---|
| "Narrative was strange and jumpy" | No story editor; script written slide-by-slide with no arc or beat structure | **Story Editor** gate (arc + signposts) + **Fresh-Ears** read on the locked script |
| "Audio examples out of place (wrong spot)" | Cue placed by intuition; no temporal-contiguity discipline | **Sound Designer** cue-placement gate (operative word overlaps the audible event within ~¼s) |
| "Described parameter changes missing from the demo" | The demo and the script were authored separately and never reconciled | **Ableton Expert** owns demo↔script reconciliation; the patch step-table is the single source of truth |
| "Examples don't clearly demonstrate the concept" | No one verified the demo *actually demonstrates* anything; we only checked it wasn't silent | **Ableton Expert** demonstration-verification gate (A/B obvious on bad speakers + spectral proof) |
| (new requirement) "I can't reproduce the patches" | Patches lived only as render params | **Ableton Expert** ships an `.adv` preset **and** a click-by-click tutorial for every patch |

The fix is not "try harder." It is **a pipeline where each concern is owned, and no stage
advances until its gate passes.**

---

## 1. Core principles (from the production-craft and learning-science research)

1. **The Story Editor is the load-bearing role and the gatekeeper.** In real shows the editor
   is "the proxy for the audience." Structure is locked *before* any sound work. We make the
   Story Editor the pipeline's orchestrator, not a peer reviewer.
2. **Hard, blocking phase gates.** Sound design does not begin until the **script is LOCKED**.
   Mixing does not begin until **fact-check clears**. These are dependencies, not suggestions.
   (This is the film-post model the whole audio industry borrows.)
3. **Demonstrate → label, framed by silence, with the word over the event.** Temporal
   contiguity is one of the most robust findings in multimedia learning (median *d = 1.31*):
   the naming word must overlap the audible event in working memory. Default structure for
   every demo: **frame ("notice the brightness") → demo → label ("that was the modulation index")**.
4. **One variable, A/B on a loop, exaggerated, audible on bad speakers.** If you can't pick A
   from B blind on laptop/phone speakers, the demo cannot teach — exaggerate it, sweep it, or
   cut it. Never lead with the subtle version.
5. **A demo is music; two musics = ambiguity. Mute the bed entirely during every demo.** Beds
   are for narration only. Under a demo, the bed goes to silence, the demo plays alone, the bed
   returns after a beat of silence.
6. **Reproducibility is a deliverable.** Every Ableton patch ships as an `.adv` preset *and* a
   tutorial that rebuilds it click-by-click from the default device. Any "long string of device
   settings" mentioned in narration generates a tutorial automatically.
7. **Adversarial, isolated verification.** The fact-checker and the fresh-ears reviewer have no
   stake in the draft and (deliberately) limited prior context — they catch what the authors are
   too close to see.

---

## 2. The roster (one line each — full specs in `01-PERSONAS.md`)

| Agent | Owns | Exists to prevent |
|---|---|---|
| **Showrunner / EP** | Brand voice, greenlight, final sign-off | Off-brand or unfinished episodes shipping |
| **Researcher** | The fact dossier + source map | Unsupported claims, thin reporting |
| **Story Editor** *(orchestrator + gatekeeper)* | Arc, beat structure, **script LOCK** | Jumpy / disjointed narrative |
| **Writer** | Prose in-voice; `[cue]`/`[bed]`/`[pause]` placement | Flat, jargon-heavy, or off-voice copy |
| **Ableton Expert / Patch Director** | Demo correctness, **presets + tutorials**, demo↔script reconciliation | Demos that don't demonstrate; missing param changes; irreproducible patches |
| **Sound Designer** | Cue placement, bed-muting, silence framing, A/B structure | Examples "out of place"; beds competing with demos |
| **Mix / Master Engineer** | Loudness spec, intelligibility, consistency | Muddy mix, masked dialogue, loudness jumps |
| **Fact-Checker** *(isolated)* | Every claim verified against source **and tape** | Errors, defamation, retraction |
| **Fresh-Ears Reviewer** *(no prior context)* | The cold listen — script and final cut | Confusion the authors can't see ("tape-loop-interrupter") |

---

## 3. The pipeline — phases, owners, and gates

Each phase produces a **reviewable artifact** and ends at a **blocking gate**. A gate FAIL routes
back with specific notes (notes culture: specific, motivating, critique-the-work). The Story
Editor adjudicates; the Showrunner holds final authority, used sparingly.

| # | Phase | Owner | Artifact | **GATE (blocking) — pass criteria** |
|---|---|---|---|---|
| 0 | Commission | Showrunner | `brief.md` (topic, angle, audience, the one idea) | Brief states a real *angle*, not just a topic |
| 1 | Research | Researcher | `research-dossier.md` + `source-map.json` | **XY test**: "story about X; what's interesting is Y" and Y is interesting to the audience; every future claim has a source |
| 2 | Structure | Story Editor | `outline.md` (beat sheet: acts, concept blocks, where demos go *conceptually*) | Arc present (anecdote + reflection alternate); signposts planted; **focus sentence writeable** in one line |
| 3 | Demo design *(parallel w/ 4)* | Ableton Expert | `demos/<id>.md` (recipe + what-you-hear + verification + structure) + `presets/<id>.adv` + `tutorials/<id>.md` + `clip_manifest.yaml` rows | Every demo isolates ONE variable, has an A/B or sweep structure, a stated "what you'll clearly hear," and a verification method |
| 4 | Script | Writer | `script/*.md` with frame→demo→label around each `[cue]` | Lexicon clean (no banned phrases, no exclamations); every `[cue]` resolves to a demo; demo↔script param claims reconciled with the Expert |
| 5 | Story edit + table read | Story Editor + Fresh-Ears (on script) | revised `script/*.md` | Read aloud passes; each beat raises a question the next answers; transitions smooth → **SCRIPT LOCK** |
| 6 | Fact-check | Fact-Checker *(isolated)* | `factcheck-report.md` (every claim → source, incl. spoken claims) | 100% of claims cleared or corrected |
| 7 | Render | Renderers + Ableton Expert | narration WAVs + `.cues.json`; demo/song WAVs | Every demo **passes demonstration-verification** (A/B obvious + spectral proof, not just "not silent"); preset+tutorial round-trip verified |
| 8 | Sound design / assembly | Sound Designer + assembler | episode MP3 + `cuemap.json` | **17-point demo-placement QA** passes for every cue (contiguity, bed muted, silence framing, loudness-matched) |
| 9 | Mix / master | Mix Engineer | mastered MP3 + `mix-report.json` | −16 LUFS (±1), true-peak ≤ −1 dBTP, VO intelligible over every bed |
| 10 | Fresh-ears final | Fresh-Ears *(no context)* | `freshears-report.md` | Cold listen: "could I tell what's the example and what it demonstrates?" — no confusion flags |
| 11 | Sign-off & publish | Showrunner | `signoff.md` + feed | EP approves; `build_podcast_feed.py` runs |

**The two hardest, most important gates:** the **SCRIPT LOCK** (5) — sound design must never
chase a moving target — and **demonstration-verification** (7) — the demo must provably
demonstrate the concept before it's allowed into the mix.

---

## 4. The demo-correctness system (the heart of the fix)

This is what was missing. The **Ableton Expert** turns each concept into a *provably
demonstrative* demo, and owns three artifacts per demo that stay in sync:

### 4a. The demo spec (`demos/<id>.md`) — extends the `clip_manifest.yaml` schema
New required fields per `operator_demos` entry:

```yaml
- id: op-index-sweep
  concept: "Modulation index → brightness"
  what_you_hear: "One held pitch, constant in pitch & loudness, opening from a pure sine into a brass-like buzz."
  structure: sweep            # one of: ab | sweep | ladder | single
  isolates: "Osc-B Level"     # the ONE variable that changes; everything else is held
  verification:
    audible: "Pitch/loudness constant; only harmonic content rises."
    spectral: "Spectrum analyzer: lone fundamental → symmetric sidebands at f_c ± n·f_m grow with Level."
    assertion: "rms-flat ± 2 dB across the clip AND spectral-centroid rises monotonically"   # machine-checkable
  preset: op-index-sweep      # -> presets/op-index-sweep.adv
  tutorial: op-index-sweep    # -> tutorials/op-index-sweep.md
  # ...existing params/automation/midi fields...
```

`structure` drives how the demo is built and how the Sound Designer places it:
- **ab** — play A, beat of silence, play B (same loop, one variable changed). For discrete
  contrasts (integer vs irrational ratio, algorithm A vs B).
- **sweep** — hold a note, move ONE continuous parameter from min→max so the listener hears it
  *move* (index, feedback, cutoff).
- **ladder** — 3 discrete steps (none / slight / dramatic) so the listener calibrates the axis.
- **single** — one self-contained sound (used sparingly; must still be unmistakable).

### 4b. Demonstration-verification (Gate 7) — a demo that doesn't demonstrate is rejected
For every rendered demo the Expert runs a machine check tied to `verification.assertion`, e.g.:
- *index sweep*: RMS roughly flat across the clip (loudness constant) **and** spectral centroid
  rises monotonically (brightness grows). If centroid is flat → the sweep didn't take → reject.
- *ratio A/B*: segment A's partials land on integer multiples (harmonic); segment B's don't
  (inharmonic) → measurable as harmonic-comb correlation. If A and B look the same → reject.
- *rhythmic FM*: onset rate matches the intended grid at the set BPM. (This is exactly the check
  that caught `op-rhythmic-single == instance2` in ep1.)
- *velocity → depth*: high-velocity segment has more sideband energy than low. If equal → reject.

These are not "is it audible" checks — they are "does the audible change *prove the concept*"
checks. The toolkit for them already exists (`librosa`, `ffmpeg volumedetect`, the spectral
analysis used in the ep1 post-mortem) and becomes a reusable `verify_demo.py`.

### 4c. Reproducibility — preset + tutorial, kept in sync, for every patch
Single source of truth: the **patch step-table** (the ordered list of `{operator, param, value}`).
From it the Expert produces, and the harness persists:
- **`presets/<id>.adv`** — the Ableton preset (gzipped XML), saved from Live, so the patch is
  recallable with one drag. Committed to the repo.
- **`tutorials/<id>.md`** — a click-by-click rebuild from the *default* Operator, one parameter
  per step, each row stating the panel, exact name, exact value, and **what you should hear after
  this step** so the learner self-checks. Template in `02-QUALITY-GATES.md`.
- **Round-trip check:** load the `.adv` fresh, walk the tutorial from default, confirm identical
  sound + analyzer image; `gzip -cd` both presets and diff the XML — any drift between tutorial
  and shipped preset shows up as a changed `<Manual Value>`.

**Rule enforced at Gate 4 (Script):** if the narration utters a string of device settings
("Coarse 1, Fine 414, Level 80, feedback 30…"), that string MUST have a corresponding tutorial
id, or the line is rejected. No orphan setting-strings.

The companion HTML/PDF (already built per episode) gains a **Patch Tutorials** appendix and links
each demo to its `.adv` download.

---

## 5. Anti-failure mapping (which gate catches each ep1 failure)

- **Jumpy narrative** → Gate 2 (arc/signposts/focus-sentence) + Gate 5 (read-aloud, beat
  question-chain, transitions) + Gate 10 (fresh-ears cold listen).
- **Examples in the wrong spot** → Gate 8 item: the operative naming word overlaps the demo
  onset within ~¼s; the `cuemap.json` makes cue timing measurable, so this is auto-checkable
  against the script's frame→demo→label structure.
- **Missing parameter changes** → Gate 3 (the demo's `isolates`/params are the source of truth)
  + Gate 4 (demo↔script reconciliation: every param the script names must be in the patch and
  audibly present) + Gate 7 (verification confirms the change is in the render).
- **Demo doesn't demonstrate** → Gate 7 demonstration-verification (reject if the spectral/onset
  proof fails) + Gate 10 fresh-ears ("could I tell what it demonstrates?").
- **Bed competing with the example** → Gate 8 (bed hard-muted for the demo's full duration; not
  ducked — muted).

---

## 6. Schema & tooling upgrades (build on what exists, don't reinvent)

The existing Python pipeline (`render_voiceover`, `extract_clips`, `operator_render_osc`,
`build_episode` + `cuemap.json`, `build_podcast_feed`, `alignment_report`) is reusable as the
mechanical substrate. The harness adds the *editorial* and *verification* layers:

1. **`clip_manifest.yaml` demo schema** gains `concept`, `what_you_hear`, `structure`,
   `isolates`, `verification`, `preset`, `tutorial` (§4a).
2. **Script convention**: codify **frame → demo → label** as the required shape around every
   `[cue]`; add `[demo-mute-bed]` semantics so the assembler knows to silence the bed for that
   cue's duration. (Today beds only duck — they must *mute* under demos.)
3. **`build_episode.py`**: bed track must drop to silence over any demo cue's span (not just
   sidechain-duck), with a short fade and the standard 0.5–1s silence frame before/after the demo.
4. **New `verify_demo.py`**: runs the §4b assertions; emits a `demo-verification.json` gate report.
5. **New `sound_design_qa.py`**: runs the 17-point checklist against `cuemap.json` + script;
   emits `sound-design-qa.json` (extends `alignment_report.py`).
6. **New `build_tutorials.py`**: from each patch step-table, render `tutorials/<id>.md` and validate
   it round-trips against `presets/<id>.adv`.
7. **Mastering**: confirm final integrated loudness −16 LUFS ±1 and true-peak ≤ −1 dBTP as a
   hard gate (today it's applied but not asserted).

---

## 7. Orchestration — how it actually runs

Two viable implementations; recommend starting with **(A)** and graduating to **(B)**.

**(A) Phase-gated runbook (Claude Code subagents).** A top-level orchestrator (the Story Editor
persona) walks the 12 phases. Each phase spawns the owning persona as a subagent with its system
prompt (`01-PERSONAS.md`) + the phase's input artifacts; the gate is a check the orchestrator runs
before advancing; a FAIL loops back with notes. Mechanical steps call the existing Python CLIs.
This is buildable now and matches how the repo already works.

**(B) Deterministic Workflow.** Encode the pipeline as a workflow script: `phase()` per stage,
`agent()` per role, hard barriers at the gates, and revision loops (`while !gate_pass`). Parallel
where independent (Demo Design ∥ Script; per-demo verification fans out). Adversarial verification
(fact-check, fresh-ears, demonstration-verify) runs as isolated agents with no draft context. This
is the scalable target once the personas and gates are validated on one episode.

Either way the **invariants** are the same: blocking gates, isolated verifiers, artifacts at every
handoff, and the Story Editor as adjudicator.

---

## 8. Artifacts & handoff contracts (the paper trail)

```
episodes/<ep>/
  brief.md                 # Showrunner
  research-dossier.md      # Researcher
  source-map.json          # Researcher  (claim -> source)
  outline.md               # Story Editor (beat sheet, arc, concept blocks)
  demos/<id>.md            # Ableton Expert (recipe + verification)
  presets/<id>.adv         # Ableton Expert (committed)
  tutorials/<id>.md        # Ableton Expert (click-by-click rebuild)
  clip_manifest.yaml       # Ableton Expert + Sound Designer
  script/*.md              # Writer  (frame->demo->label, [cue]/[bed]/[pause])
  factcheck-report.md      # Fact-Checker (isolated)
  build/ … cuemap.json     # render + assembly
  demo-verification.json   # Gate 7
  sound-design-qa.json     # Gate 8
  mix-report.json          # Gate 9
  freshears-report.md      # Gate 10 (isolated)
  signoff.md               # Showrunner
```

Each artifact is the *contract* the next role consumes — no role reaches behind another's output.

---

## 9. Implementation roadmap

- **M1 — Personas + gates as docs (this commit).** The roster, rubrics, schema, checklists.
- **M2 — Verification tooling.** `verify_demo.py`, `sound_design_qa.py`, `build_tutorials.py`;
  wire bed-muting-under-demos into `build_episode.py`. Backfill ep1 as the test fixture.
- **M3 — Persona agent files.** Turn each persona into a runnable subagent prompt
  (`.claude/agents/`), with its gate rubric inlined.
- **M4 — Orchestrator (A).** The phase-gated runbook over one fresh episode (e02), proving the
  gates catch the ep1 failure classes.
- **M5 — Re-cut ep1** through the full harness as the reference episode.
- **M6 — Workflow (B).** Encode the validated pipeline as a deterministic workflow for scale.

---

*This plan is grounded in: commercial narrative/music-podcast production practice (Radiolab,
99% Invisible, Song Exploder, Switched on Pop, This American Life), multimedia-learning science
(Mayer's temporal-contiguity & signaling principles; the generation effect), instructional
sound-design practice (FabFilter/Sound on Sound demonstration technique; broadcast bed-level
standards), and the FM/Operator domain (Ableton manual, Chowning FM theory). Full source lists
live in the research records that produced this design.*
