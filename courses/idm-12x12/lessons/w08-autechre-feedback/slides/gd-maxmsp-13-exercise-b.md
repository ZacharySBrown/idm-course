# Exercise B — gen~ Lorenz attractor as rhythm generator

The ancestor move. A Lorenz system is three coupled ODEs; its phase-space trajectory is a butterfly. Used as a modulator, it produces slow, non-repeating, fully-deterministic motion. This is the Navier-Stokes idea, simplified.

The equations:

```
dx/dt = σ(y − x)
dy/dt = x(ρ − z) − y
dz/dt = xy − βz
```

With σ=10, ρ=28, β=8/3, the system is chaotic but bounded.

Build as a Max for Live audio effect (or MIDI effect with `snapshot~`):

1. New M4L audio effect. Inside, make a `gen~` object.
2. Inside gen~, use a `codebox`:
   ```
   History x(1.0), y(1.0), z(1.0);
   sigma = 10; rho = 28; beta = 8/3;
   dt = 0.005;
   dx = sigma * (y - x);
   dy = x * (rho - z) - y;
   dz = x*y - beta*z;
   x += dx * dt;
   y += dy * dt;
   z += dz * dt;
   out1 = x / 20;  out2 = y / 30;  out3 = z / 40;
   ```
3. Outside gen~, `snapshot~ 20` samples the three outputs 50 Hz. Route to three `live.thisdevice` modulation outputs mapped to a filter cutoff, a drum rack macro, and a reverb size on the track.
4. As a **rhythm** source: compare z-axis to a threshold. When z crosses, emit a trigger. The crossing rate is irregular but fully deterministic.

**Deliverable.** A 64-bar rendered audio clip where the filter, macro, and reverb are all driven by the same Lorenz system. Render twice — outputs will be identical. Deterministic. Non-periodic. Ship it.

`bib:cycling74_max_msp_docs` · `bib:dillon_bastan_devices`
