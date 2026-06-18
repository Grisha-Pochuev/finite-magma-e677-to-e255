# Next Action

Date: 2026-06-18.

Read this file first.  Then read `CURRENT_FRONTIER.md` only if more context is
needed.

## Current Goal

Continue the E677 -> E255 proof through the bad-target crossed-fan route.

Do not restart broad case search.

## Current Narrow Frontier

The clean proper bad-target crossed-fan residual has:

```text
h!=k,
{c,d} ∩ {u,v}=empty,
t=a*b,
k -> t in H_b,
ell=t*a=pred_b(k),
b*ell=k.
```

The right-`b` orbit is:

```text
x_0=a,
x_1=t,
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b).
```

Each row `x_i` gives:

```text
A_i -> x_{i+1}
```

in `H_b`.

## Important Correction

The right-`b` orbit is not itself an `H_b` path.  Consecutive generated
`H_b` edges do not automatically concatenate.

Use the stronger full ported states:

```text
E_i=(b,A_i,x_{i+1}).
```

## Next Proof Target

Prove a connector lemma:

```text
A closed ported-transition cycle from the clean external bridge must either
hit the visible crossed-fan footprint, create an independent full-interval
collision, become core-attached, or reduce to same-row recurrence.
```

Start from:

```text
right_b_orbit_repeat_core_attachment_gap.md
right_b_orbit_ported_transition_lemma.md
proper_crossed_fan_clean_external_bridge_boundary.md
```

## Do Not Repeat

Do not rerun broad size-8 crossed-fan timeouts.

Do not expect `t*b=a`, `t*b=t`, `t*b=h`, or `t*b=k` to close locally; these
were checked and routed in:

```text
right_b_orbit_second_successor_boundary.md
```

