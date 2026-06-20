# M496 First Extra Intersection Roles Diagnostic

Date: 2026-06-20.

Status:

```text
diagnostic / clean first-extra matching absent in M496
```

## Purpose

This refines:

```text
m496_shared_step_orbit_split_diagnostic.md
two_row_first_extra_intersection_routing_lemma.md
```

After finding that every shared-step row pair in M496 has an extra cycle
intersection, this diagnostic classifies the first such intersection by:

```text
same_target_pair_collision_trichotomy_lemma.md
```

## Script

The permanent script is:

```text
tools/m496_first_extra_intersection_roles.js
```

## Result

For all `892800` shared-step row pairs:

```text
full interval collision: 0
same input fan:          168480
same output fan:         724320
cross hit/path:          0
clean matching:          0
no extra intersection:   0
```

## Interpretation

In M496, the first extra row-cycle intersection is always immediately a fan:

```text
same input,
or same output.
```

The clean same-target matching subcase left open by:

```text
two_row_first_extra_intersection_routing_lemma.md
```

does not appear.

This suggests the next structural target:

```text
prove that a first extra intersection in a minimal separated period >= 3
G12 loop cannot be clean-disjoint; it must create same input, same output,
cross hit, or full interval collision.
```

This is only a diagnostic pattern, not a proof.
