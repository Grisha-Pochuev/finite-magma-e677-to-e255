# Directed Path Bridge-Pair Transport Lemma

Date: 2026-06-17.

Status:

```text
general proved / path certificate transport
```

## Purpose

This lemma rewrites the full edge certificate in a form useful for clean
mixed-theta paths.

Instead of tracking only the directed edge:

```text
x -> y
```

in `H_b`, it tracks the two bridge labels attached to each vertex:

```text
H_x=pred_b(x),
K_x=pred_x(b).
```

These satisfy:

```text
b*H_x=x,
x*K_x=b.
```

## One Directed Edge

Fix a target `b`.  Suppose row `t` gives an edge:

```text
t*x=b,
t*b=y.
```

So in `H_b`:

```text
x -> y.
```

Define:

```text
H_x=pred_b(x),
K_y=pred_y(b),
U=t*y.
```

Then the full edge certificate gives:

```text
y*t=H_x,
U*t=K_y,
b*H_x=x,
y*K_y=b.
```

Equivalently:

```text
t=pred_y(H_x),
U=pred_t(K_y).
```

Thus the row source `t` is determined by the ordered pair:

```text
(H_x,y)
```

or, equivalently, by the original ordered two-step interval:

```text
x -> b -> y.
```

## Consecutive Path Form

Let:

```text
x_0 -> x_1 -> ... -> x_m
```

be a directed path in `H_b`.  For the edge:

```text
x_i -> x_{i+1}
```

write its source row as `t_i`:

```text
t_i*x_i=b,
t_i*b=x_{i+1}.
```

Define vertex bridge pairs:

```text
H_i=pred_b(x_i),
K_i=pred_{x_i}(b).
```

Then every edge of the path carries:

```text
x_{i+1}*t_i=H_i,
(t_i*x_{i+1})*t_i=K_{i+1},
b*H_i=x_i,
x_{i+1}*K_{i+1}=b.
```

So a directed path transports from the initial bridge pair:

```text
(H_0,K_0)=(pred_b(x_0), pred_{x_0}(b))
```

to the terminal bridge pair:

```text
(H_m,K_m)=(pred_b(x_m), pred_{x_m}(b)).
```

The edge `x_i -> x_{i+1}` connects the previous `H_i` to the next `K_{i+1}`
through the same source row `t_i`.

## Clean Mixed-Theta Relevance

In a clean mixed theta, the two outgoing branches have common endpoints:

```text
v -> ... -> z,
v -> ... -> z.
```

Therefore both branch certificate chains start with the same bridge pair:

```text
(pred_b(v), pred_v(b))
```

and end with the same bridge pair:

```text
(pred_b(z), pred_z(b)).
```

At the initial mixed junction, the shared first-edge bridge is:

```text
pred_b(v).
```

At the terminal first merge, the shared last-edge bridge is:

```text
pred_z(b).
```

Thus the clean-theta pressure is a two-ended bridge-pair problem:

```text
two internally disjoint directed certificate chains
connect the same bridge-pair endpoints.
```

The next desired step is to prove that such two chains must force a repeated
ordered two-step interval in distinct rows, unless a side attachment or relay
case appears earlier.

