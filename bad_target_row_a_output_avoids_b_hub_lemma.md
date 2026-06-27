# Bad-Target Row-a Output Avoids b-Hub Lemma

Date: 2026-06-18.

Status:

```text
general proved / specialization of bad_target_no_predecessor_output_lemma.md
```

## Setup

Fix a bad target `b` and an element `a!=b`.  Let:

```text
h=pred_b(a),
```

so:

```text
b*h=a.
```

Assume row `a` has:

```text
a*b=h.
```

## Statement

Then:

```text
(b*a)*b=b.
```

Therefore, if `b` is bad, the assumption `a*b=h` is impossible.

Equivalently, in any bad-target crossed-fan setting:

```text
a*b != pred_b(a).
```

This is the `x=a` instance of:

```text
bad_target_no_predecessor_output_lemma.md
```

## Proof

Apply E677 with:

```text
x=a,
y=b.
```

It gives:

```text
a = b*(a*((b*a)*b)).
```

But:

```text
b*h=a.
```

Since row `b` is injective, the two inputs sent by row `b` to `a` must be
equal:

```text
h = a*((b*a)*b).
```

By assumption:

```text
a*b=h.
```

So:

```text
a*b = a*((b*a)*b).
```

Row `a` is injective, hence:

```text
b=(b*a)*b.
```

Thus `b*a` right-fixes `b`.

For a bad target, no row right-fixes `b`, so `a*b=h` is impossible.

## Use In The Row-a Bridge Edge

In the crossed-fan row-a bridge edge:

```text
a*k=b,
a*b=t,
k -> t in H_b,
```

the output cannot be the `b`-hub:

```text
t!=h.
```

This removes one possible bridge-edge return into the hub `h`.

## Diagnostic Check

The bounded saturation script agrees: with flag `ab=h`, it finds short
right-fixers of `b`, including `b*a`.

```text
tools/crossed_double_fan_saturation.js 4 ab=h
```

The proof above is independent of that diagnostic.
