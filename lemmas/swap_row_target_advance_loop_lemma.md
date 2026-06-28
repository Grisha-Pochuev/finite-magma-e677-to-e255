# Swap-Row Target-Advance Loop Lemma

Date: 2026-06-17.

Status:

```text
general proved
```

## Statement

Suppose a row `p` swaps two distinct elements `a,b`:

```text
p*a=b,
p*b=a.
```

Then the edge of `H_b` carried by `p` is a loop at `a`:

```text
A_b(p)=a,
R_b(p)=a.
```

Under target advance, this loop becomes the corresponding loop at `b` in
`H_a`, and the next target advance returns to the original loop:

```text
(target b, row p, loop a -> a)
  -> (target a, row p, loop b -> b)
  -> (target b, row p, loop a -> a).
```

Thus a swap row is a same-row recurrence, not an independent branch-return
incidence.

## Proof

For target `b`, the row `p` has:

```text
p*a=b,
p*b=a.
```

So `A_b(p)=a` and `R_b(p)=a`.

For target `a`, the same two cells read in the opposite order give:

```text
p*b=a,
p*a=b.
```

So `A_a(p)=b` and `R_a(p)=b`.

The target-advance rule for a full ported interval

```text
(target,input,output)=(b,a,c)
```

with `p*a=b` and `p*b=c` is:

```text
(b,a,c) -> (c,b,p*c).
```

Here `c=a`, so:

```text
(b,a,a) -> (a,b,p*a) = (a,b,b).
```

Applying the same rule again gives:

```text
(a,b,b) -> (b,a,p*b) = (b,a,a).
```

Therefore the swap row produces a two-state same-row target-advance loop.

## Use

In the bad-target crossed-fan frontier, any crossed count that depends on a
shared swap row should be routed to the same-row recurrence boundary:

```text
target_advance_row_orbit_lemma.md
ported_interval_recurrence_boundary.md
```

The remaining genuinely crossed case is the proper case where no selected
source row swaps `a` and `b`.
