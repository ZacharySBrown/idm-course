# StemForgeLoader.amxd — the UI

The screenshot shows the loader device in Live's device view. Single rack with a Manifest path field, a Build button, a template-list readout, and an operation log.

What you see:

- **Manifest path** — the `.json` produced by a stemforge recipe. For this week, point it at `build/audio/stemforge-renders/w03/express_oneshots/manifest.json`.
- **Build** button — the single action. Duplicates the Drums Rack template, renames to `Drums Rack | <song>`, loads each one-shot into its Simpler at chromatic C1 upward.
- **Operation log** — one line per action. Track rename, Simpler load, chain add. Use it to audit what the loader did.
- **Templates** — the seven template tracks are created on first run if missing. SF Source, Drums Rack, Bass Rack, Vocals Rack, Other Rack, Chromatic Simpler, Beat Chop Simpler.

Screenshot deferred to Wave 5 if the device UI changes between now and render.

[ref: bib:stemforge_repo]
