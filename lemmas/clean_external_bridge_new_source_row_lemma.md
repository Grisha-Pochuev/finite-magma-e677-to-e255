# Clean External-Bridge New Source Row Lemma

Date: 2026-06-18.

Status:

```text
general proved / clean residual separation
```

## Setup

In the clean external-bridge residual, use the selected crossed-fan rows:

```text
p*a=b,  q*a=b,
p*b=c,  q*b=d,

r*b=a,  s*b=a,
r*a=u,  s*a=v.
```

Let:

```text
t=a*b.
```

The clean residual routes out:

```text
t in {a,c,d}.
```

## Statement

In the clean external-bridge residual:

```text
a notin {p,q,r,s}.
```

So row `a` is a genuinely new source row relative to the selected crossed-fan
sources.

## Proof

If:

```text
a=p,
```

then:

```text
t=a*b=p*b=c,
```

contradicting the clean residual condition `t notin {c,d}`.

If:

```text
a=q,
```

then:

```text
t=a*b=q*b=d,
```

again contradicting `t notin {c,d}`.

If:

```text
a=r,
```

then:

```text
t=a*b=r*b=a,
```

contradicting `t!=a`.

The case `a=s` is identical:

```text
t=a*b=s*b=a.
```

Thus `a` is distinct from all four selected source rows.

## Use

The three-source predecessor fan:

```text
p,q,a
```

at pivot `b` really uses a third source row, not one of the already selected
crossed-fan rows.  This strengthens:

```text
clean_external_bridge_three_source_predecessor_fan_lemma.md
```
