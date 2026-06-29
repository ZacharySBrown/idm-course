# Patch: MPE Per-Note (Two Fingers, Two Timbres)  (preset: presets/meld-mpe-per-note.adv)

**Demo:** `meld-mpe-per-note`  ·  **Slide:** `04c-mpe-hands-on`  ·  **Structure:** ab (the still note vs the expressed note, sounding together)
**Concept demonstrated:** the matrix runs PER VOICE over MPE — two simultaneously-held notes morph independently under two fingers. This is where the control went.

> ## ⚠ THIS DEMO IS PLAYED BY HAND ON AN MPE CONTROLLER — IT CANNOT BE RENDERED OVER OUR HEADLESS PATH.
> TWO blockers: (1) per-note MPE expression (per-note channels, Press / Slide curves) is **not
> authorable** over our MIDI-clip render path; (2) the Press/Slide → macro routes live in the
> **modulation matrix**, which is **not in Meld's LOM param map**. A static two-note render makes
> sound but proves NOTHING about per-voice morphing — do NOT ship it as the demo. Perform this on an
> **MPE controller** (Push 3 in MPE mode / ROLI Seaboard / LinnStrument). For listeners without MPE,
> the channel-aftertouch fallback (one note expressed globally) still sounds but loses the per-finger
> independence.

Build from a **freshly loaded default Meld**. One parameter per step.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine B | `B On` | Off (0) | Engine B silent |
| 2 | Engine A | `A On` | On (1) | Engine A only |
| 3 | Engine A | `A Osc Type` | **9 = Harmonic FM** | A metallic FM source |
| 4 | Engine A | `A Osc Shape` (macro 1 = FM Amount) | 0.30 (base — raised per-note by Press over MPE) | A modest FM brightness at rest |
| 5 | Engine A | `A Osc Tone` (macro 2 = FM Ratio) | 0.40 | A fixed FM ratio |
| 6 | Engine A | `A Transpose` | 0 | (no offset) |
| 7 | Engine A | `A Detune` | 0.50 (0 cents) | Centered tuning |
| 8 | Engine A | `A Filter On` | On (1) | (routing) |
| 9 | Engine A | `A Filter Type` | **0 = Analog** | Transparent filter |
| 10 | Engine A | `A Filter L-B-H-N` | 0.0 (lowpass) | Lowpass response |
| 11 | Engine A | `A Filter Freq` | 0.60 (base cutoff — raised per-note by Slide over MPE) | A half-open, slightly darkened tone at rest |
| 12 | Engine A | `A Filter Q` | 0.10 | A touch of resonant edge |
| 13 | Engine A | `A Amp Attack` | 0.05 | Fast note start |
| 14 | Engine A | `A Amp Sustain` | 1.0 | Holds at full level |
| 15 | Engine A | `A Amp Release` | 0.30 | Short tail |
| 16 | Engine A | `A Volume` | 0.70 | Solid level |

### HAND-BUILD: the per-note MPE matrix routes (this is the whole demo)
In the live device's **Matrix** tab, add these MPE-source routes:

| Source | Destination | Amount |
|---|---|---|
| `MPE Press` (per-note pressure) | `A Osc Shape` (macro 1 = FM Amount) | **+0.7** |
| `MPE Slide` (per-note Y / CC74) | `A Filter Freq` (cutoff) | **+0.6** |

*(Non-MPE fallback: route `Press` = channel aftertouch → `A Osc Shape` — global, NOT per-voice. Use only to demonstrate the gesture; it cannot prove the per-voice claim.)*

### THE MPE GESTURE TO PERFORM
Hold **two** notes together (e.g. `C3` + `G3`). Keep `C3` **still** (no press, no slide). On `G3`, **press harder and slide your finger up** over the ~5.5 s hold. Listen for the two notes pulling apart: only `G3` brightens and morphs; `C3` does not move.

**Final check:** two notes start identical in character; only the expressed note brightens/morphs over the hold while the still note does not.
**Analyzer (per-voice isolation):** the expressed voice's centroid rises over time; the still voice's stays flat.

**Save:** with the two MPE matrix routes built, right-click Meld → **Save Preset** → `presets/meld-mpe-per-note.adv`.
