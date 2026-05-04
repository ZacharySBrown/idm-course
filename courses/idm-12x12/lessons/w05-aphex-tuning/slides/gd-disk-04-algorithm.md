# The algorithm — velocity-to-solenoid and why the click is velocity-dependent

The Disklavier's velocity curve is the model. <Citation bib="wikipedia_disklavier" />

MIDI velocity V arriving at the piano:
1. Lookup: solenoid drive current I = f(V) where f is a calibrated curve — nonlinear, approximating a trained pianist's force-to-velocity map. Typical: V=1 produces ~0.3A pull, V=127 produces ~1.1A pull.
2. Solenoid pulls for a duration T = g(V) — shorter at high velocity (faster strike), longer at low velocity (slower, more controlled).
3. The plunger accelerates toward the key. Mechanical impact: two audible events — the key-bottoming (soft thump) and the solenoid seating at end-of-travel (metallic click). Higher velocity = louder click *and* louder string.
4. The hammer, driven by the key, strikes the string. The string vibrates as a **Helmholtz resonator** — fundamental f = (1/2L)√(T/μ), where L is string length, T is tension, μ is linear density. <Citation bib="roads_computer_music_tutorial" />
5. The soundboard radiates the string vibration. The body cavity resonates at ~60–80 Hz regardless of which note is played — a body resonance that adds a low-end "woof" to every note.

The click and the string are **independent signals that share a cause**. Velocity controls both, but mic placement controls their relative level. Under-lid miking flips the ratio. Body-cavity miking captures the ~70 Hz thud separately from either.

Three layers from one MIDI note. That is the mechanical receipt for why Drukqs sounds three-dimensional.
