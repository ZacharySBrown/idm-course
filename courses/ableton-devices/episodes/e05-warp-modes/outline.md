# Episode 5 — Warp Modes as Sound Design — Beat Sheet (Gate 2)

**Story Editor outline.** Structure locks here before any line-level or sound work.
Source dossier: `specs/ableton_course_ep5_warp_modes_research.md`. Voice enforced from
`shared/style/voice.md` + `shared/style/lexicon.md`.

> **Scope note (read first).** Warp is not a synth. Every demo in this episode is a *warped
> audio source* — "take source X, apply mode Y, push control Z to an extreme → you hear effect."
> The `warp_demos:` in `clip_manifest.yaml` are recipes (mode + key control + source description),
> not device-param dumps. They get rendered later by warping audio in Live, not by a synth render.

---

## Focus sentence

> Every Warp Mode is a real-time time-stretch algorithm, and every time-stretch algorithm has a
> characteristic failure mode — and the failure mode *is the sound*.

It is writeable in one line. It carries a driving question (*if Warp is just for matching tempo,
why are there six of them, and why does the manual admit even the best one is "never neutral"?*)
and a payoff (you don't pick a mode for transparency — you pick it for how it breaks: Beats into
glitch, Texture into clouds, Complex into ghosts, Re-Pitch into lo-fi grain). Gate 2
focus-sentence check: PASS.

## The driving question and the payoff

- **Question planted in the cold open:** the ambient wash you are hearing is a Justin Bieber song
  slowed down past recognition — and the same trick traces back to a 1946 physicist trying to save
  telephone bandwidth. Underneath: the thing you treat as invisible tempo-matching plumbing is
  actually six different DSP algorithms with 80 years of academic history. So why have you never
  turned the grain size up?
- **Payoff at the end:** the six modes are three DSP families — granular (Beats/Tones/Texture),
  phase vocoder (Complex/Complex Pro), varispeed (Re-Pitch) — answering one question: how do I make
  this longer/shorter without it falling apart? Each one's way of falling apart is a usable
  instrument. Gabor's grains, Xenakis's razor blade, Flanagan's phase vocoder, the lab in Paris, the
  Bieber meme — all collapse into one dropdown. The instrument is the decision about how you let the
  sound break.

## The arc (six acts, ~40 min)

1. **Cold open (90s)** — confession/contradiction: the ambient masterpiece that is a pop song you
   already own, broken on purpose, and an 80-year line that ends in a dropdown you ignore.
2. **History & theory (8–9 min)** — the two lineages: Gabor's quantum → Xenakis's tape → Roads/Truax
   real-time granular; and Flanagan's 1966 phase vocoder → GRM/CDP/SoundHack → élastique. Why a lab
   in Paris is now two clicks.
3. **The three DSP families (8–9 min)** — the physics, for a physicist: granular overlap-add, the
   phase vocoder and why it smears, the Flux paradox (randomness makes it *smoother*), formant
   preservation, varispeed and Nyquist.
4. **Ableton Warp deep-dive (8–9 min)** — the six modes specifically: the shared substrate (Warp
   Markers, transient detection), then Beats, Tones vs Texture, Re-Pitch, Complex/Complex Pro, and
   the abuse map.
5. **Sound-design walkthrough (5–6 min)** — one 2-second source, destroyed six ways, live, ending in
   the Hopkins resample loop.
6. **IDM application (5–6 min)** — Oval's damaged CDs, Akufen's microsampling, the Truax cloud, then
   the listener exercise: forty seconds of music from the same two seconds, broken six ways.

## Anecdote ⇄ reflection alternation (Ira Glass)

The two modes trade off; flagged per beat below. **A** = anecdote (events that raise→answer a
question). **R** = reflection (why am I still listening). Macro shape: each act opens on an anecdote
and lands on a reflection, so no act is a flat list. The history act is anecdote-heavy (Gabor,
Xenakis, Roads, Flanagan are *people doing things*); the DSP and device acts are reflection-heavy,
so each gets an anecdote anchor (the Bieber meme, Oval's knife) to break the lecture.

## The act-boundary signpost (the Ep1 lesson)

Ep1's table read showed sections blur without a planted "we are changing chapters now" line. Each
act here ends on an **explicit signpost sentence** that names the door we walk through. Those lines
are the conceptual homes of the inter-section **transitions** in `episode.yaml` (after `02e`,
`03e`, `04f`, `05h`). They are noted `>> SIGNPOST` below.

## Payoff refrain (seed early, land late — the Ep1 fix)

Seed the three-word refrain **"Pick the breakage."** in the cold open. It is the focus sentence made
sayable. Echo it once at each act boundary (the `>> SIGNPOST` lines carry it) and *land* it in `06d`
as the resolution, so the ending reads as a return, not a new thought.

---

## ACT 1 — Cold Open  ·  slide `01-cold-open`  ·  90s

- **A.** Open cold on ~12s of a Texture-warped vocal at high Flux — a smooth, de-pitched ambient
  wash (built for the episode; the "U Smile" cousin). Hold, fade under narration. Then the reveal:
  in 1946 a physicist named Dennis Gabor — later a Nobel laureate, for holography — proposed every
  sound could be chopped into grains, quanta of time and frequency. He was trying to save telephone
  bandwidth. He had no idea he'd written the theory behind a Justin Bieber song slowed so far it
  became ambient music. Xenakis built Gabor's grains by hand with a razor blade in 1959; in the '80s
  you needed a lab in Paris to do it well; today it is two clicks in a dropdown you ignore because
  you think it is for matching tempos.
- **Demo home:** `cold-open-texture-wash` — the cold-open bed itself (Texture, small grain, Flux
  ~90, extreme stretch on a vocal).
- **R.** The contradiction stated plainly: every one of those six little modes is a different way of
  breaking a sound on purpose, and by the end of the walk you will not call it "tempo-matching."
- **Callback hook to prior episodes:** Operator *generated* a spectrum from almost nothing; Analog
  *carved* a rich one down. Warp takes a finished recording and *breaks* it — a third verb.
- **Payoff-refrain seed:** plant **"Pick the breakage."** here.
- **>> SIGNPOST into Act 2:** "Four stops: where this came from, the physics of how it breaks, the
  six modes in the dropdown, and how to destroy two seconds of audio six different ways." (Cold-open
  MAP — give the act structure up front so every later seam reads as 'next stop,' not 'non
  sequitur.')

## ACT 2 — History & Theory  ·  slides `02a`–`02e`  ·  8–9 min

Ordered by "what do I need next for this to make sense?": the grain as an object → the grain as
composition → the grain going digital then real-time → the *other* family (frequency domain) → the
labs that owned it, and how it got democratized.

- **`02a-gabor-quantum` — Gabor's acoustic quantum (A→R, 90s).** 1946, *Theory of Communication*;
  the acoustic quantum; bounded by time-frequency uncertainty (the audio Heisenberg); motivation was
  bandwidth, not music. *Physicist hook:* a grain is a windowed sinusoid — a Gabor atom — and a
  wavelet/STFT frame is built from exactly these. You already know this object. *Anecdote opens,
  reflection lands.*
- **`02b-xenakis-razor` — Xenakis and the razor blade (A, 120s).** "All sound is an integration of
  grains." *Analogique A-B* (1959): tape splicing as the first granular synthesis — cut sound into
  tiny pieces and re-schedule them. *This is literally what Beats mode does.* Anchor the abstraction
  to a man with a razor blade. *Anecdote beat.*
- **`02c-roads-truax` — Digital, then real-time (A, 90s).** Roads, 1975, weeks to render a minute of
  mono (*Microsound*, the canonical citation); Truax's DMX-1000, the first real-time granular system,
  *Riverrun* (1986). The 40-year line — Gabor → Xenakis → Roads → Truax — ends at a held loop in
  Live. *Anecdote beat; plant "the DAW is the last station on the line."*
- **`02d-phase-vocoder` — The other family: the phase vocoder (A→R, 120s).** Flanagan & Golden, Bell
  Labs, 1966 (*BSTJ*); Portnoff's FFT (1976); Dolson's tutorial. Analyze into STFT frames, stretch by
  re-spacing frames, then *fix the phase* — the hard part, and the source of its artifacts. "This is
  the Complex modes. Different math, different breakage." *Sets up §3.2.*
- **`02e-democratization` — The lab era and the dropdown (R, 90s).** GRM (Paris), CDP/Wishart,
  SoundHack/Erbe — spectral processing you needed an institution for, offline and expensive. All of
  it now in the Warp dropdown; élastique (zplane) is the modern *transparent* endpoint inside Complex
  Pro. *Reflection peak: the same 60-year math is sold as "transparency," and its artifacts are the
  whole point of the aesthetic.* Caveat inline: élastique-in-Complex-Pro is [CONFIRMED] via zplane
  and industry reporting, but the manual does not name the vendor — say so.
  - **>> SIGNPOST into Act 3:** "That is the history. Now the physics — because for a physicist, the
    artifact is not a flaw, it is the math becoming audible." (Transition clip after `02e`.)

## ACT 3 — The Three DSP Families  ·  slides `03a`–`03e`  ·  8–9 min

Ordered: the granular mechanism → the phase-vocoder mechanism and why it smears → the Flux paradox
→ formant decoupling → varispeed and aliasing. Reflection-heavy act; each beat carries a live demo
so the math is *heard*, not lectured.

- **`03a-granular-math` — Granular, in one breath (R, 90s).** Tile the output with overlapping
  windowed grains, overlap-add; read rate decoupled from write rate; slow down = repeat material,
  speed up = omit it (the manual's "repeating or omitting segments"). Grain size vs signal sets the
  character. *Live demo: Texture at 400%, drag Grain Size — hear the grain rate move; "that buzz is
  the seam between grains."*
  - **Demo home:** `granular-seam-grainsize` (§5.7-1).
- **`03b-phase-vocoder-smear` — Phase vocoder, for the physicist (R, 120s).** STFT $X(k,m)$,
  re-space synthesis frames, re-derive each bin's phase from the unwrapped phase difference. Two
  failure modes: transient smearing (sines have no time localization → the click softens to a
  "thwip") and "phasiness"/reverberant smear (horizontal phase continuity without vertical coherence
  → watery, hollow ghost). *Drop the Bernsee quote.* "That haunted sound isn't a preset; it's the
  algorithm failing to keep phase." *A/B demo: a break at 50% in Beats vs Complex.*
  - **Demo home:** `transient-survival-ab` (§5.7-3).
- **`03c-flux-paradox` — The Flux paradox (A→R, 120s).** Counterintuition: adding randomness makes
  it *smoother*, not noisier. PaulStretch randomizes STFT phase → no repeating buzz → smooth cloud;
  Texture's Flux is the granular-domain version. Anchor with the "U Smile 800%" meme (Shamantis,
  PaulStretch by Paul Nasca, 2010; Jace Clayton sped it back up to prove the source was unchanged).
  *Live demo: Flux 0 → 100 on a held note; the periodic buzz dissolves into a wash.* Caveat inline:
  Flux ≡ STFT-phase-randomization is a well-supported *inference*, not Ableton-confirmed — flag it.
  - **Demo home:** `flux-smooths-buzz` (§5.7-2).
- **`03d-formants` — Formant decoupling (R, 90s).** Excitation (glottal pulse → pitch) vs vocal-tract
  resonances (formants → vowel/body). Naive pitch-shift moves both → chipmunk. Formant-preserving
  transpose estimates the spectral envelope, divides it out, shifts the fine structure, re-applies
  the envelope. That is Complex Pro's Formants control. *Live demo: Complex Pro, +12, Formants
  100% ↔ 0% — human-up vs chipmunk.*
  - **Demo home:** `formant-decouple-ab` (§5.7-4).
- **`03e-varispeed-nyquist` — Varispeed and Nyquist (R, 90s).** Re-Pitch does not stretch — it
  resamples. Rate $r$ multiplies every frequency, divides duration (the turntable law). Speed up →
  partials cross Nyquist → aliasing fizz; slow down → dark, imaging, no aliasing. "The one honest
  mode: the only artifact is sampling theory." *Live demo: bright cymbals at 2×, hear the fold-back
  fizz.* Caveat inline: Live's resampler quality is unpublished — phrase as "the artifact of
  sample-rate conversion," not a measured spec.
  - **Demo home:** `aliasing-on-speedup` (§5.7-5).
  - **>> SIGNPOST into Act 4:** "Three families, one menu. Now open the dropdown and meet all six —
    starting with the analysis that happens before any of them run." (Transition clip after `03e`.)

## ACT 4 — Ableton Warp Deep-Dive  ·  slides `04a`–`04f`  ·  8–9 min

**Section driving question (the Ep1 device-tour fix — plant at `04a` so the tour is not a feature
list).** Ableton put three unrelated DSP families behind one dropdown and the manual admits even the
best one is "never neutral." So: *what runs before any mode does, which mode breaks which way, and
which control is the one that does the breaking?* Every beat is an answer: `04a` = the shared
substrate; `04b`–`04e` = the modes, one breakage each; `04f` = the abuse map that indexes them.
Surface the framing at the top of `04a` and re-touch it opening each beat. Ordered: the analysis
that precedes everything → the glitch engine → the granular twins → the purist → the spectral ghosts
→ the index.

- **`04a-substrate` — Warp Markers and transient detection (R, 60s).** Live analyzes the file,
  finds transients (amplitude peaks), drops gray Transient Markers; pseudo-warp markers promote to
  yellow Warp Markers. The sound-design lever: transient detection *is* the segmentation Beats loops
  between, so deliberately mis-placing markers tells the engine to cut in the wrong place. The
  manual's framing, verbatim: Complex modes use "an entirely different technology"; even the best is
  "never neutral — not even at the original tempo." *Warping is always an effect.*
- **`04b-beats-glitch` — Beats: the glitch engine (A, 120s).** Transient-locked granular; grain
  boundaries anchor to transients, so transients survive a stretch. Controls: **Preserve**,
  **Transient Loop Mode**, **Transient Envelope**. *Live demo: Loop Forward + Envelope 100 at
  half-tempo = the stutter/freeze.* Mis-grid Preserve = manufactured glitch. *Anecdote anchor: this
  is Oval's CD-skip, automated.*
  - **Demo home:** `beats-stutter-freeze` (the recipe from §4-Ref1).
- **`04c-tones-texture` — Tones vs Texture: the granular twins (A→R, 120s).** Tones tracks pitch
  (signal-dependent; Grain Size is a *suggestion* it overrides). Texture ignores the signal
  (signal-blind) and hands you a real **Grain Size** knob plus **Flux**. "Texture is the hero
  mangler — a granular cloud generator hiding in a clip." *Live demo: same source in Tones (warbles,
  hunting a pitch) vs Texture (de-pitched cloud).*
  - **Demo homes:** `tones-warble` and `texture-cloud`.
- **`04d-repitch-purist` — Re-Pitch: the purist (R, 90s).** No parameters, no time-stretch, transpose
  *disabled* — pitch only moves with tempo (varispeed). Lo-fi grain and aliasing are the only
  character. The honest mode: SP-1200/Akai key-shift, tape varispeed, the pitched-up Amen.
  - **Demo home:** `repitch-halfspeed` (the §4-Ref5 recipe).
- **`04e-complex-ghosts` — Complex & Complex Pro: the spectral ghosts (A, 120s).** Phase vocoder;
  Complex Pro is élastique (per zplane/industry, not the manual). For whole songs and pads; the
  smear is the sound. **Formants** (preserve/destroy, not a free shifter — flag) and **Envelope**
  (default 128). "Same 1966 math sold as 'transparency' — turn it off and you're back in Wishart's
  CDP." *Live demo: vocal +12, Formants 0% (goblin) ↔ −7, Formants 0% (giant).*
  - **Demo home:** `complexpro-formant-monster` (the §4-Ref6 recipe).
- **`04f-abuse-map` — The abuse map (R, 60s).** One slide: each mode's transparency lever vs its
  sound-design lever (Section 1.7 table). The index the listener keeps. *Reflection: every row is the
  same sentence — "transparent here, instrument there."*
  - **>> SIGNPOST into Act 5:** "Enough touring the dropdown. Take two seconds of one sound and
    destroy it six ways without leaving the clip." (Transition clip after `04f`.)

## ACT 5 — Sound-Design Walkthrough  ·  slides `05a`–`05h`  ·  5–6 min

A single arc: one 2-second source (a sung "ah" or a field recording), run through every mode live,
narrating each. Each step is an anecdote (a move that raises and answers "what just happened to the
sound"). Lands on the Hopkins resample loop and a saved instrument.

- **`05a-the-source` (A, 30s).** Establish the dry 2-second source so every destruction has a
  reference. "Two seconds of a voice. No plugins. Just the dropdown." Demo `walk-source-dry`.
- **`05b-beats-stutter` (A, 45s).** Beats, Preserve 1/16, Loop Forward, Envelope 100, half-tempo →
  stutter-glitch. Demo `walk-beats-stutter`.
- **`05c-tones-warble` (A, 45s).** Tones, stretch 300%, large Grain Size → brittle jungle-vocal
  warble. Demo `walk-tones-warble`.
- **`05d-texture-cloud` (A, 60s).** Texture, 800%, mid Grain Size, Flux ~60 → ambient granular cloud
  (the "U Smile" move). Demo `walk-texture-cloud`.
- **`05e-repitch-tape` (A, 45s).** Re-Pitch, 50% → dark lo-fi; 200% → chipmunk + aliasing. Demo
  `walk-repitch-tape`.
- **`05f-complexpro-formant` (A, 60s).** Complex Pro, +12 Formants 0% (goblin), −7 Formants 0%
  (giant), Envelope tweaks. Demo `walk-complexpro-formant`.
- **`05g-resample-loop` (A→R, 60s).** Resample the Texture cloud, re-warp it in Complex Pro, resample
  again — the Jon Hopkins destructive loop (commit-and-mangle, hunt artifacts; [CONFIRMED ethos,
  paraphrase — verify exact wording before quoting]). "Three passes and the source is gone. That's
  the method." Demo `walk-resample-pass3`.
- **`05h-save-instrument` (R, 30s).** Save the cloud as an instrument. "You started with two seconds
  of a voice and built six instruments out of how it breaks."
  - **>> SIGNPOST into Act 6:** "Six instruments from two seconds. Now where this lives in actual
    records — and the homework for the walk home." (Transition clip after `05h`.)

## ACT 6 — IDM Application & Exercise  ·  slides `06a`–`06d`  ·  5–6 min

Ordered: glitch-from-order (Oval) → microsampling (Akufen) → the cloud (Roads/Truax) → the
exercise. Closes on the exercise, then a stop (voice rule — no kicker).

- **`06a-oval-glitch` — Glitch from order: Oval (A, 90s).** Markus Popp scratched CDs, drew on them
  with markers, taped them to force skips — "playback malfunctions into deliberate musical elements"
  (*Systemisch*, 1994). The error is the instrument — the stance this whole episode teaches. The
  in-the-box version: Beats with wrong-grid Preserve + Loop modes. "Popp scratched CDs with a knife;
  you have a dropdown." Caveat inline: Björk-sampled-Oval and "influenced Autechre" are secondary —
  flag.
  - **Demo homes:** `systemisch-clip` (the record, for the A/B) and `oval-beats-glitch` (the rebuild).
- **`06b-akufen-microsample` — Microsampling: Akufen (A, 90s).** *My Way* (2002): sub-second FM-radio
  micro-samples reassembled like a collage (Ableton's own artist interview confirms). The microsample
  is a grain you cut by hand; Beats Preserve + Transient Loop is the automated descendant.
  "Transient placement is composition."
  - **Demo homes:** `akufen-clip` (the reference) and `akufen-microslice` (transient-placement
    rebuild).
- **`06c-truax-cloud` — The cloud: Roads/Truax (R, 60s).** Texture at high Flux *is* a real-time
  granular cloud — the thing Truax needed a DMX-1000 for in 1986, now in a clip. Resample it and you
  have an original instrument. *Closes the history loop opened in 02c.*
  - **Demo home:** `truax-texture-cloud` (the §4-Ref7 recipe).
- **`06d-exercise` — Listener exercise (R, 90s).** Homework for the walk home: pick the most boring
  two seconds you have — a vocal "ah," a snare, a chord. No plugins. Just warp it. Texture + Flux up
  until the pitch dissolves; Beats + Loop-Forward into a stutter; Complex Pro until it's a goblin.
  Make forty seconds of music where every sound is the same two seconds, broken six ways. If you can,
  you understood that warping was never about tempo: Gabor's grains, Xenakis's razor blade,
  Flanagan's phase vocoder, the lab in Paris, the Bieber meme — they collapse into one dropdown, and
  the whole instrument is the decision about how you let the sound fall apart. *Land the refrain:*
  "Pick the breakage." Then stop talking (no kicker). Outro: the Texture cloud, Flux slowly to zero
  so a recognizable source re-emerges (the Jace-Clayton "speed it back up" reveal), fade to silence.

---

## Gate 2 rubric — self-check

- [x] One-line **focus sentence** is writeable (above).
- [x] The piece has an **arc**: driving question (why six modes, and why "never neutral"?) +
      surprising payoff (you pick a mode for *how it breaks*; six modes are three DSP families
      answering one question).
- [x] **Anecdote** beats alternate with **reflection** beats (tagged A/R per beat; history act is
      anecdote-driven, DSP/device acts are reflection with anecdote anchors — the Bieber meme,
      Oval's knife — so no act flatlines).
- [x] **Signposts** planted at every act boundary (`>> SIGNPOST`, mapped to transition clips after
      `02e`, `03e`, `04f`, `05h`), plus the cold-open four-stop map and the seeded refrain.
- [x] Concept blocks ordered by "what do I need next for this to make sense?" — grain → composition
      → digital/real-time → the other family → democratization; then granular → phase vocoder → Flux
      → formants → varispeed; then substrate → Beats → Tones/Texture → Re-Pitch → Complex → abuse
      map.
- [x] Each demo has a **conceptual home** in a block (noted inline; bare-word ids = song clips,
      `walk-`/`*-cloud`/`*-glitch` etc. = warp-render recipes, all resolved in `clip_manifest.yaml`
      after lock).

**Gate 2: PASS.** Cleared to scripting. This is not a flatline list — do not advance line-level work
past one.

## Voice/lexicon flags for the Writer (enforce at draft)

- Cold-open is a **contradiction** (a pop song that became ambient art; a lab tool that became a
  dropdown), not a welcome.
- Close is the **exercise then a stop**, no motivational kicker. Hold the line.
- Keep caveats **inline** where they live: élastique-in-Complex-Pro (zplane/industry, *not* the
  manual); Flux ≡ phase-randomization (well-supported inference, not Ableton-confirmed); Re-Pitch
  aliasing (sampling theory, Live's resampler quality unpublished); Hopkins mode preferences
  (community/secondary, not a direct quote); Burial (CONFIRMED aesthetic, tooling UNVERIFIED — never
  claim his sound is Live's warp engine); Björk-sampled-Oval and Oval→Autechre (secondary). These are
  dossier flags; do not bury them.
- **Never** assert a specific commercial record "was made with Texture/Complex" unless the artist
  said so. Warp-as-sound-design is documented at the *technique* level, not per-track DSP.
- **Banned (hard fail):** journey / sonic journey, unleash, level up, game-changing, mind-blowing,
  magic happens, sonic landscape, secret sauce, pro tips, synergy, AI-powered/-enhanced, unlock the
  power of, deep dive (noun), next-level, truly unique, really really / very very. Zero exclamation
  points, zero emojis.
