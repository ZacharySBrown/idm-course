# Episode 3 — Wavetable: Morphing Through Spectra — Beat Sheet (Gate 2)

**Story Editor outline.** Structure locks here before any line-level or sound work.
Source dossier: `specs/ableton_course_ep3_wavetable_research.md`. Voice enforced from
`shared/style/voice.md` + `shared/style/lexicon.md`.

---

## Focus sentence

> Wavetable synthesis is the art of modulating one parameter — Position — and everything from the
> 1982 PPG choir to the 2021 dubstep growl is the same gesture at a different rate: you don't filter
> a sound to make it move, you walk between sounds.

It is writeable in one line, it carries a driving question (*why is the most important knob the one
that changes neither pitch, nor volume, nor the filter?*), and it has a payoff (the harsh scan Palm
tried to filter out and then kept is the same gesture that became 80s pop, 90s grit, and the modern
growl; the pad and the Skrillex bass are one LFO-rate apart on the same patch). Gate 2
focus-sentence check: PASS.

## The driving question and the payoff

- **Question planted in the cold open:** In 1978 Wolfgang Palm set out to build a digital low-pass
  filter and failed — what came out sounded harsh and alien. He kept it. So why did a *mistake*
  become the defining timbre of three separate decades, and why is the knob it produced — Position —
  the one that changes which sound you're playing while you play it, and nothing else?
- **Payoff at the end:** the orthogonality of pitch and timbre is the whole technique; every
  signature sound is one source routed to Position; each generation re-decides whether the aliasing
  is a flaw to remove (Hi-Q on, the Serum aesthetic) or the signature to keep (Hi-Q off, the Hamburg
  sound). The PPG choir and the Skrillex growl are the same instrument with the LFO rate turned up —
  proven live in the walkthrough by one macro. And for the physicist: FM *generates* spectra via
  Bessel sidebands (Episode 1); wavetable *interpolates* between pre-stored additive snapshots —
  last episode the magic knob was modulation index, this one it's Position.

## The arc (six acts, ~40 min)

1. **Cold open (90s)** — confession/contradiction: the failed filter Palm kept on purpose.
2. **History & theory (8–9 min)** — PPG → Waldorf → Massive/Serum/Vital → Ableton; how a 1978
   accident became the default architecture of modern electronic music.
3. **Synthesis deep-dive (8–9 min)** — the physics: a wavetable as a sequence of additive
   snapshots, pitch/timbre orthogonality, interpolation, aliasing, and wavetable vs FM.
4. **Device deep-dive (8–9 min)** — Ableton Wavetable specifically: architecture, the oscillator
   effects, the destination-first matrix, envelopes/LFOs, filters/unison, vs Serum/Massive.
5. **Patch walkthrough (5–6 min)** — build a PPG-style morph pad, then turn it into a Subtronics
   growl with one macro, on the same patch.
6. **IDM application (5–6 min)** — import your own table (Plaid), loop-envelope rhythm, aliasing on
   purpose, MPE-Position, then the exercise.

## Anecdote ⇄ reflection alternation (Ira Glass)

The two modes must trade off; flagged per beat below. **A** = anecdote (events that raise→answer a
question). **R** = reflection (why am I still listening). Macro shape: each act opens on an anecdote
and lands on a reflection, so no act is a flat list. The ep1 Section-4 flatline failure was a run of
device-tour beats with no question pulling one into the next — guarded against in Act 4 below.

## The act-boundary signpost (the Ep1 lesson)

Ep1's table read showed sections can blur into one another without a planted "we are changing
chapters now" line. Each act here ends on an **explicit signpost sentence** that names the door we
are walking through. Those signpost lines are the conceptual homes of the inter-section
**transitions** in `episode.yaml` (after `02e`, `03e`, `04f`, `05g`, `06d`). They are noted as
`>> SIGNPOST` below.

## The payoff refrain

Three beats, made sayable: **"Pitch and timbre, separate dials. Walk the timbre."** Seed it in the
cold open, echo it once at each act boundary (the `>> SIGNPOST` lines carry it), and *land* it in
`06e` as resolution — so the ending reads as a return, not a new thought. This is the Ep1 fix: seed
the payoff line early so it pays off late.

---

## ACT 1 — Cold Open  ·  slide `01-cold-open`  ·  90s

- **A.** 1978, a workshop in Hamburg: Wolfgang Palm tries to build a digital low-pass filter and
  fails — what comes out is harsh, metallic, alien, nothing like the warm analog sweep he wanted. He
  does what every good inventor does with a failure: he keeps it, bolts a real analog filter on the
  end to make customers happy, and keeps the harsh part too.
- **Demo home:** `see-you-cold-open` — ~10s of Depeche Mode "See You" intro, the ghostly PPG choir
  pad alone, held under the open then ducked as narration enters.
- **R.** The contradiction stated plainly: that harsh part — scanning through a row of single-cycle
  waveforms — became the defining timbre of the next decade of pop, went underground, and came back
  as the most-used synthesis method in modern electronic music. The choir you're hearing is a PPG.
- **Callback hook to Ep1:** "Last episode the magic knob was modulation index — FM generated a
  spectrum from almost nothing. This episode the magic knob is Position, and it changes neither the
  pitch, the volume, nor the filter. It changes which sound you're playing, while you play it." Plant
  the pitch-vs-timbre orthogonality we pay off in `03a`.
- **Payoff-refrain seed:** plant **"Pitch and timbre, separate dials. Walk the timbre."** here. Echo
  it at each act boundary (the `>> SIGNPOST` lines carry it) and *land* it in `06e`.
- **>> SIGNPOST into Act 2:** "Four stops: where this sound came from, the physics under it, the one
  Ableton device built around it, and how to build a PPG choir and a dubstep growl out of the same
  patch." (The cold-open MAP — the Ep1 lesson's highest-leverage anti-"jumpy" fix: give the act
  structure up front so every later seam reads as 'next stop,' not 'non sequitur.')

## ACT 2 — History & Theory  ·  slides `02a`–`02e`  ·  8–9 min

Ordered by "what do I need next for this to make sense?": the accident that made the sound → the
machine that made it 80s pop → who carried the grit when PPG folded → how plugins inverted the
aesthetic and made it the default → how Ableton finally arrived.

- **`02a-palm-accident` — The Palm accident (A, 90s).** Hamburg 1978, the Wavecomputer 360 — 30
  wavetables, no analog filter, "buzzy and thin," ~40 built. The failed filter that became a feature.
  **Drop the Palm quote:** "these wavetable sweeps sounded very harsh; not at all like an analogue
  filter sweep." One concrete sentence on what a wavetable is: "a row of single-cycle waveforms; you
  don't filter the sound, you walk between sounds." *Anecdote — opens the act.*
- **`02b-ppg-defines-80s` — The PPG Wave defines the 80s (A, 120s).** 1981 Wave 2; the hybrid
  (digital oscillators → analog VCF). The artist receipts: Tangerine Dream / Froese's "completely
  new musical structures"; Depeche Mode's Martin Gore choir + bell on "See You"; Numan's "heart and
  soul of *Berserker*"; the hidden PPG transient "click" on Tears for Fears' "Everybody Wants to Rule
  the World." Myth-busters inline: Bowie's PPG is *Tonight* (1984), credit only, no quote; "Shout"
  is a Fairlight, not PPG; Jarre's PPG link is likely a misattribution — drop or flag.
  - **Demo homes:** `see-you-choir` (~10s "See You" — the canonical glassy wavetable choir/bell) and
    `everybody-wants-bass` (~8s "Everybody Wants to Rule the World" — the PPG as percussive
    high-end click under the DX7, the *subtle* PPG, our best transient-design example).
- **`02c-waldorf-grit` — Waldorf carries the grit (A→R, 90s).** PPG folds end of 1987; Palm's chip
  into the Microwave (1989); Waldorf was the former German PPG distributor. **Drop the SoS quote:**
  "aliasing and other digital nasties are part and parcel of the Microwave's distinctive sound." The
  strongest 90s case: Charlie Clouser's Microwave on early Nine Inch Nails — "the most brutal
  industrial bass sounds." Reflection tag: the grit was now the *point*, not a defect.
- **`02d-plugin-revival` — The plugin revival (A→R, 120s).** Massive (2007) — "the wobbly basses …
  of dubstep"; the wobble is an LFO on wavetable position. Serum (2014) — Duda's clean, import-
  everything wavetable editor (FFT/draw/import); correct the deadmau5 myth (attribute the rationale
  to **Duda**, not deadmau5). Vital (2020) — free, spectral-warping. Timeline trap stated up front:
  Skrillex's foundational growls (2010–11) are **Massive + FM8, not Serum** — Serum didn't ship
  until 2014. **The thesis line (R):** "The PPG's limitation — you can only scan through fixed
  timbres — became the plugin era's signature feature: you can modulate through fixed timbres. Same
  idea, opposite verdict."
  - **Demo home:** `scary-monsters-growl` — ~8s of "Scary Monsters and Nice Sprites" growl drop, the
    LFO-on-position "talking bass," set up correctly as Massive (the authoritative-fact move).
- **`02e-ableton-enters` — Ableton enters (R, 60s).** Live 10, February 2018, Suite-only; PPG named
  as the inspiration; Henke's "you can get lost, but in the sound, not in tons of parameters." 194
  tables, 12 categories. User import added in 10.1 (2019). Lands the act: forty years of scanning,
  finally inside the DAW.
  - **>> SIGNPOST into Act 3:** "Before we open the device — the physics, because in wavetable the
    physics is the whole reason Position is the only knob that matters." (Transition clip after
    `02e`.)

## ACT 3 — Synthesis Deep-Dive  ·  slides `03a`–`03e`  ·  8–9 min

Ordered: what a wavetable IS → why a physicist already knows it (additive) → how scanning is made
smooth (interpolation) → the central DSP fight that *is* the PPG-vs-Serum aesthetic (aliasing) →
how it differs from last episode's FM.

- **`03a-what-a-wavetable-is` — What a wavetable IS (R, 90s).** An ordered collection of single-cycle
  frames; all frames share the base period, so scanning Position changes only the harmonic content —
  pitch is on a separate dial. The orthogonality the cold open promised. *Reflection beat — sets the
  lens; pays off the cold-open plant.*
  - **Demo home:** `wt-position-by-hand` — Basic Shapes table, **hold one note, drag Position 0→100
    by hand**; the sound walks sine → triangle → saw → square at constant pitch. The single most
    important demo in the episode — it isolates pitch/timbre orthogonality.
- **`03b-additive-connection` — The additive connection, for the physicist (R, 120s).** Each frame's
  DFT is a fixed harmonic spectrum; a wavetable is therefore a *sequence of additive snapshots*, and
  scanning Position is interpolating between two spectra — "you already know this; it's walking a path
  through Fourier space, one frame to the next." Note Serum's FFT import: any sample becomes a frame.
  Direct address to the physicist listener — the reflection payoff of the act's first half.
  - **Demo home:** `wt-ab-two-positions` — Osc 1 at a low position, Osc 2 at a high position of the
    *same* table, equal gain; toggle each cube. Two distinct timbres from one waveform set — proof a
    table is a collection of spectra.
- **`03c-interpolation` — Interpolation: the math of scanning (R, 90s).** The linear cross-fade
  `x_p = (1-α)x_i + α·x_{i+1}`; why neighbors must be phase- and spectrum-compatible (Ableton's "no
  inharmonic content between waves" curation rule); why naive frame-jumps zipper — and why the PPG
  zippered *gloriously* because 8-bit hardware had no real-time interpolation. Serum's ~50 ms fade.
  *Reflection — but the zipper anecdote keeps it from going dry.*
  - **Demo home:** `wt-zipper-vs-smooth` — same slow sweep, naive-step vs interpolated (or coarse vs
    Hi-Q proxy) to hear stepping become a glide.
- **`03d-aliasing` — Aliasing: the central DSP fight (R→A, 120s).** High harmonics fold past Nyquist
  into inharmonic alias tones; two fixes — band-limited mip-mapping and oversampling. **The punchline
  (A):** "Hi-Q off is a PPG. Hi-Q on is a Serum. The entire forty-year argument, in one switch." The
  uncorrected aliasing — 8-bit playback, no interpolation, ~26 Hz control updates — *is* the Hamburg
  grit; Serum and Wavetable spend their DSP budget removing exactly what made the PPG iconic.
  - **Demo home:** `wt-hiq-on-vs-off` — same patch, fast position sweep, toggle Hi-Q. The whole
    aesthetic in two seconds. (Reused conceptually in `06c` for the on-purpose move.)
- **`03e-wavetable-vs-fm` — Wavetable vs FM (R, 90s).** **The explicit Ep1 callback:** FM *generates*
  spectra via Bessel sidebands; wavetable *interpolates* between pre-stored additive snapshots. Both
  shape timbre with one envelope/LFO — FM via the modulator's Level, wavetable via Position. "Last
  episode the magic knob was modulation index. This episode it's Position." FM is generative;
  wavetable is interpolative — and Wavetable hides an FM oscillator inside each wavetable oscillator,
  the seam into the device.
  - **Demo home:** `wt-fm-inside-wavetable` — one oscillator, sweep FM Amount (or Modern→Fold) on a
    held note to hear harmonics grow *inside* the wavetable; the bridge from this episode to last.
  - **>> SIGNPOST into Act 4:** "That's the physics. Now the one device that puts Position at the
    center of everything — and came to wavetable last, on purpose." (Transition clip after `03e`.)

## ACT 4 — Device Deep-Dive (Ableton Wavetable)  ·  slides `04a`–`04f`  ·  8–9 min

**Section driving question (the explicit Ep1 fix — plant it at `04a` so the tour is not a feature
list).** Ep1's table read failed here: device-tour beats joined by "and also," no question pulling
one into the next. This act must answer one live question end to end: *"Ableton came to wavetable
LAST — after Massive, Serum, and Vital already owned it. So what did they do differently: what did
they leave OUT on purpose, what did they build the whole instrument AROUND, and what can it do that
Serum can't do in one click?"* Every beat is an answer: `04b` = what they built around (per-osc
effects, including FM inside the oscillator); `04c` = the destination-first matrix is the heart;
`04d`/`04e` = the parts that exist to serve Position (envelopes/LFOs, filters/unison); `04f` = what
they left out (no FFT/draw editor) and the two distinctive moves (Split routing, Position Spread).
Surface the framing at the top of `04a` and re-touch it opening each beat.

Ordered: architecture → the oscillator's warp engine → the matrix that ties it together → the
modulators that drive Position → the filters and the unison trick → how it stacks up against Serum.

- **`04a-architecture` — Wavetable architecture (A, 60s).** Two wavetable oscillators + a Sub; 194
  tables across 12 categories; Suite-only, Live 10, 2018; user import in 10.1 (256 frames). Henke's
  "get lost in the sound, not the parameters." Plant the driving question here.
- **`04b-oscillator-effects` — The oscillator effects (R, 90s).** The per-oscillator warp engine:
  **FM** (a hidden sine modulator, ±2 oct), **Classic** (synced PWM), **Modern** (Warp / Fold
  wavefolding). "There's an FM oscillator hiding inside each wavetable oscillator — Serum's grid
  can't quite do FM this cleanly." *Reflection on what makes Wavetable's oscillator distinctive.*
  - **Demo home:** `wt-modern-fold-sweep` — Modern→Fold with a slow envelope on Fold amount; a
    wavefolder sweep with no separate device.
- **`04c-mod-matrix` — The modulation matrix, the heart (A, 120s).** Destination-first design —
  Hobson's "I want this parameter modulated by this, rather than 'I have this modulator, I want to
  modulate that.'" The mechanism: tweak almost any control and it appears as a new matrix row. Three
  envelopes + two LFOs + five MIDI sources (and MPE Pressure/Slide). The 10 canonical routings;
  emphasize **LFO→Position** (wobble), **slow Env→Position** (pad), **multiple sources→Position +
  filter** (growl). The reflection refrain echoes: every signature sound is a source on Position.
  - **Demo home:** `wt-lfo-to-position` — tweak Position so it enters the matrix, assign LFO 1 →
    Position, amount ~40, rate 1/8 synced; the held note wobbles *without changing pitch*. Raise the
    rate into audio range to hear it cross into FM-like sidebands.
- **`04d-envelopes-lfos` — Envelopes and LFOs (R, 90s).** Three envelopes (one is Amp) with
  None/Trigger/Loop modes — a free envelope in Loop → Position is a self-cycling timbral sequencer.
  Two LFOs (Sine/Tri/Saw/Square/S&H + Shape skew) with **Attack fade-in** (the underrated control —
  a ~2 s fade-in makes movement bloom only after a sustained note, the "comes alive on long notes"
  pad trick) and LFO→LFO-Rate for non-periodic motion. *Inventory beat, kept short and lensed onto
  Position.*
  - **Demo home:** `wt-lfo-attack-bloom` — slow LFO → Position with ~2 s Attack; the morph blooms
    after the note is held.
- **`04e-filters-unison` — Filters and unison (A, 90s).** Two identical multimode filters, three
  routings — Serial / Parallel / **Split** (Osc 1→F1, Osc 2→F2; per-oscillator filtering nothing
  else exposes this cleanly). The five Cytomic circuits — Clean / OSR (OSCar) / MS2 (MS-20) / SMP /
  PRD (Moog Prodigy) — the *same* physically-modeled analog circuits as Auto Filter and Operator, so
  a patch's filter character matches Live exactly. Six unison modes; highlight **Position Spread** — a
  *chord of timbres from one note*, nothing in Serum does this in one click.
  - **Demo home:** `wt-position-spread-chord` — one chord, Position Spread unison (4 voices); each
    voice sits at a different wavetable position. The "one note, many timbres" proof.
- **`04f-vs-serum-massive` — Wavetable vs Serum vs Massive (R, 90s).** The honest verdict: reach for
  **Serum** when you need to *build* tables (full editor: draw, import, FFT-resynthesis); reach for
  **Wavetable** when you want to *play and modulate* them inside Live with the least friction. What
  they left out — no drawing/FFT editor — is a *curation* choice; what they won on — native
  integration, the destination-first matrix, Cytomic circuits, Position Spread. *Reflection; lands
  the act on the trade, not a cheer.*
  - **>> SIGNPOST into Act 5:** "Enough touring the panel. Build one patch that is a PPG choir and a
    dubstep growl at the same time — and prove it with a single knob." (Transition clip after `05g`
    closes the build.)

## ACT 5 — Patch Walkthrough  ·  slides `05a`–`05g`  ·  5–6 min

A single arc: build a PPG-style evolving morph pad from the default, then turn the *same* patch into
a Subtronics-style growl bass with one macro — proving they're the same instrument. The narrative
payoff is the macro sweep. Each step is an anecdote (a move that raises and answers "what changed").
Plant explicit position markers in the steps ("step 3 of 7", "halfway — now we arm the growl") — the
ep1 Section-5 progress-marker gap.

- **`05a-vowel-pad` (A, 45s).** Default Wavetable; Osc 1 → a Formants / vocal-choir table; Amp env
  A≈800 ms, S full, R≈1.5 s. Hold a chord — a static vowel pad. Demo `wt-spectra-step1`.
- **`05b-lfo-position` (A, 45s).** Tweak **Position** so it enters the matrix; assign LFO 1
  (triangle) → Position, amount ~30, rate sub-1 Hz, **LFO Attack ~2 s**. The pad blooms and morphs
  after you hold it. "That's the PPG choir — a slow Position scan." Demo `wt-spectra-step2`.
- **`05c-position-spread` (A, 45s).** Unison → **Position Spread**, 4 voices, light detune. The chord
  becomes a chord of timbres. Add an OSR filter, gentle. Demo `wt-spectra-step3`.
- **`05d-sub-and-bell` (A, 60s).** **Sub** at −1 oct, Tone ~15% for weight; **Osc 2** an octave up
  on a bell / Harmonics table, low gain, for glassy overtones (the DM bell riff). Demo
  `wt-spectra-step4`.
- **`05e-arm-the-growl` (A, 60s).** *(Halfway — now we arm the transform.)* Add **LFO 2 (saw) →
  Position** at 1/8 synced, amount ~50, **bypassed for now**. Add **Env → Filter Freq**. Switch Osc 1
  effect to **FM**, amount ~20, for a metallic edge. Demo `wt-spectra-step5`.
- **`05f-macro-morph` (A, 60s).** Map a **Macro**: at 0 = the slow pad LFO; at 127 = LFO 2 fast
  wobble + filter tighter + mono/glide on. Sweep the macro live: "Same oscillators, same table — a
  pad and a dubstep growl are one Position-modulation decision apart." The payoff the act exists for.
  Demo `wt-spectra-macro-sweep`.
- **`05g-save` (R, 30s).** Save as "Spectra-Morph." "The PPG and Skrillex are the same instrument
  with the LFO rate turned up." Reflection that ties the build back to the focus sentence.
  - **>> SIGNPOST into Act 6:** "One patch, two genres. Now four ways IDM uses Position when nobody's
    selling a preset for it." (Transition clip after `05g`.)

## ACT 6 — IDM Application  ·  slides `06a`–`06e`  ·  5–6 min

Ordered: scan your *own* source → rhythm from a looping envelope → the grit on purpose → per-note
expression → the exercise. Closes on an exercise, not a kicker (voice rule).

- **`06a-import-your-own` — Import your own wavetable (A, 90s).** Drag an audio file — a vowel, a
  field recording, a resampled Operator FM patch — onto the sprite area; Live reads up to 256 frames.
  Route Env (Loop) or LFO → Position to scan your own source. "This is Plaid's *Polymer* method —
  wavetable as texture, not bass." *Anecdote — opens the act.*
  - **Demo homes:** `wt-user-table-scan` (the import + scan rebuild) and `polymer-clip` (~8s of
    Plaid *Polymer* scanning-texture, the IDM software-wavetable reference).
- **`06b-loop-envelope-rhythm` — Rhythmic timbre via loop envelopes (A, 90s).** A free envelope in
  **Loop** → Position; sync an LFO to 1/16 onto FM Amount. One held note becomes a self-sequencing
  timbral pattern — "the line between sequencing and synthesis disappears," the Autechre idea,
  achieved by modulating Position instead of writing notes. *(Autechre framed honestly: their
  wavetable lineage is the Ensoniq EPS transwave, not PPG/Waldorf — name it as the idea, not a
  hardware claim.)*
  - **Demo home:** `wt-loop-env-sequence` — held note, Loop env → Position, LFO→FM; a pattern from a
    single key.
- **`06c-aliasing-on-purpose` — The aliasing aesthetic, on purpose (R, 60s).** Turn **Hi-Q OFF**,
  push a fast position sweep through a Distortion-category table, Modern→Fold up. "You've just rebuilt
  the PPG grit Palm tried to filter out and then kept. Aliasing isn't a bug here — it's the Hamburg
  sound." Pays off the `03d` switch as a creative decision.
  - **Demo home:** `wt-hiq-off-grit` — Hi-Q off, fast sweep, Fold up; the on-purpose grit.
- **`06d-mpe-position` — MPE: pressure scans the timbre (A, 60s).** With MPE enabled, route **Pressure
  → Position**; finger pressure scans the timbre per note — the per-note expressivity Aphex demanded
  from the Waldorf Iridium (2026 collaboration; confirmed, but no James quote and no confirmed
  released track — flag inline), available in Live.
  - **Demo home:** `wt-mpe-pressure-position` — a held chord, Pressure → Position, brightness rising
    per note with pressure.
  - **>> SIGNPOST into the exercise:** "One last thing, for the walk home." (Transition clip after
    `06d`.)
- **`06e-exercise` — Listener exercise (R, 90s).** Open Wavetable. Pick the most boring table — Basic
  Shapes. Hold one note and do nothing but modulate Position: an envelope, an LFO, your mod wheel,
  your finger pressure. No new notes, no filter sweeps. Make forty seconds of music where every change
  in the sound is a change in which waveform you're playing. If you can, you've understood Palm's 1978
  accident — that you don't have to filter a sound to make it move, you can walk between sounds. Same
  idea from the PPG choir to the Skrillex growl; only the rate of the walk is different. Pitch and
  timbre, separate dials. Walk the timbre. Then stop talking (no kicker).

---

## Gate 2 rubric — self-check

- [x] One-line **focus sentence** is writeable (above).
- [x] The piece has an **arc**: driving question (why is Position the only knob that matters?) +
      surprising payoff (the harsh accident Palm kept is the same gesture three decades over; the pad
      and the growl are one LFO-rate apart, proven by one macro).
- [x] **Anecdote** beats alternate with **reflection** beats (tagged A/R per beat; each act opens
      anecdote, lands reflection; no act runs >2 reflection beats without an anecdote — the ep1
      Section-4 fix, and Act 4 carries an explicit driving question instead of a feature list).
- [x] **Signposts** planted at every act boundary (`>> SIGNPOST`, mapped to the transition clips
      after `02e`, `03e`, `04f`, `05g`, `06d`).
- [x] Concept blocks ordered by "what do I need next for this to make sense?" — accident → 80s
      machine → grit-keeper → plugin inversion → Ableton; then what-it-is → additive → interpolation
      → aliasing → vs FM; then architecture → osc effects → matrix → modulators → filters/unison →
      vs Serum.
- [x] Each demo has a **conceptual home** in a block (noted inline; `wt-` = Wavetable render, bare
      ids = song clips, all to be resolved in `clip_manifest.yaml` after lock).

**Gate 2: PASS.** Cleared to scripting. Do not advance line-level work past a flatline list — this
is not one.

## Voice/lexicon flags for the Writer (enforce at draft)

- Cold-open is a **contradiction** (a failed filter kept on purpose), not a welcome. Hold this.
- Close is the **exercise then a stop**, no motivational kicker. Hold the line in `06e`.
- Keep caveats **inline** where they live (these are dossier flags — do not bury them):
  - **Skrillex (2010–11) is Massive + FM8, NOT Serum** (Serum = 2014) — lead with this in `02d`.
  - **No "deadmau5 built Serum" rationale quote exists** — attribute the design to **Steve Duda**.
  - **Bowie's PPG = *Tonight* (1984)**, credit only, no quote; **"Shout" = Fairlight**, not PPG;
    **Jarre's PPG link** is likely a misattribution (Jean-Benoît Dunckel confusion) — drop or flag.
  - **PPG filter chips** — phrase generically (CEM 3320 for Wave 2; SSM 2044 for 2.2/2.3); sources
    are loose.
  - **Tangerine Dream "White Eagle"** arpeggio is two Jupiter-8s; credit only the lead to the PPG.
  - **Autechre's** wavetable lineage is the **Ensoniq EPS transwave**, not PPG/Waldorf — frame the
    Loop-envelope move (`06b`) as the *idea*, not a hardware claim.
  - **Aphex × Waldorf Iridium** (2026) collaboration is confirmed, but **no James quote and no
    confirmed released track** — flag in `06d`.
- **Banned (hard fail):** journey / sonic journey, unleash, level up, game-changing/-changer,
  mind-blowing, magic happens, crafting sonic landscapes / sonic landscape, secret sauce, pro tips,
  synergy, AI-powered/-enhanced, unlock the power of, deep dive (noun), next-level, truly unique,
  really really / very very. Zero exclamation points, zero emojis.
