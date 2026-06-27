# Offset Source-Orbit First-Return Lemma

Date: 2026-06-04.

Status:

```text
candidate / symbolic refinement of the no-bridge orbit tail
```

Purpose:

```text
Start the no-bridge orbit from the offset edge itself, not from a local
case45 senior marker.
```

This refines:

```text
offset_bridge_orbit_dichotomy_lemma.md
no_bridge_orbit_tail_candidate.md
```

## Setup

Let:

```text
s=b_3
t=b_t=r_2
```

The offset edge is:

```text
s*t=b_4.
```

Now follow the row-`s` orbit beginning at `t`:

```text
c_0=t
c_1=b_4
c_{i+1}=s*c_i.
```

Thus:

```text
c_2=s*b_4
c_3=s*c_2
...
```

Because row `s` is a permutation in every finite E677 magma, this orbit is a
finite cycle.

## The Offset Relay Is The First Orbit Relay

For every two consecutive source edges:

```text
s*c_i=c_{i+1}
s*c_{i+1}=c_{i+2}
```

the inverse-edge chain gives:

```text
c_{i+1}*(c_{i+2}*s)=c_i.
```

For `i=0` this is:

```text
b_4*(c_2*s)=t.
```

Since:

```text
c_2=s*b_4
p=(s*b_4)*s=c_2*s,
```

we recover the offset relay:

```text
b_4*p=t.
```

So the offset relay is not an isolated trick.  It is the first return edge of
the row-`b_3` source orbit.

## First-Return Roles

The no-free-tail problem can now be stated as a first-return problem for:

```text
c_0=t
c_1=b_4
c_2=s*b_4
...
```

Track the first time this orbit meets the already occupied block:

```text
0, t, b_4, s, b_5, b_6, ...
```

The roles are:

```text
hit 0:
  zero-hit descent; if s*q=0 and s*0=r, then r*s=pred0(q).

return to t:
  a closed source cycle; every edge in the cycle has a forced reverse relay.

return to b_4:
  impossible before returning to t, because row s has unique predecessor
  of b_4, namely t.

hit s immediately at c_2:
  s*b_4=s, so row s itself is a bridge:
    s*t=b_4
    s*b_4=s.
  Therefore this is not a no-bridge branch.

hit s later:
  source row reaches its own label after a nontrivial prefix; this is a
  self-label boundary and should be treated like the self-loop/no-tail cases.

hit a lower bad-cycle point b_j:
  descent to an already named lower source row.
```

This is more precise than saying only:

```text
the row-b_3 orbit eventually hits something.
```

The first return has to be one of the roles above.

## No-Bridge Consequence

In a no-bridge branch:

```text
c_2 != s.
```

because:

```text
c_2=s*b_4=s
```

would make row `s` a bridge.

Therefore the first new source step after:

```text
t -> b_4
```

is genuinely outside:

```text
{s}
```

unless the branch already falls into the bridge case.

The expected compact-prefix-collapse lemma becomes:

```text
In a no-bridge branch, the row-s orbit starting
  t -> b_4 -> c_2 -> ...
cannot keep meeting fresh nonzero, nonoccupied values until it returns.
Before or at the first return, the relay edges
  c_{i+1}*(c_{i+2}*s)=c_i
force zero-hit descent, a closed source cycle, or descent to a lower occupied
source row.
```

## Why This Is Useful

This removes the case45-specific choice:

```text
start with b_1=8 and split by b_3*b_1.
```

That senior marker is still useful locally, but the general proof should start
from the universal offset orbit:

```text
b_t -> b_4 -> b_3*b_4 -> ...
```

The old senior-orbit checks now become evidence for one possible first-return
role, not the definition of the global no-bridge mechanism.

