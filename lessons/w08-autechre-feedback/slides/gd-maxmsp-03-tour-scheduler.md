# Tour continued — the scheduler and signal vectors

Two clocks run inside a Max patch.

**The scheduler clock.** Drives Max (non-tilde) objects. Resolution is typically 1 ms; configurable via "Overdrive" and "Scheduler in Audio Interrupt" toggles in the options pane. A `metro 250` object emits bangs every 250 ms. Control-rate data is ms-accurate, not sample-accurate.

**The signal vector.** Drives MSP (tilde) objects. The DSP engine processes audio in fixed-size chunks — default **64 samples** at 44.1 kHz = about 1.45 ms per vector. Signal Vector Size and I/O Vector Size in DSP options determine latency vs CPU tradeoff. Smaller vector = lower latency, higher CPU.

**gen~** collapses the signal-vector distinction for audio DSP. Inside a `gen~` patcher, every operation is sample-accurate — you write one-sample-at-a-time code (via the `codebox` object) and Max compiles it into an efficient DSP chain at load.

For Autechre-grade micro-timing drums, the Max scheduler is not precise enough — you want `gen~` or `phasor~`-driven triggering for sample-accurate hits. This is why the Max patches you see in WATMM screenshots have a lot of tildes on the audio path.

`bib:cycling74_max_msp_docs`
