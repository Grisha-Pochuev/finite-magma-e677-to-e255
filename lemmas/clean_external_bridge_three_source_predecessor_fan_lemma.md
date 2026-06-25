# Clean External-Bridge Three-Source Predecessor-Fan Lemma

Date: 2026-06-18.

Status:

```text
general proved / conceptual coupling lemma
```

## Setup

In the clean external-bridge residual:

```text
p*a=b,  q*a=b,
p*b=c,  q*b=d,

a*k=b,
a*b=t.
```

Define:

```text
h=c*p=d*q=pred_b(a),
ell=t*a=pred_b(k).
```

## Statement

At the pivot element `b`, the three source rows:

```text
p, q, a
```

form a cross-source predecessor fan:

```text
pred_p(b)=a,
pred_q(b)=a,
pred_a(b)=k.
```

In row `b`, the corresponding predecessor columns are:

```text
(p*b)*p = c*p = h,
(q*b)*q = d*q = h,
(a*b)*a = t*a = ell.
```

Thus row `b` contains:

```text
b*h=a,
b*ell=k.
```

In the clean residual:

```text
a!=k,
h!=ell.
```

## Proof

The equations:

```text
p*a=b,
q*a=b,
a*k=b
```

mean:

```text
pred_p(b)=a,
pred_q(b)=a,
pred_a(b)=k.
```

The cross-source predecessor fan lemma says that for each source row `x`, row
`b` contains:

```text
b*((x*b)*x)=pred_x(b).
```

For `x=p`:

```text
(p*b)*p=c*p=h,
b*h=a.
```

For `x=q`:

```text
(q*b)*q=d*q=h,
b*h=a.
```

For `x=a`:

```text
(a*b)*a=t*a=ell,
b*ell=k.
```

Since the clean residual has `a!=k`, row `b` injectivity gives `h!=ell`.

## Use

The clean external bridge is not an isolated new edge.  It upgrades the
original two-source predecessor fan at pivot `b`:

```text
p,q -> predecessor a
```

to a three-source predecessor fan:

```text
p,q,a -> predecessors a,a,k.
```

In the clean residual, row `a` is distinct from the selected rows `p,q,r,s`;
see:

```text
clean_external_bridge_new_source_row_lemma.md
```

The next proof should exploit this three-source fan rather than treating the
right-`b` orbit chain as completely independent.
