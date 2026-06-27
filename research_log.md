# E677 -> E255: текущий исследовательский журнал

Новый компактный журнал начат 2026-06-09 после архивирования полной истории.

Полный журнал за 2026-05-12 -- 2026-06-09:

```text
archive/research_log_full_through_2026-06-09.md
```

Актуальная математическая карта:

```text
CURRENT_FRONTIER.md
```

## Стартовый статус

Доказанные общие результаты текущего фронта:

```text
double_interval_edge_certificate_lemma.md
bicyclic_component_branch_fan_lemma.md
bad_target_core_fan_lemma.md
bicyclic_core_junction_lemma.md
target_swap_fan_duality_lemma.md
right_fixer_to_balanced_witness_lemma.md
```

Открытая цель:

```text
закрыть тройной ядровый веер и смешанный узел 2+1
через перенос полных сертификатов до первого слияния или цикла.
```

Кандидат Directed Two-Edge Witness остается модельной гипотезой. Два
ограниченных слоя ground-насыщения не дали доказательства. Без нового
промежуточного тождества глубину не повышать.

Следующие записи добавлять только если они содержат:

```text
- новое доказанное тождество;
- точный результат 1-3 целевых проверок и его структурный смысл;
- снятие ошибочного предположения;
- изменение единственного активного фронта.
```

## 2026-06-09: постоянный Node и воспроизводимая диагностика

Выполнена инфраструктурная оптимизация:

```text
tools/directed_two_edge_witness_diagnostics.js
run_directed_witness_diagnostics.ps1
install_portable_node.ps1
tools/node-portable/node.exe
```

Установлен переносной Node.js:

```text
v22.22.3
```

Постоянный скрипт воспроизводит прежнюю временную диагностику Node REPL:

```text
M496 parameters: zeta=8, omega=6
F7 E677: true, E255: true
M496 E677: true, E255: true
base directed paths: 144
product samples: 144
product path certificates: true
Y=(b*c)*(u*k) right-fixes b on product samples: true
right-fixer -> balanced witness conversion works: true
depth 1 synthesis: fresh=43, total=50
depth 2 synthesis: fresh=2153, total=2203
depth<=2 path-dependent z witnesses: none
```

Теперь временное состояние Node REPL не нужно восстанавливать вручную.

## 2026-06-17: mixed junction bridge square

For the outgoing-majority mixed junction:

```text
p*v=b, p*b=c
q*v=b, q*b=d
r*a=b, r*b=v
```

the target swap `b -> v` was made fully explicit. In `H_v` the same rows
form:

```text
p*alpha=v, p*v=b
q*gamma=v, q*v=b
r*b=v,     r*v=s.
```

Thus the junction becomes incoming-majority at `b`:

```text
alpha -> b
gamma -> b
b     -> s.
```

The two majority rows carry the bridge:

```text
h=c*p=d*q=pred_b(v),
b*h=v.
```

The minority row carries the opposite bridge:

```text
s*r=pred_v(b),
v*(s*r)=b.
```

Recorded as:

```text
mixed_junction_target_swap_bridge_square.md
```

This is a structural map only. It does not prove `h=s*r`, does not prove a
right fixer, and does not by itself keep the relayed edge inside a bicyclic
core of `H_v`.

Targeted diagnostic on `300` mixed junctions in the size-496 model:

```text
hEqualsJ: 0
hRightFixesB: 0
jRightFixesB: 0
edgeHtoJ: 0
edgeJtoH: 0
```

where `j=s*r=pred_v(b)`.

Interpretation: do not seek a proof by directly identifying the two bridge
labels or by turning one of them into a right fixer. The next comparison must
use full last-edge certificates.

Script:

```text
tools/mixed_junction_bridge_square_diagnostics.js
```

## 2026-06-17: first-merge certificate separation

For two directed branches in `H_b` first merging at `z`, write the last
edges:

```text
p*x=b, p*b=z,
q*y=b, q*b=z,
x!=y.
```

Let:

```text
H_x=z*p=pred_b(x),
H_y=z*q=pred_b(y),
U=p*z,
W=q*z,
K=U*p=W*q=pred_z(b).
```

Then:

```text
H_x!=H_y,
U!=W.
```

Reason:

```text
H_x=H_y => x=y;
U=W => rows p,q share b -> z -> U => p=q => x=y.
```

Recorded as:

```text
first_merge_certificate_separation_lemma.md
```

Consequence: the common terminal `K_z` is not enough, and the adjacent
last-certificate labels cannot be identified at a first merge. The remaining
local pressure is exactly the crossed equality:

```text
(p*z)*p=(q*z)*q=K.
```

## 2026-06-17: first-merge target-swap mixed relay

Continue the first-merge setup:

```text
p*x=b, p*b=z,
q*y=b, q*b=z,
x!=y.
```

If the cyclic core has a fresh outgoing continuation from `z`:

```text
t*z=b,
t*b=m,
t notin {p,q},
```

then after changing target from `b` to `z`, the same source rows form:

```text
p*b=z, p*z=U,
q*b=z, q*z=W,
t*theta=z, t*z=b.
```

So in `H_z`:

```text
b -> U
b -> W
theta -> b.
```

This is an outgoing-majority mixed `2+1` junction at `b`. Recorded as:

```text
first_merge_target_swap_mixed_relay.md
```

Interpretation: in the generic non-loop continuation case, a first merge is
not an endpoint. It becomes a new mixed split after swapping the target pair
`{b,z}`. The remaining separate boundary is the degenerate case where the
continuation uses `p`, `q`, or a loop at `z`.

## 2026-06-17: first-merge degenerate continuation boundary

The same-row part of the previous boundary is now closed.

If a genuine first merge has:

```text
p*x=b, p*b=z,
q*y=b, q*b=z,
x!=z,
y!=z,
```

and an outgoing continuation:

```text
t*z=b,
```

then `t=p` would imply:

```text
p*z=b
p*x=b
=> x=z
```

by row injectivity. Similarly `t=q => y=z`.

So a genuine outgoing continuation row is automatically fresh:

```text
t notin {p,q}.
```

The only remaining local boundary is the loop:

```text
t*z=b,
t*b=z.
```

After target swap `b -> z`, this becomes a loop `b -> b` in `H_z`, not a
right fixer. Recorded as:

```text
first_merge_degenerate_continuation_boundary.md
```

## 2026-06-17: first-merge target-swap junction dichotomy

The loop boundary has now been classified.

At a genuine first merge:

```text
p*x=b, p*b=z,
q*y=b, q*b=z,
x!=z,
y!=z,
x!=y,
```

write:

```text
U=p*z,
W=q*z.
```

Then:

```text
U!=W,
U!=b,
W!=b.
```

After changing target to `z`, the two last rows are:

```text
b -> U,
b -> W
```

in `H_z`.

If an outgoing continuation from `z` is non-loop:

```text
t*z=b, t*b=m, m!=z,
```

then target swap gives an incoming edge `theta -> b`; hence a mixed `2+1`
junction in `H_z`.

If it is a loop:

```text
t*z=b, t*b=z,
```

then target swap gives the loop `b -> b`; together with `b -> U` and
`b -> W`, this is a triple outgoing fan in `H_z`.

Recorded as:

```text
first_merge_target_swap_junction_dichotomy.md
```

Conclusion: first merge with outgoing continuation is closed under the same
two-type split:

```text
mixed 2+1 or triple fan.
```

The next separate boundary is a purely incoming core shape at the merge
vertex, if such a shape can occur in the selected branch-closure process.

Model orientation diagnostic:

```text
tools/core_orientation_diagnostics.js
```

on targets `0,1,17,31,255,495` of the known size-496 model gave:

```text
coreEdges=45
coreVertices=45
hist=(1,1):45
pureIncomingGe2=0
pureOutgoingGe2=0
```

for each target. This says only that the known good model has directed
cycle-like cores at those targets. It does not settle the hypothetical bad
target boundary.

Stage summary:

```text
branch_closure_relay_stage_2026-06-17.md
```

## 2026-06-17: pure-incoming merge target-swap fan

The pure-incoming boundary has been sharpened.

Suppose a vertex `z` has incoming incidences in `H_b`:

```text
p_i*x_i=b,
p_i*b=z.
```

Set:

```text
U_i=p_i*z.
```

After target swap `b -> z`, the same row gives:

```text
p_i*b=z,
p_i*z=U_i,
```

so every incoming incidence into `z` in `H_b` becomes an outgoing edge:

```text
b -> U_i
```

in `H_z`.

If `U_i=U_j`, the two rows contain the same ordered interval:

```text
b -> z -> U_i,
```

so two-step source reconstruction gives `p_i=p_j`, and row injectivity gives
`x_i=x_j`. Thus distinct incoming incidences give distinct tips after target
swap.

For a genuine first merge, `x_i!=z`, so also `U_i!=b`.

Recorded as:

```text
pure_incoming_merge_target_swap_fan_lemma.md
```

Conclusion: pure incoming degree at least three is not a new terminal
obstruction. It relays to a triple outgoing fan in `H_z`.

The remaining local first-merge boundary is now only:

```text
binary pure incoming sink:
two incoming branches,
no outgoing continuation,
no loop,
no third incoming incidence.
```

## 2026-06-17: binary sink core escape

The remaining binary pure incoming sink was reduced graph-theoretically.

Two branch paths with a common split `s` and first merge `z`, if they have no
earlier mutual intersection, form one simple undirected cycle:

```text
s ... z ... s.
```

A binary pure incoming sink has no extra incidence at `z`. Therefore, inside a
forced bicyclic core, the second independent cycle cannot be supplied at `z`.

Since the ambient core is connected and has at least two independent cycles,
the extra core material must attach before `z`:

```text
at the initial split s,
or at an internal vertex of one active branch path.
```

Recorded as:

```text
binary_sink_core_escape_lemma.md
```

Conclusion: the binary sink is not a standalone terminal obstruction. The next
frontier is the earliest side attachment to the two-branch corridor before the
sink.

## 2026-06-17: earliest side attachment is mixed 2+1

The earliest side attachment has now been classified.

Let an active directed branch path pass through an internal vertex `v`:

```text
x -> v -> y
```

with rows:

```text
p*x=b, p*b=v,
q*v=b, q*b=y.
```

Thus the path itself contributes one incoming and one outgoing incidence at
`v`.

If the extra core incidence is incoming:

```text
r*a=b,
r*b=v,
```

then `p,r,q` form an incoming-majority mixed `2+1` junction.

If the extra core incidence is outgoing:

```text
r*v=b,
r*b=c,
```

then `p,q,r` form an outgoing-majority mixed `2+1` junction.

If the side incidence is a loop, it is both incoming and outgoing and falls
under the same mixed/loop relay already classified.

Recorded as:

```text
earliest_side_attachment_mixed_junction_lemma.md
```

Conclusion: the binary pure incoming sink is not an independent obstruction.
Combined with the core-escape lemma, it relays back to the already retained
triple fan / mixed `2+1` framework.
