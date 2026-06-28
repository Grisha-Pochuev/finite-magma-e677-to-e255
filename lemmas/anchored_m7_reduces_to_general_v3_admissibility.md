# Anchored-M7 Reduces To General V3 Admissibility

Date: 2026-06-25.

Status:

```text
conditional reduction / M7 clean necklace closes under general V3 admissibility
```

## Purpose

This records the current best structural compression:

```text
anchored M7 clean self-repeat
```

is no longer an independent local residual if the general clean V3
admissibility principle is available.

## General V3 Admissibility Principle Needed

The needed principle is a slight strengthening of:

```text
general_v3_bridge_descent_boundary.md
```

from:

```text
clean V3 bridge born at a first-extra intersection
```

to:

```text
any clean same-input two-target bridge born before the current terminal event
inside the chosen minimal G12 object.
```

Principle:

```text
A clean same-input two-target bridge either routes by a local hit, or is
admissible as a smaller measured relay object.
```

## Anchored-M7 Application

In the clean M7 self-repeat, the coupled zipper bridge gives for each adjacent
pair:

```text
H_{r_i}:     h -> A_i,
H_{r_{i+1}}: h -> A_{i+1}.
```

This is a clean same-input two-target bridge unless one of the already routed
hits occurs:

```text
A_i=A_{i+1},
A_i=r_{i+1},
A_{i+1}=r_i,
A_i=h,
A_{i+1}=h,
watched/core hit,
full interval collision.
```

By:

```text
fixed_target_zipper_bridge_necklace_lemma.md
anchored_m7_zipper_lift_advance_equivalence_lemma.md
```

this bridge is not artificial: its target-lift is exactly the adjacent pair
of `H_h` zipper edges.

## Descent

The terminal M7 event is:

```text
r_n=r_0.
```

Every adjacent V3 bridge in the necklace is born at a position:

```text
i<n.
```

Thus, under the general V3 admissibility principle, choose the earliest clean
adjacent V3 bridge.  It is a smaller measured object under:

```text
M8. anchored V3 necklace bridge rank.
```

Therefore the clean M7 self-repeat cannot be terminal in a minimal G12 loop.

## Conditional Conclusion

Assuming general V3 admissibility:

```text
anchored-X3 false branch
  -> first M7 event
  -> clean self-repeat
  -> clean V3 necklace
  -> smaller admissible V3 object
```

or one of the already routed hits occurs.

So the remaining M7 branch is not a separate obstruction.  It reduces to the
global clean V3 admissibility problem.

## Remaining Global Target

The next proof should focus on one unified admissibility statement:

```text
Clean same-input two-target bridge admissibility.
```

It must cover both:

```text
1. clean first-extra V3 bridges from general_v3_bridge_descent_boundary.md;
2. clean adjacent V3 bridges from anchored M7 necklaces.
```

If that statement is proved, the anchored M7 residual closes with it.
