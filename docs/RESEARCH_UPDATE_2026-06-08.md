# Research Update: 2026-06-08

This update records the latest public research progress on the finite-magma
problem `E677 -> E255`.

## Main advance

The project now has a recursive pressure mechanism for a common edge:

```text
q*0=P
q*P=T
T*q=h.
```

Each source `q` creates a bridge

```text
w=(q*T)*q
T*w=P.
```

If

```text
V=T*P,
```

then the bridge extends by

```text
V*T=pred_P(w)
P*(V*T)=w.
```

Thus a fan tip is not a terminal free value.  It creates a new bridge, and the
bridge creates a backward zipper return.

## Connection to the old bad cycle

The terminal element

```text
A=0*0=b_{m-1}
```

is one of the fan sources:

```text
A*0=P.
```

Its backward foot is exactly the old tail:

```text
A*r_{m-2}=0
0*(P*A)=r_{m-2}.
```

This anchors the recursive fan to the original bad cycle.

## New proved files

```text
fan_tip_bridge_expansion_lemma.md
fan_bridge_zipper_extension_lemma.md
terminal_source_anchored_fan_lemma.md
```

The preceding fan-spine and reconstruction layers are indexed in
`docs/RESULTS_INDEX.md`.

## Finite closure update

The complete normalized size-9 role

```text
u=b_3
```

is recorded as closed.  The last two occupied fan-tip roles returned:

```text
C=b_7 -> status none, 46.31s, 640 nodes
C=b_6 -> status none, 28.37s, 410 nodes
```

These are bounded computational results, not a general theorem.

## Current open candidate

The remaining candidate is:

```text
three_source_good_six_pressure_candidate.md
```

Size-9 evidence indicates that the third source is decisive for closing the
good-six-cycle configuration.  A general symbolic proof is still missing.

## Exact next step

Classify the first intersection of the three bridge paths with:

```text
their sources;
existing fan tips;
the good six-cycle;
the terminal anchor r_{m-2}.
```

No new broad computation should be started before this classification.

## Status boundary

The No-Free-Tail Lemma and the full implication `E677 => E255` remain unproved.

