# Texture — grain cloud, Flux = stochastic offset

<term key="texture_warp">Texture mode</term> is <term key="granular_synthesis">granular synthesis</term> with two creative controls.

- **Grain Size** — the length of each individual <term key="grain">grain</term> in milliseconds. 50 ms = smooth blended clouds; 10 ms = chatter that reveals pitch of the grain boundary rather than pitch of the source.
- **Flux** — the allowed randomness of the grain's sampling position within the source. Flux 0 = strictly sequential, pseudo-Complex-Pro behaviour. Flux 60 = grains drift a windowed amount. Flux 100 = the grain is allowed to wander, and the clip never repeats the same way twice.

The diagram shows three flux settings for the same four grid positions. Flux 0 locks to the dashed markers; Flux 100 scatters anywhere in the source.

Practical: Texture is what turns a drone into a pad bed; it is also what turns a drum loop into a noise wash when you dial Flux up. The cost: because Flux is stochastic, the print is different every time. Bounce the output, not the source.

Cite: `bib:ableton_live_12_manual`. Granular theory: `bib:roads_computer_music_tutorial`.
