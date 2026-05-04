# The half-decibel threshold

Andrew Huang's claim — roughly: most listeners, under controlled A/B, cannot reliably identify a half-decibel level difference. Above one dB, they can. Below half a dB, it's a coin flip. <Citation bib="andrew_huang_sonic_boom" />

This is why <term key="lufs">LUFS</term> level-matching matters in the reference protocol. If your reference is 1.5 dB louder than your WIP, the louder track always wins the A/B — not because it's better, because it's louder.

The linter policy at the top of this lesson flags unconfirmed attributions. The half-dB claim is well-repeated in production YouTube; an exact peer-reviewed source is not in bibliography.json. Treat as a studio-rat heuristic, not a double-blind result.
