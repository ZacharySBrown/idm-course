# Meld: Two Synths, Twenty-Five Oscillators, Ten Fingers — Episode 4 Research Dossier

A complete research artifact for a ~40-minute walking podcast aimed at an experienced Ableton Live 12 Suite user who is also a physicist and IDM producer. Six sections, dense and citation-heavy, designed to be cut directly into a script. This episode covers **Ableton Live 12's Meld instrument** — a **bi-timbral, dual macro-oscillator, MPE-capable synthesizer** — and the broader history, theory, and practice of **macro-oscillator synthesis** (the Mutable Instruments *Plaits* lineage) and **MPE as an expressive paradigm**.

**Confidence flags** are used throughout: **[CONFIRMED]** (primary/authoritative — Ableton manual, Ableton DSP reference, named developer quote, or named-publication review), **[LIKELY]** (strong secondary or single good source), **[UNCERTAIN]** (thin, crowd-sourced, contradicted, or inference). Where a common assumption is wrong, it is corrected and flagged. **Every nontrivial claim carries a URL.**

---

## ⚠️ TWO FRAMING CORRECTIONS — read before anything else

**Correction 1 — the subtitle "Physical Modelling Hybrid" is WRONG and must be changed.** [CONFIRMED]
Meld is **not** a physical-modelling synthesizer in the Karplus-Strong / waveguide sense. It is a **bi-timbral, dual macro-oscillator subtractive-hybrid synth** with a large bank of pre-designed oscillator types built from *many* synthesis methods (virtual analog, FM, granular-esque looping, noise, additive-ish swarms, chiptune, etc.). A *minority* of its components are **physical-modelling-flavoured** — specifically the **Plate Resonator** and **Membrane Resonator** filters (scale-aware modal resonators), and impulse/excitation-style oscillators like **Tarp** and **Extratone** — but the instrument as a whole is a macro-oscillator synth, not a physical modeller. The honest one-line reframe: **"Meld: Live's bi-timbral macro-oscillator MPE synth — two synths in one box, twenty-five oscillator engines, built for the fingers."** Source: Ableton blog (ableton.com/en/blog/meld-a-look-at-live-12s-new-bi-timbral-synth); SOS (soundonsound.com/techniques/ableton-live-meld); Ableton DSP reference (docs.cycling74.com/reference/abl.dsp.meldosc~). The Plaits lineage (Section 2) *does* include true Karplus-Strong and modal physical models, which is likely where the "physical modelling" association leaked in — but Meld did **not** inherit a Karplus-Strong oscillator.

**Correction 2 — the version number in the brief is WRONG.** [CONFIRMED]
The brief (and a coordinator note) say Meld "was introduced in Live 12.1." **It was not.** Meld shipped in the **initial Live 12.0 release on 5 March 2024**, alongside **Roar** and **Granulator III**, as the three headline new instruments (ableton.com/en/blog/ableton-live-12-coming-march-5; engadget.com/ableton-live-12-whats-new-meld-roar-094528196; musictech.com/news/gear/ableton-live-12-daw). The user is on **Live 12.4**, so every feature below is present for them. The one Meld feature *added after launch* is the **Chord oscillator type, added in Live 12.2 (11 June 2025)** (ableton.com/en/release-notes/live-12). I scope feature claims to **12.0–12.4** and flag the Chord oscillator's 12.2 origin explicitly. So Meld ships with **24 oscillator types as of 12.0** and **25 as of 12.2+** (the user's 12.4 has all 25).

**Edition note.** Meld is a **Live 12 Suite-exclusive** device (ableton.com/en/live/compare-editions — Meld bulleted only in the Suite column; engadget.com confirms Suite-only). *(One Ableton **pack** page lists "Live 12 Lite … or higher" as a requirement (ableton.com/en/packs/meld) — that refers to opening the downloadable preset **pack**, not to the Meld **device** itself, which is Suite. Flag if it comes up.)*

---

## SECTION 1 — Ableton Meld: Full Parameter Reference (Annotated)

Meld is a **bi-timbral, dual macro-oscillator synthesizer**: two complete, independent synth engines — **Engine A** and **Engine B** — each with its own oscillator, filter, two envelopes, two LFOs, mixer strip, and MIDI/MPE-enabled modulation matrix. *"Each of the device's engines has a dedicated filter, envelopes, LFOs, and a MIDI and MPE-enabled Modulation Matrix"* (ableton.com/en/manual/live-instrument-reference). Ableton's framing: *"Meld is bi-timbral, meaning its distinct engines can produce, sculpt and combine two complete sounds without being tied to the amplitude and filter envelopes of one system"* (ableton.com/en/blog/meld-a-look-at-live-12s-new-bi-timbral-synth). **[CONFIRMED]** Suite-only, shipped Live 12.0, 5 March 2024.

**Design team — [CONFIRMED].** Concept lead / UX designer **Christian Kleine**; lead engineer **Rob Tubb** (soundonsound.com/techniques/ableton-live-meld). Kleine: *"It's two synthesizers in one. It allows for a combination of two things, and this makes the sum bigger than its parts."* Tubb on the modular influence: *"The sheer adaptability and multi-function stuff that modules can do, that was a big influence."* Kleine on scale-awareness: *"Even if you don't use scale awareness, this is a feature that I think is a must-have for any modern synth."* (all soundonsound.com/techniques/ableton-live-meld).

### 1.1 The two engines (bi-timbral architecture) — [CORE]

Two engines, **A** and **B**, run in parallel and are summed. **[DISTINCTIVE]** Unlike Wavetable (two oscillators sharing one amp/filter/mod system) or Operator (four operators in one voice), **each Meld engine is a full voice**: independent oscillator + filter + amp env + mod env + 2 LFOs + matrix. This is the literal meaning of *bi-timbral* — two timbres, independently shaped, from one device. Cross-engine modulation is allowed: *"Synth A's LFOs can modulate Synth B's parameters"* (soundonsound.com/techniques/ableton-live-meld) — i.e., A's LFO 1 is selectable as a source in B's matrix and vice-versa. **[CONFIRMED]**
**[CAVEAT — get this right on air]:** the two engines combine by **summing two audio outputs**; they do **not** audio-rate-cross-modulate each other (one engine's oscillator does not FM the other's). SOS: the two halves *"cannot cross-modulate audio like"* a classic dual-VCO mono synth (soundonsound.com/techniques/ableton-live-meld). Cross-engine routing is at **control/modulation rate** (LFOs, envelopes), not audio rate.

### 1.2 The oscillator — 24 macro-oscillator types (25 in 12.2+) — [CORE]

Each engine selects **one** of **twenty-four oscillator types** (*"a selection of twenty-four oscillator types … including six scale aware oscillators"* — ableton.com/en/manual/live-instrument-reference), each driven by exactly **two macro knobs** whose *meaning changes with the type*: *"two dedicated macro knobs, which change along with the oscillator type selected"* (ableton.com/en/packs/meld). This is the **macro-oscillator paradigm** (Section 2): a complex DSP algorithm collapsed behind two intuitive controls.

**Full oscillator-type table — from the Ableton DSP reference `abl.dsp.meldosc~`** (docs.cycling74.com/reference/abl.dsp.meldosc~). **[CONFIRMED — primary]**. Index, name, verbatim description, and the two macros:

| # | Type | Description (verbatim) | Macro 1 | Macro 2 |
|---|---|---|---|---|
| 0 | **Basic Shapes** | "Morphs through classic synth waveforms, adds overtones or changes the pulse width." | Shape | Tone |
| 1 | **Bitgrunge** | "A pseudo-random lo-fi square wave oscillator reminiscent of loading an old computer game from a tape." | Frequency | Mult |
| 2 | **Bubble** | "A synthesized bubble generator." | Density | Spread |
| 3 | **Chip** ♭♯ | "A chiptune oscillator which provides pitch, pulse width and interval." | Tone | Rate |
| 4 | **Crackle** | "A synthesized crackle generator." | Density | Intensity |
| 5 | **Dual Basic Shapes** ♭♯ | "Morphs through classic synth waveforms, adds overtones or changes the pulse width." | Shape | Detune |
| 6 | **Extratone** | "An oscillator that retriggers a kick drum oscillator at fast rates to produce granular-esque tonal sounds." | Pitch | Env Amount |
| 7 | **Filtered Noise** | "A noise generator with a resonant band-pass filter." | Frequency | Narrowness |
| 8 | **Fold FM** | "A harmonic FM oscillator with modulation amounts and wave folding." | FM Amount | Shape |
| 9 | **Harmonic FM** | "A harmonic FM oscillator with modulation ratio and amount." | FM Amount | FM Ratio |
| 10 | **Noise Loop** | "An oscillator that loops a noise buffer at fast rates to produce granular-esque tonal sounds." | Rate | Fade |
| 11 | **Noisy Shapes** | "Morphs through classic synth waveforms and defines the amount of noise injection." | Shape | Rough |
| 12 | **Rain** | "A rain generator with synthesized drops and wind." | Tone | Rate |
| 13 | **Shepard's Pi** | "A Shepard tone oscillator with depth and direction." | Rate | Width |
| 14 | **Simple FM** | "A simple FM oscillator with modulation index and amount." | FM Amount | FM Ratio |
| 15 | **Square 5th** | "Morphs a square to a square pitched a fifth above with pulse width adjustment." | 5th Amount | Pulse Width |
| 16 | **Square Sync** | "Two synced square waves where the frequency of each can be defined." | Freq 1 | Freq 2 |
| 17 | **FM Bass (Squelch)** | "A FM oscillator with modulation index amount and operator feedback." | FM Amount | Feedback |
| 18 | **Sub** | "A sub oscillator with waveform morphing and an additional sub (aux)." | Tone | Aux |
| 19 | **Swarm Saw** ♭♯ | "A swarm of saw waves with modulation and frequency spacing." | Motion | Spacing |
| 20 | **Swarm Sine** ♭♯ | "A swarm of sine waves with modulation and frequency spacing." | Motion | Spacing |
| 21 | **Swarm Square** ♭♯ | "A swarm of square waves with modulation and frequency spacing." | Motion | Spacing |
| 22 | **Swarm Triangle** ♭♯ | "A swarm of triangle waves with modulation and frequency spacing." | Motion | Spacing |
| 23 | **Tarp** | "An impulse/drum oscillator with decay and tone controls." | Decay | Tone |
| — | **Chord** *(added 12.2)* | "comprised of four sawtooth oscillators that play a variety of chords." (ableton.com/en/release-notes/live-12) | *(per release notes)* | *(per release notes)* |

**[FAMILY MAP — for the DSP section]** The 24+1 types cluster into recognizable synthesis families:
- **Virtual-analog / subtractive:** Basic Shapes, Dual Basic Shapes, Noisy Shapes, Square 5th, Square Sync, Sub, Chord (12.2).
- **FM:** Simple FM, Harmonic FM, Fold FM, FM Bass (Squelch — note the **operator feedback** macro, the one place Meld exposes FM feedback). **[CONFIRMED]**
- **Swarm (supersaw-style / additive-adjacent):** Swarm Saw/Sine/Square/Triangle — many detuned voices with Motion + Spacing.
- **Granular-esque buffer looping:** Noise Loop, Extratone (kick-osc retrigger). Ableton's own word is *"granular-esque"* (DSP reference) — **[CAVEAT]** these are buffer-loop/retrigger algorithms, **not** a true granular cloud engine; don't oversell.
- **Noise / textural / "real-world":** Filtered Noise, Bubble, Crackle, Rain — synthesized environmental textures. **[DISTINCTIVE]** "Rain," "bubble," "crackle" as *oscillators* is unusual and central to Meld's identity (engadget.com).
- **Lo-fi / chiptune:** Bitgrunge, Chip.
- **Special:** Shepard's Pi (barberpole / Shepard tone — endless rising/falling illusion), Tarp (impulse/drum excitation).

**Coarse vs Fine / normalized-vs-Hz note for headless rendering:** Meld's per-engine pitch is set by **Transpose (semitones, integer)** + **Detune (cents, fine)** plus the standard global tuning — analogous to Operator's Coarse(integer)/Fine(fraction) split. The **two oscillator macros are normalized 0–100% (or 0–1) parameters**, NOT Hz — their *audible* effect (e.g., FM Ratio, Freq 1/Freq 2 on Square Sync, Frequency on Bitgrunge/Filtered Noise) maps to frequency internally but the LOM/automation value is normalized. **For headless rendering you address macros and matrix amounts as normalized floats, not Hz.** **[LIKELY — confirm exact LOM parameter ranges against the live `meld` device by ear/inspection before rendering; the public docs give names, not value ranges.]**

### 1.3 Scale-aware oscillators (six) — [DISTINCTIVE]

**Six** oscillator types are **scale-aware**, marked **(♭♯)** in the device: **Dual Basic Shapes, Chip, Swarm Sine, Swarm Triangle, Swarm Saw, Swarm Square** (ableton.com/en/manual/live-instrument-reference). On these, components that would otherwise produce arbitrary inharmonic pitches (detuned swarm partials, the chip interval, etc.) are **snapped to the current scale**, so the spread stays musical. Kleine treats this as core, not a gimmick: *"this is a feature that I think is a must-have for any modern synth"* (soundonsound.com). Scale awareness ties into Live 12's global **Scale** system. **[CONFIRMED]**

### 1.4 The filter — 17 types, two macros, scale-aware resonators — [CONFIRMED]

Each engine has **one dedicated filter** offering **seventeen filter types**, each with **two macro knobs** that vary by type (ableton.com/en/manual/live-instrument-reference; musicradar.com/news/ableton-live-12-ultimate-guide-to-meld — *"17 types available"*). Types span the usual **low-pass / high-pass / band-pass**, plus **phasers, comb filters, vocal/vowel formant**, lo-fi/bitcrusher-style effects, and **resonators**. SOS lists the resonators explicitly: scale-aware **Plate Resonator** and **Membrane Resonator** that *"snap those resonant frequencies into tune with your track"* (soundonsound.com/techniques/ableton-live-meld). **[PHYSICAL-MODELLING-FLAVOURED ELEMENT]** The Plate/Membrane Resonators are **modal-resonator filters** — the closest Meld gets to physical modelling, but they are a *filter on the oscillator*, not a Karplus-Strong oscillator. This is the honest "hybrid" hook for the corrected subtitle.

### 1.5 Envelopes — two per engine, ADSR + loop modes — [CONFIRMED]

Each engine has **two envelopes**: an **Amplitude** envelope and a **Modulation** (free) envelope (musicradar.com/news/ableton-live-12-ultimate-guide-to-meld; ableton.com/en/manual/live-instrument-reference). Controls: **Attack, Decay, Sustain, Release**, with **adjustable segment slopes** and **three loop modes**: **Trigger**, **Loop**, and **AD Loop** (ableton.com/en/manual/live-instrument-reference). **[DOMAIN ANCHOR — keep loop-mode names exact for this device]** Meld's loop modes are **Trigger / Loop / AD Loop** — note this is *Meld's* set; it differs from Operator's **None / Loop / Beat / Sync / Trigger**. Do not transplant Operator's names onto Meld. A **Link Envelopes** button *"links each engine's Amplitude and Modulation envelopes"* so they move together (ableton.com/en/manual/live-instrument-reference). **[IDM USE]** A Modulation envelope in **Loop** or **AD Loop** mode routed (via the matrix) to an oscillator macro = a self-cycling timbral sequencer on one held note — the Meld analogue of Operator's loop-mode-envelope and Wavetable's Loop-envelope-on-Position trick.

### 1.6 LFOs — LFO 1 + LFO 1 FX + LFO 2, up to 200 Hz — [CONFIRMED]

Each engine has **two LFOs** with an asymmetric design (ableton.com/en/manual/live-instrument-reference; musicradar.com):
- **LFO 1** — the main LFO, with a dedicated **FX panel** for serial processing.
- **LFO 1 FX** — **eighteen effect types** applied serially to LFO 1 (e.g., **S&H**, fade-in, shaping). **[KEY]** **LFO 1 and LFO 1 FX are *independent* modulation sources in the matrix** — i.e., you can route the raw LFO 1 to one target and the FX-processed version to another (ableton.com/en/manual/live-instrument-reference; soundonsound.com).
- **LFO 2** — a simpler LFO with **six classic waveforms** (ableton.com/en/manual/live-instrument-reference).

**LFO rate reaches ~200 Hz** — into **audio rate** — so an LFO routed to amplitude or filter produces tonal/sideband effects, not just modulation (soundonsound.com/techniques/ableton-live-meld: *"LFO rate goes up to a relatively fast 200 Hz, allowing … real audio-rate tonal effects"*). **[CONFIRMED]** **[IDM USE]** Audio-rate LFO → filter cutoff or amp is a back-door FM/AM, complementing the dedicated FM oscillator types.

### 1.7 Modulation Matrix — per engine, MIDI + MPE sources — [CORE]

Each engine has its **own Modulation Matrix**: *"Meld's Modulation Matrix lets you assign modulation sources to modulation targets within the device"* — **sources across the top, targets down the side**, with **bipolar (±)** amounts (ableton.com/en/manual/live-instrument-reference). MusicRadar counts *"approximately 23 targets in expanded view"* (musicradar.com/news/ableton-live-12-ultimate-guide-to-meld — **[LIKELY]**, treat "~23" as approximate).

**Modulation sources** (ableton.com/en/manual/live-instrument-reference):
- **Internal:** LFO 1, LFO 1 FX, LFO 2, Amp Env, Mod Env (per engine), **plus the other engine's LFOs/envelopes** (cross-engine).
- **MIDI tab:** **Velocity, Pitch (note/keytrack), Random**, plus hardware **Pitch Bend, Press (channel aftertouch), Modulation Wheel**.
- **MPE tab:** per-note **Note Pitch Bend, Slide (Y / CC74), Press (per-note pressure)** (ableton.com/en/manual/live-instrument-reference; musicradar.com — *"MPE Slide and Press options"*).

**Modulation targets:** the two oscillator macros, pitch/detune, the two filter macros + filter frequency, amp level/pan, LFO rates, envelope amounts, even other modulators' amounts (the *"~23 targets"*). **[KEY]** The **two oscillator macros are first-class matrix targets** — the macro-oscillator equivalent of Wavetable's "Position is a destination": you modulate the *macro* and the whole timbre morphs.

### 1.8 MPE / per-note expression — the headline paradigm — [CONFIRMED]

Meld is built **MPE-first**: *"Live's new MPE-capable synthesizer is designed for sound variety, playfulness and character"* (ableton.com/en/packs/meld). The MPE tab exposes **per-note Pitch Bend, Slide, and Press** as matrix sources, so on an MPE controller (ROLI Seaboard, LinnStrument, Push 3 in MPE mode, etc.) **each finger independently drives modulation** — e.g., per-note pressure → an oscillator macro means each note morphs timbre under its own finger. Ableton: *"Meld's MIDI and MPE tabs let you use MIDI and MPE functionality as modulation sources, which can turn Meld into an extremely dynamic performance tool"* (ableton.com/en/packs/meld; ableton.com/en/blog/meld-a-look-at-live-12s-new-bi-timbral-synth). **[CONFIRMED]** **[CAVEAT for non-MPE listeners]** MPE sources still resolve sensibly from a normal keyboard (Press → channel aftertouch, etc.), so the patch is playable without an MPE controller, just less expressive.

### 1.9 Mixer, global, voicing — [CONFIRMED]

- **Per-engine mixer strip:** **Volume, Pan, Tone Filter** (a simple per-engine high/low tone cut) (ableton.com/en/manual/live-instrument-reference; musicradar.com — *"high/low tone cut in mixer section"*).
- **Global:** **Drive** (saturation/overdrive into the output), **Limiter** (built-in output limiter), **Master Volume** (ableton.com/en/manual/live-instrument-reference; soundonsound.com).
- **Voicing:** **Poly / Mono**; **up to 32 voices** per the manual summary (ableton.com/en/manual/live-instrument-reference). **[CONFLICT — FLAG]** One search-summarized reading of the manual said the Poly drop-down maxes at **12 voices**; the structured manual read said **up to 32**. **Verify the exact maximum in the live device before stating a number on-mic** — say *"up to a few dozen voices"* if unverified. **[UNCERTAIN on the exact cap]**
- **Glide:** **Portamento** and **Glissando** modes (glissando = stepped/chromatic glide) (ableton.com/en/manual/live-instrument-reference).
- **Stacked Voices / Spread (unison):** a **Stacked Voices** control with a **Spread** parameter; *"when a voice number is set in Stacked Voices, Spread produces an offset between each stacked voice, and when Stacked Voices is set to Off, Spread produces a range of different values for each note in a held chord"* (search-summarized manual — **[LIKELY]**). I.e., Spread is **dual-purpose**: unison-detune when stacking, and per-note variation across a chord when not. **Phase-reset** options exist for consistent transients across notes. **[CONFIRMED that Spread/Stacked Voices exist; exact behaviour LIKELY.]**

### 1.10 Meld vs Wavetable vs Operator vs Analog — where it sits

| Axis | **Meld** | Wavetable | Operator | Analog |
|---|---|---|---|---|
| Core method | **Macro-oscillator bank (24+1 algos)** | Wavetable (scan position) | 6-op… no, **4-op FM** | 2-osc subtractive (VA) |
| Voice structure | **Bi-timbral — 2 full engines** | 1 voice, 2 osc + sub | 1 voice, 4 operators | 1 voice, 2 osc + 2 filt |
| Mod system | **Per-engine matrix, MIDI+MPE** | Destination-first matrix | Fixed routings + matrix-lite | Mod matrix |
| FM | **Dedicated FM osc types (4)** incl. feedback (Squelch) | Hidden-sine per-osc FM | **The whole instrument** | Osc-2→Osc-1 FM |
| Physical-modelling flavour | **Plate/Membrane resonator filters** (modal) | none | none | none |
| Scale-aware | **Yes (6 osc types)** | no | no | no |
| MPE | **First-class, designed-in** | yes (Live 11+) | yes | yes |
| Texture/"real-world" | **Rain/Bubble/Crackle osc** | no | no | no |
| Edition / version | **Suite, 12.0 (2024); Chord osc 12.2** | Suite, 10.0 (2018) | Suite, Live 8-era | Suite, Live 7-era |

(ableton.com/en/manual/live-instrument-reference; soundonsound.com/techniques/ableton-live-meld.) **The Meld verdict:** where Operator asks you to *build* a spectrum from sine operators and Wavetable asks you to *scan* a curated spectrum, **Meld asks you to *pick* a ready-made complex algorithm and *play it with your fingers*** — two of them at once, snapped to your scale, modulated per-note. It is the **least "engineer-y"** and most **performance-/texture-oriented** of Live's synths, and its center of gravity is **MPE + two oscillator macros**, not a deep editing surface.

---

## SECTION 2 — History & Theory: Macro-Oscillators and MPE

### Pass 1 — What a "macro-oscillator" IS

A **macro-oscillator** is a single oscillator *slot* that hides an entire complex synthesis algorithm behind a **small, fixed set of high-level "macro" controls** (usually two), letting one knob sweep through behaviours that would otherwise require many parameters. Meld's own design: each of the 24+1 types is *"a complex DSP algorithm collapsed behind two macros"* whose meaning changes per type (ableton.com/en/packs/meld). The point is **breadth with playability**: you trade fine editability for instant access to subtractive, FM, granular-esque, noise, and additive-ish sources from one control surface. **[CONFIRMED, definitional]**

### Pass 2 — Mutable Instruments *Plaits*: the direct lineage [CONFIRMED lineage, INFERRED code-reuse]

The macro-oscillator-as-a-product idea was crystallized by **Émilie Gillet / Mutable Instruments** in **Braids (2013)** and especially **Plaits (2018)** — a Eurorack "macro oscillator" module with **16 synthesis models** spanning virtual analog, waveshaping, 2-op FM, formant, **24-harmonic additive**, wavetable, chord, speech, granular, filtered noise, "dust" particle resonators, **Karplus-Strong**, **modal resonator**, and analog kick/snare/hat models (pichenettes.github.io/mutable-instruments-documentation/modules/plaits). Mutable's firmware and DSP were **released open-source (MIT)**, and that code propagated widely — Behringer Brains, Arturia MicroFreak oscillators, VCV Rack ports, and numerous others (synthanatomy.com/2021/06/behringer-brains-macro-oscllator-with-15-mutable-instruments-plaits-algorithms; github.com/pichenettes/eurorack). **[CONFIRMED that Plaits is the genre-defining macro oscillator and its DSP is open-source and widely reused.]**

**The Meld→Plaits connection — be precise.** Lead engineer **Rob Tubb** explicitly credits Mutable / modular thinking: *"The sheer adaptability and multi-function stuff that modules can do, that was a big influence"* (soundonsound.com/techniques/ableton-live-meld). The structural parallels are striking and worth noting on air: **Plaits = "macro oscillator," Meld = "macro oscillator engines"; Plaits has TWO macro-ish timbre/morph knobs per model, Meld has TWO macros per type; Meld's "Tarp"/impulse, "Filtered Noise," swarm, FM, and resonator ideas all have Plaits cousins.** **[LIKELY — strong design-lineage inference; CONFIRMED only as far as Tubb's "Mutable was a big influence" quote.]** **[FLAG — do NOT claim Meld *contains* Plaits' open-source code; no source states code reuse. Frame as "same lineage / acknowledged influence," not "Plaits inside Meld."]**

**Where physical modelling actually lives in the lineage (the subtitle origin).** *Plaits* genuinely contains **Karplus-Strong** and **modal-resonator** physical models (pichenettes.github.io/.../plaits). **Meld inherited the *modal-resonator* idea as the Plate/Membrane Resonator *filters*** — but **not** a Karplus-Strong oscillator. So "physical modelling" is a *thread* in the lineage that surfaces in Meld only as resonator filters. This is the accurate, honest version of the "hybrid" claim. **[CONFIRMED via the two source sets.]**

### Pass 3 — MPE as an expressive paradigm

**MIDI Polyphonic Expression (MPE)** is an extension of MIDI 1.0 (formally adopted by the MIDI Manufacturers Association in 2018) that gives **each note its own MIDI channel**, so **pitch bend, a Y-axis "Slide" (CC74), and per-note pressure** can be controlled **independently for every finger** — impossible in legacy MIDI, where bend/aftertouch are channel-global. Hardware that popularized it: **ROLI Seaboard, LinnStrument, Roli Lightpad, Push 3 (MPE mode)**. **[CONFIRMED — standard MIDI history; flag as general knowledge, not a single-source claim.]**

**Why MPE matters for synthesis, not just playing.** MPE turns the *performance gesture* into a **per-voice modulation source**. In Meld this is the whole pitch: per-note **Press** and **Slide** are matrix sources, so finger pressure and vertical position can drive an oscillator macro, filter, or LFO depth **per note**. This collapses the old divide between "the patch" and "the performance" — the timbre is *played*, not just triggered. **[CONFIRMED — Meld manual + Ableton blog framing.]**

### Pass 4 — Where Meld sits among Live's synths (the four-instrument map)

Live's Suite synths now span the four classic methods plus Meld's hybrid:
- **Operator** — **FM** (Bessel-sideband spectrum *generated* from sine operators; modulation index ≈ modulator Level; feedback only on un-modulated operators; 11 algorithms; Coarse integer / Fine fraction). [Episode 1]
- **Analog** — **subtractive / virtual-analog** (two oscillators → filters). [Analog episode]
- **Wavetable** — **wavetable** (scan Position through interpolated single-cycle frames). [Episode 3]
- **Meld** — **macro-oscillator hybrid** (pick a complex algorithm, two macros, two engines, MPE). [Episode 4]

The teaching arc across the course: **Operator builds spectra, Wavetable scans spectra, Meld picks whole algorithms and plays them with the body.** Meld is the "breadth + performance" capstone — the synth you reach for when you want *character and texture fast* and want to *play it expressively*, not when you want to engineer a spectrum from first principles. **[Editorial synthesis — grounded in the per-instrument sources above.]**

---

## SECTION 3 — Artist / Track Deep Dives (CONFIRMED vs PLAUSIBLE vs UNVERIFIED)

> **Honesty preamble.** Meld is a **2024** instrument. There is **no canon of famous records made with Meld**, and almost no confirmed artist statements naming it yet. This section therefore splits into (a) **macro-oscillator / Plaits** users [some CONFIRMED], (b) **MPE** artists [CONFIRMED for the paradigm], and (c) **honest negatives / cautions**. **Mark everything; invent nothing.** No artist quote about Meld specifically should be asserted unless it carries a URL — and as of this research, I found none worth stating as fact.

### Macro-oscillator (Plaits/Braids) in practice — [CONFIRMED at module level]

- **Plaits is one of the best-selling Eurorack modules ever** and is ubiquitous in modular/IDM/ambient setups; its open-source DSP put macro-oscillators into Behringer Brains, Arturia MicroFreak, VCV Rack, and more (synthanatomy.com/2021/06/behringer-brains-macro-oscllator-with-15-mutable-instruments-plaits-algorithms). **[CONFIRMED]** Use this to establish that *macro-oscillator synthesis is a real, widespread practice* — Meld is the DAW-native entry into it.
- **[UNVERIFIED — do NOT name specific famous tracks "made with Plaits."]** Despite Plaits' ubiquity, track-level confirmations ("X song uses Plaits") are rarely documented in interviews. Resist the temptation to attribute. Safe framing: *"Plaits is everywhere in modular electronic music; pinning it to a specific hit is usually guesswork."*

### MPE artists — [CONFIRMED for the paradigm, per-track UNVERIFIED]

- **Jordan Rudess (Dream Theater)** is a prominent, *documented* MPE/Seaboard and Continuum performer and an outspoken advocate of per-note expression. **[LIKELY — well-documented advocate; verify a specific quote/URL before stating verbatim.]**
- **The ROLI Seaboard / Continuum / LinnStrument community** (e.g., players like **Marco Parisi**) demonstrates MPE expressivity. **[LIKELY]** Use to *illustrate the paradigm*, not to claim Meld usage.
- **[FLAG]** Do not claim any named artist has released a track using **Meld** specifically. I found no such confirmed claim.

### IDM / electronic relevance — honest mapping

- **Aphex Twin (Richard D. James)** — relevant to the *paradigm* (per-note design): the **Waldorf Iridium MK2 Per-Note Parameter Locks** were *"the result of a collaboration with legendary Aphex Twin"* (musicradar.com/music-tech/synths/waldorf-upgrades-its-iridium-desktop-synth-with-a-little-help-from-aphex-twin — **[CONFIRMED collaboration]**), and his Novation Bass Station II "AFX Mode" (2019) shows the same per-note-parameter obsession that **MPE in Meld** serves. **[FLAG — this connects Aphex to the *idea of per-note timbre control*, NOT to Meld. No source links James to Meld. State the connection as thematic, not factual usage.]**
- **Autechre** — the *"modulate a parameter instead of writing notes"* / self-sequencing-timbre aesthetic (custom Max/MSP from *Confield* on; documented in soundonsound.com/people/autechre-techno-logical) maps perfectly onto **Meld's loop-mode Mod-Env → oscillator-macro** trick. **[LIKELY as an aesthetic analogy; UNVERIFIED as Meld usage.]**
- **Squarepusher (Tom Jenkinson)** — emphatically builds his own tools in Reaktor and avoids off-the-shelf presets (soundonsound.com/people/squarepusher). **[CONFIRMED stance]** Use as an *honest negative*: a Squarepusher-type would treat Meld's macros as raw material, not finished sounds. Don't claim he uses Meld.
- **Honest negatives worth stating on air:** there is **no confirmed Aphex/Autechre/Squarepusher Meld track**. The defensible claim is the *aesthetic kinship* between Meld's per-note + self-sequencing-timbre capabilities and the IDM tradition — clearly framed as kinship, not credit. **[CONFIRMED as an honest framing.]**

---

## SECTION 4 — Song Curation & Demo Mapping

> **Method note.** Because Meld has no confirmed track canon, this section pairs **each Meld concept** with (a) a **catalog track that demonstrates the *underlying technique*** (with confidence flag + gear attribution) and (b) a **demo recipe to reproduce the concept in Meld**. Tracks are chosen for *technique illustration*, not Meld-usage claims. Lean IDM/electronic. **Verify timestamps by ear before stating on-mic.**

### Concept 1 — Macro-oscillator breadth (one knob, whole new timbre)

- **Reference track — Plaid, *Polymer* (2019), scanning/morphing textures throughout.** Gear — **[CONFIRMED]** Tone2 Icarus + Madrona Polymer, *"making and scanning through wavetables"* (headphonecommute.com/2019/09/17/interview-with-plaid). Used here as the *"timbre-as-the-composition"* exemplar, not a Plaits/Meld claim.
- **Meld demo.** Engine A, hold one note, sweep **Macro 1** on **Basic Shapes** (Shape) then switch the *type* to **Harmonic FM**, **Swarm Saw**, **Rain** — same note, radically different worlds. **Teaches: the macro-oscillator promise — breadth from two knobs.**

### Concept 2 — FM with feedback, the macro way

- **Reference — any classic FM-feedback growl (Operator/DX-style bass).** Use the course's own Operator episode FM material as the callback. **[Internal callback]**
- **Meld demo.** Engine A → **FM Bass (Squelch)**: Macro 1 = FM Amount, **Macro 2 = Feedback** (the one place Meld exposes operator feedback — mirrors Operator's feedback-only-on-unmodulated-operator rule conceptually). Drive up for the squelch. **Teaches: Meld's FM family + feedback as a macro.**

### Concept 3 — "Real-world" texture oscillators (Rain / Bubble / Crackle)

- **Reference — Boards of Canada-style field-recording ambience** (analog + sampled texture — gearnews.com/boards-of-canada-sound-perfect-match — **[CONFIRMED gear is analog/sampler, NOT Meld]**). Used as the *aesthetic target* for environmental texture.
- **Meld demo.** Engine A → **Rain** (Tone/Rate) or **Crackle** (Density/Intensity); route **Mod Env (Loop) → Macro** for evolving weather; Engine B → a quiet **Sub** for body. **Teaches: synthesized environmental texture as an oscillator, not a sample.**

### Concept 4 — Bi-timbral layering (two synths, one note)

- **Reference — ODESZA-style "movement everywhere" layered lead** (Serum + Massive, community-inferred — productionmusiclive.com — **[INFERRED]**). Illustrates two-layer richness.
- **Meld demo.** Engine A → **Swarm Saw** (anthemic body), Engine B → **Harmonic FM** an octave up (glassy overtone layer), each with its own filter; **A's LFO 1 → B's macro** for cross-engine motion. **Teaches: bi-timbral layering + cross-engine modulation.**

### Concept 5 — Scale-aware swarm / chord-of-timbres

- **Reference — generative/microtonal ambient (e.g., modular Plaits chord patches).** **[UNVERIFIED track-level; CONFIRMED that scale-aware swarm is a Meld feature.]**
- **Meld demo.** Engine A → **Swarm Sine (♭♯)**, raise **Spacing** so partials spread — they **snap to the Live Scale** instead of going inharmonic. Hold a chord; each note stays in key. **Teaches: scale-aware oscillators — Kleine's "must-have."**

### Concept 6 — Self-sequencing timbre (loop-mode envelope → macro)

- **Reference — Autechre, *Confield*-era self-generating patterns** (custom Max/MSP — soundonsound.com/people/autechre-techno-logical — **[CONFIRMED method, INFERRED per track]**). The aesthetic target: motion from modulation, not from notes.
- **Meld demo.** Engine A, **Mod Env → AD Loop**, route it to **Macro 1**; hold ONE note. The timbre sequences itself. Add audio-rate **LFO 1 (≈200 Hz) → filter** for sideband grit. **Teaches: the line between sequencing and synthesis dissolving — Meld's loop-mode trick.**

### Concept 7 — Per-note MPE expression

- **Reference — MPE/Seaboard performance (Jordan Rudess-style per-note bends/pressure).** **[LIKELY advocate; per-track UNVERIFIED.]**
- **Meld demo.** MPE tab → **Press → Macro 1**, **Slide → Filter macro**, **Note Pitch Bend → Detune**. On an MPE controller, each finger morphs its own note. (Without MPE: Press falls back to channel aftertouch — still works, less granular.) **Teaches: the headline MPE paradigm.**

### Concept 8 — Shepard's Pi (the endless illusion) — great radio

- **Reference — Shepard-tone usage in film/electronic music (e.g., the "endless rising" illusion).** **[CONFIRMED as a phenomenon; no Meld track claim.]**
- **Meld demo.** Engine A → **Shepard's Pi** (Rate/Width); let it run under a pad. **Teaches: a psychoacoustic-illusion oscillator built into a stock synth — and a memorable cold-open candidate.**

### Honest-negatives / myth-buster beat (good radio)

- **"Meld is a physical modeller."** **FALSE.** It's a macro-oscillator synth; only the Plate/Membrane *Resonator filters* are modal/physical-modelling-flavoured (Correction 1, top of dossier).
- **"Meld came in 12.1."** **FALSE** — 12.0, March 2024 (Correction 2). The **Chord** oscillator is the only Meld feature added later (12.2).
- **"Meld has Plaits' code inside it."** **UNSUPPORTED** — acknowledged *influence* (Tubb), not documented code reuse. Say "lineage," not "contains."

---

## SECTION 5 — Technical Synthesis Depth

### 5.1 The macro-oscillator abstraction — what's really happening

A macro-oscillator is **a parameterized DSP algorithm with a deliberately reduced control surface**. Internally, each Meld type is a different signal-generation routine (a VA oscillator bank, an FM operator pair, a noise-buffer loop, a swarm of detuned partials, a modal exciter); the **two macros are mapped, per type, onto the few internal parameters that matter most musically** (e.g., on Harmonic FM, Macro 1 = modulation depth/index, Macro 2 = C:M ratio; on Square Sync, the two macros are the two oscillator frequencies). The design tradeoff is explicit: **you lose the full parameter set, you gain instant range and playability** (ableton.com/en/packs/meld; docs.cycling74.com/reference/abl.dsp.meldosc~). **[CONFIRMED definitional + per-type macros from DSP ref.]**

### 5.2 DSP families inside Meld — how each generates sound

- **Virtual-analog (Basic/Dual Basic/Noisy Shapes, Square 5th/Sync, Sub, Chord):** classic band-limited geometric waveforms (saw/square/tri/pulse) with morphing and PWM. Square Sync is **hard-sync** (one osc resets another → formant-rich spectrum). Square 5th adds a fifth-up copy. **[CONFIRMED via descriptions.]**
- **FM (Simple/Harmonic/Fold FM, FM Bass/Squelch):** carrier + modulator sine pair(s). Harmonic/Simple FM expose **index (Amount)** and **ratio**; **Fold FM** adds **wavefolding** after FM for extra harmonics; **Squelch** exposes **operator feedback** (a sine operator modulating itself → sawtooth-toward-noise as feedback rises). **[CONFIRMED.]** **Callback to Episode 1:** modulation index ≈ modulator depth; feedback is self-modulation — same Bessel-sideband physics as Operator, but collapsed to two macros.
- **Swarm (Saw/Sine/Square/Triangle):** a **supersaw-style cluster** of many detuned copies — **Motion** animates the detune, **Spacing** sets the frequency spread; spectrum approaches a dense, additive-like comb. Scale-aware variants quantize the spread to the scale. **[CONFIRMED.]**
- **Buffer-loop / "granular-esque" (Noise Loop, Extratone):** a short buffer (noise, or a kick-drum oscillator) **retriggered/looped at audio rates** so the loop period sets pitch and the content sets timbre — *granular-esque*, not true granular clouds (Ableton's own hedge). **[CONFIRMED — and flag the "granular-esque" caveat.]**
- **Noise / environmental (Filtered Noise, Bubble, Crackle, Rain):** stochastic generators — band-pass-filtered noise (resonant → pitched), and *modeled* particle/bubble/rain processes (density/intensity/spread controls a swarm of synthesized events). **[CONFIRMED.]** These are the closest Meld gets to *generative texture synthesis*.
- **Lo-fi (Bitgrunge, Chip):** deliberately quantized/aliased square-wave generators — Bitgrunge is *"pseudo-random lo-fi square,"* Chip is a chiptune oscillator with interval. The aesthetic is **embraced digital nastiness** (cf. the Wavetable-episode PPG-grit thread). **[CONFIRMED.]**
- **Special (Shepard's Pi, Tarp):** Shepard's Pi = a **Shepard/barberpole tone** (stacked octaves crossfading → endless-glide illusion); Tarp = an **impulse/drum excitation** (decay + tone) — useful as a percussive exciter, and the nearest thing to a "physical exciter" oscillator. **[CONFIRMED.]**

### 5.3 The modal-resonator filters — the one true physical-modelling element

The **Plate Resonator** and **Membrane Resonator** filters are **modal resonators**: they impose a bank of resonant modes (the natural frequencies of a plate / a drum membrane) onto whatever the oscillator feeds them — i.e., a *resonant-body model* applied as a filter. Made **scale-aware**, their modal frequencies *"snap … into tune with your track"* (soundonsound.com/techniques/ableton-live-meld). This is genuine physical-modelling DSP (modal synthesis) — but it is a **filter on an oscillator**, not a self-contained Karplus-Strong string. **This is the precise, honest core of any "hybrid / physical-modelling" framing.** **[CONFIRMED.]**

### 5.4 MPE routing — the signal path of a finger

On an MPE controller, each note occupies its **own MIDI channel**, carrying three continuous per-note streams: **per-note pitch bend** (X), **Slide / CC74** (Y), and **per-note pressure** (Z). Meld's **MPE tab** exposes these as **per-voice matrix sources**; routed to an oscillator macro, filter macro, or LFO depth, they modulate **each voice independently** (ableton.com/en/manual/live-instrument-reference). The DSP consequence: **the modulation matrix runs per-voice**, so the same patch produces different timbres on simultaneously-held notes — the defining capability MPE adds over channel-global MIDI. **[CONFIRMED — manual + standard MPE definition.]**

### 5.5 Why bi-timbral matters (DSP and musical)

Two **independent voice paths** summed at the output means: (1) **two different synthesis methods at once** (e.g., a granular-esque texture + a clean sub) without a second device; (2) **independent envelopes/filters per layer** — a slow-attack pad in A under a percussive transient in B, from one note; (3) **cross-engine *control-rate* modulation** (A's LFO shapes B) for coupled-but-distinct motion. **[CONFIRMED.]** **[CAVEAT — restate]:** "bi-timbral" here = **two summed voices**, not audio-rate cross-modulation between engines (soundonsound.com). The musical payoff is **layered richness with per-layer control** — the thing you'd otherwise build with two instrument racks.

### 5.6 Precise demo recipes that make each concept UNMISTAKABLE

1. **Hear a macro do everything.** Engine A, **Basic Shapes**, hold one note, sweep **Macro 1 (Shape)** 0→100: sine→tri→saw→square. Then *change the oscillator type* live (Harmonic FM → Swarm Saw → Rain) on the same note. **The single most important demo — it isolates "two knobs, whole new instrument."**
2. **FM + feedback.** **FM Bass (Squelch)**, raise **Feedback** macro on a held note: sine → saw → noise edge. The Operator-episode callback in one knob.
3. **Scale-aware swarm.** **Swarm Sine (♭♯)**, raise **Spacing**; hold a chord; toggle Live's **Scale** — partials snap in key. Proof of scale awareness.
4. **Self-sequencing timbre.** **Mod Env → AD Loop → Macro 1**; hold ONE note; the timbre sequences itself. Add **LFO 1 ≈ 200 Hz → filter** for sideband grit. The Autechre move without writing notes.
5. **MPE per-note.** **Press → Macro 1**, **Slide → filter macro**; on a Seaboard/Push 3, each finger morphs its own note. The headline paradigm, audible.
6. **Bi-timbral split.** A = **Rain** (slow pad), B = **Tarp** (percussive transient), Link Envelopes OFF; one note plays a textured hit-plus-bloom. Proof that two synths live in one note.
7. **Modal resonator = the "physical" hook.** Any bright oscillator → **Plate Resonator** filter, scale-aware ON; pluck-like, body-resonant tone. *"This — and only this — is the physical-modelling part."*

---

## SECTION 6 — Episode Script Outline (~40 min)

### Cold Open (90 seconds)

**Audio bed.** Open on a **Meld "Shepard's Pi"** patch — an endless-rising barberpole tone, alone, 8 seconds, slowly resolving under the narration. (Or a slow **Rain** texture if a calmer open is wanted.)

**Opening narration (draft).** *"There's an oscillator in this synth that sounds like it's rising forever and never gets anywhere — a staircase with no top. There's another that sounds like actual rain. A third that sounds like loading a video game off a cassette tape in 1984. They all live in the same box, and you reach any of them with one knob. This is Meld — Ableton's newest synthesizer, and the strangest of the four. The last three episodes, we built sounds: we generated spectra with FM in Operator, we scanned spectra in Wavetable, we subtracted them in Analog. This episode we do something different. We don't engineer a sound — we **pick** one, from twenty-five ready-made worlds, two at a time, and then we play it with our fingers. Because here's the thing the manual buries: Meld was built for ten fingers, not one. By the end of this walk you'll know why the most important part of this synth isn't an oscillator at all — it's the matrix that lets every note you hold be a different sound under a different finger. Two corrections before we start, because I got them wrong too: Meld is **not** a physical-modelling synth — that's a myth we'll bust — and it didn't arrive in some point-update, it shipped the day Live 12 did. This is Episode Four. This is Meld."*

Cut to title music — a bi-timbral Meld patch (Swarm Saw + Harmonic FM), 4 seconds. Then Section 2.

### History & Theory: macro-oscillators + MPE (8–9 min)

- **Beat 1 (90s). What a macro-oscillator is.** Two knobs, a whole algorithm behind each. The tradeoff: breadth + playability vs deep editing. *"You don't build the sound, you pick it."*
- **Beat 2 (150s). The Plaits lineage.** Émilie Gillet / Mutable Instruments, Braids (2013) → Plaits (2018), 16 models, open-source DSP that spread everywhere (Behringer Brains, MicroFreak, VCV). **Drop Rob Tubb's quote:** *"The sheer adaptability and multi-function stuff that modules can do, that was a big influence."* **Myth-bust gently:** Meld is *lineage*, not Plaits-code-inside. **And the physical-modelling thread:** Plaits really has Karplus-Strong + modal models; Meld inherited only the *modal resonator*, as a filter — *"so 'physical modelling hybrid' is half-true at best; we'll show you exactly which half."*
- **Beat 3 (120s). MPE as a paradigm.** Per-note channel, bend/Slide/pressure per finger; ROLI/LinnStrument/Push 3. *"The patch and the performance stop being separate things."* Aphex's per-note obsession (Iridium collab, AFX Mode) as the IDM kinship — **framed as kinship, not Meld credit.**
- **Beat 4 (90s). Where Meld sits.** The four-synth map: Operator generates, Wavetable scans, Analog subtracts, **Meld picks-and-plays.** Suite, March 2024, Christian Kleine + Rob Tubb. Kleine: *"It's two synthesizers in one … the sum bigger than its parts."*

### Synthesis Deep Dive (8–9 min)

- **Beat 1 (120s). The 25 oscillators, by family.** VA / FM / Swarm / buffer-loop / noise-environmental / lo-fi / special. **Live demo: hold one note, change the type live** — Basic Shapes → Harmonic FM → Rain. *"Same note. Three instruments."*
- **Beat 2 (120s). FM, the macro way (callback to Ep 1).** Harmonic FM = index + ratio; Squelch = **feedback macro**. *"Last time it took a whole algorithm grid; here it's two knobs — same Bessel sidebands underneath."*
- **Beat 3 (90s). The modal resonators — the ONE physical-modelling part.** Plate/Membrane resonator filters; scale-aware; *"a model of a drumhead, used as a filter."* **Demo: bright osc → Plate Resonator.** *"This is the 'physical modelling' in the subtitle — and it's a filter, not the oscillator. Correction logged."*
- **Beat 4 (120s). Scale-aware oscillators.** Six of them; swarms and chip snap to the Live Scale. **Demo: Swarm Sine, raise Spacing, change scale.** Kleine: *"a must-have for any modern synth."*
- **Beat 5 (90s). LFOs into audio rate + loop envelopes.** LFO to 200 Hz = back-door FM/AM; LFO 1 vs LFO 1 FX as two sources; **Mod Env AD-Loop → macro** = self-sequencing timbre (the Autechre move).

### Meld Deep Dive — architecture (8–9 min)

- **Beat 1 (90s). Bi-timbral = two full engines.** Each with osc + filter + 2 env + 2 LFO + matrix. **Caveat on air:** they **sum**, they don't audio-rate-FM each other; cross-engine modulation is control-rate. *"Two synths, one note, one box."*
- **Beat 2 (120s). The two macros + the matrix.** Two macros per oscillator are first-class matrix targets — *"the macro is the new Position."* ~23 targets; sources = LFOs, envs, MIDI, MPE, and the *other engine*. **Demo: route LFO 1 → Macro 1.**
- **Beat 3 (120s). MPE, hands-on.** MPE tab: Press / Slide / Note Bend → macros & filter. **Demo on an MPE controller (or fallback to aftertouch):** each finger morphs its own note. *"This is what the whole thing was built for."*
- **Beat 4 (90s). Filters, mixer, global.** 17 filter types incl. phaser/comb/vowel/lo-fi/resonators; per-engine Volume/Pan/Tone; global Drive + Limiter; Poly/Mono, glide (Portamento/Glissando), Stacked Voices + Spread. **(Flag the 12-vs-32 voice cap as TBD-verify.)**
- **Beat 5 (60s). Meld vs the family.** When to reach for it: character + texture + expression, fast. When NOT to: surgical spectrum design (that's Operator/Wavetable).

### Patch Walkthrough — build one signature Meld sound (6–7 min)

**Target: a bi-timbral, MPE-played texture-lead that proves "two synths, one note, ten fingers."**

- **Step 1 (45s).** Engine A → **Swarm Saw (♭♯)**, Motion ~30, Spacing ~40; OSR/LP filter gentle. Anthemic body, scale-locked.
- **Step 2 (45s).** Engine B → **Harmonic FM** an octave up, low level; **Plate Resonator** filter on B, scale-aware ON — a glassy, body-resonant overtone layer. *"There's your 'physical modelling' — one filter."*
- **Step 3 (45s).** **A's LFO 1 → B's Macro 1** (cross-engine), slow. The two layers breathe together but differently.
- **Step 4 (60s).** **Mod Env (A) → AD Loop → A's Macro 1**, gentle: the body self-morphs on held notes.
- **Step 5 (60s).** **MPE tab:** Press → B's FM Amount; Slide → A's filter; Note Bend → A detune. Each finger now shapes its own note's timbre + brightness + pitch.
- **Step 6 (45s).** Global **Drive** up a touch, **Limiter** on; Stacked Voices 2 + small Spread for width.
- **Step 7 (30s).** Save as **"Two-Hands."** *"Operator built a spectrum. Wavetable scanned one. Meld? Meld gave you two synths and ten fingers and got out of the way."*

### IDM Application + listener exercise (5–6 min)

- **Beat 1 (90s). Self-sequencing texture (the Autechre idea).** Mod Env AD-Loop → macro, audio-rate LFO → filter; one held note becomes a pattern. *"Modulate the timbre instead of writing the notes."*
- **Beat 2 (90s). Environmental oscillators as composition.** Rain / Crackle / Bubble as the *source*, not an effect; layer a Sub in Engine B. The BoC-adjacent texture target, synthesized not sampled.
- **Beat 3 (60s). The Shepard trick.** Shepard's Pi under a pad for an endless build; great for IDM tension. (Tie back to the cold open.)
- **Beat 4 (120s). The listener exercise.** *"Homework for the walk home. Open Meld. Engine A only. Hold exactly one note — and don't play another for forty seconds. Your only job: make that one note tell a story. Change the oscillator type once. Loop a mod-envelope onto a macro so the timbre moves on its own. If you've got an MPE controller, press harder and slide your finger and hear the sound bend to your hand. No chords. No new notes. Just one note and the matrix. If you can make forty seconds of music that way, you've understood the whole point of this strange synth: that Operator and Wavetable ask you to design a sound, but Meld asks you to **perform** one — to pick a world, layer a second one underneath it, and play both with your fingers. It isn't a physical-modelling synth, whatever the box says. It's a macro-oscillator synth built for two hands. That's Meld."*

Outro music: the "Two-Hands" patch, MPE pressure trailing off, fade to silence. End ~40:00.

---

## Conclusion

The thesis across all six sections: **Meld is a bi-timbral, dual macro-oscillator, MPE-first synth — not a physical modeller — whose center of gravity is breadth and performance, not spectrum-engineering.** You **pick** one of 24+1 ready-made oscillator algorithms (collapsed behind two macros), run **two full engines** at once, snap them to your **scale**, and **play them per-note over MPE**. Its lineage is **Mutable Instruments' Plaits** (acknowledged influence via Rob Tubb, not code reuse), and the *only* genuinely physical-modelling DSP in it is the **modal Plate/Membrane resonator filters** — the honest, narrow truth behind the "hybrid" label. Against the rest of Live's Suite — Operator (FM generation), Wavetable (spectral scanning), Analog (subtractive) — Meld is the **"pick-and-play"** capstone: the synth for *character, texture, and expression, fast.* For the physicist-producer, the clean picture: **Operator generates spectra, Wavetable interpolates between them, Meld parameterizes whole algorithms behind two macros and routes your fingers into them.**

---

### Source-reliability notes (verify before recording)

- **Subtitle "Physical Modelling Hybrid" is INACCURATE** — Meld is a macro-oscillator synth; only the **Plate/Membrane Resonator filters** are physical-modelling-flavoured (modal). Correction logged at top. **Change the subtitle.** [CONFIRMED]
- **Version: Meld shipped Live 12.0, 5 March 2024**, NOT 12.1. The brief and a coordinator note both said "12.1" — both wrong. **Chord** oscillator added in **12.2**. User is on 12.4 (all features present). [CONFIRMED]
- **Edition: Suite-only** device (compare-editions). The "Live 12 Lite or higher" on the **pack** page refers to the preset pack, not the device. [CONFIRMED]
- **Oscillator count: 24 types at 12.0; 25 at 12.2+ (Chord).** Full named list from the Ableton DSP reference `abl.dsp.meldosc~` (primary). [CONFIRMED]
- **Bi-timbral = two summed engines, control-rate cross-mod only** — NOT audio-rate cross-modulation between engines. [CONFIRMED via SOS]
- **Plaits lineage is acknowledged INFLUENCE (Tubb quote), not documented code reuse.** Say "lineage," never "Plaits inside Meld." [LIKELY/CONFIRMED-as-influence]
- **No confirmed artist/track uses Meld** (2024 instrument). All Section 3/4 tracks illustrate *techniques*, not Meld usage. Aphex/Autechre/Squarepusher framed as **aesthetic kinship**, never as Meld credit. [CONFIRMED honesty stance]
- **Voice cap (12 vs 32) UNRESOLVED** between two manual reads — verify in the live device; say "up to a few dozen" if unstated. [UNCERTAIN]
- **Exact LOM parameter ranges / normalized-vs-Hz for macros** not in public docs — **inspect the live device before headless rendering.** Macros are normalized (0–1 / 0–100%), not Hz. [LIKELY]
- **MPE history (per-note channel, 2018 MMA adoption)** is general MIDI knowledge, flagged as such.
- Several sources reached via search summaries rather than direct fetch (some Ableton manual/SOS pages and the DSP ref); the 24-type table is corroborated across the DSP reference and two independent searches. No URLs or quotes were fabricated; uncertain items are flagged.
