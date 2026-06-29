# Episode 3 — Wavetable: Morphing Through Spectra

| | |
|---|---|
| **Device** | Ableton **Wavetable** (two wavetable oscillators + Sub; destination-first mod matrix; Cytomic filters) |
| **Status** | published |
| **Runtime** | ~39 min (target 40) |
| **Device demos** | 20 (`wt-*`, rendered via the AbletonOSC / M4L headless pipeline) |
| **Song clips** | 14 (5 foreground cues · 5 transitions · 4 beds) from 4 acquired tracks |
| **Focus sentence** | *Wavetable synthesis is the art of modulating one parameter — Position — and everything from the 1982 PPG choir to the 2021 dubstep growl is the same gesture at a different rate: you don't filter a sound to make it move, you walk between sounds.* |
| **Driving question** | Why is the most important knob the one that changes neither pitch, nor volume, nor the filter — only which waveform you're playing while you play it? |
| **Payoff refrain** | "Pitch and timbre, separate dials. Walk the timbre." (seeded in the cold open, echoed at each act boundary, landed in 06e) |

**Primary artists:** Plaid, Aphex Twin, Autechre. **Records:** Plaid — *Polymer*; Depeche Mode — *A Broken Frame*; Skrillex — *Scary Monsters and Nice Sprites*. **Adjacent genres:** synth-pop, dubstep, melodic bass/EDM.

---

## Table of Contents

1. [Cold Open](#1-cold-open--01-cold-open--90s)
2. [History & Theory](#2-history--theory--02a02e--89-min)
3. [Synthesis Deep-Dive](#3-synthesis-deep-dive--03a03e--89-min)
4. [Device Deep-Dive (Ableton Wavetable)](#4-device-deep-dive-ableton-wavetable--04a04f--89-min)
5. [Patch Walkthrough — PPG choir → Subtronics growl](#5-patch-walkthrough--ppg-choir--subtronics-growl--05a05g--56-min)
6. [IDM Application](#6-idm-application--06a06e--56-min)
7. [Demos at a Glance](#7-demos-at-a-glance)
8. [Reproducibility & Known Limitations](#8-reproducibility--known-limitations)

---

## 1. Cold Open  ·  `01-cold-open`  ·  ~90s

**Synopsis.** A confession, not a welcome: in 1978 Wolfgang Palm tried to build a digital low-pass filter in Hamburg and failed — what came out was harsh, metallic, alien. He kept it. That harsh part — scanning through a row of single-cycle waveforms — became the defining timbre of three separate decades. The cold open plants the four-stop map (history / physics / the device / make-IDM-with-it) and the payoff refrain.

- **Songs:** `see-you-cold-open` — ~10 s of Depeche Mode "See You" intro, the bare PPG choir pad alone, held then ducked under narration.
- **Key facts/claims.** The choir you're hearing is a PPG. Callback to Ep1: last episode the magic knob was modulation index (FM *generates* a spectrum); this episode it's Position, which changes which sound you're playing while you play it. Plants pitch/timbre orthogonality (paid off in 03a).

## 2. History & Theory  ·  `02a`–`02e`  ·  8–9 min

**Synopsis.** Ordered by "what do I need next?": the accident that made the sound → the machine that made it 80s pop → who carried the grit when PPG folded → how plugins inverted the aesthetic into a default → how Ableton finally arrived. The thesis: a 1978 mistake became the default architecture of modern electronic music; each generation re-decided whether the aliasing was a flaw to remove or the signature to keep.

- **Songs:** `see-you-choir` (the canonical glassy PPG choir/bell on "See You"); `everybody-wants-bass` (Tears for Fears — the PPG as a percussive high-end *click* under the DX7 bass, the subtle/transient-design example); `scary-monsters-growl` (Skrillex — the LFO-on-position "talking bass" growl drop).
- **Demos:** none (history beats are song-anchored).
- **Key facts/claims.** Palm's Wavecomputer 360 (1978, ~40 built, no analog filter, "buzzy and thin"); the Palm quote *"these wavetable sweeps sounded very harsh; not at all like an analogue filter sweep."* PPG Wave 2 (1981) hybrid: digital oscillators → analog VCF; receipts — Tangerine Dream/Froese, Depeche Mode's Martin Gore choir+bell, Numan's *Berserker*, the hidden PPG click on "Everybody Wants to Rule the World." **Inline myth-busters:** Bowie's PPG = *Tonight* (credit only); "Shout" = Fairlight not PPG; Jarre PPG link likely a misattribution. PPG folds end of 1987 → Palm's chip into the Waldorf Microwave (1989); SoS quote *"aliasing and other digital nasties are part and parcel of the Microwave's distinctive sound"*; Charlie Clouser's Microwave on early NIN. Massive (2007, dubstep wobble = LFO on position); Serum (2014, **attribute the editor rationale to Steve Duda, not deadmau5**); Vital (2020). **Timeline trap, stated up front: Skrillex's 2010–11 growls are Massive + FM8, NOT Serum** (Serum shipped 2014). Ableton Wavetable: Live 10, Feb 2018, Suite-only, PPG-inspired, Henke's "get lost in the sound, not in tons of parameters," 194 tables / 12 categories, user import added in 10.1 (2019). **>> SIGNPOST → Act 3.**

## 3. Synthesis Deep-Dive  ·  `03a`–`03e`  ·  8–9 min

**Synopsis.** The physics: a wavetable as a sequence of additive snapshots, pitch/timbre orthogonality, interpolation, the central aliasing fight, and how it differs from last episode's FM. Ordered what-it-is → additive → interpolation → aliasing → vs FM. This act pays off the cold open's orthogonality plant and bridges back to Ep1.

- **Demos:**
  - `wt-position-by-hand` (03a) — **THE key demo:** hold one note, drag Position 0→100, the tone walks sine→tri→saw→square at constant pitch. Isolates pitch/timbre orthogonality.
  - `wt-ab-two-positions` (03b) — two positions of one table = two distinct timbres; proof a table is a collection of spectra.
  - `wt-zipper-vs-smooth` (03c) — frame interpolation turns a stepped scan into a glide. *(⚠ Hi-Q not settable headless — hand-render or cut.)*
  - `wt-hiq-on-vs-off` (03d) — Hi-Q off (PPG) vs on (Serum); the 40-year argument in one switch. *(⚠ Hi-Q not settable headless — hand-render.)*
  - `wt-fm-inside-wavetable` (03e) — sweep FM Amount on a held note; harmonics grown *inside* the wavetable oscillator (the Ep1 bridge).
- **Key facts/claims.** A wavetable = an ordered collection of single-cycle frames sharing one base period, so scanning Position changes only harmonic content (pitch on a separate dial). Each frame's DFT is a fixed harmonic spectrum → a wavetable is a *sequence of additive snapshots*; scanning = walking a path through Fourier space. Linear cross-fade `x_p = (1-α)x_i + α·x_{i+1}`; Ableton curates "no inharmonic content between waves"; the PPG zippered *gloriously* because 8-bit hardware had no real-time interpolation; Serum's ~50 ms fade. Aliasing: high harmonics fold past Nyquist into inharmonic alias tones; fixes = band-limited mip-mapping + oversampling. Punchline: *"Hi-Q off is a PPG. Hi-Q on is a Serum."* FM *generates* (Bessel sidebands); wavetable *interpolates* between pre-stored snapshots; Wavetable hides an FM oscillator inside each osc. **>> SIGNPOST → Act 4.**

## 4. Device Deep-Dive (Ableton Wavetable)  ·  `04a`–`04f`  ·  8–9 min

**Synopsis.** Ableton-specific, structured around one live driving question (the Ep1 Section-4 anti-flatline fix): *Ableton came to wavetable LAST — what did they leave OUT on purpose, what did they build the whole instrument AROUND, and what can it do that Serum can't in one click?* Every beat answers it: architecture → the per-osc warp engine → the destination-first matrix (the heart) → the modulators that serve Position → filters/unison → the honest verdict vs Serum.

- **Demos:**
  - `wt-modern-fold-sweep` (04b) — Modern→Fold wavefolder sweep; buzzy upper harmonics from one oscillator, no extra device. *(⚠ Effect Mode = Modern set by hand.)*
  - `wt-lfo-to-position` (04c) — LFO→Position wobble at 1/8 with NO pitch change (the wub). *(⚠ matrix routing set by hand.)*
  - `wt-lfo-attack-bloom` (04d) — slow LFO→Position with ~2 s Attack; the morph blooms only after the note is held. *(⚠ matrix routing set by hand.)*
  - `wt-position-spread-chord` (04e) — Position Spread unison; a chord of timbres from one note. *(⚠ Unison Mode set by hand; headless proves width only.)*
- **Key facts/claims.** Two wavetable oscillators + a Sub; 194 tables / 12 categories; Suite-only, Live 10 (2018); user import in 10.1 (256 frames). The per-osc warp engine: **FM** (hidden sine modulator, ±2 oct), **Classic** (synced PWM), **Modern** (Warp / Fold wavefolding) — "an FM oscillator hiding inside each wavetable oscillator." The matrix is **destination-first** (Hobson: "I want this parameter modulated by this") — tweak a control and it appears as a new row; 3 envelopes + 2 LFOs + 5 MIDI sources (incl. MPE Pressure/Slide); the canonical routings emphasize **LFO→Position** (wobble), **slow Env→Position** (pad), **multiple sources→Position+filter** (growl). LFO **Attack fade-in** (~2 s) is the underrated control. Two identical multimode filters, three routings — Serial / Parallel / **Split** (per-osc filtering); five **Cytomic** circuits — Clean / OSR (OSCar) / MS2 (MS-20) / SMP / PRD (Moog Prodigy) — the same physically-modeled circuits as Auto Filter and Operator. Six unison modes; **Position Spread** = a chord of timbres in one click. Verdict: reach for **Serum** to *build* tables (draw/import/FFT); reach for **Wavetable** to *play and modulate* them inside Live with least friction — the missing FFT editor is a *curation* choice. **>> SIGNPOST → Act 5.**

## 5. Patch Walkthrough — PPG choir → Subtronics growl  ·  `05a`–`05g`  ·  5–6 min

**Synopsis.** One cumulative arc: build a PPG-style evolving morph pad from the default, then turn the *same* patch into a Subtronics-style growl with one macro — proving they're the same instrument. Each step adds ONE thing so the listener hears exactly what it does. Explicit progress markers ("step 3 of 7", "halfway — arm the growl") guard the Ep1 Section-5 marker gap. The macro sweep is the payoff the act exists for.

- **Demos (7 cumulative build steps):**
  - `wt-spectra-step1` (05a) — static vowel pad (Formants table + slow amp env). *(⚠ Formants table by hand.)*
  - `wt-spectra-step2` (05b) — slow LFO→Position + ~2 s Attack = the PPG choir bloom. *(⚠ matrix by hand.)*
  - `wt-spectra-step3` (05c) — Position Spread unison (chord of timbres) + gentle OSR filter. *(⚠ Unison Mode by hand.)*
  - `wt-spectra-step4` (05d) — Sub for weight + Osc 2 (+1 oct bell/Harmonics) for glass (the DM bell layer). *(⚠ bell table + Sub Transpose by ear.)*
  - `wt-spectra-step5` (05e) — halfway: arm the growl — fast LFO 2→Position (bypassed), Env→Filter, Osc 1 FM edge. *(⚠ FM mode + matrix by hand.)*
  - `wt-spectra-macro-sweep` (05f) — ONE Macro 0→127 turns the pad into a growl (the payoff). *(⚠ Macro + matrix by hand.)*
  - `wt-spectra-morph-final` (05g) — the saved **"Spectra-Morph"** patch, demonstrated as a phrase.
- **Key facts/claims.** Build order on-screen: Formants/vocal table → Amp env A≈800 ms/S full/R≈1.5 s → LFO 1 (triangle) → Position ~30 with ~2 s Attack → Unison Position Spread 4 voices + OSR filter → Sub −1 oct (Tone ~15%) + Osc 2 +1 oct bell (low gain) → LFO 2 (saw) → Position 1/8 amount ~50 bypassed + Env → Filter + Osc 1 FM ~20 → Macro: 0 = slow pad LFO, 127 = fast wobble + tighter filter + mono/glide. Landing line: *"The PPG and Skrillex are the same instrument with the LFO rate turned up."* **>> SIGNPOST → Act 6.**

## 6. IDM Application  ·  `06a`–`06e`  ·  5–6 min

**Synopsis.** Four ways IDM uses Position when nobody's selling a preset for it: scan your own source → rhythm from a looping envelope → the grit on purpose → per-note expression → then the exercise. Closes on the exercise and a stop, never a kicker (voice rule); lands the focus sentence and the refrain as resolution.

- **Demos & songs:**
  - `wt-user-table-scan` + `polymer-clip` (06a) — import a WAV onto the sprite area (up to 256 frames), route Env/LFO → Position; "Plaid's *Polymer* method — wavetable as texture, not bass." *(⚠ import + Env→Pos by hand.)* Song: ~8 s of Plaid *Polymer* scanning texture.
  - `wt-loop-env-sequence` (06b) — a free envelope in Loop → Position + 1/16 LFO on FM Amount; one held note becomes a self-sequencing pattern. *(⚠ FM mode + Env→Pos by hand.)*
  - `wt-hiq-off-grit` (06c) — Hi-Q OFF + Distortion table + Modern→Fold + fast sweep = the on-purpose Hamburg grit; pays off the 03d switch as a creative decision. *(⚠ Modern + Distortion table; Hi-Q default OFF.)*
  - `wt-mpe-pressure-position` (06d) — MPE Pressure → Position; per-note brightness scanned by finger pressure. *(⚠ MPE + matrix by hand; headless proves a ladder, not per-voice independence.)*
- **Key facts/claims.** Live reads up to 256 frames on import. **Autechre framed honestly:** their wavetable lineage is the Ensoniq EPS transwave, not PPG/Waldorf — the loop-envelope move is named as the *idea* (sequencing/synthesis line blurring), not a hardware claim. **Aphex × Waldorf Iridium (2026)** collaboration is confirmed but **no James quote and no confirmed released track** — flagged inline at 06d. Exercise (06e): open Wavetable, pick Basic Shapes, hold one note, modulate only Position (envelope / LFO / mod wheel / pressure) for ~40 s — no new notes, no filter sweeps. *"You don't have to filter a sound to make it move, you can walk between sounds … Pitch and timbre, separate dials. Walk the timbre."* Then stop (no kicker).

---

## 7. Demos at a Glance

| Section | Demos (id · concept) |
|---|---|
| 3 — Synthesis | `wt-position-by-hand` (Position→timbre, pitch held — THE key demo) · `wt-ab-two-positions` (a table = a set of spectra) · `wt-zipper-vs-smooth` (interpolation: zipper→glide ⚠) · `wt-hiq-on-vs-off` (Hi-Q: PPG vs Serum ⚠) · `wt-fm-inside-wavetable` (hidden FM osc, Ep1 bridge) |
| 4 — Device | `wt-modern-fold-sweep` (Modern→Fold wavefold) · `wt-lfo-to-position` (LFO→Pos wobble, no pitch change) · `wt-lfo-attack-bloom` (LFO Attack fade-in bloom) · `wt-position-spread-chord` (Position Spread = chord of timbres) |
| 5 — Walkthrough | `wt-spectra-step1`…`step5` · `wt-spectra-macro-sweep` (one macro pad→growl) · `wt-spectra-morph-final` (saved "Spectra-Morph") |
| 6 — IDM | `wt-user-table-scan` (import + scan, Plaid) · `wt-loop-env-sequence` (loop env→Pos self-sequencer) · `wt-hiq-off-grit` (aliasing on purpose) · `wt-mpe-pressure-position` (Pressure→Pos) |

## 8. Reproducibility & Known Limitations

Each demo ships a `tutorials/<id>.md` (click-by-click build from a default Wavetable) and an `.adv`
preset (see `presets/SAVE_CHECKLIST.md`). Params/automation are reconciled verbatim against
`param_maps/wavetable.json` (93 real LOM params); see `DEMO_VERIFICATION.md` for the full table.

**Hard LOM limitations** (set in Live by hand before saving — flagged per tutorial):
wavetable table/category selection · Osc Effect Mode (FM/Classic/Modern) · Hi-Q oversampling toggle ·
the mod matrix (rendered as direct destination automation) · Unison Mode/Voices (Position Spread) ·
Macros / MPE Pressure. **Two demos cannot demonstrate their concept headless** —
`wt-zipper-vs-smooth` and `wt-hiq-on-vs-off` (both hinge on the Hi-Q toggle); hand-render or fold the
point into narration. **Two render at reduced fidelity** — `wt-position-spread-chord` (proves width,
not the spread mode) and `wt-mpe-pressure-position` (proves a brightness ladder, not MPE per-voice
independence); note on-mic or supplement with a hand demo.
