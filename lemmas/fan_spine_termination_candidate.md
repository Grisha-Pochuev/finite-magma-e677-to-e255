# Fan-Spine Termination Candidate

Date: 2026-06-08.

Status:

```text
main candidate sublemma / not proved
```

Purpose:

```text
State the next large termination problem created by the double-interval
pressure mechanism without reverting to numeric tip splits.
```

## Setup

Let `0` be a bad element:

```text
there is no y with y*0=0.
```

Assume an active value `P` satisfies:

```text
P*0=P.
```

Define:

```text
C=P*P
h=0*C=C*P
a=0*P
e=h*a.
```

Then:

```text
P*e=h
P*h=0
P*0=P
P*P=C.
```

So row `P` contains:

```text
e -> h -> 0 -> P -> C.
```

Let:

```text
F={q : q*0=P}.
```

For each `q in F`, define:

```text
T_q=q*P.
```

Then:

```text
the T_q are pairwise distinct;
T_q!=P;
T_q*q=h.
```

In the bad-tail role `u=b_3`, the source set contains:

```text
P=b_2
B=b_4
A=0*0.
```

## Candidate Statement

In a finite `E677` magma with bad `0`, the fan spine above cannot close with
all its spine points and return tips avoiding:

```text
1. a row-0 shared edge;
2. an aligned two-edge overlap;
3. an older bad-cycle tail;
4. a zero-column fixed point y*0=0.
```

Equivalently, the fan spine cannot remain a finite isolated pressure component.

## Proved First-Hit Roles

### Tips do not repeat

For distinct sources:

```text
q!=r,
```

the fan theorem gives:

```text
T_q!=T_r.
```

### No tip equals P

Since:

```text
q*0=P
```

and `0!=P`, row-`q` injectivity gives:

```text
q*P!=P.
```

Thus:

```text
T_q!=P.
```

### General zero-tip transfer

Suppose:

```text
T_q=q*P=0.
```

Since:

```text
q*0=P,
```

the unique preimage of `0` in row `q` is `P`.

Apply E677 with:

```text
x=0
y=q.
```

It gives:

```text
0=q*(0*(P*q)).
```

Therefore:

```text
0*(P*q)=P.
```

Writing:

```text
s=pred_0(P),
```

we get:

```text
P*q=s.
```

Also:

```text
h=T_q*q=0*q.
```

So every zero tip enters the explicit transfer:

```text
q*0=P
q*P=0
P*q=s
0*q=h.
```

For the three sources:

```text
q in {P,b_4,0*0}
```

of the `u=b_3` role, all zero tips are already closed in:

```text
bad_tail_u_equals_s_zero_tip_closure.md
```

### Spine repetitions e=h and e=0

The equality:

```text
e=h
```

is impossible because row `P` would send the same column to both:

```text
h and 0.
```

If:

```text
e=0,
```

then row `P` gives `h=P`.  Together with `P*h=0` and `P*P=C`, this gives
`C=0`.  In the long bad-cycle role this contradicts the already proved
zero-tip closure.

Thus:

```text
e notin {0,h}.
```

### Row-0 shared edge

If any active row in the fan spine contains:

```text
b_{j+1} -> b_j,
```

then:

```text
bad_cycle_shared_edge_descent_lemma.md
```

forces a return to:

```text
r_{j-1}.
```

This is an explicit descent, not an open role.

### Aligned overlap

If two active source rows share two consecutive edges, then:

```text
two_step_source_reconstruction_lemma.md
```

forces the source rows to be equal.

Thus a genuine cross-source aligned overlap is impossible.

## Remaining Open First Hits

Update 2026-06-08:

```text
fan_spine_four_cycle_descent_lemma.md
tip_source_collision_zero_tooth_lemma.md
two_sided_common_edge_fan_lemma.md
```

The former four-cycle role is now classified:

```text
e=C
=>
rows P and 0 share C -> h
=>
(0*h)*0=0*P.
```

If `C=b_j`, this is:

```text
r_{j-2}=b_1.
```

Moreover `P` becomes a bad element with an own row cycle of length four.
Hence `e=C` is impossible after choosing a bad element with a minimal own-row
cycle of length greater than four.

A tip-source collision is also reduced:

```text
q*P=r
q*0=r*0=P
v=q*r
=>
v*q=0.
```

Thus it enters the zero-tooth machinery.

The first occupied return of that zero tooth is now split by:

```text
zero_tooth_bad_cycle_return_lemma.md
```

If:

```text
q=b_k
v*q=0
v*0=q,
```

then:

```text
v=r_{k-1}.
```

So an aligned return is an old-tail descent. A return to a different
bad-cycle index gives two distinct forced edges in that occupied row.

The internal source-tip graph is also restricted by:

```text
fan_source_tip_graph_lemma.md
```

It proves:

```text
P has no incoming internal tip;
at least one fan tip is external to the source fiber;
distinct sources cannot form a two-cycle q -> r -> q;
an internal self-loop q -> q creates h*q=0.
```

For the three sources `P,B,A`, the possible internal swap `B <-> A` is
therefore impossible.

After these reductions, the genuinely unresolved events are:

```text
1. the zero tooth created by a tip-source collision has a fresh or
   non-aligned return;

2. e or a tip hits a bad-cycle point without immediately matching a row-0
   directed edge;

3. the spine closes inside a longer source-row cycle while all fan tips
   remain external to it.
```

The longer row-`P` closure now has an exact test:

```text
fan_spine_fourth_predecessor_test.md
```

For:

```text
f=L_P^{-4}(P)
g=L_P^{-5}(P),
```

one has:

```text
P is good <=> f*f=g <=> h*P=P.
```

After choosing a minimal bad element, any row-`P` closure shorter than the
original bad cycle must satisfy `f*f=g`. If that equality fails, `P` is bad
and its own cycle cannot be shorter than the original one.

The exact length-five good-P role is impossible:

```text
fan_spine_length_five_badness_lemma.md
```

Indeed, a five-cycle would force:

```text
C*C=P
h*C=P
h*P=P,
```

contradicting row-`h` injectivity because `C!=P`.

Therefore every exact row-`P` five-cycle is bad. Under minimal bad-cycle
selection, closures of lengths four and five are both excluded whenever the
original minimal bad cycle is longer.

The first unresolved shorter good-P closure is length six:

```text
P -> C -> f -> e -> h -> 0 -> P
f*f=C
h*P=P.
```

For occupied `C=b_j`, the good-P condition has an additional pressure split:

```text
good_p_occupied_tip_pressure_lemma.md
```

It proves:

```text
h=b_{j-1}
h*P=P
h*r_{j-2}=C
=>
r_{j-2}!=P.
```

If `r_{j-2}=P`, contradiction. Otherwise row `b_{j-1}` carries two distinct
forced occupied edges.

The full exact six-cycle structure is recorded in:

```text
good_six_cycle_cross_ladder_lemma.md
```

Besides:

```text
e*P=f
f*f=C,
```

it creates:

```text
column P: P -> C -> h -> P;
k=f*P;
C*k=P;
k!=P.
```

For occupied `C=b_j`, row `b_j` now has:

```text
r_{j-1} -> b_{j+1}
P       -> b_{j-1}
k       -> P.
```

The exact next classifier for the length-six branch is `k=f*P`.

General upgrade:

```text
fan_tip_bridge_expansion_lemma.md
```

For every source `q*0=P`, with tip `T_q=q*P`, define:

```text
w_q=(q*T_q)*q.
```

Then:

```text
T_q*w_q=P
w_q!=q.
```

Moreover:

```text
w_q=0 <=> T_q is another source in F(0,P);
w_q=P <=> T_q=h.
```

If two bridge values coincide, the two tip rows form a second-generation
common-edge fan over `w -> P`. If they do not coincide, the bridges form a new
injective family.

This is now the preferred recursive formulation of Fan-Spine Termination.

The exact three-source good-six target is isolated in:

```text
three_source_good_six_pressure_candidate.md
```

The size-9 diagnostic shows that adding only the third source `B*0=P` kills
the remaining good-six row-`P` candidates; the special row-`b_3` continuation
is not needed. The general theorem still requires a structural classification
of bridge/source and bridge/tip intersections.

For a fan tip on the bad cycle there is now an exact index split:

```text
fan_tip_bad_cycle_alignment_lemma.md
```

If:

```text
C=b_j
T_q=b_{j-2},
```

then:

```text
q=r_{j-3}.
```

So the aligned occupied-tip role is an old-tail descent. Only non-aligned
bad-cycle tips remain as extra occupied-row pressure.

These are structural roles, not numeric values.

## Size-9 Evidence

In the full normalized size-9 `u=b_3` role:

```text
C in {0*0,b_7,b_6,b_4}.
```

All four roles are closed:

```text
C=0*0 -> closed;
C=b_4 -> closed;
C=b_7 -> closed;
C=b_6 -> closed.
```

For the far roles, the general zero descent gives:

```text
C=b_7 -> P*b_6=0;
C=b_6 -> P*b_5=0.
```

The remaining closure uses the finite boundary geometry of the 9-cycle.

## Next Proof Strategy

Do not enumerate all values of `e,D,E`.

Work by the three remaining first-hit types above:

```text
zero-tooth continuation after a tip-source collision;
non-edge bad-cycle hit;
longer source-row cycle closure, now split by f*f=g.
```

The desired result is to show that each type either becomes a shared-edge
descent or creates a smaller fan spine nearer to the bad-cycle origin.

Minimal-cycle boundary:

```text
minimal_bad_short_cycle_reduction.md
```

After choosing a bad element with minimal own-row cycle, the present long-cycle
candidate only needs to handle cycle length at least five. The exact length-3
and length-4 base configurations are recorded separately.
