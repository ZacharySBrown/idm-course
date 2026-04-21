# Algorithm continued — constraints and limits

The Machinedrum + Monomachine duo are not magic; they are constrained in very specific ways that shaped Autechre's live sound.

Hard limits:

- **Max 16 steps per pattern, 1/16 resolution.** For finer timing you either chain patterns or use the TRC (trig condition) feature on later OS versions. Micro-timing is per-step offset, not continuous.
- **Six voices per machine.** Drum kits are limited to 6 concurrent tracks; the Monomachine likewise 6. Stacking sounds means committing upstream or muting live.
- **No random operators in the sequencer.** Later OS versions added Trig Conditions (A:B, PRE, NEI, FILL) which are probabilistic — Autechre largely pre-date this on the rig they toured. Forum consensus: they used **Retrig** and length variation, not probability.
- **Mono audio per track.** Stereo is achieved via routing to the stereo master bus or external effects. Intra-track stereo imaging is limited.
- **No audio recording of the internal state.** You record the stereo output; the per-step plock values are not exported.

The constraint set is what makes the rig composable. Random would have broken the promise.

`bib:elektron_machinedrum_manual` · `bib:elektronauts_autechre_threads`
