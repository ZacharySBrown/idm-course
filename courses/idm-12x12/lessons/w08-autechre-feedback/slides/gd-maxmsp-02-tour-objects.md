# Tour — the five object families

Max patches look chaotic until you recognize the types.

- **UI objects** — `number`, `int`, `flonum`, `toggle`, `button`, `message`, `slider`, `dial`. These are the inlets and outlets a human touches.
- **Max (control-rate) objects** — `metro`, `counter`, `select`, `gate`, `route`, `pack`/`unpack`, `trigger`. These run at the scheduler rate (ms precision). MIDI lives here.
- **MSP (signal-rate) objects** — `cycle~`, `phasor~`, `noise~`, `gate~`, `*~`, `+~`. The tilde suffix means "audio-rate." These run at the sample rate (44.1 kHz / 48 kHz).
- **Jitter (matrix) objects** — `jit.matrix`, `jit.noise`, `jit.op`. Video and multi-dimensional arrays.
- **Abstractions / patchers** — `patcher`, `bpatcher`, `poly~`. User-defined subpatches. A big Autechre patch is 99% abstractions.

The visual grammar: **thin black cords = Max messages, red/yellow striped cords = signal-rate audio, green cords = MIDI.** Cords travel top-to-bottom, left-to-right.

`bib:cycling74_max_msp_docs`
