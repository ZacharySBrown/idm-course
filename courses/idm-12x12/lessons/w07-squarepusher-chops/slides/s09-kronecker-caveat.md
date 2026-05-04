# Kronecker King — the 1–2ms snare

On *Hello Everything* (2006), the "Kronecker King" snare is reportedly a Kronecker-delta impulse: a snare sample trimmed to a **1–2 ms transient-only envelope**, so only the attack survives. The rest is synthesis built around that impulse.

Caveat, inline: the 1–2 ms figure is KVR and Jenkinson-site community consensus, not a direct Tape Op quote. The general technique — transient-only envelope, synthesize the body — is confirmed by Jenkinson's broader *Go Plastic*-onward move to drums *"synthesized inside Reaktor"* rather than sampled. Flagged in `needs_bib:`.

## Ableton translation

1. Load a snare into **Simpler** (One-Shot mode).
2. Set **Fade** → 1 ms, **Length** → 2 ms. Only the click survives.
3. On the same rack chain, drop a **Meld** or **Operator** instance tuned to the same pitch. Trigger them from the same MIDI note.
4. The click is the transient. The synth is the body. The "snare" is a two-device sandwich. <Citation bib="ableton_live_12_manual" />

Why it matters: once you start synthesizing the body, the drum stops being a sample and starts being a voice. The transient stays real; everything else is yours.
