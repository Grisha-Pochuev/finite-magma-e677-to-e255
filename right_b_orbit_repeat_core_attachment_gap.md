# Right-b Orbit Repeat Core-Attachment Gap

Date: 2026-06-18.

Status:

```text
boundary correction / missing connector lemma
```

## Purpose

The right-`b` orbit first-repeat lemma is valid, but its use in the clean
external-bridge residual needs one extra connector step.

The first repeat creates an incoming fan in `H_b`.  It does not automatically
prove that this fan lies in the same cyclic core component as the original
proper crossed fan.

## Setup

For a bad target `b`, take the right-`b` orbit:

```text
x_{i+1}=x_i*b.
```

For each orbit label:

```text
A_i=pred_{x_i}(b),
x_i*A_i=b,
x_i*b=x_{i+1}.
```

So row `x_i` contributes the `H_b` edge:

```text
A_i -> x_{i+1}.
```

## The Proved Fan-Regeneration Step

If the first repeat is internal:

```text
x_i=x_j=v,
0<i<j,
```

then the predecessor labels:

```text
y=x_{i-1},
z=x_{j-1}
```

satisfy:

```text
y*b=v,
z*b=v,
y!=z.
```

Therefore the rows `y,z` create two incoming `H_b` edges into `v`:

```text
A_{i-1} -> v,
A_{j-1} -> v,
A_{i-1}!=A_{j-1}.
```

This is the content of:

```text
right_b_orbit_first_repeat_fan_lemma.md
```

## The Missing Connector

The sequence:

```text
x_0, x_1, x_2, ...
```

is a right-translation orbit:

```text
x_{i+1}=x_i*b.
```

It is not itself an `H_b` path.  The corresponding `H_b` edges are:

```text
A_i -> x_{i+1}.
```

The next edge starts at `A_{i+1}`, not at `x_{i+1}`.  Thus consecutive
right-`b` orbit steps do not automatically concatenate inside `H_b`.

Consequently:

```text
first repeat of x_i
=> incoming fan in H_b
```

but not yet:

```text
=> incoming fan in the original cyclic core component.
```

## Corrected Use In The Clean External Bridge

In the clean external-bridge residual, the row-a bridge gives the first edge:

```text
A_0=k,
x_1=t,
k -> t in H_b.
```

The successor edge is:

```text
A_1 -> x_2,
```

where generally:

```text
A_1 != t.
```

So the clean external bridge is not closed merely by saying that the
right-`b` orbit eventually repeats.

The missing lemma should show one of:

```text
1. some A_i or x_i visibly attaches to the original crossed-fan/core footprint;
2. two generated H_b edges share a full ported interval in independent roles;
3. the generated incoming fan is forced into the same bad-target core by an
   additional predecessor-fan/cross-source relation;
4. or the independent orbit cycle is a genuine remaining same-row recurrence
   boundary.
```

## Consequence

Future work should distinguish:

```text
fan regeneration
```

from:

```text
core-attached branch relay.
```

The former is proved.  The latter is the next connector lemma, not yet proved.

