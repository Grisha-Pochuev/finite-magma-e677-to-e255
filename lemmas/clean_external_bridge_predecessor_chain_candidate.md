# Clean External-Bridge Predecessor-Chain Candidate

Date: 2026-06-18.

Status:

```text
candidate / successor label identified, termination still not proved
```

## Purpose

This records the likely next finite argument for the clean external-bridge
residual of the proper bad-target crossed fan.

Do not treat it as proved.  The missing step is the exact recursion after the
second bridge `ell`.

## Starting Data

In the clean residual:

```text
h=pred_b(a),
k=pred_a(b),
t=a*b,
ell=t*a=pred_b(k).
```

The already proved relations are:

```text
b*h=a,
b*ell=k,
h!=ell,
a!=k.
```

Thus row `b` contains two distinct predecessor arrows:

```text
h -> a,
ell -> k.
```

The clean second-layer residual may assume:

```text
ell not in {a,b,c,d,u,v,h,k,t}.
```

## Candidate Mechanism

The hoped-for finite descent is:

```text
row-a bridge edge
=> fresh row-b predecessor arrow ell -> k
=> either ell hits the visible footprint
   or the self-labeled recursion creates another fresh predecessor arrow
   in row b
=> by finiteness, the first nonfresh hit is routed by the visible-hit cases.
```

This would turn the clean external bridge into a predecessor-chain problem,
similar in spirit to the older paired predecessor chain work:

```text
paired_predecessor_recursion_lemma.md
paired_chain_first_obstruction_lemma.md
paired_chain_cross_hit_lemma.md
```

## Missing Formal Step

What is not yet proved:

```text
Given the fresh arrow b*ell=k, construct a canonical next row/source that
forces b*ell_2=k_2 with ell_2 fresh unless a routed hit occurs.
```

The obvious self-labeled edge recursion applies to any row label `x`, but it
does not automatically say which next label should replace `a` in the clean
crossed-fan residual.

The correct successor label has now been identified by:

```text
bad_target_right_b_orbit_predecessor_recursion_lemma.md
```

It is:

```text
x_{i+1}=x_i*b.
```

For the first step, after `x_0=a`, the successor is:

```text
x_1=t=a*b.
```

The remaining missing proof is no longer the local recursion.  It is the
classification of the first repeat or first visible hit of this right-`b`
orbit/predecessor chain.

Local repeat roles for this chain are recorded in:

```text
right_b_orbit_local_repeat_roles.md
right_b_orbit_first_repeat_boundary.md
right_b_orbit_first_repeat_fan_lemma.md
```

These roles show that some first repeats are only recurrence boundaries, not
direct contradictions.  But the first repeat is not neutral: it creates a new
incoming fan in `H_b`.  The missing proof must show that this new fan cannot
close independently.

## Boundary Conditions Already Routed

The first nonfresh hit of `ell` is already classified:

```text
row_a_second_bridge_visible_hit_cases.md
```

The row-a output cases are also routed:

```text
row_a_bridge_edge_attachment_cases.md
bad_target_row_a_output_avoids_b_hub_lemma.md
row_a_bridge_loop_recurrence_boundary.md
```

So the remaining work is not more case-listing at the first bridge.  It is the
recursion step after a fresh second bridge.
