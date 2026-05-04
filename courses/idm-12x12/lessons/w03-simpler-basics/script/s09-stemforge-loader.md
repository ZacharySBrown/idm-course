StemForgeLoader.amxd. This is also the dedicated Max for Live lesson of the course. One device, one job, worth knowing.

[pause 400ms]

The problem the loader solves is boring and therefore worth solving — every time you want to audition a new stemforge-generated kit in a new Live set, you would otherwise have to: create seven tracks, load a Drum Rack on one, load an Instrument Rack on three more, set up a Simpler for chromatic chopping, set up another Simpler for beat chopping, wire an effect chain to each, and then walk through the stemforge manifest and drop each one-shot onto the correct pad at the correct MIDI note.

That is fifteen to twenty minutes of mouse work, and you do it every session. Every producer who has done this more than three times has quietly thought about writing a Max for Live device to automate it. The loader is that device.

[pause 500ms]

What it does when you drag it onto a MIDI track and press its button.

It auto-creates **seven template tracks**. In order — SF Source, Drums Rack, Bass Rack, Vocals Rack, Other Rack, Chromatic Simpler, and Beat Chop Simpler. Each of the Rack tracks arrives with its own pre-wired effect chain — an EQ, a gate on the drums, a compressor, a send to a shared reverb bus, and output routing set to the default audio out.

The templates are the blueprint. You do not edit them. That is Phase One of the loader's lifecycle — templates present in the set.

Then — for a given song manifest — the loader moves to Phase Two. It duplicates the Drums Rack template, renames the copy to *Drums Rack | song-name*, and walks the manifest. For each one-shot in the manifest — kick, snare, hat, tom, cymbal — the loader navigates into the correct Simpler inside the correct pad in the duplicated rack, and calls `replace_sample` with the path to the one-shot file. Chromatic layout, C1 upward. Same for bass, vocals, and other racks when their manifests are present.

[pause 500ms]

The template tracks remain untouched. The duplicates are what you edit. If you load a new song, the loader duplicates again — new copies, new song suffix, old ones left alone.

[pause 400ms]

Screenshots are deferred to Wave Five, so you are reading this without pictures. The loader lives in the stemforge repository at `/Users/zak/zacharysbrown/stemforge/m4l/`. For this week's exercise, we will point it at the `w03-express-oneshots` output and let it build the song-specific Drums Rack from the *Express Yourself* one-shot pack.

[pause 300ms]

~That is the M4L lesson.~ One device. Knows what to do. Out of your way.
