# Right-b Orbit Ported-Transition Lemma

Date: 2026-06-18.

Status:

```text
general proved / connector in ported-interval state space
```

## Purpose

The right-`b` orbit:

```text
x_{i+1}=x_i*b
```

is not an `H_b` path.  However, it is a canonical path in the stronger state
space of full ported intervals.

This is the correct connector after the core-attachment gap:

```text
right_b_orbit_repeat_core_attachment_gap.md
```

## Setup

Fix a bad target `b`, and define:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
x_i*A_i=b.
```

Then row `x_i` carries the `H_b` edge:

```text
A_i -> x_{i+1}.
```

Equivalently, it carries the full ported interval:

```text
E_i=(b,A_i,x_{i+1})
```

with source row:

```text
x_i.
```

## Transition Rule

Apply the complete edge certificate to the edge:

```text
x_i*A_i=b,
x_i*b=x_{i+1}.
```

For this edge, the certificate gives:

```text
A_{i+1}=(x_i*x_{i+1})*x_i.
```

Indeed, the certificate says that if row `q` carries:

```text
q*A=b,
q*b=C,
```

then:

```text
(q*C)*q = A_b(C).
```

With:

```text
q=x_i,
C=x_{i+1},
```

this is exactly:

```text
(x_i*x_{i+1})*x_i=A_b(x_{i+1})=A_{i+1}.
```

Therefore the next right-`b` orbit source row:

```text
x_{i+1}
```

has its input-to-`b` already produced inside the previous certificate:

```text
x_{i+1}*A_{i+1}=b.
```

So the transition of full ported intervals is:

```text
E_i=(b,A_i,x_{i+1})
  -> E_{i+1}=(b,A_{i+1},x_{i+2}).
```

## Consequences

The right-`b` orbit is not a vertex path in `H_b`, because the next `H_b` edge
starts at `A_{i+1}`, not at `x_{i+1}`.

But it is a genuine path in the ported-interval transition graph:

```text
source row of E_{i+1} = output of E_i.
```

A first repeat:

```text
x_i=x_j
```

is therefore also a same-source repeat of the full ported edge state:

```text
E_i=E_j.
```

This is not a contradiction by itself, because it is the same source row /
same row-orbit recurrence boundary.

If the repeat is internal:

```text
0<i<j,
```

then the preceding states:

```text
E_{i-1}, E_{j-1}
```

have distinct source rows but the same output:

```text
x_i=x_j.
```

This is exactly the incoming-fan regeneration recorded in:

```text
right_b_orbit_first_repeat_fan_lemma.md
```

## Use

The clean external bridge should now be viewed in two layers:

```text
1. H_b layer:
   the generated edges A_i -> x_{i+1} need not concatenate as an H_b path;

2. ported-transition layer:
   the full intervals E_i concatenate canonically because each output becomes
   the next source row.
```

Thus the missing connector is sharper than before:

```text
show that a closed ported-transition cycle born from the clean external bridge
must either hit the visible crossed-fan footprint, produce a cross-role full
ported interval collision, or force a core-attached branch relay.
```

