# E677 Bad-square tau-subgraph root/merger/cycle lemma

Date: 2026-07-24.

Status:

```text
proved: every Bad diagonal state (x,x) is an actual indegree-zero vertex in
        the induced Bad x Bad tau graph;
proved: every exit of that graph has a concrete coloured C certificate;
proved: perfect reuse of the square roots is an actual tau-functional
        component, whose terminal object is a genuine all-Bad tau cycle;
proved: the former mixed-row/permutation pseudo-cycle cannot occur in this
        routing
```

Let `B=Bad`.  On multiplication states use

```text
tau(r,u)=(v,h),
v=r*u,
h=v\u.                                          (1)
```

Companion factorization gives

```text
v*h=u.                                          (2)
```

Consider the induced partial functional graph

```text
Omega=B x B.                                    (3)
```

A state in `Omega` keeps its `tau` edge precisely when both coordinates of
its target in (1) are Bad.

## Exact internal indegree

Fix a state `(v,h) in Omega` and put `u=v*h`.  Its full `tau` predecessors
are exactly the states

```text
(r,u),  r*u=v.                                  (4)
```

Such a predecessor belongs to `Omega` exactly when `r,u` are Bad.  Hence

```text
indeg_Omega(v,h)
 = 0,          if u is Good;
 = N_B(u,v),   if u is Bad.                     (5)
```

This retains both source-row colour and the fact that every edge is a real
`tau` edge.

## Every Bad square is a genuine root

For `x in B`, put

```text
delta_x=(x,x) in Omega,
s(x)=x*x.                                       (6)
```

If `s(x)` is Good, formula (5) gives zero internal indegree because the
product of `delta_x` is Good.  If `s(x)` is Bad, the square-source lemma
gives

```text
N_B(s(x),x)=0,                                  (7)
```

and (5) again gives zero internal indegree.  Therefore

```text
indeg_Omega(delta_x)=0 for every x in B.        (8)
```

The `b=|B|` roots `delta_x` are pairwise distinct.  They are also distinct
from the older canonical zero-path reserve: they use the literal diagonal
state `(x,x)`, not `rho(x,x)=(x,x\x)`.

There is a stronger first-shell separation in the all-Bad residue.  Put

```text
kappa(x)=x\x=x*sigma(x),
gamma_x=rho(x,x)=(x,kappa(x)).                  (9)
```

Both `gamma_x` and `delta_x` have full `tau` indegree zero, and

```text
tau(gamma_x)=(x,sigma(x)),
tau(delta_x)=(s(x),q(x)),
q(x)=s(x)\x.                                    (10)
```

The four `|M|`-element families

```text
{gamma_x}, {delta_x}, {tau(gamma_x)}, {tau(delta_x)}               (11)
```

are pairwise disjoint.  Within each successor family this follows from the
row coordinate, or from the fact that the product of `tau(delta_x)` is `x`.
A successor cannot equal either root family unless that root acquires a
predecessor.  For completeness, the only possible cross equality between
the two successor families would give

```text
y=kappa(x),  s(y)=x.                             (12)
```

But `x*kappa(x)=x` and `kappa(x)*kappa(x)=x`; the proved right-orbit lemma

```text
c*c=a and a*c=a  =>  c=a
```

then gives `kappa(x)=x`, making `x` idempotent and hence Good.  This is
impossible in the all-Bad residue.

Thus the new square roots cannot reuse the old diagonal reserve or either
reserve's first edge.  Before the first genuine merger/exit, they contribute
an additional disjoint two-level shell, not a relabelling of an old charge.

## Every graph exit is coloured

Let `(r,u) in Omega`, and retain the notation (1).

If `v` is Good, the original cell

```text
r*u=v                                           (13)
```

is a member of the Bad-row `Bad -> Good` crossing set `C`.

Suppose `v` is Bad but `h` is Good.  Put

```text
a=r*v.
```

The companion page is

```text
r*u=v,  r*v=a,  a*r=h,  v*h=u.                 (14)
```

If `a` is Good, `r*v=a` belongs to `C`; if `a` is Bad, `a*r=h` belongs to
`C`.  Thus every edge leaving `Omega` has a concrete coloured certificate.

Within either of these two certificate types the source state `(r,u)` is
recoverable, so the map is injective.  A coincidence between the two types
is the explicit two-step coloured renewal

```text
r*u=v,  r*v=g,
v*u'=w, v*w=r,                                  (15)
```

with all displayed non-`g` labels Bad and `g` Good.  It is therefore a
marked renewal intersection, not an anonymous loss of a charge.

## The exact finite functional identity

For the induced graph on `Omega`, let

```text
Z_Omega = number of vertices of internal indegree zero;
K_Omega = sum_w max(indeg_Omega(w)-1,0);
E_Omega = number of vertices whose tau edge leaves Omega.          (16)
```

The number of internal edges is both `|Omega|-E_Omega` and the sum of the
internal indegrees.  Therefore

```text
Z_Omega=K_Omega+E_Omega.                        (17)
```

By (8), `Z_Omega>=b`.  The merger term in (13) is exactly supported on
Bad-source collision fibres `N_B(u,v)>=2` whose companion hinge `v\u` is
Bad.  The exit term has the coloured certificates (9)--(11).

There is a sharp equality consequence which will be used before any cycle
is collapsed.  If

```text
Z_Omega=b,                                      (18)
```

then the `delta_x` are all the zero-indegree vertices.  Every cell

```text
r*u=g,  r,u Bad, g Good
```

itself represents a vertex `(r,u) in Omega` whose product is Good, and hence
has internal indegree zero by (5).  Equality (14) therefore forces

```text
r=u,
g=r*r.                                          (19)
```

In other words, the exact root-equality core has the off-diagonal closure

```text
r,u Bad and r!=u  =>  r*u Bad,                  (20)
```

and every Bad-row `Bad -> Good` crossing is one of the selected square
cells.  Any non-square coloured crossing is automatically a strict extra
root beyond the `b` square reserve.

Follow all selected roots `delta_x` simultaneously.  A path either:

```text
1. leaves Omega and reaches a named C certificate;
2. meets another selected path, or enters an already visited state, using
   one actual indegree-surplus unit in K_Omega;
3. after all rooted trees are removed, terminates in a directed cycle of
   the restricted map.                           (21)
```

Every edge in the third outcome is an edge of `tau`, and every vertex has
both coordinates Bad.  Consequently its terminal cycle is a genuine
all-Bad `tau` cycle.  No row-successor edge, `J` switch, or relative
permutation edge has been inserted.

Thus perfect reuse of all square roots can no longer produce the former
mixed `mu/nu` pseudo-cycle.  Its exact residue is a collection of rooted
functional components whose cores are actual CYCLE objects.

## Continuation boundary

Equation (13) by itself is balanced and is not a contradiction.  Its value
is that the last global closure is now legitimate:

```text
square root -> coloured HIT exit;
square root -> named Bad-source merger;
perfect closed reuse -> genuine all-Bad tau cycle.                 (22)
```

The remaining strict step is to choose a minimal terminal genuine `tau`
cycle and compare the square-root merger slots feeding its component with
the already reserved `J/M/E_U/E_A` slots.  Equality may be passed to
PORT-MINIMAL only after this actual component comparison; it must not be
replaced by a relative permutation cycle.
