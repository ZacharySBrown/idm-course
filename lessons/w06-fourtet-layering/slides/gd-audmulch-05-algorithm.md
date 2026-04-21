## Underlying algorithm — modular routing as instrument

AudioMulch's algorithmic identity is not any single DSP. It is the **patch graph** as the unit of composition.

- **Pull-based audio graph** — downstream nodes pull samples from upstream nodes at audio rate. Identical to Max/MSP's gen~ or PureData's DSP chain. `Roads 1996` on patch-based DSP graphs.
- **Metasurface interpolation** — all parameters of all modules can be keyframed into "scenes," and Metasurface interpolates linearly between scenes based on XY position. A primitive version of modern DAW macro-morphing.
- **Live recording** — the output bus is always-capturable, so any live gesture on the Metasurface while the graph is running becomes part of the take.

The paradigm is <term key="real_time_dsp">real-time processing with live parameter morph</term>, printed to tape. Closer to Jeskola Buzz or early Reaktor than to any DAW. Hebden's contribution was *not* innovating AudioMulch — it was using it as a pre-arrangement sample factory, not as a live performance tool.
