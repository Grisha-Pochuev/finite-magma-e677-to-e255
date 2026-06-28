# Ported Interval Recurrence Boundary

Date: 2026-06-17.

Status:

```text
boundary clarification / prevents a false termination claim
```

## Purpose

The current No-Free-Tail route tracks full ported intervals:

```text
(target,input,output).
```

This is the correct state because it reconstructs the source row.  However,
not every repeated ported interval is automatically a contradiction.

## Collision That Really Contradicts Branching

If two independent active branch occurrences have:

```text
p*x=b, p*b=y,
q*x=b, q*b=y,
```

then the full ported interval `(b,x,y)` reconstructs the source row, so:

```text
p=q.
```

In a genuine fan, first merge, or side-attachment split, those two rows are
supposed to be distinct.  This is a real contradiction.

This is the useful recurrence:

```text
same full ported interval
in two independent branch roles
=> impossible.
```

## Recurrence That Is Not Enough

If the same source row returns to the same ported interval in the same branch
role, this is only a row-orbit recurrence:

```text
(b,x,y) --same row p--> ... --same row p--> (b,x,y).
```

That by itself is not a contradiction.  It just says row `p` has a cycle
through the displayed inputs.

This is formalized in:

```text
target_advance_row_orbit_lemma.md
```

Therefore relay termination cannot be stated as:

```text
any repeated full ported interval stops the proof.
```

It must be stated as:

```text
a repeated full ported interval in two independent branch roles stops the
proof; same-row recurrence is a separate boundary.
```

## Updated Relay Target

The remaining No-Free-Tail proof should show that a minimal closed relay cycle
has one of:

```text
1. a cross-role full ported interval collision;
2. a same-row recurrence that produces a smaller bad own-row cycle or a
   target-swapped shorter relay;
3. a strict clean theta, already excluded.
```

This file does not prove case 2.  It isolates it as the exact remaining
nonlocal obstruction after the local relay classifications.
