# StemForgeLoader.amxd — the loader does the plumbing

This is also the dedicated Max for Live lesson of the course. One device, one job.

What the loader does when you drag it onto a MIDI track and press its button:

- Auto-creates **seven template tracks** — SF Source, Drums Rack, Bass Rack, Vocals Rack, Other Rack, Chromatic Simpler, Beat Chop Simpler.
- Each Rack template arrives with its own effect chain wired — EQ, gate, compressor, a send to a shared reverb.
- For a song manifest, the loader duplicates the Drums Rack template, renames it `Drums Rack | <song>`, and walks the manifest — each one-shot into its Simpler at chromatic C1 upward.
- Templates stay untouched; duplicates are what you edit.

Screenshots deferred to Wave 5. The loader is in the stemforge repo under `m4l/`. For this lesson we will point it at the `w03-express-oneshots` output.

[ref: bib:stemforge_repo]
