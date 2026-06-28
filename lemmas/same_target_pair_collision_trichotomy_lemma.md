# Same-Target Pair Collision Trichotomy Lemma

Date: 2026-06-18.

Status:

```text
general proved / collision roles for two edges in one H-target
```

## Purpose

This is the common local mechanism behind the remaining cross-role residuals:

```text
U3. beta-coupled same-target pair;
U4. shifted-repeat same-input split lifted to H_T;
U5. beta-anchored reversible square.
```

U3 and U4 contain such a pair directly.  U5 supplies a beta-anchored edge that
can be compared with another edge of the same target when such an edge appears.

## Statement

Fix a target `T`.  Suppose rows `p` and `q` give two ported intervals in
`H_T`:

```text
p*P=T,   p*T=S,
q*Q=T,   q*T=R.
```

So in `H_T`:

```text
P -> S     carried by row p,
Q -> R     carried by row q.
```

Then the first collision among the two inputs/outputs has the following exact
roles.

### 1. Same full ported interval

If:

```text
P=Q and S=R,
```

then the two rows realize the same full ported interval:

```text
(T,P,S).
```

By:

```text
ported_interval_state_lemma.md
```

we get:

```text
p=q.
```

So in a genuine cross-role occurrence, this is a contradiction.

### 2. Same input, different outputs

If:

```text
P=Q and S!=R,
```

then `H_T` has an outgoing fan at `P`:

```text
P -> S,
P -> R.
```

### 3. Different inputs, same output

If:

```text
P!=Q and S=R,
```

then `H_T` has an incoming fan at `S`:

```text
P -> S,
Q -> S.
```

### 4. Input-output cross hit

If:

```text
P=R
or
Q=S,
```

then the two edges concatenate into a directed path in `H_T`:

```text
Q -> P -> S
or
P -> Q -> R.
```

This is a path-attachment role, not a fresh disjoint pair.

## Fresh Pair Boundary

If none of:

```text
P=Q,
S=R,
P=R,
Q=S
```

holds, and none of the four endpoints hits the watched footprint, then the
pair is a clean disjoint two-edge matching inside `H_T`.

This is the exact residual form for same-target pair branches.  The next
step must use the source rows `p,q` or their target-advance squares; the
same-target pair alone has no further local collision.

## Use In The Current Frontier

Apply this lemma to:

```text
U3: H_{A_j}: E_{i,j}->A_i and Beta_j->b;
U4: H_T after shifted-repeat target lift;
U5: the beta-anchored edge Beta_j->b when another edge with target A_j is
    present.
```

The useful hits are:

```text
same full interval -> source collision;
same input/output  -> fan in the relevant H_T;
cross hit          -> directed path concatenation.
```

Only the clean disjoint matching case remains.
