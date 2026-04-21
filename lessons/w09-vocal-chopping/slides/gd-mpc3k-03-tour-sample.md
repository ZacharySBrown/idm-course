# Annotated tour, 2/2 — sample edit and signal path

The sample-edit page is where the chop happens:

- **Truncate** — crop head and tail. Destructive on the sample in RAM.
- **Loop points** — set start/end loop in frames. Used for the sustained-vowel chipmunk-soul moves, not for the Dilla micro-chop.
- **Pitch (tune)** — semitone + fine cents, implemented as <term key="varispeed">varispeed</term>. Raising pitch shortens the sample; lowering lengthens it. Pitch and time are *coupled*. This is not a bug. This is the reason every Dilla chop sounds like Dilla.
- **Filter** — 2-pole low-pass per voice. The "<term key="mpc_lpf">MPC low-pass</term>" character on Slum Village records came from here, not from an outboard box (`bib:akai_mpc3000_manual`).

Signal path: pad trigger → sample RAM → varispeed pitch → envelope → LPF → assigned output → DAC → mix out. The DAC is a Burr-Brown PCM61P-K, 18-bit. The summing bus is where the MPC3000 gets its "weight" — a topic producers argue about and Akai never marketed.
