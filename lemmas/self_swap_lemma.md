# Self-Swap Lemma

Status:

```text
historical working lemma / recurring closure pattern
```

This file records the self-swap mechanism used in earlier finite branch
closures.

## Idea

A self-swap is a short forced exchange between two values.  In the project
notation it often appears as a two-step return rather than a free tail.

Instead of allowing a branch to keep producing new values, the self-swap forces
the branch back into a small occupied configuration.

## Why it mattered

Self-swap behavior repeatedly turned dangerous-looking residual branches into
closed branches.

## Current role

The current frontier contains a direct descendant of this case:

```text
u_2=t -> origin self-swap 0 <-> t in row b_2
```

See:

```text
docs/CURRENT_FRONTIER.md
lemmas/double_interval_pressure_lemma.md
```

