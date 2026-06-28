# Fan-Spine Fourth-Predecessor Test

Date: 2026-06-08.

Status:

```text
general proved / exact dichotomy for longer row-P closure
```

## Setup

Use the fan spine:

```text
P*0=P
P*P=C
C*P=h
P*h=0
P*e=h.
```

Extend row `P` two more steps backward:

```text
P*f=e
P*g=f.
```

Equivalently:

```text
f=L_P^{-4}(P)
g=L_P^{-5}(P).
```

The edge-predecessor triangle gives explicit forms:

```text
f=e*(h*P)
g=f*(e*P).
```

## E255 Test At P

The fixed-point criterion for E255 at `P` says:

```text
P*(f*f)=f.
```

But:

```text
P*g=f.
```

Since row `P` is injective:

```text
P*(f*f)=f
<=>
f*f=g.
```

Therefore:

```text
E255 holds at P
<=>
f*f=g.
```

There is also the direct E255 form:

```text
((P*P)*P)*P=(C*P)*P=h*P.
```

Hence the equivalent test:

```text
E255 holds at P
<=>
h*P=P.
```

Combining:

```text
f*f=g
<=>
h*P=P.
```

## Badness Dichotomy

Exactly one of the following occurs:

```text
good-P role:
  f*f=g
  h*P=P;

bad-P role:
  f*f!=g
  h*P!=P.
```

Thus a longer row-`P` cycle closure is not an unstructured event. Its fourth
backward predecessor supplies one exact deciding cell.

## Minimal-Bad-Cycle Consequence

Choose the original bad element `0` with minimal own-row cycle length `m`.

Let the own row-`P` cycle have length `ell`.

If:

```text
ell<m,
```

then `P` cannot be bad. Therefore:

```text
f*f=g
h*P=P.
```

Conversely, if:

```text
f*f!=g,
```

then `P` is bad, so minimality forces:

```text
ell>=m.
```

For the shortest closure `e=C`, one has:

```text
ell=4
f=P
g=0
f*f=C!=0,
```

which recovers the four-cycle badness transfer.

## New Frontier

The longer-cycle branch now has a precise split:

```text
shorter-than-minimal closure
  -> forced good-P cell f*f=g;

bad-P closure
  -> its cycle cannot be shorter than the original minimal bad cycle.
```

The next useful question is whether the forced good-P cell `f*f=g`, together
with:

```text
row P: g -> f -> e -> h -> 0 -> P -> C,
```

creates an aligned overlap or a new common-edge fan.

