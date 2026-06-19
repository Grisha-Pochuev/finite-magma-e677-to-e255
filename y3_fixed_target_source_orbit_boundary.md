# Y3 Fixed-Target Source-Orbit Boundary

Date: 2026-06-19.

Status:

```text
boundary / Y3 source rows reduce to two right-A_j source orbits in H_{A_j}
```

## Purpose

This continues:

```text
y3_three_cycle_first_intersection_boundary.md
fixed_target_source_successor_lemma.md
```

The clean Y3 residual has three source rows through `A_j`:

```text
p, x_j, b.
```

But inside the fixed target graph `H_{A_j}`, these are not three independent
source-successor starts.  Since:

```text
x_j*A_j=b,
```

the row `b` is already the next right-`A_j` source successor of `x_j`.

## Source-Orbit Setup

For a fixed target:

```text
T=A_j,
```

define the right-`T` source successor:

```text
R_T(r)=r*T.
```

The `H_T` edge carried by row `r` is:

```text
pred_r(T) -> r*T.
```

By:

```text
fixed_target_source_successor_lemma.md
```

an `H_T` edge carried by `r` forces the next `H_T` edge carried by:

```text
R_T(r).
```

## Y3 Two-Orbit Form

The clean Y3 source rows lie on two right-`A_j` source orbits:

```text
P-orbit:       p -> S -> S*A_j -> ...

generated orbit:
               x_j -> b -> D_j -> D_j*A_j -> ...
```

because:

```text
p*A_j=S,
x_j*A_j=b,
b*A_j=D_j.
```

Thus the third row `b` is a built-in successor in the generated orbit, not an
independent source direction.

## First Source-Orbit Hit Split

Compare the two source-successor orbits:

```text
p, S, S*A_j, ...
```

and

```text
x_j, b, D_j, D_j*A_j, ...
```

The first event is one of:

```text
1. the P-orbit hits the generated source orbit;
2. one orbit hits the visible crossed-fan/core footprint;
3. one orbit hits a generated A/X/H/Beta layer in a nonlocal role;
4. an orbit repeats one of its own source rows before any cross-hit;
5. both orbits remain clean until they enter disjoint source cycles.
```

Cases 1-3 are routed hits.

In case 1, the same source row appears in `H_{A_j}` in both roles.  Since the
target is the same, the full ported interval is the same:

```text
(A_j, pred_r(A_j), r*A_j).
```

So this is not a new bridge; it is a source-row collision between the two Y3
layers.

Case 4 is a fixed-target source recurrence boundary.  It repeats the same
source row and hence the same full ported interval in `H_{A_j}`.  It is weak
by itself, but useful when paired with the left-row cycle comparison from:

```text
y3_three_cycle_first_intersection_boundary.md
```

## Remaining Clean Residual

The only source-orbit residual left by this split is:

```text
Z3-source. two clean disjoint right-A_j source cycles in H_{A_j},
           one born from p and one born from x_j -> b.
```

Together with:

```text
Z3. clean disjoint three left-row cycles through A_j,
```

the Y3 obstruction is now a coupled two-direction cycle shell:

```text
left-row cycles through A_j:
  row p, row x_j, row b;

fixed-target source cycles in H_{A_j}:
  p -> S -> ...
  x_j -> b -> D_j -> ...
```

The next useful question is whether the shared first step:

```text
p*A_j=S
```

can make the left row-`p` cycle:

```text
A_j -> S -> p*S -> ...
```

stay disjoint from the right-`A_j` source orbit:

```text
p -> S -> S*A_j -> ...
```

without producing a watched hit or a repeated ported interval.

