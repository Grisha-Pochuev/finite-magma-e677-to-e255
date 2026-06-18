# Paired Predecessor Recursion Lemma

Date: 2026-06-05.

Status:

```text
proved recursion / candidate finite-termination framework
```

Purpose:

```text
Replace the growing double interval by two explicit backward recursions.
```

## Setup

Use the nonzero-offset setup:

```text
t=r_2=b_2*0
t!=0
b_3*t=b_4.
```

Define two backward chains.

For row `b_2`:

```text
A_1=t
A_0=0
A_{-1}=u_2=0*(t*b_2).
```

For row `b_3`:

```text
B_1=b_4
B_0=t
B_{-1}=c_{-1}=t*(b_4*b_3).
```

Then:

```text
b_2*A_i=A_{i+1}   for i=-1,0
b_3*B_i=B_{i+1}   for i=-1,0.
```

## Recursion Rule

The edge predecessor triangle says:

```text
a*z=c
=> a*(z*(c*a))=z.
```

Therefore, whenever:

```text
b_2*A_i=A_{i+1},
```

define:

```text
A_{i-1}=A_i*(A_{i+1}*b_2).
```

Then:

```text
b_2*A_{i-1}=A_i.
```

Likewise, whenever:

```text
b_3*B_i=B_{i+1},
```

define:

```text
B_{i-1}=B_i*(B_{i+1}*b_3).
```

Then:

```text
b_3*B_{i-1}=B_i.
```

So the two forced backward chains are:

```text
... -> A_{-2} -> A_{-1}=u_2 -> A_0=0 -> A_1=t

... -> B_{-2} -> B_{-1}=c_{-1} -> B_0=t -> B_1=b_4.
```

with:

```text
A_{i-1}=A_i*(A_{i+1}*b_2)
B_{i-1}=B_i*(B_{i+1}*b_3).
```

## First Collision Roles

For either chain, if the next predecessor equals the current point, then the
current edge is trivial.

Example in the `A` chain:

```text
A_{i-1}=A_i
```

and:

```text
b_2*A_{i-1}=A_i
b_2*A_i=A_{i+1}
```

force:

```text
A_i=A_{i+1}.
```

Thus this can occur only at a self-loop boundary.

If the next predecessor equals the next point:

```text
A_{i-1}=A_{i+1},
```

then row `b_2` swaps:

```text
A_i <-> A_{i+1}.
```

The same role split holds in the `B` chain for row `b_3`.

Therefore a first repeat in either backward chain is not a neutral event.  It
is a self-loop, a self-swap, or a row-cycle closure containing the already
occupied segment:

```text
0 -> t
```

or:

```text
t -> b_4.
```

## Finite-Termination Target

The hard branch can now be stated compactly:

```text
Both backward recursions keep producing new points,
and none of the new A_i or B_i hits:
  the bad-cycle block;
  the other chain;
  row-t pressure columns;
  row-b_4 pressure columns;
  a self-loop/self-swap boundary.
```

Since rows `b_2` and `b_3` are permutations in a finite magma, each chain must
eventually repeat.  The remaining missing proof is not the existence of a
repeat, but the classification:

```text
show that the first repeat or first cross-hit must be one of the already
forbidden pressure roles, rather than a harmless separate row cycle.
```

This is now the cleanest form of the no-free-tail termination problem.
