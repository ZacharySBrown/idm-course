# Quality Gates — Concrete Rubrics & Checklists

Every gate is **blocking**: the pipeline does not advance until it passes. A FAIL routes back to
the owning role with specific notes. These are the checklists the agents (and the verification
tooling) run.

---

## Gate 1 — Research (Researcher)
- [ ] **XY test**: "This is a story about **X**; what's interesting is **Y**" — and Y is interesting
      *to the audience*, not just the maker.
- [ ] Every technical claim has a primary source in `source-map.json`.
- [ ] Domain facts spot-correct (e.g., algorithm count, Coarse=integer/Fine=fraction, loop-mode names).

## Gate 2 — Structure (Story Editor)
- [ ] A one-line **focus sentence** is writeable. (If it's hard to write, the story isn't focused.)
- [ ] The piece has an **arc**: a driving question and a surprising payoff — not a flatline list.
- [ ] **Anecdote** beats (events that raise→answer questions) alternate with **reflection** beats
      ("why am I listening to this?").
- [ ] **Signposts** are planted that tell the listener why to keep going.
- [ ] Concept blocks are ordered by **"what do I need to know next for this to make sense?"** —
      not by best-material-first.
- [ ] Each demo has a *conceptual* home in a block (not yet timed).

## Gate 3 — Demo Design (Ableton Expert)
For **every** demo:
- [ ] States `concept` and `what_you_hear` in one sentence each.
- [ ] **Isolates ONE variable** — `isolates:` names it; everything else (note, patch, envelope,
      carrier) is held constant.
- [ ] Has a teaching `structure`: **ab** (A→silence→B), **sweep** (move one continuous param across
      a held note), or **ladder** (none/slight/dramatic). `single` only with strong justification.
- [ ] The change is **obvious on laptop + phone speakers** (not just monitors). If subtle →
      exaggerate, sweep, or cut.
- [ ] Has a `verification` block with a **machine-checkable `assertion`** (see Gate 7).
- [ ] Has `preset:` and `tutorial:` ids.

## Gate 4 — Script (Writer)
- [ ] **Lexicon clean**: zero banned phrases ("journey", "unleash", "game-changing", "AI-powered",
      noun-"deep dive"), zero exclamation points, zero emojis. (Hard fail.)
- [ ] Every `[cue: id]` resolves to a real demo in `clip_manifest.yaml`.
- [ ] **frame → demo → label** around each cue: an attention cue *before* the demo for perception
      demos ("notice the brightness…"), or **name-then-show** for build/procedure demos.
- [ ] **Demo↔script reconciliation:** every parameter/behavior the narration says the listener will
      hear is actually in that demo's patch and audibly present (confirmed with the Ableton Expert).
- [ ] Any spoken **string of device settings** carries a `tutorial:` reference — no orphan setting-strings.
- [ ] Reads aloud in-voice (concrete before abstract; deflate before inflate).

## Gate 5 — Story Edit + Table Read (Story Editor + Fresh-Ears on script) → **SCRIPT LOCK**
- [ ] Read **aloud** end to end — no tongue-knots, no run-ons.
- [ ] **Each beat raises a question the next answers** (no orphan facts, no "and also").
- [ ] Transitions between beats/sections are *motivated*, not abrupt.
- [ ] Fresh-Ears (cold) can follow the through-line and predicts no confusion.
- [ ] Editor's hierarchy satisfied: Clarity → Storytelling → Economy → Integrity → Meaning → Fine-tuning.
- [ ] **→ Lock the script. No sound work starts before this.**

## Gate 6 — Fact-Check (isolated Fact-Checker)
- [ ] Line-by-line: every number, name, date, quote, causal claim mapped to a source.
- [ ] **The tape (rendered narration) is checked**, not only the script.
- [ ] Ambiguous/uncertain claims re-verified or softened to what the source supports.
- [ ] Where a fact collides with the narrative, the **fact wins** (note the change).

## Gate 7 — Demonstration-Verification (Ableton Expert, after render) — `verify_demo.py`
A demo that doesn't *prove its concept* is rejected, not shipped. Per `structure`:

| Concept / structure | Machine-checkable assertion |
|---|---|
| **Index → brightness** (sweep) | RMS roughly flat across clip (loudness constant) **AND** spectral centroid rises monotonically start→end. Flat centroid ⇒ sweep didn't take ⇒ **reject**. |
| **Ratio: harmonic vs inharmonic** (ab) | Segment A's spectral peaks correlate with an integer harmonic comb of f0; segment B's do **not** (irregular spacing). A≈B ⇒ **reject**. |
| **Feedback → complexity** (sweep) | Harmonic count / spectral spread increases with feedback; tail approaches broadband. |
| **Rhythmic FM** (loop modes) | Onset rate matches the intended grid at the set BPM (e.g., 1/16 @120 ⇒ ~8 onsets/s); two layered instances have **distinct** onset rates. *(This is the exact check that caught `op-rhythmic-single == instance2`.)* |
| **Velocity → depth** (ab) | High-velocity segment has more sideband energy than low at identical pitch. Equal ⇒ **reject**. |
| **Algorithms** (ab) | Parallel algo shows discrete tuned peaks; deep-series shows dense modulated spectrum — measurably different. |

Plus, for every demo:
- [ ] Peak ≥ −22 dB and the demonstrative event is clearly above the noise floor on bad speakers.
- [ ] No dead-air tail (trailed silence trimmed to ≤ ~0.4 s).
- [ ] **Preset round-trip:** load `presets/<id>.adv` fresh, walk `tutorials/<id>.md` from the default
      Operator → identical sound + analyzer image; `gzip -cd` both presets and **diff the XML** clean.

## Gate 8 — Sound-Design Placement (Sound Designer) — `sound_design_qa.py`, **17 points per cue**
**Isolation & audibility**
1. Demo changes exactly ONE variable; source/note/patch/envelope held.
2. Change is audible in blind A/B on **laptop AND phone** speakers.
3. Continuous params use a **live sweep or stepped ladder** (motion, not two stills).
4. A/B'd **back-to-back on a short loop** (A→B, ideally A→B→A→B).

**Cue placement & temporal contiguity**
5. **Attention cue before** the demo (frame → demo → label).
6. **Operative naming word overlaps the demo onset within ~¼ s** (checked vs `cuemap.json`).
7. The label/name lands **immediately after** the demo, while the percept is still in working memory.
8. Right order for the content type: demonstrate-then-label (perception) vs label-then-demonstrate (procedure).

**Bed & competition (the big one)**
9. **Music bed fully MUTED (silent) for the entire demo** — not ducked. A ducked-but-audible bed
   under a synth demo is a FAIL.
10. Bed returns **after** the trailing silence, not on the demo's tail.
11. Beds under *narration* sit **≥18–20 dB below voice**, sidechain-ducked, never within 15 dB.

**Pacing & level**
12. **~0.5–1 s clean silence before and after** the demo frames it.
13. Demo length tight (**~1–2 bars / a few seconds per state**), not a meandering pass.
14. Demo **loudness-matched to dialog** when it's the focus (not 6 dB under/over).
15. ≤ ~4 demos per concept block before narration recovery.

**Episode-level**
16. Integrated loudness −16 LUFS (±1), true-peak ≤ −1 dBTP, consistent with prior episodes.
17. **Cold-window test:** from any 10-second window, could a listener tell which sound is THE
    example and what it demonstrates? If no → it reads as "out of place."

## Gate 9 — Mix / Master (Mix Engineer) — `mix-report.json`
- [ ] Integrated loudness **−16 LUFS ±1** (Apple target; hold episode-to-episode).
- [ ] True-peak **≤ −1 dBTP** after limiting (survives platform transcode).
- [ ] **VO intelligible over every bed** — no masking on earbuds.
- [ ] Dialog gently compressed (2:1–4:1); demos sit at dialog loudness when focal.

## Gate 10 — Fresh-Ears Final (isolated Fresh-Ears)
- [ ] Cold listen to the assembled cut, no prior context.
- [ ] Through-line followable per concept; no "wait, what just happened" flags.
- [ ] Every demo passes the **cold-window test** (item 17).
- [ ] Report is timestamped; any flag routes back to the owning role.

## Gate 11 — Sign-off (Showrunner)
- [ ] All upstream gate reports green.
- [ ] Voice matches `voice.md`; off-brand nothing.
- [ ] Publish: `build_podcast_feed.py`.

---

## Appendix A — Tutorial template (`tutorials/<id>.md`)
Start from a **freshly loaded default Operator**. One parameter per step. The "hear" column is the
self-check.

```markdown
# Patch: Polynomial-Bell  (preset: presets/op-poly-bell-final.adv)

Concept demonstrated: inharmonic FM bell via a √2 modulator ratio + feedback.

| # | Panel (A/B/C/D/Global) | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Operator | init | A pure sine on each note |
| 1 | Global | Algorithm | 1 (linear stack D→C→B→A) | (routing only — no change yet) |
| 2 | A | Wave / Coarse / Level | Sine / 1 / 0 dB | A pure sine carrier |
| 3 | A | Env A / D / S / R | 1 ms / 400 ms / −inf / 200 ms | A short sine pluck |
| 4 | B | On / Wave / Coarse / Fine | On / Sine / 1 / 414 (≈ ×1.414) | A bell-like inharmonic ring |
| 5 | B | Level | 80% | Stronger metallic shimmer |
| 6 | C | On / Coarse / Level / Feedback | On / 7 / 50% / 30% | A gritty high shimmer in the attack |
| 7 | Global | Spread / Filter (LP24 OSR ~8 kHz, Drive +3) | as listed | Stereo width + analog warmth |

Final check: a struck-bell pluck with metallic, detuned partials.
Analyzer: irregular (non-integer) partial spacing.
```

Rules: every row gives **panel · exact name · exact value · expected sound**; the patch is built
from this table, then `Save Preset` → `.adv`; the two ship side by side and must round-trip.

## Appendix B — Notes culture (how a FAIL is communicated)
- Specific, not vague: "the transition from the DX7 history to the math is abrupt — plant a
  signpost" beats "feels off."
- Motivating; critique the work, not the person.
- Model the fix (rewrite an example line) **or** propose one and let the owner choose.
- Persuade first; the Story Editor/Showrunner use final authority sparingly. Choose the hill to die on.

## Appendix C — Mapping to existing tooling
| Gate | Enforced by |
|---|---|
| 1 | Researcher agent + `source-map.json` |
| 2, 5 | Story Editor agent (rubric above) + Fresh-Ears on script |
| 3 | Ableton Expert + extended `clip_manifest.yaml` schema |
| 4 | Writer + lexicon linter (`validate.ts`) + demo↔script reconciliation |
| 6 | isolated Fact-Checker + `source-map.json` + narration audit |
| 7 | `verify_demo.py` (new) + preset round-trip (`build_tutorials.py`, new) |
| 8 | `sound_design_qa.py` (new, extends `alignment_report.py`) + `cuemap.json` |
| 9 | `build_episode.py` mastering + loudness assertion |
| 10 | isolated Fresh-Ears on final cut |
| 11 | Showrunner + `build_podcast_feed.py` |
