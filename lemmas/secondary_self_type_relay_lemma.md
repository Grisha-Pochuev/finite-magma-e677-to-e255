# Secondary Self-Type Relay Lemma

Status:

```text
historical relay candidate
```

This file summarizes a relay pattern involving secondary self-type behavior.

## Idea

When a branch produced a secondary self-return or self-swap, `E677` often
forced the branch to relay into an older occupied row rather than continue as
a fresh tail.

Schematic form:

```text
self-type edge
  -> predecessor relay
  -> occupied-row pressure
  -> closure or descent
```

## Current role

This pattern is now treated as one of several ways a fresh tail can fail.  It
is conceptually related to:

```text
self_swap_lemma.md
double_interval_pressure_lemma.md
```

