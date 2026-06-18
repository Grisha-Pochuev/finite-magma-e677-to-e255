# Good Six-Cycle Cross-Ladder Lemma

Date: 2026-06-08.

Status:

```text
general proved / exact structure, termination not yet proved
```

## Setup

Assume the exact row-`P` six-cycle:

```text
P -> C -> f -> e -> h -> 0 -> P.
```

Thus:

```text
P*P=C
P*C=f
P*f=e
P*e=h
P*h=0
P*0=P.
```

Assume `P` is good:

```text
h*P=P.
```

## Backward Zipper

Apply the source-orbit zipper to:

```text
f -> e -> h
```

in row `P`. It gives:

```text
e*(h*P)=f.
```

Using:

```text
h*P=P,
```

we obtain:

```text
e*P=f.
```

Apply the zipper to:

```text
C -> f -> e.
```

It gives:

```text
f*(e*P)=C.
```

Therefore:

```text
f*f=C.
```

This recovers the fourth-predecessor good-P cell directly from the row cycle.

## Right-Column Three-Cycle

The fixed-source descent already gives:

```text
C*P=h.
```

Together with goodness:

```text
h*P=P.
```

and:

```text
P*P=C,
```

the right column `P` contains the three-cycle:

```text
P -> C -> h -> P.
```

The same column also contains:

```text
e -> f.
```

So the exact six-cycle creates simultaneous cycles in:

```text
the left row P;
the right column P.
```

## New Return k

Define:

```text
k=f*P.
```

Apply the zipper to:

```text
P -> C -> f
```

in row `P`. It gives:

```text
C*(f*P)=P.
```

Hence:

```text
C*k=P.
```

Equivalently:

```text
k=pred_C(P).
```

The value `k` cannot be `P`, because:

```text
C*P=h
C*k=P
h!=P.
```

Thus:

```text
k!=P.
```

## Immediate k-Roles

```text
k=h:
  row C swaps P and h:
    C*P=h
    C*h=P;

k=C:
  row C contains C -> P -> h;

k=0:
  C*0=P;

k occupied:
  row C gains a new forced edge k -> P beside P -> h;

k fresh:
  the six-cycle creates a new active predecessor of P in row C.
```

## Occupied Central Tip

If:

```text
C=b_j
h=b_{j-1},
```

then row `C=b_j` already has the bad-cycle ladder edge:

```text
C*r_{j-1}=b_{j+1}.
```

The good six-cycle adds:

```text
C*P=h
C*k=P.
```

So row `b_j` contains three forced outputs:

```text
r_{j-1} -> b_{j+1}
P       -> b_{j-1}
k       -> P.
```

Every collision among the three columns is now explicit:

```text
k=P       -> impossible;
k=r_{j-1} -> P=b_{j+1};
P=r_{j-1} -> h=b_{j+1}.
```

Outside those collision roles, this is genuine three-edge occupied-row
pressure.

## Significance

The good length-six role is not merely:

```text
f*f=C.
```

It is the cross-ladder:

```text
row P:
  P -> C -> f -> e -> h -> 0 -> P

column P:
  P -> C -> h -> P
  e -> f
  f -> k

row C:
  k -> P -> h.
```

The next classifier is:

```text
k=f*P.
```

The desired termination step is to show that `k` cannot remain fresh while
the row-`C` bad-cycle edge and the additional fan tips also avoid collision.

This classifier is now recognized as a general fan-tip bridge:

```text
fan_tip_bridge_expansion_lemma.md
```

For the self source `q=P`, its tip is `C` and its bridge is exactly:

```text
w_P=(P*C)*P=f*P=k.
```

The bridge zipper adds:

```text
h*C=pred_P(k)
P*(h*C)=k.
```

Consequently:

```text
k!=C,
```

because `k=C` would force both `h*C=P` and `h*P=P`.

Thus the self bridge already avoids:

```text
k notin {P,C}.
```
