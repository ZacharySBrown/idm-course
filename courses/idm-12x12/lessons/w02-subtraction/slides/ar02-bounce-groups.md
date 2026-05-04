# Bounce Groups — Live 12.3's commit-to-tape button

<term key="bounce_groups">Bounce Groups</term> landed in Live 12.3 (2025). Right-click a <term key="group_track">group track</term> header → **Bounce Group**. Ableton consolidates the group's output to a single audio track, preserving the group's send/insert state as a frozen artifact.

**Parameter table — what the dialog asks:**

| Parameter          | Default                | What it does                                   |
|--------------------|------------------------|------------------------------------------------|
| Render range       | Entire arrangement     | Or loop region, or selected time               |
| Sample rate        | Project rate (48 kHz)  | Inherits project unless overridden             |
| Bit depth          | 32-bit float           | Keep at 32-bit for reversible headroom         |
| Include return fx  | On                     | Captures send-returns into the bounced region  |
| Delete source      | Off                    | Keep off until you are sure; destructive       |
| Preserve sidechain | Group-internal only    | External sidechains are not captured           |

**For Subtraction.** Bounce the Peak group *before* you mute anything. Frozen audio is cheap to mute, expensive to un-freeze. The expense is the feature — it forces commitment. `bib:ableton_live_12_manual`.
