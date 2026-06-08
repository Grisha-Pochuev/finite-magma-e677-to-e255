# Current Frontier

Date: 2026-06-08.

The project studies whether

```text
E677: x = y * (x * ((y * x) * y))
```

implies

```text
E255: x = ((x*x)*x)*x
```

in every finite magma.

The full implication is not yet proved.

## Latest proved mechanism

Suppose several source rows share an edge

```text
q*0=P
q*P=T
T*q=h.
```

Each source `q` forces a bridge

```text
w=(q*T)*q
T*w=P.
```

The bridge itself extends by a zipper step.  If

```text
V=T*P,
```

then

```text
V*T=pred_P(w)
P*(V*T)=w.
```

These statements are proved in:

```text
lemmas/fan_tip_bridge_expansion_lemma.md
lemmas/fan_bridge_zipper_extension_lemma.md
```

Thus a bridge is not a free endpoint.  It extends the forward orbit while also
returning one step backward in row `P`.

## Anchor to the original bad cycle

Let

```text
A=0*0=b_{m-1}.
```

The terminal element of the original bad cycle is itself a source:

```text
A*0=P.
```

Its backward fan foot is the old bad tail:

```text
A*r_{m-2}=0
0*(P*A)=r_{m-2}.
```

This is proved in:

```text
lemmas/terminal_source_anchored_fan_lemma.md
```

Therefore the recursive fan is not external to the old bad cycle.  One branch
is rigidly anchored to it.

## Current main candidate

The remaining candidate is:

```text
lemmas/three_source_good_six_pressure_candidate.md
```

Finite size-9 diagnostics show that three sources of the same edge produce
enough pressure to close the normalized good-six-cycle role.  This is evidence,
not a general proof.

The global candidates remain:

```text
lemmas/fan_spine_termination_candidate.md
lemmas/main_bad_cycle_no_free_tail_lemma.md
```

## Exact next question

Do not begin a new broad finite search.

The next structural task is:

```text
Classify the first intersection of the three bridge paths
with:
  their sources;
  existing fan tips;
  points of the good six-cycle;
  the old bad tail r_{m-2}.
```

For every bridge intersection, immediately use:

```text
T*w=P
V*T=pred_P(w).
```

The goal is either:

```text
return to an occupied bad tail;
an already forbidden aligned overlap;
an occupied-row pressure collision;
or a proof that the branching creates new distinct elements.
```

## Current status boundary

Proved:

```text
bridge from every common-edge source;
zipper extension from every bridge;
new common-edge fan when bridges collide;
terminal-source anchoring to r_{m-2};
short-cycle and aligned-return reductions recorded in the fan-spine lemmas.
```

Not proved:

```text
arbitrary three-source fan termination;
the No-Free-Tail Lemma;
E677 => E255 for all finite magmas.
```

