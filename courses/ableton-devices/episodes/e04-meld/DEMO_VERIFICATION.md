# e04-meld — Demo Reconciliation & Verification

Reconciliation of `clip_manifest.yaml` `device_demos:` against the dumped LOM param map
`courses/ableton-devices/tools/device_render/param_maps/meld.json` (129 params, captured 2026-06-29).
Authoritative source for names/ranges = that map. Concept anchors = `specs/ableton_course_ep4_meld_research.md`.

**Reconciled:** 2026-06-29. **All 19 demos** now use param names that exist verbatim in meld.json and
values in range (machine-checked). The blocker for full headless coverage is the **modulation matrix and
MPE**, neither of which is exposed in the LOM param map.

---

## Hard LOM facts that drove the reconciliation

| Manifest used (wrong) | Real LOM name | Notes |
|---|---|---|
| `Engine A `/`Engine B ` | `A `/`B ` | every prefix renamed |
| `Osc Macro 1` / `Osc Macro 2` | `A Osc Shape` / `A Osc Tone` | the two oscillator macros; 0–1, meaning per type |
| `Osc Type: "Basic Shapes"` | `A Osc Type` = **numeric index** | value_items come back **EMPTY** over LOM → enum **strings do not resolve**; must pass index (dossier §1.2 table) |
| `Filter Macro 1` / `Filter Macro 2` | `A Filter Freq` / `A Filter Q` | cutoff / resonance, 0–1 |
| `Filter Type: "Lowpass"` | `A Filter Type` = **numeric** + `A Filter L-B-H-N` | analog filter idx 0; L-B-H-N=0 = lowpass response |
| `Filter Scale Aware` | `A Filter Filter Scale Aware` | (yes, doubled word — verbatim LOM) |
| `Amp Env Attack/Decay/Sustain/Release` | `A Amp Attack/Decay/Sustain/Release` | no "Env" token; times normalized 0–1 |
| `Mod Env Mode: "AD Loop"` | `A Mod Loop Mode` = **numeric 0–3** | order of {Trigger/Loop/AD Loop/…} UNCERTAIN — placeholders set |
| `Mod Env Attack/Decay` | `A Mod Attack/Decay` | mod env is Initial/Attack/Peak/Decay/Sustain/Release/Final |
| `LFO 1 Shape: "Sine"` | `A LFO 1 Type` = **numeric 0–5** | `A LFO 1 Shape` is a separate wave-SHAPING macro, not the selector |
| `LFO 1 Rate: 200` (Hz) | `A LFO 1 Rate` = **0–1 normalized** | 1.0 = top ≈ 200 Hz; NEVER pass Hz |
| `Transpose: 12` | `A Octave: 1` | `A Transpose` maxes ±12 **semitones**; use `A Octave` (-3..3) for octaves |
| `Detune: 0` | `A Detune: 0.5` | 0–1, **0.5 = 0 cents** |
| `Global Drive` | `Drive` | 0–1 |
| `Global Limiter: "On"` | `Limiter On: 1` | 0/1 |
| `Spread` | `Voice Spread` | 0–1 |
| `Stacked Voices: 2` | **(no param)** | removed — not in LOM map |
| `Voicing: "Poly"/"Mono"` | **(no param)** | removed — voicing is not an exposed device param (there is `Mono Legato`, per-engine `Glide Mode`) |
| `Global Scale: "C Minor"` | **(no param)** | removed — scale is a Live-set/clip property; device has master `Scale Aware` (0/1) + per-osc `A Osc Scale Aware` |

### Two structural blockers (flagged per demo)

1. **No modulation matrix in the LOM map.** Every `LFO→macro`, `Mod Env→macro`, cross-engine `A→B`, and
   `MPE→target` route is **unrenderable** over the param-set path. Those demos keep a `matrix:` block for the
   hand-build / `.adv` / tutorial, and carry an `automation:` **NO-MATRIX-FALLBACK** that moves the target
   macro **directly** so audible motion still renders. A single ramp is **not** an LFO/loop, so it does **not**
   satisfy the cyclic/recurrence assertions — those demos must be **hand-built in the live device** to pass Gate 7.
2. **MPE per-note expression is not authorable** over this MIDI-clip render path. MPE demos are **play-it-yourself**
   moments; any static render proves layering but **not** per-voice behavior.

### Index placeholders that need live confirmation
- **`A/B Filter Type` Plate Resonator index** — set to **15 (PLACEHOLDER)**. No value_items, no doc ordering.
  Orchestrator must read the live filter-type list and correct the index in: `meld-plate-resonator`,
  `meld-twohands-step2/3/4/5/6/final`.
- **`A/B Mod Loop Mode` order** — AD Loop set to **2**, Loop to **1** (PLACEHOLDER). Confirm the 0–3 ordering live.

---

## Per-demo table

| id | concept | param-names OK? | isolates one variable? | reference | key changes | confidence | LOM limitation |
|---|---|---|---|---|---|---|---|
| meld-one-knob-three-worlds | macro sweep + type switch = breadth | ✅ all verbatim | ✅ Osc Shape sweep (seg1) then Osc Type | §5.6 #1; §1.2 table | Engine→A, macros→Osc Shape/Tone, types→indices 0/9/12, added `A Volume`, Filter→Freq/Q+L-B-H-N | High | none — renderable (A/B is split render) |
| shepard-pi-cold-open | Shepard illusion = one osc type | ✅ | ✅ Osc Type=13 | §5.6, §6 cold open; idx 13 | renamed all, type 13, Limiter On=1, Detune 0.5 | High | none — fully renderable |
| meld-type-switch-live | one note, change the world | ✅ | ✅ Osc Type 0/9/12 | §5.6 #1, Beat "25 oscillators" | renamed, indices, Volume added | High | none (A/B split render) |
| meld-squelch-feedback | FM feedback → complexity (Ep1 callback) | ✅ | ✅ Osc Tone (Feedback) swept | §4 Concept 2, §5.2 | type 17, macro2=Osc Tone swept, Drive 0.1 | High | none — sweep renders headless |
| meld-plate-resonator | the "physical modelling" is a FILTER | ✅ (Filter idx placeholder) | ✅ Filter Type OFF/ON | §1.4, §5.3, §6 Beat 3 | Filter Type→numeric, Plate idx **15 placeholder**, scale-aware param, Freq/Q as resonator macros | Med — Plate idx unconfirmed | **Plate Resonator index UNCONFIRMED** (no value_items) |
| meld-swarm-scale-snap | scale-aware partials snap to key | ✅ | ✅ A Osc Scale Aware 0/1 | §1.3, §4 Concept 5 | type 20, scale-aware param 0/1, removed Global Scale (Live-set prop), added master `Scale Aware` | Med-High | scale is a **Live-set/clip** property — orchestrator sets the Set's Scale before render |
| meld-modenv-loop-macro | Mod-Env loop → macro = self-sequencer | ✅ | ✅ (concept) Mod Loop → Osc Shape | §1.5, §4 Concept 6, §5.6 #4 | type/macros/env renamed, Mod Loop Mode idx 2 (placeholder), **NO-MATRIX-FALLBACK** automation | Low for Gate-7 | **matrix route not renderable** → hand-build to prove recurrence; loop-mode idx UNCERTAIN |
| meld-lfo-to-macro | macro is a matrix target (timbre breathes) | ✅ | ✅ (concept) LFO 1 → Osc Shape | §1.7, §6 Beat 2 | LFO Rate→0–1 normalized, LFO Type numeric, **NO-MATRIX-FALLBACK** | Low for Gate-7 | **matrix route not renderable** → cyclic assertion fails without hand-build |
| meld-mpe-per-note | per-voice morph over MPE | ✅ | ✅ (concept) per-note Press/Slide | §1.8, §5.4, §6 Beat 3 | renamed, targets→A Osc Shape/Filter Freq | n/a render | **CANNOT RENDER** — MPE + matrix; play-it-yourself |
| meld-twohands-step1 | build: Swarm Saw body | ✅ | ✅ Engine A only | §6 Patch Step 1 | type 19, scale-aware, Volume | High | none — renderable |
| meld-twohands-step2 | build: + Engine B FM → Plate Resonator | ✅ (Plate placeholder) | ✅ Engine B added | §6 Step 2 | B engine, `B Octave 1` (was Transpose 12), Plate idx placeholder | Med | Plate idx unconfirmed |
| meld-twohands-step3 | build: cross-engine A LFO → B macro | ✅ | ✅ (concept) cross-engine route | §6 Step 3 | **NO-MATRIX-FALLBACK** (sweep B Osc Shape) | Low for Gate-7 | matrix cross-engine not renderable |
| meld-twohands-step4 | build: + Mod-Env AD-Loop self-morph | ✅ | ✅ (concept) Mod Env → A macro | §6 Step 4 | Mod Loop Mode 2, **NO-MATRIX-FALLBACK** | Low for Gate-7 | matrix not renderable |
| meld-twohands-step5 | build: wire MPE in | ✅ | ✅ (concept) MPE sources | §6 Step 5 | renamed targets | n/a render | **CANNOT RENDER** — MPE + matrix |
| meld-twohands-step6 | build: global glue (Drive/Limiter/Spread) | ✅ | ✅ Drive+Limiter+Voice Spread | §6 Step 6 | `Stacked Voices` removed (no param), `Spread`→`Voice Spread` | High (glue renders) | matrix carried as hand-build; glue contrast IS provable |
| meld-twohands-final | capstone MPE phrase | ✅ | n/a (capstone) | §6 Step 7, outro | renamed; full matrix as hand-build | n/a render | **CANNOT FULLY RENDER** — MPE phrase + matrix |
| meld-self-sequence-onenote | one note → pattern (Autechre move) | ✅ | ✅ (concept) Mod Loop + audio-rate LFO | §4 Concept 6, §6 IDM Beat 1 | LFO Rate→1.0 normalized (was 200), Mod Loop 2, **NO-MATRIX-FALLBACK** | Low for Gate-7 | matrix routes not renderable → hand-build for recurrence |
| meld-rain-crackle-sub | environmental osc as source | ✅ | ✅ A Osc Type=Rain (Rate evolves) | §4 Concept 3, §6 IDM Beat 2 | Rain=12, Sub=18, **WORKING FALLBACK** (sweep Rate macro directly → real evolving weather) | **Med-High** | matrix Loop-env kept for tutorial; **direct Rate sweep fallback DOES evolve & verify** |
| meld-shepard-under-pad | Shepard build under pad (callback) | ✅ | ✅ A=Shepard, B=pad | §4 Concept 8, §6 IDM Beat 3 | renamed, `B Octave`, no matrix needed | High | none — **fully renderable** |

---

## Render-readiness summary

**Fully renderable headless, will pass Gate 7 as written (no hand-build):** 8
`meld-one-knob-three-worlds`, `shepard-pi-cold-open`, `meld-type-switch-live`, `meld-squelch-feedback`,
`meld-swarm-scale-snap` (set Live-set Scale first), `meld-twohands-step1`, `meld-rain-crackle-sub`
(working direct-Rate fallback), `meld-shepard-under-pad`.

**Renderable but with an UNCONFIRMED filter-type index (Plate Resonator) to fix live before trusting:** 2
`meld-plate-resonator`, `meld-twohands-step2` (and the Plate idx carries into steps 3/4/5/6/final).

**NEEDS HAND-BUILD of the modulation matrix to satisfy the cyclic/recurrence assertion (fallback renders
audible motion but FAILS Gate 7 as-is):** 5
`meld-modenv-loop-macro`, `meld-lfo-to-macro`, `meld-twohands-step3`, `meld-twohands-step4`,
`meld-self-sequence-onenote`.

**CANNOT render headless — MPE play-it-yourself (per-note + matrix):** 4
`meld-mpe-per-note`, `meld-twohands-step5`, `meld-twohands-final`. *(`step6` renders the global-glue contrast;
its matrix is carried for the hand-build only.)*

### Orchestrator action items before/at render
1. **Confirm the `A Filter Type` 0–16 ordering** in the live device and correct the **Plate Resonator** index
   (placeholder = 15) everywhere it appears.
2. **Confirm the `A Mod Loop Mode` / `A Amp Loop Mode` 0–3 ordering** (AD Loop placeholder = 2, Loop = 1).
3. **Confirm Osc Type indices** map to the dossier §1.2 table at the live device (they should — same DSP ref).
4. **Set the Live Set's Scale** (e.g. C Minor) before rendering `meld-swarm-scale-snap` and the Two-Hands steps.
5. **Hand-build the matrix routes** for the 5 matrix-dependent demos (and MPE for the 4 MPE demos) to pass Gate 7;
   the fallbacks in the manifest are audible stand-ins only.
