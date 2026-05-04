# The IDM Production Handbook: Deep Research Compendium

This document compiles research across artist techniques, plugin-specific craft, DAW-specific (Ableton Live 12.3) workflows, sampling and drum programming, arrangement, pedagogy, and track-level breakdowns for a serious intermediate-to-advanced IDM production curriculum. Sources include verified producer interviews (Tape Op #89, Sound On Sound, Tape Notes #140, RBMA archives), published manuals, forum archives (WATMM, KVR, Gearspace, Elektronauts), and producer AMAs. Unverified/mythologized claims are flagged. The text prioritizes actionable specifics — gear models, parameter values, step sequences — over biography.

---

## 1. Artist technique profiles

### Aphex Twin (Richard D. James) — curation over complexity

Aphex Twin's working method is best understood as **gear-as-library curated into track-specific micro-rigs**. Rather than one mega-studio, he assembles small, temporary setups for each track — a "self-imposed constraint through gear curation." The Syro packaging made this explicit: every track title encodes its specific setup ("s950tx16wasr10" = Akai S950 + Yamaha TX16W + Ensoniq ASR-10; "CIRCLONT6A/14" = Sequentix Cirklon, the primary sequencer across Syro).

**Early-era foundations (SAW 85-92 → Polygon Window):** Per a 1993 *Future Music* interview, the London studio housed a **Roland TB-303, Yamaha DX7, an old Korg analog sequencer, Atari 520ST, DAT and CD decks**. James kept three **Korg MS-20s** stock ("the only keyboard I haven't changed"), but the **Roland SH-101 was heavily butchered** — "doesn't look like a 101 anymore." A **Casio FZ-10M** with custom filters handled ~80% of sampling. Drums came from a **Roland R-8 with an 808 expansion card**, enabling repitched 808 kicks that double as basslines on "Ageispolis" and "Xtal." Reverb was near-exclusively an **Alesis Quadraverb**. Sequencing was done in part on the **Roland MC-4 Microcomposer**, programmed numerically — "like making tracks on a taxi meter." James explicitly dislikes pre-programmed drum sounds and designs his own.

**Tracker workflow (Drukqs era):** James confirmed on Bleep (July 2017) that Drukqs was "mostly written in **PlayerPro** for the mac, my fave tracker" — a Mac classic tracker with per-cell DSP effects that he helped code. This numeric, step-time heritage runs straight through from the MC-4 to PlayerPro. A beatless PlayerPro render of "Vordhosbn" exists on his Vimeo.

**Drukqs prepared piano hybrid:** James modified a **Yamaha Disklavier** (MIDI-controlled acoustic grand) after John Cage — screws, bolts, felt between strings — and fed MIDI sequences rather than playing the keyboard. He **placed mics inside the piano body** so solenoid clicks became rhythmic counterpoint (audibly present on "Avril 14th"). His SoundCloud "Avril 14th Notes Played Backwards" log confirms: "played & programmed customised Yamaha Disklavier Pro, Recorded To Nagra IVS 5" — a Nagra IVS reel-to-reel captures the output. He also made MIDI-controlled solenoid drum mechanisms himself.

**Microtuning and tuned drums:** James to Pitchfork: "A lot of composers before me have been on this mission to change the world by getting off equal temperament, and I'm definitely one of those... When it's right in tune, it's like there's something slightly off." He advised Korg on the Monologue and Novation on the Bass Station II "AFX Mode" (per-key parameter locks, microtuning). He also retunes his **Roland MKS-50** via MIDI Mode 4 using an external HPI box. **His drum hits are tuned to the key of the track so percussion carries harmonic content** — a technique any producer can reproduce in Ableton by setting Simpler's Transpose per pad to match the track's root/fifth.

**Iterative resampling and feedback:** The "Ventolin" distortion was confirmed as **mixer feedback** — overgaining input-send with the same input signal — plus drum tracks fed into the **MS-20 filter CV input**. Drums were loaded into the **FZ-20M** sampler, then run back through MS-20 filters. His SoundCloud dumps (user18081971, 230+ tracks from 2015) reveal dense hashtag metadata (#tapedel #nagra #disklavier), extensive **SuperCollider 1** patch work ("listening to this reminds me I should release all the patches I made in Supercollider"), and polyrhythmic **Max/MSP** patches (the Barbican 2018 live-orchestra rehearsal included a patch that "broke directly before the gig").

**Syro disinfographic (caveat):** The Syro gear list is partially disinformation by James' own admission. Verified centerpieces: **Sequentix Cirklon** as the master sequencer; **Casio FZ-10/FZ-20M** with HXC floppy emulator for his trademark chord sound; **Korg PS3200** for the "Aphex chord"; **Yamaha CS80, DX100 (modded), Prophet-5 and VS, ARP 2500, Kawai K5000R**; **TR-808, R-8, Minipops 7 MIDI'd with separate outs**; **Serge Modular 9-panel, Make Noise DPO, Jomox Sunsyn ×2**; **Sound Devices 722** as the main field recorder. The minipops 7 reference is literalized in the track name "minipops 67 [120.2][source field mix]."

### Squarepusher (Tom Jenkinson) — signal flow as mental model

Jenkinson's core principle, from **Tape Op #89 (May 2012, Vijith Assar)**: "In order to really work fluently in a studio you need to have a model, or virtual image, of all those pathways in your head. If I'm running bits of data through it, I run it through the same pathway in my mental image, and then I know exactly what the results are going to be." He refuses engineers: "I'd have to convey a musical idea verbally to somebody — translating from one language to another. In my head the links are direct." This is why he prefers the **blind-numeric Yamaha QY700** — "When the graphical information is too vivid, it makes it harder to retain the information in my memory."

**Half-speed tape bass technique (Tape Op #89):** "In the late '90s, when I was still recording on multitrack tape, I did a lot of stuff by recording at half speed. What I'd do is run the tape machine at 7 1/2 IPS and pitch everything down an octave, play it at half speed so that the tracking and timing issues would diminish once I put it back to 15 IPS... It completely interferes with human fallibility regarding timing. The whole thing just goes unnaturally tight." Tape chain was **Fostex M80 → Tascam MSR16 ½" 16-track**; he moved to **Sonic Foundry Vegas**, then **Nuendo** in 2001 but keeps a "tape-recorder mentality" — no take-compiling.

**Hard Normal Daddy (1997) — "program like a player":** "It's just something I was trying to do — program like a player, make it have that swing, with a bionic aspect." On earlier records he inverted this: "trying to play like a robot, with no feeling whatsoever." Entire **Big Loada** tracks were one-pass sequences from a **Boss DR-660 MIDI-sequencing the Akai S950**: "To this day, nobody believes that the tracks on Big Loada were a single pass of me sequencing my Akai S950 from my DR660." The **S950's aliased pitch-shift algorithm is part of the D&B aesthetic** — crude repitching is a feature, not a defect.

**Amen break philosophy (SOS):** "I first heard it being used in the Mantronix track 'King Of The Beats'… the way that the drummer does the ghosting, the timing of the ghosting, the sound of his kit, the way it is recorded, the vinyl... everything works. You can pitch it up, down, stretch it, reverse it, it does everything. The Amen break is very sonically rich, very spectrally dense." On "Come On My Selector," the Amen is chopped/re-pitched/ghost-reversed inside the **S950**, triggered by the **DR-660**, with re-pitched hits layered to create rolls impossible from a single loop.

**Go Plastic (2001) no-computer rig:** "I didn't use a computer on Go Plastic. It was made with a **Yamaha QY700, TX81Z and FS1R, an Eventide DSP4000 and Orville, an Akai S6000 and a Mackie 16-channel desk.**" The DSP4000/Orville pair ran **custom algorithms Jenkinson wrote in Eventide's PC-based VSIG editor**, a modular-patch environment transferred via SysEx. Go Plastic's chopped-percussion granular sound came from Orville patches that randomised buffer length, reversed/pitched slices, and gated them. Specific example: "The bass distortion on the track 'Megazine' was done with an old-school 110V Morley Wah pedal and an Orville distortion patch based on a curve, X/Y-mapping module."

**Custom hardware:** Jenkinson built his own spring reverb using **four pairs of Accutronics type 1, 4, 8 and 9 springs** with soft-clip input stages, high-shelf EQ, invert/pan on each of four outputs, and series/parallel routing — used extensively on *Hello Everything*, audible at the start of "Bubble Life," "Circlewave," "Plotinus." His current synths "are all stuff that I've built myself in software, augmented with the FS1R and the TX81Z"; he uses **Reaktor Core, SuperCollider, Pure Data**. Self-taught via Curtis Roads' *The Computer Music Tutorial*.

**MIDI-bass trigger:** An **Axon AX100** MIDI pickup on his bass triggers S6000 samples, FS1R FM patches, or Reaktor instruments — he plays keyboard/sampler parts on bass strings ("it's my first instrument, so it makes sense").

### Autechre (Sean Booth & Rob Brown) — the studio as instrument

The foundational premise, Booth to *Sound On Sound* (April 2004): "I didn't want to learn how to mike up a drum kit, I wanted to know how to use the studio as an instrument. **Constructing harmony from a load of predefined frequencies is essentially no different [from building a bridge]. To me it's all construction, building.**" By 2013 (WATMM AMA) he declared: "the line between sequencing and synthesis is pretty much gone now. textures are sequences, sequences are like harmonies. it's all the same thing when you get down to it." Timbre, pitch, rhythm, structure share one parameter space.

**Max/MSP as bespoke instrument:** Acquired in 1997. Booth: "**Most of Confield came out of experiments with Max that weren't really applicable in a club environment.**" Max replaced the hardware patchbay as the organising metaphor; for any new track the duo "put the studio together in a certain way." On Gen: "i was getting quite into c a couple of years ago and then gen came out so i dropped it i way prefer using max to coding." On why they don't ship hardware: "part of the reason we make software is so that we can hack it easily, and save tons of versions."

**Generative but not random:** "When we do generative stuff we work with real-time manipulation of MIDI faders that determines what the rhythms sound like... **We don't use random operators because they're irritating to work with — every time you run the process it sounds different. How we play the system dictates how the system responds.**" The technique is **nested sequencers modulating each other**: "on Confield we also used analogue sequencers and drum machines, because you can do a lot with restarting patterns. You can hack things and maybe use a control volume to determine what step the drum machine is playing from. Perhaps you send that control volume from an analogue sequencer, so the drum machine is skipping around. And then you get another analogue sequencer to drive that analogue sequencer with a different timing. Immediately you have something that some people would call random, but I would say is quantifiable."

**Hardware → software evolution:** Early era — pause-button cassette edits, Atari + Cubase/Creator, TR-606, R8, Casio FZ1/SK1 (hacked by shorting chip pins), MC-202, SH-2, MS-10/MS-20, Ensoniq ASR-10. Middle era (Untilted–Quaristice) — the published 2008 tour rig: **Machinedrum SPS-1 UW MKII + Monomachine + Nord Modular G2X + Akai MPC1000 (JJOS1 firmware) + Bitstream 3X**, with MIDI running MD→MnM→MPC→G2 and Monomachine audio re-sampled live through the Machinedrum's FX chain. Late era (2010 onward) — almost entirely Max/MSP on an Apple laptop; per 2016 RA, neither member had bought new gear in 5 years. Community consensus: Autechre never adopted the Octatrack — the brief's mention of it is a misattribution.

**Routing signature:** Mackie 16:8 and 24:8 desks + Shure Auxpander (8×8 patchbay with knobs "so you can decide how much signal goes into each one"). "Stuff can go back in and back out as many times as we want it to" — **feedback-routing is central to the Autechre sound design**. DAW: MOTU Digital Performer long-standing. Booth manifesto: "You can make anything you do in the computer sound amazing… computers do compression really well, and even reverb." Screen-off discipline: "There's nothing better than turning the screen off and just going analogue."

**NTS Sessions (2018):** 8 hours across four 2-hour broadcasts. Method — a persistent Max/MSP environment ("the system") described in press as "a labyrinthine compendium of software synthesizers, virtual machines, and digital processes." "I think the oldest thing is from 2011… weird recent jams using old patches" (Booth to *Pitchfork*, 2018). **Archival, version-controlled composition** — save many states, revisit years later. The closing "all end" is a ~58-minute near-static reverb piece that brings the runtime to exactly 8 hours.

The signature "rubbery/twangy" drums across Chiastic Slide/Confield/Untilted are community-attributed to **home-brewed FM drum synthesis in Max/MSP** with short-decay resonant filters and programmed micro-timing (KVR/Elektronauts consensus, not officially confirmed).

### Four Tet (Kieran Hebden) — arrangement above all

Primary source: **Tape Notes Podcast #140 (2024)** on *Three* and the KH track "Looking At Your Pager."

**The core workflow is absurdly stripped:** "Everything's done on this laptop. The whole record was made on this laptop." Listening: "**90% of the listening and mixing and everything for this album, all the music I make these days is just the laptop speakers.**" Writes in bed, on trains, on planes, on Audio-Technica reference headphones + Sennheiser HD25s. Hardware exists for sample creation only: "I have quite a few drum machines and I'm not somebody who has everything hooked up with MIDI… I'll spend time with hardware and instruments to create samples."

**Plugin arsenal:** **Spectrasonics Omnisphere** is "the synth, main synth plugin I use for absolutely everything." He uses presets alphabetically ("Plectra Sub," "Swaggering Around"): "I pretty much only use presets on things. I don't really mess with... definitely not one of those people that's like, I'm going to start with a sine wave." **NI Kontakt** for orchestral (harp on "Daydream Repeat"). **SoundToys MicroShift** — "makes things sound more three dimensional." **FabFilter Pro-L2 + iZotope Ozone Maximizer** on his own master bus. Hardware sample sources: **Roland TR-8, Arturia DrumBrute**, two cassette four-tracks used heavily during lockdown.

**The MIDI randomisation trick — used on "pretty much everything":** "get some sort of midi pattern together and then put some sort of randomization on the velocity of the midi notes. So I've put the velocity and I've made it random 15%... And then I'm asking it also to 15% of the time to pick one of the notes and play either an octave up or an octave below. And it stops the pattern being totally repetitive. You just get these little sparkles and twinkles." Consequence: **every render is different** — "the version on the vinyl will be different probably to the version that's digitally available."

**Subliminal layering philosophy:** "there's little quiet echo-y bits of vocals and noises and little things happening all the time combined with everything else… tons of subliminal little sounds and textures all the time." Historical Fridge precedent: live room mics of players chatting and playing video games, quietly in the mix with delay — "these little bits of texture mixed in with everything actually put things in a world… a way for people to connect to it without them really even understanding why they're connecting to it."

**Doubling trick — "Skater":** Omnisphere "Plectra Sub" bass doubled by an identical MIDI bell part — "you can't really hear the bell too much… without it, it's burying the bass more in the mix." The main lead is the same melody on three different instruments, layered in sequence.

**Kick-stack on "Daydream Repeat":** **Four stacked elements** — main kick sample, sine-wave sub layer "almost inaudible on headphones but just gives the weight in a big club," short transient click (cutting through), fourth sub-layer for body. Process: iteratively add layers over months of club playbacks solving only-on-big-rig problems.

**Arrangement is the whole game:** "arrangement is just everything… none of it really matters in comparison to the arrangement. Like the arrangement is the whole thing that's going to make it work... there's no point in having a good sound if it's not arranged into anything." And on simplification: "ideally you're doing as little as possible… I pretty much never want to put a compressor on anything. Like if I have to put a compressor on something, it's to deal with a problem."

### J Dilla — per-element swing and disabled quantize

Primary gear was the **Akai MPC3000** (now at the Smithsonian); early work used the **E-mu SP-1200**; Donuts used Pro Tools + MPC3000 with the **Boss SP-303/Roland SP-404** only arriving in the hospital (contra popular myth — see Dan Charnas, *Dilla Time*).

Dilla's signature: **quantize disabled, hands on the pads, per-pad swing**. The MPC3000's decisive advantage over the SP-1200 was **per-pad swing**, enabling different swing values across kicks, snares, and hats simultaneously — a near-polyrhythmic feel where hats might tightly swing while kicks drag. Typical displacements: kicks ±20–30ms off grid (not consistent direction), snares creeping ~20ms *early*, hats freehand. On "Get Dis Money" (Slum Village) he refuses to place kick on the downbeat and builds on a 7-bar Herbie Hancock loop.

**Drum tuning and layering:** Multiple kicks — high-passed click layer (compressed hard, rolled-off top, 1kHz+), plus low-end thud — transient-aligned. Narrow-Q EQ boosts 1–10kHz on click layers. Kicks pitched to complete/harmonize with the sample's bassline. On "Runnin'" (Pharcyde) he chopped Stan Getz's "Saudade Vem Correndo" guitar pitched up a half-semitone, then low-passed the sax sample to extract a new bassline from the same source.

**Questlove's canonical quote:** "My mission to get accepted by the hip-hop nation was to sound synthetic like a drum machine, to sound like a sample. His approach was to sound as sloppy as a real musician. But it was so sloppy, I know he wasn't doing it by accident."

### DJ Shadow — Entroducing as sample monasticism

*Entroducing.....* (1996) made on an **Akai MPC60 II + Technics 1200 + Alesis ADAT**, nothing else. "I did the album on the MPC-60 MKII, with nothing else, really. It was truly an exploration." On preferring MPC over SP-1200: "the SP-1200 had been around for like four years, the sound was well established, and it had some real audio limitations in terms of the bit rate and stuff." Workarounds: sample at 45rpm to save RAM, pitch back down in the MPC; multi-pass SMPTE lockup to ADAT to bypass polyphony limits.

**"Building Steam with a Grain of Salt":** melodic hook is Jeremy Storch's "I Feel a New Shadow" (1970) piano refrain, looped; vocals from THX 1138 and jazz snippets. The **drum break at ~2:43** — chopped/reprogrammed on MPC60 pads, including sick kick triplets, not quantized, hand step-edited. Tension structure: slow ambient intro → sudden break-chop kick triplet → drop to sparse piano → drums return augmented. Most of Entroducing's "loops" are actually carefully arranged programmings.

### Pete Rock, RZA, Kanye, Madlib, Premier — hip-hop translations

**Pete Rock's SP-1200 approach:** "I only sample stuff that gives me a good feel. Something that sets my soul on fire." Pioneered **filtering full-mix stereo records with studio EQ (a wah-wah-type) at Greene Street** to extract basslines where no stem existed. "T.R.O.Y." uses two different sections of Tom Scott's "Today" for verse vs. chorus; drums from James Brown "Say It Loud."

**RZA's gear switch unlocked the Wu sound:** SP-1200 through "Bring the Pain" / "Method Man," then **Ensoniq EPS-16 Plus** on "C.R.E.A.M.," "Bring da Ruckus," "Protect Ya Neck," then **ASR-10** on "Shame on a Nigga," "Clan in da Front." RZA: "Nobody was doing 2-bar and 4-bar loops. So it was the EPS that turned me onto that, and I fell in love with the EPS." And: "The whole first 100 Wu-Tang songs was made on ASR-10." The 4-bar loop (vs SP-1200's 2.5-second pad limit) is **why Wu-Tang sounds more cinematic than contemporaneous boom-bap**. The "Red Box" drum bank + Novation Bass Station (on "Triumph") + Ampex MM-1200 tape = dusty/lo-fi signature.

**Kanye chipmunk soul** is **Re-Pitch warp mode + 4–7 semitones up**. Coupled pitch-tempo via old-gear varispeed is the authentic artifact — time-stretch loses the character. Just Blaze (RBMA): "RZA started it in like 1996… RZA's style was closer to a sped-up loop… The way me, Kanye and Just chopped it, it was more: We'll get seven pieces of a record, put it back together, add a breakdown part and make the sample do the hook."

**Madlib's SP-303 aesthetic:** Most of Madvillainy tracked in Brazil — "Raid,' 'Rhinestone Cowboy' — I did in my hotel room on a portable turntable, my 303, and a little tape deck." His "boomsauce" bass wobble is sampled bass + realtime SP-303 filter/drive FX modulation during resampling. His Pro Tools-era mix engineer **Dave Cooley**: "Madlib likes to shoot from the hip, so sometimes it's a deliberate and intentional choice on his part to go with the most rough-hewn version of a mix."

**DJ Premier micro-chopping:** "Mass Appeal" uses ~2 seconds of Vic Juris's "Horizon Drive" (at 3:36). "N.Y. State of Mind" pairs a Joe Chambers piano/bass unison with Kool & the Gang "N.T." drums pitched **down 16 BPM** (from 100 to ~84) — the deep, stretched, golden-era drum texture. Scratching as hook: "That loop [Ten Crack Commandments] is me sampling my scratching by hand. It was me experimenting, and it sounded dope."

### Death Grips — distortion as percussion

Ableton-based (Morin's Instagram, via Equipboard). Shure Beta 58A vocal, Korg MicroKorg, Roland VP-03, Korg Monologue, Fender P-Bass. Zach Hill's drumming is aggressively syncopated, resampled and chopped — on *Niggas on the Moon* it's entirely V-drums with chopped Björk vocals. Morin's processing chain on drums (reconstructable in Ableton): **Drum Bus → Saturator → Overdrive (Drive max, Tone ~60%) → Saturator (Analog Clip) → OTT → hard limiter into clip → EQ notch at 200–400 Hz → parallel compressor 10:1.** On "System Blower," Williams Sisters' tennis grunts are time-stretched and pitch-shifted into both snare layers and melodic hits; Vancouver SkyTrain noise is an atonal drone bed. "Hustle Bones" (110 BPM, E minor, 4/4) feels rhythmically complex because **every-third-16th accents against 4/4** and MC Ride groups syllables in 3s — the meter-friction is the complexity, not actual odd meter.

---

## 2. Plugin-specific technique guides — SoundToys for IDM

### Decapitator — five analog saturators
Style decoder: **A** = Ampex 350 tape (smooth even-order, best all-purpose and mix bus); **E** = EMI TG channel (Abbey Road punch, drum bus and vocals); **N** = Neve 1057 germanium (dull/weighty, thickens synths); **T** = Culture Vulture Triode (warm even-order — the producer favorite on snare/bass/breaks); **P** = Culture Vulture Pentode (odd-order aggressive, for destruction and leads).

IDM recipes (all settings synthesized from SoundToys manual + reverbmachine.com Aphex Twin reconstructions + Gearspace):
- **Breakbeats:** Style T, Drive 5.0–6.5, Tone 1–2 o'clock, Low Cut ~80 Hz. Crunchier Squarepusher: Style P, Drive 7–8, Punish ON, High Cut ~8 kHz with Steep.
- **808s:** Style A, Drive 2–3, Thump ON, Low Cut ~30 Hz, Mix 40–60% parallel.
- **Reese bass:** Style N, Drive 3–4, Thump ON, Mix 70%.
- **Aphex Twin SAW 85-92 master-bus chain (confirmed by reverbmachine.com):** Decapitator Style A, Drive ~3 → XLN RC-20 Cassette 1st Gen → master. This single chain produces the album's lo-fi vibe.
- **Parallel via Return track:** Decap at Mix=100%, Style P, Drive 8, Punish, LP ~100 Hz; sidechain-duck the return against kick.
- **Aliasing warning:** at 44.1 kHz with Drive >6 + Style P, Gearspace reports audible aliasing. Run at 88.2/96 kHz or HP with Pro-Q3 at 16 kHz.

### EchoBoy — 30 echo styles
Essential styles: Studio Tape (Ampex 102 @ 15 ips, clean), EchoPlex/Plex (EP-3), Space Echo (RE-201, self-oscillates beautifully), Memory Man (BBD pedal), Cheap Tape (lo-fi), TelRay (oil-can), Transmitter (CB radio mids).

IDM recipes:
- **Aphex 1/8-dotted dub delay:** Space Echo, Single, 1/8-dotted, Feedback 55%, Saturation 40%, Wobble 25%, Diffusion 15%, LC 300 Hz, HC 4 kHz, Groove +10%.
- **BoC lo-fi:** Cheap Tape, 1/4 triplet, Feedback 40%, Wobble MAX, Saturation 60%, Mix 25% on send.
- **Polyrhythmic ping-pong (IDM-critical):** Mode Ping-Pong; **Ping = 1/8, Pong = 1/4 triplet** — uneven sides produce non-repeating bouncing, Feedback 60% recursively offsets L/R.
- **16-tap Rhythm mode (Autechre):** Mode Rhythm, 16 taps at steps 1/3/4/7/10/11/14/16, varying Shape amplitudes, Style Plex, Feedback 0 (rhythm provides complexity), Accent 30%. Any single hit becomes a polyrhythmic sequence.
- **Space Echo runaway:** Feedback 85–95%, slam Input; automate feedback past 90% for RE-201 squeal.

### Crystallizer — granular reverse echo (H3000 lineage)
Knobs: Pitch ±4800c, Splice 0–~500 ms, Delay up to 1500 ms, Recycle, Threshold/Gate/Duck, Forward/Reverse. IDM recipes:
- **Shimmer pad:** Pitch +1200, Splice 200 ms, Delay 1/4, Recycle 60%, Forward, LC 200 Hz.
- **Reverse-tail on drums:** Pitch 0, Splice 300–400 ms, Delay 1/8, Reverse, Recycle 30%, Gate triggering on transients only.
- **Granular glitch vocals:** Pitch 0, Splice 30–80 ms (short = glitch artifacts), Delay 1/16 triplet, Recycle 70%, Mix 100% on return.
- **Reverse-pad from mono pluck:** Pitch +1900 (oct+fifth), Splice 500 ms, Delay 1/2, Recycle 75%, Reverse.

### PhaseMistress, Tremolator, FilterFreak, Radiator, MicroShift, Little AlterBoy
- **PhaseMistress odd-stage trick:** 3/5/7-stage gives inherent LP filtering and stutter — unique to PhaseMistress. Rhythm Mode 1/16 + custom pattern + Resonance 70% = filter-jump patterns impossible on hardware.
- **Tremolator stutter gate:** Shape Square, Rhythm 1/16, custom 16-step (e.g., X.X.XX..X.X.XXX.), Depth 100%, Accent 50%, Analog ON — instant Squarepusher stutter pad on held synth. **Rhythm patterns share clipboards across Tremolator, FilterFreak, PhaseMistress, Crystallizer and EchoBoy's Rhythm Mode** — program once, paste into all five for synchronized gate+filter+phase+slice+delay (the SoundToys secret IDM workflow).
- **FilterFreak acid resonance:** Res ≤ 85% to stay sub-self-oscillation; Analog Mode + Pump style adds compression-like limiting. Envelope Follower with Attack 2 ms, Release 150 ms = TB-303 squelch.
- **Radiator:** Input drives Tube 1 pre-EQ; Output drives Tube 2 post-EQ. Thick 808: Line, Input 6, Output 3, Bass +3, Treble −2. Broken radio: Mic, Noisy ON, Input 8, Output 7.
- **MicroShift:** Style I = H3000 preset 231 (classic widener); Style II = H3000 preset 519 (warmer); Style III = AMS DMX 15-80 (wider, more aggressive). Use **Focus** at 200–400 Hz to keep lows mono.
- **Little AlterBoy metallic hats:** Pitch +12, Formant −3, Quantize ON, Mix 60%. Hidden killer: **Robot mode MIDI-controlled**, sequencing a 16-note pattern that forces any input to those pitches — effectively a monophonic vocoder.

---

## 3. Ableton Live 12.3 workflow essentials for IDM

Live 12.3 (released November 25, 2025; maintenance through April 13, 2026) is the most generative-friendly version.

**MIDI Transform & Generate tools (12.0 introduced, iterated through 12.3):** Transform — **Arpeggiate** (set Style Converge, Rate 1/32, Steps 3, Distance 7st for melodic shrapnel), **Strum** (Low +15%, Tension −80% for fast-to-slow rolled chords), **Connect** (interpolates notes, Density 70%), **Ornament** (flams and grace notes at Length 1/64), **Recombine** (randomize order/pitch/velocity — the "card-shuffler"), **Time Warp** (breakpoint speed curve 2.0x → 0.25x across two bars = Autechre-style tempo warp on a snare roll), **Velocity Shaper**, **Quantize** granular edition. Generate — **Seed**, **Stacks**, **Shape** (draw sawtooth + Jitter 25%, Density 60% = broken Squarepusher leads), **Rhythm**, **Euclidean** (16/5/rotate 3 for forward hats; 16/7/0 for dense syncopation). **12.3 additions:** Generators by Iftah pack (includes **Sting** acid-bassline generator), Rhythm Generator Drum Rack layout for Push 3.

**Note chance and velocity range** (refined through 12.x): combined with Follow Actions, hi-hat Chance 60–75% + kick 100% + ghost snare 40% yields non-repeating patterns.

**Capture MIDI in 12.3** no longer clears its buffer when notes play over a playing clip and transport stops — your improvisation survives.

**Arrangement 12.3 wins:** **Bounce to New Track** (12.2), **Bounce Groups** and **Paste Bounced Audio** (12.3) enable the bounce-and-arrange workflow as a native loop. **Arrangement Mixer** (⌥⌘M) opens strips beside the timeline.

**Simpler vs Sampler:** Simpler has **Warp** (Sampler doesn't), so Simpler is the right choice for rhythmic sample triggering in any of its three modes — **Classic** (melodic play), **One-Shot** (drum hits, Fade In/Out, Trigger/Gate), **Slicing** (transient/beat/region/manual markers, Mono/Poly/Thru). Sampler handles multi-sample zones and round-robin. **Slice-to-MIDI for breakbeats:** right-click warped clip → Slice to New MIDI Track → choose a saved Drum Rack default with Simpler in One-Shot/Trigger mode (clean one-shots for breakcore); nudge markers to zero-crossings to kill pre-hit clicks.

**Stem Separation (12.3, Suite only, GPU on macOS 26.3+ Apple Silicon)** splits a clip into Vocals/Drums/Bass/Others locally. Separate → isolated drum stem → Slice to MIDI → chop cleanly without bass bleed. Game-changer for sampling messy breaks.

**Wavetable for IDM:** Modulate Osc 1 Pos with LFO 1 (square, Rate 1/16, Depth ±30%) for stuttering timbral shifts. Env 3 in Loop mode (A 66ms/D 141ms/S 0) driving Pos = evolving pads. Osc FX FM (Tuning +7st, Amount 40%, Env 3 modulating Amount) = metallic IDM leads. Unison Random Note (2 voices, 20%) for stereo wobble.

**Granulator III (M4L, 12.0, Henke):** Grain 2ms–2s. Classic/Loop/Cloud modes. Full MPE. Built-in Capture. IDM parameter recipes: **glitchy grains** — Cloud, Grain 10ms, Shape 0%, Variation 30%; **smooth pad** — Cloud, Grain 50–100ms, Shape 100%, Scan 0.1–0.5x; **rhythmic re-pitching** — Classic, tempo-synced LFO on Position at 1/8, Grain 50ms.

**Complex Pro warp artifacts:** Formants 100% preserves vowel character at heavy pitch shifts; Envelope 64 for high-freq sources, 256 for low. **Texture mode:** Grain 50ms smooth, 10ms glitchy; Flux 0 stable, 80–100% evolving cloud. **Pitfall:** Complex Pro softens kick transients — nudge warp markers a few ms *before* each kick or layer Beats mode underneath via crossover.

**Follow Actions generative drums:** 4 variations per track (main/fill/stripped/syncopated), Action A=Any, Action B=Other, Chance 50/50, Linked — non-repeating beats that never play the same sequence twice. Scene Follow Actions advance structure while clip FAs add within-section variation.

**Racks for parallel IDM processing:**
- **Multiband saturation Rack:** 3 EQ-Eight BP chains; low (<200 Hz) → Saturator Analog Clip +6 dB; mid → Saturator Soft Sine +3 dB; high → Roar Tube with feedback. Each chain's vol on its own macro.
- **Transient/Body/Tail kick Rack:** Chain 1 click (HP 2 kHz, A=0 H=5 D=20), Chain 2 body (60–200 Hz, D=100), Chain 3 sub/tail (30–60 Hz sine, D=100–300, plus Drum Sampler Stretch FX + Resonators). Macros: Transient vol, Body pitch ±12st, Tail length, Rack vol.
- **Chain Selector** + **Macro Variations** (12.2+) enables Autechre-style patch-flipping across 8–16 recallable snapshots.

**CV Tools** (free for Suite/Standard+M4L; requires DC-coupled interface like ES-9): CV Instrument, CV Triggers, CV Clock In/Out, CV In, CV Utility, CV Shaper, CV Envelope Follower, CV LFO, Rotating Rhythm Generator. Envelope Follower on kick → CV Out → Mother-32 VCA = hardware sidechain ducking.

**M4L essentials:** K-Devices TTAP (dual-buffer delay with Bend, Repeats, reversed buffers), Surreal Machines Magnetic/Diffuse (RE-201 tape + reverb hybrids), K-Devices Modulators 21 (KNOR gesture recorder, LFOH! with swing/squeeze), POLYRHYTHMUS (free polyrhythm engine), Euclidean Sequencer Pro (alkman, 4 voices routable).

---

## 4. Sampling and drum programming — curated techniques

**Extreme timestretch (800%+) as instrument:** Stretch clip by setting Seg. BPM to 1/8 of project tempo in Complex Pro. Formants 100 to preserve character when transposing, Formants 0 for aliased "chipmunk." Envelope 64 for hats, 256 for bass. Switch to Beats + Preserve 1/4 + Transient Envelope 0 for choppy stretched segments; Texture mode with Flux 100% for evolving drones from any source. **Bounce frozen tracks** above 4× stretch — CPU scales.

**Creating drums from non-drum samples:** Kicks — sample a slam/"buh", Amp Envelope A=0 D=80–150ms S=0, pitch −12 to −24st, HP 30 Hz, LP 200 Hz, layer 2–5ms click HP 2 kHz. Snares — book-slam or "ts/ch", D=120–200ms, transient shaper Attack +40–60%/Sustain −20–40%, layer white-noise burst BP 200 Hz. Stagger transients by 1–3ms between layers to avoid phase cancellation (Attack Magazine's fix).

**Spectral freeze (PaulXStretch):** Stretch 20×–50×, Freeze to sustain current frame, small windows = choppy, large windows = smooth FFT smear. Bounce because Freeze response lags with large FFT. Render 3 different Window sizes of same source and layer for "ghost-in-the-machine" pads. In-Ableton alternative: **Hybrid Reverb** with infinite freeze.

**Reverse reverb recipe:** Duplicate snare track → Reverse → Consolidate → Reverb (100% wet, Decay 2–4s, Predelay 20–40ms, LC 200 Hz) → resample → reverse resampled clip → align swell crescendo to next snare transient.

**Self-resampling feedback:** Bounce drum bus to new track, add Redux (bit/SR reduce) + Saturator Soft Sine + short self-feeding delay, bounce again, repeat 3–6 times. **HP at 20 Hz in the chain** to prevent DC buildup.

**Groove Pool for Dilla feel:** Cmd/Ctrl-Alt-6 opens pool. Extract Groove from any audio clip (right-click → Extract Groove) and drop on MIDI. Timing 0–130%, Random for micro-ms jitter, Base = 1/16 for IDM. Rule: keep kick and main hat straight; swing off-beat elements. For Dilla feel, push snare ~3–7ms early or late and hats 2–5ms late on separate tracks.

**Amen break manipulations:** Ableton → Slice to MIDI (1/16), reorder. Venetian Snares method — map same slice to multiple keys with different loop/start points for ultra-tight 1/32 stutters. Squarepusher method — S950-style repitch aliased hits layered into rolls impossible from one loop. Aphex method — manual chop + reverse random slices, then resample and restart.

**Polyrhythms in Ableton (Ali Jamieson method):** Separate MIDI clips on 4 tracks feeding one Drum Rack at unequal lengths — kick 16/16, perc 5/16, hats 7/16, claps 3/16. Pattern repeats only at LCM of clip lengths, creating long evolving phrases. Or use POLYRHYTHMUS / Euclidean Sequencer Pro: Kick 16/4/0, Snare 16/3/2, Hat 16/7/1, Clave 12/5/0.

**Filter-per-hit:** Drum Rack chain with Auto Filter mapped to Macro; draw per-note MPE/Note Expression envelopes (Live 11+); or use Expression Control / Note Modulator M4L to drive filter from velocity.

**Multiband sidechain:** Split bass into 0–120/120–800/800+; sidechain only 0–120 band from kick via Pro-MB. Decouples low-end duck from mid-bass continuity. Alternate: use a muted dummy MIDI kick (downbeats-only) as the sidechain key while the audible kick plays busier patterns.

**Drum layering frequency discipline:** Transient 2–8 kHz / 5–15ms, Body 60–200 Hz / 40–80ms, Sub 30–60 Hz sine / 100–300ms. HP transient above 2 kHz, LP body at 300 Hz, LP sub at 80 Hz. Align zero-crossings within ±2ms, then intentionally stagger transient layer 1–3ms to prevent identical-peak cancellation.

---

## 5. Arrangement and composition for IDM

**Five loop-breaking workflows:**
1. **Bounce-and-Arrange / Burial method** — once a loop "feels finished enough," freeze + flatten to one stereo clip, drop on a 4-minute timeline. You can no longer sound-design; you can only chop, mute, and vary. Burial's actual quote on Sound Forge: "Fuckit, I'm going to stick to this shitty little computer program, Soundforge."
2. **Session → Arrangement performance** — build scenes (Intro/A/Break/Drop/Outro), arm Arrangement Record, perform mute/solo/scene-launches live, then refine.
3. **Reference-track locators** — drag a reference at bar 1, insert locators at every section change, build beneath the stencil, delete reference before export.
4. **Subtraction** — start with the full drop, work backwards muting layers.
5. **Skeleton first** — block 4-minute form with placeholders in 30 minutes, then detail.

**IDM structural analysis:** Linear IDM (Four Tet, Boards of Canada) = gradual accretion, ABA arc. Non-linear IDM (Autechre, Squarepusher) = hard collage, algorithmic recombination. Aphex "Alberto Balsalm" holds one harmonic loop and varies drum patterns every 4–8 bars. "Flim" is ABA′ — 0:00 intro / 0:45 drum entry / 2:00 breakdown / 2:40 return with counterpoint / 3:40 outro. "Come On My Selector" is hard-cut collage, no risers. "Parallel Jalebi" is 8 minutes of one loop with muting and vocal recession.

**Tension/release parameters (automate independently):** Filter sweeps, frequency build (sub in / air in), rhythmic density (quarters → 16ths → 32nds), harmonic tension (one dissonance against a 24-bar drone), **dynamic range** (pull −6 dB out of the master in a break so the drop punches through glass), stereo width collapse/open.

**Silence as instrument:** Aphex "#3" / Autechre Tri Repetae — in a 4-minute track, write at least 8 bars with one element only, and at least 2 bars of true silence/reverb tail. This fights the fill-every-inch pathology.

**IDM-specific drops:** Textural (new timbre replaces kick energy), inverse (remove kick at EDM-drop moment — Aphex "Come to Daddy Dub," Burial "Archangel" at 1:30), ghostly (Burial — pitched vocal stutters + vinyl-crackle rise + foregrounded foley; no white-noise riser).

**Transitions palette:** Risers (layer white noise + pitched sine + Shepard; automate HP + vol + reverb send), downlifters (LP closing, pitched-down sample), filter/delay swells (1/2-note ping-pong with 60% feedback, automate send), reverse cymbals, **dblue.TapeStop** on master, **1-bar dead silence** (under-used), feedback drones (route two synths into each other, record 5 min of chaos, slice for transition material).

---

## 6. Pedagogy — intermediate-producer curriculum

**Diagnosed intermediate mistakes** (Berklee Online, Point Blank, EDMProd consensus): starting with sound design instead of arrangement skeleton; over-layering; mixing in a loop not in context; no A/B with commercial releases; preset-chasing; never finishing.

**Suggested 12-week curriculum:** Wk 1–2 critical listening + reference analysis; Wk 3–4 sound design primitives (one synth, 10 patches from scratch); Wk 5–6 arrangement (bounce-and-arrange, scene workflow); Wk 7–8 transitions + mixing in context; Wk 9–10 two constraint exercises (one-sample, time-box); Wk 11–12 finish and release two tracks.

**Constraint exercises** (drawn from Eno's 1994 *The Mix* — "the assumption that if you remove all constraints from people they will behave in some especially inspired manner… doesn't seem to be true in any sense at all"):
- **Oblique Strategies** — draw a card pre-session. DAW-useful cards: "Honour thy error as a hidden intention" (keep the glitch), "Only one element of each kind" (no layered kicks), "Change instrument roles" (kick plays melody, hat plays bass), "Use fewer notes," "Take away the elements in order of apparent non-importance."
- **One-sample challenge** (Andrew Huang's *4 Producers 1 Sample*) — every element derived from one source via pitch/granular/time-stretch/resample.
- **Four-sound challenge** — only four named audio sources; unlimited processing.

**One-sample teaching ladder (4 weeks):** Week 1 — 1 sample, 2 minutes of music with drums/bass/melody. Week 2 — 3 samples, 3 minutes with clear sections. Week 3 — add one synth, 4 minutes. Week 4 — full palette + obeyed Oblique Strategies card; A/B demo of Week 1 vs Week 4 shows growth.

**Time-boxing:** 24-hour track (Andrew Huang's *Sonic Boom*, Gourmet Ravioli); Pomodoro (25/5, long break after four cycles); "Finish one first" — no new project opens until current is bounced/exported (EDMProd's non-negotiable rule).

**Breaking loop addiction:** Hide the grid (collapse track heights in Arrangement View; turn off snap). Long improvisation — record 10 continuous minutes over a loop without editing; then extract the 20 best seconds as composition material (Autechre long-jam method at beginner scale). **Arrangement-first** — open the session in Arrangement View with section markers already placed before opening any synth. Bounce-and-mute discipline — no re-opening stems for 48 hours.

**Critical-listening protocol (Berklee Online OMPRD-382):** Load reference and WIP on adjacent tracks, level-matched via LUFS meter. Listen in 30-second chunks, switching. Note: low-end energy, stereo width, vocal/lead clarity, transient sharpness, reverb depth.

**Reverse-engineer exercise:** Pick a 30-second reference excerpt. In 2 hours, recreate with only stock DAW instruments. Side-by-side A/B critique in class. Song Exploder assignments — one episode/week, 200-word summary of a production decision (Porter Robinson's "Get Your Wish" for subtlety-as-subconscious-perfume is canonical).

---

## 7. Track-specific production insights

- **"Windowlicker" (1999):** C minor; uses **MetaSynth** (U&I Software's image-to-sound tool — confirmed) to embed a spiral image and a "devil face" visible in spectral analysis at track's end. Community-attributed synths: Yamaha GX-1, Korg MS-20. Bass wall of distortion likely granular/spectral plus subs. The orchestral arrangement is live strings doubled/processed.
- **"Flim" (1997):** 148 BPM, C minor, 2:57. Kicks on 1/3, snares on 2/4, eighth hats, plus extra snares between backbeats creating "push."
- **"Alberto Balsalm" (1995):** No confirmed external samples (WhoSampled). The warm-pad-with-fast-pitch-jumps section (2:34–3:20) is two layered synths — a saw/tri pad through 24dB/oct LP plus a saw with fast VCA decay and BP filter wah (KVR analysis).
- **"Vordhosbn" (2001):** D♭ minor with microtuning. Written in PlayerPro (confirmed, RDJ Vimeo). Drums are resampled knob-turning sessions, tight amp/pitch envelopes, sequenced in tracker. 8-bar turnarounds; bass enters at bar 9, counter-melody bar 21, delay-feedback sound bar 138.
- **"minipops 67" (2014):** References Korg Mini Pops 7 1967 drum machine (MIDI-modded). Moog modular bass (RDJ admits, with "disinfographic" caveat).
- **"Rhubarb":** Rumored Oberheim Matrix-1000 based on preset similarity; Yamaha CS-5 had liner notes handwritten on it. 2024 expanded edition adds an orchestral version by AUKSO Tychy Chamber Orchestra.
- **"My Red Hot Car" (2001):** No computer — Eventide DSP4000/Orville, QY700, TX81Z, FS1R, Akai S6000. Vocoder by Jenkinson; Amen break chopped/restitched. Orville custom patch handles the granular bass resampling.
- **"Come On My Selector" (1997):** Amen break + Lyn Collins "Think" woos, S950-triggered from DR-660, likely single-pass (per Jenkinson's Big Loada claim).
- **"Iambic 9 Poetry" (2004):** 78 BPM, D major feel (D/Bm/G/F♯m). Live fretless-style bass from Jenkinson; likely live drums for ~first half. Eventide Orville was primary processor.
- **"Vic Acid":** Amen break resequenced with acid-bass (303 or TX81Z) lines on top.
- **"She Moves She" / *Rounds*:** Made entirely in a North London flat on AudioMulch + Cool Edit Pro, ~200–300 samples for the album, 20–30 per track, most processed beyond recognition.
- **"Parallel Jalebi" (2013):** Mariah Carey "Lead the Way" vocal + Mulatu Astatke "Kasalefkut-Hulu (2)" Ethiopian jazz (WhoSampled confirmed).
- **NTS Sessions (2018):** Persistent Max/MSP system with patches dating to 2011, modular (Buchla + Eurorack) inputs, archival recombination.
- **Death Grips "Takyon":** Distorted 4-on-the-floor pitched-up kick, layered clap/handclap/noise-burst snare, industrial techno kick with 808 slides in half-time, monophonic square-wave bass through heavy distortion, ride chant as counter-rhythmic hook.
- **"Ten Crack Commandments":** Premier resampled his own hand-scratched loop and triggered it as a drum sample.
- **"N.Y. State of Mind":** Drum break (Kool & the Gang "N.T.") pitched **down 16 BPM** — the trick for that big, slow, golden-era drum feel.

---

## Conclusion — design principles distilled

Three cross-cutting philosophies unite this entire corpus.

First, **build instruments, not tracks.** Autechre save Max patches across decades and revisit them. Aphex Twin curates temporary micro-rigs as constraint. Squarepusher writes VSIG algorithms for the Orville. Four Tet uses 15% MIDI velocity/octave randomisation so every render breathes. The lesson: persistent systems produce the idiosyncrasies that separate IDM from its influences. In Ableton this maps to racks-with-macro-variations, Follow Action pools, and self-referential M4L modulation.

Second, **arrangement beats sound design.** Hebden, the producer with arguably the widest-reaching influence in this set, works on laptop speakers, uses Omnisphere presets, refuses compression by default, and considers arrangement "the whole thing." Every canonical IDM track analyzed here rewards form-level listening more than plugin archaeology — "Flim," "Alberto Balsalm," "Parallel Jalebi," Autechre's NTS Sessions. The pedagogical corollary is the bounce-and-arrange method combined with ruthless time-boxing: intermediate producers need to finish, not to perfect.

Third, **constraint is a creative tool.** From Eno's Oblique Strategies and the one-sample challenge to Jenkinson's half-speed tape gambit, to Aphex's track-specific gear libraries, to Burial's "shitty little computer program Soundforge," every serious practitioner in this tradition makes art by choosing what *not* to do. A curriculum that teaches intermediate producers to impose constraints — single-sample weeks, 24-hour tracks, hide-the-grid improvisations, one-plugin mixes — will develop faster ears and more finished music than one that teaches more plugins. The craft ceiling is not set by the tools; it's set by the discipline to resist them.

---

**Important caveats:** Aphex Twin gear lists (especially Syro's) are partly disinformation by his own admission; many community claims about specific synths per track are speculation. The "Korg Poly 800 modification" specifically referenced in the original brief is less documented than the confirmed SH-101 and DX100 mods — treat it with caution. The Octatrack in Autechre's rig is a misattribution; their confirmed Elektron rig is Machinedrum + Monomachine. Some setting recommendations (SoundToys numeric values, Death Grips distortion chain) are reconstructions from audio analysis and forum consensus, not artist-confirmed. SoundCloud artist dumps and hashtag metadata are authentic primary sources. The "Dilla wrote Donuts on the SP-303 in hospital" narrative is myth — Charnas's *Dilla Time* documents Donuts was primarily Pro Tools + MPC3000, with SP-404 arriving very late. Where precision matters for a curriculum, teach the technique and the attribution caveat together.