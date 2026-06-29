# Episode 4 — Meld: The Bi-Timbral Macro-Oscillator Synth — Beat Sheet (Gate 2)

**Story Editor outline.** Structure locks here before any line-level or sound work.
Source dossier: `specs/ableton_course_ep4_meld_research.md`. Voice enforced from
`shared/style/voice.md` + `shared/style/lexicon.md`. Slide ids mirror `episode.yaml`.

---

## Focus sentence

> Operator builds a spectrum and Wavetable scans one, but Meld hands you twenty-five ready-made
> worlds — two knobs each — lets you run two of them at once, and routes your fingers into them:
> so you don't engineer a sound here, you pick one and play it.

It is writeable in one line, it carries a driving question (*if this synth gives you almost
nothing to edit — two knobs per oscillator — where did all the control go, and why is the most
important part of Meld not an oscillator at all?*), and it has a payoff (the control didn't
vanish; it moved out of the patch and into the performance — the matrix and MPE are the
instrument, and every held note can be a different sound under a different finger; and the
"physical-modelling synth" on the box is a myth that resolves to two resonator *filters*). Gate 2
focus-sentence check: PASS.

## The driving question and the payoff

- **Question planted in the cold open:** one oscillator in this synth sounds like it's rising
  forever and never arrives; another sounds like actual rain; a third sounds like loading a
  cassette game in 1984 — and you reach any of them with one knob. So if Meld gives you almost no
  surface to edit, where did the control go, and why is the headline of this synth not an
  oscillator at all?
- **Payoff at the end:** the control didn't disappear — it moved out of the patch and into the
  *performance*. You pick one of 24+1 finished algorithms (each behind two macros), run two full
  engines at once, snap them to your scale, and route your fingers — per-note pressure, slide, and
  bend over MPE — straight into the timbre. The capstone reframe for the physicist: Operator
  generates spectra, Wavetable interpolates between them, Meld parameterizes whole algorithms
  behind two macros and lets ten fingers drive them. And the two myths planted in the cold open
  get logged on the way out: Meld is **not** a physical modeller (only the modal Plate/Membrane
  resonator *filters* are, and they're a filter, not the oscillator), and it did **not** arrive in
  a point update — it shipped the day Live 12 did, 5 March 2024.

## The arc (six acts, ~40 min)

1. **Cold open (90s)** — confession/contradiction: three impossible-sounding oscillators in one
   box, both myths the host got wrong, and the reframe — you don't build the sound here, you pick
   it and play it.
2. **History & theory (8–9 min)** — what a macro-oscillator IS → the Mutable Instruments Plaits
   lineage (acknowledged influence, not code-reuse) → MPE: a channel per finger → where Meld sits
   in the four-synth map.
3. **Synthesis deep-dive (8–9 min)** — the oscillator families (hear one knob cross worlds),
   FM-the-macro-way (Ep1 callback), the one true physical-modelling element (modal resonators —
   myth payoff), scale-aware oscillators, audio-rate LFOs + loop envelopes.
4. **Device deep-dive (8–9 min)** — Ableton Meld specifically: bi-timbral = two summed engines,
   the two macros + the matrix ("the macro is the new Position"), MPE hands-on, filters/mixer/
   global/voicing, and when to reach for it vs the family.
5. **Patch walkthrough (5–6 min)** — build "Two-Hands": one bi-timbral, MPE-played texture-lead
   that proves "two synths, one note, ten fingers."
6. **IDM application (5–6 min)** — self-sequencing timbre (the Autechre idea), environmental
   oscillators as composition, the Shepard trick (cold-open callback), the two myths logged, then
   the exercise.

## Anecdote ⇄ reflection alternation (Ira Glass)

The two modes must trade off; flagged per beat below. **A** = anecdote (events that raise→answer
a question). **R** = reflection (why am I still listening). Macro shape: each act opens on an
anecdote and lands on a reflection, so no act is a flat list. The ep1 Section-4 flatline failure
was a run of device-tour beats with no question pulling one into the next — guarded against in
Act 4 with an explicit driving question. The two myth-busts (physical-modelling, the version
number) are planted as **anecdote** beats, not footnotes.

**Honesty constraint for this episode (dossier Section 3).** Meld is a 2024 instrument with **no
canon of famous records**. **No artist/track may be claimed to use Meld.** Every artist beat is
**aesthetic kinship or technique illustration only** — Aphex (per-note timbre / Iridium collab,
AFX Mode), Autechre (self-sequencing-timbre aesthetic), Squarepusher (honest negative — builds
his own tools), Plaid/BoC (texture targets, not Meld gear). Flagged at the structural level so the
Writer never builds a beat on a false attribution — it would fail Integrity in the editor's
hierarchy.

## The act-boundary signpost (the Ep1 lesson)

Ep1's table read showed sections can blur without a planted "we are changing chapters now" line.
Each act here ends on an **explicit signpost sentence** that names the door we are walking
through. Those signpost lines are the conceptual homes of the inter-section **transitions** in
`episode.yaml` (after `02d-where-meld-sits`, `03e-lfo-loop-env`, `04e-when-to-reach`, `05g-save`,
`06c-shepard-trick`). They are noted as `>> SIGNPOST` below.

## The payoff refrain

Three beats, made sayable: **"You don't build the sound. You pick it — and then you play it."**
Seed it in the cold open, echo it once at each act boundary (the `>> SIGNPOST` lines carry it),
and *land* it in `06e` as resolution — so the ending reads as a return, not a new thought. This is
the Ep1 fix: seed the payoff line early so it pays off late. A second, smaller refrain carries the
myth-bust: **"It's a filter, not the oscillator."** — planted at the resonator beat (`03c`),
echoed at the patch step that uses it (`05b`), landed in `06d`/`06e`.

---

## ACT 1 — Cold Open  ·  slide `01-cold-open`  ·  90s

- **A.** Open on a Meld **Shepard's Pi** patch alone — a barberpole tone that sounds like it's
  rising forever and never arrives, a staircase with no top, held ~8s under the narration. Then
  name the strangeness concretely: there's another oscillator in this same synth that sounds like
  actual rain; a third that sounds like loading a cassette game in 1984. They all live in the same
  box, and you reach any of them with one knob.
- **Demo home:** `shepard-pi-cold-open` — ~8s of the Shepard's Pi endless-rising tone, held alone
  under the open then ducked as narration enters (the dossier's named cold-open candidate).
- **R.** The reframe stated plainly: the last three episodes we *built* sounds — generated a
  spectrum with FM in Operator, scanned one in Wavetable, subtracted one in Analog. This episode is
  different. We don't engineer a sound — we **pick** one, from twenty-five ready-made worlds, two
  at a time, and play it with our fingers. Meld was built for ten fingers, not one.
- **Two myths, planted as confessions (the dossier's two corrections — air them up front so no
  later beat builds on the wrong frame).** "Two things the box gets wrong, and I did too: it calls
  Meld a physical-modelling hybrid — it mostly isn't, and we'll show you the one filter where that's
  true. And it did not arrive in a point-update — it shipped the day Live 12 did, March 2024." Both
  pay off later (`03c` and `02d`/`06d`).
- **Payoff-refrain seed:** plant **"You don't build the sound. You pick it — and then you play
  it."** here. Echo it at each act boundary (the `>> SIGNPOST` lines carry it) and *land* it in
  `06e`.
- **>> SIGNPOST into Act 2:** "Four stops: where this idea came from, how it actually works, the
  one Ableton device built around it, and how to make IDM with two synths and ten fingers." (The
  cold-open MAP — the Ep1 lesson's highest-leverage anti-"jumpy" fix: give the act structure up
  front so every later seam reads as 'next stop,' not 'non sequitur.')

## ACT 2 — History & Theory  ·  slides `02a`–`02d`  ·  8–9 min

Ordered by "what do I need next for this to make sense?": what the *thing* is (macro-oscillator)
→ where it came from (Plaits) → the paradigm that makes Meld matter (MPE) → where it lands among
Live's synths.

- **`02a-what-a-macro-osc-is` — What a macro-oscillator IS (R→A, 90s). ACT OPEN — signpost: "Stop
  one — where this idea came from."** A single oscillator slot that hides an entire complex DSP
  algorithm behind a small, fixed set of high-level controls — in Meld, exactly two macros, whose
  meaning changes per type. The explicit tradeoff: you lose fine editability, you gain instant
  breadth and playability. *"You don't build the sound, you pick it."* Hear it immediately so the
  definition lands as a sound, not a sentence.
  - **Demo home:** `meld-one-knob-three-worlds` — Engine A, one held note, one knob crossing three
    worlds (Basic Shapes → Harmonic FM → Rain). The episode's thesis, audible in the first 90s.
- **`02b-plaits-lineage` — The Plaits lineage (A, 150s).** Émilie Gillet / Mutable Instruments:
  Braids (2013) → Plaits (2018), a Eurorack "macro oscillator" with 16 models, open-source MIT DSP
  that propagated everywhere (Behringer Brains, Arturia MicroFreak, VCV Rack). **Drop Rob Tubb's
  quote:** *"The sheer adaptability and multi-function stuff that modules can do, that was a big
  influence."* **Myth-bust gently, in place:** Meld is *lineage*, not "Plaits code inside" — say
  "lineage," never "contains." Seed the physical-modelling thread: Plaits genuinely has
  Karplus-Strong + modal models; Meld inherited only the *modal resonator*, and only as a filter
  (paid off in `03c`). *Anecdote — the origin story; a name, a date, a quote.*
  - **Demo home:** `plaits-module-ref` — a short Plaits patch as the lineage reference (a module,
    not Meld — labelled as such).
- **`02c-mpe-paradigm` — MPE: a channel per finger (R→A, 120s).** MIDI Polyphonic Expression
  (MMA-adopted 2018): each note gets its own channel, so pitch bend, a Y-axis Slide (CC74), and
  per-note pressure are independent for every finger — impossible in legacy MIDI. The hardware:
  ROLI Seaboard, LinnStrument, Push 3 in MPE mode. **The reflection that makes it matter:** MPE
  turns the performance gesture into a per-voice modulation source — *"the patch and the
  performance stop being separate things."* The IDM kinship (flagged honestly): Aphex's per-note
  obsession — the Waldorf Iridium per-note parameter-lock collaboration, the Bass Station II "AFX
  Mode" — is the *idea* MPE serves, **framed as kinship, not Meld credit.**
- **`02d-where-meld-sits` — Where Meld sits: pick-and-play (R, 90s).** The four-instrument map made
  clean: Operator **generates** (FM, Ep1), Wavetable **scans** (Ep3), Analog **subtracts**, Meld
  **picks-and-plays**. Suite, March 2024 (version myth busted here: 12.0, not 12.1; the Chord
  oscillator is the only post-launch addition, 12.2; user is on 12.4). Christian Kleine + Rob Tubb;
  Kleine: *"It's two synthesizers in one … the sum bigger than its parts."* Lands the act on the
  map, not a cheer. Echo the refrain.
  - **>> SIGNPOST into Act 3:** "We said each of those worlds is a whole algorithm behind two
    knobs. Stop two — what's actually behind the knobs." (Transition clip after `02d`.)

## ACT 3 — Synthesis Deep-Dive  ·  slides `03a`–`03e`  ·  8–9 min

Ordered: the families it spans (hear them) → FM as a special case the physicist already knows (Ep1
callback) → the ONE physical-modelling element (myth payoff) → scale-awareness → audio-rate
modulation + loop envelopes that set up the IDM act.

- **`03a-the-osc-families` — The 25 oscillators, by family (A, 120s). ACT OPEN — signpost: "Stop
  two — how it actually works."** Each type is a parameterized DSP routine with a deliberately
  reduced surface; the two macros map per-type onto the few internal parameters that matter
  (Harmonic FM: index + ratio; Square Sync: the two oscillator frequencies). The families:
  virtual-analog, FM, swarm (supersaw-style), buffer-loop "granular-esque" (caveat: not a true
  granular cloud), noise/environmental (Rain/Bubble/Crackle — synthesized, not sampled),
  lo-fi/chiptune, special (Shepard's Pi, Tarp). **The single most important demo: hold one note,
  change the oscillator type live.** *"Same note. Three instruments."* *Anecdote — a move that
  raises and answers "how far does one knob reach?"*
  - **Demo home:** `meld-type-switch-live` — Engine A, one held note, sweep Macro 1 on Basic
    Shapes, then switch the *type* live (Harmonic FM → Swarm Saw → Rain). Isolates "two knobs,
    whole new instrument."
- **`03b-fm-the-macro-way` — FM, the macro way (R, 90s). The explicit Ep1 callback.** Harmonic FM
  = index (Amount) + ratio; FM Bass (Squelch) exposes **operator feedback** — the one place Meld
  surfaces FM feedback. *"Last episode it took a whole algorithm grid; here it's two knobs — same
  Bessel sidebands underneath."* Self-modulation as feedback: sine → saw → noise edge as feedback
  rises — the Operator-episode physics, collapsed. *Reflection — ties Meld back to the course.*
  - **Demo home:** `meld-squelch-feedback` — FM Bass (Squelch), raise the Feedback macro on a held
    note; sine → saw → noise edge. The Ep1 callback in one knob.
- **`03c-modal-resonators` — The modal resonators: the ONE physical-modelling part (R→A, 90s). The
  myth payoff.** Plate Resonator and Membrane Resonator are modal-resonator *filters* — they
  impose the natural modes of a plate or a drum membrane onto whatever the oscillator feeds them,
  scale-aware so the modes snap into tune. **The punchline:** *"This — and only this — is the
  'physical modelling' on the box. And it's a filter, not the oscillator. Correction logged."*
  Plant the **"It's a filter, not the oscillator."** refrain here. *Anecdote-tinted reflection —
  the promised myth-bust, made audible.*
  - **Demo home:** `meld-plate-resonator` — any bright oscillator → Plate Resonator filter,
    scale-aware on; a pluck-like, body-resonant tone. The "physical" hook, isolated.
- **`03d-scale-aware` — Scale-aware oscillators, six of them (A, 90s).** Six oscillator types (the
  four swarms, Chip, Dual Basic Shapes) snap their otherwise inharmonic partials to the Live Scale
  — Kleine: *"a must-have for any modern synth."* Raise the spread; hold a chord; toggle the scale
  and hear the partials snap in key. *Anecdote — a move with a clear before/after.*
  - **Demo home:** `meld-swarm-scale-snap` — Swarm Sine (scale-aware), raise Spacing, hold a chord,
    toggle the Live Scale; the spread snaps into key.
- **`03e-lfo-loop-env` — LFOs into audio rate + loop envelopes (R, 90s).** The modulation side that
  sets up Act 6: LFO rate reaches ~200 Hz — audio-rate, a back-door FM/AM; LFO 1 and LFO 1 FX are
  two independent sources; a Mod Env in **AD Loop** routed to a macro is a self-cycling timbral
  sequencer on one held note. *Reflection — the seam into the device and the IDM act.*
  - **Demo home:** `meld-modenv-loop-macro` — one held note, Mod Env AD-Loop → a macro; the timbre
    sequences itself (re-used conceptually in `06a`).
  - **>> SIGNPOST into Act 4:** "That's the physics behind the knobs. Now the one device that wraps
    two of those engines into a box and points your fingers at them." (Transition clip after `03e`.)

## ACT 4 — Device Deep-Dive (Ableton Meld)  ·  slides `04a`–`04e`  ·  8–9 min

**Section driving question (the explicit Ep1 fix — plant it at `04a` so the tour is not a feature
list).** Ep1's table read failed here: device-tour beats joined by "and also," no question pulling
one into the next. This act answers one live question end to end: *"Meld gives you almost nothing
to edit — two knobs per oscillator. So where did the control GO, what is the actual heart of the
instrument, and what does bi-timbral + MPE let it do that no other Live synth can?"* Every beat is
an answer: `04a` = two full engines, summed (and the cross-mod caveat); `04b` = the macros are
first-class matrix targets ("the macro is the new Position"); `04c` = MPE is where the control
went (the answer); `04d` = filters/mixer/global serve the two engines; `04e` = when to reach for
it / when NOT to. Surface the framing at `04a` and re-touch it opening each beat.

- **`04a-bi-timbral` — Bi-timbral: two full engines, summed (A, 90s). ACT OPEN — plant the driving
  question.** Each engine is a complete voice: oscillator + filter + two envelopes + two LFOs + its
  own matrix. Unlike Wavetable (two osc, one amp/filter) or Operator (four operators, one voice),
  each Meld engine is a *full* voice. **Get the caveat right on air:** the two engines **sum** their
  outputs — they do **not** audio-rate cross-modulate (one engine's oscillator does not FM the
  other's); cross-engine routing is control-rate (A's LFO can modulate B's parameter). *Anecdote-
  framed: "two synths, one note, one box."*
- **`04b-macros-and-matrix` — The two macros + the matrix, the heart (A, 120s).** The two
  oscillator macros are first-class matrix *targets* — *"the macro is the new Position"* (the Ep3
  callback). ~23 targets; sources = LFOs, LFO FX, envelopes, MIDI, MPE, and **the other engine**;
  bipolar amounts. **Demo: route LFO 1 → Macro 1** and hear the timbre breathe without touching
  pitch. *Anecdote — a routing that raises and answers "what does modulating a macro do?"*
  - **Demo home:** `meld-lfo-to-macro` — tweak a macro so it enters the matrix, assign LFO 1 →
    Macro 1, slow; the held note's timbre morphs, pitch unchanged.
- **`04c-mpe-hands-on` — MPE, hands-on: a finger's signal path (A→R, 120s). Answers the act's
  driving question — this is where the control went.** The MPE tab exposes per-note Pitch Bend,
  Slide (Y/CC74), and Press as matrix sources; the matrix runs **per-voice**, so the same patch
  makes different timbres on simultaneously held notes. **Demo: Press → a macro, Slide → filter**,
  each finger morphs its own note (fallback for non-MPE listeners: Press → channel aftertouch,
  still works, less granular). *"This is what the whole thing was built for."* The reflection that
  lands the act's question.
  - **Demo home:** `meld-mpe-per-note` — MPE controller (or aftertouch fallback): Press → Macro 1,
    Slide → filter macro; two held notes morph independently under two fingers.
- **`04d-filters-mixer-global` — Filters, mixer, global, voicing (R, 90s).** 17 filter types per
  engine (LP/HP/BP, phaser, comb, vowel/formant, lo-fi, and the modal resonators), two macros each;
  the per-engine mixer (Volume / Pan / Tone); global Drive + Limiter + Master; Poly/Mono, glide
  (Portamento / Glissando), Stacked Voices + Spread. *Keep this short and lensed onto the two
  engines — supporting cast, not headline.* **Flag inline:** the voice cap (12 vs 32) is unresolved
  in the dossier — say "up to a few dozen voices" unless verified in the live device. *Inventory
  beat, kept tight — the ep1 Section-4 anti-flatline rule applies hardest here.*
- **`04e-when-to-reach` — Meld vs the family: when to reach for it (R, 90s).** The honest verdict:
  reach for **Meld** when you want character, texture, and per-note expression *fast*; reach for
  **Operator / Wavetable** when you want to *engineer* a spectrum from first principles. It is the
  least engineer-y, most performance-oriented of Live's synths; its center of gravity is MPE + two
  macros, not a deep editing surface. *Reflection — lands the act on the trade, not a cheer.*
  - **>> SIGNPOST into Act 5:** "Enough touring the panel. Build one patch that is two synths and
    ten fingers at once — and play one note with it." (Transition clip after `04e`.)

## ACT 5 — Patch Walkthrough  ·  slides `05a`–`05g`  ·  5–6 min

A single arc: build "Two-Hands" — a bi-timbral, MPE-played texture-lead that proves "two synths,
one note, ten fingers." Each step is an anecdote (a move that raises and answers "what changed").
Plant explicit position markers in the steps ("step 3 of 7", "halfway — now the second engine
joins / now we wire the fingers in") — the ep1 Section-5 progress-marker gap. ACT SEAM motivated:
"two macros only mean something one decision at a time." ACT OPEN — signpost: "Stop three — build
it."

- **`05a-engine-a-swarm` (A, 45s).** Engine A → **Swarm Saw** (scale-aware), Motion ~30, Spacing
  ~40; gentle low-pass. Anthemic body, scale-locked. Demo `meld-twohands-step1`.
- **`05b-engine-b-fm-resonator` (A, 60s).** Engine B → **Harmonic FM** an octave up, low level →
  **Plate Resonator** filter, scale-aware on. A glassy, body-resonant overtone layer. *"There's
  your 'physical modelling' — one filter."* (Echo the **"It's a filter, not the oscillator."**
  refrain.) Demo `meld-twohands-step2`.
- **`05c-cross-engine-lfo` (A, 45s).** **A's LFO 1 → B's Macro 1** (cross-engine, control-rate),
  slow. The two layers breathe together but differently. *(Half-built — two engines, now coupled.)*
  Demo `meld-twohands-step3`.
- **`05d-self-morph-loop-env` (A, 45s).** **Mod Env (A) → AD Loop → A's Macro 1**, gentle. The body
  self-morphs on held notes — the seam to the IDM act. Demo `meld-twohands-step4`.
- **`05e-mpe-routing` (A, 60s).** *(Halfway — now we wire the fingers in.)* **MPE tab:** Press → B's
  FM Amount; Slide → A's filter; Note Bend → A detune. Each finger now shapes its own note's
  timbre, brightness, and pitch. The step the whole patch exists to reach. Demo `meld-twohands-step5`.
- **`05f-drive-limiter-spread` (A, 45s).** Global **Drive** up a touch, **Limiter** on; **Stacked
  Voices** 2 + small **Spread** for width. The finishing glue. Demo `meld-twohands-step6`.
- **`05g-save` (R, 30s).** Save as **"Two-Hands."** *"Operator built a spectrum. Wavetable scanned
  one. Meld gave you two synths and ten fingers and got out of the way."* Reflection that ties the
  build back to the focus sentence. Echo the refrain.
  - **>> SIGNPOST into Act 6:** "One patch, two engines, ten fingers. Now three ways IDM uses Meld
    when there's no preset for what you want." (Transition clip after `05g`.)

## ACT 6 — IDM Application  ·  slides `06a`–`06e`  ·  5–6 min

Ordered: modulate-don't-write (the Autechre idea) → environmental oscillators as the source → the
Shepard trick (cold-open callback) → the two myths logged → the exercise. Closes on an exercise,
not a kicker (voice rule). ACT OPEN — signpost: "Stop four — make IDM with two synths and ten
fingers." All IDM artists framed as KINSHIP, never as Meld credit.

- **`06a-self-sequencing` — Self-sequencing timbre, the Autechre idea (A, 120s).** Mod Env in **AD
  Loop** → an oscillator macro; add an audio-rate **LFO (~200 Hz) → filter** for sideband grit;
  hold ONE note and it becomes a pattern. *"Modulate the timbre instead of writing the notes"* —
  the *Confield*-era aesthetic. *(Framed honestly: the method-kinship is real; no claim Autechre
  used Meld.)* *Anecdote — opens the act with a move.*
  - **Demo home:** `meld-self-sequence-onenote` — one held note, Mod Env AD-Loop → macro,
    audio-rate LFO → filter; a pattern from a single key.
- **`06b-environmental-osc` — Environmental oscillators as composition (A→R, 90s).** Rain / Crackle
  / Bubble as the *source*, not an effect; route Mod Env (Loop) → macro for evolving weather;
  Engine B → a quiet Sub for body. The Boards-of-Canada-adjacent texture target — synthesized, not
  sampled. *(Flagged: BoC's gear is analog/sampler, not Meld — aesthetic target only.)* *Reflection
  on texture-as-source.*
  - **Demo home:** `meld-rain-crackle-sub` — Engine A → Rain/Crackle, Mod Env Loop → macro; Engine
    B → Sub; an evolving synthesized-weather bed.
- **`06c-shepard-trick` — The Shepard trick, back to the cold open (A, 60s).** Shepard's Pi under a
  pad: an endless build for IDM tension. Ties straight back to the cold open — *"that staircase
  with no top from the start of the walk? Here's how you'd use it."* *Anecdote — the cold-open
  callback as a usable move.*
  - **Demo home:** `meld-shepard-under-pad` — Shepard's Pi running under a pad; the cold-open patch
    put to work.
  - **>> SIGNPOST into the close:** "Before the walk home — two corrections to put on the record."
    (Transition clip after `06c`.)
- **`06d-myth-recap` — Two myths, logged (R, 45s).** A tight, honest recap, not a new argument:
  Meld is **not** a physical modeller — that was two resonator *filters*, the rest is
  macro-oscillators (**"It's a filter, not the oscillator."**). And it did **not** arrive in 12.1 —
  it shipped with Live 12.0, March 2024 (Chord oscillator added 12.2). *Reflection — clears the
  desk before the exercise so the close is clean.*
- **`06e-exercise` — Listener exercise (R, 90s).** Open Meld. Engine A only. Hold exactly one note
  and don't play another for forty seconds. Your only job: make that one note tell a story. Change
  the oscillator type once. Loop a mod-envelope onto a macro so the timbre moves on its own. If you
  have an MPE controller, press harder and slide your finger and hear the sound bend to your hand.
  No chords, no new notes — just one note and the matrix. If you can make forty seconds of music
  that way, you've understood the whole point of this strange synth: Operator and Wavetable ask you
  to *design* a sound, but Meld asks you to **perform** one — pick a world, layer a second
  underneath, play both with your fingers. You don't build the sound here. You pick it — and then
  you play it. That's Meld. (Then stop talking — no kicker.)

---

## Gate 2 rubric — self-check

- [x] One-line **focus sentence** is writeable (above).
- [x] The piece has an **arc**: driving question (where did the control go, and why is the headline
      not an oscillator?) + surprising payoff (it moved into the performance — the per-note matrix
      is the instrument; and "physical-modelling hybrid" is two filters).
- [x] **Anecdote** beats alternate with **reflection** beats (tagged A/R per beat; each act opens
      anecdote-or-lens and lands reflection; no act runs >2 reflection beats without an anecdote —
      the ep1 Section-4 fix; Act 4 carries an explicit driving question instead of a feature list).
- [x] **Signposts** planted at every act boundary (`>> SIGNPOST`, mapped to the transition clips
      after `02d-where-meld-sits`, `03e-lfo-loop-env`, `04e-when-to-reach`, `05g-save`,
      `06c-shepard-trick`).
- [x] Concept blocks ordered by "what do I need next for this to make sense?" — what-it-is →
      Plaits → MPE → the four-synth map; then families → FM → modal resonators → scale-aware →
      LFO/loop-env; then two-engines → macros+matrix → MPE → filters/global → vs the family.
- [x] Each demo has a **conceptual home** in a block (noted inline; `meld-` = Meld device render,
      bare ids = song/module clips, all resolved in `clip_manifest.yaml` after lock).

**Gate 2: PASS.** Cleared to scripting. Do not advance line-level work past a flatline list — this
is not one.

## Voice/lexicon flags for the Writer (enforce at draft)

- Cold-open is a **contradiction/confession** (three impossible oscillators + two myths the host
  got wrong), not a welcome. Hold this.
- Close is the **exercise then a stop**, no motivational kicker. Hold the line in `06e`.
- Keep the dossier's honesty flags **inline** where they live — these are integrity gates, not
  decoration:
  - **No confirmed artist/track uses Meld** (2024 instrument). Aphex / Autechre / Squarepusher /
    Plaid / BoC appear as **aesthetic kinship or technique illustration only** — never as Meld
    credit. (`02c`, `06a`, `06b`.)
  - **"Plaits inside Meld" is FALSE** — say "lineage" / "acknowledged influence" (Tubb quote),
    never "contains Plaits' code." (`02b`.)
  - **"Physical-modelling hybrid" is mostly FALSE** — only the modal Plate/Membrane resonator
    *filters* qualify; they're a filter, not the oscillator. Bust it in `03c`, echo `05b`/`06d`.
  - **Version: Meld shipped Live 12.0, 5 March 2024**, NOT 12.1; the Chord oscillator is the only
    post-launch addition (12.2). Correct in the cold open and `02d`; recap in `06d`. (User on 12.4.)
  - **Suite-only** device; the "Live 12 Lite or higher" on the pack page refers to the preset pack,
    not the device — flag only if it comes up.
  - **Bi-timbral = two *summed* engines, control-rate cross-mod only** — not audio-rate cross-mod
    between engines. Get this exactly right in `04a`.
  - **"Granular-esque" (Noise Loop, Extratone) is buffer-loop/retrigger, NOT a true granular
    cloud** — don't oversell in `03a`.
  - **Voice cap 12 vs 32 is UNRESOLVED** — say "up to a few dozen" unless verified live (`04d`).
  - **Macros are normalized (0–1 / 0–100%), not Hz** — matters for the Sound Designer's headless
    renders; flag at the `meld-` demo handoff, not on-air.
- **Banned (hard fail):** journey / sonic journey, unleash, level up, game-changing/-changer,
  mind-blowing, magic happens, crafting sonic landscapes / sonic landscape, secret sauce, pro tips,
  synergy, AI-powered/-enhanced, unlock the power of, deep dive (noun), next-level, truly unique,
  really really / very very. Zero exclamation points, zero emojis.
