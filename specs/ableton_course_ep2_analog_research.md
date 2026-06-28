# Analog: The Subtractive Foundation — Episode 2 Research Dossier

A complete research artifact for a ~40-minute walking podcast aimed at an experienced Ableton Live 12 Suite user who is also a physicist and IDM producer. Six sections, ~7,000 words of dense research, designed to be cut directly into a script. This is the companion to the Episode 1 dossier on Operator/FM; where Episode 1 was *additive-by-sideband* (build a spectrum from nothing), Episode 2 is its conceptual inverse: *subtractive* — start with a harmonically rich waveform and **carve away** what you don't want with a filter.

Every nontrivial claim carries a full-URL citation inline. Conflicts and uncertainties are flagged explicitly throughout and gathered at the end. Where Ableton **Analog** differs from a real analog synth — and it differs in important, instructive ways — it is flagged with **[VA vs HW]**.

---

## SECTION 1 — Ableton Analog: Full Parameter Reference (Annotated)

Analog is **a virtual-analog synthesizer built on physical modeling, created in collaboration with Applied Acoustics Systems (AAS)** of Montreal. The Ableton manual is explicit and this is the single most important framing fact for the whole episode: *"Analog generates sound by simulating the different components of the synthesizer through physical modeling … uses no sampling or wavetables; the sound is simply calculated in real time by the CPU"* — the mathematical equations describing how the analog circuits behave are solved every sample ([Ableton manual: Analog](https://www.ableton.com/en/manual/live-instrument-reference/)). It is **not a sampler-ROMpler and not a model of one specific vintage synth** — it "combines different features of legendary vintage synthesizers into a modern instrument" ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)).

**Origin and lineage.** AAS was founded in 1998 by Marc-Pierre Verge and Philippe Dérogis, PhD-level researchers out of the IRCAM tradition; their flagship modular environment **Tassman** (2000) pioneered the physical-/analog-modeling hybrid, and their **Ultra Analog** engine is the technology licensed into Ableton's Analog ([Sound on Sound: AAS Ultra Analog](https://www.soundonsound.com/reviews/aas-ultra-analog); [Vintage Synth Explorer: Tassman](https://www.vintagesynth.com/applied-acoustics/tassman)). **[FACT-CHECK]** Analog did **not** ship with Live 4 or Live 5. It **debuted with Ableton Suite alongside Live 7 on 29 November 2007**, in the same Suite-bundle wave as Electric and Tension (also AAS-derived) ([Ableton press: Live 7 / Suite](https://www.ableton.com/en/press/press-archive/press-archive-release-7/); [Sound on Sound: Ableton announces Live 7 + Suite](https://www.soundonsound.com/news/ableton-announces-live-7-new-add-instruments-and-ableton-suite)). This is the cleanest contrast with Operator (a 2005, Henke-built, in-house FM machine): **Operator is Ableton's own; Analog is licensed AAS physical modeling.**

**Signal flow.** Two oscillators plus a noise generator → two multimode filters (routable in **series or parallel**) → two amplifiers ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). The "two of everything, freely cross-routable" architecture is the defining feature versus a classic mono synth; think of it as **two semi-independent synth voices that share oscillators**, which is what makes split routings (osc 1 → filter 1, osc 2 → filter 2, panned hard) possible.

### 1.1 Oscillator section (OSC1, OSC2 — identical controls)

| Parameter | Behaviour |
|---|---|
| **On** | Engages the oscillator. |
| **Shape** | **[KEY PARAM]** Selects waveform: **sine, sawtooth, rectangular (pulse/square), and white noise** ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). Note: only four shapes — no triangle. This is a *deliberately classic* East-Coast oscillator palette; the harmonic content is entirely conventional (see §5.1). **[VA vs HW]** Because the oscillators are physically modeled and **alias-free**, the saw/square stay clean at the top of the keyboard where a naive digital oscillator would alias — but they also lack the subtle drift and waveform asymmetry of a real VCO unless you add it deliberately via the global **Error** control (§1.6). |
| **Pulse Width (PW)** | **[KEY PARAM]** Active only when Shape = rectangular. Sweeps the duty cycle from very narrow ("tinny/pinched," strong even harmonics) to 100% (a perfect square = odd harmonics only) ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). **PW is modulatable by LFO → this is PWM**, the single most important "fat analog" trick (see §5.3). |
| **Octave / Semi / Detune** | Pitch. Octave = octave transposition; Semi = semitone steps; **Detune = ±300 cents** continuous ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). **[KEY PARAM]** Detuning OSC2 a few cents from OSC1 produces beating — the foundation of the Reese bass and of any "fat" two-oscillator patch (§3, §4). |
| **F1 / F2 (balance slider)** | **[KEY PARAM]** Routes this oscillator's output between Filter 1 and Filter 2 — a continuous balance, not a switch. This is how you build a split-filter voice (e.g., OSC1 fully to F1, OSC2 fully to F2). |
| **Key (key tracking)** | How much oscillator tuning follows MIDI note pitch. **Default 100% = conventional equal-tempered scale**; lower values flatten the keyboard's pitch response (0% = fixed pitch regardless of note — useful for tuned drones / drum tones) ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). |
| **Pitch Env (Initial / Time)** | Per-oscillator pitch envelope: **Initial** sets the starting pitch offset, **Time** sets how long the pitch glides to its final (played) value ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). Short Time + large Initial = the "blip/zap" attack chirp; long Time = a slow tape-like pitch slide. |
| **Sub (Level)** | **[KEY PARAM]** Adds a **sub-oscillator one octave below**. Its waveform follows the main Shape: **square when the main osc is rectangular or sawtooth; sine when the main osc is sine** ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/); [Ableton/Lynda: Analog's hidden sub and sync](https://www.linkedin.com/learning/learning-ableton-analog/analog-s-hidden-sub-and-sync-oscillators)). This is the analog-bass weight knob — adds fundamental energy an octave down without a second oscillator. |
| **Sync (Mode + Ratio)** | **[KEY PARAM]** When Mode = Sync, **the audible oscillator's waveform is hard-restarted by an internal (inaudible) oscillator whose frequency is set by the Ratio slider.** Raising Ratio increases the internal rate, which reshapes the harmonic content — the classic "sync sweep" tearing/formant sound ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). Ableton's own tip: *"For maximum analog nastiness, try mapping a modulation wheel … to the Sync ratio"* — sweeping Ratio gives the screaming sync lead (Cars/The Cars/prodigy-style). **[VA vs HW]** Modeled hard sync, alias-free; on hardware sync sweeps often alias audibly, which is part of their grit — here it stays clean. |

**Noise generator.** A dedicated white-noise source feeds the filters in parallel with the oscillators (per the signal-flow description) ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). Essential for breath, wind, hi-hats, and filtered-noise percussion (the "I Feel Love" hi-hat trick of §3).

### 1.2 Filter section (FIL1, FIL2 — the heart of subtractive synthesis)

Two **independent multimode filters**, each selectable from: **2nd-order and 4th-order low-pass, band-pass, notch, high-pass, and formant** filters ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). 2nd-order = **12 dB/oct (2-pole)**; 4th-order = **24 dB/oct (4-pole)** — see §5.2 for why slope matters.

| Parameter | Behaviour |
|---|---|
| **Type** | LP/BP/Notch/HP each in 2nd or 4th order, plus **Formant**. **[VA vs HW]** This is far more flexible than any single vintage synth: a Minimoog only has a 24 dB LP; the Oberheim SEM only has a 12 dB state-variable; Analog gives you all of them per filter. The closest hardware analog to Analog's "two multimode filters" concept is the Oberheim SEM's state-variable design (§2) and the Korg MS-20's dual HP→LP design (§3). |
| **Freq** | **[KEY PARAM]** Cutoff frequency. The single most-automated control in subtractive synthesis — the "filter sweep" knob. |
| **Reso** | **[KEY PARAM]** Resonance: boosts a peak at the cutoff by feeding output back to input. At high settings the filter **self-oscillates into a near-sine at the cutoff** (§5.2). **In Formant mode, Reso instead cycles through vowel sounds** (ah/eh/ee/oh/oo) rather than setting a peak ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/); [Ableton forum: Analog's formant filters](https://forum.ableton.com/viewtopic.php?t=246278)). |
| **Drive (Sym / Asym / Off)** | **[KEY PARAM]** Selectable saturation at the filter. **Three Sym options apply symmetrical distortion; Asym modes apply asymmetrical saturation; higher numbers = more distortion** ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). **[VA vs HW]** This is the device's deliberate re-introduction of analog non-linearity. Symmetrical drive ≈ odd-harmonic (square-ish) clipping; asymmetrical ≈ adds even harmonics (more "tube/transformer" character). On real hardware this nonlinearity is intrinsic to the VCF and unavoidable; here it's an explicit, dialable stage. |
| **To F2** (Filter 1 only) | **[KEY PARAM]** Sets how much of Filter 1's output passes to Filter 2 — the **series-routing amount**. Full = strict series (F1 → F2 in cascade, slopes add); zero with both oscillators feeding both filters = parallel. |
| **Follow** (Filter 2 only) | Makes Filter 2's cutoff **track Filter 1's cutoff**, so one Freq knob sweeps both — useful for keeping a series LP→LP or HP→LP pair locked together ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). |
| **Freq Mod / Res Mod** | Independent modulation of cutoff and resonance by **LFO, note pitch (key tracking), and envelope** — each with its own amount ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). The **envelope → Freq** routing is the filter-envelope sweep that makes plucks, wahs, and the 303 "wow." |

**Routing (series vs parallel).** Quick-routing buttons set the topology ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)):
- **Series:** OSC → Filter 1 → (To F2) → Filter 2 → amp. Cascading two 24 dB LPs gives a steeper, more aggressive 48 dB-ish slope; HP→LP in series = a **bandpass with independent edges** (the MS-20 trick).
- **Parallel:** OSC → Filter 1 → amp 1 and OSC → Filter 2 → amp 2 separately. Two independent timbres summed (e.g., a bright BP layer + a dark LP layer).

### 1.3 Amplifier section (AMP1, AMP2)

Each filter feeds its own amplifier ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)):

| Parameter | Behaviour |
|---|---|
| **Level** | Output volume of that amp/voice path. |
| **Pan** | Stereo position of that path. **[KEY PARAM]** Hard-panning AMP1 left and AMP2 right, with each fed by a differently-detuned/filtered oscillator, gives a true stereo synth voice (a built-in unison-spread). |
| **Pan Mod / Level Mod** | Pan and Level can each be **independently modulated by LFO, note pitch, and the amp envelope** ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). LFO → Pan = auto-pan; LFO → Level = tremolo. |

### 1.4 Envelopes (4 total: 2 filter + 2 amp — identical ADSR controls)

Analog has **four ADSR envelopes** with identical controls: **two amp envelopes and two filter envelopes**, one of each per signal path ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). **[VA vs HW]** Four envelopes is generous for a "vintage" synth — a Minimoog had effectively one-and-a-bit (a contour generator shared between filter and loudness); Analog gives each of its two voices a dedicated filter AND amp envelope, so you can have a fast filter pluck on one voice and a slow pad swell on the other simultaneously.

| Parameter | Behaviour |
|---|---|
| **Attack / Decay / Sustain / Release** | Standard ADSR. **A/D/R are times; S is a level.** |
| **Att < Vel** | Velocity modulates **attack time** (harder = different attack) ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). |
| **Env < Vel** | Velocity modulates **overall envelope amount** — the standard "harder = louder/brighter" routing (on a filter env this is velocity → brightness). |
| **S.Time (Sustain Time)** | A decay applied to the **sustain stage while the key is still held** — i.e., the sustain level itself slowly falls. Lets you make held notes decay like a struck/plucked instrument without releasing the key. |
| **Slope (Linear / Exponential)** | Per-envelope toggle between **linear and exponential** segment shapes ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). Exponential decays sound more natural/"analog" (matches RC discharge curves); the manual's own example uses **Formant filter + EXP envelope for a rounded "wow" attack** ([Studio Brootle: Analog tutorial](https://www.studiobrootle.com/ableton-analog-tutorial/)). |
| **Legato** | A new note played while another is held **continues the first note's envelope at its current position** rather than retriggering — essential for smooth mono leads and 303-style slides ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). |
| **Free** | **[KEY PARAM]** Bypasses the sustain phase entirely → notes have **equal, fixed duration regardless of how long the key is held** (one-shot/percussive trigger) ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). The percussion/drum-tone switch. |
| **Loop (Off / AD-R / ADR-R / ADS-R)** | **[KEY PARAM]** Envelope looping. **AD-R** loops attack-decay (an LFO-like cycling envelope); **ADR-R** and **ADS-R** loop with release segments included ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). A looping filter envelope is a free, tempo-independent rhythmic filter wobble — the IDM glitch-pulse tool. **[VA vs HW]** No vintage subtractive synth had looping envelopes; this is a modern affordance closer to a modular's cycling EG. |

### 1.5 LFO section (LFO1, LFO2)

Two independent LFOs, usable as modulation sources for **oscillators, filters, and amplifiers** ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)):

| Parameter | Behaviour |
|---|---|
| **On** | Toggles the LFO. |
| **Waveform** | **Sine, triangle, rectangle, and two types of noise (smooth/stepped random)** ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). Stepped noise = sample-and-hold random (the "computer bleep / random pitch" source). |
| **Rate (+ Hz/sync toggle)** | Speed, switchable between **Hz (free)** and **tempo-synced beat divisions** ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). |
| **Width** | Pulse width of the LFO shape (triangle/rectangle only) — skews the waveform (e.g., ramp vs triangle). |
| **Delay / Attack** | LFO onset: **Delay** = time before the LFO starts after note-on; **Attack** = fade-in time of LFO depth. Together they produce **delayed vibrato** (the human "let the note settle, then add vibrato" gesture). |
| **Retrig** | Phase restart per note (on) vs free-running (off). **[VA vs HW]** Free-run = each note catches the LFO at a different phase, the "analog looseness"; retrig = tight, repeatable modulation. |
| **Offset** | Starting phase of the LFO. |

### 1.6 Global / Keyboard section

| Parameter | Behaviour |
|---|---|
| **Volume** | Master output. |
| **Vibrato** | **[KEY PARAM]** Essentially a **third LFO hardwired to the pitch of both oscillators**, with Rate, Delay, Attack, **Error**, and **Amt < MW** (mod-wheel depth) ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). Dedicated vibrato is a classic performance feature (cf. Minimoog osc-3-as-LFO). |
| **Unison (Voices 2/4 + Detune + Delay)** | **[KEY PARAM]** Stacks **2 or 4 voices per note**, spread by **Detune**, with optional **Delay** between voice onsets ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). This is the supersaw/Reese-machine knob — multiple detuned copies = thick, chorusing unison. |
| **Glide (Const / Prop + Legato)** | Portamento between notes; **Const** = fixed glide time regardless of interval, **Prop** = proportional to interval size; Legato option restricts glide to overlapping notes — the 303-slide behavior ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). |
| **Octave / Semi / Detune (global)** | Master tuning, **Detune ±50 cents**. |
| **Stretch** | **[KEY PARAM] [VA vs HW]** **Stretch tuning** — raises the pitch of upper notes and lowers lower notes, simulating piano-style inharmonic stretch tuning ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). A modeling nicety with no analog-synth precedent. |
| **Error** | **[KEY PARAM] [VA vs HW]** **Random per-voice tuning deviation.** This is the single most important "make it sound analog" control: it deliberately re-injects the VCO drift/instability that the alias-free physical model otherwise lacks. Small Error = subtle warmth; large Error = drunk, detuned, vintage-broken character. **The thesis of the whole instrument lives in this knob:** a perfect digital model has to *add back* the imperfection that made analog sound alive. |
| **Voices / Priority (High/Low/Last)** | Polyphony cap and voice-stealing logic. Voices=1 + Glide = mono lead. |
| **PB Range** | Pitch-bend range in semitones. |
| **MPE (Pressure / Slide / per-note pitch)** | Three MPE sources, each with routable destination and amount ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). Added in the modern (Live 11/12) MPE era. |

### 1.7 How Analog differs from a real analog synth — the consolidated "[VA vs HW]" list

1. **No aliasing.** Oscillators and filters are physically modeled and band-limited; a real VCO's saw aliases nowhere, but a *naive digital* one does — Analog sits between, sounding clean by design ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)).
2. **Perfect stability → you must add instability.** Real VCOs drift with heat and age; Analog is dead-stable until you dial in **Error** (random per-voice detune) and **Vibrato Error**. The imperfection is a feature you opt into.
3. **No specific-chip character.** It is not a Moog-ladder model or a 303-diode-ladder model — it's a *generic, clean* multimode filter set. It will not self-distort with the exact Moog "growl" or the 303 "squelch dirt" unless you add **Drive** and push **Reso** hard. (Compare Operator's Cytomic filters, which *do* model specific circuits — OSR/MS2/PRD — making Operator's filter arguably more "vintage-flavored" than Analog's.)
4. **Two full multimode filters + four envelopes + two LFOs** exceed almost any single vintage mono/poly synth; Analog is a *composite* of the tradition, not a clone of one machine.
5. **Modern affordances:** looping envelopes, tempo-synced LFOs, stretch tuning, MPE, total recall — none of which existed on the 1970s–80s hardware it evokes.

### 1.8 Analog vs Operator vs other softsynths (quick map)

| | **Analog** (VA, subtractive) | **Operator** (FM/PM) | Native role |
|---|---|---|---|
| Engine | Physical-modeled VA, AAS | 4-op phase modulation, Henke | — |
| Oscillators | 2 + noise + sub + sync | 4 operators | — |
| Filters | **2× multimode (LP/HP/BP/Notch/Formant, 12/24 dB), series/parallel** | 1× Cytomic (models specific circuits) | Analog's filters are more numerous; Operator's are more *characterful* |
| Best at | Fat saws, pads, basses, acid, sync leads, PWM strings | Bells, plucks, e-pianos, inharmonic metal | — |
| "Make it vintage" knob | **Error** (drift) + **Drive** | **Spread** + Antialias-off | — |

For uncompromising vintage *character*, many producers reach for dedicated emulations — **u-he Diva** (zero-delay-feedback circuit modeling), **Arturia V Collection** (Mini V, Jup-8 V, ARP 2600 V), **TAL-U-No-LX** (Juno), or **Roland Cloud TB-303** — but Analog wins on **CPU efficiency, native Live integration (clip envelopes, Max for Live, the modulation system), and breadth** (everything-in-one-device). Use Analog as the teaching instrument precisely because its controls map 1:1 onto the textbook subtractive chain.

---

## SECTION 2 — Subtractive Synthesis: History & Theory

### Pass 1: The signal chain and why it's "subtractive"

The canonical subtractive voice is three stages: **oscillator → filter → amplifier**, realized in hardware as **VCO → VCF → VCA** ([Sound on Sound: Synth Secrets](https://www.soundonsound.com/series/synth-secrets-sound-sound); [Wikipedia: Subtractive synthesis](https://en.wikipedia.org/wiki/Subtractive_synthesis)). It is *subtractive* because you begin with a **harmonically rich source** — sawtooth, square/pulse, or noise — and **attenuate (subtract) overtones with a filter**. Wikipedia: "a method of sound synthesis in which overtones of an audio signal are attenuated by a filter to alter the timbre" ([Wikipedia: Subtractive synthesis](https://en.wikipedia.org/wiki/Subtractive_synthesis)). A sawtooth is the favored raw material "because it contains all the integer harmonics" ([Wikipedia: Sawtooth wave](https://en.wikipedia.org/wiki/Sawtooth_wave)).

This is the conceptual inverse of the two other paradigms — and the perfect counterpoint to Episode 1: **additive** *builds up* a tone by summing sine partials; **FM** (Chowning, Episode 1) *generates sidebands* economically via modulation; **subtractive** *filters away* from a rich source ([Home Studio Guys: subtractive vs additive vs FM](https://homestudioguys.com/blog/subtractive-vs-additive-vs-fm-synthesis-explained/)). In one line: **additive adds sines, FM generates sidebands, subtractive filters away.**

### Pass 2: Moog and the East Coast (1964–1971)

The story starts with **Robert Moog** and composer **Herbert Deutsch** in 1963–64; Moog formalized the voltage-controlled module concept in his AES paper *"Voltage-Controlled Electronic Music Modules"* (October 1964), where Alwin Nikolais saw the demo and placed the first order ([Wikipedia: Moog synthesizer](https://en.wikipedia.org/wiki/Moog_synthesizer); [Wikipedia: Robert Moog](https://en.wikipedia.org/wiki/Robert_Moog)).

**The ladder filter — the sonic signature.** Moog's defining contribution is the **transistor ladder voltage-controlled filter, US Patent 3,475,623**, *"Electronic High-Pass and Low-Pass Filters Employing the Base to Emitter Diode Resistance of Bipolar Transistors,"* **filed 10 October 1966, granted 28 October 1969** ([Google Patents: US3475623A](https://patents.google.com/patent/US3475623A/en); [Mix: Moog Hall of Fame, Patent 3,475,623](https://www.mixonline.com/the-wire/moog-inducted-national-inventors-hall-fame-patent-no-3475623-moog-ladder-filter-416600)). It exploits the exponential relationship between a transistor's base-emitter resistance and its standing current so cutoff sweeps **exponentially over ~1000:1** via a control voltage — perfect for music's exponential pitch perception. Two symmetrical cascades of four transistors give a **24 dB/oct (4-pole)** low-pass; feedback around the ladder produces the resonance and, pushed far, **self-oscillation** (a pure sine at cutoff) ([Google Patents: US3475623A](https://patents.google.com/patent/US3475623A/en); [Mix](https://www.mixonline.com/the-wire/moog-inducted-national-inventors-hall-fame-patent-no-3475623-moog-ladder-filter-416600)).

**The Minimoog Model D.** Introduced **1970**, regular production **1971** at **US $1,495** ([Equipboard: 1971 Minimoog Model D](https://equipboard.com/items/1971-minimoog-model-d); [Synthfool 1971 price list](https://synthfool.com/pricelists/prices71.html)). Architecture: **three VCOs** (osc 3 doubles as a modulation/LFO source), the 24 dB ladder VCF, a noise generator, a contour generator, a 44-note keyboard with low-note priority, and **pitch-bend + modulation wheels** — all on a **fixed, hardwired path** (no patch cables) ([Wikipedia: Minimoog](https://en.wikipedia.org/wiki/Minimoog); [Sound on Sound: Minimoog Model D](https://www.soundonsound.com/reviews/moog-minimoog-model-d)). It was **the first synthesizer sold in retail stores**, ran 13 years, and made **over 12,000 units** before production stopped July 1981 ([Wikipedia: Minimoog](https://en.wikipedia.org/wiki/Minimoog)). This is the "rubber-band bass / fat lead" machine of §3.

### Pass 3: ARP, and the lawsuit filter (1971–1981)

**ARP Instruments** was founded **1969** by **Alan R. Pearlman** (initials = ARP), motivated by the tuning instability of early Moog/Buchla gear; he wanted a *stable* commercial instrument ([Wikipedia: Alan R. Pearlman](https://en.wikipedia.org/wiki/Alan_R._Pearlman); [Sweetwater: ARP history](https://www.sweetwater.com/insync/arp-instruments-history/)). The **ARP 2600 (1971)** was **semi-modular**: fixed internal prewiring overridable with patch cords, with printed signal-flow graphics ([Wikipedia: ARP 2600](https://en.wikipedia.org/wiki/ARP_2600)). Early units used the **Model 4012** 24 dB ladder filter — which copied Moog's patented design closely enough that, after a Moog visit and under legal threat, ARP redesigned it into the **4072** in 1977 ([Vintage Synth Explorer: ARP 2600](https://www.vintagesynth.com/arp/2600); [Wikipedia: ARP 2600](https://en.wikipedia.org/wiki/ARP_2600)). The **ARP Odyssey (1972)** was **duophonic**; its filter lineage ran **4023 (2-pole) → 4035 (4-pole, "infringing") → 4075** ([Wikipedia: ARP Odyssey](https://en.wikipedia.org/wiki/ARP_Odyssey)). **[FLAG]** "lawsuit filter" is partly a nickname — whether a suit was formally *filed* (vs threatened and settled out of court) is debated ([Wikipedia: ARP 2600](https://en.wikipedia.org/wiki/ARP_2600)). Architecturally ARP favored **sliders + semi-modular patching**, the engineer's alternative to Moog's streamlined knobs-and-wheels.

### Pass 4: Roland — affordable subtractive, and the TB-303 (1973–1984)

Roland (Ikutaro Kakehashi, founded 1972) built the vocabulary of *affordable* analog subtractive synthesis.

- **SH series:** from the **SH-1000 (1973**, Roland's first synth) to the icon, the **SH-101 (Nov 1982, US $495)** — single VCO (pulse/PWM + saw + sub-osc + noise) → resonant LP VCF → ADSR, with a built-in sequencer/arpeggiator and an optional **modulation grip + strap (keytar)** ([Wikipedia: Roland SH-101](https://en.wikipedia.org/wiki/Roland_SH-101)). The SH-101 is a Detroit-techno and Aphex Twin staple (§3).
- **Juno series:** the **Juno-6/60 (1982)** and **Juno-106 (1984)** used a **DCO (digitally *controlled* analog oscillator)** for tuning stability, the **IR3109** 4-pole 24 dB LP filter, and the famous **BBD stereo chorus** to fatten the single-oscillator-per-voice sound ([Wikipedia: Roland Juno-60](https://en.wikipedia.org/wiki/Roland_Juno-60); [Wikipedia: Roland Juno-106](https://en.wikipedia.org/wiki/Roland_Juno-106); [AMSynths: IR3109](https://amsynths.co.uk/2022/04/06/all-about-the-ir3109-chip/)). The Juno chorus pad is one of the most-used sounds in house and pop (§3).
- **Jupiter-8 (1981):** the 8-voice flagship, two VCOs/voice, sync + cross-mod, IR3109 filter switchable **12/24 dB**, praised for "clarity and transparency" ([Wikipedia: Roland Jupiter-8](https://en.wikipedia.org/wiki/Roland_Jupiter-8); [Sound on Sound: Roland Jupiter](https://www.soundonsound.com/reviews/roland-jupiter)).
- **TB-303 Bass Line (1981, US $395):** designed by **Tadao Kikumoto**, intended as automatic bass accompaniment for guitarists alongside the TR-606 ([Wikipedia: Roland TB-303](https://en.wikipedia.org/wiki/Roland_TB-303); [Attack Magazine: TB-303](https://www.attackmagazine.com/technique/hardware-focus/roland-tb-303/)). A single oscillator (saw or square) → **diode-ladder resonant LP** → with **accent** (per-step emphasis) and **slide/glide** (per-step portamento) ([Wikipedia: TB-303](https://en.wikipedia.org/wiki/Roland_TB-303)). **[FLAG — genuinely contested]** Filter slope is variously cited **18 vs 24 dB/oct**, and it is "frequently described as 3-pole/18 dB" but Tim Stinchcombe's circuit analysis shows it is **actually a 4-pole, diode-ladder, discrete-transistor** design whose interacting poles produce the dirty, sharp squelch ([Vintage Synth Explorer: TB-303](https://www.vintagesynth.com/roland/tb-303); [Tim Stinchcombe: diode-ladder analysis](https://www.timstinchcombe.co.uk/index.php?pge=diode2); [Eddy Bergman: TB-303 VCF](https://www.eddybergman.com/2025/03/TB303-VCF.html)). It does **not** use the IR3109 (that's the polysynth filter). A commercial **failure, discontinued 1984** (~10,000 units), dumped for ~$50, then reborn as the engine of acid house (§3) ([Wikipedia: TB-303](https://en.wikipedia.org/wiki/Roland_TB-303); [DJ TechTools: TB-303 history](https://djtechtools.com/2015/12/02/history-tb-303-rolands-accidental-legend/)).

### Pass 5: Oberheim, Sequential, and East vs West Coast

**Oberheim SEM (1974):** the Synthesizer Expander Module's defining feature is a **voltage-controlled state-variable filter** with simultaneous **LP/HP/BP** outputs at **12 dB/oct**, plus a **notch** by summing LP+HP — a single knob continuously morphs the response. Notably it **does not self-oscillate**, giving a brighter, more open character than Moog's steeper ladder ([Sound on Sound: Tom Oberheim SEM](https://www.soundonsound.com/reviews/tom-oberheim-sem)). The **OB-X/OB-Xa/OB-8** (1979–1983) scaled this into programmable polyphony, the OB-Xa moving to **Curtis CEM** chips with a switchable 12/24 dB filter (famously Van Halen's "Jump") ([Wikipedia: Oberheim OB-Xa](https://en.wikipedia.org/wiki/Oberheim_OB-Xa)). **The SEM's multimode-state-variable concept is the closest hardware ancestor of Analog's per-filter LP/HP/BP/Notch selector.**

**Sequential Prophet-5 (1978):** **the first fully programmable polyphonic synth** — microprocessor patch memory (40 patches), 5 voices, 2 VCOs each, 4-pole resonant LP; Rev 1–2 used **SSM** chips, Rev 3 used **Curtis CEM** chips ([Wikipedia: Prophet-5](https://en.wikipedia.org/wiki/Prophet-5); [sdiy.info: Prophet-5](https://sdiy.info/wiki/Sequential_Circuits_Prophet-5)). It founded the modern programmable polysynth category and solved the "total recall" problem that VA would later perfect digitally.

**East Coast vs West Coast.** **Moog = East Coast** (Trumansburg, NY): keyboard-driven, **subtractive**, VCF-centric — start rich, filter down. **Buchla = West Coast** (Berkeley, CA): **no keyboard** (touch plates + sequencers), start *simple* (sines) and *add* complexity via **waveshaping/wavefolding** and **complex oscillators (FM/AM)**, with the signature **low-pass gate (LPG, Buchla 292)** combining filter + amplifier in a vactrol-based "plucky" circuit ([Perfect Circuit: East/West Coast](https://www.perfectcircuit.com/signal/east-coast-west-coast-synthesis); [Perfect Circuit: low-pass gate](https://www.perfectcircuit.com/signal/what-is-a-lowpass-gate); [Wikipedia: Buchla](https://en.wikipedia.org/wiki/Buchla_Electronic_Musical_Instruments)). **Analog — and this whole episode — is firmly East Coast.** (Worth one sentence in the script: West Coast is the *next* episode's territory if there is one; Operator's wavefolding-adjacent FM is the closest the show has come to West Coast so far.)

### Pass 6: Why subtractive dominated, and the move to virtual analog

Subtractive became the default for converging reasons: **conceptual transparency** (oscillators supply harmonics, the filter subtracts them — one-knob-per-function), **cheap to build** with analog VCO/VCF/VCA circuits, and a **rich, warm, hands-on** sound "crafted by the user, not the manufacturer" ([MusicTech: subtractive synthesis](https://musictech.com/guides/essential-guide/what-is-subtractive-synthesis/)). Its dominance is exactly why later digital instruments chose to **model** it rather than replace it.

**The virtual-analog (VA) revolution.** Classic analog polyphony was expensive (one VCO/VCF per voice) and unstable (temperature drift); recall was impossible before microprocessor memory ([MusicRadar: history of VA synths](https://www.musicradar.com/music-tech/the-history-of-virtual-analogue-synthesizers)). By the mid-90s, cheap DSP could model analog oscillators and filters in real time:
- **Clavia Nord Lead (1995)** — "popularized the term 'virtual analog synthesis'" (Clavia coined it); red-bodied, DSP subtractive+FM ([Wikipedia: Nord Lead](https://en.wikipedia.org/wiki/Nord_Lead)). **[FLAG]** "first VA" is contested — Korg Prophecy shipped the same year ([Wikipedia: Korg Prophecy](https://en.wikipedia.org/wiki/Korg_Prophecy)).
- **Access Virus (1997)** — German DSP VA, 12-voice, the trance/techno workhorse ([Wikipedia: Access Virus](https://en.wikipedia.org/wiki/Access_Virus)).
- **Roland JP-8000 (1997)** — the **Supersaw**: a single oscillator algorithm of **7 detuned sawtooths**; Adam Szabo's thesis dissects it (osc 4 = center, six side oscillators offset by a nonlinear **Detune** curve, **Mix** amplitude-controls the sides, phases free-running/random) ([Wikipedia: Roland JP-8000](https://en.wikipedia.org/wiki/Roland_JP-8000); [Szabo: How to Emulate the Super Saw](https://www.adamszabo.com/internet/adam_szabo_how_to_emulate_the_super_saw.pdf)). **This is exactly what Analog's Unison (4 voices + Detune) approximates** — and what a manual stack of detuned saws builds.
- **The DSP modeling problem** is recreating analog imperfection (anti-aliasing, nonlinearity). The landmark reference is **Huovilainen, "Non-Linear Digital Implementation of the Moog Ladder Filter," DAFx-04 (2004)**, extended in **Huovilainen & Välimäki, CMJ 30(2), 2006** ([Semantic Scholar: Huovilainen DAFx-04](https://www.semanticscholar.org/paper/NON-LINEAR-DIGITAL-IMPLEMENTATION-OF-THE-MOOG-Huovilainen/c4904c04a7be1d675e360409178da71a1253f6d8)). **Ableton Analog's AAS physical-modeling engine is a sibling of this lineage** — and its **Error** knob is the explicit re-injection of the drift these models otherwise eliminate.

---

## SECTION 3 — Artist Deep Dives

### The TB-303 acid lineage (the defining subtractive performance technique)

**Phuture — "Acid Tracks" (1987).** Phuture (Nathaniel "DJ Pierre" Jones, Earl "Spanky" Smith Jr., Herbert "Herb J" Jackson, formed Chicago 1985) are credited with inventing acid house ([Wikipedia: Phuture](https://en.wikipedia.org/wiki/Phuture); [Wikipedia: Acid Tracks](https://en.wikipedia.org/wiki/Acid_Tracks)). Spanky bought the discarded TB-303 secondhand for ~$40 ([Red Bull Music Academy: DJ Pierre interview](https://daily.redbullmusicacademy.com/2012/12/dj-pierre-interview/); [Roland Articles: DJ Pierre & Phuture](https://articles.roland.com/lifetime-achievement-dj-pierre-and-phuture/)). Not knowing how to program it conventionally, they tweaked the knobs live — *"Spanky was like, 'Woah woah woah. Keep doing that'"* — producing a "squelching, resonant and liquid sound" ([Red Bull Music Academy](https://daily.redbullmusicacademy.com/2012/12/dj-pierre-interview/); [Wikipedia: TB-303](https://en.wikipedia.org/wiki/Roland_TB-303)). DJ Ron Hardy debuted it at the Muzic Box; released on Trax (re-recorded with Marshall Jefferson) in 1987 ([Roland Articles](https://articles.roland.com/lifetime-achievement-dj-pierre-and-phuture/)). **The acid technique = saw/square through a resonant LP, cutoff and resonance swept by hand in real time, with accent (per-step emphasis deepening the filter envelope) and slide (per-step glide).**

**Josh Wink — "Higher State of Consciousness" (1995).** **[ATTRIBUTION RESOLVED]** Long debated as 303 vs MC-202; Wink settled it: *"used two original, non-modified 303s … For the record, it's a 303. No 202s used!"* ([Mixmag: Josh Wink](https://mixmag.net/feature/josh-wink-tells-us-how-he-really-made-higher-state-of-consciousness); [Roland Articles: HSOC](https://articles.roland.com/higher-state-of-consciousness-josh-wink/)). Built with two 303s, a TR-909, and a DOD distortion pedal; the famous screaming sweep comes from **cutoff automated through the whole rise/build/fall, with resonance boosted (reportedly via PCB trimpots)** ([Roland Articles: HSOC](https://articles.roland.com/higher-state-of-consciousness-josh-wink/)). **[FLAG]** the Mixmag page returned a 403 on fetch — verify quote against live page before reading verbatim.

**Hardfloor — "Hardtrance Acperience" (1992).** German duo Bondzio/Zenker; signature is **layering multiple 303s** (sources cite up to six; they later owned 12) ([Wikipedia: Hardfloor](https://en.wikipedia.org/wiki/Hardfloor); [Decoded Magazine: Hardfloor](https://www.decodedmagazine.com/hardfloor/)). **[FLAG]** "six 303s" is general practice, not pinned to this track.

**Plastikman / Richie Hawtin — "Sheet One" (1993).** "Perhaps the most definitive example of Roland's TB-303 ever released in album format" — Hawtin: *"I had my 303s, a 606 and an 808 going here,"* lines often pitched up an octave, jammed live, aiming for "acidic but not Chicago acid" — a colder, minimal, dub 303 ([MusicRadar: Plastikman Sheet One](https://www.musicradar.com/news/tech/classic-album-richie-hawtin-on-plastikmans-sheet-one-633433); [DJ Mag: Sheet One](https://djmag.com/content/solid-gold-how-plastikman-redefined-acid-techno-sheet-one)).

### Reese bass — detuned saws through a filter

**Origin: Kevin Saunderson as "Reese," "Just Want Another Chance" (1988, KMS).** One of the Belleville Three; the bassline that producers later sampled and synthesists reverse-engineered ([Attack Magazine: Reese deconstructed](https://www.attackmagazine.com/technique/deconstructed/reese-just-want-another-chance/); [Discogs](https://www.discogs.com/release/18335-Reese-Just-Want-Another-Chance)). **[ATTRIBUTION — the famous correction]** The *original* Reese was made on a **Casio CZ-series phase-distortion synth, most likely the CZ-5000** — but Saunderson himself is unsure: *"It was a CZ-5000. A 5 or a 2, but I think it was the 5000 … just straight-up parameters, getting down with the oscillators, and I found some magic"* ([MusicRadar: Kevin Saunderson](https://www.musicradar.com/news/tech/kevin-saunderson-on-the-reese-bass-synths-software-and-a-life-in-techno-586401); [Attack Magazine](https://www.attackmagazine.com/technique/deconstructed/reese-just-want-another-chance/)). The CZ uses **phase distortion** (digital, two "lines" per voice — the doubled beating character) ([Vintage Synth Explorer: CZ-5000](https://www.vintagesynth.com/casio/cz-5000)). DJ Mag's "Sequential Prophet" and the "Juno-106" attributions are **later misattributions** (Saunderson's Prophet-5 post-dates the track) ([DJ Mag: Terrorist](https://djmag.com/longreads/how-renegades-terrorist-created-blueprint-jungle)).

**The MODERN Reese = subtractive re-creation.** Two or three **detuned sawtooth oscillators through a low-pass filter** ([Native Instruments: Reese bass](https://blog.native-instruments.com/reese-bass/); [Futureproof: Reese sound design](https://futureproofmusicschool.com/blog/reese-bass-sound-design-everything-you-need-to-know)). The "wub" is **phase cancellation between the out-of-phase saws**; because detune is constant in *cents*, the beating **accelerates as pitch rises**. A 24 dB LP tames the bright saws into a growl, cutoff modulated for movement. **This is the cleanest Analog teaching patch: OSC1 saw + OSC2 saw detuned ±10–20 cents (or Unison 4 + Detune) → 24 dB LP.** Sampled into jungle by **Renegade / Ray Keith, "Terrorist" (1994)** ([WhoSampled](https://www.whosampled.com/sample/36267/); [DJ Mag](https://djmag.com/longreads/how-renegades-terrorist-created-blueprint-jungle)).

### Aphex Twin (Richard D. James) — the analog/subtractive side

The April 1993 *Future Music* feature "The Aphex Effect" lists a setup built around a **Korg MS-20, Roland SH-101, Yamaha DX7, and Roland TB-303**, through an Alesis Quadraverb ([Lanner Chronicle transcription](https://lannerchronicle.wordpress.com/2020/08/30/the-aphex-effect-future-music-magazine-april-1993/); [FACT: Aphex gear](https://www.factmag.com/2017/04/14/aphex-twin-gear-synths-samplers-drum-machines/)). Zoe Blade's cross-referenced ledger adds a modded SH-101, two TB-303s (one "heavily modded and broken"), Roland System-100/100M, EMS Synthi A, and **three Korg MS-20s** ([Zoe Blade: Aphex notebook](https://notebook.zoeblade.com/Aphex_Twin.html)).

**Korg MS-20 — why it screams.** The one synth RDJ refused to modify. Its aggression comes from a **dual, independently-resonant filter: a resonant high-pass feeding a resonant low-pass, both self-oscillating**, with the early Rev-1 Korg-35 Sallen-Key topology distorting asymmetrically when pushed ([Vintage Synth Explorer: MS-20](https://www.vintagesynth.com/korg/ms-20); [Perfect Circuit: MS-20](https://www.perfectcircuit.com/signal/korg-ms-20)). **This HP→LP series filter is exactly reproducible in Analog: Filter 1 = HP (resonant), Filter 2 = LP (resonant), routed in series.** The MS-20's external-signal input also let RDJ feed drums/samples *into* the filters.

**Tracks.** "Digeridoo" (1992) is purely electronic — a self-oscillating drone, *no* didgeridoo sample ([Wikipedia: Digeridoo](https://en.wikipedia.org/wiki/Digeridoo_(EP))). *Selected Ambient Works 85–92* uses heavily detuned SH-101/MS-20/System-100 patches through the Quadraverb ([Reverb Machine: SAW 85–92](https://reverbmachine.com/blog/aphex-twin-selected-ambient-works-85-92/)). The **Analord series (2005)** is his most overtly analog/Roland project — TB-303s, TR-808s, and analog synths sequenced via CV on a Roland MC-4, "like making tracks on a taxi meter" ([FACT: Aphex gear](https://www.factmag.com/2017/04/14/aphex-twin-gear-synths-samplers-drum-machines/)).

### Squarepusher (Tom Jenkinson) — analog side

Primarily a virtuoso bassist, but with a real analog rig confirmed in *Sound on Sound*: **Roland SH-101** ("I've had the 101 forever"), **TB-303** ("the very deep bass synth comes from that" on the Shobaleader album), **TR-909** drums, and a **Yamaha CS-80** ([Sound on Sound: Squarepusher](https://www.soundonsound.com/people/squarepusher); [Tape Op #89](https://tapeop.com/interviews/89/squarepusher)). His subtractive bass work is the analog counterweight to his FM lead work (Episode 1).

### Autechre (Sean Booth & Rob Brown) — analog roots

Per *Sound on Sound*, the early chronology: *"a [TR-]606, a [Casio] SK1 and SK5 … Then we got our [MC-]202, a Tascam 244 4-track and a Juno 106"* ([Sound on Sound: Autechre](https://www.soundonsound.com/people/autechre-techno-logical)). Confirmed analog: **Korg MS-10 / MS-20**, **Roland MC-202**, **Roland SH-2**, **Juno-106** ([MusicRadar: Autechre classic interview](https://www.musicradar.com/news/autechre-classic-interview); [aepages: Amber](https://aepages.org/wiki/Amber); [aepages: Tri Repetae](https://aepages.org/wiki/Tri_Repetae)). On *Tri Repetae* (1995) a "resonant 202" self-oscillating-filter texture is audible. **[FLAG]** the Roland is an **SH-2, not SH-101**; the Juno is a **106** (no reliable Juno-60 attribution). The "warmth" is analog subtractive synthesis **colored by lo-fi digital processing** (Ensoniq EPS-16+ Waveboy disks, Alesis QuadraVerb).

### Classic subtractive signature sounds (the canon)

- **Moog "rubber-band" bass — Parliament, "Flash Light" (1978).** Bernie Worrell stacked *several Minimoogs* (sources say 3–4) — the moment synth-bass overtook electric bass in funk ([Wikipedia: Flash Light](https://en.wikipedia.org/wiki/Flash_Light_(song)); [Reverb: classic Minimoog tracks](https://reverb.com/news/video-the-synth-sounds-of-5-classic-minimoog-tracks)). The elasticity is three detuned VCOs through the 24 dB ladder, worked with pitch-bend. **[FLAG]** Polymoog/modular hypothesis disconfirmed; count (3 vs 4) uncertain.
- **Juno chorus pad — Mr. Fingers (Larry Heard), "Can You Feel It" (1986)** — Juno-60 + TR-909, the lush BBD-chorus pad that defined deep house ([Roland Articles: Can You Feel It](https://articles.roland.com/can-you-feel-it-mr-fingers/)).
- **Sequenced subtractive template — Giorgio Moroder / Donna Summer, "I Feel Love" (1977).** A **Moog Modular** (3P, borrowed from Eberhard Schoener), programmed by engineer **Robbie Wedel**, who synced the sequencer to tape via a reference pulse; the Moog drifted so it was recorded in 20–30s bursts; **hi-hats were filtered Moog white noise** ([Sound on Sound: I Feel Love](https://www.soundonsound.com/techniques/classic-tracks-donna-summer-feel-love); [Wikipedia: I Feel Love](https://en.wikipedia.org/wiki/I_Feel_Love)). A single repeating CV sequence, pitch-transposed under the chords — the blueprint for techno/trance/house. **[FLAG]** engineer is **Wedel** (not "Wootton"); a specific "Moog 960 sequencer" is plausible but unconfirmed by primary sources.
- **Gary Numan — Minimoog lead ("Are 'Friends' Electric?", 1979) + Polymoog "Vox Humana" ("Cars")** ([MusicRadar: Numan synth sounds](https://www.musicradar.com/news/the-40-greatest-synth-sounds-of-all-time-no-13-gary-numan-are-friends-electric)).
- **Kraftwerk — Minimoog (Autobahn bassline, 1974, pre-dating "I Feel Love"), ARP Odyssey, custom Synthanorma sequencer** ([Gearnews: Kraftwerk synths](https://www.gearnews.com/kraftwerk-synths-sequencers-sounds/); [FACT: Kraftwerk gear](https://www.factmag.com/2017/06/24/kraftwerk-gear-synths-drum-machines/)).
- **Detroit techno toolkit:** Juan Atkins (Korg MS-10, Sequential Pro-One, ARP Odyssey on Cybotron "Clear," 1983); the **SH-101** as the shared "fat bass" machine across the Belleville Three from ~1985 ([Sound on Sound: Model 500 No UFOs](https://www.soundonsound.com/techniques/classic-tracks-model-500-no-ufos); [Red Bull Music Academy: SH-101](https://daily.redbullmusicacademy.com/2017/09/roland-sh101-instrumental-instruments/)).

---

## SECTION 4 — Song Curation & Demo Mapping

Each entry: section map → technique → **Analog demo hook** (what to reproduce) → demo script. **[REAL]** = genuine analog hardware; **[VA]** = virtual analog / software.

### 1. Phuture — "Acid Tracks" (1987) **[REAL — TB-303]**

**Sections.** 0:00 raw 303 + drum machine; the super-squelchy resonant 303 becomes prominent **~1:27**, cutoff and resonance manipulated live throughout the 12-minute track ([Vibebox: TB-303](https://vibebox.studio/en/learn/house/roland-tb-303); [Roland Articles: DJ Pierre](https://articles.roland.com/lifetime-achievement-dj-pierre-and-phuture/)).

**Technique.** Saw/square → resonant LP; **cutoff swept by hand, resonance near self-oscillation, accent deepening the filter envelope, slide gluing notes**. The "performance" is the synthesis.

**Analog demo hook — the 303 acid line.** OSC1 = **saw** (try square for the harder variant), Sub off, mono (Voices 1), Glide on (Const, short) + Legato for slides. Filter 1 = **LP 24 (4th-order)**, Reso ~70–85%, **Drive = Asym** for dirt. Filter envelope → Freq with **short Decay, S near zero** (the per-note "wow"); raise **Env<Vel** so accented notes open brighter. Then **automate Filter Freq** live across 16–32 bars. **[VA caveat]** Analog's clean filter won't be *exactly* the 303 diode-ladder squelch — push Reso + Asym Drive to approximate the dirt; for a true clone reach for Roland Cloud TB-303 ([Roland Articles: HSOC](https://articles.roland.com/higher-state-of-consciousness-josh-wink/)).

**Demo script (40s).** *"This is the sound that an entire genre is named after — and it's the textbook subtractive chain doing one thing. A sawtooth, a resonant low-pass filter, and a hand on the cutoff knob. At 1:27 the resonance is cranked so high the filter is almost singing its own sine wave. The accent button deepens the filter envelope on chosen steps; the slide glues notes together. Phuture didn't program this — they tweaked it live, because they didn't know how it was supposed to be used. That's the whole lesson: in subtractive synthesis, the performance IS the synthesis."*

### 2. Josh Wink — "Higher State of Consciousness" (1995) **[REAL — two TB-303s]**

**Sections.** 0:00 breakbeat + 909; the 303 bassline enters and becomes prominent **~1:01**; cutoff automated through the entire rise/build/fall, resonance boosted (reportedly via PCB trimpots) for the screaming sweep ([Roland Articles: HSOC](https://articles.roland.com/higher-state-of-consciousness-josh-wink/)).

**Technique.** The acid filter sweep taken to its extreme — a long, slow cutoff automation across the whole arrangement, resonance pushed past stock range, then distorted (DOD pedal).

**Analog demo hook — the long resonant sweep.** Same 303 patch as above, but assign **Filter Freq to a Macro / clip envelope** and draw an extremely slow sweep over 16+ bars; add an **Overdrive/Saturator after Analog** to mimic the DOD pedal. Demonstrate that resonance + slow cutoff automation = rising tension.

**Demo script.** *"Same machine, opposite scale of gesture. Where Acid Tracks twitches the cutoff bar-to-bar, Wink draws one enormous filter sweep across the whole track, with the resonance pushed past where a stock 303 can even go — he tweaked the trimpots on the circuit board. Then he ran it through a guitar distortion pedal. Two 303s, a 909, a pedal. That's it. The drama is entirely in one automated parameter: cutoff frequency."*

### 3. Reese / Kevin Saunderson — "Just Want Another Chance" (1988) → Renegade "Terrorist" (1994) **[REAL — Casio CZ-5000, phase distortion]**

**Sections.** 0:00 sparse 909 + the heavy detuned bass; the bass is the entire identity of the track ([Attack Magazine](https://www.attackmagazine.com/technique/deconstructed/reese-just-want-another-chance/)).

**Technique.** **The famous correction:** the *original* Reese is **Casio CZ phase distortion** (two detuned "lines" beating), NOT subtractive saws ([MusicRadar: Saunderson](https://www.musicradar.com/news/tech/kevin-saunderson-on-the-reese-bass-synths-software-and-a-life-in-techno-586401)). The *modern* DnB Reese is the subtractive re-creation: **detuned saws → LP**.

**Analog demo hook — the modern Reese bass.** OSC1 = saw, OSC2 = saw, **Detune OSC2 ±12–25 cents** (or use **Unison = 4 + Detune**). Both → Filter 1 = **LP 24**, cutoff low-ish, slight Reso. Add a touch of **Drive (Sym)**. Play a low note and hold — the saws beat and the "wub" emerges with no LFO at all. Note the beating speeds up as you play higher (constant-cents detune).

**Demo script.** *"This is the most-corrected misconception in dance music, so let's get it right. The original Reese bass — Kevin Saunderson, 1988 — was a Casio CZ. Phase distortion. Not the detuned-saws-through-a-filter sound everyone teaches. But the MODERN Reese, the one in every drum-and-bass track since Terrorist sampled it in '94, IS subtractive: two sawtooths, detuned a few cents, run through a low-pass filter. Hold the note. Hear that movement? There's no LFO. That's just two saws drifting in and out of phase with each other — phase cancellation, sweeping like a comb filter. And because the detune is fixed in cents, it beats faster the higher you play. One oscillator, copied and detuned. That's the entire trick."*

### 4. Aphex Twin — "Digeridoo" (1992) **[REAL — self-oscillating analog]**

**Sections.** A relentless self-oscillating drone bass over an accelerating breakbeat — **no actual didgeridoo** ([Wikipedia: Digeridoo](https://en.wikipedia.org/wiki/Digeridoo_(EP))).

**Technique.** A resonant filter pushed into **self-oscillation** so it produces its own sine-ish tone, modulated — pure subtractive physics weaponized as a bass drone.

**Analog demo hook — filter self-oscillation as an oscillator.** Turn OSC levels DOWN; set Filter 1 = LP 24, **Reso to maximum** until it self-oscillates into a sine. Now **modulate Filter Freq with an LFO** (or play it from the keyboard via Freq key-tracking) — the filter IS the sound source. Teaches the §5.2 self-oscillation concept viscerally.

**Demo script.** *"There's no didgeridoo on Digeridoo. That drone is a filter eating itself. Crank the resonance until the feedback loop hits unity gain — and the filter stops filtering and starts oscillating, ringing a near-pure sine at the cutoff frequency. Now it's an oscillator. Modulate the cutoff and you're playing the filter like a synth. Richard James was 19, working out that the filter is just an oscillator you haven't turned on yet."*

### 5. Giorgio Moroder / Donna Summer — "I Feel Love" (1977) **[REAL — Moog Modular]**

**Sections.** 0:00 the relentless 16th-note Moog sequence enters; chords transpose the same single CV pattern; filtered-noise hi-hats throughout ([Sound on Sound: I Feel Love](https://www.soundonsound.com/techniques/classic-tracks-donna-summer-feel-love)).

**Technique.** A single repeating sequencer pattern, **pitch-transposed under the harmony**, plus **white noise filtered into a hi-hat** — the foundational sequenced-subtractive record.

**Analog demo hook — two things.** (a) The **filtered-noise hi-hat**: OSC off, **Noise on** → Filter 1 = **HP** (or BP), short **Free/percussive amp envelope** → instant hat, no sample. (b) The **driving sequence bass**: simple saw → LP with a short filter-env pluck, sequenced in 16ths, then transpose the clip under chord changes.

**Demo script.** *"1977. Before techno had a name, Giorgio Moroder built its blueprint on a Moog modular. One sixteenth-note sequence, transposed by hand under the chords. The hi-hats? White noise through a high-pass filter with a fast envelope — no sample, just noise carved into a transient. Listen to how the whole groove is a single subtractive voice running a sequencer. Every four-on-the-floor record since owes this its DNA."*

### 6. Mr. Fingers (Larry Heard) — "Can You Feel It" (1986) **[REAL — Roland Juno-60]**

**Sections.** The warm chorused Juno pad is the emotional core, under a 909 ([Roland Articles: Can You Feel It](https://articles.roland.com/can-you-feel-it-mr-fingers/)).

**Technique.** Single-DCO-per-voice pad fattened by **BBD stereo chorus** — the "Juno sound."

**Analog demo hook — the Juno pad + chorus.** OSC1 = saw (or pulse), slow **amp-envelope attack/release**, gentle **LP**, then **Chorus-Ensemble after Analog** (Analog has no built-in chorus). Add small **Error** for analog drift. Demonstrates that the Juno's magic is partly *outside* the synth — the chorus.

**Demo script.** *"The Juno only had one oscillator per voice — thin, on paper. Roland's fix was a bucket-brigade chorus that doubled and detuned the signal in real time. That's the whole 'Juno sound': a simple subtractive pad plus a chorus that makes one oscillator sound like three. In Analog we get the warmth with the Error knob and the width with a chorus after the device. Same idea, four decades apart."*

### 7. Autechre — "Tri Repetae"-era textures (1995) **[REAL — MS-10/MS-20/MC-202]**

**Sections.** Resonant, self-oscillating filter pings and filtered basslines woven into the rhythm ([aepages: Tri Repetae](https://aepages.org/wiki/Tri_Repetae)).

**Technique.** Resonant analog filters (MS-20 dual-filter, MC-202 self-oscillating) used as **timbral/rhythmic** sources, then processed lo-fi.

**Analog demo hook — the MS-20 dual-filter scream.** Filter 1 = **HP 24 resonant**, Filter 2 = **LP 24 resonant**, **routed in series** → reproduces the MS-20's HP→LP architecture. Push both resonances; sweep both cutoffs. Run the output through bitcrushing/short reverb for the Autechre lo-fi color.

**Demo script.** *"Autechre's early warmth is analog filters abused. The MS-20 has two resonant filters in series — a high-pass into a low-pass — and both can self-oscillate. In Analog you can rebuild that exactly: filter one as a resonant high-pass, filter two as a resonant low-pass, in series. Sweep them against each other and you get that vocal, screaming, semi-broken character. Then they ran it through cheap digital gear until it sounded like a memory of itself."*

### 8. Parliament — "Flash Light" (1978) **[REAL — stacked Minimoogs]**

**Sections.** The bouncing, elastic Moog bass riff is the hook ([Wikipedia: Flash Light](https://en.wikipedia.org/wiki/Flash_Light_(song))).

**Technique.** Three detuned VCOs → 24 dB Moog ladder, worked with **pitch-bend** for the "rubber-band" elasticity ([Reverb: Minimoog tracks](https://reverb.com/news/video-the-synth-sounds-of-5-classic-minimoog-tracks)).

**Analog demo hook — the rubber-band Moog bass.** Two saws (OSC1/OSC2) **slightly detuned** + **Sub on** for weight → **LP 24**, moderate Reso, short filter-env pluck. Set a **wide PB Range** and bend into notes. **Drive (Asym)** for ladder-ish grit.

**Demo script.** *"Funk's synth-bass revolution, 1978: Bernie Worrell stacked Minimoogs and played the pitch-bend wheel like a fretless. Three detuned oscillators through Moog's 24-dB ladder filter — fat because of the detuning, elastic because of the bend. In Analog: two detuned saws, a sub-oscillator for the bottom, a 24-dB low-pass, and a generous pitch-bend range. The 'rubber band' isn't an effect — it's the pitch wheel and the slight tuning drift of three oscillators that never quite agree."*

### Recommended additions / honorable mentions

- **Roland JP-8000 Supersaw trance (e.g., the "anthem trance" lead sound)** **[VA]** — directly demo Analog's **Unison = 4 + Detune** as a 7-saw approximation; the cleanest VA-on-VA teaching moment ([Szabo: Super Saw](https://www.adamszabo.com/internet/adam_szabo_how_to_emulate_the_super_saw.pdf)).
- **Gary Numan — "Cars"** **[REAL — Polymoog Vox Humana]** — a PWM-rich preset; demo **PWM** (LFO → Pulse Width) as the source of that chorusing string-organ character ([MusicRadar: Numan](https://www.musicradar.com/news/the-40-greatest-synth-sounds-of-all-time-no-13-gary-numan-are-friends-electric)).
- **The PWM string pad (generic)** **[VA demo]** — Sound on Sound's insight that a single PWM oscillator equals two oscillators beating; the lush "string machine" sound from one oscillator ([Sound on Sound: PWM strings](https://www.soundonsound.com/techniques/synthesizing-strings-pwm-string-sounds)).

---

## SECTION 5 — Technical Synthesis Depth

### 5.1 Oscillator spectra (the raw material Analog filters)

For fundamental angular frequency ω = 2πf, amplitude A ([Wikipedia: Sawtooth](https://en.wikipedia.org/wiki/Sawtooth_wave); [Square](https://en.wikipedia.org/wiki/Square_wave_(waveform)); [Triangle](https://en.wikipedia.org/wiki/Triangle_wave); [Pulse](https://en.wikipedia.org/wiki/Pulse_wave)):

- **Sawtooth — ALL harmonics, amplitude ∝ 1/n:**
  x(t) = −(2A/π)·Σ_{k≥1} [(−1)^k / k]·sin(kωt). The brightest, richest standard wave — every integer harmonic present. *This is why saw is the default subtractive source.*
- **Square — ODD harmonics only, ∝ 1/n:**
  x(t) = (4A/π)·[sin ωt + (1/3)sin 3ωt + (1/5)sin 5ωt + …]. Hollow, "woody/clarinet" character from the missing even harmonics.
- **Triangle — ODD harmonics only, ∝ 1/n²:** far darker than square (faster roll-off). **[NOTE]** Analog has **no triangle** — its four shapes are sine/saw/rectangular/noise. To get a triangle-ish darkness, low-pass a square.
- **Pulse / variable width (PWM) — content depends on duty cycle d:** the harmonic envelope is a **sinc**, with **nulls at integer multiples of 1/d**. At d = 0.5 the nulls fall on every even harmonic (recovering the odd-only square); narrower pulses spread energy upward (brighter, thinner) and introduce **even harmonics** for any d ≠ 0.5.
- **Sine — fundamental only.** The thing a self-oscillating filter produces (§5.2).

**Demo recipe (UNMISTAKABLE).** On a held note, set Analog OSC1 to **rectangular**, open the filter fully, and **sweep Pulse Width** from 50% downward. The listener hears even harmonics fade in and the tone thin/nasalize — the spectrum visibly changing with no filter involved.

### 5.2 Filters — slopes, resonance, self-oscillation (the math)

- **Slope ↔ poles:** roll-off is **6 dB/octave per pole** (= 20 dB/decade), so 1/2/3/4 poles → **6/12/18/24 dB/oct** ([Wikipedia: Low-pass filter](https://en.wikipedia.org/wiki/Low-pass_filter); [Sweetwater: slope](https://www.sweetwater.com/insync/slope/)). **Analog's "2nd order" = 12 dB/oct; "4th order" = 24 dB/oct.** Cascading two 24 dB filters in **series** (To F2 full) approaches 48 dB/oct.
- **Cutoff = the −3 dB half-power point:** output power halved (10·log₁₀(½) ≈ −3.01 dB), an amplitude drop to 1/√2 ≈ 0.707 ([Wikipedia: Low-pass filter](https://en.wikipedia.org/wiki/Low-pass_filter)).
- **Resonance / Q:** feeds output back to input to boost a peak at cutoff; Q = f_r/Δf where Δf is the full width between half-power points ([Wikipedia: Q factor](https://en.wikipedia.org/wiki/Q_factor)).
- **Self-oscillation:** as resonance feedback rises, loop gain at cutoff → 1; at unity with the right phase (**Barkhausen condition**) the loop becomes **marginally stable** and rings into a sustained **near-pure sine at the cutoff frequency** — the filter has become a sine oscillator ([Electronic Music Wiki: self-oscillation](https://electronicmusic.fandom.com/wiki/Self-oscillation)). The resonant pole pair has been pushed onto the imaginary axis (zero damping). **This is the physics behind Digeridoo (§4.4).**

**Demo recipe (UNMISTAKABLE).** Held note, LP 24, no oscillator modulation. (a) **A/B 12 dB vs 24 dB** at the same cutoff — the steeper slope is audibly darker above cutoff. (b) **Sweep Reso from 0 → max** and listen to the peak emerge, then the filter "sing." (c) Turn oscillator level to zero and play the keyboard — the self-oscillating filter is now a (slightly impure) sine synth.

### 5.3 Detuning, beating, PWM — "fat" from interference (the math of the Reese and the Juno)

Two oscillators detuned by Δf produce **amplitude beating at frequency Δf** (the sum of two near-equal sinusoids is a carrier at the mean frequency, amplitude-modulated at Δf/2). Because synth detune is set in **cents** (a constant *ratio*), Δf grows with pitch, so **beating accelerates as you play higher** — the defining behavior of the Reese bass (§4.3) and of any detuned-saw stack ([Native Instruments: Reese](https://blog.native-instruments.com/reese-bass/)).

**PWM is the same phenomenon from one oscillator.** Sound on Sound's key identity: *"the PWM wave produced by a single oscillator is no different from the signal produced by two independent oscillators, the pitch of one of which is frequency-modulated with respect to the other"* — so sweeping pulse width with an LFO moves the sinc nulls continuously, producing the lush, chorusing "string ensemble" character from a single oscillator ([Sound on Sound: PWM strings](https://www.soundonsound.com/techniques/synthesizing-strings-pwm-string-sounds)).

**Demo recipe (UNMISTAKABLE).** (a) **Reese:** OSC1 saw + OSC2 saw, Detune from 0 → 20 cents on a held low note — the static tone blooms into movement. (b) **PWM:** one rectangular oscillator, route **LFO → Pulse Width** at a slow rate, held chord — instant chorusing strings, no second oscillator.

### 5.4 Envelopes — amp vs filter (orthogonal jobs)

A subtractive voice runs **two** envelopes doing perceptually distinct jobs ([Wikipedia: Envelope (music)](https://en.wikipedia.org/wiki/Envelope_(music)); [Sound on Sound: Synth Secrets](https://www.soundonsound.com/series/synth-secrets-sound-sound)):
- **Amp envelope → VCA:** *loudness* contour (is the note heard, and how does its volume evolve).
- **Filter envelope → VCF cutoff:** *brightness/timbre* contour. A fast-decay filter envelope = the classic **pluck/wah** — harmonics open then close while the note stays at constant volume.

**This is the precise inverse of the Episode 1 (FM) insight.** In FM, the *modulator's level envelope* IS the brightness envelope (no filter). In subtractive, **a separate filter envelope** owns brightness, decoupled from loudness. Same perceptual outcome (a "dwah" attack), opposite topology. **[CALLBACK to Ep1]** worth stating explicitly on the walk.

**Demo recipe (UNMISTAKABLE).** Held note, sustained amp envelope (no amp decay). Now give the **filter envelope** a fast decay with high **Env→Freq** amount: the note stays at constant volume but audibly "plucks" as brightness collapses. Then flatten the filter envelope and put the same decay on the **amp** envelope: now the loudness drops but the timbre is static. A/B the two — same envelope shape, different destination, completely different musical result.

### 5.5 Drive / saturation — re-introducing analog nonlinearity

Real VCFs distort intrinsically; Analog makes this explicit via the filter **Drive (Sym / Asym)** ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)). **Symmetric** clipping adds **odd** harmonics (square-ward, "fuzzy"); **asymmetric** adds **even** harmonics (tube/transformer "warmth," more 2nd-harmonic). This is what separates a sterile digital filter sweep from a "living" analog one. The DSP-modeling literature (Huovilainen) is precisely about capturing these nonlinearities ([Semantic Scholar: Huovilainen](https://www.semanticscholar.org/paper/NON-LINEAR-DIGITAL-IMPLEMENTATION-OF-THE-MOOG-Huovilainen/c4904c04a7be1d675e360409178da71a1253f6d8)).

**Demo recipe.** Hold a resonant filter sweep with Drive OFF, then switch to **Asym** — the sweep gains body and grit without changing cutoff. A/B Sym vs Asym to hear odd- vs even-harmonic character.

### 5.6 Voice architecture — Analog's "two of everything"

Analog's two-oscillator / two-filter / two-amp / four-envelope / two-LFO architecture means each note is effectively **two cross-routable sub-voices**. Key consequences for sound design:
- **Split-filter timbres:** OSC1 → F1 (e.g., bright BP), OSC2 → F2 (dark LP), summed = layered spectrum from one note.
- **True stereo voice:** AMP1 panned L, AMP2 panned R, each fed a differently-detuned oscillator → built-in unison spread.
- **Series filtering for steep/complex responses:** HP→LP series = bandpass with independent edges (MS-20); LP→LP series ≈ 48 dB/oct.
- **The "make it analog" stack:** small **Error** (per-voice detune), **Vibrato Error**, **Asym Drive**, and free-running (non-retrig) LFOs together re-inject the drift/looseness the clean model lacks. **[VA vs HW]** — this is the entire art of making a perfect digital subtractive synth sound imperfect.

---

## SECTION 6 — Episode Script Outline

### Cold Open (90 seconds)

**Audio bed.** Crossfade from silence into **~8 seconds of Phuture "Acid Tracks" at ~1:27** — the squelchy resonant 303 alone. Hold 12s. Fade under as narration enters.

**Opening narration.** *"In 1981, Roland built a little silver box meant to replace a bass guitarist. It was so bad at its job they discontinued it in three years and dumped it on the secondhand market for the price of a pizza. A few Chicago kids bought one, didn't read the manual, and turned the knobs until it screamed. They named a whole genre after the noise it made. This is the story of the oldest idea in synthesis — start with a rich sound and carve away what you don't want — and the one Ableton instrument built to teach it to you. This is Episode Two. This is Analog, and the subtractive foundation everything else is built on."*

Cut to title music — a self-oscillating filter sweep resolving into a detuned-saw chord. 4s. Into Section 2.

### History & Theory (8–9 minutes)

Beat 1 (90s). **What "subtractive" means.** Oscillator → filter → amplifier. Start rich (saw = every harmonic), subtract with a filter. The one-line contrast with Episode 1: *"FM generates a spectrum from almost nothing; subtractive starts with everything and sculpts. Opposite philosophies, same goal — control the harmonics over time."*

Beat 2 (120s). **Moog and the ladder filter.** 1964 AES paper. Patent 3,475,623 (filed '66, granted '69). The 24 dB transistor ladder, exponential cutoff, self-oscillation. The Minimoog (1970/71, $1,495, 12,000 units, first synth in retail stores). **Drop 8s of "Flash Light"** under "rubber-band bass."

Beat 3 (90s). **The filter wars.** ARP copies the ladder (the 4012 "lawsuit filter"); Roland's IR3109; Oberheim's state-variable SEM (LP/HP/BP/notch, 12 dB, doesn't self-oscillate). *"Every company in the 70s was, in some sense, arguing about how to build one filter."*

Beat 4 (90s). **East vs West Coast.** Moog (keyboard, subtractive, filter-centric) vs Buchla (no keyboard, waveshaping, low-pass gates). *"We are firmly East Coast tonight. Buchla is a different show."*

Beat 5 (120s). **The TB-303 and acid.** Kikumoto's bass box, the diode-ladder filter, accent + slide. The commercial failure. **Drop 8s of "Acid Tracks."** Phuture, DJ Pierre, "we didn't know how to work it." The genre named after a filter.

Beat 6 (60s). **Virtual analog.** Why model analog (drift, cost, recall). Nord Lead 1995, Virus, the JP-8000 Supersaw. *"And then Ableton handed AAS the job of modeling all of it — and called it Analog."*

### Synthesis Deep Dive (8–9 minutes)

Beat 1 (90s). **Oscillator spectra.** Saw (all harmonics, 1/n), square (odd, 1/n), pulse/PWM (sinc nulls move with duty cycle). **Demo in Analog: sweep Pulse Width on a held note** — hear even harmonics appear.

Beat 2 (120s). **The filter, for a physicist.** Poles and slope (6 dB/oct per pole). Cutoff = the −3 dB half-power point — *"yes, the same −3 dB from your filter labs."* Resonance = Q = feedback around the filter. **A/B 12 vs 24 dB** on a held note.

Beat 3 (90s). **Self-oscillation.** Barkhausen condition, loop gain = 1, the pole pair on the imaginary axis. The filter becomes a sine oscillator. **Demo: crank Reso to max, kill the oscillators, play the filter.** *"This is Digeridoo. There's no didgeridoo — it's a filter eating itself."*

Beat 4 (120s). **Detuning, beating, and PWM.** Two near-equal sines = beating at Δf; cents-detune means beating accelerates with pitch. PWM = one oscillator behaving like two. **Demo the Reese: two saws, detune 0→20 cents.** Then **demo PWM strings.** *"This is the loudest single idea in the episode — 'fat' is just interference. The Reese bass and the Juno string pad are the same physics: two waves that almost agree."*

Beat 5 (90s). **Two envelopes, two jobs.** Amp env = loudness; filter env = brightness. **The Episode 1 callback:** *"In FM, the modulator's envelope WAS the brightness. Here it's a separate filter envelope. Same 'dwah,' opposite topology."* **Demo: same decay on filter env vs amp env, A/B.**

Beat 6 (60s). **Drive.** Symmetric (odd harmonics) vs asymmetric (even). *"The difference between a digital sweep and an analog one is the distortion you can't hear until it's gone."*

### Ableton Analog Deep Dive (8–9 minutes)

Beat 1 (60s). **Origin.** AAS, IRCAM roots, Tassman/Ultra Analog physical modeling. **Shipped with Live 7 / Suite, November 2007** — licensed modeling, not Henke's in-house code. *"Operator is Ableton's own FM machine. Analog is borrowed physics — and it shows in the best way: every control maps onto the textbook."*

Beat 2 (90s). **Physical modeling, not emulation.** No samples, no wavetables — the circuit equations solved every sample, alias-free. **The Error knob is the thesis:** *"A perfect model of an imperfect machine sounds wrong until you add the imperfection back. That's the Error knob — random per-voice detune. The whole instrument is an argument about what 'analog' actually means."*

Beat 3 (120s). **The oscillators.** Four shapes (sine/saw/rect/noise — no triangle), Pulse Width + PWM, Sub (octave down), **Sync (Ratio sweep = the scream)**, Detune ±300 cents, F1/F2 routing balance, the noise generator.

Beat 4 (120s). **The two filters.** LP/HP/BP/Notch/Formant in 12 or 24 dB, per filter. Series vs parallel (To F2, Follow). **Rebuild the MS-20: HP→LP in series, both resonant.** Formant mode = vowels on the Reso knob. Drive Sym/Asym.

Beat 5 (90s). **Envelopes, LFOs, modulation.** Four ADSRs (two filter, two amp), **Free** (percussive) and **Loop** modes, S.Time. Two LFOs with delay/attack (delayed vibrato), free-run vs retrig. Vibrato as a third hardwired LFO.

Beat 6 (90s). **Voice architecture + "make it analog."** Two sub-voices per note: split-filter timbres, stereo voices (pan AMP1/AMP2), Unison (2/4 + Detune = supersaw). The stack: **Error + Asym Drive + free-run LFOs + Detune.** *"Analog gives you everything the canon had, in one device — and then a single knob to make it drift like 1978."*

### Patch Walkthrough (5–6 minutes) — Build a 303 acid line, then morph it into a Reese

**Target A: the 303 acid line.**
- Step 1 (45s). Default Analog. **Voices = 1, Glide = Const (short) + Legato** for slides. OSC1 = **saw**, OSC2 off, Sub off.
- Step 2 (45s). Filter 1 = **LP 24 (4th-order)**, route OSC1 fully to F1. Cutoff ~mid, Reso ~40% to start.
- Step 3 (60s). **Filter envelope → Freq**, high amount, **short Decay, Sustain ≈ 0** — the per-note "wow." Listen: each note now blips open and shut.
- Step 4 (45s). **Reso up to ~80%.** Listen — the squelch sharpens toward self-oscillation.
- Step 5 (45s). **Drive = Asym** for dirt. **Env<Vel up** so accented (high-velocity) notes open brighter — that's the accent.
- Step 6 (45s). Program a 16th line with some slid (overlapping/legato) notes; **automate Filter Freq** across 16 bars. *"That's acid. A saw, a resonant low-pass, and your hand on the cutoff."*

**Target B: morph into a Reese (45s).** Turn **OSC2 on (saw), Detune ±18 cents**, Sub on, drop the filter envelope, lower the cutoff, hold a low note. *"Same device, two genres apart. We went from Chicago 1987 to Bristol 1994 by turning on a second oscillator and detuning it. That's the entire distance between acid house and drum-and-bass, expressed as one parameter."*

Step 7 (30s). **Save as "Subtractive-303-Reese."** *"Two of the most influential bass sounds in electronic music, from one default Analog patch. In 1981 the box that made the first one was considered a failure."*

### IDM Application (5–6 minutes)

Beat 1 (90s). **Self-oscillation as a sound source.** Fresh Analog: oscillators down, **Reso = max**, LP 24, Filter Freq key-tracked → play the self-oscillating filter as a sine synth, then **modulate Freq with an LFO** for the Digeridoo drone. *"The filter is an oscillator you forgot to turn on. Aphex worked that out at 19."*

Beat 2 (90s). **The MS-20 dual-filter, abused.** HP→LP series, both resonant, sweep both against each other; run into bitcrush + short reverb. *"This is the Autechre move: analog filters pushed past politeness, then degraded with cheap digital gear until they sound like a memory."*

Beat 3 (60s). **Looping envelopes as rhythmic filter motion.** Set a **filter envelope to Loop (AD-R), tempo-ish rate** → a free, evolving rhythmic filter pulse from a single held note. *"No LFO, no sequencer — the envelope is the rhythm."*

Beat 4 (60s). **The fat-from-interference principle, generalized.** Unison 4 + Detune for supersaw leads; PWM for string pads; two detuned saws for Reese. *"Every 'huge' analog sound in this episode is the same trick: copies of a wave that almost agree. Beating, phase cancellation, PWM — interference is the whole game."*

Beat 5 (90s). **The listener exercise.** *"Homework for the walk home. Open Analog. Build the 303 from the walkthrough — saw, 24-dB low-pass, resonant, filter-envelope pluck, mono, glide. Now do the thing Phuture did: don't program it. Just turn the cutoff and resonance knobs while a loop plays, for ten minutes, and find the moment the filter starts to sing. When it does, you've found unity gain — the Barkhausen condition — by ear, the same way a 19-year-old in Cornwall found Digeridoo and three kids in Chicago found acid house. Subtractive synthesis is the oldest idea in the box, and it's still the one where your hand on a knob is the instrument. Start rich. Carve. Listen. That's everything."*

Outro music: a slow detuned-saw pad with rising Error, resolving into a single self-oscillating sine. Fade to silence. End ~40:00.

---

## Conclusion

The thesis across all six sections: **subtractive synthesis is the art of controlling harmonics over time by removal, and "analog character" is the controlled re-introduction of imperfection.** The signal chain — oscillator, filter, amplifier — has not changed since Moog's 1964 modules; what changed is that the filter became a *performance* instrument (Phuture's hands on the 303), then a *physics demonstration* (Aphex's self-oscillating Digeridoo), and finally a *perfectly-modeled abstraction* (Analog) that has to **add drift back** to sound alive. For a physicist who already builds patches in Live 12, the payoff is a unified picture: the −3 dB cutoff, Q, and the Barkhausen self-oscillation condition are the same objects from a filter lab; the Reese bass, the Juno pad, the Supersaw, and PWM strings are all the same interference phenomenon; and the difference between Episode 1's FM "dwah" and Episode 2's subtractive "wah" is purely topological — a modulator envelope versus a filter envelope, doing the identical perceptual job. Analog is the instrument where the textbook and the knob are the same thing.

---

## APPENDIX — Flagged Conflicts & Uncertainties

- **Analog's release:** **Live 7 / Suite, 29 Nov 2007** — NOT Live 4/5. Confirmed via Ableton press + SOS ([Ableton press](https://www.ableton.com/en/press/press-archive/press-archive-release-7/); [SOS](https://www.soundonsound.com/news/ableton-announces-live-7-new-add-instruments-and-ableton-suite)).
- **Analog parameter ranges** (Detune ±300 cents osc / ±50 cents global, etc.) drawn from the Live 12 manual; minor wording varies between manual versions ([Ableton manual](https://www.ableton.com/en/manual/live-instrument-reference/)).
- **TB-303 filter slope** genuinely contested: 18 vs 24 dB/oct; nominal 3-pole vs actual 4-pole (Stinchcombe). Diode-ladder, discrete transistors, NOT the IR3109. Unit count ~10,000 (dominant) vs ~20,000. Release 1981 vs 1982.
- **Reese bass synth:** Casio CZ (phase distortion), likely CZ-5000, but Saunderson is unsure (5000/2000/1000 share an engine). Prophet/Juno attributions are later errors. Modern detuned-saws-through-LP Reese is a subtractive *re-creation*, not the original method.
- **Josh Wink HSOC:** confirmed two stock 303s (artist quote); Mixmag source 403'd on fetch — verify quote against live page.
- **"Flash Light":** Minimoog(s) confirmed; Polymoog/modular disconfirmed; count 3 vs 4 uncertain.
- **"I Feel Love":** engineer is **Robbie Wedel** (not "Wootton"); Moog Modular (3P); "Moog 960 sequencer" likely but unconfirmed by primary sources.
- **Nord Lead "first VA":** contested — *popularized the term*; Korg Prophecy contemporaneous (both 1995). **JP-8000:** 1996 (infobox) vs 1997 (better-supported).
- **ARP "lawsuit filter":** patent dispute settled out of court / under threat; whether a suit was formally filed is debated.
- **Moog Patent 3,475,623:** 1966 = filing, 1969 = grant.
- **Autechre:** Roland is **SH-2** (not SH-101); Juno is **106** (no reliable Juno-60). 
- **Triangle Fourier signs** are time-origin dependent; magnitudes (odd-only, 1/n²) are invariant. **Analog has no triangle wave** — flagged in §5.1.
- **−3 dB cutoff** = half-power (1/√2 amplitude), not "quarter-power."
- Some sources (Perfect Circuit East/West & LPG explainers, Mixmag) returned HTTP 403 to the fetcher; their content here rests on detailed indexed search snippets consistent with corroborating sources.
