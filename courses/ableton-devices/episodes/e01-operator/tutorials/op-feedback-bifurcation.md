# Patch tutorial — `op-feedback-bifurcation`  ⚠️ BUILD/VERIFY BY EAR IN LIVE

**Preset:** `presets/op-feedback-bifurcation.adv`  ·  **Concept:** Feedback → progressive harmonic complexity (sine → saw → broadband)  ·  **Used in slide:** `03e-feedback`

> ⚠️ **KNOWN LIMITATION — headless renderer cannot prove this demo.** Setting `Osc-A Feedb`
> (or `Osc-B Feedb`) over our AbletonOSC path produces **no audible change** — every feedback
> rung renders as a near-pure sine (centroid ≈ the fundamental, ~0% energy > 2 kHz). See
> `FEEDBACK_FIX.md`. **This patch must be built and ear-verified in Live by hand**; do not
> trust a headless render of it. The shipped ep1 keeps its original (weak) feedback demo until
> a configuration is ear-confirmed and re-rendered as a static-rung ladder (envelopes cannot
> sweep feedback).

> **You should hear (target):** one held note, a pure sine progressively roughening — clean
> sine → softer asymmetric shape → triangle → sawtooth-like buzz → fracturing toward broadband
> noise — as feedback rises across four discrete steps (≈ 1.5 s each).

**Structure:** `sweep`, realised as a 4-rung **ladder** of static feedback values (envelopes
can't modulate Feedback). In Live, automate `Osc-A Feedb` in the clip, or render four concat
clips at the four levels.

Build from a **freshly loaded Operator** (init). One parameter per step.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack) | No change yet — routing only |
| 2 | Osc A | On | On | Default sine carrier |
| 3 | Osc A | Wave | Sine | Pure sine |
| 4 | Osc A | Coarse | 1 | Carrier at the played pitch (C3) |
| 5 | Osc A | Fine | 0 | No detune |
| 6 | Osc A | Level | 1.0 (0 dB) | Carrier full |
| 7 | Osc A | Env Mode | None | Sustains while held |
| 8 | Osc A | Env Attack / Decay / Sustain / Release | 0.0 / 1.0 / 1.0 / 0.30 | Held, steady sine |
| 9 | Osc B | On | Off | (single operator only) |
| 10 | Osc C | On | Off | (unused) |
| 11 | Osc D | On | Off | (unused) |
| 12 | Osc A | **Feedback** — rung 1 | **0** | Pure sine (reference) |
| 13 | Osc A | **Feedback** — rung 2 | **40** | Sine softens / leans asymmetric — first audible grit |
| 14 | Osc A | **Feedback** — rung 3 | **60** | Triangle→sawtooth character; clearly brighter and reedier |
| 15 | Osc A | **Feedback** — rung 4 | **70** | Sawtooth buzz fracturing toward broadband — the "tipping point" |

⚠️ **Ear-verify each rung in Live.** If a lone carrier does **not** audibly saw as you raise
the Feedback knob by hand, route a modulator into A instead and raise the *modulator's*
feedback until the FM tone gains grit; capture those exact settings and update this table +
the manifest. (Feedback only takes on the operator that is at the top of an algorithm branch,
i.e. not being modulated by another operator.)

**Final check (target):** four steps, each rougher than the last, ending in a broadband buzz —
the canonical FM source for hi-hats, breath, and snare attacks.

**Verification (Gate 7):** `feedback-sweep` — harmonic count / spectral spread increases with
feedback; the final rung approaches broadband. **Currently FAILS headlessly (see FEEDBACK_FIX.md).**

_To persist: build and ear-verify in Live, then right-click the Operator title bar →
**Save Preset** → save as `op-feedback-bifurcation` into the episode's `presets/` folder._
