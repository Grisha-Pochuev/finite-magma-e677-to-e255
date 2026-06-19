# Y3 Commuting Second-Step Reduction Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / U=V becomes a same-target pair in H_U
```

## Purpose

This treats case 2 from:

```text
y3_shared_successor_square_boundary.md
```

The case is:

```text
U=p*S=S*A_j.
```

The shallow diagnostic shows this does not immediately collapse the named Y3
vertices.  But it is not an anonymous residual: it creates a standard
same-target pair in `H_U`.

## Setup

Use:

```text
p*A_j=S,
p*S=U,
S*A_j=U.
```

Assume the clean branch where:

```text
p!=S,
A_j!=S,
```

and no watched hit has already occurred.  If one of these equalities fails,
the case is a source-row repeat or watched/local hit boundary.

## Same-Target Pair In H_U

Since:

```text
p*S=U,
S*A_j=U,
```

rows `p` and `S` both hit the same target `U`.

Therefore in `H_U` they give two ported intervals:

```text
row p: pred_p(U)=S      -> p*U,
row S: pred_S(U)=A_j    -> S*U.
```

So `U=V` creates the same-target pair:

```text
S   -> p*U,
A_j -> S*U
```

inside:

```text
H_U.
```

## Routing

Apply:

```text
same_target_pair_collision_trichotomy_lemma.md
```

to this pair.

The possible roles are:

```text
1. same full ported interval:
   rows p and S coincide, contradicting the clean branch;

2. same input:
   S=A_j, a watched/local hit;

3. same output:
   incoming fan in H_U;

4. input-output cross hit:
   directed path in H_U;

5. clean disjoint pair:
   a fresh same-target pair attached to the Y3 square through U.
```

Thus the commuting second-step branch:

```text
p*S=S*A_j
```

is converted into a standard same-target pair problem.  It should not be
treated as a direct contradiction, but it also should not be left as an
unstructured equality.

## Consequence For Z3

The next clean Z3 square split may assume either:

```text
p*S != S*A_j,
```

or else it must carry the additional attached pair in `H_{p*S}`:

```text
S   -> p*(p*S),
A_j -> S*(p*S).
```

