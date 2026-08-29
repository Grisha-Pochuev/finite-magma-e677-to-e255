# E677 Omega-root equality forces every Bad point to HIT

Date: 2026-07-24.

Status:

```text
proved: equality in the new Bad-square root reserve forces kappa(Bad) into
        Good;
proved: together with off-diagonal Bad closure it forces sigma(Bad) into
        Good;
proved: with the Good-row SHORT equality it forces D(Bad) into Good;
consequence: the exact terminal root equality cannot contain a Bad D-cycle
```

Let `B=Bad`, `b=|B|`, and let `Omega=B x B` carry the induced partial
`tau` graph from
`e677_bad_square_tau_subgraph_root_merger_cycle_lemma.md`.  Assume its exact
root equality

```text
Z_Omega=b.                                      (1)
```

Then the `b` square roots

```text
delta_x=(x,x),  x in B,                         (2)
```

are all the internal indegree-zero vertices.  The same equality already
proved

```text
r,u in B and r!=u  =>  r*u in B.                (3)
```

Assume also the terminal Good-row equality

```text
Good*Bad subset Good.                           (4)
```

## The old root forces kappa(x) to be Good

For `x in B`, put

```text
kappa(x)=x\x=x*sigma(x).
```

The self band gives

```text
x*kappa(x)=x.                                   (5)
```

If `kappa(x)` were Bad, the state

```text
gamma_x=(x,kappa(x)) in Omega                   (6)
```

would have product `x`.  Its internal indegree is therefore

```text
N_B(x,x)=0                                      (7)
```

by the unique-fixer criterion.  Moreover `gamma_x!=delta_x`, since
`kappa(x)=x` in (5) would make `x*x=x`.  Thus (6) would be an additional
root beyond the `b` roots in (2), contradicting (1).  Hence

```text
kappa(x) is Good for every x in B.              (8)
```

## Off-diagonal closure forces sigma(x) to be Good

Suppose `sigma(x)` were Bad.  It cannot equal `x`, because

```text
sigma(x)=(x*x)*x=x
```

would exhibit the row `x*x` as a fixer of the Bad input `x`.  Thus `x` and
`sigma(x)` are distinct Bad points.  But the self cell

```text
x*sigma(x)=kappa(x)                             (9)
```

has Good output by (8), contradicting the off-diagonal closure (3).
Therefore

```text
sigma(x) is Good for every x in B.              (10)
```

Finally (4) and the canonical cell give

```text
D(x)=sigma(x)*x is Good for every x in B.       (11)
```

## Consequence

Under the two terminal equalities, every Bad point has `D`-depth one.  There
is no Bad `D`-cycle and no all-Bad terminal component.  Thus a surviving
CYCLE branch must satisfy the strict alternative

```text
Z_Omega>b.                                      (12)
```

Equivalently, it must retain at least one specifically named extra root:

```text
a Bad kappa(x),
a non-square Bad*Bad -> Good cell,
or another source-coloured zero state.          (13)
```

The root-equality/PORT terminal is therefore closed size-independently; the
remaining global task is to route the strict extra root through its genuine
`tau` component without recycling its merger slot.
