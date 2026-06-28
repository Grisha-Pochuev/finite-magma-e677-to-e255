# Right-b Orbit Local Repeat Roles

Date: 2026-06-18.

Status:

```text
general proved / role classification
```

## Setup

Fix a bad target `b`.  Let:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
H_i=x_{i+1}*x_i=pred_b(A_i).
```

Then:

```text
x_i*A_i=b,
x_i*b=x_{i+1},
b*H_i=A_i.
```

So row `x_i` carries the `H_b` edge:

```text
A_i -> x_{i+1},
```

and row `b` carries the predecessor arrow:

```text
H_i -> A_i.
```

## Bad-Target Restrictions

For every `i`:

```text
x_i!=b,
x_{i+1}!=b,
A_i!=b,
x_{i+1}!=pred_b(x_i).
```

The first two hold because if `x_i=b` for `i>0`, then `x_{i-1}*b=b`,
contradicting badness; and `x_0` is chosen outside `b` in the crossed-fan
application.  The third follows from `x_i*A_i=b`: if `A_i=b`, then
`x_i*b=b`.  The fourth is:

```text
bad_target_no_predecessor_output_lemma.md
```

applied to `x_i`.

## Local Repeat Roles

### 1. `A_i=x_{i+1}`

Then:

```text
x_i*x_{i+1}=b,
x_i*b=x_{i+1}.
```

So row `x_i` swaps `b` and `x_{i+1}`.  In `H_b`, the edge is a loop:

```text
x_{i+1} -> x_{i+1}.
```

Under target advance, this is a same-row recurrence:

```text
(b,x_{i+1},x_{i+1})
  -> (x_{i+1},b,b)
  -> (b,x_{i+1},x_{i+1}).
```

Thus `A_i=x_{i+1}` is routed to the same-row recurrence boundary.

### 2. `A_i=x_i`

Then:

```text
x_i*x_i=b.
```

So row `x_i` belongs to the outgoing fiber `F(x_i,b)`.  This is an enlarged
self-source fan boundary if `x_i` is part of a current visible footprint.  It
is not automatically a contradiction.

### 3. `x_{i+1}=x_i`

Then:

```text
x_i*b=x_i.
```

The right-`b` orbit has a fixed point at `x_i`.  Since `x_i!=b`, this does not
contradict badness of `b`.  It is a closed right-`b` orbit boundary and must be
handled by additional predecessor-fan pressure.

### 4. `H_i=A_i`

Then:

```text
b*A_i=A_i.
```

Row `b` has a fixed point at `A_i`.  This is not a right fixer of the bad
target `b`; it is a row-`b` cycle boundary.

### 5. `H_i=x_i` or `H_i=x_{i+1}`

These are visible hits of the predecessor arrow:

```text
b*H_i=A_i.
```

They attach the row-`b` predecessor fan to the right-`b` orbit footprint.  They
should be routed as visible-hit cases, not treated as immediate contradictions.

## Use

For the clean external bridge, the first step has:

```text
x_0=a,
x_1=t=a*b,
A_0=k,
H_0=ell.
```

The equality:

```text
A_0=x_1
```

is exactly:

```text
k=t,
```

which was already routed to:

```text
row_a_bridge_loop_recurrence_boundary.md
```

The new classification applies to later steps of the right-`b` orbit
predecessor chain.
