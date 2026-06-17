# Current Frontier

Date: 2026-06-17.

The project studies whether

```text
E677: x = y * (x * ((y * x) * y))
```

implies

```text
E255: x = ((x*x)*x)*x
```

in every finite magma.

The full implication is not yet proved.

## Latest proved mechanism

For a fixed target `b`, define:

```text
A_b(q) = the unique a such that q*a=b
R_b(q) = q*b.
```

Every row `q` gives a two-step interval:

```text
A_b(q) -> b -> R_b(q).
```

For a target edge:

```text
q*a=b
q*b=c,
```

the current proof layer gives a full local certificate:

```text
row q: beta -> a -> b -> c
row c: q -> pred_b(a), A_b(c) -> b
row b: pred_b(a) -> a.
```

This generalizes the earlier common-edge fan and bridge recursion.

## Current reduction

The active frontier is the **branch-closure No-Free-Tail** candidate.

The proved branch layer reduces a hypothetical bad target to one of:

```text
triple core fan;
mixed 2+1 core junction.
```

The current candidate says that these branch-closure configurations cannot
remain fresh indefinitely in a finite E677 magma.

See:

```text
lemmas/branch_closure_no_free_tail_candidate.md
lemmas/crossed_double_fan_pressure_candidate.md
lemmas/bicyclic_core_junction_lemma.md
lemmas/bad_target_core_fan_lemma.md
```

## Exact next question

Do not begin a broad finite search.

The next structural task is:

```text
Transport the full edge certificates along the two or three forced branches.
Classify the first merge, cycle closure, or aligned two-step overlap.
Show that every remaining closure forces a forbidden fan pressure collision.
```

## Current status boundary

Proved:

```text
complete target-edge certificate;
right-target bridge recursion;
cycle-entry fan creation;
target-swap fan duality;
bicyclic core reduction to triple-fan or mixed 2+1 branch pressure;
sizes 5, 6, 7, and 8 computational closures.
```

Not proved:

```text
branch-closure No-Free-Tail Lemma;
crossed double-fan exclusion as a general lemma;
E677 => E255 for all finite magmas.
```
