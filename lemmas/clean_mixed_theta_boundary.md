# Clean Mixed-Theta Boundary

Date: 2026-06-17.

Status:

```text
candidate / normalized remaining boundary
```

## Purpose

The pure-incoming stage and side-attachment orientation reduction show that
the branch-closure frontier keeps returning to:

```text
triple fan,
mixed 2+1.
```

This file records the sharp mixed `2+1` shape that remains after all already
proved relays are applied.

It is not yet a proof of No-Free-Tail.

## Starting Mixed Junction

Fix a target `b`.  Consider an outgoing-majority mixed `2+1` junction at a
core vertex `v`:

```text
p*v=b, p*b=c,
q*v=b, q*b=d,
r*a=b, r*b=v.
```

Rows `p,q` start two outgoing branches:

```text
v -> c,
v -> d.
```

Row `r` is the incoming minority branch:

```text
a -> v.
```

The bridge-square labels are:

```text
h=c*p=d*q=pred_b(v),
k=v*r=pred_b(a),
s=r*v,
j=s*r=pred_v(b).
```

with:

```text
b*h=v,
v*j=b.
```

## Already Relayed Cases

Follow the two outgoing branches from `c` and `d` until their first merge or
until a side attachment forces a new junction.

The following cases are no longer independent boundaries.

### First Merge With Outgoing Continuation

Already relays by:

```text
first_merge_target_swap_junction_dichotomy.md
```

to:

```text
mixed 2+1,
or triple fan.
```

### Pure Incoming Merge Of Degree At Least Three

Already relays by:

```text
pure_incoming_merge_target_swap_fan_lemma.md
```

to a triple fan after target swap.

### Binary Sink With Internal Incoming Side Attachment

Already relays by:

```text
side_attachment_orientation_reduction_lemma.md
```

because an incoming side attachment is a first merge with outgoing
continuation.

### Binary Sink With Internal Outgoing Side Attachment

This creates a new outgoing-majority mixed `2+1` split before the sink.  It is
not a contradiction by itself, but it moves the active frontier from the sink
endpoint to the earlier side-attachment vertex.

## Clean Boundary Shape

After those reductions, the unresolved mixed boundary can be represented as a
clean mixed theta:

```text
one incoming minority edge enters v;
two outgoing majority branches leave v;
the two outgoing branches first meet at z;
z is a binary pure incoming sink;
there are no usable side attachments on the interiors of the two branches.
```

The last edges into the sink have the form:

```text
P*x=b, P*b=z,
Q*y=b, Q*b=z,
x!=y.
```

Define:

```text
U=P*z,
W=Q*z,
K=U*P=W*Q=pred_z(b).
```

Known separations:

```text
U!=W,
U!=b,
W!=b.
```

The remaining algebraic pressure is:

```text
U*P=W*Q=K,
```

together with the initial mixed bridges:

```text
c*p=d*q=h=pred_b(v),
s*r=j=pred_v(b).
```

## Next Algebraic Target

The next proof attempt should compare the initial mixed bridge square:

```text
b*h=v,
v*j=b
```

with the terminal merge bridge:

```text
z*K=b.
```

The desired contradiction is not expected from identifying the bridge labels
directly. Diagnostics already warn against shortcuts like:

```text
h=j
```

or right-fixer shortcuts.

The promising target is a path-ordered statement:

```text
in a clean mixed theta, the two outgoing branch certificates must eventually
force the same ordered two-step interval in two different source rows.
```

That would contradict two-step source reconstruction and prove the branch
closure step for this normalized boundary.

## Minimal-Layer Diagnostic

A short local diagnostic was run for the smallest labelled clean-theta layer:

```text
v -> c -> z,
v -> d -> z,
minority edge a -> v.
```

Using the existing E677 propagation script in `rawmodeldiagnose` mode, the
initial requirements did not immediately contradict E677.  The diagnostic
printed `status: ok` with large remaining row domains.

Interpretation:

```text
the clean-theta boundary is not closed by local two-edge propagation alone.
```

So the next proof should not try to close only the last two edges of each
branch.  It needs a full path invariant comparing the two certificate chains
between the shared bridge-pair endpoints.
