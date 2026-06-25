# Two-Row First Extra Intersection Routing Lemma

Date: 2026-06-20.

Status:

```text
proved reduction / routes first extra row-orbit intersection
```

## Purpose

This routes branch 1 of:

```text
two_row_orbit_theta_boundary.md
```

where two separated period `>= 3` row cycles meet again outside their shared
step.

## Setup

Let two distinct rows `p,q` share:

```text
p*b=z,
q*b=z.
```

Write their row orbits as:

```text
x_{i+1}=p*x_i,
y_{j+1}=q*y_j,
x_0=y_0=b,
x_1=y_1=z.
```

Suppose the two row cycles have a first extra intersection:

```text
w=x_i=y_j
```

outside the shared pair `{b,z}`.

Then in the fixed target graph `H_w`, the two rows give:

```text
x_{i-1} -> x_{i+1}   carried by row p,
y_{j-1} -> y_{j+1}   carried by row q.
```

because:

```text
p*x_{i-1}=w, p*w=x_{i+1},
q*y_{j-1}=w, q*w=y_{j+1}.
```

## Routing By Same-Target Trichotomy

Apply:

```text
same_target_pair_collision_trichotomy_lemma.md
```

to the two edges in `H_w`.

There are four local hit roles.

### 1. Same full ported interval

If:

```text
x_{i-1}=y_{j-1},
x_{i+1}=y_{j+1},
```

then the full interval:

```text
(w,x_{i-1},x_{i+1})
```

appears in two independent branch roles.  Source reconstruction gives
`p=q`, contradiction for a genuine two-row occurrence.

### 2. Same input

If:

```text
x_{i-1}=y_{j-1},
x_{i+1}!=y_{j+1},
```

then `H_w` has an outgoing fan at the shared input.

### 3. Same output

If:

```text
x_{i-1}!=y_{j-1},
x_{i+1}=y_{j+1},
```

then `H_w` has an incoming fan at the shared output.

### 4. Input-output cross hit

If:

```text
x_{i-1}=y_{j+1}
or
y_{j-1}=x_{i+1},
```

then the two edges concatenate into a directed path in `H_w`.

## Clean Matching Subcase

If none of these equalities holds, the first extra intersection produces a
clean disjoint same-target matching in `H_w`.

This matching is not a free new object.  Target advance sends it to the
same-input two-target bridge:

```text
target x_{i+1}:  w -> x_{i+2},
target y_{j+1}:  w -> y_{j+2}.
```

This is exactly the general transport in:

```text
same_input_lift_target_advance_lemma.md
```

read in the forward direction from same-target matching back to a shared-input
two-target bridge.

## Consequence For G12

The first-extra-intersection branch of the separated period `>= 3` residual
does not create a new kind of same-source recurrence.

It routes to:

```text
1. independent full ported-interval collision;
2. outgoing/incoming fan in H_w;
3. directed path attachment in H_w;
4. clean same-input two-target bridge after target advance.
```

The only part not closed inside this file is branch 4.  It is the familiar
clean two-target bridge form, not a new pure same-row recurrence.

The exact bridge alignment is recorded in:

```text
clean_first_extra_matching_bridge_alignment.md
```
