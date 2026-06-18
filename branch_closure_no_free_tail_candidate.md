# Branch-Closure No-Free-Tail Candidate

Date: 2026-06-09.

Status:

```text
main active candidate / not proved
```

## Directed Path Certificate

Fix a target `b`. Let:

```text
x_0 -> x_1 -> ... -> x_m
```

be a directed path in `H_b`. Let row `p_i` carry the edge:

```text
p_i*x_{i-1}=b
p_i*b=x_i.
```

Define the two vertex predecessor coordinates:

```text
H_i=pred_b(x_i)
K_i=pred_{x_i}(b)=A_b(x_i).
```

The complete edge certificate gives, for every `i>=1`:

```text
x_i*p_i=H_{i-1}
b*H_{i-1}=x_{i-1}

(p_i*x_i)*p_i=K_i
x_i*K_i=b.
```

It also gives the backward foot:

```text
beta_i=x_{i-1}*(b*p_i)
p_i*beta_i=x_{i-1}.
```

Thus a directed graph path is a coupled transport of:

```text
vertex x_i;
old-target predecessor H_i=pred_b(x_i);
new-target predecessor K_i=pred_{x_i}(b);
source row p_i.
```

## Split Boundary

Suppose an outgoing core fan splits at `v=x_0=y_0`:

```text
p_1*v=b, p_1*b=x_1
q_1*v=b, q_1*b=y_1
x_1!=y_1.
```

Then both first branches have the same initial return:

```text
x_1*p_1=y_1*q_1=pred_b(v).
```

So the two path transports start with one common boundary value:

```text
H_0=pred_b(v).
```

## Merge Boundary

Suppose the two directed branches first merge at:

```text
x_m=y_l=z.
```

Their last source rows share:

```text
b -> z.
```

The two-sided fan at the merge gives a common terminal bridge:

```text
pred_z(b)=A_b(z)=K_z.
```

The penultimate vertices are distinct, and the two forward tips at input `z`
are distinct.

Thus a directed reconvergence has boundary data:

```text
same initial H_0;
same final K_z;
different first and last branch intervals.
```

## Candidate Statement

```text
Boundary-Transport Uniqueness.

Two distinct core paths in H_b cannot start in one outgoing common-edge fan
and first merge at the same vertex z.

Equivalently, the complete edge certificates with a common initial H_0 and
common terminal K_z must create an aligned ordered two-step interval before
the merge.
```

The target-changing version is required when one branch encounters an
outgoing junction before the merge. The hub then becomes the predecessor
coordinate for the graph with the new target, as recorded in:

```text
bicyclic_component_branch_fan_lemma.md
```

## Withdrawn Directed-Diamond Diagnostic

The first reconvergence shape was fixed as:

```text
v -> c -> z
v -> d -> z
```

using four source rows:

```text
5*0=1, 5*1=2
6*0=1, 6*1=3
7*2=1, 7*1=4
8*3=1, 8*1=4.
```

The earlier size-9 search used canonical representatives for row `0` while
also fixing all diamond roles independently. Those two normalizations cannot
in general be imposed simultaneously. Therefore the reported size-9
rejection and the comparison with the three-edge prefix are withdrawn.

The size-10 timeout is also not evidence.

## Relation To The Full No-Free-Tail Lemma

For a bad target, the core-junction lemma gives either:

```text
a triple core fan;
a mixed 2+1 core junction.
```

Every branch remains in the finite cyclic core. It must therefore eventually:

```text
merge with another active branch;
enter an already visited cycle point;
or trigger a target-changing outgoing junction.
```

Boundary-transport uniqueness, together with its target-changing version,
would forbid every such closure. This would prove the pseudoforest property
for the bad target and hence complete No-Free-Tail.

## Next Symbolic Step

Do not test longer diamonds numerically.

The common terminal value:

```text
K_z=pred_z(b)
```

is determined by the merge vertex `z` itself. It is not, by itself, a
path-uniqueness invariant.

The first-merge boundary has now been sharpened in:

```text
first_merge_certificate_separation_lemma.md
```

For last edges:

```text
p*x=b, p*b=z,
q*y=b, q*b=z,
```

with `x!=y`, define:

```text
H_x=z*p,
H_y=z*q,
U=p*z,
W=q*z,
K=U*p=W*q=pred_z(b).
```

Then:

```text
H_x!=H_y,
U!=W.
```

So the common `K` does not propagate backward by simple equality of adjacent
last-certificate labels. The remaining local pressure is the crossed equality:

```text
(p*z)*p=(q*z)*q=K.
```

In the generic continuation case, where the merge vertex has a fresh outgoing
core incidence:

```text
t*z=b, t*b=m, t notin {p,q},
```

the first merge relays to a new mixed junction after target swap:

```text
first_merge_target_swap_mixed_relay.md
```

In `H_z` the same rows form:

```text
b -> U
b -> W
theta -> b.
```

Thus a first merge followed by a fresh outgoing edge is not terminal; it is a
target-swapped mixed split.

The apparent same-row degeneracies are removed in:

```text
first_merge_degenerate_continuation_boundary.md
```

If the branches genuinely first arrive at `z`, then a continuation row
`t*z=b` cannot equal `p` or `q`; otherwise row injectivity gives `x=z` or
`y=z`.

The remaining local boundary is exactly the loop continuation:

```text
t*z=b,
t*b=z.
```

It becomes a loop `b -> b` in `H_z`, not a right fixer.

This loop boundary is also structurally classified in:

```text
first_merge_target_swap_junction_dichotomy.md
```

Since the two merging rows become:

```text
b -> U,
b -> W
```

in `H_z`, and `U,W` are distinct from each other and from `b`, the loop
continuation gives a triple outgoing fan:

```text
b -> U,
b -> W,
b -> b.
```

Therefore a first merge with an outgoing continuation relays to one of the
same two types:

```text
mixed 2+1;
triple fan.
```

For two directed paths with a common split and first merge, compare the full
last certificates, not only `K_z`, and derive an equality that propagates one
step backward. The desired induction remains:

```text
common terminal K
=> common preceding certificate
=> ...
=> identical first ordered interval,
```

contradicting the distinct fan tips.

## Pure-Incoming Boundary Reduction

The pure-incoming merge boundary is now partially reduced in:

```text
pure_incoming_merge_target_swap_fan_lemma.md
```

If the merge vertex `z` has incoming incidences:

```text
p_i*x_i=b,
p_i*b=z,
```

then after target swap `b -> z` the same rows give:

```text
b -> U_i,
U_i=p_i*z,
```

in `H_z`. The tips `U_i` are pairwise distinct by two-step source
reconstruction. In a genuine first-merge setting, none of them equals `b`.

Therefore a pure incoming merge of degree at least three relays to a triple
outgoing fan. The remaining local obstruction is only the binary pure incoming
sink:

```text
two incoming branches merge at z,
no outgoing continuation from z,
no loop at z,
no third incoming incidence at z.
```

This residue is further reduced graph-theoretically in:

```text
binary_sink_core_escape_lemma.md
```

The two branches plus a binary sink give only one simple cycle. Since the
forced bad-target core has at least two independent cycles, some extra core
material must attach to the branch corridor before the sink. The next target is
the earliest such side attachment.

This next target is classified in:

```text
earliest_side_attachment_mixed_junction_lemma.md
```

At an internal branch vertex, the active path has one incoming and one outgoing
incidence. Any extra core incidence makes a mixed `2+1` junction. Therefore
the binary sink residue does not add a new type beyond:

```text
triple fan,
mixed 2+1.
```
