# Special Branch Low-Layer Meta Lemma

Date: 2026-06-03.

Status:

```text
candidate meta-lemma / strategic pivot
```

Scope:

```text
case45
7*0=5
6*5=5
```

This file is a deliberate step upward from layer-by-layer closure.  The point
is not to keep closing `6*6=4` mechanically after the full closures of
`6*6=2` and `6*6=3`.  The point is to extract the shared pattern and turn it
into a lemma candidate.

## Evidence Already Obtained

Two neighboring low layers are fully closed:

```text
6*6=2 -> closed
6*6=3 -> closed
```

In both layers the same role split closes the layer:

```text
immediate zero-hit
eventual zero-hit
low-successor prefix-collapse
direct killer exits
```

The layer `6*6=4` has only been started:

```text
6*4=0 -> already closed by zero-hit
6*4=1 -> direct check timed out at 60s
```

This timeout should not be treated as a reason to continue deeper in `6*6=4`.
It is the expected signal that direct search is the wrong shape and that the
meta-pattern should be formulated first.

## Observed Common Shape

For the closed low layers:

```text
6*6=k
k in {2,3}
```

the first source successor has the same form:

```text
6*k in {0,1,2,3,4,6,7,8} \ {k}
```

Equivalently:

```text
6*k avoids 5 and avoids k.
```

The expected same shape for the next low layer is:

```text
6*6=4
6*4 in {0,1,2,3,6,7,8}
```

This is consistent with the already closed zero-hit branch `6*4=0` and the
started timeout branch `6*4=1`.

## Candidate Role Split

For a low layer:

```text
6*6=k
k in {2,3,4}
```

classify the first source successor:

```text
s = 6*k
```

### Role A: zero-hit

```text
s=0
```

Then:

```text
6*0=r
r*6=pred0(k)
```

This is the clean source-orbit ladder consequence and is already confirmed for
`k=2,3,4`.

### Role B: direct killer

```text
s=6
```

This closes directly in the model layers.

### Role C: high successor

```text
s in {7,8}
```

In the closed layers `k=2,3`, the direct check may time out, but splitting by:

```text
6*s
```

closes by the same zero-hit plus direct-exit pattern.

### Role D: low-successor prefix-collapse

```text
s in {1,2,3,4} \ {k}
```

In the closed layers `k=2,3`, the next source edge:

```text
6*s
```

again splits into:

```text
zero-hit exit
direct killer exits
compact zero-avoiding exits
```

and the node closes.

## Candidate Lemma Statement

Working candidate:

```text
In the special branch case45, 7*0=5, 6*5=5, every low layer
6*6=k with k in {2,3,4} is killed by the same source-orbit role split.

The proof should not enumerate all cases.  It should prove that the successor
s=6*k falls into one of the four roles above, and each role is contradictory
by the finite E677 inverse-edge/source-orbit ladder.
```

Current evidence:

```text
k=2 -> fully checked
k=3 -> fully checked
k=4 -> zero-hit checked, first nonzero branch timed out directly
```

## Proof Skeleton To Extract

The closed layers `k=2` and `k=3` suggest the following proof skeleton.

### General row-0 predecessor ladder

There is a general row-0 consequence which should be used before any further
case split.

For every element `z`, E677 with:

```text
x=z
y=0
```

gives:

```text
z = 0*(z*((0*z)*0))
```

Since row `0` is the fixed 9-cycle, the preimage of `z` under row `0` is
`pred0(z)`.  Hence:

```text
z*((0*z)*0)=pred0(z)
```

or, using `succ0(z)=0*z`:

```text
z*(succ0(z)*0)=pred0(z)
```

This is the higher-level source of several previously found cells:

```text
5*(6*0)=4
6*(7*0)=5
k*((k+1)*0)=pred0(k) for k in {2,3,4}
```

In the current branch:

```text
7*0=5
6*5=5
```

the middle identity `6*(7*0)=5` becomes exactly `6*5=5`.
So the special branch is aligned with the row-0 predecessor ladder; it should
not be treated as an arbitrary local coincidence.

### Step 1: source successor restriction

Show that under:

```text
7*0=5
6*5=5
6*6=k
k in {2,3,4}
```

the value:

```text
s=6*k
```

cannot be:

```text
5 or k
```

This reduces the first source successor to:

```text
s in {0,1,2,3,4,6,7,8} \ {k}
```

This is not yet proved in this file; it is the first proof obligation.

Status update 2026-06-03:

```text
proved
```

Proof:

```text
6*5=5
6*6=k
k in {2,3,4}
```

Since every left row is a permutation, row `6` is injective.

If:

```text
6*k=k
```

then row `6` sends two different inputs `6` and `k` to the same output `k`,
contradiction.

If:

```text
6*k=5
```

then row `6` sends two different inputs `5` and `k` to the same output `5`,
contradiction.

Therefore:

```text
6*k notin {5,k}
```

### Step 2: zero-hit proof

If:

```text
s=0
```

then the source-orbit ladder gives:

```text
6*0=r
r*6=pred0(k)
```

The computational evidence says this role closes for `k=2,3,4`.

Proof obligation:

```text
derive contradiction from 6*6=k, 6*k=0, 6*0=r, r*6=pred0(k)
without enumerating all r.
```

Status update 2026-06-03:

```text
normal form extracted / not yet proved
```

Let:

```text
p = pred0(k)
```

So:

```text
0*p=k
```

Assume the zero-hit role:

```text
6*6=k
6*k=0
6*0=r
r*6=p
```

The source-orbit ladder applied to:

```text
6 -> k -> 0
```

gives:

```text
k*(0*6)=6
```

Since row `0` is fixed and `0*6=7`, this becomes:

```text
k*7=6
```

Now use E677 with:

```text
x=7
y=k
```

E677 says:

```text
7 = k*(7*((k*7)*k))
```

Using:

```text
k*7=6
6*k=0
7*0=5
```

this becomes:

```text
7 = k*5
```

So the zero-hit role always forces:

```text
k*7=6
k*5=7
r*6=pred0(k)
```

The same normal form also forces a second, row-5 return.

Use E677 with:

```text
x=5
y=0
```

Since row `0` is the fixed cycle:

```text
0*5=6
0*4=5
```

E677 gives:

```text
5 = 0*(5*((0*5)*0))
```

so the inner term must be the predecessor of `5` in row `0`, namely `4`:

```text
5*((0*5)*0)=4
```

Using:

```text
0*5=6
6*0=r
```

this becomes:

```text
5*r=4
```

So zero-hit is not only a row-6 return; it also forces the row-5 return:

```text
6*0=r
r*6=pred0(k)
5*r=4
```

### Shared-target inverse lift for L3

The strengthened normal form shows the next non-enumerative route.

Let:

```text
p=pred0(k)
```

There are two independent edges landing at the same target `p`:

```text
r*6=p
k*((k+1)*0)=p
```

The second edge is the row-0 predecessor ladder for `z=k`.

Applying the inverse-edge chain to both edges gives:

```text
r*6=p
=> 6 = p*((r*p)*r)

k*((k+1)*0)=p
=> (k+1)*0 = p*((k*p)*k)
```

So `L3` should be attacked by row `p`, not by enumerating `r`.
The row `p` is forced to contain the paired outputs:

```text
p*((r*p)*r)=6
p*((k*p)*k)=(k+1)*0
```

If the two inner inputs can be shown equal, or if `(k+1)*0` is forced into an
already used row-`p` output, the zero-hit role closes without an `r` split.
This is the current best higher-level target.

Also, by injectivity of row `6` and by `r*6=pred0(k)`, the return value `r`
cannot be:

```text
0, 5, 6, or k
```

Therefore:

```text
r in {1,2,3,4,7,8} \ {k}
```

This matches exactly the computational return sets in the closed model layers.

Remaining proof obligation:

```text
derive contradiction from the normal form:
  6*6=k
  6*k=0
  6*0=r
  r*6=pred0(k)
  k*7=6
  k*5=7
  5*r=4
  r notin {0,5,6,k}
```

This is now the precise target for `L3`.

### Step 3: low-successor prefix-collapse

If:

```text
s in {1,2,3,4} \ {k}
```

then the model layers show that the next source edge:

```text
6*s=t
```

again falls into the same small role split:

```text
t=0       -> zero-hit proof
t=6       -> direct killer
t in high -> high successor proof
t in low  -> compact prefix-collapse
```

Proof obligation:

```text
show that this descent cannot continue indefinitely without hitting one of the
killer roles.
```

This is the main conceptual gap.  The current computations prove it for
`k=2` and `k=3`, but not yet as a theorem.

### Step 4: high-successor proof

If:

```text
s in {7,8}
```

the model layers show direct search may time out, but splitting by:

```text
6*s
```

again gives:

```text
zero-hit plus direct exits
```

Proof obligation:

```text
explain why high successors are not a separate infinite family, but fold back
into the same source-orbit role split after one step.
```

### Step 5: direct killer proof

If:

```text
s=6
```

the node closes immediately in the model layers.

Proof obligation:

```text
derive the contradiction symbolically from 6*6=k and 6*k=6.
```

Status update 2026-06-03:

```text
proved
```

Proof:

Assume:

```text
6*6=k
6*k=6
k != 6
```

From the source-orbit ladder applied to:

```text
6 -> k -> 6
```

we get:

```text
k*(6*6)=6
```

Since `6*6=k`, this is:

```text
k*k=6
```

Now use E677 with:

```text
x=6
y=6
```

It gives:

```text
6 = 6*(6*((6*6)*6))
```

Using `6*6=k`, this is:

```text
6 = 6*(6*(k*6))
```

Since row `6` is injective and `6*k=6`, the unique preimage of `6` under row
`6` is `k`.  Therefore:

```text
6*(k*6)=k
```

Since row `6` is injective and `6*6=k`, the unique preimage of `k` under row
`6` is `6`.  Therefore:

```text
k*6=6
```

But we already have:

```text
k*k=6
```

So row `k` sends two different inputs `k` and `6` to the same output `6`,
contradicting injectivity of row `k`.

Thus:

```text
6*6=k, k != 6  ==>  6*k != 6
```

## Proposed Sublemmas

Instead of proving the whole meta-lemma at once, split it into small symbolic
sublemmas:

```text
L1. successor restriction:
    6*6=k, k in {2,3,4} => 6*k notin {5,k}
    status: proved by injectivity of row 6

L2. direct killer:
    6*6=k, 6*k=6 is impossible
    status: proved by source-orbit ladder + E677 x=6,y=6 + injectivity

L3. zero-hit killer:
    6*6=k, 6*k=0, 6*0=r, r*6=pred0(k) is impossible
    status: normal form extracted; key forced cells k*7=6 and k*5=7 are now
    proved symbolically

L4. high successor folds back:
    6*6=k, 6*k in {7,8} reduces after one source step to L2/L3/L5

L5. low prefix-collapse:
    6*6=k, 6*k=s low, s != k, reduces after one source step to L2/L3/L4
```

The immediate next symbolic target should now be `L3`, because `L1` and `L2`
are proved.

Update 2026-06-03:

```text
L3 universal row-k marker is proved:
  6*k=0 and 0*6=7 give k*7=6 by the source-orbit ladder.
  Then E677 with x=7,y=k gives k*5=7.
```

This creates a sharper transfer split:

```text
k=4:
  row k is row 4, so the marker k*5=7 interacts with 4*(5*0)=3 and leads to
  the row-5 descent / row-3 late trap.

k=2,3:
  row k is not row 4; the marker should close earlier or route into the
  already closed low-layer role split.
```

The late row-3 trap for the hard `k=4,r=1,w=2,a=3` representative is now
symbolically closed in `row3_late_trap_lemma.md`.  Current transfer map:

```text
l3_zero_hit_transfer_lemma.md
```

## Next Correct Work

Do not continue by simply closing every branch of `6*6=4`.

Next work should be:

```text
1. Prove or diagnostically confirm the common successor-shape:
   6*k avoids 5 and k for k in {2,3,4}.

2. Compare the already closed tables/diagnostics for k=2 and k=3 to extract
   the exact reusable prefix-collapse proof.

3. Use k=4 only as a sanity check for the extracted proof, not as another
   layer to exhaust mechanically.
```

The last interrupted branch:

```text
6*6=4
6*4=1
direct check -> timeout at 60s
```

should be recorded as a boundary signal, not as the next thing to brute force.
