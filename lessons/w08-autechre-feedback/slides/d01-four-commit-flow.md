# The four-commit chain, visualized

Four discrete <term key="procedural">procedural</term> acts. Not a macro. Not a preset. A sequence of decisions, each of which renames the MIDI in place before the next decision sees it.

The shape is: generate a grid → scramble while preserving content → bend time non-linearly → un-uniform the velocity → decorate. Per the Live 12 manual's MIDI Transform & Generate chapter, each operation can be previewed before commit — use that. Audition, decide, commit, move on.

If you try to chain two transforms without committing in between, the second one operates on a preview, not on notes, and you lose the ability to revert step-by-step. One commit per act. The commits are the composition.

`bib:ableton_live_12_manual`
