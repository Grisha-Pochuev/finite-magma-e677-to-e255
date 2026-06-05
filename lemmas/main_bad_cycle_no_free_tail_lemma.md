# Main Bad-Cycle No-Free-Tail Lemma

Date: 2026-06-04.

Status:

```text
main candidate lemma / not proved
```

Purpose:

```text
This is the current best candidate for a lemma that would solve the whole
finite E677 -> E255 problem.
```

The point is to stop treating the size-9 work as a list of cases.  The repeated
local mechanisms all say the same thing:

```text
a bad row-0 cycle cannot support a free relay tail.
```

## Global Setup

Assume, toward a counterexample, that `0` is a bad element:

```text
there is no y with y*0=0.
```

Let the row-0 cycle containing `0` be written backward as:

```text
b_j = L_0^{-j}(0)
```

so:

```text
0*b_j = b_{j-1}
```

with:

```text
b_0 = 0.
```

Write:

```text
r_j = b_j*0.
```

For the bad element `0`, E255 is equivalent to:

```text
b_2*0 = 0
```

so a counterexample must have:

```text
r_2 != 0.
```

## Proved Universal Pieces

### 1. Inverse edge chain

In every finite E677 magma, left rows are permutations and:

```text
a*z=c  ==>  z = c*((a*c)*a).
```

This is the basic relay rule.

### 2. Bad-cycle predecessor ladder

For every cycle element `b_j`, E677 with `x=b_j,y=0` gives:

```text
b_j*(b_{j-1}*0)=b_{j+1}
```

or:

```text
b_j*r_{j-1}=b_{j+1}.
```

This is the first global ladder along the bad cycle.

### 3. Source-orbit ladder

For any row `s`, if:

```text
s*z0=z1
s*z1=z2
```

then:

```text
z1*(z2*s)=z0.
```

More generally, every source-row orbit creates reverse relay constraints.

### 4. Source-row zero trap

This is the global version of the local `a_row_zero_trap_lemma.md`.

If a source row `s` has:

```text
s*0=a
s*a=b
c=b*s
```

then the source-orbit ladder gives:

```text
a*c=0.
```

Let:

```text
d=a*0.
```

Then the inverse-edge chain and row-0 cycle give:

```text
d*a=pred0(c)
```

and E677 with `x=c,y=a` gives:

```text
c=a*(c*succ0(a)).
```

So every two-step source orbit from `0` creates a trap:

```text
s*0=a
s*a=b
c=b*s
=> a*c=0
=> d=a*0, d*a=pred0(c), c=a*(c*succ0(a)).
```

This is no longer a row-5 accident.  Row `5` in the current special branch is
only one instance.

## Candidate Main Lemma

Working statement:

```text
No-Free-Tail Lemma.

In a finite E677 magma, a bad element 0 cannot have r_2=b_2*0 != 0.

More precisely, once the bad-cycle predecessor ladder
  b_j*r_{j-1}=b_{j+1}
is combined with source-orbit ladders and source-row zero traps, every possible
nonzero value of r_2 either:

  1. hits 0 and triggers a pred0 return;
  2. creates a collision in a left row;
  3. enters a source-row zero trap a*c=0;
  4. creates a self-loop/no-tail boundary that is killed by the next known edge.

Therefore r_2 must be 0, which is exactly E255 for the bad element 0.
```

If this lemma is proved, the whole finite problem is solved:

```text
for every x, E255 holds at x.
```

Reason:

```text
if E255 failed at some x, rename x to 0 and apply the No-Free-Tail Lemma.
```

## Evidence From Existing Work

### Size 8

The size-8 closure did not rely on random brute force at the end.  The decisive
split was already:

```text
k*0
```

where `k=L_0^{-1}(0)`.

This is the first appearance of the bad-cycle ladder as the controlling object.

### Size 9, cycle length 4

The hard cases with a 4-cycle around the bad element closed through the same
ladder:

```text
b_j*r_{j-1}=b_{j+1}
```

and second-level splits such as:

```text
2*0, 2*2, 2*3.
```

These are not arbitrary cells; they are relay descendants of the bad-cycle
ladder.

### Case45, branch `7*0=4`

The self-type branch was closed by relay graph mechanisms:

```text
known edge -> inverse chain -> next row -> no-tail trap.
```

This is the same pattern, but in the earlier notation.

### Case45, branch `7*0=5`

The current special branch gives the cleanest form.

Here:

```text
b_2=7
b_3=6
b_4=5
b_5=4
```

The branch:

```text
7*0=5
```

means:

```text
r_2=b_4.
```

The bad-cycle ladder gives:

```text
b_3*r_2=b_4
```

which becomes:

```text
6*5=5.
```

Then the next descent uses:

```text
5*(6*0)=4
4*(5*0)=3.
```

The local row-5 cascade:

```text
w=5*6
a=5*0
b=5*a
a*(b*5)=0
```

is exactly the source-row zero trap with `s=5`.

The newest restriction:

```text
a in {1,2,3,8} \ {w}
```

shows how a local branch becomes a finite role table above the late traps.

## Why This Could Be The Main Lemma

The same three operations explain all recent progress:

```text
1. move along the bad row-0 cycle by b_j*r_{j-1}=b_{j+1};
2. continue the active source row orbit;
3. if the source orbit reaches 0, apply pred0; if it avoids 0, it creates a
   zero trap or a row collision.
```

This is stronger than a search heuristic because each step is a direct E677
consequence.

The main missing proof is not another branch closure.  It is a termination
argument:

```text
show that the relay process cannot keep producing fresh nonzero, noncolliding
tails forever inside a finite bad-cycle normalization.
```

## Precise Current Gap

The current work proves the pattern in several important local settings, but
does not yet prove the global termination step.

Needed theorem:

```text
Every zero-avoiding source-orbit prefix generated by the bad-cycle ladder
either reaches a pred0 zero-hit, or strictly descends to a smaller bad-cycle
index, or collides with an already forced row output.
```

In the `7*0=5` special branch, the descent is visible:

```text
6 -> 5 -> 4 -> 3/8/2 traps.
```

For a full proof, this must be expressed without the special names
`6,5,4,3,8,2`.

## Next Correct Work

Do not keep closing isolated `k=4` tails first.

Next work should try to prove the missing termination statement in symbolic
bad-cycle notation:

```text
b_j, r_j, source row s, source orbit 0 -> a -> b -> ...
```

The first concrete target is:

```text
generalize the k=4 restriction
  a in {1,2,3,8} \ {w}
to bad-cycle notation:
  after s*0=a and s*u=v, the value a is restricted to already-known relay
  roles, not a new free value.
```

If this generalization fails, record exactly which local assumption from
`k=4` was essential.  That assumption is then the true boundary of the current
candidate main lemma.

## First Generalization: Occupied-Block Exclusion

New file:

```text
bad_cycle_descent_domain_template.md
```

The local `k=4` restriction has now been rewritten in bad-cycle notation.

In the special branch:

```text
b_1=8, b_2=7, b_3=6, b_4=5, b_5=4, b_6=3, b_7=2, b_8=1.
```

The local restriction:

```text
a in {1,2,3,8} \ {w}
```

is exactly:

```text
a outside {0,b_2,b_3,b_4,b_5} and a != w.
```

The template proves:

```text
a notin {0,b_2,b_3,b_4,b_5,w}.
```

Interpretation:

```text
the descent cannot choose a value from the already occupied bad-cycle block;
it must move to a small outside role set.
```

This is the first explicit form of the hoped-for no-free-tail invariant.

Current boundary:

```text
The exclusion a != b_3 uses the special fixed edge b_3*b_4=b_4
coming from the offset r_2=b_4.
```

So the global theorem likely needs an offset split:

```text
r_2=b_t
```

and for each offset, an analogous occupied-block exclusion.

## Offset Relay Template

New file:

```text
offset_relay_template_for_main_lemma.md
```

The offset split has a clean symbolic core.  If:

```text
r_2=b_t
```

then the bad-cycle ladder gives:

```text
b_3*b_t=b_4.
```

Applying the inverse-edge chain:

```text
b_t = b_4*((b_3*b_4)*b_3).
```

Let:

```text
u=b_3*b_4
p=u*b_3.
```

Then every offset has the relay:

```text
b_4*p=b_t.
```

For the special offset:

```text
t=4
```

this becomes:

```text
b_4*(b_4*b_3)=b_4,
```

which is the local marker:

```text
5*(5*6)=5.
```

For general `t`, this is weaker but still structured:

```text
b_4*p=b_t.
```

The important correction is:

```text
the global proof should not expect the same occupied block for every offset.
It should classify what p=(b_3*b_4)*b_3 does.
```

Three offset roles now look natural:

```text
1. p creates an occupied-output collision;
2. p=0 folds the offset relay into a=b_4*0;
3. a=b_3 creates a zero-hit b_4*succ0(b_3*b_4)=0.
```

This is the next version of the no-free-tail mechanism.
