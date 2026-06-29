# Fresh-Ears — Harness Contribution Report

**Role:** isolated, no-prior-context Fresh-Ears Reviewer (Gate 5 table-read + Gate 10 cold listen).
**What this report actually is — read this first (honesty mandate):** I performed a **cold script read**
of the locked scripts, as the audience would *hear* them in their head, file by file in slide order. I
**did not** listen to any audio. I cannot hear the rendered MP3s, so I cannot run the true cold-window
test (item 17) on real sound, cannot judge whether a demo is loudness-matched, whether the bed is muted,
or whether the named percept actually arrives within ¼ s of the cue. **A genuine Gate-10 audio listen has
not happened.** Everything below is a Gate-5-style prediction of where a first-time *listener* would lose
the thread, inferred from the words and cue placements on the page. Treat the demo-audibility findings as
"flagged for the audio pass," not "cleared."

---

## 1. Readiness (Gate 5/10) per episode

### EP1 — Operator (the published re-cut)

**Verdict: it no longer reads as a mess.** The re-cut's two structural devices carry a cold reader through
cleanly:

- **The four-stop map**, planted in `01-cold-open.md` ("Where this sound came from, how it works, the one
  device, and how to build Aphex and Autechre yourself"), is then *explicitly* re-announced at every act
  boundary: `03a-equation.md` opens "That's stop one… So: stop two." `04a-origin.md` opens "Stop three:
  the device." `05a-algo1.md` opens "Stop four — the one you do with your hands." A cold reader always
  knows which of four rooms they are standing in. This is the single biggest fix and it works.
- **The repeated spine line** — "Same equation, different decisions" — lands in the cold open, in 03a,
  03c, and the outro. It gives the episode a refrain a first-timer can hold onto, and the final
  `06e-exercise.md` payoff (the actual equation spoken aloud, then the refrain, then "That's everything")
  is a genuinely earned close.
- **The "keep this question in your hand" device** in act three (`04a`: "what do you keep from Chowning,
  what do you cut, what do you add?") gives the device-tour a through-line so it doesn't read as a
  feature list. 04e/04f explicitly tag themselves "the *added* column," which keeps the reader oriented.

**Remaining seams I'd still flag (Gate 5):**

- **`02c-american-failure.md` → `02d-yamaha-license.md` ordering jolt.** 02d ("Stanford's licensing
  office took FM on the road… starting nineteen seventy-one… all said no") chronologically *precedes* the
  successful Yamaha meeting in 02d-yamaha (1973). But 02c already covered the tenure denial and CCRMA
  founding "around the time the Yamaha deal was coming together." Cold-reading straight through, I hit a
  small "wait, are we before or after the deal?" wobble across 02c→02d. The dates are all correct; the
  *narrative* time-arrow stutters. Minor, but it's the one place the history act doubles back on itself.
- **`03f-4op-vs-6op.md` ends on a forward-reference that a cold listener can't yet cash:** "Hold onto
  that one: it's the seam where the math stops being physics and starts being one specific device." Good
  signpost — but it sits at the end of *stop two* and points into *stop three*, while the same paragraph
  is still mid-explaining workarounds (loop modes, LFO routing). The beat is doing two jobs at once
  (closing the math, teasing the device) and on a cold read the tease slightly buries the close.
- **`04d-envelopes.md` "seven envelopes total per voice."** This is the densest single beat in the
  episode — seven envelopes, ADSR-plus-four-levels, draggable curves, then five loop modes, all before
  the first demo (`an-ending-pad`). A cold listener's working memory is full before any sound arrives. I
  flag it not as wrong but as the most likely **boredom/overload point** in act three.
- **Cold-window risk I cannot clear without audio:** several cues in act two fire in tight succession in
  `03c-ratios.md` — five ratio demos (`op-ratio-1to1` … `op-ratio-1-phi`), then `stria-excerpt-2`, then
  `xtal-bell`, with only a one-line frame each. On the page the *frame-then-demo* discipline is present
  (each ratio is named before its cue), so it should pass — but five demos plus two music excerpts in one
  file is exactly the "≤4 demos per concept block" pressure point, and whether each 10-second window
  reads as "THE example" depends entirely on the bed being muted and the levels matched. **Routed to the
  audio pass.**

### EP2 — Analog (lighter pass)

Reads clean and is arguably the **most disciplined cold open** of the three. `01-cold-open.md` does
something the others should copy: it explicitly bridges from the prior episode ("In the last episode, FM
generated a whole spectrum out of almost nothing… This is the opposite philosophy. You begin with
everything and you sculpt"). That contrast gives a returning listener instant orientation and a new
listener a clean mental model. The "Error knob" mystery is planted in the cold open and paid off in
`04b-error-thesis.md` — a textbook raise-a-question/answer-it arc. Same four-stop map, same act
signposts. The "start rich / carve / listen" refrain mirrors ep1's spine line and closes the episode.
**No structural seams flagged on the read.**

### EP3 — Wavetable (lighter pass)

Also clean. The spine phrase "Pitch and timbre, separate dials. Walk the timbre" is planted in the cold
open and paid off in the outro, and the "Position" mystery is the magic-knob hook. `03e-wavetable-vs-fm.md`
does the same prior-episode callback ep2 does, and the `wt-fm-inside-wavetable` demo is a clever literal
bridge between episodes. **One Gate-5 note:** `04a-architecture.md` front-loads a long inventory — "194
tables across twelve categories" then names all twelve. That is the same overload shape as ep1's 04d; a
cold listener will not retain the list, and reading it aloud is a tongue-load. Flag for trimming.

---

## 2. Where a cold listener would get confused or bored — concrete moments

- **EP1 `02d-yamaha-license.md`, closing line:** "Yamaha now runs the synth division of Yamaha." On a
  cold *read aloud* this parses as a typo/tautology ("Yamaha runs Yamaha"). I assume the intent is a
  contrast (the engineer who said yes vs. the companies who said no), but as written it stops the reader.
  **Confusion flag.**
- **EP1 `03c-ratios.md`, final paragraph (the *Xtal* caveat):** the pivot "the pad underneath that bell
  is not FM at all… trust the lead, learn from the pad" is conceptually rich but arrives *after* five
  ratio demos and a Stria excerpt. It asks the listener to hold "this demo teaches two things at once"
  at the most fatigued point of act two. **Boredom/overload flag.**
- **EP1 `04d-envelopes.md`:** seven-envelopes density wall (see above). **Overload flag.**
- **EP1 `04e-lfo.md`, "This is how you escape the eleven-algorithm prison."** "Prison" arrives as a
  metaphor the listener wasn't told they were in — the constraint was framed as "the added column," not a
  prison. Minor tonal seam.
- **EP3 `04a-architecture.md`:** the twelve-category table list (see above). **Boredom flag.**
- **General, all three:** the device-tour acts (section 04 across every episode) are where attention is
  thinnest — lots of named parameters, fewer demos. This is inherent to the format, but it's the
  predictable sag in every episode and worth watching in the audio pass for pacing.

---

## 3. What I'm proud of / what I actually did

I read **35 ep1 script files end to end** plus the structural seams (cold open, act transitions, build
opener, outro, and one mechanics beat) of ep2 and ep3 — as a true cold read, no outline, no dossier, no
demo specs, the way the isolation mandate requires. I caught the one genuine **narrative time-arrow
stutter** in the ep1 history act (02c↔02d) and the one **parse-stopping line** ("Yamaha runs Yamaha")
that a maker who knows the intent would read straight past — which is exactly the tape-loop-interrupter
blind spot this role exists to catch.

**What I did NOT do, and you should not pretend I did:** I did not listen to a single second of audio. I
cannot confirm any demo passes the real cold-window test, cannot confirm beds are muted under demos,
cannot confirm the named percept ("listen to the even harmonics arrive," "that metallic buzz") is
actually audible and on-time. **Gate 10 remains open.** This report discharges a Gate-5 table-read only.

## 4. Concerns — the single biggest listener-experience risk per episode

- **EP1 (Operator):** the act-three device tour (`04c`/`04d`) is a **density wall** — it front-loads more
  named parameters and envelope theory than a first-time listener can hold before a demo rewards them.
  The four-stop map saves the macro-structure; the micro-pacing inside stop three is the risk.
- **EP2 (Analog):** lowest structural risk of the three. The only real exposure is whether the **`Error`
  / drift demos are audibly different on phone speakers** — the whole thesis rests on a *subtle* drifting
  chorus being perceptible, and that is unverifiable until the audio pass. If it's too subtle, the
  episode's central argument doesn't land sonically.
- **EP3 (Wavetable):** the entire episode hinges on **one demo** — `wt-position-by-hand`, explicitly
  called "the single most important demo in the episode" — proving that pitch holds while timbre walks.
  If that one cold window doesn't unambiguously read as "pitch fixed, tone moving," the spine phrase
  collapses. Highest single-point-of-failure dependency on an unheard demo of the three.

**Bottom line:** all three scripts **pass the Gate-5 table-read** for through-line and signposting (ep1's
re-cut is genuinely fixed), with the small flags above routed back via the Story Editor. **Gate 10 is not
discharged** — a real cold audio listen still has to happen, and the demo-audibility concerns above are
where I'd point it first.
