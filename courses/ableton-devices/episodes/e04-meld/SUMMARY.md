# e04-meld — Episode Summary

## Metadata

| Field | Value |
|---|---|
| **Episode id** | `e04-meld` |
| **Title** | Meld: The Bi-Timbral Macro-Oscillator Synth |
| **Device** | Ableton **Meld** — a **bi-timbral, dual macro-oscillator, MPE-first synth**. **NOT a physical modeller** (the only physical-modelling DSP is the modal Plate/Membrane resonator *filters*). |
| **Shipped** | Live **12.0**, **5 March 2024** (NOT 12.1). Chord oscillator added 12.2 → 24 osc types at launch, 25 for a 12.4 user. **Suite-only.** |
| **Status** | **Editorial-locked, NOT yet published.** Scripts drafted (`script/*.md`), demos reconciled to the real LOM param map, tutorials + save checklist written. |
| **Scope** | ~27 slides across 6 acts · 19 device demos · target ~40 min. |
| **Focus sentence** | "Operator builds a spectrum and Wavetable scans one, but Meld hands you twenty-five ready-made worlds — two knobs each — lets you run two of them at once, and routes your fingers into them: so you don't engineer a sound here, you pick one and play it." |
| **Driving question** | If this synth gives you almost nothing to edit — two knobs per oscillator — where did all the control go, and why is the most important part of Meld not an oscillator at all? |
| **Payoff** | The control didn't vanish — it moved out of the patch and into the **performance**: the per-note matrix over MPE is the instrument. |
| **Payoff refrain** | "You don't build the sound. You pick it — and then you play it." (seeded cold open, echoed each act boundary, landed in 06e). |
| **Myth refrain** | "It's a filter, not the oscillator." (planted 03c, echoed 05b, landed 06d/06e). |

### Two on-air myth-busts (aired as cold-open confessions, recapped in 06d)
1. **Meld is NOT a physical-modelling hybrid.** The "physical modelling" on the box resolves to exactly two **modal resonator filters** (Plate / Membrane) — a *filter*, not the oscillator.
2. **Meld did NOT arrive in 12.1.** It shipped the day Live 12 did — **12.0, 5 March 2024**. The Chord oscillator is the only post-launch addition (12.2).

### Honesty constraint (no canon)
Meld is a 2024 instrument with **no canon of famous records**. **No artist/track is claimed to use Meld.** Every artist beat is **aesthetic kinship or technique illustration only**: Aphex Twin (per-note timbre, Iridium/AFX Mode), Autechre (self-sequencing-timbre aesthetic), Squarepusher (honest negative — builds his own tools), Plaid / Boards of Canada (texture targets, not Meld gear), Mutable Instruments Plaits (the macro-oscillator *lineage*, not "Plaits inside").

### Render-readiness at a glance (19 demos)
- **Fully renderable headless (pass Gate 7 as written): 8** — `shepard-pi-cold-open`, `meld-one-knob-three-worlds`, `meld-type-switch-live`, `meld-squelch-feedback`, `meld-swarm-scale-snap` (set Scale first), `meld-twohands-step1`, `meld-rain-crackle-sub` (working direct-Rate fallback), `meld-shepard-under-pad`.
- **Renderable but PLACEHOLDER Plate-Resonator filter index to confirm live: 1** — `meld-plate-resonator` (idx carries into Two-Hands steps).
- **Hand-build (modulation matrix not exposed over LOM): 5** — `meld-modenv-loop-macro`, `meld-lfo-to-macro`, `meld-twohands-step3`, `meld-twohands-step4`, `meld-self-sequence-onenote`.
- **Play-it-yourself MPE (per-note + matrix, cannot render): 4** — `meld-mpe-per-note`, `meld-twohands-step5`, `meld-twohands-final` (`-step6` renders the glue contrast; its matrix is carried hand-build).

*(~9 demos cannot be proven over the headless path — the 5 matrix-dependent + the 4 MPE play-it-yourself. For these the tutorial IS the deliverable.)*
*Two placeholder enum indices need live confirmation: **Plate Resonator** `Filter Type` idx, and **Mod Loop Mode** 0–3 ordering (AD Loop / Loop).*

---

## Table of Contents
1. [Act 1 — Cold Open](#act-1--cold-open) · `01-cold-open`
2. [Act 2 — History & Theory](#act-2--history--theory) · `02a`–`02d`
3. [Act 3 — Synthesis Deep-Dive](#act-3--synthesis-deep-dive) · `03a`–`03e`
4. [Act 4 — Device Deep-Dive (Ableton Meld)](#act-4--device-deep-dive-ableton-meld) · `04a`–`04e`
5. [Act 5 — Patch Walkthrough ("Two-Hands")](#act-5--patch-walkthrough-two-hands) · `05a`–`05g`
6. [Act 6 — IDM Application](#act-6--idm-application) · `06a`–`06e`

---

## Act 1 — Cold Open
**Slide:** `01-cold-open` · ~90s · structure: confession/contradiction.

**Synopsis.** Open cold on a Meld **Shepard's Pi** patch alone — a barberpole tone that seems to rise forever and never arrives, held ~8s under the narration, then ducked. Name the strangeness concretely: another oscillator in the same box sounds like actual rain; a third like loading a cassette game in 1984 — and you reach any of them with one knob. State the reframe plainly (the last three episodes we *built* sounds; this one we **pick** one and play it), and air **both myth-busts as confessions** up front so no later beat builds on the wrong frame. Plant the four-stop act map and the payoff refrain.

**Demos used.** `shepard-pi-cold-open` — Shepard's Pi endless-rise, one oscillator type / one knob; the cold-open hook (fully renderable).

**Catalog / kinship.** None foreground; bed = Plaid (wavetable drift) seeded later. The Shepard illusion is a psychoacoustics reference, not a track.

**Key facts.** Both myth-busts land here (not a physical modeller; shipped 12.0 not 12.1). First instance of the "you pick it, and you play it" refrain. `>> SIGNPOST` into Act 2 names the four stops.

---

## Act 2 — History & Theory
**Slides:** `02a-what-a-macro-osc-is` · `02b-plaits-lineage` · `02c-mpe-paradigm` · `02d-where-meld-sits` · 8–9 min.

**Synopsis.** Ordered by "what do I need next?" — what a macro-oscillator IS (one slot hiding a whole DSP algorithm behind two macros, meaning per type; the explicit trade: lose fine editability, gain instant breadth) → the **Mutable Instruments Plaits lineage** (Braids 2013 → Plaits 2018; Émilie Gillet; open-source MIT DSP that propagated to Brains / MicroFreak / VCV; *lineage, not "Plaits inside"*) → **MPE: a channel per finger** (MMA-adopted 2018; per-note bend, Slide/CC74, pressure; the gesture becomes a per-voice modulation source) → where Meld sits in Live's four-synth map (Operator generates, Wavetable scans, Analog subtracts, Meld picks-and-plays). The act opens on the thesis-as-sound and lands on the map.

**Demos used.**
- `meld-one-knob-three-worlds` (`02a`) — one held note, Macro 1 sweeps Basic Shapes, then Osc Type switches to Harmonic FM, then Rain; the thesis audible in 90s (renderable).
- `plaits-module-ref` (`02b`) — a real Plaits *module* sweeping a couple of models; the lineage reference, labelled "a module, not Meld" (song/module clip, not a Meld render).

**Catalog / kinship.** Plaits = the macro-oscillator genre-definer (lineage). Aphex Twin per-note obsession (Waldorf Iridium collab / Bass Station II "AFX Mode") as the *idea* MPE serves — kinship, not Meld credit.

**Key facts.** "Plaits inside Meld" is FALSE — say "lineage" / "acknowledged influence" (Rob Tubb quote). **Version myth busted at 02d**: 12.0, 5 March 2024; Chord oscillator added 12.2. Christian Kleine + Rob Tubb design team; Kleine: "two synthesizers in one … the sum bigger than its parts." `>> SIGNPOST` into Act 3.

---

## Act 3 — Synthesis Deep-Dive
**Slides:** `03a-the-osc-families` · `03b-fm-the-macro-way` · `03c-modal-resonators` · `03d-scale-aware` · `03e-lfo-loop-env` · 8–9 min.

**Synopsis.** What's actually behind the two knobs. The **families** (virtual-analog, FM, swarm/supersaw, buffer-loop "granular-esque" — caveat: NOT a true granular cloud, noise/environmental Rain/Bubble/Crackle — synthesized not sampled, lo-fi/chiptune, special: Shepard's Pi / Tarp), each a parameterized DSP routine whose two macros map per-type onto the few internal parameters that matter. Then **FM the macro way** (the explicit Operator/Ep1 callback: Harmonic FM = index + ratio; FM Bass/Squelch surfaces operator **feedback**, same Bessel sidebands underneath) → the **modal resonators** (the ONE physical-modelling element, myth payoff) → **scale-aware oscillators** (six types snap inharmonic partials to the Live Scale) → **audio-rate LFOs + loop envelopes** (LFO reaches ~200 Hz back-door FM/AM; Mod Env in AD Loop → macro = a self-cycling sequencer — the seam into Act 6).

**Demos used.**
- `meld-type-switch-live` (`03a`) — one held note, A/B/C across Osc Type (Basic Shapes → Harmonic FM → Rain); "same note, three instruments" (renderable).
- `meld-squelch-feedback` (`03b`) — FM Bass (Squelch), raise the Feedback macro; sine → saw → noise edge (renderable sweep; the Ep1 feedback callback).
- `meld-plate-resonator` (`03c`) — bright source → Plate Resonator filter; a struck body-resonant tone (renderable; **Plate filter idx PLACEHOLDER — confirm live**).
- `meld-swarm-scale-snap` (`03d`) — Swarm Sine, wide spacing, scale-aware OFF vs ON; the spread snaps into key (renderable; set Set Scale first).
- `meld-modenv-loop-macro` (`03e`) — one held note, Mod Env AD-Loop → macro; the timbre sequences itself (**HAND-BUILD — matrix route not renderable**).

**Catalog / kinship.** Squarepusher — TX81Z FM lead / metallic feedback (the FM-feedback callback for 03b); honest negative: he builds his own tools.

**Key facts.** **MYTH PAYOFF at 03c:** "This — and only this — is the physical modelling on the box. And it's a filter, not the oscillator." Plants the **"It's a filter, not the oscillator."** refrain. "Granular-esque" buffer-loop is NOT a true granular cloud — don't oversell (03a). Kleine: scale-aware oscillators are "a must-have for any modern synth" (03d). `>> SIGNPOST` into Act 4.

---

## Act 4 — Device Deep-Dive (Ableton Meld)
**Slides:** `04a-bi-timbral` · `04b-macros-and-matrix` · `04c-mpe-hands-on` · `04d-filters-mixer-global` · `04e-when-to-reach` · 8–9 min.

**Synopsis.** The act is held together by ONE planted driving question (the ep1 Section-4 anti-flatline fix): two knobs per oscillator — so where did the control GO, what is the heart of the instrument, and what do bi-timbral + MPE do that no other Live synth can? Every beat answers it: **04a** — bi-timbral = two *full* engines (each a complete voice: osc + filter + two envelopes + two LFOs + its own matrix), **summed**, with control-rate cross-mod only (no audio-rate cross-mod between engines); **04b** — the two oscillator macros are first-class matrix *targets* ("the macro is the new Position," the Ep3 callback; ~23 targets, sources incl. the other engine, bipolar amounts); **04c** — **MPE is where the control went** (per-note Bend / Slide / Press as matrix sources; the matrix runs **per-voice**, so one patch makes different timbres on simultaneously held notes — the answer); **04d** — 17 filter types per engine + mixer + global serve the two engines (kept tight); **04e** — when to reach for Meld (character / texture / per-note expression fast) vs Operator/Wavetable (engineer a spectrum).

**Demos used.**
- `meld-lfo-to-macro` (`04b`) — LFO 1 → Macro 1; the timbre breathes, pitch unchanged (**HAND-BUILD — matrix route**).
- `meld-mpe-per-note` (`04c`) — two held notes, express one (Press/Slide) while the other sits still; per-voice morph (**PLAY-IT-YOURSELF MPE — cannot render**; channel-aftertouch fallback noted on-air).

**Catalog / kinship.** Boards of Canada texture bed under the act (aesthetic only). Aphex per-note expression as the MPE idea (kinship).

**Key facts.** **Bi-timbral = two *summed* engines, control-rate cross-mod only** — get this exactly right (04a). "The macro is the new Position" reframes Wavetable's Position as a matrix target (04b). **Voice cap 12 vs 32 is UNRESOLVED** — say "up to a few dozen voices" unless verified live (04d). `>> SIGNPOST` into Act 5.

---

## Act 5 — Patch Walkthrough ("Two-Hands")
**Slides:** `05a` … `05g` · 5–6 min · build one bi-timbral, MPE-played texture-lead, one element per step.

**Synopsis.** A single additive arc proving "two synths, one note, ten fingers." Each step isolates exactly the one added element vs the previous (verification = `build-step`), with explicit position markers (the ep1 Section-5 progress-marker fix). Step 1 Engine A Swarm Saw, scale-locked (the anthemic body) → Step 2 Engine B Harmonic FM an octave up into a Plate Resonator filter (echo the filter myth) → Step 3 cross-engine A's LFO drives B's macro (control-rate) → Step 4 Engine A Mod Env AD-Loop → A's macro (self-morph; the seam to Act 6) → Step 5 "halfway — wire the fingers in": MPE Press → B FM Amount, Slide → A filter, Note Bend → A detune → Step 6 global glue (Drive, Limiter, Voice Spread) → Step 7 save as **"Two-Hands."**

**Demos used.**
- `meld-twohands-step1` (`05a`) — Swarm Saw body (renderable; set Scale).
- `meld-twohands-step2` (`05b`) — + Engine B Harmonic FM → Plate Resonator (renderable; **Plate idx PLACEHOLDER**).
- `meld-twohands-step3` (`05c`) — + cross-engine LFO → B macro (**HAND-BUILD — matrix**).
- `meld-twohands-step4` (`05d`) — + Mod Env AD-Loop self-morph (**HAND-BUILD — matrix**).
- `meld-twohands-step5` (`05e`) — + MPE Press/Slide/Bend (**PLAY-IT-YOURSELF MPE**).
- `meld-twohands-step6` (`05f`) — + global Drive/Limiter/Voice Spread (glue contrast renderable; matrix carried hand-build).
- `meld-twohands-final` (`05g`) — the capstone "Two-Hands" MPE phrase (**PLAY-IT-YOURSELF MPE + full matrix**).

**Catalog / kinship.** Squarepusher squelchy FM-bass transition out of the act (aesthetic bridge).

**Key facts.** **05b echoes "It's a filter, not the oscillator."** **No "Stacked Voices" param exists** — the slide heading says it, but width comes from `Voice Spread`; do not narrate "Stacked Voices" (05f). `B Octave 1` (not `B Transpose 12`) for the octave-up layer. `>> SIGNPOST` into Act 6. 05g ties the build back to the focus sentence: "Operator built a spectrum. Wavetable scanned one. Meld gave you two synths and ten fingers and got out of the way."

---

## Act 6 — IDM Application
**Slides:** `06a-self-sequencing` · `06b-environmental-osc` · `06c-shepard-trick` · `06d-myth-recap` · `06e-exercise` · 5–6 min.

**Synopsis.** Three ways IDM uses Meld when there's no preset for what you want, then the myths logged and the exercise. **06a** modulate-don't-write (the Autechre idea): Mod Env AD-Loop → macro + audio-rate LFO → filter for sideband grit; hold ONE note and it becomes a pattern (the Confield-era aesthetic, method-kinship only). **06b** environmental oscillators as the *source* (Rain / Crackle / Bubble; Loop Mod Env → macro for evolving weather; Engine B Sub for body — the Boards-of-Canada-adjacent texture target, synthesized not sampled). **06c** the **Shepard trick**, back to the cold open: Shepard's Pi under a pad as an endless build for tension. **06d** the two myths logged (not a physical modeller — that was two resonator filters; not 12.1 — shipped 12.0). **06e** the exercise: one note, forty seconds, make it tell a story — then stop, no kicker. The payoff refrain and the myth refrain both LAND here as resolution.

**Demos used.**
- `meld-self-sequence-onenote` (`06a`) — one held note → pattern via Mod Env AD-Loop → macro + audio-rate LFO → filter (**HAND-BUILD — matrix**; LFO Rate 1.0 normalized = audio-rate, not 200 Hz).
- `meld-rain-crackle-sub` (`06b`) — Rain (source) + Sub (body), evolving weather (renderable via working direct-Rate fallback; Loop matrix kept for the tutorial/.adv).
- `meld-shepard-under-pad` (`06c`) — Shepard's Pi under a Basic-Shapes pad; the cold-open patch put to work (fully renderable, no matrix).

**Catalog / kinship.** Autechre — self-generating pattern (06a, method-kinship; custom Max/MSP, not Meld). Boards of Canada — environmental-texture aesthetic (06b; analog/sampler, not Meld). All kinship, never Meld credit.

**Key facts.** **06d recaps both myth-busts** and lands "It's a filter, not the oscillator." 06c is the explicit cold-open callback (Shepard's Pi). 06e closes on the exercise + the landed payoff refrain ("You don't build the sound here. You pick it — and then you play it. That's Meld."), then stops — **no motivational kicker** (voice rule).

---

## Cross-act references

- **Catalog spine (kinship only, no Meld credit):** Plaid — *Polymer* (timbre-as-composition); Boards of Canada — *Geogaddi* (environmental texture); Autechre — *Confield* (self-sequencing timbre); Squarepusher — *Beep Street* (TX81Z FM feedback); Mutable Instruments Plaits (the macro-oscillator lineage).
- **Course callbacks:** Operator/Ep1 (FM + feedback, 03b); Wavetable/Ep3 ("the macro is the new Position," 04b); Analog (subtractive) in the four-synth map (02d).
- **Refrains:** payoff "You don't build the sound. You pick it — and then you play it." (01 → act boundaries → 06e); myth "It's a filter, not the oscillator." (03c → 05b → 06d/06e).
- **Artifacts:** `tutorials/<id>.md` (19, one per demo) · `presets/SAVE_CHECKLIST.md` (19 presets, grouped) · `clip_manifest.yaml` `device_demos` (19, reconciled to `param_maps/meld.json`) · `DEMO_VERIFICATION.md` (LOM reconciliation + render-readiness).
