# Case45 Relay Progress

Status:

```text
historical progress note / relay mechanism source
```

This file summarizes the relay mechanism found during the case45 analysis.

## Core idea

The branch did not close because isolated cells were filled one by one.  It
closed because `E677` repeatedly transferred pressure from one row to another.

Typical pattern:

```text
one forced edge creates a predecessor edge;
the predecessor edge creates a relay;
the relay either hits 0, returns to an occupied row, or forces a collision.
```

## Why it mattered

The relay behavior in case45 later informed the global no-free-tail strategy.
Instead of trying to enumerate all possible finite tables, the project searches
for a structural reason why fresh tails cannot continue indefinitely.

## Related files

```text
relay_graph_lemma.md
row6_orbit_relay_lemma.md
row6_compact_residual_lemma.md
source_orbit_ladder_lemma.md
source_orbit_zipper_lemma.md
```

