# First Right-b Successor Fan-Attachment Lemma

Date: 2026-06-18.

Status:

```text
general proved / routing classification
```

## Setup

In the clean external-bridge residual, let:

```text
t=a*b,
ell=t*a.
```

Thus `t` is the first successor of `a` in the right-`b` orbit.

## Statement

The first successor `t` has two immediate fan-attachment tests.

### 1. `ell=b`

Since:

```text
ell=t*a,
```

the equality `ell=b` is exactly:

```text
t*a=b.
```

So row `t` belongs to the outgoing fiber:

```text
F(a,b)={x:x*a=b}.
```

If `t` is distinct from the selected source rows `p,q`, this enlarges the
outgoing fan at `a`.

### 2. `t*b=a`

Then row `t` belongs to the incoming-side fiber:

```text
F(b,a)={x:x*b=a}.
```

If `t` is distinct from the selected source rows `r,s`, this enlarges the
incoming side.

This equality also means the right-`b` orbit has a two-cycle:

```text
a -> t -> a.
```

## Badness Boundary

Badness of `b` forbids:

```text
t*b=b.
```

but it does not forbid:

```text
t*b=a.
```

Therefore the return `t*b=a` is a routed orbit-cycle / enlarged-fan boundary,
not an immediate contradiction.

## Clean Residual Use

The clean external-bridge residual may route out the cases:

```text
ell=b,
t*b=a.
```

If neither occurs, the first right-`b` successor does not immediately enlarge
the selected crossed fan.

