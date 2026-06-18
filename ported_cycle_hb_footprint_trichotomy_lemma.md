# Ported-Cycle H_b Footprint Trichotomy Lemma

Date: 2026-06-18.

Status:

```text
general proved / connector criteria for right-b ported cycles
```

## Purpose

The right-`b` orbit is not itself an `H_b` path.  This lemma records exactly
which equalities inside the generated full-interval cycle do create real
`H_b` incidence.

It refines the gap recorded in:

```text
right_b_orbit_repeat_core_attachment_gap.md
right_b_orbit_ported_transition_lemma.md
```

## Setup

Fix a bad target `b`.  Let:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
x_i*A_i=b.
```

The row `x_i` carries the `H_b` edge:

```text
e_i: A_i -> x_{i+1}.
```

Equivalently, row `x_i` carries the full ported interval:

```text
E_i=(b,A_i,x_{i+1}).
```

For the edge certificate define:

```text
H_i=x_{i+1}*x_i=pred_b(A_i),
```

so:

```text
b*H_i=A_i.
```

Work on a simple segment of the right-`b` orbit before the first repeated
source row, so the source rows `x_i` are pairwise distinct on the displayed
indices.

## Trichotomy

For two generated edges:

```text
e_i: A_i -> x_{i+1},
e_j: A_j -> x_{j+1},
```

with distinct source rows `x_i!=x_j`, exactly the useful incidence types are:

### 1. Same Output: Incoming Fan

If:

```text
x_{i+1}=x_{j+1}=v,
```

then the rows `x_i,x_j` form an incoming common-edge fan at `v`:

```text
x_i*b=v,
x_j*b=v,
x_i!=x_j.
```

Their `H_b` inputs must be distinct:

```text
A_i!=A_j.
```

Otherwise the two rows would carry the same full ported interval:

```text
(b,A_i,v),
```

and two-step source reconstruction would force:

```text
x_i=x_j,
```

contradiction.

Thus in `H_b`:

```text
A_i -> v,
A_j -> v
```

is a genuine incoming fan.

### 2. Same Input: Outgoing Fan

If:

```text
A_i=A_j=A,
```

then the rows `x_i,x_j` form an outgoing common-edge fan from `A`:

```text
x_i*A=b,
x_j*A=b,
x_i!=x_j.
```

Their outputs are distinct:

```text
x_{i+1}!=x_{j+1}.
```

Indeed, if the outputs were also equal, then the full ported intervals:

```text
(b,A,x_{i+1})
```

would coincide and two-step source reconstruction would again force
`x_i=x_j`.

The common fan hub is:

```text
H_i=H_j=pred_b(A),
```

because:

```text
H_i=pred_b(A_i),
H_j=pred_b(A_j).
```

So in `H_b`:

```text
A -> x_{i+1},
A -> x_{j+1}
```

is a genuine outgoing fan.

### 3. Input Hits Output: Actual H_b Concatenation

If:

```text
A_i=x_{j+1},
```

then the generated `H_b` edges concatenate:

```text
A_j -> x_{j+1}=A_i -> x_{i+1}.
```

Thus an input-output hit is the precise condition under which the
right-`b` ported-transition cycle creates an actual directed path segment in
`H_b`.

The adjacent special case:

```text
A_i=x_{i+1}
```

is the already routed same-row swap recurrence:

```text
x_i*x_{i+1}=b,
x_i*b=x_{i+1}.
```

See:

```text
right_b_orbit_local_repeat_roles.md
```

## Clean Matching Residual

If, on a closed right-`b` ported-transition cycle, all routed visible hits are
absent and:

```text
A_i are pairwise distinct,
A_i notin {x_j : j on the cycle},
```

then the generated `H_b` footprint is only a matching:

```text
A_i -> x_{i+1}.
```

It has no internal `H_b` concatenation and no generated outgoing fan.

The first repeat of the right-`b` orbit still creates an incoming fan at the
repeated output, but without an input-output hit or an input repeat, this fan
is not yet core-attached by the generated footprint alone.

## Use In The Clean External-Bridge Residual

The missing connector should now be attacked through this sharper split:

```text
1. A-repeat      -> new outgoing fan in H_b;
2. X-repeat      -> new incoming fan in H_b;
3. A-X hit       -> actual H_b path concatenation / core-attachment candidate;
4. no such hit   -> clean matching residual.
```

Thus the next hard case is no longer a vague ported cycle.  It is the clean
matching residual of the generated `H_b` footprint, together with the row-`b`
predecessor arrows:

```text
b*H_i=A_i.
```

