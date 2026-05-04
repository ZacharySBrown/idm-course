# What else Max can do

Max is not just the IDM-patch thing. Once the dataflow clicks, it is the most flexible prototyping environment in the studio.

Non-IDM uses worth knowing:

- **Instrument mapping layer.** A Max patch that takes in OSC from a phone, remaps, and sends MIDI to Live. Zero code for a custom controller.
- **Sample management.** Build a sample browser with `umenu` + `sfinfo~` + `sfplay~`. Preview, tag, drop into Live via drag.
- **Generative video.** Jitter is a full-on video environment. `jit.gl.*` objects render OpenGL. Sync to Live's transport.
- **Hardware protocol bridges.** Serial → MIDI, USB-HID → OSC, MQTT → anything. Max speaks every protocol with one or two external objects.
- **Compositional sketches.** Before committing a generative idea to a full M4L device, prototype it as a standalone patch. You do not have to open Live at all until the idea works.

For the course scope, we stay in M4L. But knowing the ceiling exists is useful — a lot of Autechre live-set mysteries dissolve once you realize Max can do literally anything you can wire into it.

`bib:cycling74_max_msp_docs`
