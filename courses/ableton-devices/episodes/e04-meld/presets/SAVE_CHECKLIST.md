# e04-meld — Preset Save Checklist

Save one `.adv` per demo. In Live: build the patch from the matching
`tutorials/<id>.md` step-table, then **right-click the Meld device title bar → Save Preset…**
and write it to `episodes/e04-meld/presets/<id>.adv`. Commit the `.adv` files so each patch is
recallable with one drag.

**Source of truth = the patch step-table in each `tutorials/<id>.md`.** The `.adv` and the tutorial
must round-trip (`gzip -cd` the saved `.adv` and diff the XML against a re-save; any drift shows up
as a changed `<Manual Value>`).

19 presets total. Save the demonstrative state named in each tutorial's **Save** line (not the
A-segment-only base, where the demo's point is the B/ON state).

---

## ⚠ Confirm these LIVE before saving (they affect multiple presets)

- [ ] **`A/B Filter Type` Plate Resonator index** — PLACEHOLDER **15** everywhere. Read the live
      filter-type list (EMPTY value_items over LOM) and correct it in: `meld-plate-resonator`,
      `meld-twohands-step2`, `-step3`, `-step4`, `-step5`, `-step6`, `-final`.
- [ ] **`A/B Mod Loop Mode` 0–3 order** — AD Loop PLACEHOLDER **2**, Loop PLACEHOLDER **1**
      (EMPTY value_items). Confirm in: `meld-modenv-loop-macro`, `meld-self-sequence-onenote`,
      `meld-rain-crackle-sub` (Loop), and Two-Hands `-step4`/`-step5`/`-step6`/`-final` (AD Loop).
- [ ] **Osc Type indices** map to the dossier §1.2 table at the live device (set numeric — enum
      strings do not resolve over LOM).
- [ ] **Set the Live Set's Scale** (e.g. C Minor) before saving the scale-aware patches
      (`meld-swarm-scale-snap`, Two-Hands steps).

---

## GROUP A — Headless-renderable presets (8)
*Fully renderable over the param path; pass Gate 7 as written. No matrix, no MPE.*

- [ ] `presets/shepard-pi-cold-open.adv` — Shepard's Pi cold-open hook (Engine A only).
- [ ] `presets/meld-one-knob-three-worlds.adv` — save base state (Type 0, Osc Shape 0.0); ladder rendered as split.
- [ ] `presets/meld-type-switch-live.adv` — save segment A (Type 0 = Basic Shapes); A/B/C split render.
- [ ] `presets/meld-squelch-feedback.adv` — FM Bass (Squelch); save at Feedback = 0.0 (sweep start).
- [ ] `presets/meld-swarm-scale-snap.adv` — Swarm Sine; save with `A Osc Scale Aware` = ON (in-key state). *Set Scale first.*
- [ ] `presets/meld-twohands-step1.adv` — Two-Hands Step 1, Swarm Saw body. *Set Scale first.*
- [ ] `presets/meld-rain-crackle-sub.adv` — Rain + Sub; working direct-Rate fallback renders; save with the Loop matrix route built (tutorial version).
- [ ] `presets/meld-shepard-under-pad.adv` — Shepard build under a pad (Engine A + B, no matrix).

## GROUP B — Renderable but PLACEHOLDER filter index to confirm live (1)
*Renderable once the Plate Resonator index is confirmed; save the demonstrative (resonator-ON) state.*

- [ ] `presets/meld-plate-resonator.adv` — save with `A Filter Type` = **confirmed Plate Resonator index** (the B/ON state), Harmonic FM source.

## GROUP C — HAND-BUILD presets: modulation matrix required (4)
*The audible concept lives in a matrix route NOT exposed over LOM. Build the route(s) in the live
device BEFORE saving — the manifest fallback is an audible stand-in only and fails Gate 7. The
`.adv` preserves the matrix; the headless render cannot.*

- [ ] `presets/meld-modenv-loop-macro.adv` — route: `A Mod Env → A Osc Shape` (+0.85), AD-Loop. *Confirm Mod Loop Mode order.*
- [ ] `presets/meld-lfo-to-macro.adv` — route: `A LFO 1 → A Osc Shape` (+0.8, bipolar).
- [ ] `presets/meld-twohands-step3.adv` — route: `A LFO 1 → B Osc Shape` (+0.6, cross-engine). *Confirm Plate idx.*
- [ ] `presets/meld-twohands-step4.adv` — routes: `A LFO 1 → B Osc Shape` (+0.6); `A Mod Env → A Osc Shape` (+0.7). *Confirm Plate idx + Mod Loop order.*

*(Note: `meld-self-sequence-onenote` also needs hand-built matrix routes — listed in Group D because
it sits in the IDM act alongside the play-it-yourself moments; it is matrix-only, not MPE.)*

## GROUP D — HAND-BUILD presets: MPE play-it-yourself + matrix (5)
*Cannot render headless — needs per-note MPE expression (not authorable over our clip path) and/or
matrix routes. These presets exist so the patch is recallable for live performance on an MPE
controller (Push 3 / ROLI Seaboard / LinnStrument). Build the matrix in the device before saving.*

- [ ] `presets/meld-self-sequence-onenote.adv` — *(matrix-only, no MPE)* routes: `A Mod Env → A Osc Shape` (+0.8); `A LFO 1 → A Filter Freq` (+0.5, audio-rate, LFO Rate = 1.0). *Confirm Mod Loop order.*
- [ ] `presets/meld-mpe-per-note.adv` — MPE routes: `MPE Press → A Osc Shape` (+0.7); `MPE Slide → A Filter Freq` (+0.6).
- [ ] `presets/meld-twohands-step5.adv` — full matrix incl. MPE: `MPE Press → B Osc Shape` (+0.7); `MPE Slide → A Filter Freq` (+0.5); `MPE Note Bend → A Detune` (+0.3); + carried LFO/Mod-Env routes. *Confirm Plate idx + Mod Loop order.*
- [ ] `presets/meld-twohands-step6.adv` — global glue (Drive/Limiter/Voice Spread) IS renderable; matrix carried as hand-build. Save the full patch. *Confirm Plate idx + Mod Loop order.*
- [ ] `presets/meld-twohands-final.adv` — the complete **"Two-Hands"** capstone; full matrix incl. all MPE routes. Save as the user "Two-Hands" preset too. *Confirm Plate idx + Mod Loop order.*

---

## Round-trip verification (per preset, Gate 7 reproducibility)
After saving each `.adv`:
1. Load it fresh into a default Meld slot.
2. Walk its `tutorials/<id>.md` step-table from a default Meld → identical sound + analyzer image.
3. `gzip -cd presets/<id>.adv` and diff the XML against a clean re-save → no drift in `<Manual Value>`.

**Save total: 19** — Group A (8) + Group B (1) + Group C (4) + Group D (5).
Headless-renderable presets: **9** (Group A + the glue contrast in `meld-twohands-step6`, and Plate-pending Group B once confirmed).
Hand-build presets (matrix and/or MPE): **9** (Groups C + D, minus the renderable glue overlap).
