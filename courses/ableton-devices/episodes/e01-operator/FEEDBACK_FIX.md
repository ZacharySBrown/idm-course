# op-feedback-bifurcation — diagnostic (NEEDS HANDS-ON LIVE VERIFICATION)

**Status: unresolved headlessly. Shipped ep1 is unchanged (this demo was left as-is).**

## The concept
"Feedback → progressive harmonic complexity": one Operator oscillator's self-feedback
should morph sine → saw → broadband noise as the feedback amount rises.

## What was tried this session (2026-06-29) and the MEASURED result
Both candidate headless recipes were rendered through the AbletonOSC path and the
spectral centroid / high-band energy were measured on the actual renders:

1. **Lone-carrier self-feedback** (Osc-A as sole carrier, `Osc-A Feedb` set 0→100 across
   a 5-rung ladder, held C2). Result: **all 5 rungs are pure sine** — centroid ≈ 133 Hz
   (the C2 fundamental), **0.0% energy above 2 kHz at every rung, including Feedb=100.**
   The values were NOT clamped (`Osc-A Feedb` range is 0–100). Feedback had zero effect.

2. **Modulator self-feedback** (Alg. 1, B→A, `Osc-B Level` fixed = 0.4 as a constant FM
   index, `Osc-B Feedb` swept 0→100). Result: **still essentially sine** — centroid
   149→156 Hz, 0.0% > 2 kHz. Notably the *baseline FM* (B modulating A at all) barely
   produced sidebands either, so B was hardly modulating A in this configuration.

## Conclusion
The Operator **feedback parameter does not take audible effect when set over AbletonOSC**
in any configuration drivable headlessly here (carrier or modulator). This matches the
original handoff's warning ("static Feedb ≈ pure sine, centroid 360 Hz"). The earlier
agent's claim that lone-carrier feedback is the clean demonstration was based on the
in-repo digest only (external sources were blocked) and is **contradicted by the render
measurements above.**

## Recommended next step (requires the user at the machine)
Verify by EAR in Live which feedback configuration actually buzzes:
- Load Operator, single carrier A, turn the **Feedback** knob up by hand — does a lone
  carrier audibly saw? If yes, the issue is the OSC param write (wrong index/path or a
  value-scaling quirk); re-probe `Osc-A Feedb` with `/live/device/get/parameter/value`
  after setting it to confirm Live actually stored it.
- If a lone carrier does NOT buzz, route a modulator into A and raise the *modulator's*
  feedback by hand until the FM tone gains grit; capture those exact settings.
Once a configuration is ear-confirmed, encode it as the 5-rung concat ladder (the
structure is right — discrete static rungs, since envelopes can't sweep feedback) and
re-render. Until then, ep1 keeps its original (weak but audible) feedback demo.
