# Good-P Unique Reverse Edge Lemma

Date: 2026-06-09.

Status:

```text
general proved / classifies the aligned right-P edge
```

## Setup

Assume `P` is good. Let:

```text
h=(P*P)*P
h*P=P.
```

By Lemma 13.1(ii), `h` is the unique solution of:

```text
x*P=P.
```

## Unique Fixed Point Of L_P R_P

Suppose:

```text
P*(z*P)=z.
```

Apply E677 with:

```text
x=z
y=P.
```

It gives:

```text
z=P*(z*((P*z)*P)).
```

Comparing with:

```text
z=P*(z*P)
```

and cancelling first in row `P`, then in row `z`, gives:

```text
(P*z)*P=P.
```

Thus `P*z` is a right fixer of `P`, so:

```text
P*z=h.
```

Since row `P` is injective, `z` is unique:

```text
z=L_P^{-1}(h).
```

Write this unique value as:

```text
e=L_P^{-1}(h).
```

Then:

```text
P*e=h
P*(e*P)=e.
```

## Unique Fixed Point Of R_P L_P

Now suppose:

```text
(P*y)*P=y.
```

Set:

```text
z=P*y.
```

Then:

```text
P*(z*P)=P*y=z.
```

By the previous section:

```text
z=e.
```

Therefore `y` is unique:

```text
y=L_P^{-1}(e).
```

Write:

```text
f=L_P^{-1}(e).
```

Then:

```text
P*f=e
e*P=f.
```

## Reverse-Edge Classification

Suppose an edge in the right column `P` is exactly reversed by row `P`:

```text
x*P=Q
P*Q=x.
```

Then:

```text
(P*Q)*P=Q.
```

So `Q` is the unique solution of `R_P L_P(y)=y`. Hence:

```text
Q=f
x=e.
```

Therefore:

```text
x*P=Q and P*Q=x
<=>
x=e and Q=f.
```

There is exactly one row-`P`/column-`P` reverse-aligned edge.

## Exact Six-Cycle Form

For:

```text
P -> C -> f -> e -> h -> 0 -> P
```

the unique reverse-aligned pair is already the known cross-ladder edge:

```text
P*f=e
e*P=f.
```

## Cycle-Entry Consequence

At a cycle-entry fan, two distinct rows satisfy:

```text
x*P=Q
y*P=Q.
```

If either incoming edge is reverse-aligned with row `P`, then necessarily:

```text
Q=f
and that incoming source is e.
```

Thus the aligned cycle-entry role is completely occupied by the known
good-six spine. Every other cycle-entry fan is genuinely non-aligned with row
`P`.

