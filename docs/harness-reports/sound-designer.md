# Sound Designer — Harness Contribution Report (Gate 8)

Role: place every demo so it lands; mute beds under demos; frame with silence; loudness-match;
prevent "out of place" examples and beds smearing demos. Gate 8 = timeline assembly
(`build_episode.py`) + demo-placement QA (`sound_design_qa.py`) + beds/transitions.

This report describes the **actual** placement state on disk, not the intended one. Sources
inspected: the `beds:`/`transitions:` blocks in all five `episode.yaml` files, the QA output
`courses/ableton-devices/tools/alignment_app/sound-design-qa.json`, the extracted clips under
`build/ableton-devices/audio/clips/`, and the bed/mute logic in `shared/tools/build_episode.py`.

---

## 1. Readiness (Gate 8) per episode — beds + transitions

Each `episode.yaml` carries a `beds:` block (`enabled`, `duck_db: -14`, `insertions[]`) and a
`transitions:` block (`insertions[]`). Each bed insertion names a `clip_id`, a
`start_at_slide`/`end_at_slide` span, and a `gain_db`; each transition names an `after_slide` and a
`clip_id`. The structure exists in **all five** episodes. What differs is whether the `clip_id`s are
real (resolve to a WAV on disk) or `TBD` placeholders.

| Ep | Beds (sections covered) | Bed clips on disk? | Transitions | Trans clips on disk? | Truth |
|----|------------------------|--------------------|-------------|----------------------|-------|
| **e01-operator** | 4 bed spans (§02,§03,§04,§06) | YES — all 4 (`bed-stria-drift`, `bed-xtal-pad`, `bed-ascent-pad`, `bed-black-refraction-amb`) | 5 | YES — all 5 (`trans-syro-warm`, `trans-bike-pulse`, …) | **Placed & resolvable** |
| **e02-analog** | 4 bed spans (§02,§03,§04,§06) | YES — all 4 (`bed-i-feel-love`, `bed-flash-light`, `bed-can-you-feel-it`, `bed-tri-repetae`) | 5 | YES — all 5 | **Placed & resolvable** |
| **e03-wavetable** | 4 bed spans (§02,§03,§04,§06) | YES — all 4 (`bed-see-you-drift`, `bed-everybody-pad`, `bed-polymer-texture`, `bed-polymer-amb`) | 5 | YES — all 5 | **Placed & resolvable; QA run (see §3)** |
| **e04-meld** | 4 bed spans named | **NO — every `clip_id` is literally `TBD`** | 5 | **NO — every `clip_id` is `TBD`** | **Placeholder only.** No `clips/e04-meld/` dir exists |
| **e05-warp-modes** | **only 2 bed spans** (§02,§06); §03,§04,§05 have **no bed** | **NO — `clips/e05-warp-modes/` dir does not exist**; both spans reuse one id `bed-warp-cloud` | 4 (`trans-warp-seam-1..4`) | **NO — no clips dir** | **Named but unrendered; partial coverage** |

Per-episode bed coverage of the four narration-heavy sections (§02 history, §03 mechanism, §04
architecture, §06 advanced) — the boundaries where a bed is expected:

- e01: 4/4 covered, all clips present.
- e02: 4/4 covered, all clips present.
- e03: 4/4 covered, all clips present.
- e04: 4/4 *named* but 0/4 renderable (all TBD).
- e05: **2/5** sections carry a bed at all, and 0 of those clips are on disk.

**Were ep2/ep3 beds auto-filled by the pipeline or by hand?** They were **scripted/orchestrated, not
agent-reasoned.** The `produce-episode` orchestrator wrote concrete `clip_id`s into ep1/ep2/ep3 and
those bed/transition WAVs were rendered and extracted (they sit in `clips/e0{1,2,3}-*/`). That is why
ep1–ep3 look "done." It was a pipeline+human pass for those three episodes, not a generalizing rule.

**Are ep4/ep5 still TBD?** Yes. e04 is editorially complete (locked, fact-corrected — commit
`009f945`) but its bed/transition `clip_id`s are unfilled `TBD` and **no `clips/e04-meld/` directory
exists** — neither demos nor beds have been rendered/extracted. e05 is editorially complete (commit
`700038d`) with *named* bed/transition ids, but **no `clips/e05-warp-modes/` directory exists**, and
its bed block only covers 2 of 5 sections to begin with. So ep4 and ep5 are **not built**, and their
bed placement is not real.

---

## 2. Will we ALWAYS have background sounds at appropriate places? — honest answer: **No, not today.**

Two separate things must both be true, and only one of them is currently guaranteed:

**What the engine guarantees (mixing behavior).** `build_episode.py` is solid here. If a bed
insertion resolves, the engine: (a) loops the clip across the section span with fade-in/out
(`build_bed_track`), (b) **sidechain-ducks** it under narration (`sidechaincompress
threshold=0.04:ratio=8`, mixed at weight `0.55`), and (c) **hard-mutes** it to silence under every
foreground demo/song cue — not a duck — via `volume=0:enable='between(t,...)'`, with the mute span
padded 200ms so the bed is already silent as the demo begins. That directly implements Gate 8 items
9–11 and is exactly the ep1 "beds competing with demos" failure, fixed in code. When a bed is
present, it behaves correctly.

**What is NOT guaranteed (the placement decision).** The engine only acts on insertions whose
`clip_id` resolves to a file. Read the resolver in `build_bed_track`:

```python
cid = ins.get("clip_id")
if not cid:
    continue
# ... search for {cid}.wav/.aif/.aiff ...
if not src:
    continue   # <-- TBD, or any missing clip, is SILENTLY SKIPPED
```

A `clip_id: TBD` matches no file, so the insertion is **silently dropped with no warning, no error,
no FAIL.** This is the load-bearing risk: **ep4 (all TBD) and ep5 (clips dir absent) would build to a
finished episode with NO bed under any section and NO transition stings — and nothing in the build
would complain.** The "appropriate place" decision — *which* bed clip belongs under *which* section
boundary — is **not reliably auto-generated.** It was hand/orchestrator-filled for ep1–ep3 and left
as `TBD` for ep4–ep5.

**What it would take to GUARANTEE coverage on every episode:**
1. **Make TBD/missing-clip a hard FAIL.** `build_episode.py` and `sound_design_qa.py` must reject any
   `enabled: true` bed/transition block containing an unresolved `clip_id` instead of skipping it.
   Silent-skip is the single most dangerous behavior here.
2. **A bed-coverage assertion in Gate 8:** every narration section ≥ N seconds must be covered by a
   resolvable bed span; flag uncovered sections (today e05 §03/§04/§05 would flag).
3. **A bed-selection step that runs per episode** (not per-ep1-3-by-hand): given the section themes,
   pick or generate a bed clip and emit a real `clip_id` + render it. Until that exists, "always have
   background" is a manual promise, not a guarantee.

---

## 3. What I'm proud of / what actually happened (no inflation)

Honest accounting: **this gate did not run as an autonomous agent that reasoned over five episodes.**
The work that exists was done by **scripts plus the orchestrator, with a human in the loop**, and it
covers **one episode end-to-end (e03) plus correct mixing infrastructure for ep1–ep3.**

- `sound_design_qa.py` exists and ran, but `sound-design-qa.json` contains **only e03-wavetable** (25
  cues, 4 bed spans). ep1/ep2 have no committed QA report from this tool, and ep4/ep5 have none.
- The QA that did run is **partly automated, partly deferred to manual review.** Auto checks cover
  `audible`, `loudness_matched`, `framed_by_silence`, `overlaps_bed`. The genuinely perceptual
  items — temporal contiguity (item 6), frame→demo→label ordering, A/B sequencing, the cold-window
  test — are emitted as `manual_review` strings, **not machine-verified.** I should not claim item 6
  is enforced; it is asserted as a to-do.
- That e03 run was **not all-green**: **12 of 25 cues are flagged.** Real flags: `wt-spectra-step1`
  is `demo +8.0dB vs nearby voice`; `everybody-wants-bass`, `wt-position-by-hand`, `wt-user-table-scan`
  are +6–7 dB hot (item 14 fail); and **10 cues report `no silence frame before the demo onset`**
  (item 12 fail). Per the mandate, all 17 points are blocking — so **e03 has not actually passed
  Gate 8**, and ep1/ep2 were never measured by this tool at all.

What I'm genuinely proud of, accurately stated: the **bed-vs-demo competition bug from ep1 is fixed
in the engine** (hard-mute, not duck, framed by a 200ms pre-roll), and **ep1–ep3 have real, rendered
bed and transition clips correctly anchored to section boundaries** with sensible per-bed gains. That
is a meaningful improvement over the shipped ep1. I am **not** claiming an agent passed Gate 8 on all
five episodes — it did not.

---

## 4. Concerns + concrete recommendation

**Concerns (ranked):**
1. **Silent-skip of unresolved clips** turns a missing decision into a clean-looking but bed-less
   episode. ep4/ep5 would ship dry and nothing would catch it. (Highest risk.)
2. **Gate 8 is advisory, not enforced.** The flagged e03 cues (hot demos, missing silence frames)
   would pass through because the QA report doesn't gate the build. The gate's own "every point is
   blocking" rule isn't wired to anything.
3. **Bed placement is bespoke per episode.** ep5 only covers 2/5 sections — there's no rule that says
   "every narration section gets a bed," so coverage drifts episode to episode.

**Recommendation — make bed/transition placement consistent and automatic:**
- **Promote bed/transition resolution to a build-blocking check.** In `build_episode.py`, if a
  `beds`/`transitions` block is `enabled` and any `clip_id` is `TBD` or unresolvable, **raise** —
  do not `continue`. Mirror it as a FAIL in `sound_design_qa.py`.
- **Add a deterministic bed-planner pass** that runs for *every* episode from the locked script's
  section structure: for each narration section ≥ ~20s with no bed, auto-assign a bed `clip_id` from
  a per-episode palette (or flag for one to be rendered), and emit the insertion. This converts "did
  someone remember to fill ep5 §03?" into a generated artifact.
- **Make `sound_design_qa.py` cover all built episodes and machine-check more of the 17 points** —
  at minimum item 6 (naming-word/onset overlap from `cuemap.json`), item 9 (assert bed RMS ≈ silence
  across every demo span, which the engine already enables), and item 12 (silence-frame presence,
  already detected but currently only warned). Then **fail the build on any flagged cue** so e03's 12
  flags can't slip through.
- **Before calling ep4/ep5 ready:** render+extract their `clips/` dirs, replace every `TBD`, extend
  e05's beds to all five sections, and run QA per episode to green.

Bottom line: the *mixing* of beds is correct and trustworthy; the *placement decision* is currently a
manual artifact that exists for ep1–ep3 and is missing for ep4–ep5 — and the build won't tell you.
That gap is the one thing standing between "we sometimes have background sounds in the right places"
and "we always do."
