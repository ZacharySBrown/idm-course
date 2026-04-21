# Follow Actions 2.0 — state-machine architecture

Follow Actions are not random. They are a two-action-per-clip state machine with weighted edges. Live 12 shipped the 2.0 revision with per-scene Follow Actions, <term key="follow_actions">probability</term>, and <term key="legato">legato</term> support. <Citation bib="ableton_live_12_manual" />

Every clip carries:

- **Action A** + **Chance A**
- **Action B** + **Chance B**
- a **trigger interval** (bars/beats/sixteenths)

At each interval Live rolls Chance A vs Chance B, then dispatches to the chosen Action — Stop, Play Again, Previous, Next, First, Last, Any, Other, Jump-to-<clip>.

The *pool* is the whole Session track column. The state machine selects within it.

Key terms — **Any** draws uniformly from the column including the current clip. **Other** excludes the current clip, which is how you get non-repeating variation with zero code.
