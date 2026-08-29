# E677 order-9 two-Bad no-HIT exclusion

Date: 2026-08-29.

Status:

```text
proved: if |Bad|=2, every state in Bad x Bad is an Omega-root and every
        outgoing tau edge leaves Bad x Bad;
proved: after 0*0=1, the no-HIT D-chain has exactly four normalized forms;
checked exactly: all four forms are UNSAT at order 9;
checked independently: the two nontrivial terminal orbit families are
                       UNSAT with both CaDiCaL195 and Glucose42;
consequence: an order-9 counterexample with no HIT has |Bad|>=3.
```

This is a finite order-nine exclusion.  It does not close HIT, the no-HIT
cases with at least three Bad points, or the full implication E677 -> E255.

## Two Bad points make the whole Omega graph root-only

Let `B={p,q}` in any finite E677 magma.  The square states `(p,p)` and
`(q,q)` are genuine roots in the induced graph `Omega=B x B` by the proved
Bad-square root lemma.

Consider an off-diagonal state `(r,u)`, so `{r,u}=B`, and put `v=r*u`.
If `v` is Good, the exact indegree formula makes `(r,u)` a root.  If `v` is
Bad, then `v!=u`: the equality `r*u=u` would be a left fixer of the Bad input
`u`.  Hence `v=r`, and the same formula gives

```text
indeg_Omega(r,u)=N_B(r,r)=0,                                  (1)
```

because no row fixes a Bad input.  Thus all four states in `Omega` have
internal indegree zero.  The sum of internal indegrees is the number of
internal edges, so

```text
|B|=2  =>  every tau edge from B x B leaves B x B.              (2)
```

The SAT checker uses (2) only as redundant propagation.  For Bad
`r,u,v,h`, it forbids the simultaneous cells

```text
r*u=v,  v*h=u,                                                   (3)
```

which would be an internal edge `tau(r,u)=(v,h)`.

## Four exhaustive D-chain forms

Now let the magma have order `9`, assume `D(B) subset B`, choose `0 in B`,
and normalize

```text
0*0=1,
f(t)=t*0.
```

Since `0` is Bad, `D(0)!=0`, and

```text
D(0)=f(f(1)).                                                   (4)
```

If `1` is Bad, then `B={0,1}` and no-HIT forces `D(0)=1`.  The value `f(1)`
is either `1` or a new Good label normalized to `2`.  If `1` is Good, name
the other Bad point `2`; then `D(0)=2`, and `f(1)` is either `2` or a new
Good label normalized to `3`.  This gives exactly

```text
I.    B={0,1}, f(1)=1;
II.   B={0,1}, f(1)=2, f(2)=1;
III.  B={0,2}, f(1)=2, f(2)=2;
IV.   B={0,2}, f(1)=3, f(3)=2.                                 (5)
```

In every form the other Bad point maps back to `0` under `D`, since a Bad
point cannot be fixed by `D`.

## Exact formula

The checker

```text
tools/e677_order9_no_hit_bad_count_sat.py
```

encodes all nine permutation rows, every one of the `81` E677 pairs, the
audited `x=0` and `y=0` redundant consequences, exact Good/Bad colours via
the unique-fixer criterion, exact `D` terms, `D(B) subset B`, and exact Bad
cardinality.  Every SAT table is decoded and checked independently against
all these semantic conditions.

With the two-Bad `OMEGA-EXIT` clauses, forms I and II give

```text
I:  CaDiCaL195 UNSAT (direct, 22 conflicts in the first audit);

II: CaDiCaL195 UNSAT, 160,201 conflicts in the final wrapper run;
    Glucose42  UNSAT, 186,242 conflicts.                          (6)
```

## Form III: forced renewal core

Put

```text
a=0*2,
g=2*2.
```

Splitting only by the colours of `a` and `g` closes three of the four
profiles immediately.  The sole residual has `a,g` Good.  Write

```text
h=g*2.
```

The cells `2*0=2`, self-E677 at `2`, and E677 at `(x,y)=(0,2)` give

```text
g*2=h,
2*h=0,
h*2=0,
0*g=h.                                                          (7)
```

Equation (2) makes `h` Good, and `h!=g` follows from `D(2)=0`.  Self-E677 at
`0` also gives

```text
0*a=0.                                                          (8)
```

Consequently row `2` contains the fixed Q_GOOD_LONG renewal block

```text
h Good -> 0 Bad -> 2 Bad -> g Good,                              (9)
```

while the crossing `0*0=1` renews to `0*2=a`.  The remaining `0*2=a`
block is SHORT: if its renewal value were Bad it would equal `2`, identify
the entry with `g`, and contradict `0*g=h` with `h` Good.

For the exact finite check, label `a=3`.  Then `g` is `1` or a new label
`4`; after fixing `g`, the residual relabelling gives exactly five `(g,h)`
orbits:

```text
(1,3), (1,4), (4,1), (4,3), (4,5).                              (10)
```

All five are UNSAT:

```text
CaDiCaL195: 5/5 UNSAT, maximum observed 0.265s;
Glucose42:  5/5 UNSAT, maximum observed 0.233s.                   (11)
```

## Form IV: all four crossings

The colour split closes seven of eight profiles.  In the sole residual,

```text
0*0, 0*2, 2*0, 2*2 are all Good.                                (12)
```

Thus every maximal Bad block in rows `0` and `2` has length one.  The two
diagonal blocks are SHORT.  Each off-diagonal block is either SHORT or its
Q_BAD renewal lands on the corresponding diagonal crossing; there is no
clean renewal cycle left in this four-crossing system.

Put

```text
a=0*2, b=2*0, c=2*2.
```

The labels `0,1,2,3` are already fixed by form IV.  Row injectivity gives
`a!=1` and `b!=c`.  Successive first-new-label normalization gives exactly
`20` joint orbits of `(a,b,c)`.  The full formula gives

```text
CaDiCaL195: 20/20 UNSAT, maximum 0.515s;
Glucose42:  20/20 UNSAT, maximum 0.450s.                          (13)
```

Equations (5)--(13) exclude every order-nine no-HIT model with two Bad
points.

## Exact continuation

Together with the terminal ZERO-shadow exclusion, an order-nine
counterexample must now satisfy

```text
HIT,
or
no HIT, |Bad| in {3,4,5,6,7,8,9}, and Z_Omega>|Bad|.             (14)
```

Do not rerun the two-Bad formulas or enlarge their budgets.  The next
finite structural question is the three-Bad `D`-orbit/root pattern: unlike
the two-Bad case, an off-diagonal product may be the third Bad label, so the
whole Omega graph is no longer automatically root-only.
