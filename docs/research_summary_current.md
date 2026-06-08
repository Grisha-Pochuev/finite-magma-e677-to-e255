# Current Research Summary

This is a compact English summary of the current state of the project.

## High-level picture

The project investigates whether the identity `E677` forces `E255` in every
finite magma.  The approach is structural rather than brute force:

1. assume a finite counterexample;
2. choose a bad element `0`;
3. derive forced edges from `E677`;
4. organize those edges into cycles, ladders, or pressure patterns;
5. use small computations only to test bounded structural branches.

## Closed finite regions

The public package records the following closed regions:

```text
sizes 5, 6, 7, 8: recorded closed
size 9, cases 1-33: recorded closed
case45 branch 7*0=4: recorded closed
normalized size-9 role u=b_3: recorded closed
```

The strongest reproducible checkpoint included in the public folder is the
size-8 verification script:

```powershell
.\verify_size8_closed.ps1
```

## Main proof candidate

The current global candidate is the **No-Free-Tail Lemma**:

```text
In a finite E677 magma, the bad-cycle construction cannot keep producing
fresh zero-avoiding tails.  Therefore the supposed bad element must satisfy
E255.
```

This is not yet a complete proof.  It is the organizing target for the next
research phase.

## Latest proved mechanism

Several source rows may share the forced edge

```text
q*0=P
q*P=T
T*q=h.
```

Every source then produces a bridge:

```text
w=(q*T)*q
T*w=P.
```

Every bridge also produces a backward zipper return.  If

```text
V=T*P,
```

then

```text
V*T=pred_P(w)
P*(V*T)=w.
```

The terminal source of the original bad cycle is anchored to the old bad tail
`r_{m-2}`.  These are general proved statements, recorded in the bridge,
zipper, and terminal-anchor lemma files.

## What remains open

The full theorem remains open in this repository.

The current candidate is the three-source good-six pressure lemma.  The next
mathematical task is to classify the first intersections of its three bridge
paths with the sources, fan tips, good six-cycle, and terminal bad-cycle
anchor.  This is a symbolic task, not a new broad computation.
