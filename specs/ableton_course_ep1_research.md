# Operator: The FM Machine — Episode 1 Research Dossier

A complete research artifact for a 40-minute walking podcast aimed at an experienced Ableton Live 12 Suite user who is also a physicist and IDM producer. Six sections, ~6,500 words of dense research, designed to be cut directly into a script.

---

## SECTION 1 — Ableton Operator: Full Parameter Reference (Annotated)

Operator is, strictly, a **4-operator phase-modulation synthesizer**. Robert Henke (Monolake; Ableton co-founder) confirms: *"this is technically not really frequency modulation but phase modulation, which provides very similar sonic results whilst being significantly easier to calculate"* (roberthenke.com/technology/operator.html). What Yamaha called FM in the DX7 was also PM under the hood; Operator inherits that lineage exactly. It first shipped with **Live 4 in late 2004**, was sold as a $149 standalone add-on starting **20 January 2005**, and was prototyped under the codename **"Onyx"** by Henke (design), Matthias Mayrock (C++ implementation), and Torsten Slama (UI). Henke modelled it on his personal **Yamaha DX27** — which is why Operator is 4-op rather than 6-op. The name itself is an explicit homage to Yamaha's term for DX-series oscillators.

### 1.1 Oscillator section (A, B, C, D — identical controls)

Each operator is a colour-coded "shell" (yellow A, green B, blue C, orange D) feeding a context-sensitive central LCD — an interface paradigm that subsequently propagated through every Live device.

| Parameter | Behaviour |
|---|---|
| **On** | Engages oscillator output / modulator path. |
| **Coarse** | **[KEY PARAM]** Frequency *multiplier*, not octave selector. Steps 0 → 0.25, 0.5, 0.75, 1, 2, 3 … up to 32. The C/M ratio determines harmonic vs inharmonic spectrum. **[COMPARE: hardware]** DX7 max is 31.99; Operator goes to 32. |
| **Fine** | One-octave span in 1000 steps, **positive-only**. Detuning down requires lowering Coarse one octave and pushing Fine to ~980-999 — the canonical Francis Preve "supersaw" trick. **[UNDERDOCUMENTED]** The asymmetry is rarely explained by Ableton. |
| **Fixed** | Toggles to absolute Hz mode; Coarse becomes **Freq** (Hz, down to 0.1 Hz) and Fine becomes **Multi**. **[IDM USE]** Foundation for inharmonic percussion: tune modulators to primes (137, 311, 523 Hz) at small Multi against a key-tracked carrier — every key produces a different inharmonic ratio. |
| **Level** | dB output. When operator is a modulator, Level controls **modulation index I** (∝ spectral bandwidth). **[KEY PARAM]** This is the brightness control. |
| **Wave** | See waveform list below. |
| **Feedback** | **[KEY PARAM]** Only enabled when no other operator modulates this one (greys out otherwise — common gotcha). At max with sustain, sine self-feedback morphs through saw shape into broadband noise. **[IDM USE]** Modulating Feedback at audio rate via clip envelope = controllable noise gates / digital fizz. |
| **Phase** | 0–100% start phase. **Retrigger (R) toggle** sets free-run vs reset-on-note-on. **[UNDERDOCUMENTED]** With R OFF the four oscillators free-run analog-style: amplitude/phase variance per note and click suppression on slow attacks; with R ON they retrigger at the Phase value (kick-drum click design relies on this). With Spread on, free-run phases differ between L/R, doubling the chorus depth. |
| **Osc<Vel** | Velocity → oscillator pitch with a **Q (quantize)** toggle. Q on jumps Coarse by integer harmonics for instant velocity-driven timbre changes; Q off glides inharmonically. **[IDM USE]** Drive Osc<Vel of a modulator with carefully placed velocities and Q on for programmable harmonic gestures locked to the harmonic series. |
| **Repeat** | Harmonic-repeat in the additive editor (¼, ½, etc.); duplicates harmonic content above the visible bar-graph window for high-frequency shimmer. **[UNDERDOCUMENTED]** |

**Available waveforms** (all four operators share this list — the lo-fi options are the prized IDM tools): Sine, **Sine 4** (4-bit quantized — chip-grit, audible odd harmonics), **Sine 8** (8-bit quantized), **Saw D** (digital, ∞-bandwidth, aliases harshly at high notes — Henke confirms by design), **Saw W** (Sw3, Sw6, Sw12, Sw32 band-limited variants), **Square D**, **Square W** (Sq3 → Sq32), **Triangle**, **Noise** (real-time pink, untunable), **NoiseLoop** **[KEY PARAM] [COMPARE: hardware]** — a 1024-sample cyclic random LUT, **tunable** (no DX7 equivalent; Henke: *"bad noise as a feature"*), and **User** — a 64-partial additive editor (Live 8, 2009). Right-click User → Export AMS allows drag-into-Sampler as single-cycle wavetables.

### 1.2 Per-operator envelopes (one per oscillator + Filter + LFO + Pitch = 7 envelopes total)

Each envelope exposes **A/D/S/R** plus **Initial / Peak / Sustain / End** levels and **draggable slope curves** (linear vs exponential per segment, exponential being the DX7-style default). The five **loop modes** are the genuine power tool:

| Mode | Behaviour |
|---|---|
| None | Standard ADSR. |
| Loop | Re-triggers Attack-Decay segments while note held; rate set by envelope times. |
| Beat | Re-triggers at tempo-quantised beat division (1/16, 1/8, etc.). |
| Sync | Same as Beat but quantised to song-position grid. |
| Trigger | One-shot, ignores note-off — essential for percussive patches. |

**Time<Vel** (bipolar; harder velocity shortens or lengthens), **Time<Key** (high notes shorten — mimics natural string decay), and **R<Vel** are common to all seven envelopes. **[IDM USE]** Loop mode in modulator envelopes is a built-in arpeggiator/rhythmic-FM gate without an external sequencer; Sync at 1/16 on a B-modulator yields glitch-pattern timbral wobble locked to the grid. **[UNDERDOCUMENTED]** A long-standing forum-confirmed quirk (forum.ableton.com t=217479): the pitch envelope's LFO destination accidentally modulates LFO rate too — a bug-or-feature.

### 1.3 LFO

Shapes: Sine, Square, Triangle, Sample & Hold, Noise (smooth random). **Rate** in Hz or tempo-synced; **Range** chooser **Low / Hi / Hi audio** — in Hi the LFO reaches ~12 kHz so it functions as **a fifth audio-rate operator**. **[KEY PARAM] [IDM USE]** This is the killer Operator trick: route the audio-rate LFO simultaneously to A, B, C and D pitch destinations to synthesise routings the 11 algorithms don't otherwise allow. **R<Key** at 100% makes LFO frequency double per octave (it behaves like a true oscillator). **[UNDERDOCUMENTED]** The LFO has its own ADSR envelope on its amount — most users don't realise the LFO is itself a fully-enveloped modulation source.

### 1.4 Filter section

The filter sits **at the very end of the chain, after each operator's amp envelope** — there is no global VCA after it, so high resonance with self-oscillating circuits can ring indefinitely. **[COMPARE: hardware]** The DX7 had no filter at all; Henke originally didn't want one either: *"I wanted a 'pure' FM machine. But ultimately I agreed."*

Types (Live 9.5+, present in Live 12): LP 12 / LP 24 / HP 12 / HP 24 / BP / Notch / **Morph** (single-knob LP→BP→HP→Notch sweep). **Circuit models** are Cytomic-developed (Andy Simper): **Clean** (linear SVF, identical to EQ Eight), **OSR** (Oxford OSCar SVF with diode-clipped resonance), **MS2** (Korg MS-20 Sallen-Key with soft-clipped resonance, LP/HP only), **SMP** (hybrid OSR/MS2), **PRD** (Moog Prodigy ladder). Parameters: Frequency, Resonance (up to 125%, self-oscillating), **Drive** (per-circuit overdrive), Envelope amount (bipolar), Env<Vel, Key (cutoff tracks MIDI note 0–100%), LFO Amt.

### 1.5 Pitch / Global ("Aux Env")

Exposed in routing menus as **Aux Env** — a single global pitch envelope with the same I/P/S/E shape as the operator envelopes. **[UNDERDOCUMENTED]** Its destinations are user-routable to LFO rate, individual oscillators, filter, or volume — which is why the routing menu lists "Aux Env" rather than "Pitch Env."

Other global parameters: **Voices** (1–32 polyphony cap; Voices=1 + Glide on = mono lead), **Glide / Portamento** (polyphonic), **Time** (pitch-envelope segment time), **Spread** **[KEY PARAM] [UNDERDOCUMENTED]** — stacks two voices, hard-panned L/R, detuned by the Spread amount, with *all random elements (free-run osc phase, LFO random, NoiseLoop seed) independent per channel*. Spread is therefore not a simple chorus — it's two semi-independent voice instances costing 2× CPU per note, inspired by the Synclavier II. **[IDM USE]** Spread + free-run phase + slow envelope on a 39:1 modulator = endlessly evolving stereo cloud (Boards-of-Canada-style washes). **Transpose** (±48 semitones), pitch-bend range, modwheel and aftertouch routing in the Modulation pane.

### 1.6 Global pane

| Parameter | Behaviour |
|---|---|
| **Time** | **[KEY PARAM]** Master scaler for all seven envelopes simultaneously, modulatable by velocity/key/LFO/Aux-env. Henke: *"Every synth needs this."* |
| **Tone** | Global low-pass at the *modulation input* of each operator — tames aliasing in cascading FM stacks. **[UNDERDOCUMENTED]** Sometimes labelled "Global Tone." |
| **Volume** | Master output. |
| **Antialias** | Toggle. Henke recommends leaving off for metallic/cymbal patches because the aliasing fold-back *is* the sound. |
| **Interpolation** | High-quality interpolation for low-frequency complex waves. |
| **MPE** (Live 12) | Operator now responds to per-note pitch, slide, pressure (added 2024). |

**Note on the brief's "Effects pane":** Operator does **not** contain a chorus/delay/reverb effects pane. Its on-board "effects" are the Cytomic filter (with Drive), the global Tone filter, and the Spread stereo doubler. For traditional FX you follow Operator with Live's Chorus-Ensemble, Echo, Reverb. Live 12 added MPE support, MPE-aware modulation, and theme integration to Operator; the major sonic upgrades remain Live 9.5 (Cytomic filters) and Live 8 (additive editor + antialias).

### 1.7 The 11 algorithms

Operator's algorithm icons read **top-to-bottom = signal flow into the bottom-row carriers, summed**. An operator at the top of any column has Feedback available.

1. **D→C→B→A** — pure linear stack; classic 4-op DX-style "telephone bell." Only A is heard.
2. **D→C→B; B + parallel unmodulated A** carry to output.
3. **D→C; C modulates B and A in parallel** — single mod feeding two stacked carriers.
4. **D→C→A and B→A** — D-C stack and B both modulate A.
5. **D, C, B all modulate A in parallel** — three parallel modulators, one carrier; excellent for envelope-controlled timbral layers.
6. **D→C→B→A but B also outputs** — modulator-with-tap, two carriers.
7. **D→A and C→B; A and B carriers** — two independent C/M pairs in parallel ("dual-pair" — Francis Preve's all-time favourite). **[KEY ALGORITHM]**
8. **D→B, C→A, B also modulates A** — hybrid of pair-FM and series.
9. **D modulates A, B, C in parallel; A B C all carriers** — single modulator brightens three octave-stacked carriers ("triple-carrier" trick: A=1, B=2, C=4, raise D level for spectral evolution). **[KEY ALGORITHM]**
10. **D→A plus B and C as independent carriers** — one C/M pair + two parallel oscillators.
11. **A B C D all parallel carriers, summed** — no FM at all; Operator becomes a 4-osc additive synth.

**[COMPARE: hardware]** DX7 has 32 fixed algorithms; Operator's 11 are roughly the most musically useful subset. Crucially, **the algorithm number is itself MIDI-mappable and modulatable** — a feature absent on DX7 hardware. Holding a chord while scrolling produces dramatic timbral cuts no DX7 allows.

### 1.8 Operator vs other FM softsynths

| Feature | Operator (Live 12) | NI FM8 | Dexed | Arturia DX7 V | Plogue OPS7 | TX81Z (HW) |
|---|---|---|---|---|---|---|
| Operators | **4** | 6 + saturator/filter/noise | 6 (DX7-exact) | 6 + extras | 6 (bit-accurate) | **4** (OPZ) |
| Algorithms | 11 fixed | **Free routing matrix** | 32 (DX7) | 32 + extras | 32 + extended | 8 |
| SYSEX import | **No** | DX7 | **DX7-exact** | DX7 | **Hardware-accurate DX7** | n/a |
| Filter | 7 types × 5 Cytomic circuits | basic | none | modern | none | none |
| DAW integration | **Native** (clip env, M4L, MPE) | VST/AU | LV2/VST/AU **free** | VST | VST | hardware |

For a 6-op linear stack you get up to five nested PM modulations, producing inter-modulation products combinatorially richer than 4-op can manage. Compensate in Operator by: (1) using non-sine carrier waveforms (Sine 4, SawW, additive User — a 32-partial User wave plus one modulator already approximates three-deep DX7 sine FM); (2) layering Operator instances in an Instrument Rack; (3) audio-rate LFO as effective fifth operator. Use **Dexed** when bit-accurate DX7 SYSEX recall matters (Eno patches, Lately Bass); reach for **FM8** when 6-op linear stacks or the modulation matrix are needed; reach for **Plogue OPS7** for hardware-accurate DX7 output.

### 1.9 Power-user / IDM techniques

(1) **Inharmonic percussion via Fixed mode** — all four operators Fixed, primes at small Multi, Trigger envelopes with short decays, DFM-1 12 dB filter with Drive at 6–8 dB. (2) **Spread for chorus-without-comb-filtering** at 8–15% with retrigger off on at least one operator. (3) **Loop-mode envelopes for arpeggios** — modulator envelope set to Beat at 1/16, peak decay shorter than loop period. (4) **Feedback as noise generator** — Operator at top of algorithm 1, sine, max feedback, sustain at 0 dB → broadband character noise. (5) **Zero-Hz wave-shaping** — Henke's documented obscure trick: an oscillator at 0.1 Hz Fixed becomes a phase-shifted wave-shaper for whatever modulates it. (6) **Algorithm modulation** — MIDI-map the algorithm icon to a Macro / 11-step note range. (7) **AMS export → Sampler** for free wavetable synthesis. (8) **Disable Antialias** for character on cymbals and metals.

---

## SECTION 2 — FM Synthesis History: Deep Narrative

### Pass 1: Invention (Stanford, 1967)

The story begins not with mathematics but with **vibrato**. In autumn 1967, **John M. Chowning** — a percussionist who had studied composition with Nadia Boulanger in Paris before earning a 1966 doctorate at Stanford under Leland Smith — was working alone in the *dungeons* of the **Stanford Artificial Intelligence Laboratory (SAIL)** on a **DEC PDP-6/PDP-10** running David Poole's local rewrite of Max Mathews's MUSIC IV, called **MUSIC 10**. Chowning was chasing not timbre but **spatialization** — the perceptual cues by which the ear locates a sound in a room. He needed sounds with "internal dynamism" so that direct and reverberant signals would phase-decorrelate. Vibrato was the obvious tool.

In Chowning's words to Yamaha's *Hub* magazine: *"I was searching for sounds that had some internal dynamism… Vibrato is one of the ways that one can do that."* He patched two sine oscillators together — one frequency-modulating the other — and began doubling the modulator's rate. *"I was experimenting with very rapid and deep vibrato. As I increased the vibrato in speed and depth, I realized I was no longer hearing instant pitch and time."* When the modulating oscillator crossed roughly 20 Hz into the audio band, the cyclical pitch wobble vanished and was replaced by **a stable but radically new timbre** — bright, clangorous, evolving. As he later told MIT: **"It was a discovery of the ear."** An undergraduate confirmed that the standard radio-engineering equations for FM (Frederick Terman's 1947 *Radio Engineering*) held perfectly well at audio rates.

The mathematics is unreasonably economical:

**y(t) = A · sin(ω_c·t + I·sin(ω_m·t))**

Expansion via the **Jacobi-Anger identity** shows that this single equation produces sidebands at **f_c ± n·f_m** with amplitudes governed by **Bessel functions of the first kind, J_n(I)**. Crank up the modulation index I and energy migrates outward into higher-order sidebands; the spectrum literally inflates. Why this mattered on 1960s hardware: subtractive synthesis required a complex waveform plus a steep VCF; additive needed dozens of sine oscillators per voice. **FM needed only two oscillators, an adder, and a multiplier** — no filters at all. On a PDP-10 chewing samples non-real-time, this was the difference between a piece taking minutes versus hours to render.

Chowning's manuscript was **rejected by several journals before the JAES finally accepted it in 1973**. His compositions traced FM's musical maturation: **Sabelithe (1971)** opens like a percussion étude and gradually morphs through brass-like FM tones, demonstrating that one algorithm could traverse a "trumpet-to-drum" continuum. **Turenas (1972)** — quadraphonic, all-FM, the **first electronic piece to convince listeners that point sources were flying through 360° space**; Chowning fused his Doppler/distance-cued reverb localization algorithm with FM's "internal dynamism." **Stria (1977)**, commissioned by IRCAM, abandoned equal temperament entirely: **all frequency components, all temporal divisions, and all formal proportions are based on powers of the Golden Ratio φ ≈ 1.618**, producing crystalline inharmonic spectra and slowly decaying glassy reverberations. **Phoné (1981)**, from his IRCAM residency, used a custom FM configuration to model the **singing voice** — both the periodic glottal source and resonant formants — anticipating CHANT-style vocal synthesis.

The licensing saga is one of American industrial myopia. Stanford's Office of Technology Licensing shopped FM to **Hammond, Wurlitzer, and Lowrey starting around 1971** — all refused; their engineers could not follow the math. In 1973 Yamaha engineer **Kazukiyo Ishimura** flew to Palo Alto; Chowning recalled, *"I gave him some examples and showed some code — with a brief explanation — and in ten or so minutes he understood exactly what I was doing."* **Stanford signed a license to Yamaha 1973–75**. The patent — **US 4,018,121, filed 1974, granted 19 April 1977** — became the **second-most lucrative patent in Stanford history** by its 1995 expiration, generating roughly **$22.9 million in royalties** (Mix Online), surpassed only by recombinant-DNA. Chowning, ironically, had been **denied tenure** by Stanford's traditional music department; FM's success funded his founding of **CCRMA in 1975**.

### Pass 2: The DX7 Moment (1980–1989)

Yamaha's first FM hardware was *not* the DX7. The lineage runs **GS1 (1981, ~$16,000, dual 4-op, no programming) → GS2 → CE20/CE25 (1982 preset-only consumer FM) → DX1 (1983, $13,900 wood-encased flagship)**. The GS1's most famous appearance is on **Toto's "Rosanna" and "Africa"** (1982), where Steve Porcaro layered it alongside CS-80, Prophet-5, Minimoog, Hammond, and Polyfusion modular.

Then **the Yamaha DX7, May 1983**, $1,995 USD launch (≈ $5,800 in 2024 dollars). **Six operators, 32 algorithms, 16-voice polyphony, 61 velocity- and aftertouch-sensitive keys, 32 RAM patches plus ROM cartridge, the first synth with an LCD, the first to permit user-named patches.** Two custom Yamaha LSI chips: the **YM21290 (EGS)** supplying 12-bit envelope and 14-bit frequency words to the **YM21280 (OPS)**, which time-multiplexed 96 sub-samples (6 ops × 16 voices) per master sample at **49.096 kHz**. The OPS used a logarithmically-stored sine LUT so envelope multiplication became cheap addition. Roughly 45,000 transistors on a 3-µm process. **Within a year, orders exceeded 150,000 units; over 200,000 in three years** — the first synth to break that barrier. Moog had sold only ~12,000 Minimoogs in eleven.

The factory voices were programmed in late 1982, in **less than four days**, by **Dave Bristow and Gary Leuenberger**. **ROM 1A "E.PIANO 1"** — built to emulate a Dyno-My-Piano-modified Fender Rhodes — became the most ubiquitous keyboard timbre of the decade: **Whitney Houston "Greatest Love of All" (1985), Chicago "Hard to Say I'm Sorry" (1982), Berlin "Take My Breath Away" (1986), Tina Turner "What's Love Got to Do With It" (1984), Phil Collins "One More Night" (1985), Luther Vandross, the *Twin Peaks* theme**. **In 1986, the DX7 was used on roughly 40% of US Billboard Hot 100 number-ones and 60% of R&B number-ones** (Wikipedia/Yamaha). **BASS 1 / BRASS 1** drove **a-ha "Take On Me" (1985)**, Kenny Loggins's "Danger Zone," countless Stevie Wonder cuts. **MARIMBA** — Talking Heads, Peter Gabriel.

Producers most associated: **Brian Eno** (who actually programmed it), **Mark Knopfler** (entire timbral palette of *Brothers in Arms*, 1985), **Daniel Lanois** (U2, Peter Gabriel), **Jan Hammer** (the *Miami Vice* theme, 1984), **Quincy Jones, David Foster, Trevor Horn**, **Ryuichi Sakamoto**.

The **backlash was swift**. By 1988–89 the same E.Piano and slap-bass presets had become shorthand for soulless overproduction. By 1993–94 used DX7s dumped on the secondhand market for **$200–400** while analog Junos were repatriated.

The **broader Yamaha FM ecosystem** filled every price point: **TX7 (1985, desktop DX7), TX802 (1987, rack 8× DX7), TX816, DX21 (1985, 4-op), DX27, DX100 (mini 4-op, battery-powered, strap-on), DX11 (1988), V50 (1989), FB-01 (1986), DX7II (1986–87)**. The pivotal sub-DX7 machine for dance music was the **TX81Z (1987)** — built around the **YM2414B (OPZ)** chip, four operators, 8-voice — **the first FM synth to offer non-sine waveforms** for its operators. Its preset bank included **C15 "Lately Bass"** (named after Janet Jackson's 1986 *Control* track "What Have You Done For Me Lately," not Reese), used by Babyface and on **Orbital's "Chime" (1989), Lil' Louis's "French Kiss" (1989), Gat Decor's "Passion,"** and countless white-label house records 1988–95. The **DX100 (1985)** owned the same patch family; per gearnews.com it was *"caned by the Detroit techno guys, especially Derrick May."*

A crucial sibling tangent: the **Reese bass — synonymous with drum-and-bass — was made on a Casio CZ-5000 (phase distortion synthesis, not FM)** for Reese's "Just Want Another Chance" (1988), later sampled into Renegade & Ray Keith's "Terrorist" (1994). Phase distortion is FM's close cousin: instead of perturbing instantaneous frequency, it warps the phase angle into a fixed waveshape, producing similar bright digital timbres with a distinct character. Worth airing this correction directly in the episode.

### Pass 3: IDM Rehabilitation (1990s)

By the time **Aphex Twin's *Selected Ambient Works 85–92*** appeared on R&S in November 1992, secondhand DX7s and DX100s were almost free. **Richard D. James told *Future Music* (April 1993)** that his rig was a Roland SH-101, Korg MS-20, and Yamaha DX7, mixed through an Alesis Quadraverb. He owned a Yamaha DX100 and **sold custom DX patches by mail order under the name "Lannerlog."** Decades later he told *The MagPi*: **"I'm nuts about FM synthesis. The first proper synth I got was a DX100 and I've always thought there's got to be a more interesting way to program the damn things than laboriously going through all the hundreds of parameters."** He subsequently built **Midimutant**, a Raspberry-Pi-driven evolutionary algorithm that hill-climbs FM patches on a TX7 by Mel-frequency cepstral-coefficient distance from a target sample.

The **technical distinction between "smooth FM" and "harsh FM"** is the entire game. Polite DX7 timbres come from: low modulation index (I ≤ 3), integer C:M ratios (1:1, 1:2, 2:1) yielding harmonic spectra, low or zero feedback, slow envelopes — Bessel sidebands stay narrow, fall in the harmonic series, ear hears a "musical" pitched timbre. Harsh/inharmonic FM exploits: **high feedback (5–7), non-integer ratios (1:√2 ≈ 1.414, 1:φ ≈ 1.618), large modulation-index sweeps via fast envelopes, operator detuning** to break phase symmetry. The result is metallic clangs, bell inharmonicity, percussive transients, noisy resonances. *This* attracted Aphex Twin, **Autechre, µ-Ziq, Plaid, Squarepusher, Luke Vibert**.

Sean Booth has confirmed FM's centrality across multiple interviews. The **Caesura Magazine** essay on *Elseq 1-5* frames it explicitly: *"Their interest in FM synthesis continues Brian Eno's position that FM synthesis is important because it is the means by which he learns the most about sound."* Squarepusher told *Sound on Sound* (May 2011): *"My current synths are all stuff that I've built myself in software, augmented with the FS1R and the TX81Z, which is a rackmounted version of a lower-spec DX7."* For *Go Plastic* (2001) he was even more specific: *"I didn't use a computer on Go Plastic. It was made with a Yamaha QY700, TX81Z and FS1R, an Eventide DSP4000 and Orville, an Akai S6000 and a Mackie 16 channel desk."*

The **software FM** lineage closes the loop into Live: Native Instruments released **FM7 in 2002**, modeled on the DX7; **FM8 followed October 2006**, expanding to 8 operators with a free FM matrix instead of fixed algorithms. **Robert Henke** had been writing FM instruments in **Max/MSP since 1997**, and on January 20, 2005, Ableton released **Operator** as a $149 standalone for Live 4.1. **Dexed**, an open-source faithful DX7 emulator that loads original .syx banks bit-accurately, appeared in 2014.

**FM in hip hop**: the **Korg Triton (1999)** workstation's "Phase 9" lead and bell pads, plus the SR-JV80 expansions on the **Roland XV-3080/5080**, codified ROMpler **samples** of FM patches into late-90s/early-2000s R&B beats — **J Dilla, Timbaland, The Neptunes**. This is largely sample playback rather than real-time operator math, but the timbral DNA is direct DX7/TX802 lineage.

The arc: **Chowning's PDP-10 vibrato accident → 1973 JAES paper rejected, then accepted → Yamaha license 1973–75 → GS1 (1981) → DX7 (1983) defines pop → 200,000 used DX7s on the market by 1993 → Aphex Twin, Autechre, Squarepusher mine the same hardware for harsh inharmonic timbres → patent expires 1995 → NI FM7 (2002), Operator (2005), Dexed (2014).** Same equation, **y(t) = A·sin(ω_c·t + I·sin(ω_m·t))**, vastly different cultural readings — **the algorithm is invariant under genre transformation; only the parameter envelope changes.**

---

## SECTION 3 — Artist Deep Dives

### Aphex Twin (Richard D. James)

The earliest documented purchase is the **Yamaha DX100** — the 49-key, 4-op, 8-voice mini that James saved up for as a teenager. He confirmed this directly to Korg's Tatsuya Takahashi in 2017: *"The first thoughts I had about tuning happened with my early noodlings on a Yamaha DX100, one of the first synths I saved up for. I remember looking at the master tuning of 440 Hz and thinking I would change it."* The April 1993 *Future Music* interview lists his rig as **DX7, SH-101, MS-20, TB-303** through an Alesis Quadraverb. The 2014 *SYRO* gear list explicitly includes a (modified) DX100. He has subsequently evangelised for the **Yamaha Reface DX**: *"one of my fave keyboards ever."*

**Polynomial-C** (Polygon Window, *Surfing on Sine Waves*, Warp 1993). The title is almost a thesis: a "polynomial" in FM math is the carrier-modulator equation, and the "C" is the carrier operator label used in DX algorithm diagrams. The arpeggiated lead has the unmistakable plucky, glassy attack of a 4-op DX-family patch — fast envelope, mid-range C:M ratio producing an inharmonic-but-musical bell/marimba hybrid. **Caveat**: Attack Magazine and Vintage Synth Explorer threads sometimes attribute the riff to an SH-101; James has not confirmed publicly. Frame as "FM-style sound design regardless of source synth."

**Xtal** (*SAW 85–92*, R&S 1992). The chord bed was identified by SynaMax in 2022 as sampled from the 1986 library record *Evil at Play* — not a synthesis at all. The **bell-like keyboard motif** and the closing track "Actium," however, both rely on what Reverb Machine identifies as **DX7 ROM "11 E.PIANO 1"**. The "Xtal" name (= crystal) telegraphs the metallic FM timbre James was after.

**Lichen** and **Rhubarb** (*SAW II*, 1994). SAW II's pads are most likely **Oberheim Matrix-1000** (verified by the 2006 auction of James's CS5 with SAW II liner notes etched into the bottom plate). But FM is unmistakably present — Gearspace consensus: *"A lot is FM, using microtuning (DX100), low-fi samples, many things 100% wet through cheap reverb units."* **"Rhubarb"** specifically — slow-attack, hollow-spectrum sine pad — is the cleanest example of James pushing 4-op FM into pure-tone Chowning territory.

**Inharmonic FM percussion.** The *Drukqs* hammer-clang sounds and metallic hits across *Come to Daddy* exploit the central FM trick: non-integer C:M ratios produce partials at inharmonic positions — the spectrum of struck metal. Because this is invisible from the front panel of an analogue synth, **FM is essentially the only practical hardware path to this sound** short of physical modelling. The Korg Monologue collaboration grew out of James's insistence on microtuning for precisely this reason.

### Squarepusher (Tom Jenkinson)

In Tingen's May 2011 *Sound on Sound* feature, Jenkinson's FM rig was unambiguous: **TX81Z + Yamaha FS1R**. The FS1R (1998) was Yamaha's swansong of dedicated FM hardware: 16 operators (8 standard + 8 with noise sources for formant modeling) and microtuning — the direct descendant of Chowning's *Phoné*-era voice-modeling work.

**Beep Street** (*Hard Normal Daddy*, Warp 1997). The iconic minor-key plucky lead is broadly identified within the Squarepusher community as a 4-op FM patch consistent with the TX81Z. The track's sampled drum break is from James Brown's "Soul Pride" (WhoSampled). The pattern — live-feel funk-break drums under FM-synthesised bass and lead — is the IDM template. **Caveat**: Jenkinson has not in any located interview specifically named the Beep Street lead synth; identification is by inference from his confirmed inventory.

**My Red Hot Car** (*Go Plastic*, Warp 2001). Jenkinson confirmed the vocoder treatment was performed on the **Eventide Orville**: *"The vocoder sound on my vocals was done with the Orville, in which I programmed a 24-band patch."* The bass — both wet (FM) and dry (live electric bass) — is doubled. Jenkinson on the wet/dry approach: *"I'd often play something quite harmonious on the bass and create electronic parts that would combat and almost try to contradict this. In my mind I was setting up a dialogue in which each instrument would question the other to the point of being a danger."*

**Port Rhombus** (*Port Rhombus EP*, Warp 1996). Brittle, glass-edged lead and warbling chord stabs use plucky, fast-decay FM patches characteristic of the TX81Z. *"To this day, nobody believes that the tracks on Big Loada were a single pass of me sequencing my Akai S950 from my DR660"* — meaning the FM lead and the breakbeat sample were committed live, not multitracked.

**Aesthetic.** Jenkinson's FM is the opposite of Eno's preset-driven plushness: high feedback, high modulator levels, plucky envelopes, aggressive distortion through Eventide processing.

### Autechre (Sean Booth & Rob Brown)

When asked directly in the 2013 WATMM AMA whether they preferred FM, Booth confirmed it has long been their favourite mode of synthesis. Their inventory across the 2005–2009 live era is unambiguous: **Elektron Machinedrum and Monomachine** (the Monomachine SFX-60 includes an explicit 4-op FM machine — the "FM+" engine), **Akai MPC1000**, **Nord Modular G2**. Autechre confirmed this by uploading the actual sysex files for that tour gear in November 2018 to bleepstores.com (covered FactMag). Earlier, *Tri Repetae*-era interviews note **Roland MS-20, MS-10, Juno, MC-202, Roland R-8**, and the **Ensoniq EPS-16+** with Waveboy disks (granular, formant, bitcrushing).

**Bike** is on **Incunabula (1993), not Tri Repetae** — flag this in script. The track's signature is its tuned-percussion top end — a pinging, mid-register ostinato with the classic FM signature: sharp attack with rapid spectral decay, partials rolling off non-linearly the way struck metal does. Booth has said in the WATMM AMA that they used *"loads of FM-Synths"* alongside MS-20, Juno, and Roland drumboxes.

**Cavity Job** (Hardcore Records, 1991, their debut). The bassline is squarely analogue (MS-10/Juno) but the metallic stabs and ringing clave-like accents already prefigure their FM appetite.

**Eutow** (*Tri Repetae*, 1995). Near-canonical example of "tuned percussion as melody": pitched bell-strikes with FM signature — bright initial transient with upper partials decaying faster than the fundamental.

**Max/MSP and built FM modules.** From *Confield* (2001) onward they migrated bespoke synthesis into Max/MSP. Booth (WATMM AMA 2013): *"The line between sequencing and synthesis is pretty much gone now. textures are sequences, sequences are like harmonies. it's all the same thing when you get down to it."* Their custom FM modules are not pitched-melody devices — they're rhythmic-timbre devices: the FM operator network is being driven by the same algorithmic data that drives the rhythm. This is qualitatively different from Eno's slow-pad use and from Jenkinson's bass/lead use.

### Brian Eno (contrast/context)

**Pre-DX7 chronology — correct the assumption**: *Ambient 2: The Plateaux of Mirror* (with Harold Budd, 1980) **predates** the DX7 (1983), so its "synthesizer accents" cannot be DX7. Period gear from Eno's 1980 setup that fits: Prophet 5 (which he later said he didn't actually like), EMS gear, and the Yamaha CS-80. The follow-up **The Pearl (1984) explicitly used the DX7** alongside CS-80, Casio CT-200, Pro One, AMS digital delay, Eventide Harmonizer, and EMT 250 plate.

**An Ending (Ascent)** — *Apollo: Atmospheres and Soundtracks* (EG, 1983). Daniel Lanois told Gearspace that *"the main synth was a Yamaha CS-80,"* making the track's foundation likely a CS-80 pad with DX7 layering — not pure DX7. The DX7 patch most associated is **"Glide,"** which Eno published — along with Kalimba 2, Tamboura, and Violin 3 — in *Keyboard* magazine in 1987. CDM republished the patch sheets in 2017; Gearspace users have loaded them into Dexed and confirmed phase-cancellation against the original.

**Eno's DX7 philosophy.** Contrary to the urban myth that he relied on factory presets, Eno programmed extensively. Future Music, December 1995: *"I use the DX7 because I understand it. I was quite ill for a while, and I filled the time by learning it. Sticking with this is choosing rapport over options. I know that there are theoretically better synths, but I don't know how to use them. I know how to use this. I have a relationship with it."* This is the inverse of the cliché — and the inverse of Aphex's adversarial, mutate-via-genetic-algorithm relationship with the same chip family. He later credited Native Instruments FM7: *"It's the DX7 I always wanted. With the FM7 you can suddenly connect things in different ways. You can also tune the keyboard in any way you want, so you can make music in just intonation, or Arabic intonation."*

**Why Eno's DX7 sounds nothing like Aphex's.** Same instrument, opposite aesthetic. Eno's "Glide" patch: slow attacks (envelopes ramping over hundreds of ms), gentle modulator levels (partials restrained, near-harmonic), buried in Lexicon PCM-70 / EMT 250 plate reverb. James does the inverse: short envelopes, high feedback, irrational ratios, cheap Quadraverb at extreme settings. **Same six operators — different decisions about envelope time and modulation index.**

---

## SECTION 4 — Song Curation & Demo Mapping

### 1. Aphex Twin — Polynomial-C (1993, Warp)

**Sections.** 0:00–0:08 cold open, plucky 16th arpeggio enters dry; 0:08–0:24 bass + 808 kick enter; 0:24–0:58 Simon Harris "105 BPM Dopejam" break and hi-hats kick in; 0:58 second muted-bell answering line joins; ~1:30 sub-bass swells; 2:30–3:30 filter sweeps brighten the lead.

**Stem.** Lead/arpeggio (Spleeter "other" gives a clean 8-second solo before drums hit).

**Technique.** Plucky envelope: near-instant attack, ~150–250 ms decay, no sustain. Forum debate over SH-101 vs DX100 origin; sonically the *behavior* is FM-textbook.

**Operator hook.** Demo for **plucky FM with fast modulator-envelope decay**. 1:1 C:M ratio, modulator level ~80, decay 200 ms.

**Demo script (40 sec).** *"Listen at 0:04, before the drums hit: that arpeggio has no filter sweep. Its movement comes entirely from the envelope on a modulator. Each note slams in and decays in about a fifth of a second. That's the canonical FM pluck shape: short modulator envelope, 1:1 ratio, no sustain. When the breakbeat enters at 0:24, the bell-edge of the arp cuts through — that high-end isn't EQ, it's inharmonic upper partials."*

### 2. Aphex Twin — Xtal (1992, R&S)

**Sections.** 0:00–0:14 808 kick alone, drowned in Quadraverb; 0:14–0:30 sampled "Evil at Play" Rhodes/vocal pad enters; 0:30 plucky crystalline bell lead enters; ~1:30 Apache breakbeat (repitched −5 semitones); ~2:30 layering peaks; 4:00–end peel-away outro.

**Stem.** Lead + pad. RipX harmonic separation will give clean 2:30 lead-vs-pad layers.

**Technique.** FM-bell character: sharp attack, audibly inharmonic decay (metallic ringing hangs longer than a sine envelope would suggest). Lead is plausibly DX-family; pad is the *Evil at Play* sample.

**Operator hook.** Inharmonic ratio (1:√2 or 1:3.5) with slow modulator decay produces long, detuned overtones. Pair with low feedback for slight breathiness.

**Demo script.** *"When that bell-like lead enters around 0:34, listen for how each note's tail isn't a clean sine — there's a metallic shimmer that decays slower than the fundamental. That's the signature of inharmonic FM partials: the modulator's frequency isn't a whole-number multiple of the carrier. The pad underneath, by the way, is not synthesized — it's a 1986 library sample of Donald Greig and Mary Carewe through a Quadraverb, traced by Reverb Machine in 2022. So Xtal teaches us two things: real FM-bell timbres in the lead, and how a sampled Rhodes-and-voice can stand in for an FM pad."*

### 3. Squarepusher — Beep Street (1997, Warp)

**Sections.** 0:00–0:20 atmospheric synth-wash intro; ~0:20 iconic FM lead head-melody enters, vocal-like, with vibrato; ~0:45 live fretless bass guitar layers under, doubled with synth bass; ~1:10–1:30 programmed breakbeat enters in full; ~3:00–4:00 lead returns with re-harmonized chordal pad; 5:00–end echoes thin out.

**Stem.** Lead during 0:20–0:45 (clean isolation before bass enters).

**Technique.** TX81Z/FS1R lead with breath-controller character: soft attack, sustained body with vibrato, pitch-bend portamento, metallic edge on louder notes (modulator level rising with velocity).

**Operator hook.** **Velocity routed to modulator level.** Soft notes near-pure sine; hard notes brighten with sidebands, mimicking embouchure dynamics. Demo of the 2-operator "FM flute" algorithm.

**Demo script.** *"Between 0:20 and 0:40, before the drums explode, you're hearing one of the most beloved sounds in IDM. Tom Jenkinson confirmed in Sound on Sound that his FM workhorses are a Yamaha TX81Z and FS1R. Listen to how the louder notes have more bite: that's velocity routed to the modulator's level. Soft notes are nearly pure sine; hard notes break open into a metallic, almost trumpet-like edge. That's not a filter — there is no filter on a DX. It's pure modulation depth responding to your finger."*

### 4. Autechre — Bike (1993, Warp)

**Correction**: Bike is on **Incunabula (1993)**, not *Tri Repetae* (1995).

**Sections.** 0:00–0:30 slow rolling pad and soft panning rhythmic click (bicycle-spoke-like, hence the title); 0:30–1:30 detuned synth chord pulse, metallic high-frequency clicks enter; 1:30–3:30 full beat — programmed Roland R-8 layered with bell-toned percussion; 4:00–6:00 long evolution; 6:00–end fades on percussion alone.

**Stem.** Drums/percussion (Spleeter "drums" pulls the metallic FM percussive layer cleanly during sparser opening).

**Technique.** Inharmonic-partial signature: hits don't have a single pitch but a cluster of metallic frequencies decaying independently — exactly what FM operators do at non-integer ratios with short envelopes. Perfect for cowbell-like, anvil-like, "broken machine" percussion.

**Operator hook.** **FM as percussion synthesis tool.** Two operators at wildly inharmonic ratio (1:11.7); modulator envelope ~50 ms decay; carrier envelope ~300 ms decay = pinged metallic transient that sounds nothing like a drum sample but functions as one. Direct lineage from Yamaha's RX-series drum machines into Autechre's aesthetic.

**Demo script.** *"Bike, from Autechre's 1993 debut Incunabula, is where the Warp aesthetic begins to flirt seriously with FM. Listen for the metallic, almost bicycle-bell-on-pavement clicks in the first 30 seconds. Each one is a tiny inharmonic explosion — short modulator envelope ringing a carrier at a ratio that doesn't correspond to any musical interval. The result: percussion with pitch character but not pitch identity. Booth and Brown have said they love FM synths because they don't behave like analog filters; they don't get warmer when you hit them harder, they get more inharmonic."*

### 5. Brian Eno — An Ending (Ascent) (1983, EG)

**Sections.** 0:00–0:30 single sustained DX7 pad with ~3-sec attack; 0:30–1:00 second voice/chord adds, harmonic motion begins, enormous reverb tail; 1:00–2:30 full chord cycle, ~5-sec releases; 2:30–3:30 lead voice traces melody on top; 3:30–end long fade with shimmer reverb.

**Stem.** Pad / full mix (track is essentially monolithic).

**Technique.** **Confirmed**: DX7 + Mesa Boogie tube amp coloration + Lexicon PCM-70 plate. Very slow attack (multi-second), pure-ish sine fundamentals with subtle inharmonic shimmer in upper partials, long release blooming into reverb. Lanois quote: *"On top of that, we put all the DX7 sounds through a Mesa Boogie."* Patch: **"Glide,"** verified by Gearspace recreators via phase-cancellation.

**Operator hook.** **The anti-pluck demo** — proof that FM is not just bells and basses. Long modulator-envelope attack, low-to-moderate I, very slow carrier amplitude envelopes.

**Demo script.** *"An Ending is what happens when somebody actually programs a DX7 instead of using presets. Brian Eno bought seven of them, hand-built his patches, and published four in Keyboard Magazine in 1987 — the patch behind this track is Glide. Listen at 0:00: there is no attack transient at all. Each note swells in over two or three seconds. That's the modulator envelope rising slowly, so the harmonics fade in behind the fundamental. Then Lanois ran it through a Mesa Boogie tube amp into a Lexicon PCM-70. Same six operators, opposite aesthetic to Aphex. The medium is identical. The decisions are everything."*

### Recommended additions

**a-ha — Take On Me (1985).** 0:00–0:18 LinnDrum + DX7 bass groove enters with no chords. The bass is **DX7 ROM 1A 15 "BASS 1"**. Cleanest demo of the DX7 plucked-string algorithm: single carrier with one modulator at 1:1, sharp modulator envelope. Eighty percent of '80s pop bass came from this exact patch.

**Whitney Houston — Greatest Love of All (1985).** 0:00–0:25 solo E.PIANO 1 plays the introduction with no other instrumentation — gold-standard isolated demo of the most famous synth preset of all time. Built from a 4-operator Rhodes simulation: a carrier sine (the "tine") plus a modulator at a high ratio producing the bell-attack chirp not present on a real Rhodes. **Velocity sensitivity is huge** — soft notes mellow, hard notes ring.

**Tim Hecker — Black Refraction (Virgins, 2013).** [corrected: this track is on *Virgins* (2013), not *Ravedeath, 1972* (2011) — verified Discogs/Wikipedia/Fact.] Modern FM ambient practice: stack multiple Operator instances at irrational ratios (1:√2, 1:√3), very long envelopes, modulator level automated by slow LFOs to make harmonic content drift. The 2010s descendant of *Apollo*, darker.

**Drop the Reese & Santonio reference** — the Reese bass is Casio CZ-5000 phase distortion, not FM. Address this misconception directly in script as a teaching moment about the FM/PD cousin technologies.

---

## SECTION 5 — Technical Synthesis Depth

### 5.1 The basic FM equation and its spectrum

We start from Chowning 1973:

$$y(t) = A\sin\!\big(2\pi f_c t + I\sin(2\pi f_m t)\big)$$

Pedantically, this is *phase* modulation — but since instantaneous frequency $f_i(t) = (1/2\pi)\,d\phi/dt = f_c + I f_m \cos(2\pi f_m t)$ is just the time-derivative of phase, PM and FM by a sinusoid are equivalent up to a 90° offset. The DX7 and Operator both implement phase modulation internally because it avoids an integrator and keeps DC stability.

To get the spectrum, expand using the **Jacobi–Anger identity**:

$$e^{i\beta\sin\theta} = \sum_{n=-\infty}^{\infty} J_n(\beta)\, e^{i n \theta}$$

Taking imaginary parts:

$$\sin(\alpha + \beta\sin\theta) = \sum_{n=-\infty}^{\infty} J_n(\beta)\sin(\alpha + n\theta)$$

Setting $\alpha = 2\pi f_c t$, $\theta = 2\pi f_m t$, $\beta = I$:

$$y(t) = A \sum_{n=-\infty}^{\infty} J_n(I)\, \sin\!\big(2\pi(f_c + n f_m)\,t\big)$$

So an FM signal is a discrete line spectrum at $f_c \pm n f_m$, weighted by **Bessel functions of the first kind $J_n(I)$**. The Bessel function appears because the integral $\int e^{i\beta\sin\theta}e^{-in\theta}d\theta$ *is* the integral definition of $J_n(\beta)$ — same mathematical creature as the radial Helmholtz problem.

**Bessel facts.** Reflection: $J_{-n}(\beta) = (-1)^n J_n(\beta)$ — lower sidebands have the same magnitude as upper but alternate sign. Small-argument asymptotic: $J_n(\beta) \approx (\beta/2)^n / n!$, so $J_n(I) \to 0$ rapidly once $n > I$. **Carson's rule (1922)**: significant sidebands extend to roughly $I+1$ each side, total bandwidth $\approx 2(I+1) f_m$, capturing ≥98% of signal power for $1 \le I \le 5$. $J_0$'s first zero at $\beta \approx 2.4048$ — at $I = 2.4048$ the carrier line vanishes entirely (signature DX bell trick).

**Concrete example, $I=2$, $f_c=f_m=440$ Hz.** Carson's rule predicts BW ≈ 2640 Hz. Tabulated $J_n(2)$ values: $J_0=0.224$, $J_1=0.577$, $J_2=0.353$, $J_3=0.129$, $J_4=0.034$, $J_5=0.007$. Upper sidebands at 440(1+n) Hz. Lower sidebands fold to negatives via $\sin(-x)=-\sin x$ and **add algebraically** to positive-frequency components: $f_c - f_m = 0$ Hz, $f_c - 2f_m = -440$ folds onto +440 with sign $(-1)^2 J_2 = +J_2$, $-880$ folds onto +880 with sign $-J_3$, and so on. This sign bookkeeping is exactly why $f_c/f_m = 1$ produces a sawtooth-like spectrum with sign-alternating partials — same mechanism as analog saw's $1/n$ partials, but envelope $J_n(I)$ instead.

### 5.2 Modulation index and brightness

$I \equiv \beta \equiv \Delta f / f_m$ where $\Delta f$ is peak instantaneous frequency deviation. Increasing $I$ pushes spectral energy outward. **Crucial pedagogical point: $I$ controls timbral brightness, not loudness.** Total signal power $\sum_n |J_n(I)|^2 = 1$ — changing $I$ redistributes spectral energy without changing RMS amplitude. This is why FM envelopes shape *timbre* directly — opposite to subtractive synthesis where amplitude and brightness are decoupled.

**Operator translation.** The modulator's **Level** parameter is functionally proportional to $I$. Operator's Level is logarithmic, calibrated so maximum modulator level corresponds to $I$ on the order of 10–15 depending on coarse/fine ratios. Enveloping modulator Level → enveloping $I(t)$ → time-varying brightness — the entire mechanism behind the FM "wahh," "vocal-formant," and "pluck" gestures.

### 5.3 Integer vs non-integer ratios

Let $r = f_m/f_c$. Spectrum lines at $f_c(1 + nr)$. If $r = p/q$ in lowest terms, every line is integer multiple of $f_0 = f_c/q$ — spectrum is *harmonic* with fundamental $f_0$. If $r$ irrational, lines are *inharmonic*: no common subharmonic exists, ear cannot fuse them into one pitched note — instead bell, gong, metal, or noise textures.

Examples ($f_c=1$): **1:1** — partials 1,2,3,…, sawtooth-like (brass/reed). **1:2** — odd harmonics only (clarinet/square). **1:3** — partials 1,2,4,5,7,8,…, missing every third, hollow. **3:1** — fundamental at $f_0=1$, dense brassy spectrum. **7:11** — rational but high-$q$, fundamental $f_0=f_c/7$ below the carrier, dense chime-like spectrum perceived as harmonic but very thick. **1:√2** — irrational, classic bell/gong. **1:φ** — Chowning's *Stria* used the golden mean for both pitch structure and C:M ratios.

The auditory system performs an approximate harmonic template match — only when sidebands fall on (or near) integer multiples of *some* $f_0$ does pitch fusion occur. For irrational $r$ the percept becomes *object-like* (bell, plate, drum) rather than *note-like*.

### 5.4 Feedback in FM

Operator feedback implements (in continuous-time idealization)

$$y(t) = \sin(\omega t + k\, y(t))$$

— Kepler's equation in disguise; no closed form. Solved by one-sample delay: $y[n] = \sin(\omega n T + k\, y[n-1])$, often with two-sample averaging $y[n] = \sin(\omega n T + k(y[n-1]+y[n-2])/2)$ as in the DX7 to suppress aliasing zipper.

Iteratively expanding gives a series whose $n$th term involves $J_n$-like coefficients with self-referential argument $k\cdot y$. As $k$ ramps from 0 upward the waveform morphs sine → asymmetric sine → triangle → smooth saw → "hyper-saw" → broadband noise. Empirical Dexed measurements: at DX7 feedback level 4 the first eight saw partials emerge cleanly with $1/n$ spacing; level 5 yields ~18 partials; level 6 develops a peak near partial 34; level 7 is essentially band-limited noise. The bifurcation to chaos sits near $k \sim \pi$ in the continuous formulation.

Operator feedback is per-operator with similar character. Use cases: slight lean at $k\approx 1$–$2$ thickens basses and reeds; high feedback is the canonical FM source for hi-hats, breath transients, snare attacks, percussive noise — no separate noise generator needed.

### 5.5 FM envelopes vs subtractive envelopes

In subtractive synthesis, two envelopes do orthogonal jobs: amp envelope → loudness; filter envelope → cutoff → brightness. In FM, **the modulator's level envelope IS the brightness envelope** (because level $\propto I \propto$ brightness), and **the carrier's level envelope IS the amplitude envelope**. There is no equivalent of a low-pass filter; spectral shape is entirely synthesized, not subtracted.

An FM electric piano or pluck requires *two distinct envelopes minimum per voice*: modulator with fast attack, rapid decay → bright tine-strike fading in ~50–200 ms; carrier with similar attack, longer release → sustained body. The result is the FM signature pluck — bright initial transient decaying to a near-sinusoidal tail. Realistic acoustic emulation requires modulator envelopes with frequency-dependent decay (high partials decay faster, mimicking radiation damping), which is exactly why the DX7 used per-operator **8-stage rate-level envelopes** (R1-L1 through R4-L4) — six operators × 8 stages = 48 envelope parameters per voice, extraordinarily expressive and notoriously brutal to program. Operator simplifies to ADSR-with-loop, trading expressivity for usability.

### 5.6 4-op vs 6-op tradeoff

Maximum spectral complexity scales with the number of cascaded modulators per carrier. The DX7's 6 operators allow parallel stacks: algorithm 5 is three independent 2-op pairs summed at the output — perfect for layered electric pianos (E.PIANO 1 uses one stack for tine attack, another for body resonance, another for key thump). 4-op architectures cannot do this — at best one or two parallel pairs, or one 3-op stack plus a sine.

For most IDM use cases — percussive plucks, sub-bass with bite, bells, FM hi-hats, glassy keys — 4-op is more than enough and arguably preferable: smaller sound space, faster programming, lower CPU. The tradeoff is *time-evolving spectral complexity*. Workarounds in Operator: envelope **loop modes** to inject quasi-random repeating modulations; routing the LFO to operator levels for slow spectral evolution; using the Filter and Shaper sections for subtractive/waveshaping post-processing — not classical FM but Ableton added them precisely to compensate for the 4-op limit.

---

## SECTION 6 — Episode Script Outline

### Cold Open (90 seconds)

**Audio bed.** Crossfade from total silence into the *first 8 seconds of Aphex Twin "Polynomial-C"* — solo plucky arpeggio, dry, unaccompanied. Hold for 12 seconds. Fade under as narration enters.

**Opening line of narration.** *"In 1967, in the basement of Stanford's Artificial Intelligence Lab, John Chowning was trying to make a sound wobble. He turned the wobble up. He turned it up further. And somewhere around 20 cycles per second, the wobble disappeared — and a whole new sound appeared in its place. He didn't know it yet, but he had just stumbled into the equation that would generate, over the next two decades, more pop hits than any analog synthesizer in history. And then — when everyone else got bored — would become the secret weapon of an entire generation of producers who wanted to sound like a malfunctioning machine. This is Episode One. This is Operator."*

Cut to title music — could be a custom Operator-built bell motif at 1:√2 ratio. 4 seconds. Then into Section 2.

### History (8–9 minutes)

Beat 1 (90 sec). **Chowning's vibrato accident.** SAIL, PDP-10, MUSIC 10. The two sine oscillators. The "discovery of the ear" quote. The mathematics on a chalkboard: y(t) = A sin(ωt + I sin(ωt)). One sentence on Bessel functions: *"the same equation that describes how vibrating drumheads radiate energy — turns out, it also describes how to make a synthesizer."*

Beat 2 (90 sec). **The compositions.** Sabelithe (1971), Turenas (1972) — the first time anyone heard sounds fly through a quad room. Stria (1977) — built entirely on the golden ratio, **drop a 15-second Stria excerpt here**. Phoné (1981) — modeling the human voice, foreshadowing CHANT.

Beat 3 (60 sec). **The American failure.** Hammond, Wurlitzer, Lowrey — all said no, couldn't follow the math. *"Imagine being the engineer at Hammond who passed on FM synthesis. That's a career-defining 'no.'"*

Beat 4 (90 sec). **Yamaha takes the call.** Ishimura's 1973 visit. *"Ten minutes and he understood exactly what I was doing."* Patent filed 1974, granted 1977. Stanford's second-most-lucrative patent ever — $22.9 million, beaten only by recombinant DNA.

Beat 5 (120 sec). **The DX7 lands.** May 1983, $1,995. Six operators. 200,000 units in three years. **Drop 12 seconds of solo E.PIANO 1 from "Greatest Love of All"** as bed. Read the list — Whitney, Chicago, Berlin, Tina Turner, Phil Collins, the *Twin Peaks* theme. *"By 1986, the DX7 was on 40% of the Billboard Hot 100 number-ones."* Bristow and Leuenberger programmed those presets in less than four days.

Beat 6 (90 sec). **The backlash.** By 1989 the same E.Piano had become shorthand for soulless overproduction. By 1993, used DX7s sold for $200. *"Which is exactly the price point at which weird teenagers in Cornwall start buying them."*

Beat 7 (90 sec). **TX81Z and the underground.** **Drop 8 seconds of Lil' Louis "French Kiss"** under the words "Lately Bass." Detroit techno on DX100. The Reese bass detour: *"and just so we're clear — the famous Reese bass, the one in every drum-and-bass track since 1994 — that's actually a Casio, phase distortion, not FM. Technical cousins. Don't get it wrong on the internet."*

### Synthesis Deep Dive (8–9 minutes)

Beat 1 (90 sec). **The equation in one breath.** "Take a sine wave. Use a second sine wave to modulate the first one's frequency. Crank the second wave into the audio range. The result is — mathematically — a comb of new frequencies above and below the carrier, spaced by the modulator frequency, with amplitudes set by Bessel functions of the modulation index." Pause. *"If you didn't follow that, the next eight minutes are for you."*

Beat 2 (120 sec). **Bessel functions, friendly.** Spend a beat acknowledging the listener is a physicist. *"Yes, those Bessel functions. Same ones from your electromagnetism class. The same J_n that shows up in cylindrical waveguides shows up here because — surprise — phase-modulating a sinusoid is mathematically the same problem as a wave bouncing inside a drum."* **Drop a sweeping FM patch in Operator** where you ramp I from 0 to 5; listen as new partials emerge in real time.

Beat 3 (120 sec). **Ratios.** Integer vs irrational. **Build a one-bar example live in Operator**: ratio 1:1 (sawtoothy), 1:2 (clarinet-y), 1:3 (hollow), 1:√2 (bell), 1:φ (Stria-like cloud). **Drop 8 seconds of Stria after the φ example.**

Beat 4 (120 sec). **Modulation index = brightness.** Loudest single point: in subtractive synthesis the filter envelope shapes brightness; in FM, the modulator's level envelope IS the brightness envelope. Same thing. Different topology. *"This is why an FM pluck has that liquid 'dwah' attack — it's not a filter sweep, it's a modulator envelope. They sound similar because they're doing the same job to your ears."*

Beat 5 (90 sec). **Feedback.** Self-modulation as Kepler's equation. Sine → sawtooth → noise. **Demo a single Operator oscillator at feedback 0, 4, 6, 7** — listen to the bifurcation.

Beat 6 (60 sec). **4-op vs 6-op.** Honest tradeoff. Operator can't do E.PIANO 1's three-stack architecture in a single instance. But for IDM — bells, plucks, percussion — 4-op is plenty.

### Ableton Deep Dive (8–9 minutes)

Beat 1 (60 sec). **Origin story.** Henke, 2004, codename Onyx, modeled on his DX27 — *"which is why Operator is 4-op, not 6. One man's daily driver became the synth a million Live users now take for granted."* Released 2005, $149.

Beat 2 (90 sec). **Tour the algorithms.** The 11 in plain English. Algorithm 1 (linear stack), algorithm 7 (the Preve favourite, two parallel pairs), algorithm 11 (no FM at all — additive mode). *"And the algorithm number itself is MIDI-mappable. You can automate the topology. The DX7 cannot do that."*

Beat 3 (120 sec). **The four operators in detail.** Coarse as multiplier, not octave. Fine is positive-only — explain the asymmetry trick. Fixed mode and what it unlocks for inharmonic percussion. The Level parameter as the modulation index. The waveform list — emphasize Sine 4 / Sine 8 / NoiseLoop as the IDM tools.

Beat 4 (90 sec). **Envelopes.** Standard ADSR, plus initial/peak/sustain/end, plus draggable curves. **The five loop modes** as the secret weapon. Beat-sync modulation as a free arpeggiator inside the synth.

Beat 5 (60 sec). **LFO as fifth operator.** Range Hi at 12 kHz with R<Key 100% — turn the LFO into a pitch-tracking audio-rate modulator routed to multiple operators simultaneously. *"This is how you escape the 11-algorithm prison."*

Beat 6 (60 sec). **Filter and Spread.** Cytomic models. Spread as two semi-independent voice instances, not a chorus.

Beat 7 (60 sec). **Quick comparison.** Dexed for SYSEX recall, FM8 for 6-op stacks and modulation matrix, Plogue OPS7 for hardware-accurate DX7 output. Operator wins on integration, CPU, and Live's modulation system.

### Patch Walkthrough (5–6 minutes)

Build a single patch live, narrating every parameter value. **Target: an Aphex-style inharmonic bell-pluck.**

Step 1 (45 sec). **Algorithm 1** (linear stack D→C→B→A). Start with a default Operator. Set all operators to Sine.

Step 2 (45 sec). **Carrier (A)**: Coarse 1, Fine 0, Level −12 dB. Standard ADSR: A=1ms, D=400ms, S=−inf, R=200ms. Listen — pure sine pluck.

Step 3 (60 sec). **First modulator (B)**: Coarse 1, **Fine 414** (this approximates the √2 ratio offset). Level around 80%. Envelope: A=1ms, D=120ms, S=−inf, R=80ms. Listen — bell-like inharmonic ringing emerges.

Step 4 (45 sec). **Second modulator (C) feeding B**: Coarse 7, Level 50%, envelope similar but D=60ms. Listen — high-frequency shimmer adds.

Step 5 (45 sec). **Feedback on C**: 30%. Listen — gritty edge appears in the attack.

Step 6 (45 sec). **Spread**: 12%. **Filter**: LP24 at 8 kHz, OSR circuit, Drive +3 dB. Listen — stereo width and analog warmth.

Step 7 (45 sec). **Velocity routing**: Time<Vel on operator B at +30 (harder = brighter shorter pluck), Level<Vel at +50. Play soft and hard — listen to the dynamic range.

Step 8 (30 sec). **Save the patch as "Polynomial-Bell."** *"That's eight minutes of work to build something that, in 1985, would have taken Brian Eno a week."*

### IDM Application (5–6 minutes)

Beat 1 (90 sec). **Specific technique: rhythmic FM percussion via envelope loop mode.** Open a fresh Operator. Algorithm 1, both A and B sine. Set B's envelope to **Beat at 1/16**, peak decay 30ms. Set A to Trigger envelope, decay 200ms. Set B Coarse to a prime number — **11**. Listen: a self-rhythmic metallic percussion synth driven by a single held note.

Beat 2 (90 sec). **Layer it.** Add a second Operator instance with B Coarse = 13, Beat at 1/8 dotted. Listen to the polyrhythm emerge from a single MIDI note. *"This is why Autechre stopped making melodies and started making textures. Once your synth is the rhythm, the line between sequencing and synthesis disappears — Sean Booth's exact words from the 2013 AMA."*

Beat 3 (60 sec). **Connect to the math.** *"Coarse 11 against Coarse 1 is a rational ratio with a high q — the perceived fundamental falls below the audible range, so you hear inharmonic clusters instead of a pitched note. This is exactly the territory of struck metal — gongs, plates, anvils."*

Beat 4 (60 sec). **The wet/dry idea, Squarepusher-style.** Suggest the listener layer this Operator percussion in a Drum Rack alongside live-recorded foley — keys, coins, kitchen utensils. Frequency-isolate the foley to the upper register where Operator is weakest, and the FM percussion to the mid where it shines.

Beat 5 (90 sec). **The listener exercise.** *"Here's your homework for the walk home. Open Operator. Set algorithm 1. Set everything to sine. Set operator B to Coarse 1, Fine 414 — that's the irrational ratio. Now: program a melody that sounds beautiful only because of inharmonic spectra. No filter sweeps. No reverb. Just operator levels and envelopes. Forty minutes. If you can't, you've understood the depth of what Eno did with Glide. If you can, you've understood why Aphex Twin sold patches by mail order in 1991. Either way, you've spent forty minutes inside the same equation Chowning wrote in 1967. Y of t equals A sine of omega-c-t plus I sine of omega-m-t. Same equation. Different decisions. Everything."*

Outro music: a soft Eno-style "Glide"-derived pad, fade to silence. End at ~40:00.

---

## Conclusion

The thesis crystallizing across all six sections: **FM synthesis is mathematically invariant under genre transformation; only the parameter envelope changes**. Chowning, Bristow, Eno, James, Booth, and Henke are all interrogating the same handful of equations — Bessel sidebands, modulation index, integer-vs-irrational ratios, feedback as Kepler's equation. What separates "Greatest Love of All" from "Polynomial-C" is not the chip, the algorithm, or even the ratio — it is the **shape of three or four envelopes** and a decision about whether modulator level should rise slowly or snap shut. That insight, delivered to a physicist who already builds patches in Live 12, justifies the 40-minute walk: the listener leaves with a unified picture of why FM hardware that was scrap in 1993 became foundational to IDM, why Operator's 4-op limit is rarely a real limit, and why the next bell patch they program is one envelope away from the next pluck.