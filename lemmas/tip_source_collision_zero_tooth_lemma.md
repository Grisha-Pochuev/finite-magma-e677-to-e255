# Tip-Source Collision Zero-Tooth Lemma

Date: 2026-06-08.

Status:

```text
general proved
```

## Statement

Assume two rows belong to the self-containing source fiber:

```text
q*0=P
r*0=P.
```

Suppose the forward tip of row `q` is the other source:

```text
q*P=r.
```

Define:

```text
v=q*r.
```

Then:

```text
v*q=0.
```

Thus every tip-source collision creates an explicit zero tooth:

```text
q*0=P
q*P=r
q*r=v
v*q=0
r*0=P.
```

## Proof

Apply the inverse edge chain to:

```text
q*P=r.
```

It gives:

```text
P=r*((q*r)*q).
```

Using:

```text
v=q*r,
```

this is:

```text
r*(v*q)=P.
```

But:

```text
r*0=P.
```

Row `r` is injective, so:

```text
v*q=0.
```

## Two-Sided Interpretation

Row `q` contains:

```text
0 -> P -> r -> v,
```

and the collision forces:

```text
v ->[row q as right factor] 0
```

in the return row:

```text
v*q=0.
```

Equivalently, the source-orbit ladder for:

```text
q*P=r
q*r=v
```

gives:

```text
r*(v*q)=P,
```

and comparison with `r*0=P` again yields `v*q=0`.

## Significance

The first-hit role:

```text
T_q=r in F(0,P)
```

is no longer an arbitrary fan collision. It immediately enters the existing
zero-tooth and zero-triangle machinery.

The remaining work in this role is to classify the return value:

```text
v*0,
```

or to show that the zero tooth meets an older bad-cycle interval.

