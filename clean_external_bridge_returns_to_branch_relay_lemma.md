# Clean External-Bridge Fan-Regeneration Boundary

Date: 2026-06-18.

Status:

```text
proved fan-regeneration step / core-attachment connector still missing
```

## Setup

Work in the clean external-bridge residual of the proper bad-target crossed
fan.

The row-a bridge creates the right-`b` orbit:

```text
x_0=a,
x_{i+1}=x_i*b.
```

The first-repeat fan lemma says that the first repeat of this orbit gives:

```text
1. a triple incoming fan at a, if the orbit returns to a; or
2. a fresh incoming common-edge fan at the first repeated vertex v; or
3. a visible-source hit, already routed out of the clean residual.
```

## Statement

Therefore the clean external-bridge residual is not a one-step local
contradiction.  Its first finite obstruction regenerates a branch-fan shape:

```text
right-b orbit first repeat
=> incoming fan in H_b
```

More explicitly, in the internal repeat case:

```text
x_i=x_j=v, 0<i<j,
y=x_{i-1}, z=x_{j-1}.
```

Then:

```text
y*b=v,
z*b=v,
y!=z,
A_{i-1}!=A_{j-1}.
```

So in `H_b` there is an incoming fan:

```text
A_{i-1} -> v,
A_{j-1} -> v.
```

The common hub for the shared edge `b -> v` is:

```text
A_i=pred_v(b),
```

and the canonical transport edge is:

```text
A_i -> v*b=x_{i+1}.
```

This is the same algebraic incoming-branch transport shape used in:

```text
bicyclic_component_branch_fan_lemma.md
bad_target_core_fan_lemma.md
```

However, the right-`b` orbit:

```text
x_{i+1}=x_i*b
```

is not itself an `H_b` path.  Its `H_b` edges are:

```text
A_i -> x_{i+1}.
```

The next edge starts at `A_{i+1}`, not at `x_{i+1}`.  Therefore the regenerated
incoming fan is not automatically proved to lie in the original cyclic core
component.  This connector gap is recorded in:

```text
right_b_orbit_repeat_core_attachment_gap.md
```

## What Is Still Missing

This lemma does not prove E677 -> E255.  It proves only the finite
fan-regeneration step from the clean external bridge.

The remaining task has one more connector before the global No-Free-Tail
termination problem:

```text
show that the regenerated fan is core-attached, or else classify the
independent right-b orbit cycle as a same-row / predecessor-chain boundary.
```

## Use

After this reduction, future work should not expect the clean external bridge
to close by a one-step visible equality.  Its first finite obstruction is a
new incoming branch fan, but a separate core-attachment connector is still
needed before it can be used as an ordinary recursive branch relay.
