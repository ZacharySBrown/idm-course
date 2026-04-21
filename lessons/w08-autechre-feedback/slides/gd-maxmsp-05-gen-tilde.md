# Technique continued — gen~ for audio-rate DSP

Plain MSP objects are fine for LFOs and mixers; for **custom oscillators, filter algorithms, and waveshapers** you want `gen~`.

gen~ exposes a sample-accurate language (GenExpr, or a node-based patcher) that compiles to optimized DSP. Key idioms:

- **`history`** — a one-sample delay. Lets you write feedback equations. `y = x + history(y) * 0.5` is a single-pole IIR filter.
- **`codebox`** — write GenExpr code inline. For-loops, conditionals, sample-accurate state.
- **`data` / `buffer`** — read/write buffers at audio rate.
- **Chaotic attractors** — a Lorenz or Rössler system is four lines of codebox. Output the X/Y/Z channels at audio rate; resample down for modulation.

The Autechre move is to use gen~ patches as **self-contained instruments**: a whole drum synth lives in one gen~ box. Inputs are trigger, pitch, decay. Outputs are left/right audio. The patch above — five Max-rate objects + one gen~ drum synth — is a credible Untilted-era skeleton.

`bib:cycling74_max_msp_docs`
