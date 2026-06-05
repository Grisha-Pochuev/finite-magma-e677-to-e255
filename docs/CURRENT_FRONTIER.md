# Current Frontier

Date: 2026-06-05.

This file is the current public continuation point for the finite-magma problem

```text
E677: x = y * (x * ((y * x) * y))
E255: x = ((x * x) * x) * x.
```

The project is trying to prove that every finite magma satisfying `E677` also
satisfies `E255`.

## Current main candidate

The current main candidate is the **No-Free-Tail Lemma**.

In the bad-cycle notation used in the project, let `0` be a hypothetical bad
element for which `E255` fails.  Define

```text
b_j = L_0^{-j}(0)
r_j = b_j * 0.
```

The target statement is:

```text
No-Free-Tail Lemma:
In a finite E677 magma, a bad element 0 cannot have r_2=b_2*0 != 0.
Therefore r_2=0, which is exactly E255 for 0.
```

## Strongest recorded obstruction

The current sharp obstruction is recorded in:

```text
lemmas/double_interval_pressure_lemma.md
```

The key observation is that a nonzero `r_2=t` is not merely part of one
two-sided row-`b_3` interval.  It becomes the common pivot of two forced
adjacent intervals:

```text
row b_2:
  u_2 -> 0 -> t

row b_3:
  c_{-1} -> t -> b_4
```

where

```text
u_2 = 0*(t*b_2)
c_{-1} = t*(b_4*b_3).
```

This combines with pressure in two additional rows:

```text
row t:
  z_t -> 0
  b_4*b_3 -> c_{-1}

row b_4:
  p -> t
  r_3 -> b_5
```

## Next mathematical question

The next meaningful step is not another broad finite search.

The next question is:

```text
Can the two forced intervals keep both predecessors fresh while avoiding
the row-t zero pressure and the row-b_4 occupied-row pressure?
```

The candidate answer is no.

## Immediate role split

The next work should split only by the role of `u_2`.

```text
u_2=t      -> origin self-swap 0 <-> t in row b_2
u_2=b_j    -> occupied bad-cycle row pressure/descent
u_2 fresh  -> track a second fresh interval together with c_{-1}
```

Any computation from this point should test one of these roles, not the whole
search space.

## Read next

Recommended reading order:

1. `docs/LEMMA_STATUS.md`
2. `lemmas/main_bad_cycle_no_free_tail_lemma.md`
3. `lemmas/offset_pressure_diamond_lemma.md`
4. `lemmas/double_interval_pressure_lemma.md`
5. `docs/CLOSED_CASES.md`

