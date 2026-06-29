# e02-analog — Episode Summary

| | |
|---|---|
| **Episode** | `e02-analog` — *Analog: The Subtractive Foundation* |
| **Device** | Ableton **Analog** (AAS / UltraAnalog) — subtractive, VCO → VCF → VCA |
| **Status** | published |
| **Runtime** | ~45 min (target 40; six acts) |
| **Demos** | 23 device demos (`an-` prefix) + 14 song clips (5 foreground cues, 5 transitions, 4 beds) |
| **Primary artists** | Aphex Twin · Autechre · Squarepusher |
| **Adjacent genres** | acid house · Detroit techno · drum & bass |

**Focus sentence:** Subtractive synthesis is the art of controlling harmonics over
time by *taking away* — start with a rich source and carve what you don't want — and
"analog character" is just the imperfection a perfect digital model has to add back;
your hand on the cutoff knob is still the instrument.

**Driving question:** if the signal chain hasn't changed since Moog's 1964 modules,
why does the box that models it ship with a knob marked "Error"? **Payoff:** the −3 dB
cutoff, Q, and Barkhausen self-oscillation are the same objects from a filter lab; the
Reese, Juno pad, Supersaw, and PWM strings are one interference phenomenon; and the
only difference from Episode 1's FM "dwah" is topological — a modulator envelope vs a
filter envelope. **Refrain** (seeded in 01, echoed at each act boundary, landed in
06e): *"Start rich. Carve. Listen."*

---

## Table of Contents

1. [Act 1 — Cold Open](#act-1--cold-open)
2. [Act 2 — History & Theory](#act-2--history--theory)
3. [Act 3 — Synthesis Deep-Dive](#act-3--synthesis-deep-dive)
4. [Act 4 — Device Deep-Dive (Ableton Analog)](#act-4--device-deep-dive-ableton-analog)
5. [Act 5 — Patch Walkthrough: 303 → Reese](#act-5--patch-walkthrough-303--reese)
6. [Act 6 — IDM Application](#act-6--idm-application)
7. [Asset index](#asset-index)

---

## Act 1 — Cold Open
*Slide `01-cold-open` · ~90 s · anecdote → reflection*

A confession, not a welcome: in 1981 Roland built the TB-303 to replace a bass player,
it was bad at the job, and it was discontinued in three years and dumped secondhand for
the price of a pizza — until a few Chicago kids ignored the manual, turned the knobs
until it screamed, and named a genre after the noise. The act plants the cold-open MAP
(four stops: where it came from, the physics, the device, build acid + a Reese) and the
first instance of the refrain, so every later seam reads as "next stop," not non sequitur.

- **Songs:** `acid-tracks-cold-open` — Phuture, "Acid Tracks" (~1:27), the squelchy resonant 303 alone, under the open.
- **Key facts:** TB-303 released 1981, discontinued ~1984; acid house is named after the filter sound. Callback to Ep1 planted: "FM generated a spectrum from almost nothing; this starts with everything and sculpts."

## Act 2 — History & Theory
*Slides `02a`–`02f` · 8–9 min · 6 beats*

Ordered by "what do I need next for this to make sense?": define the chain → the
filter that gave it a voice → the rivals arguing about that filter → the fork we are
NOT taking → the box that made the filter a performance instrument → why we ended up
modeling all of it. **>> SIGNPOST into Act 3** (after `02f`): "Before we open the
device, the physics — because in subtractive synthesis the physics *is* the manual."

- **02a-silver-box** — *What subtractive means.* VCO → VCF → VCA; saw = every integer harmonic, so you start with everything and attenuate. The trichotomy: additive adds sines, FM generates sidebands, subtractive filters away.
- **02b-moog-ladder** — *Moog and the ladder filter (1964–71).* 1964 AES paper; Patent 3,475,623 (filed '66, granted '69); the 24 dB transistor ladder, exponential cutoff, self-oscillation; Minimoog (1970/71, $1,495, ~12,000 units — first synth sold in stores).
- **02c-filter-wars** — *ARP, Roland, Oberheim.* ARP 4012 "lawsuit filter" (threatened/settled, not cleanly sued); Roland IR3109; Oberheim state-variable SEM (LP/HP/BP/notch at 12 dB, no self-osc) — the closest ancestor of Analog's per-filter multimode selector.
- **02d-east-west** — *East vs West Coast.* Moog (keyboard, filter-centric) vs Buchla (no keyboard, waveshaping, low-pass gates). Named only to close the fork — we are firmly East Coast.
- **02e-tb303-acid** — *The TB-303 and acid house.* Kikumoto's bass box; the diode-ladder filter (caveat: 18-vs-24 dB and 3- vs 4-pole genuinely contested — Stinchcombe); accent + slide; the commercial failure; Phuture / DJ Pierre.
- **02f-virtual-analog** — *Why model analog at all.* Drift, cost, recall; Nord Lead 1995 ("first VA" contested — Korg Prophecy same year), Virus, JP-8000 Supersaw. Lands on: AAS got the job and called it Analog.

- **Songs:** `flash-light-bass` (Parliament, "Flash Light" — the rubber-band Minimoog bass, under 02b); `acid-tracks-303` (Phuture, a second longer Acid Tracks excerpt under 02e). Bed: `bed-flash-light`. Transition out: `trans-i-feel-love`.
- **Demos:** none rendered here — history beats lean on the record references.

## Act 3 — Synthesis Deep-Dive
*Slides `03a`–`03f` · 8–9 min · 6 beats*

The physics, motivated as an answer to the just-heard acid squelch: "we heard the
filter perform; for a physicist, what is it doing to the harmonics?" Ordered: what the
source contains → how the filter removes it → the extreme → why two sources make "fat"
→ how brightness decouples from loudness → how to dirty it. **>> SIGNPOST into Act 4**
(after `03f`): "That is the whole physics. Now the one device that puts every one of
those knobs in front of you, one-to-one."

- **03a-oscillator-spectra** — saw (all harmonics, 1/n), square (odd, 1/n), pulse/PWM (sinc nulls move with duty cycle); Analog has no triangle. Demo `an-pwm-sweep` (PW → harmonic content; even harmonics appear).
- **03b-filter-physicist** — poles ↔ slope (6 dB/oct per pole); cutoff = the −3 dB half-power point; resonance = Q = feedback. Demo `an-slope-12-vs-24` (filter slope → darkness above cutoff).
- **03c-self-oscillation** — Barkhausen condition, loop gain → 1, pole pair on the imaginary axis; the filter becomes a sine oscillator. Plants Digeridoo (paid off in 06a). Demo `an-reso-to-self-osc` (resonance → self-oscillation).
- **03d-beating-pwm** — two near-equal sines beat at Δf; cents-detune ⇒ beating accelerates with pitch; PWM = one osc behaving like two. "Fat is interference" — the loudest single idea. Demos `an-reese-detune-sweep` (detune → beating) and `an-pwm-strings` (LFO→PW = one osc like many).
- **03e-two-envelopes** — amp env = loudness, filter env = brightness. The explicit Ep1 callback: in FM the modulator's envelope *was* the brightness; here it's a separate filter envelope — same "dwah," opposite topology. Demo `an-filter-env-vs-amp-env` (same env, two destinations).
- **03f-drive** — symmetric (odd harmonics) vs asymmetric (even); the difference between a digital sweep and an analog one is the distortion you can't hear until it's gone. Demo `an-drive-sym-vs-asym`.

- **Songs:** bed `bed-i-feel-love` (Donna Summer/Moroder pulse under the theory). Transition out: `trans-flash-light`.
- **Key facts:** Barkhausen unity-gain self-oscillation; −3 dB cutoff; Q = resonance = feedback; PWM and Reese are the same interference physics.

## Act 4 — Device Deep-Dive (Ableton Analog)
*Slides `04a`–`04f` · 8–9 min · 6 beats*

The Ep1 Section-4 fix: a single live question pulls the whole tour — "AAS had to fold
the entire subtractive canon (Moog, ARP, Roland, Oberheim, the MS-20) into one device,
then make a perfect digital model sound imperfect. What did they KEEP, what did they
ADD that no vintage synth had, and where do they hide the imperfection?" Every beat is
an answer. **>> SIGNPOST into Act 5** (after `04f`/`05i`): "Enough touring the panel.
Build the one bass sound this whole instrument is secretly about — twice."

- **04a-origin** — AAS, IRCAM roots, Tassman/Ultra Analog physical modeling; shipped with Live 7 / Suite, Nov 2007 (caveat: not Live 4/5). Every control maps onto the textbook.
- **04b-error-thesis** — no samples, no wavetables: circuit equations solved every sample, alias-free. The Error knob is the thesis — a perfect model of an imperfect machine sounds wrong until you add the imperfection back. Demo `an-error-drift` (Error → per-voice tuning drift).
- **04c-oscillators** — four shapes (sine/saw/rect/noise, no triangle), PW + PWM, Sub an octave down, Detune ±300 c, F1/F2 routing balance, the noise generator, Sync. Demo `an-sync-ratio-sweep` (hard-sync ratio → the screaming lead).
- **04d-two-filters** — LP/HP/BP/Notch/Formant in 12 or 24 dB, per filter; series vs parallel (To F2, Slave); Formant = vowels on the Reso knob; Drive Sym/Asym. Demo `an-ms20-series-filter` (resonant HP → resonant LP series).
- **04e-envelopes-lfos** — four ADSRs (two filter, two amp), Free (percussive) and Loop modes, S.Time; two LFOs with delay/attack, free-run vs retrig; Vibrato as a hardwired third LFO. *Inventory beat, kept short.*
- **04f-voice-architecture** — two sub-voices per note; split-filter timbres, stereo voices, Unison (2/4 + Detune = a supersaw). The make-it-analog stack: Error + Asym Drive + free-run LFOs + Detune. Demo `an-unison-supersaw` (unison + detune → JP-8000 Supersaw).

- **Songs:** bed `bed-can-you-feel-it` (Mr. Fingers Juno-60 pad). Transition out: `trans-acid-tracks` (leads into the 303 build).
- **Key facts:** Analog shipped with Live 7 / Suite, Nov 2007; physical-modeling (no samples/wavetables), alias-free; Error = random per-voice detune; Unison max = 4 voices (an honest partial stand-in for the JP-8000's 7-saw Super Saw).

## Act 5 — Patch Walkthrough: 303 → Reese
*Slides `05a`–`05i` · 5–6 min · 9 steps*

One arc: build a 303 acid line from the default patch, then morph the *same* patch into
a Reese without loading a new device. The payoff is the morph — two genres a parameter
apart. Progress markers ("step 3 of 9", "halfway — now Bristol 1994") keep it from
feeling open-ended. **>> SIGNPOST into Act 6** (after `05i`): "Two basses out of one
device. Now three IDM moves that come from pushing the same filter past polite."

- **05a-default** — Voices = Mono, Glide = Const (short) + Legato, OSC1 = saw, OSC2/Sub off. Demo `an-303-step1` (the raw source).
- **05b-lowpass** — F1 = LP 24, route OSC1 fully to F1, mid cutoff, Reso ~40%. Demo `an-303-step2` (the carve begins).
- **05c-filter-env** — `F1 Freq < Env` high, short `FEG1 Decay`, Sustain ≈ 0 — the per-note wow. Demo `an-303-step3`.
- **05d-resonance** — Reso up to ~80%; the squelch sharpens toward self-oscillation. Demo `an-303-step4`.
- **05e-drive-accent** — Drive = Asym2 for dirt; `FEG1 < Vel` up so accented (high-velocity) notes open brighter — the accent. Demo `an-303-step5`.
- **05f-automate** — program a 16th line with slid notes; automate `F1 Freq` across the loop. "That's acid: a saw, a resonant low-pass, and your hand on the cutoff." Demo `an-303-step6` (adds `AMP1 Level = 0.85`).
- **05g-morph-reese** — OSC2 on (saw), Detune +18 c, Sub on, drop the filter envelope, lower the cutoff. Demo `an-reese-morph` (the pivot).
- **05h-detune-listen** — hold a low note; the saws beat with no LFO; beating accelerates with pitch. Chicago 1987 → Bristol 1994 is one parameter. Demo `an-reese-final` (canonical Reese = two detuned saws, no sub).
- **05i-save** — save as "Subtractive-303-Reese." Two of the most influential bass sounds from one default patch. Demo `an-303-reese-final` (A/B `concat_from` step6 + reese-final).

- **Songs:** transition out `trans-tri-repetae` (into the IDM act).
- **Key facts:** Reese named for Kevin Saunderson ("Just Another Chance", 1988) — two detuned saws beating, not a sub osc; constant-cents detune ⇒ Δf (beat rate) doubles per octave; the 303 and the Reese are one device, two presets.

## Act 6 — IDM Application
*Slides `06a`–`06e` · 5–6 min · 5 beats*

Ordered: the most extreme filter trick → the dual-filter abuse → rhythm from an
envelope → the unifying principle → the exercise. Closes on an exercise, not a kicker
(voice rule). The payoff lands in 06e: restate the focus sentence and the refrain as
resolution, not a new thought.

- **06a-self-oscillation** — oscillators off, Reso near max, LP 24, Filter Freq key-tracked → play the self-oscillating filter as a synth, LFO → Freq for the drone. Pays off the 03c plant: there is no didgeridoo; Aphex worked it out at 19. Demos `an-digeridoo-drone` (the Analog rebuild — noise-excited high-Q key-tracked filter) and `digeridoo-clip` (the record).
- **06b-ms20-abused** — HP→LP series, both resonant, swept against each other; run into bitcrush + short reverb. The Autechre move: analog filters past politeness, then degraded with cheap digital gear. Demos `an-ms20-scream` (rebuild — opposed-cutoff sweeps) and `tri-repetae-clip` (the reference).
- **06c-loop-envelopes** — filter env to Loop (AD-R), tempo-ish rate → an evolving rhythmic pulse from one held note. No LFO, no sequencer — the envelope is the rhythm. Demo `an-loop-env-pulse`.
- **06d-fat-principle** — Unison 4 + Detune (supersaw), PWM (string pad), two detuned saws (Reese) — all the same trick: copies of a wave that almost agree. The reflection that ties the episode to the focus sentence.
- **06e-exercise** — build the 303, then do what Phuture did: don't program it — turn cutoff and resonance by hand over a loop until the filter sings. When it does, you've found unity gain — the Barkhausen condition — by ear. *"Start rich. Carve. Listen."* Then stop (no kicker).

- **Songs:** foreground references `digeridoo-clip` (Aphex, "Digeridoo") and `tri-repetae-clip` (Autechre); bed `bed-tri-repetae`. Transition before the exercise: `trans-can-you-feel-it`.
- **Key facts:** Analog's filter will NOT self-oscillate from bare resonance with the oscillators off — the Digeridoo rebuild excites a high-Q key-tracked filter with NOISE so the pitched drone is provably the filter; looping envelope = rhythm with no LFO/sequencer (the ep1 rhythmic-demo lesson); fat is interference.

---

## Asset index

**Device demos (23, `an-` prefix)** — each has a click-by-click rebuild in
`tutorials/<id>.md` and a preset to save per `presets/SAVE_CHECKLIST.md`:

| Act | Demos |
|---|---|
| 3 | `an-pwm-sweep` · `an-slope-12-vs-24` · `an-reso-to-self-osc` · `an-reese-detune-sweep` · `an-pwm-strings` · `an-filter-env-vs-amp-env` · `an-drive-sym-vs-asym` |
| 4 | `an-error-drift` · `an-sync-ratio-sweep` · `an-ms20-series-filter` · `an-unison-supersaw` |
| 5 | `an-303-step1` … `an-303-step6` · `an-reese-morph` · `an-reese-final` · `an-303-reese-final` |
| 6 | `an-digeridoo-drone` · `an-ms20-scream` · `an-loop-env-pulse` |

**Song clips (14)** — copyrighted; cited, not committed:

- *Foreground (5):* `acid-tracks-cold-open`, `flash-light-bass`, `acid-tracks-303`, `digeridoo-clip`, `tri-repetae-clip`
- *Transitions (5):* `trans-flash-light`, `trans-i-feel-love`, `trans-can-you-feel-it`, `trans-acid-tracks`, `trans-tri-repetae`
- *Beds (4):* `bed-flash-light`, `bed-i-feel-love`, `bed-can-you-feel-it`, `bed-tri-repetae`

Source tracks: Phuture "Acid Tracks" (1987) · Parliament "Flash Light" (1978) ·
Aphex Twin "Digeridoo" (1992) · Autechre / Tri Repetae-era (1995) · Donna Summer
"I Feel Love" (1977) · Mr. Fingers "Can You Feel It" (1986).
