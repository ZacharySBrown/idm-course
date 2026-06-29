# Writer — Harness Contribution Report

Role: Gate 4 (in-voice prose + audio-choreography markers). Scope of my own work:
e03-wavetable, e04-meld, e05-warp-modes. e01-operator and e02-analog predate me — assessed as
inherited.

## 1. Readiness (Gate 4) per episode

- **e03-wavetable — READY (caveated).** 29 script files, 25 `[cue]`, 81 `[pause]`. Zero banned
  phrases, zero exclamations, zero emojis. All 25 cue ids resolve in `clip_manifest.yaml`. Build
  demos (05a–g) use name-then-show; perception/history cues (cold-open, 02x) frame-then-label.
  Caveat: parameter claims reconciled against demo specs by me, not yet re-confirmed by the
  Ableton Expert post-render.
- **e04-meld — READY (caveated).** 27 files, 20 cues, 74 pauses. Clean lexicon. All cues resolve.
  The "Two-Hands" build (05a–g) is strict one-decision-at-a-time name-then-show. Caveat: Meld is
  the least-documented device; bi-timbral/MPE behavior claims need an Expert pass before lock.
- **e05-warp-modes — READY (caveated).** 29 files, 24 cues, 82 pauses, 6973 words (longest). Clean
  lexicon, all cues resolve. The "one source, six warp modes" spine (05a–h) is the strongest
  frame→demo→label run I wrote. Caveat: warp artifacts (Complex Pro formant, Texture cloud) are
  subtle on phone speakers — flagged for Sound Designer at Gate 8, not a script defect.
- **e01-operator — INHERITED, NOT READY.** Lexicon clean, cues resolve, but two known
  script↔patch mismatches remain (see Concerns) plus the documented near-silent poly-bell renders.
  Script reads in-voice; the problem is reconciliation and audio, not prose.
- **e02-analog — INHERITED, READY (caveated).** 33 files, 28 cues, 120 pauses. Clean lexicon, cues
  resolve. Reconciled against the OSC-dumped Analog param map (commit c9c5bca). Caveat: not my
  authorship; I did not re-walk every setting-string.

Marker note: no `[bed:]` / `[demo-mute-bed]` markers appear in any episode (mine or inherited) —
the assembler interleaves narration-chunk → demo → chunk and silences the bed for the cue window
automatically, so bed-muting is infra, not a script marker, in this pipeline. The persona's
`[bed:]`/`[demo-mute-bed]` convention is unused here by design; I did not invent markers the
assembler ignores.

## 2. What I'm proud of

The e03 cold-open (`01-cold-open.md`). It opens on a contradiction (Wolfgang Palm sat down to
build a low-pass filter and *failed* — the harsh accident became the most-used synthesis method in
modern music), receipt-first (Depeche Mode, *See You*, 1982 — the bare pad before the drums), then
hands the listener the episode's whole thesis in six words they can hold: "Pitch and timbre,
separate dials. Walk the timbre." The cue lands on "Listen." with the label ("That choir is a PPG
Wave — not a sample of a choir, a row of single-cycle waveforms scanned one to the next") landing
immediately after, while the percept is still in working memory. Deflate-before-inflate is built
into the structure: the same gesture gets "three different verdicts on whether it was a flaw or
the point." No motivational kicker — it ends on "This is *Wavetable*." and stops.

## 3. What I actually did (evidenced)

- Wrote 85 script files across e03/e04/e05: 18,286 words, 69 `[cue]` markers, 237 `[pause]`
  markers, 392 em-dashes (the voice's house punctuation for asides).
- Placed frame→demo→label around every cue: perception/history cues get an attention line then the
  label after (e.g. e01 `05g` "Soft note first. Then hard." → cue → "That bite on the loud notes is
  velocity routed to modulator level"); build cues use name-then-show with the operative word
  adjacent to the cue (e.g. e03 `05b` "listen for the bloom" → cue → "Static at first, then
  morphing — that's a slow Position scan").
- Voice discipline verified by grep: **0** banned-lexicon hits, **0** exclamation points, **0**
  emojis across all five episodes' scripts.
- Every spoken setting-string sits inside a numbered build step ("Step two of seven…") tied to the
  demo's tutorial, not as an orphan recitation.
- Confirmed all 69 of my cue ids resolve to entries in each episode's `clip_manifest.yaml`
  (zero unresolved).

## 4. Concerns — scripts I want re-read before lock

- **e01 `06a-rhythmic-fm.md` — script↔patch mismatch (inherited, real).** My/the script line says
  "Set **B's** envelope to *Beat* mode … the modulator's envelope re-triggers every sixteenth."
  The shipped patch (`op-rhythmic-single` in the manifest) actually puts Beat on the **carrier's**
  amplitude: `Ae Mode: Beat` — "carrier AMPLITUDE pulses on the grid." So the narration attributes
  the rhythm to the wrong operator. Either the script must say "the carrier's amplitude envelope
  pulses on the grid" or the patch must move Beat to B. Reconcile with the Ableton Expert before
  Gate 5 lock.
- **e01 velocity (`05g`).** Script claims two audible things — velocity shortens the envelope
  (`Time<Vel +30`) *and* raises modulator level/brightness (`Level<Vel +50`). The manifest patch
  only sets `Osc-B Lev<Vel: 50`; the `Time<Vel` move is asserted in narration but I did not find it
  in the patch dump. Confirm the time-shortening is present and audible, or cut that clause.
- **e01 `bike-fm-perc` / Aphex bell cues.** The manifest itself flags that some source tracks have
  a beat throughout (the Aphex/Xtal note), which undercuts an "isolated bell/percussion" listening
  target. Background-only songs (Bike, Beep Street) were promoted to foreground cues in the script;
  per the e01 alignment memo, several of those renders were near-silent or never produced. The
  prose is fine; the audio under it needs the headless re-render before these cues earn lock.
- **e04 Meld claims generally.** Least-documented device of the five; I wrote to the demo specs,
  but the bi-timbral routing and MPE-per-engine claims deserve one explicit Expert confirmation
  pass before lock since I can't verify them by ear from spec alone.

Nothing in e03/e04/e05 has a lexicon hit or an unresolved cue. The hard stops all live in inherited
e01, and they are reconciliation/audio issues, not voice issues.
