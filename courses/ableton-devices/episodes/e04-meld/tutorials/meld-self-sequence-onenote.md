# Patch: Self-Sequence One Note (the Autechre Move)  (preset: presets/meld-self-sequence-onenote.adv)

**Demo:** `meld-self-sequence-onenote`  ·  **Slide:** `06a-self-sequencing`  ·  **Structure:** single
**Concept demonstrated:** modulate the timbre instead of writing the notes — a looping Mod Env + an audio-rate LFO turn ONE held note into a pattern.

> ## ⚠ THIS DEMO IS BUILT BY HAND — IT CANNOT BE RENDERED OVER OUR HEADLESS PATH.
> BOTH the self-sequence (`A Mod Env → A Osc Shape`) and the audio-rate grit (`A LFO 1 → A Filter
> Freq`) are **modulation-matrix routes**, **not in Meld's LOM param map**. The manifest's
> single-ramp `automation:` FALLBACK is audible but not recurring — it will NOT pass the
> `self-sequence` assertion. **Hand-build both routes in the live device** to prove the recurrence.

**⚠ PLACEHOLDER ENUM INDEX — CONFIRM LIVE:** `A Mod Loop Mode` AD Loop = **2** (quantized 0–3, EMPTY value_items).

Build from a **freshly loaded default Meld**. One parameter per step.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine B | `B On` | Off (0) | Engine B silent |
| 2 | Engine A | `A On` | On (1) | Engine A only |
| 3 | Engine A | `A Osc Type` | **0 = Basic Shapes** | A clean shape — the macro target |
| 4 | Engine A | `A Osc Shape` (macro 1) | 0.40 (center the AD-Loop sweeps) | A mid-bright shape — the loop's center |
| 5 | Engine A | `A Osc Tone` (macro 2) | 0.50 | A neutral tone |
| 6 | Engine A | `A Filter On` | On (1) | (routing) |
| 7 | Engine A | `A Filter Type` | **0 = Analog** | Transparent filter |
| 8 | Engine A | `A Filter L-B-H-N` | 0.0 (lowpass) | Lowpass response |
| 9 | Engine A | `A Filter Freq` | 0.60 (modulated by the audio-rate LFO via matrix) | A half-open tone — the LFO target |
| 10 | Engine A | `A Filter Q` | 0.20 | A touch of resonant edge |
| 11 | Engine A (Mod Env) | `A Mod Loop Mode` | **2 = AD Loop (PLACEHOLDER — CONFIRM)** | The Mod Env cycles (no audible change yet — needs the route) |
| 12 | Engine A (Mod Env) | `A Mod Attack` | 0.10 | (rise of each loop cycle) |
| 13 | Engine A (Mod Env) | `A Mod Decay` | 0.35 (sets the self-sequence period) | (the pattern's tempo) |
| 14 | Engine A (LFO 1) | `A LFO 1 Type` | **0 = first waveform (sine-ish)** | (the grit source's shape) |
| 15 | Engine A (LFO 1) | `A LFO 1 Rate` | **1.0** (NORMALIZED 0–1; 1.0 = top ≈ 200 Hz, AUDIO-RATE — NOT 200) | (audio-rate; adds sidebands once routed to the filter) |
| 16 | Engine A | `A Amp Attack` | 0.05 | Fast note start |
| 17 | Engine A | `A Amp Sustain` | 1.0 | Holds at full level |
| 18 | Engine A | `A Amp Release` | 0.30 | Short tail |
| 19 | Engine A | `A Volume` | 0.70 | Solid level |

### HAND-BUILD: the matrix routes (this is what makes the demo work)
In the live device's **Matrix** tab, add TWO routes:

| Source | Destination | Amount | Note |
|---|---|---|---|
| `A Mod Env` | `A Osc Shape` (macro 1) | **+0.8** | the AD-Loop self-sequence (the pattern) |
| `A LFO 1` | `A Filter Freq` (cutoff) | **+0.5** | audio-rate → sideband grit |

From a single sustained key: a recurring rhythmic/timbral pattern, with a grainy sideband edge — no new note onsets.

**Play:** one held note `C3` for ~7.6 s — do not play another note.

**Final check:** from a single sustained key, a recurring rhythmic/timbral pattern with a grainy sideband edge; no new note onsets.
**Analyzer:** onset/timbre events recur on a steady grid from one held note; audio-rate LFO adds sidebands.

**Save:** with both routes built, right-click Meld → **Save Preset** → `presets/meld-self-sequence-onenote.adv`.
