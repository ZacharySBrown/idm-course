# Algorithm — step sequencer with per-step parameter override

The Elektron data model, simplified:

```
Pattern[step] = {
  trig: bool,                    // note on/off for this step
  note: int,                     // pitch (for melodic tracks)
  velocity: int,                 // 1–127
  plocks: {param_id → value}     // per-step parameter override dict
}
```

At playback, for each step the sequencer emits the trig + note, and for every plock entry it writes the locked value to the parameter bus **before** the voice is retriggered. When the step passes, the parameter bus reverts to the kit's base value.

Three properties that matter:

1. **Deterministic.** Same pattern, same run, same output. No seed required.
2. **Independently modulatable.** Because plocks are per-step, a parameter can have 16 different values across a 16-step pattern — the "16 snares" effect.
3. **Per-track length.** Each of the 6 tracks can have its own length (1–64 steps). Polymeter falls out for free.

This is a **UI-level generative** system. The "procedural not random" constraint lives at the hardware level: there is literally no random-trigger parameter on the front panel.

`bib:elektron_machinedrum_manual`
