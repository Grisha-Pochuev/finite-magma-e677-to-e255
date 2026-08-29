# E677 coloured bad-block renewal lemma

Date: 2026-07-21.

Status:

```text
proved that every D-HIT creates a Bad*Bad -> Good cell;
proved a global renewal map on all bad-row colour crossings;
proved the exact short-block/collision/unhit conservation law;
reduced HIT to short blocks, renewal collisions, or clean renewal cycles
```

Let

```text
C={ (y,x,z): y,x in Bad, z in Good, y*x=z }.      (1)
```

Its cardinality is the coloured crossing mass `C_BG` counted with row
multiplicity.

## Every HIT enters C

Suppose

```text
x in Bad,  D(x) in Good,
r=sigma(x),  s=x*x.                              (2)
```

If `r` is bad, the canonical cell

```text
r*x=D(x)
```

belongs to `C`.  If `r` is good, then either `s` is good and

```text
x*x=s
```

belongs to `C`, or `s` is bad and

```text
s*x=r
```

belongs to `C`.  Hence

```text
a Bad -> Good D-HIT implies C is nonempty.        (3)
```

This removes the former residual good-carrier exception at the level of
existence: it always exposes a coloured bad-row crossing through the self
band.

## Maximal bad blocks

Fix a bad-labelled row `y`.  Every crossing in (1) is the exit of a unique
complete maximal bad block in one cycle of the permutation `L_y`:

```text
row y: g Good -> b_0 -> b_1 -> ... -> b_(ell-1)=x -> z Good.  (4)
```

Conversely every such block has one exit in `C`; thus the blocks and `C` are
in bijection.  Put

```text
u=y*b_0,
q=u*y.                                           (5)
```

Companion factorization of the entry `y*g=b_0` gives

```text
b_0*q=g.                                         (6)
```

There are three exhaustive cases.

```text
Q_BAD:       q in Bad; then (b_0,q,g) is in C.
Q_GOOD_LONG: q in Good and ell>=2; then
             u=b_1 is Bad and (u,y,q) is in C.
SHORT:       q in Good and ell=1.                 (7)
```

In the SHORT case the exact five labels satisfy

```text
y*g=x,
y*x=z,
z*y=q,
x*q=g,                                           (8)
```

with `y,x` bad and `g,z,q` good.  The last two cells use (5)--(6).

Define the partial renewal map `R:C -> C` by the first two lines of (7),
using the block corresponding to the source crossing.  It is undefined
exactly on SHORT blocks.

For a Q_BAD entry pair `(g,b_0)`, the value

```text
q=b_0\g
```

depends only on the pair, not on the bad row `y`.  Therefore all
`N_B(g,b_0)` blocks with this entry pair renew to the same crossing
`(b_0,q,g)`.  This contributes at least `N_B(g,b_0)-1` to the renewal
collision surplus.  The Q_GOOD_LONG construction is injective within its
own type: from `(u,y,q)` one recovers `b_0=y\u` and hence the original block.

## Exact conservation

Let

```text
S = number of SHORT blocks,
I = number of distinct crossings hit by R,
K = sum_(c in image R)(|R^(-1)(c)|-1),
U = number of crossings in C with no R-predecessor.                  (9)
```

There are `|C|-S` defined renewal images counted with multiplicity, so

```text
|C|-S=I+K.
```

Since `U=|C|-I`,

```text
U=S+K.                                           (10)
```

This is the exact global bad-block law.  In particular, if `S=K=0`, then
`R` is a permutation of all coloured crossings and decomposes them into
clean renewal cycles.  There is no anonymous loss: every failure of a clean
cycle is exactly a SHORT block or a collision of renewal images.

The diagnostic

```text
tools\node.cmd tools\e677_coloured_block_renewal_verify.js cache\eq677-db
```

checks (4)--(10) on all `441` cached complete E677 models.  Those models have
`C=empty`, so this confirms the implementation but provides no positive
boundary example and is not evidence that the three residual cases are
impossible.

## Continuation boundary

By (3), excluding the three residual objects below excludes every HIT:

```text
SHORT block (8): couple its z-row companion to the unique Good fixers;
renewal collision K: charge its exact N_B fibre without reusing J/M;
clean R-cycle: expand all actual block and companion cells and test whether
               it closes to a coloured tau cycle or fills a bad diagonal.
```

Do not return to isolated canonical HIT blocks.  The correct object is the
simultaneous renewal system on all bad-row crossings.
