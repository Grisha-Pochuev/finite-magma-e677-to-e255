# Cross-Tip Collision Target-Advance Lemma

Date: 2026-06-18.

Status:

```text
general proved / relay routing lemma
```

## Setup

Use crossed-fan notation:

```text
p*a=b,  p*b=c,
r*b=a,  r*a=u.
```

Assume a cross-tip collision:

```text
c=u.
```

So the two rows are:

```text
p*a=b,  p*b=c,
r*b=a,  r*a=c.
```

## Statement

The collision value `c` becomes a common advanced target for the two rows.
Target-advance sends:

```text
row p: (b,a,c) -> (c,b,p*c),
row r: (a,b,c) -> (c,a,r*c).
```

Thus a cross-tip collision routes the crossed-fan branch pair to two
ported intervals with the same new target `c` and opposite inputs `a,b`.

## Proof

For row `p`, the original ported interval with target `b` is:

```text
p*a=b,
p*b=c.
```

By the target-advance form of the ported interval state lemma:

```text
(b,a,c) -> (c,b,p*c).
```

For row `r`, read its two cells with target `a`:

```text
r*b=a,
r*a=c.
```

So the ported interval is:

```text
(a,b,c),
```

and target-advance gives:

```text
(a,b,c) -> (c,a,r*c).
```

Both advanced states have target `c`.

## Distinct Source Rows

The rows `p` and `r` are distinct.  If `p=r`, then:

```text
p*a=b,
r*a=c
```

would give `b=c`, while:

```text
p*b=c,
r*b=a
```

would give `c=a`; hence `a=b`, contradiction.

So the two advanced intervals at target `c` are carried by genuinely distinct
source rows.

## Relation To Hub Separation

The fan certificates give:

```text
c*p=h,
c*r=k.
```

Since row `c` is injective and `p!=r`, we automatically get:

```text
h!=k.
```

This is the same conclusion recorded from the opposite direction in:

```text
crossed_fan_cross_tip_hub_separation_lemma.md
```

## Use In The Proper Bad-Target Crossed-Fan Frontier

A cross-tip collision should now be routed as a relay step:

```text
cross-tip collision at c
=> common advanced target c
=> compare the two full ported intervals
   (c,b,p*c) and (c,a,r*c).
```

The next useful question is not whether the original crossed fan immediately
forces a right-fixer.  It is whether these two advanced intervals:

```text
1. merge into a smaller mixed/branch junction;
2. repeat an old full ported interval;
3. or create a side attachment in the minimal relay corridor.
```
