# Patch tutorial — `op-mod-index-sweep`

**Preset:** `presets/op-mod-index-sweep.adv`  ·  **Concept:** Modulation index → brightness (the "Bessel bloom")  ·  **Used in slide:** `03b-bessel`

> Carrier (sine A) + modulator (sine B) at a 1:1 ratio. B's own amplitude envelope has a
> LONG attack, so the modulation index — and therefore the brightness — sweeps up over the
> held note with no live automation. The render is deterministic.
>
> **You should hear:** one held pitch, constant in pitch and loudness, opening from a pure
> sine into a bright brass-like buzz as the modulator fades in — partials *blooming* outward.

Build from a **freshly loaded Operator** (init). One parameter per step; the right column is
your self-check. Teaching order: Algorithm → Osc A (carrier) → Osc B (modulator) → C/D off.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Operator | init | A single pure sine on each note |
| 1 | Global | Algorithm | Alg. 1 (linear stack D→C→B→A) | No change yet — routing only |
| 2 | Osc A | On | On | Still the default sine |
| 3 | Osc A | Wave | Sine | Pure sine carrier |
| 4 | Osc A | Coarse | 1 | Pitch sits at the played note (C3) |
| 5 | Osc A | Fine | 0 | No detune |
| 6 | Osc A | Level | 1.0 (0 dB, full) | Carrier at full level |
| 7 | Osc A | Feedback | 0 | Clean sine, no grit |
| 8 | Osc A | Env Mode | None | Standard ADSR (sustains while held) |
| 9 | Osc A | Env Attack | 0.0 norm (≈ instant) | Instant onset |
| 10 | Osc A | Env Decay | 1.0 norm (long) | — (sustain holds it up anyway) |
| 11 | Osc A | Env Sustain | 1.0 (0 dB, full) | Carrier holds steady for the whole note |
| 12 | Osc A | Env Release | 0.30 norm (≈ 200 ms) | Short tail after note-off |
| 13 | Osc B | On | On | A faint upper edge begins to creep in |
| 14 | Osc B | Wave | Sine | Modulator is a sine (cleanest sidebands) |
| 15 | Osc B | Coarse | 1 | **1:1 ratio** — sidebands land on the harmonic series (pitched, not bell) |
| 16 | Osc B | Fine | 0 | No detune on the modulator |
| 17 | Osc B | Level | 0.95 (≈ 95%, near max index) | This is the *ceiling* of the sweep, not the level you hear instantly |
| 18 | Osc B | Feedback | 0 | No self-modulation |
| 19 | Osc B | Env Mode | None | Standard ADSR drives the index |
| 20 | Osc B | Env Attack | 0.85 norm (≈ 3.2 s LONG) | **The sweep** — index ramps 0→max over the held note; sine → bright buzz |
| 21 | Osc B | Env Decay | 1.0 norm (long) | — (sustain holds full index) |
| 22 | Osc B | Env Sustain | 1.0 (full) | Full brightness once the attack completes |
| 23 | Osc B | Env Release | 0.30 norm (≈ 200 ms) | Brightness fades with the note tail |
| 24 | Osc C | On | Off | (unused) |
| 25 | Osc D | On | Off | (unused) |

**Final check:** hold one C3 for ~4 s. Pitch and loudness stay put; the timbre opens from a
pure sine into a brass-like buzz. Spectrum: a lone fundamental sprouting symmetric sidebands
that grow with B's rising envelope (the Bessel bloom; listen for the carrier null mid-sweep).

**Verification (Gate 7):** `index-sweep` — RMS flat ±2 dB across the clip AND spectral
centroid rises monotonically start→end. Flat centroid ⇒ the modulator envelope didn't sweep ⇒ reject.

_To persist: in Live, right-click the Operator title bar → **Save Preset** → save as
`op-mod-index-sweep` into the episode's `presets/` folder._
