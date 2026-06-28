# Anchored-M7 Cycle Zipper Lemma

Date: 2026-06-25.

Status:

```text
proved local lemma / clean right-h source cycle has two-sided input formulas
```

## Purpose

This sharpens:

```text
anchored_m7_cycle_end_template.md
```

The remaining anchored-M7 residual is a clean same-orbit right-`h`
source-successor cycle.  The source cycle is still not an `H_h` path, but its
`H_h` inputs are not free: each input is determined from both neighboring
source rows.

## General Statement

Fix target:

```text
h.
```

Let three consecutive source rows in a right-`h` source-successor orbit be:

```text
a*h = r,
r*h = c.
```

Let `I_r` be the input of the `H_h` edge carried by row `r`:

```text
r*I_r=h,
r*h=c.
```

Then:

```text
I_r = h*(c*r)
```

and also:

```text
I_r = (a*r)*a.
```

So every internal source row `r` satisfies the zipper equation:

```text
h*(c*r) = (a*r)*a.
```

## Proof

The first formula is the usual predecessor formula for the edge:

```text
r*I_r=h,
r*h=c
=> I_r=h*(c*r).
```

For the second formula, apply the fixed-target source-successor formula to
the previous source row `a`:

```text
a*h=r
=> r*((a*r)*a)=h.
```

But row `r` has a unique input mapping to `h`, by left cancellation / left-row
permutation.  Since:

```text
r*I_r=h
and
r*((a*r)*a)=h,
```

we get:

```text
I_r=(a*r)*a.
```

Combining the two input formulas gives:

```text
h*(c*r) = (a*r)*a.
```

## Cycle-End Form

In the notation:

```text
r0*h  = r1,
rm2*h = rm1,
rm1*h = r0,
```

the corresponding `H_h` inputs satisfy:

```text
i0  = h*(r1*r0)   = (rm1*r0)*rm1,
im1 = h*(r0*rm1)  = (rm2*rm1)*rm2.
```

Similarly:

```text
im2 = h*(rm1*rm2)
```

and, if the predecessor of `rm2` in the cycle is named, it also has a
left-neighbor formula of the same kind.

## Interpretation

The clean self-repeat is no longer just a closed right-`h` source cycle:

```text
r0 -> r1 -> ... -> rm1 -> r0.
```

It is a cyclic zipper of source triples:

```text
h*(r_{i+1}*r_i) = (r_{i-1}*r_i)*r_{i-1}.
```

This is the correct next object to attack.

## Routed Collisions

If any zipper input:

```text
I_i
```

hits a neighboring source/output/input in a way that creates:

```text
same input,
same output,
full ported interval,
input-output cross hit,
watched/core hit,
```

then the branch routes by:

```text
same_target_pair_collision_trichotomy_lemma.md
anchored_m7_first_event_routing_lemma.md
```

## Remaining Clean Residual

The live residual is therefore sharper:

```text
a clean cyclic zipper of right-h source rows,
with no source repeat before the chosen return,
no input collision,
no output merge,
no input-output cross hit,
and no watched/core hit.
```

The next target should classify the first collision among the zipper
certificates:

```text
(r_{i-1}*r_i)*r_{i-1}
```

or prove that a clean cyclic zipper creates strict clean theta in `H_h`.
