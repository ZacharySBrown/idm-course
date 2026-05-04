# Complex Pro — phase-vocoder block diagram

<term key="complex_pro_warp">Complex Pro</term> is a <term key="phase_vocoder">phase vocoder</term>. The chain:

1. Cut the signal into overlapping windows. <term key="hann_window">Hann window</term> is the textbook default, hop size typically a quarter of the window length — **Ableton does not publish Complex Pro's actual internals**, so treat these as the standard phase-vocoder recipe you'd find in Roads 1996, not as spec. What you actually hear as artifacts is **vertical phase coherence breakdown** (phasiness on polyphonic transients) and **transient smearing** — Complex Pro adds formant preservation and phase-locking heuristics not shown in this diagram.
2. <term key="fft">FFT</term> each window to get a complex spectrum.
3. Split into magnitude and phase. Keep magnitudes as-is, compute the phase *advance* per frame (how fast each bin's phase is rotating).
4. Re-propagate the phase at a new hop size — this is where time changes without pitch changing.
5. <term key="ifft">IFFT</term> back to the time domain.
6. <term key="overlap_add">Overlap-add</term> the windows at the new hop.

That is the entire mechanism. "Formants 100" adds an extra step that shifts the spectral envelope back to the source envelope after pitch shifting — which is how it keeps vowels stable when you transpose. "Envelope" is the window size in samples; it sets the time/frequency trade.

Cite: `bib:roads_computer_music_tutorial` (chapter on time-frequency processing); `bib:ableton_live_12_manual`.
