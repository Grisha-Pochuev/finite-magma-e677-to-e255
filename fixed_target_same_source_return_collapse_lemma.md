# Fixed-Target Same-Source Return Collapse Lemma

Date: 2026-06-20.

Status:

```text
proved / fixed-target return cleanup
```

## Statement

Fix a target `b` and a vertex `v` in `H_b`.

Suppose the same source row `r` gives two incoming ported incidences into
`v`:

```text
r*x=b,  r*b=v,
r*y=b,  r*b=v.
```

Then:

```text
x=y.
```

So these are not two distinct return incidences.  They are the same full
ported interval:

```text
(b,x,v)=(b,y,v).
```

## Proof

In a finite E677 magma every row map is injective.  Since:

```text
r*x=b,
r*y=b,
```

row injectivity gives:

```text
x=y.
```

The output port is already the same vertex `v`, because both incidences use
`r*b=v`.

Thus the two displayed incidences are identical.

## Consequence For Relay Returns

A genuine second return to the same old split vertex inside a fixed target
graph `H_b` cannot be a new same-source incidence.  It has only two roles:

```text
1. identical to the already used edge, so it is not a new core return;
2. realized by a different source row, hence it is an independent return.
```

By:

```text
relay_same_source_return_split_boundary.md
figure_eight_closure_crossed_fan_boundary.md
```

case 2 routes to the crossed-fan / clean-bridge reductions.

Therefore the remaining same-source recurrence in G12 is not a fixed-target
double return to the old split.  It is only the target-advance row-orbit
phenomenon from:

```text
target_advance_row_orbit_lemma.md
ported_interval_recurrence_boundary.md
```

In plain terms: if the relay has really come back to the same target `b` and
the same split `v`, then "same source row" means "same edge again", not a new
branch of the core.
