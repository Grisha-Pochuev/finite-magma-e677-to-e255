# Bad-Target No Predecessor-Output Lemma

Date: 2026-06-18.

Status:

```text
general proved
```

## Statement

Fix a bad target `b`.  For any element `x`, let:

```text
h=pred_b(x),
```

so:

```text
b*h=x.
```

Then:

```text
x*b != h.
```

Equivalently:

```text
x*b != pred_b(x)
```

for every `x`.

## Stronger Conditional Form

If:

```text
x*b=pred_b(x),
```

then:

```text
(b*x)*b=b.
```

So `b*x` right-fixes `b`, contradicting badness.

## Proof

Assume:

```text
h=pred_b(x),
b*h=x,
x*b=h.
```

Apply E677 with:

```text
x=x,
y=b.
```

It gives:

```text
x = b*(x*((b*x)*b)).
```

Since:

```text
b*h=x,
```

and row `b` is injective:

```text
h = x*((b*x)*b).
```

But:

```text
x*b=h.
```

Therefore:

```text
x*b = x*((b*x)*b).
```

Row `x` is injective, hence:

```text
b=(b*x)*b.
```

Thus `b*x` right-fixes `b`.  This is impossible when `b` is bad.

## Graph Interpretation

For bad target `b`, the self-labeled `H_b` edge carried by row `x` is:

```text
pred_x(b) -> x*b.
```

This lemma says its output can never be the `b`-predecessor of its own row
label:

```text
x*b != pred_b(x).
```

So a self-labeled edge cannot return directly to the opposite bridge of its
label.

