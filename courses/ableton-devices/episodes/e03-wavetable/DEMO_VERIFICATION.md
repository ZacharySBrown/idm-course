# e03 Wavetable — Demo Verification (param-map reconciliation, 2026-06-29)

Reconciled `device_demos` (20 demos, `wt-*`) against the authoritative
`tools/device_render/param_maps/wavetable.json` (93 real LOM params). Every
`params:`/`automation:` key now matches a verbatim map name; every numeric value
is clamped into the param's real range. Quantized params take the numeric INDEX
(the dump returned empty `value_items`, so we set indices, not UI strings).

## What the renderer actually consumes

`device_render.py` → `midi_instrument_render.js` consume ONLY `params`,
`automation`, `midi` (and `mix_from`). It does **not** read `ab_param`,
`ab_values`, `ab_params`, `matrix`, `macros`, or `concat_from` — those are the
orchestrator's A/B + concat-render metadata (it re-renders with the B value /
concatenates). The `matrix:`/`macros:` blocks are retained on each demo purely as
the **patch intent** (for the preset + tutorial); they do not render.

## Hard LOM limitations (NOT in the 93-param map → cannot be set headless)

These drove most of the redesign. Each is flagged inline on every affected demo:

| Limitation | Consequence | Mitigation used |
|---|---|---|
| **Wavetable table/category** not exposed | Can't pick Basic Shapes / Formants / Harmonics / Distortion / user-import over LOM | Orchestrator pre-loads the needed table once; `Osc 1 Pos` still scans whatever table is up. Flagged per demo. |
| **Osc Effect Mode** (None/FM/Classic/Modern) not a settable enum | Can't switch to FM/Modern headless | Orchestrator pre-sets the effect mode in the device; then `Osc 1 Effect 1/2` (which ARE settable) drive Amount/Fold. |
| **Hi-Q / oversampling** toggle not exposed | The PPG-vs-Serum aliasing A/Bs can't toggle Hi-Q | `wt-zipper-vs-smooth` & `wt-hiq-on-vs-off` flagged CANNOT-RENDER (hand render or cut). `wt-hiq-off-grit` works because Hi-Q DEFAULTS OFF — leaving it at default IS the grit. |
| **Mod matrix** (LFO/Env/Pressure → Pos/Effect/Filter) not addressable | Can't create any routing | Render the IDENTICAL audible motion by AUTOMATING the destination param directly (`Osc 1 Pos`, `Osc 1 Effect 1`, `Flt 1 Freq`). |
| **Unison Mode/Voices** (incl. Position Spread) not exposed; only `Unison Amount` | Can't create the "chord of timbres" headless | `wt-position-spread-chord` renders a detune-width A/B on `Unison Amount`; orchestrator pre-sets Position Spread for B to read as timbres. Flagged. |
| **Macros / Voices / Mono / MPE Pressure** not exposed | Macro pad→growl, MPE per-note, mono-glide not settable | Macro & MPE moves rendered as direct destination automation (`Osc 1 Pos`, `Flt 1 Freq`). MPE per-voice independence is NOT proven headless (flagged). |

## Key name corrections applied everywhere

`Osc 1 Wave Position`→`Osc 1 Pos` (range **0–1**, not 0–100) · `Osc 1 Transpose`→
`Osc 1 Transp` · `Osc 1 Gain` is **0–1** (1.0=unity; the old `0.0 dB` would have
rendered SILENT) · `Osc 1 Detune` **0.5**=0 cents · `Filter 1 *`→`Flt 1 *` ·
`Filter 1 Circuit: <name>`→`Flt 1 Type: <index>` (0=Clean 1=OSR 2=MS2 3=SMP 4=PRD)
· `Env 1 *`(Amp)→`Amp *` · `Env 2 Mode`→`Env 2 Loop Mode` (0=None 1=Trigger 2=Loop)
· `Sub Transpose` quantized **0/1/2** (not −12) · removed `Effect Mode`,
`Filter Routing`, `Hi-Q`, `Wavetable Category/Table`, `Unison Mode/Voices`,
`MPE Enable`, `Macro 1` (all not in map).

## Per-demo table

| id | concept | param-names OK? | isolates ONE var? | reference | key changes | confidence | LOM limitation |
|---|---|---|---|---|---|---|---|
| `wt-position-by-hand` | Position → timbre, pitch held | ✅ all verbatim | ✅ `Osc 1 Pos` 0→1 sweep | §5.6 demo 1 (THE key demo) | Pos 0–1; Gain 1.0 (was silent); Flt names; Amp env | **High** — renders clean | table=default Basic Shapes (pre-load) |
| `wt-ab-two-positions` | a wavetable = a set of spectra | ✅ | ✅ `Osc 1 Pos` A=0.1 B=0.85 | §5.1 | ab_values→0–1; Gain fix | **High** | table pre-load |
| `wt-zipper-vs-smooth` | frame interpolation (zipper vs smooth) | ✅ | ⚠ var not settable | §5.3 | renders smooth ref only | **Low — CANNOT render concept** | Hi-Q not exposed → hand render or cut |
| `wt-hiq-on-vs-off` | Hi-Q → aliasing removed (PPG vs Serum) | ✅ | ⚠ var not settable | §5.4, §5.6 demo 6 | renders one fast sweep | **Low — CANNOT render concept** | Hi-Q not exposed → hand render both segs |
| `wt-fm-inside-wavetable` | hidden FM osc (Ep1 bridge) | ✅ | ✅ `Osc 1 Effect 1` 0→0.85 | §5.6 demo 5, §1.1 | Effect-mode pre-set; Pos fixed 0.3 | **Med-High** (needs FM mode pre-set) | Effect Mode not settable (pre-set FM) |
| `wt-modern-fold-sweep` | Modern→Fold wavefold | ✅ | ✅ `Osc 1 Effect 2` 0→0.9 | §1.1, §5.6 demo 5 | Effect-mode pre-set; Pos fixed | **Med-High** | Effect Mode not settable (pre-set Modern) |
| `wt-lfo-to-position` | LFO→Position wobble, no pitch change | ✅ | ✅ `Osc 1 Pos` triangle steps ~1/8 | §5.6 demo 3, §5.5 | matrix→direct Pos automation | **High** (audible result identical) | matrix routing not creatable |
| `wt-lfo-attack-bloom` | LFO Attack fade-in → late bloom | ✅ | ✅ `Osc 1 Pos` flat→growing wobble | §1.6, §5.6 demo 4 | matrix→direct Pos automation | **High** | matrix routing not creatable |
| `wt-position-spread-chord` | Position Spread = chord of timbres | ✅ | ⚠ partial (`Unison Amount` only) | §1.7 | ab on `Unison Amount` 0/0.3 | **Med — proves width, not the spread mode** | Unison Mode/Voices not settable (pre-set) |
| `wt-spectra-step1` | walkthrough 1/7 — static vowel pad | ✅ | ✅ baseline patch | §4 Era 1, §6 | Amp env; Gain fix | **High** (sound), table pre-load | Formants table not settable (pre-load) |
| `wt-spectra-step2` | walkthrough 2/7 — slow LFO→Pos bloom | ✅ | ✅ added Pos drift | §6 step 2 | matrix→direct Pos automation | **High** | matrix routing not creatable |
| `wt-spectra-step3` | walkthrough 3/7 — spread + OSR | ✅ | ⚠ OSR + `Unison Amount` render; spread mode pre-set | §6 step 3, §1.7 | Flt Type=1; Unison Amount | **Med** | Unison Mode not settable (pre-set) |
| `wt-spectra-step4` | walkthrough 4/7 — Sub + Osc 2 bell | ✅ | ✅ Sub + Osc 2 added | §3 DM bell, §6 step 4 | Sub/Osc2 0–1 gains; Sub Transp idx 0 | **Med** (Sub Transp & bell table by ear) | Osc 2 bell table not settable; Sub Transp quantized |
| `wt-spectra-step5` | walkthrough 5/7 — arm growl (FM, LFO2, Env2) | ✅ | ⚠ FM edge + Env2 render; routings armed-only | §6 step 5 | Effect 1=0.2; Env 2 shape | **Med** | Effect Mode + LFO2/Env2 routings not settable |
| `wt-spectra-macro-sweep` | walkthrough 6/7 — ONE macro pad→growl (payoff) | ✅ | ✅ direct `Osc 1 Pos`+`Flt 1 Freq` automation | §6 step 6, §5.5 | macro→direct dual automation | **High** (payoff renders) | Macros/matrix not settable |
| `wt-spectra-morph-final` | walkthrough 7/7 — saved patch demo | ✅ | n/a (whole instrument) | §6 step 7 | macro→direct Pos+Flt automation | **High** | Macros/matrix not settable |
| `wt-user-table-scan` | import + scan your own source | ✅ | ✅ `Osc 1 Pos` 0→1 slow ramp | §4 06a (Plaid), §6 | Env→direct Pos automation | **Med** (scan renders; needs WAV pre-dragged) | user-table import + Env routing not LOM ops |
| `wt-loop-env-sequence` | loop env → Position = self-sequencer | ✅ | ✅ `Osc 1 Pos` repeating 1/8 steps | §1.5, §6 06b | loop-env→stepped Pos automation; Flt Type=2 | **High** (rhythm renders) | Env→Pos routing + Loop-mode-to-Pos not settable |
| `wt-hiq-off-grit` | aliasing on purpose (Hamburg grit) | ✅ | ✅ Fold + fast sweep, Hi-Q default off | §5.4, §4 06c | Effect 2 Fold; Flt Drive name; Pos 0–1 | **Med-High** (Hi-Q default off = grit) | Hi-Q not settable but DEFAULTS OFF; table pre-load |
| `wt-mpe-pressure-position` | MPE Pressure → per-note Position | ✅ | ⚠ per-note Pos steps (not true MPE) | §5.5, §6 06d | MPE→stepped Pos automation | **Med — proves brightness ladder, not MPE independence** | MPE/Pressure/matrix not settable |

Legend: ✅ renders & demonstrates · ⚠ renders but with a caveat/limitation · the
two **Low** rows cannot demonstrate their concept headless at all.

## Summary

- **Demos changed:** 20 / 20 (every demo had wrong param names, wrong Position
  scale 0–100 vs 0–1, and a silent `Osc 1 Gain: 0.0 dB` that is actually 0.0 on a
  0–1 scale = silence; all corrected).
- **Demos with ALL param/automation names verified verbatim in the map:** **20 / 20**
  (validated programmatically; all numeric values in range; quantized params use
  valid integer indices).
- **Cannot render their concept cleanly headless (2):** `wt-zipper-vs-smooth` and
  `wt-hiq-on-vs-off` — both hinge on the **Hi-Q toggle**, which is not LOM-exposed
  and has no settable proxy. Recommendation: hand-render the two segments (flip
  Hi-Q in the device between takes) or fold the point into narration. Both now
  render a single valid reference segment so the build doesn't break.
- **Render-with-a-pre-set-required (orchestrator must do one manual setup):**
  FM/Modern demos (`wt-fm-inside-wavetable`, `wt-modern-fold-sweep`,
  `wt-spectra-step5/6/7`, `wt-loop-env-sequence`) need the device's **Effect Mode**
  pre-set (FM or Modern). Formants/Harmonics/Distortion/user-import demos need the
  **table pre-loaded**. Position-Spread demos need **Unison = Position Spread**
  pre-set. These are device-state setups outside LOM, not manifest bugs.
- **Concept rendered via direct destination automation** (matrix not LOM-creatable
  but the audible/spectral result is identical): all LFO→Pos, Env→Pos, loop-env→Pos,
  macro→Pos+Filter, MPE→Pos demos. These pass their Gate-7 spectral assertions
  (periodic / monotonic / late-blooming centroid motion) because the destination
  param itself moves exactly as the routing would have moved it.
- **Reduced-fidelity (renders, but does not prove the FULL concept):**
  `wt-position-spread-chord` (proves width, not per-voice position spread) and
  `wt-mpe-pressure-position` (proves a brightness ladder, not MPE per-voice
  independence). Note on-mic accordingly or supplement with a hand demo.
