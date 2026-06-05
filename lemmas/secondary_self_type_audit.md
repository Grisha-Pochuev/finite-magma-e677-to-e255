# Secondary Self-Type Audit

Status:

```text
historical audit
```

This audit separated genuine self-type closures from diagnostic artifacts in
the case45 analysis.

## Audit purpose

Some branches appeared to close when a value behaved like a self-return or
self-swap.  The audit checked whether those closures were supported by forced
`E677` edges rather than by unproved assumptions.

## Categories

```text
proved self-return
proved self-swap
diagnostic self-type pressure
unusable heuristic observation
```

## Current role

The current frontier still uses this caution.  In particular, the role

```text
u_2=t
```

in `docs/CURRENT_FRONTIER.md` should be treated as a precise self-swap case,
not as an informal guess.

