# Same-Input Split Target-Lift Lemma

Date: 2026-06-18.

Status:

```text
proved transport lemma / routes same-input split to a common target graph
```

## Purpose

This records the correct reusable treatment of a same-input split.

A same-input split is not a common-edge fan by itself:

```text
p*z=s,
q*z=r,
s!=r.
```

But E677 lets us lift both rows to the same target graph `H_z`.

## General Statement

Assume rows are left-cancellative, as in finite E677, and:

```text
p*z=s,
q*z=r.
```

Define:

```text
P_z = z*(s*p),
Q_z = z*(r*q).
```

By E677:

```text
p*P_z=z,
q*Q_z=z.
```

Therefore, in the common target graph `H_z`, the two rows give:

```text
P_z -> p*z=s     carried by row p,
Q_z -> q*z=r     carried by row q.
```

So the same-input split at `z` becomes a same-target pair in `H_z`.

## Immediate Consequences

If:

```text
P_z=Q_z
```

and:

```text
s!=r,
```

then `H_z` has an outgoing fan at the common input `P_z`.

If one of:

```text
P_z, Q_z
```

hits a watched layer, the split is routed through that hit.  If both are
fresh, the same-input split has been replaced by a precise fresh pair in a
single target graph, not by an unstructured residual.

## Application 1: X-Layer `alpha=A_j`

In the G branch:

```text
H_i=x_j,
b*x_j=A_i,
x_j*A_j=b.
```

If additionally:

```text
alpha=A_j,
```

then:

```text
b*A_j=x_j,
x_j*A_j=b.
```

Apply the general lemma with:

```text
p=b,
q=x_j,
z=A_j,
s=x_j,
r=b.
```

The lifted feet are:

```text
P_z=A_j*(x_j*b)=A_j*x_{j+1}=H_j,
Q_z=A_j*(b*x_j)=A_j*A_i=gamma=Beta_j.
```

Thus in `H_{A_j}`:

```text
H_j    -> x_j     carried by row b,
Beta_j -> b       carried by row x_j.
```

So the `alpha=A_j` same-input split is not an independent G residual.  It
couples directly to the beta layer at index `j`.

In particular:

```text
Beta_j=H_j
```

creates an outgoing fan in `H_{A_j}` unless `x_j=b`, which is excluded in the
clean bad-target orbit.

## Application 2: Beta-A Hit `Beta_i=A_j`

If:

```text
Beta_i=A_j,
```

then:

```text
x_i*A_j=A_i,
x_j*A_j=b.
```

Apply the general lemma with:

```text
p=x_i,
q=x_j,
z=A_j,
s=A_i,
r=b.
```

Define:

```text
E_{i,j}=A_j*(A_i*x_i).
```

Since:

```text
Beta_j=pred_{x_j}(A_j)=A_j*(b*x_j),
```

the lift gives, in `H_{A_j}`:

```text
E_{i,j} -> A_i     carried by row x_i,
Beta_j  -> b       carried by row x_j.
```

Therefore the beta-A hit is also not an isolated residual.  It transfers the
pressure from `Beta_i` to the next beta foot `Beta_j`, plus one explicit new
foot `E_{i,j}`.

Immediate roles:

```text
E_{i,j}=Beta_j -> outgoing fan in H_{A_j};
E_{i,j}=A_j    -> A_i=A_j, routed A-repeat;
E_{i,j}=A_i    -> A_j=b, impossible in the clean bad-target orbit.
```

Other hits of `E_{i,j}` are routed by the layer they hit.  If `E_{i,j}` is
fresh and `Beta_j` is fresh, the remaining object is a precise same-target
fresh pair in `H_{A_j}`.

## Consequence For The Current Frontier

The same-input split branches from:

```text
alpha=A_j,
Beta_i=A_j
```

should no longer be listed as opaque independent residuals.  They feed into:

```text
1. a concrete outgoing fan in H_{A_j};
2. a generated A/X hit;
3. an impossibility;
4. or a beta-coupled fresh same-target pair.
```

The remaining hard case is therefore not "same input" itself, but a fresh
beta-coupled same-target pair.
