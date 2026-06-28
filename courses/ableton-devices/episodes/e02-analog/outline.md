# Episode 2 — Analog: The Subtractive Foundation — Beat Sheet (Gate 2)

**Story Editor outline.** Structure locks here before any line-level or sound work.
Source dossier: `specs/ableton_course_ep2_analog_research.md`. Voice enforced from
`shared/style/voice.md` + `shared/style/lexicon.md`.

---

## Focus sentence

> Subtractive synthesis is the art of controlling harmonics over time by *taking away* — and
> "analog character" is the imperfection a perfect digital model has to add back.

It is writeable in one line, it carries a driving question (*if the chain hasn't changed since
1964, why does the box that models it need a knob marked "Error"?*), and it has a payoff (the Error
knob is the thesis; the filter is an oscillator you forgot to turn on). Gate 2 focus-sentence
check: PASS.

## The driving question and the payoff

- **Question planted in the cold open:** Roland built a box to replace a bass player, failed, and
  discontinued it — so why is a genre named after the noise it made? Underneath: what is the oldest
  idea in synthesis, and why does Ableton ship a whole device just to teach it?
- **Payoff at the end:** the −3 dB cutoff, Q, and the Barkhausen self-oscillation condition are the
  same objects from a filter lab; the Reese bass, the Juno pad, the Supersaw and PWM strings are all
  one interference phenomenon; and the only difference between Episode 1's FM "dwah" and this
  episode's subtractive "wah" is topological — a modulator envelope versus a filter envelope. The
  knob and the textbook are the same thing.

## The arc (six acts, ~40 min)

1. **Cold open (90s)** — confession/contradiction: the silver box built to fail.
2. **History & theory (8–9 min)** — where subtractive came from; Moog → the filter wars → the
   303 → why anyone bothered to model analog.
3. **Synthesis deep-dive (8–9 min)** — the physics: oscillator spectra, the filter as a
   physicist sees it, self-oscillation, beating/PWM, two envelopes, drive.
4. **Device deep-dive (8–9 min)** — Ableton Analog specifically: AAS origin, the Error thesis,
   oscillators, the two filters, modulation, voice architecture.
5. **Patch walkthrough (5–6 min)** — build a 303 acid line, then morph it into a Reese without
   loading a new device.
6. **IDM application (5–6 min)** — self-oscillation as a sound source, the MS-20 abused, looping
   envelopes as rhythm, the fat-is-interference principle, then the exercise.

## Anecdote ⇄ reflection alternation (Ira Glass)

The two modes must trade off; flagged per beat below. **A** = anecdote (events that raise→answer a
question). **R** = reflection (why am I still listening). The macro shape: each act opens on an
anecdote and lands on a reflection, so no act is a flat list.

## The act-boundary signpost (the Ep1 lesson)

Ep1's table read showed sections can blur into one another without a planted "we are changing
chapters now" line. Each act here ends on an **explicit signpost sentence** that names the door we
are walking through. Those signpost lines are the conceptual homes of the inter-section
**transitions** in `episode.yaml` (after `02f`, `03f`, `04f`, `05i`, `06d`). They are noted as
`>> SIGNPOST` below.

---

## ACT 1 — Cold Open  ·  slide `01-cold-open`  ·  90s

- **A.** 1981: Roland builds the TB-303 to replace a bassist; it is bad at the job; discontinued in
  three years; dumped secondhand for the price of a pizza. A few Chicago kids buy one, ignore the
  manual, turn the knobs until it screams, and name a genre after the noise.
- **Demo home:** `acid-tracks-cold-open` — ~8s of Phuture "Acid Tracks" at ~1:27, the squelchy
  resonant 303 alone, under the open.
- **R.** The contradiction stated plainly: this is the *oldest* idea in synthesis — start rich,
  carve away — and the one Ableton device built to teach it.
- **Callback hook to Ep1:** "FM generated a spectrum from almost nothing. This starts with
  everything and sculpts." Plant the topology twist we'll pay off in 03e.
- **Payoff-refrain seed:** plant the three-word refrain **"Start rich. Carve. Listen."** here, in
  the cold open. It is the spine made sayable. Echo it once at each act boundary (the `>> SIGNPOST`
  lines double as its carrier) and *land* it in `06e` as the resolution — so the ending reads as a
  return, not a new thought. This is the Ep1 fix: seed the payoff line early so it pays off late.
- **>> SIGNPOST into Act 2:** "Four stops: where it came from, the physics, the device, and how to
  build acid and a Reese out of one default patch." (This is the cold-open MAP — the Ep1 lesson's
  single highest-leverage anti-"jumpy" fix: give the listener the act structure up front so every
  later seam reads as 'next stop,' not 'non sequitur.')

## ACT 2 — History & Theory  ·  slides `02a`–`02f`  ·  8–9 min

Ordered by "what do I need next for this to make sense?": define the chain → the filter that gave
it a voice → the rivals arguing about that filter → the fork we are NOT taking → the box that made
the filter a performance instrument → why we ended up modeling all of it.

- **`02a-silver-box` — What subtractive means (R, 90s).** VCO → VCF → VCA. Saw = every integer
  harmonic, so you start with everything and attenuate. The one-line trichotomy: additive adds
  sines, FM generates sidebands, subtractive filters away. *Reflection beat — sets the lens.*
- **`02b-moog-ladder` — Moog and the ladder filter (A, 120s).** 1964 AES paper; Patent 3,475,623
  (filed '66, granted '69); the 24 dB transistor ladder, exponential cutoff, self-oscillation;
  Minimoog (1970/71, $1,495, ~12,000 units, first synth sold in stores). *Anecdote beat.*
  - **Demo home:** `flash-light-bass` — ~8s of Parliament "Flash Light" under "rubber-band bass,"
    motivating why a detuned-VCO-through-a-ladder sound matters before we can build it.
- **`02c-filter-wars` — The filter wars (A→R, 90s).** ARP's 4012 "lawsuit filter" (caveat inline:
  threatened/settled, not cleanly "sued"); Roland's IR3109; Oberheim's state-variable SEM
  (LP/HP/BP/notch at 12 dB, doesn't self-oscillate) — named here because it is the closest hardware
  ancestor of Analog's per-filter multimode selector. Reflection tag: every company in the 70s was
  arguing about how to build one filter.
- **`02d-east-west` — East vs West Coast (R, 90s).** Moog (keyboard, subtractive, filter-centric)
  vs Buchla (no keyboard, waveshaping, low-pass gates). The fork we name only to close: we are
  firmly East Coast; Buchla is a different show. *Keeps the scope honest, prevents "and also."*
- **`02e-tb303-acid` — The TB-303 and acid (A, 120s).** Kikumoto's bass box, the diode-ladder
  filter (caveat inline: 18-vs-24 dB and 3- vs 4-pole genuinely contested — Stinchcombe), accent +
  slide, the commercial failure, Phuture / DJ Pierre "we didn't know how to work it," the genre
  named after a filter. Pays off the cold-open anecdote with the history behind it.
  - **Demo home:** `acid-tracks-303` — a second, longer Acid Tracks excerpt now that the listener
    knows what the knobs are doing.
- **`02f-virtual-analog` — Why model analog at all (R, 60s).** Drift, cost, recall; Nord Lead 1995
  (caveat: "first VA" contested, Korg Prophecy same year), Virus, JP-8000 Supersaw. Lands on:
  Ableton handed AAS the job of modeling all of it and called it Analog.
  - **>> SIGNPOST into Act 3:** "Before we open the device, the physics — because in subtractive
    synthesis the physics *is* the manual." (Transition clip after `02f`.)

## ACT 3 — Synthesis Deep-Dive  ·  slides `03a`–`03f`  ·  8–9 min

Ordered: what the source contains → how the filter removes it → what happens at the extreme →
why two sources make "fat" → how brightness is decoupled from loudness → how to dirty it.

- **`03a-oscillator-spectra` — Oscillator spectra (R, 90s).** Saw (all harmonics, 1/n), square
  (odd, 1/n), pulse/PWM (sinc nulls move with duty cycle); note Analog has no triangle.
  - **Demo home:** `an-pwm-sweep` — held note, rectangular osc, sweep Pulse Width from 50% down;
    even harmonics fade in with no filter touched. The unmistakable "spectrum changing" demo.
- **`03b-filter-physicist` — The filter, for a physicist (R, 120s).** Poles ↔ slope (6 dB/oct per
  pole); cutoff = the −3 dB half-power point ("the same −3 dB from your filter labs"); resonance =
  Q = feedback. Speaks directly to the physicist listener — the reflection payoff of the act.
  - **Demo home:** `an-slope-12-vs-24` — A/B 12 vs 24 dB at the same cutoff on a held note.
- **`03c-self-oscillation` — Self-oscillation (A, 90s).** Barkhausen condition, loop gain → 1, the
  pole pair on the imaginary axis; the filter becomes a sine oscillator. Anecdote anchor: this *is*
  Digeridoo, there is no didgeridoo — planted here, paid off in 06a.
  - **Demo home:** `an-reso-to-self-osc` — crank Reso to max, kill the oscillators, play the filter.
- **`03d-beating-pwm` — Detuning, beating, PWM (R, 120s).** Two near-equal sines beat at Δf;
  cents-detune ⇒ beating accelerates with pitch; PWM = one oscillator behaving like two. The
  loudest single idea in the episode: "fat" is interference. The Reese and the Juno are the same
  physics.
  - **Demo homes:** `an-reese-detune-sweep` (two saws, detune 0→20 cents, held low note) and
    `an-pwm-strings` (one rect osc, LFO → Pulse Width, held chord).
- **`03e-two-envelopes` — Two envelopes, two jobs (R, 90s).** Amp env = loudness; filter env =
  brightness. **The explicit Ep1 callback:** in FM the modulator's envelope *was* the brightness;
  here it is a separate filter envelope — same "dwah," opposite topology. This is the topology
  payoff promised in the cold open.
  - **Demo home:** `an-filter-env-vs-amp-env` — same decay routed to filter env vs amp env, A/B.
- **`03f-drive` — Drive (R, 60s).** Symmetric (odd harmonics) vs asymmetric (even); the difference
  between a digital sweep and an analog one is the distortion you can't hear until it's gone.
  - **>> SIGNPOST into Act 4:** "That is the whole physics. Now the one device that puts every one
    of those knobs in front of you, one-to-one." (Transition clip after `03f`.)

## ACT 4 — Device Deep-Dive (Ableton Analog)  ·  slides `04a`–`04f`  ·  8–9 min

**Section driving question (the explicit Ep1 fix — plant it at `04a` so the tour is not a feature
list).** Ep1's table read failed here: seven device-tour beats joined by "and also," no question
pulling one beat into the next. This act must instead answer one live question end to end:
*"AAS had to fold the entire subtractive canon — Moog, ARP, Roland, Oberheim, the MS-20 — into one
device, and then make a perfect digital model sound imperfect. So what did they keep, what did they
add that no vintage synth had, and where do they hide the imperfection?"* Every beat below is an
answer: `04b` = the imperfection (Error); `04c`/`04d` = what they kept (the canon's oscillator and
the canon's filters, rebuilt); `04e`/`04f` = what they added (looping envelopes, two-of-everything,
the Unison supersaw). Surface that framing at the top of `04a` and re-touch it opening each beat.

Ordered: where it came from → the philosophical knob that defines it → oscillators → filters →
modulation → how two-of-everything composes into a voice.

- **`04a-origin` — Analog origin (A, 60s).** AAS, IRCAM roots, Tassman/Ultra Analog physical
  modeling; shipped with Live 7 / Suite, Nov 2007 (caveat inline: not Live 4/5). Operator was
  Ableton's own FM machine; Analog is borrowed physics — and every control maps onto the textbook.
- **`04b-error-thesis` — Physical modeling and the Error knob (R, 90s).** No samples, no wavetables
  — circuit equations solved every sample, alias-free. The Error knob is the thesis: a perfect model
  of an imperfect machine sounds wrong until you add the imperfection back. *Reflection peak of the
  act; restates the focus sentence as a device fact.*
  - **Demo home:** `an-error-drift` — same chord with Error at 0 vs dialed up; the model "comes
    alive."
- **`04c-oscillators` — The oscillators (A, 120s).** Four shapes (sine/saw/rect/noise, no
  triangle), Pulse Width + PWM, Sub an octave down, Detune ±300 cents, F1/F2 routing balance, the
  noise generator, and Sync — the Ratio sweep that screams.
  - **Demo home:** `an-sync-ratio-sweep` — map the Sync Ratio to a sweep; the tearing sync lead.
- **`04d-two-filters` — The two filters (A, 120s).** LP/HP/BP/Notch/Formant in 12 or 24 dB, per
  filter; series vs parallel (To F2, Follow); Formant = vowels on the Reso knob; Drive Sym/Asym.
  Anchor anecdote: rebuild the MS-20 — HP→LP in series, both resonant.
  - **Demo home:** `an-ms20-series-filter` — HP→LP series, both resonant, swept against each other.
- **`04e-envelopes-lfos` — Envelopes, LFOs, modulation (R, 90s).** Four ADSRs (two filter, two
  amp), Free (percussive) and Loop modes, S.Time; two LFOs with delay/attack (delayed vibrato),
  free-run vs retrig; Vibrato as a hardwired third LFO. *Inventory beat kept short and lensed.*
- **`04f-voice-architecture` — Voice architecture + make-it-analog (R, 90s).** Two sub-voices per
  note: split-filter timbres, stereo voices (pan AMP1/AMP2), Unison (2/4 + Detune = a supersaw).
  The stack: Error + Asym Drive + free-run LFOs + Detune. Lands the act: everything the canon had,
  in one device, plus a knob to make it drift like 1978.
  - **Demo home:** `an-unison-supersaw` — Unison 4 + Detune approximating the JP-8000 Supersaw.
  - **>> SIGNPOST into Act 5:** "Enough touring the panel. Build the one bass sound that this whole
    instrument is secretly about — twice." (Transition clip after `05i` closes the build.)

## ACT 5 — Patch Walkthrough  ·  slides `05a`–`05i`  ·  5–6 min

A single arc: build a 303 acid line from the default patch, then morph the *same* patch into a
Reese without loading a new device. The narrative payoff is the morph — two genres a parameter
apart. Each step is an anecdote (a knob move that raises and answers "what changed").

- **`05a-default` (A, 45s).** Voices = 1, Glide = Const (short) + Legato for slides; OSC1 = saw,
  OSC2 off, Sub off. Demo `an-303-step1`.
- **`05b-lowpass` (A, 45s).** Filter 1 = LP 24, route OSC1 fully to F1, cutoff mid, Reso ~40%.
  Demo `an-303-step2`.
- **`05c-filter-env` (A, 60s).** Filter env → Freq, high amount, short Decay, Sustain ≈ 0 — the
  per-note wow. Demo `an-303-step3`.
- **`05d-resonance` (A, 45s).** Reso up to ~80%; the squelch sharpens toward self-oscillation.
  Demo `an-303-step4`.
- **`05e-drive-accent` (A, 45s).** Drive = Asym for dirt; Env<Vel up so accented (high-velocity)
  notes open brighter — that's the accent. Demo `an-303-step5`.
- **`05f-automate` (A, 45s).** Program a 16th line with slid notes; automate Filter Freq across 16
  bars. "That's acid: a saw, a resonant low-pass, and your hand on the cutoff." Demo `an-303-step6`.
- **`05g-morph-reese` (A, 45s).** Turn OSC2 on (saw), Detune ±18 cents, Sub on, drop the filter
  envelope, lower the cutoff. Demo `an-reese-morph`. The pivot the whole act exists for.
- **`05h-detune-listen` (R, 30s).** Hold a low note; the saws beat with no LFO; beating accelerates
  with pitch. Reflection: Chicago 1987 to Bristol 1994 is one parameter — a second detuned
  oscillator. Demo `an-reese-final`.
- **`05i-save` (R, 30s).** Save as "Subtractive-303-Reese." Two of the most influential bass sounds
  in electronic music from one default patch — and in 1981 the box that made the first was a flop.
  - **>> SIGNPOST into Act 6:** "Two basses out of one device. Now three IDM moves that come from
    pushing the same filter past polite." (Transition clip after `05i`.)

## ACT 6 — IDM Application  ·  slides `06a`–`06e`  ·  5–6 min

Ordered: the most extreme filter trick → the dual-filter abuse → rhythm from an envelope → the
unifying principle → the exercise. Closes on an exercise, not a kicker (voice rule).

- **`06a-self-oscillation` — The filter as oscillator: Digeridoo (A, 90s).** Oscillators down, Reso
  = max, LP 24, Filter Freq key-tracked → play the self-oscillating filter as a sine synth, then
  LFO → Freq for the drone. Pays off the 03c plant: there is no didgeridoo; Aphex worked this out
  at 19.
  - **Demo homes:** `an-digeridoo-drone` (the Analog rebuild) and `digeridoo-clip` (the record,
    for the A/B).
- **`06b-ms20-abused` — The MS-20 dual filter, abused (A, 90s).** HP→LP series, both resonant,
  swept against each other; run into bitcrush + short reverb. The Autechre move: analog filters
  pushed past politeness, then degraded with cheap digital gear until they sound like a memory.
  - **Demo homes:** `an-ms20-scream` (the Analog rebuild) and `tri-repetae-clip` (the reference).
- **`06c-loop-envelopes` — Looping envelopes as rhythm (A, 60s).** Filter env to Loop (AD-R),
  tempo-ish rate → a free evolving rhythmic pulse from one held note. No LFO, no sequencer — the
  envelope is the rhythm.
  - **Demo home:** `an-loop-env-pulse`.
- **`06d-fat-principle` — Fat is just interference (R, 60s).** Unison 4 + Detune (supersaw), PWM
  (string pad), two detuned saws (Reese) — all the same trick: copies of a wave that almost agree.
  The reflection that ties the whole episode to the focus sentence.
  - **>> SIGNPOST into the exercise:** "One last thing, for the walk home." (Transition clip after
    `06d`.)
- **`06e-exercise` — Listener exercise (R, 90s).** Build the 303 from the walkthrough. Then do what
  Phuture did: don't program it — turn cutoff and resonance by hand over a loop until the filter
  starts to sing. When it does, you've found unity gain — the Barkhausen condition — by ear, the
  way a 19-year-old in Cornwall found Digeridoo and three kids in Chicago found acid house. Start
  rich. Carve. Listen. Then stop talking (no kicker).

---

## Gate 2 rubric — self-check

- [x] One-line **focus sentence** is writeable (above).
- [x] The piece has an **arc**: driving question (why a knob marked "Error"?) + surprising payoff
      (the filter is an oscillator; topology is the only difference from FM).
- [x] **Anecdote** beats alternate with **reflection** beats (tagged A/R per beat; each act opens
      anecdote, lands reflection).
- [x] **Signposts** planted at every act boundary (`>> SIGNPOST`, mapped to the transition clips).
- [x] Concept blocks ordered by "what do I need next for this to make sense?" — chain → filter →
      rivals → fork → 303 → why model; then source → removal → extreme → interference → envelopes →
      drive; then origin → Error → osc → filters → mod → voice.
- [x] Each demo has a **conceptual home** in a block (noted inline; `an-` = Analog render, bare ids
      = song clips, all to be resolved in `clip_manifest.yaml` after lock).

**Gate 2: PASS.** Cleared to scripting. Do not advance line-level work past a flatline list — this
is not one.

## Voice/lexicon flags for the Writer (enforce at draft)

- Cold-open is a **contradiction** (box built to fail), not a welcome. Good.
- Close is the **exercise then a stop**, no motivational kicker. Hold the line here.
- Keep caveats **inline** where they live: TB-303 slope (contested 18/24 dB, 3/4-pole), Reese synth
  (Casio CZ phase distortion, not subtractive saws — the modern Reese is the re-creation), "first
  VA" (contested), ARP "lawsuit" (threatened/settled). These are dossier flags; do not bury them.
- **Banned (hard fail):** journey / sonic journey, unleash, level up, game-changing, mind-blowing,
  magic happens, sonic landscape, secret sauce, pro tips, synergy, AI-powered/-enhanced, unlock the
  power of, deep dive (noun), next-level, truly unique, really really / very very. Zero exclamation
  points, zero emojis.
