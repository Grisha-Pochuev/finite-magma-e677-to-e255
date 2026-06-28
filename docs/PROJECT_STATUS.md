# Статус проекта

## Работа приостановлена 2026-06-09

Актуальный итог:

```text
STOP_CHECKPOINT_2026-06-09.md
```

Главный доказанный прогресс: одиночный мостовой хвост не может остаться
свободным в конечной магме; при первом повторении он создает новый
двухсторонний веер, причем новый центр равен старой мостовой метке.

Главный открытый кандидат: псевдолесность графа:

```text
A_b(q)--R_b(q).
```

Если она будет доказана, плохой элемент исключается счетом `n` ребер на
`n-1` вершинах. Пока это только сильная, многократно проверенная гипотеза.

## Active update 2026-06-09: одиночного свободного хвоста нет

Мостовая рекурсия полностью переписана как орбита правого умножения на `P`.
Доказано:

```text
любой конечный хвост либо возвращается в волокно источников,
либо при первом повторе создает новый двухсторонний веер общего ребра.
```

Основные новые файлы:

```text
right_p_orbit_bridge_recursion_lemma.md
right_p_orbit_collision_duality_lemma.md
cycle_entry_two_sided_fan_lemma.md
cycle_entry_hub_transport_lemma.md
good_p_unique_reverse_edge_lemma.md
right_fixed_point_uniqueness_lemma.md
```

В good-ветви единственное ребро столбца `P`, обратное ребру строки `P`, равно:

```text
e*P=f
P*f=e.
```

Поэтому выровненный цикл-вход классифицирован полностью. Главная
No-Free-Tail лемма еще не доказана: остается исключить рекурсивную смену
невыровненных общих ребер вдали от терминального якоря `r_{m-2}`.

При такой смене новый центр уже классифицирован: если повторенная вершина
удовлетворяет `Q*a_Q=P`, то общий возврат нового веера `P -> Q` равен ровно
`a_Q`. Для внешнего перехода в good-ветви `a_Q` не равен `0` или `P`.

## Работа приостановлена 2026-06-08

Актуальный полный итог:

```text
STOP_CHECKPOINT_2026-06-08.md
```

Найдены три новые общие доказанные леммы:

```text
fan_tip_bridge_expansion_lemma.md
fan_bridge_zipper_extension_lemma.md
terminal_source_anchored_fan_lemma.md
```

Они дают рекурсивную цепочку:

```text
q*0=P, q*P=T
=> T*((q*T)*q)=P
=> (T*P)*T=pred_P((q*T)*q).
```

Терминальный источник `A=0*0=b_{m-1}` привязывает этот механизм к старому
хвосту `r_{m-2}`. Главная No-Free-Tail лемма пока не доказана. Открытым остается
`three_source_good_six_pressure_candidate.md`: надо классифицировать первое
пересечение мостов с уже занятыми ролями, не начиная новый широкий перебор.

## Active update 2026-06-08: minimal bad-cycle fan spine

The fan-spine frontier has moved from four informal first-hit types to three
precise residual mechanisms.

General progress:

```text
common-edge fans extend in both directions;
e=C is a shared-edge descent and a badness transfer to a four-cycle;
tip-source collisions create explicit zero teeth;
aligned occupied tips and aligned zero-tooth returns are old-tail descents;
distinct internal source tips cannot form two-cycles.
```

Choosing a bad element with a minimal own-row cycle now gives a strict measure:

```text
if its cycle length is at least 5, e=C is impossible because it creates a bad
element with cycle length 4.
```

The short bases are separated:

```text
length 3 -> P*0=P and P*P escapes the bad three-cycle;
length 4 -> row b_3 contains r_2 -> 0 -> b_2.
```

Current open long-cycle roles:

```text
fresh/non-aligned zero-tooth return;
non-aligned occupied fan tip;
longer row-P cycle closure.
```

For the last role, the exact split is now:

```text
f=L_P^{-4}(P)
g=L_P^{-5}(P)

f*f=g  -> P satisfies E255;
f*f!=g -> P is bad and minimality bounds its cycle length from below.
```

An exact row-`P` cycle of length five is now proved bad as well. The first
unresolved shorter closure compatible with `P` being good has length six and
must satisfy:

```text
f*f=C
h*P=P.
```

If `C=b_j`, the good-P branch additionally forces:

```text
r_{j-2}!=P
```

and two occupied edges in row `b_{j-1}`. The next target is to terminate this
non-equal-tail pressure role.

The full No-Free-Tail Lemma remains open.

## Earlier stop checkpoint 2026-06-08

Work stopped at a clean structural boundary.

Completed:

```text
the full normalized size-9 role u=b_3 is closed;
C=b_7 -> status none, 46.31s, 640 nodes;
C=b_6 -> status none, 28.37s, 410 nodes.
```

The common forced mechanism was lifted from the finite checks to two general
proved lemmas:

```text
fixed_source_zero_descent_lemma.md
self_containing_fan_spine_lemma.md
```

They produce the active structure:

```text
row P: e -> h -> 0 -> P -> C;
fan tips: T_q*q=h for every q with q*0=P.
```

The next target is recorded in:

```text
fan_spine_termination_candidate.md
```

It remains open. In particular, the project has not proved the No-Free-Tail
Lemma or the full implication `E677 => E255`.

Resume only from the four structural first-hit types in the candidate file.
Do not return to the completed size-9 `C` split.

## Update 2026-06-07: source reconstruction and finite zero relay

New general theorem:

```text
p*a=b, p*b=c
=> p=pred_c(pred_b(a)).
```

So a two-step interval uniquely determines its source row.  This gives the
first exact aligned-overlap obstruction for the double-interval frontier:
the closed row-`b_2` and row-`b_3` cycles cannot share two aligned consecutive
edges.

The strongest bad-tail occupied role is also sharpened:

```text
r=u*0=b_4
```

forces one more zero source in the row-`b_3` orbit, but a third consecutive
zero source is impossible.  The apparent recursion therefore exits after one
relay.

Current large target:

```text
force an aligned two-edge overlap, or force an unequal-neighbor pressure role,
using the existing row-r_2 and row-b_4 fans.
```

The shared-edge fan was also generalized.  An exact edge match with row `0`
now gives explicit descent to `r_{k-1}`.  A size-496 diagnostic confirms that
large fans alone are harmless, so the proof must retain the bad-element
condition and bad-cycle geometry.

## Update 2026-05-31: special-branch role split advanced

Current new organizing files:

```text
special_branch_low_layer_meta_lemma.md
special_branch_role_split_lemma.md
```

New progress in:

```text
case45
7*0=5
6*5=5
6*6=2
```

Closed inside this layer:

```text
6*2=0 -> immediate zero-hit
6*2=1 -> prefix-collapse
6*2=3 -> prefix-collapse
6*2=4 -> prefix-collapse
6*2=6 -> direct killer
6*2=7 -> zero-hit plus direct exits
6*2=8 -> zero-hit plus direct exits
```

Status:

```text
case45, 7*0=5, 6*5=5, 6*6=2
status: closed
```

Interpretation:

```text
The source-orbit ladder is now part of a broader special-branch role split:
zero-hit, eventual zero-hit, and compact zero-avoiding prefix-collapse.
The first full neighboring layer is closed by this split, so the candidate is
now stronger than a local 6*6=8 repair.
```

Process note:

```text
The combined check of 6*2 in {6,7,8} timed out at the tool-call level and
was not counted.  These values were then checked one at a time and closed.
Transfer to 6*6=3 is now complete:
  6*3=0 closed by zero-hit
  6*3=1,2,4 closed by prefix-collapse
  6*3=6 closed directly
  6*3=7,8 closed by zero-hit plus direct exits
Loop checkpoint 2026-06-03:
  Do not continue mechanically into 6*6=4.
  6*6=4, 6*4=1 direct check timed out at 60s.
  Treat this as the signal to formulate the low-layer meta-lemma from the
  closed model layers 6*6=2 and 6*6=3.
Symbolic progress:
  General row-0 predecessor ladder extracted:
    z*(succ0(z)*0)=pred0(z).
  L1 successor restriction proved by injectivity of row 6.
  L2 direct killer proved by source-orbit ladder plus E677 x=6,y=6.
Next symbolic target:
  L3 zero-hit killer, now as a two-sided return trap:
    6*0=r, r*6=pred0(k), 5*r=4.
  Diagnostic update: attacking row p alone is too weak.
  Better next route is row-5 descent:
    w=5*6
    a=5*0
    4*a=3
    b=5*a
    a*(b*5)=0
  See row5_descent_bridge_lemma.md.
```

## Update 2026-05-31: source-orbit ladder role map

Current active candidate:

```text
source_orbit_ladder_lemma.md
source_orbit_role_map.md
```

Correction:

```text
The ladder depends on finite E677 left-row permutation / inverse edge chain.
```

New confirmed roles in:

```text
case45
7*0=5
6*5=5
6*6=8
```

```text
q=2, 6*2=0 -> immediate zero-hit closes without requiring h=2
q=4, 6*4=0 -> immediate zero-hit closes
q=7, 6*7=0 -> immediate zero-hit closes
q=4, 6*4=1, 6*1=0 -> delayed zero-hit closes
q=4, 6*4=2, 6*2=0 -> delayed zero-hit closes
q=7, 6*7=1, 6*1=2, 6*2=0 -> eventual zero-hit closes
```

Status:

```text
source-orbit ladder is a candidate role mechanism, not yet a complete
closure of the whole 6*6=8 layer.
```

Transfer check:

```text
Neighboring layers also have the zero-hit role:
6*6=2: 6*2=0, 6*0=r, r*6=1 closes for r in {1,3,4,7,8}.
6*6=3: 6*3=0, 6*0=r, r*6=2 closes for r in {1,2,4,7,8}.
6*6=4: 6*4=0, 6*0=r, r*6=3 closes for r in {1,2,3,7,8}.
```

Boundary:

```text
6*6=6 is a self-loop layer.  A non-root zero-hit test 6*8=0 closed r=7 but
timed out for r=2 and r=3.  Do not continue by raising limits; switch to a
self-loop/no-tail invariant.
```

Resolution:

```text
double_fixed_self_loop_lemma.md
6*5=5, 6*6=6, u=5*6 => 5*u=5.
u in {1,2,3,7,8} all close, so the special-branch layer 6*6=6 is closed.
```

## Update 2026-05-27: strategic pivot to two-sided relay square

## Update 2026-05-27: source-orbit ladder candidate

The two-sided square has been strengthened to a more general source-orbit
ladder:

```text
source_orbit_ladder_lemma.md
```

Key case45 zero-hit rule:

```text
6*q=0
6*0=t
=> 0*(t*6)=q
=> t*6=pred0(q)
```

because row `0` is the fixed 9-cycle.

Current confirmed application:

```text
q=2
6*2=0
r=6*0
=> r*6=1
```

All admissible `r` values closed:

```text
r in {1,3,4,7}
```

This closes the stubborn subnode:

```text
6*6=8
q=6*8=2
s=6*2=0
h=2*6=2
```

Boundary check on another zero-hit representative:

```text
q=3
6*3=0
r=6*0
r*6=pred0(3)=2
```

closed `r=2,4,7`, but `r=1` timed out.  So zero-hit is useful but not a
complete closing lemma.  The next role to understand is:

```text
8 -> 3 -> 0 -> 1
```

Next work should classify source row-6 orbit roles, not enumerate h/s cases.

The current work should move from local q-branch closure to a candidate lemma:

```text
two_sided_relay_square_lemma.md
```

Current structural situation:

```text
case45
7*0=5
6*5=5
6*6=8
q=6*8
```

Define:

```text
h=q*6
s=6*q
r=s*6
```

The two sides are:

```text
8*h=6
q*r=8
```

Reason for pivot:

```text
q=1 closed after using s=6*1.
q=2 did not close from s=6*2 alone.
Even q=2, s=0, 2*7=8 still timed out.
Adding h=2*6 helped only partly.
```

Next meaningful work:

```text
compare q=1 and q=2 structurally
find the missing diagonal constraint
do not enumerate remaining q/h/s cases mechanically
```

## Update 2026-05-26: special branch layer `6*6=1` closed

In the special branch:

```text
case45
7*0=5
6*5=5
```

the layer:

```text
6*6=1
```

is closed.

Mechanism:

```text
6*6=1
q=6*1
h=q*6
=> 1*h=6
```

The hard final q-layer was:

```text
q=8
```

and it closed by a two-level return to the source row-6 orbit:

```text
6*1=8
6*8=m
m*6=k
8*k=1
```

Closed special-branch layers so far:

```text
6*6 in {0,1,7}
```

Current remaining frontier:

```text
case45
7*0=5
6*5=5
6*6 in {2,3,4,6,8}
```

Details:

```text
t5_k1_row1_relay_progress.md
```

## Update 2026-05-25: first closed layer in special branch `t=5`

## Update 2026-05-25: second closed layer in special branch `t=5`

## Update 2026-05-25: current active frontier `t=5, 6*6=1`

Current active layer:

```text
case45
7*0=5
6*5=5
6*6=1
```

Progress:

```text
q=6*1 in {0,2,3,4,6,7,8}
q=0 closed
q=6 closed
q=2 closed by h=2*6 and 1*h=6
```

Remaining:

```text
q=6*1 in {3,4,7,8}
```

Details:

```text
t5_k1_row1_relay_progress.md
```

In the branch:

```text
case45
7*0=5
6*5=5
```

the layer:

```text
6*6=7
```

is also closed. The mechanism is row-7 relay:

```text
q=6*7
h=q*6
=> 7*h=6
```

Details:

```text
t5_k7_row7_relay_lemma.md
```

Current `t=5` frontier:

```text
6*6 in {1,2,3,4,6,8}
```

In the remaining top branch:

```text
case45
7*0=5
6*5=5
```

the layer:

```text
6*6=0
```

is closed. The mechanism is zero-pass-through:

```text
6*6=0
r=6*0
=> r*6=5
```

Coverage:

```text
r=1,2,3,4 closed directly
r=8 closed by the next orbit split s=6*8 in {1,2,3,4,7}
```

Details:

```text
t5_zero_pass_through_lemma.md
```

Current frontier:

```text
7*0=5
6*5=5
6*6 in {1,2,3,4,6,7,8}
```

Дата: 2026-05-24

Главная точка входа для продолжения: `CONTINUE_HERE.md`.

Старые логи сохранены как история работы и могут содержать промежуточные
таймауты, которые позже были закрыты. Если есть противоречие между старой
записью и `CONTINUE_HERE.md`, считать актуальным `CONTINUE_HERE.md`.

## Обновление 2026-05-25: закрыты self-layers `t=2` и `t=3`

В `case45` закрыты два соседних self-layer:

```text
7*0=t
6*t=5
6*6=6
6*5=t
t in {2,3}
status: closed
```

Механизм:

```text
no-bridge -> senior orbit relay from 6*8
bridge -> bridge-transfer 6*a=t*6
```

Для `t=2` и `t=3` закрыты обе части:

```text
no-bridge closed
bridge branch closed
```

Следующий этап: оформить это как candidate local lemma и проверить перенос на
особую верхнюю ветку `t=5`.

## Обновление 2026-05-25: орбитальная релейная лемма строки 6

Новый рабочий кандидат:

```text
row6_orbit_relay_lemma.md
```

Общая формула:

```text
6*z0=z1
6*z1=z2
=> z1*(z2*6)=z0
```

Это обобщает `senior_column_fallback_lemma.md`: прежнее

```text
6*8=m
6*m=r
=> m*(r*6)=8
```

является только первым шагом орбиты элемента `8` в строке `6`.

Проверенные no-bridge представители:

```text
t=2, 6*8=1, 6*1=3 -> row6 domain 16
t=2, 6*8=1, 6*1=0 -> row6 domain 18
t=3, 6*8=1, 6*1=2 -> row6 domain 16
```

Важный вывод: после двух ребер орбиты строка `6` действительно становится
маленькой, но попытка ветвиться по этим кандидатам уходит в таймаут. Поэтому
следующий правильный разрез:

```text
zero-hit orbit vs zero-avoiding orbit
```

а не перебор оставшихся 16-18 вариантов строки `6`.

Дополнительный результат:

```text
t=2: zero-avoiding 3-cycle 8 -> 1 -> 3 -> 8 closes all 4 row6 shapes
t=3: zero-avoiding 3-cycle 8 -> 1 -> 2 -> 8 closes all 3 row6 shapes
t=2: early zero-hit 8 -> 1 -> 3 -> 0 closes all 4 row6 shapes
```

Такой короткий zero-avoiding цикл теперь считается killer sublayer, а не
живым направлением для поиска контрпримера. Ранний zero-hit тоже ведет себя
как killer sublayer.

Закрыт один полный no-bridge orbit-prefix:

```text
t=2
6*8=1
6*1=3
```

Разрез по `6*3 in {0,4,7,8}` закрыл все подслои. Это локальный конечный
сертификат для префикса `8 -> 1 -> 3`, но еще не общая лемма для всех
префиксов орбиты.

Закрыт второй role-distinct prefix:

```text
t=2
6*8=1
6*1=0
```

Разрез по `6*0 in {3,4,8}` закрыл все подслои: `6*0=8` сразу противоречив,
а `6*0=3,4` закрываются конечными row-6 формами.

Закрыт senior 2-cycle prefix:

```text
t=2
6*8=1
6*1=8
```

Разрез по `6*0 in {3,4,7}` закрыл все 14 row-6 форм. В слое `6*8=1`
теперь закрыты `6*1 in {0,3,8}`; остаются только `6*1 in {4,7}`.

Оставшиеся `6*1=4` и `6*1=7` также закрылись прямым целевым поиском:

```text
6*1=4 -> status none, 27.24s
6*1=7 -> status none, 27.29s
```

Итог:

```text
t=2 no-bridge, 6*8=1 closed
```

Закрыт второй marker:

```text
t=2 no-bridge, 6*8=8 closed
```

Механизм другой: fixed-point `8 -> 8` переносит активность в строку `8`:

```text
8*(8*6)=8
```

Разрез по `8*6 in {0,2,3,4,5}` закрыл все подслои.

Закрыт весь no-bridge слой для `t=2`:

```text
t=2
no bridge
status: closed
```

Покрытие markers:

```text
6*8=1 closed
6*8=8 closed
6*8=3,4,7 closed
```

Остающийся фронт в `t=2` self layer:

```text
bridge branch
```

Там есть мостовая строка `a` с:

```text
a*2=5
a*5=6
=> 6*a=2*6
```

Обновление: bridge branch тоже закрыта полностью.

```text
t=2 bridge rows a in {1,3,4,7,8}
status: closed
```

Итог:

```text
t=2
7*0=2
6*2=5
6*6=6
6*5=2
status: closed
```

Следующий фронт:

```text
t=3 self-layer
7*0=3
6*3=5
6*6=6
6*5=3
```

Обновление: no-bridge часть `t=3` также закрыта.

```text
t=3 no-bridge
6*8 in {1,2,4,7,8}
status: closed
```

Следующий фронт:

```text
t=3 bridge branch
```

## Обновление 2026-05-24: bridge-transfer кандидат

После закрытия ветки `7*0=4` найден новый ручной перенос маркера для следующих
верхних веток:

```text
6*t=5
6*5=s
a*t=5
a*5=6
=> 6*a=s*6
```

Файл:

```text
marker_bridge_transfer_lemma.md
```

Смысл: старый маркер `6*0=s*6` был частным случаем, где мостовой строкой была
строка `0`. Для `7*0=2,3` нужно классифицировать мостовые строки `a`, а не
продолжать старый разрез `6*0`.

Уточнение после pair-forbid диагностики: мост не является обязательным. Если
запретить все локально возможные мосты, ветки `t=2` и `t=3` остаются живыми.
Поэтому текущая развилка:

```text
bridge branch -> использовать 6*a=s*6
no-bridge branch -> следующий маркер 6*8=6*b1
```

Дополнение: в no-bridge ветке фиксация `6*8=m` сжимает строку `6` до малого
остатка:

```text
t=2,3: row6 domain <= 90 after fixed 6*8=m
```

Найдено ролевое объяснение этого fallback:

```text
senior_column_fallback_lemma.md
```

Если `6*8=m`, `r=6*m`, `h=r*6`, то:

```text
m*h=8
```

Для `m=0` это дает `(6*0)*6=7`.

## Текущий математический статус

- Размеры `5`, `6`, `7`, `8` закрыты: конечных контрпримеров там нет.
- Размер `8` воспроизводимо подтвержден логом `size8_verified_split_log.txt`.
- В размере `9` закрыты cases `1-33`.
- В `case 45` полностью закрыты ветки:

```text
7*0=7
7*0=1
7*0=8
```

- В текущей зоне `7*0=4` полностью закрыт узел:

```text
6*6=6
```

- Senior/far transfer в этой self-swap ветке закрыт полностью.
- Zero-return `5*4=0` в этой зоне тоже уже закрыт.
- Все возможные значения `6*5=s` внутри этого узла закрыты:

```text
s in {1,2,3,4,7,8}
```

## Актуальная точка продолжения

Крупный новый результат:

```text
case 45
7*0=4
status: closed
```

Причина: в этой ветке `6*4=5`, значит `6*6=5` невозможно, а все остальные
значения

```text
6*6 in {0,1,2,3,4,6,7,8}
```

закрыты. Подробности:

```text
case45_7zero4_closed.md
```

Следующий фронт:

```text
case45
7*0=2
7*0=3
7*0=5
```

Следующий вопрос: переносится ли row-6 / low-to-low relay структура из
закрытой ветки `7*0=4` на эти верхние ветки.

Новый актуальный фронт:

```text
case 45
7*0=4
6*6=7
low-to-low transfer
6*5=s, s in {1,2,3,4}
6*0=u=s*6, u in {1,2,3,4} \ {s}
```

Найден кандидат на двухслойную low-to-low лемму:

```text
q=u*6
6*(0*q)=0

compact u=1,4:
  q-layer closes directly

wide u=2,3:
  all q close directly except q=7=b2
  q=7 closes by the second marker r=6*7=b3*b2
```

Sanity check в соседнем слое `6*6=8` подтвердил тот же механизм:

```text
6*6=8,s=2,u=1 compact -> q-layer closed
6*6=8,s=2,u=3 wide -> q-layer plus r-layer closed
6*6=8,s=4,u=2 wide -> q-layer plus r-layer closed
u=7 in s=2/4 -> closed directly
```

Статус: это уже не просто диагностика. Ролевая формулировка вынесена в:

```text
low_to_low_role_lemma.md
```

Следующий шаг - обновить карту оставшихся типов во всей ветке `7*0=4` и
выбрать следующий фронт уровнем выше, а не продолжать low-to-low перебор.

Последний закрытый широкий фронт:

```text
case 45
7*0=4
{6*6,6*5}={7,8}
status: closed
```

Обе ориентации закрыты:

```text
6*6=8, 6*5=7 -> closed
6*6=7, 6*5=8 -> closed
```

Общий механизм:

```text
u=(6*5)*6=6*0
q=u*6
6*(0*q)=0
```

Предыдущий закрытый фронт:

```text
case 45
7*0=4
6*6=8
6*5=7
status: closed
```

Ранее закрытый self-узел:

```text
case 45
7*0=4
6*6=6
status: closed
```

Новый компактный остаток строки `6` описан в
`row6_compact_residual_lemma.md`. Внутри узла `6*6=8` теперь закрыты:

```text
6*5=7
6*5=1
6*5=3
```

Значение `6*5=7` закрылось через `u=1,2,3`, включая новую лемму вторичного
self-type. Значения `6*5=1` и `6*5=3` закрылись первым `q`-слоем.

Следующая разумная точка продолжения:

```text
case 45
7*0=4
compare layers 6*6=7 and 6*6=8
open low values of 6*5
```

Причина поворота: cross-pair уже закрыт с обеих сторон. Теперь нужно искать
следующий более общий тип для низких значений:

```text
6*6=8: open 6*5 in {2,4}
6*6=7: open 6*5 in {1,2,3,4}
```

Следующее действие: коротко сравнить диагностически:

```text
6*6=7, 6*5=1
6*6=7, 6*5=3
```

Обновление после checkpoint 2026-05-24: сравнение низких значений уже дало
повторяемый маркер `u=8`. В слое `6*6=7` закрыты представители:

```text
6*5=1, u=8 -> closed by q-layer
6*5=2, u=8 -> closed by q-layer
6*5=3, u=8 -> closed by q-layer
6*5=4, u=8 -> closed by q-layer
```

Во всех четырех случаях:

```text
q=8*6 in {0,1,2,6}
6*(0*q)=0
```

Слой `u=8=b1` закрыт для всех низких `s=1,2,3,4`. Следующий шаг не должен
быть механическим закрытием оставшихся низких `u`. Нужно искать следующий
ролевой маркер для low-to-low transfer:

```text
u=s*6=6*0 in {1,2,3,4} \ {s}
```

Новая диагностика low-to-low показывает, что различие идет по роли целевого
`u`:

```text
u=1=b8 -> компактный слой, q in {0,1,2,6}
u=4=b5 -> компактный слой, q in {0,1,2,7}
u=2=b7 -> широкий слой, q in {0,1,2,6,7}
u=3=b6 -> широкий слой, q in {0,1,2,6,7}
```

Следующий шаг: объяснить этот split, а не закрывать low-to-low узлы списком.

Новая кандидат-лемма:

```text
secondary self-type relay lemma
```

Она закрыла хвост `u=2,q=2` без недоказанной связи `3*0=h`:

```text
b3*0=u
u*b3=u
s=b3*u
h=s*b3
u*h=0
r=u*0
r*u=pred0(h)
```

Подробности: `secondary_self_type_relay_lemma.md`.

## Текущая кандидат-лемма

Рабочее название:

```text
u-transfer / no-tail trap
```

Основная цепочка:

```text
s=6*5
u=s*6
=> 5*u=4
=> 6*0=u

q=u*6
=> 6*(0*q)=0
```

Проверено:

```text
s=1,u=2 -> закрыто по q=0,1,2,7
s=1,u=3 -> закрыто по q=0,1,2,7
s=1,u=4 -> закрыто по q=1,2,7
s=1,u=8 -> закрыто по q=0,1,2
s=2 -> закрыто полностью по u,q-слоям
s=3 -> закрыто полностью по u,q-слоям
s=7 -> закрыто полностью по u,q-слоям
s=8,u=1 -> закрыто
s=8,u=2 -> закрыто
s=8,u=3 -> закрыто по q=0,1,7
s=8,u=4 -> закрыто по q=1,2,7
```

Итог:

```text
7*0=4, 6*6=6 -> закрыто полностью
```

## Путеводитель

- `CONTINUE_HERE.md`: главный файл для продолжения.
- `LEMMA_STATUS.md`: компактная карта статусов лемм и аудитов.
- `RESULTS_INDEX.md`: карта файлов результата.
- `PROJECT_STATUS.md`: широкий статус проекта.
- `u_transfer_no_tail_trap_lemma.md`: текущая кандидат-лемма.
- `row6_compact_residual_lemma.md`: новый компактный остаток строки `6` после
  переноса `u-transfer` на соседний узел `6*6=8`.
- `secondary_self_type_audit.md`: актуальная поправка и новый широкий план для
  открытого вторичного self-type `u=2,q=2`.
- `secondary_self_type_relay_lemma.md`: новая кандидат-лемма, закрывшая
  `u=2,q=2` и весь узел `6*6=8, 6*5=7`.
- `row6_cross_pair_transfer_lemma.md`: новый широкий объект для зеркальных
  слоев `6*6=8,6*5=7` и `6*6=7,6*5=8`.
- `research_log.md`: полный исследовательский журнал.
- `research_summary_current.md`: широкая карта, включает исторические записи.

## Проверка размера 8

- `archive/size8_remaining_log.txt` - исторический промежуточный лог. В нем есть
  таймауты по cases `19-30`, поэтому он не является финальной проверкой.
- `size8_verified_split_log.txt` - текущий проверочный лог. Он получен свежим
  запуском `verify_size8_closed.ps1` на текущем усиленном инструменте поиска.
- Свежая проверка закончилась строкой:

```text
Done: all size-8 cases closed.
```

## Историческое структурное направление 2026-05-19

Важно: этот раздел оставлен как история. Актуальная точка продолжения находится
вверху файла и в `CONTINUE_HERE.md`.

Главный повторяющийся шаблон, который уже был выделен и закрыт как подслучай:

```text
b_2*0 = b_2
b_2*b_2 = b_{m-1} = 0*0
```

Текущий конкретный маршрут продолжения:

```text
case 45
закрыто: 7*0=7, 7*0=1, 7*0=8
текущая исследовательская зона: 7*0=2,3,4,5
общий первый маркер по диагностике: строка 6, особенно клетки 6*6 и 6*0
текущий частичный хвост: 7*0=4, 6*6=6, 6*1=1, 6*7=2/3
важно: этот хвост не добивать механически, пока не сравнена вся семья 7*0=2,3,4,5
```

Известная опорная структура:

- `b_j = L_0^{-j}(0)`;
- `r_j = b_j*0`;
- лестница: `b_j * r_{j-1} = b_{j+1}`;
- `(0*0)*0 = b_2`;
- `E255` для плохого элемента `0` эквивалентно `b_2*0 = 0`.

## Исторический путеводитель по файлам 2026-05-19

Важно: актуальный путеводитель вынесен в `RESULTS_INDEX.md`.

- `PROJECT_STATUS.md`: самый короткий актуальный статус.
- `case45_active_row_audit.md`: короткий аудит активных строк в `case 45`.
- `long_cycle_r2_classification.md`: широкая классификация веток по значению
  `r_2=b_2*0` для длинных циклов размера `9`.
- `inverse_edge_chain.md`: общая обратная цепочка известного ребра
  `a*z=c ==> c*((a*c)*a)=z`.
- `research_summary_current.md`: широкая рабочая карта; содержит также
  исторические записи.
- `research_log.md`: подробный исследовательский журнал.
- `size8_verified_split_log.txt`: финальная воспроизводимая проверка размера
  `8`.
- `archive/size8_remaining_log.txt`: старый промежуточный лог с таймаутами.
- `tools/search_counterexample_strong.js`: текущий главный инструмент поиска и
  диагностики. В нем добавлен режим `rowscores` для оценки только выбранных
  строк.

## Историческая сохраненная точка продолжения 2026-05-19

Важно: эта точка устарела. Актуальная точка продолжения:
`7*0=4, 6*6=6, 6*5=s`, где `s in {1,2,3,7,8}`.

Актуальная точка продолжения, зафиксированная в журнале:

```text
case 45
closed branches of 7*0: 7*0=7, 7*0=1, 7*0=8
current branch: 7*0=4
inside 7*0=4 closed: 6*6=0, 6*6=1, 6*6=2, 6*6=3, 6*6=4
inside 7*0=4 current: 6*6=6
inside 6*6=6 closed: 6*1=0
inside 6*6=6 partial: 6*1=1
inside 6*1=1 closed: 6*7=0
inside 6*1=1 remaining/timeouts: 6*7=2, 6*7=3
inside 7*0=4 not yet closed at 6*6 level: 6*6=7, 6*6=8
diagnostics for 6*6=7,8: active row 6
other remaining branches of 7*0: 7*0=2, 7*0=3, 7*0=5
```

Главная рабочая гипотеза после аудита 2026-05-19: для оставшихся веток
`7*0=2,3,4,5` первый общий структурный маркер - строка `6`. Причина:
после фиксации `r_2=7*0=t` лестница дает `6*t=5`. Так как строка `6` является
перестановкой, `6*6=5` уже невозможно, и клетка `6*6` становится естественным
общим разрезом. Ветка `7*0=5` особая, потому что там `6*5=5`, и строка `5`
включается раньше. Следующий осмысленный шаг - сравнить отдельно семью
`7*0=2,3,4` через `6*6`, а `7*0=5` держать как особый подтип.

Дополнение: при `6*6=0` для всех `7*0=2,3,4,5` активной снова остается строка
`6`. Для текущей ветки `7*0=4` также проверены хвосты `6*6=7` и `6*6=8`; они
тоже указывают на строку `6`. Следующая цель - лемма о заполнении строки `6`
после условий `6*t=5` и выбранного значения `6*6`, а не дальнейшее ручное
закрытие хвоста `6*7=2/3`.

Шире, для cases `34-45`, правильная ролевая формулировка такая:

```text
если r2=b_2*0=t, то b_3*t=b_4
```

Поэтому обычные ветки должны изучаться через строку `b_3`, прежде всего
`b_3*b_3` и `b_3*0`. Маленькая общая лемма:

```text
b_3*b_3 != b_4
```

потому что `b_3*t=b_4`, `t != b_3`, а строка `b_3` является перестановкой.
Особые типы:

```text
r2=b1 -> перенос к строке b1
r2=b2 -> само-тип b2
r2=b4 -> перенос к строке b4
```

Новая точка зрения на текущий тяжелый хвост: условие `6*6=6` в `case 45` -
это не случайный глубокий выбор, а self-тип второго уровня:

```text
b_3*b_3=b_3
```

Поэтому следующий объект - не конкретные `6*7=2/3`, а классификация значений
`q=b_3*b_3` после перехода в строку `b_3`.

Проверка вне `case 45` подтвердила это: в `case 44` при `5*5=5=b_3` и в
`case 42` при `4*4=4=b_3` активной остается соответствующая строка `b_3`.

Контрольное соотношение второго уровня:

```text
если q=b_3*b_3, то q*((b_3*q)*b_3)=b_3
```

При `q!=b_3` оно дает давление через клетку `b_3*q`; при `q=b_3` вырождается.
Это объясняет, почему self-тип `b_3*b_3=b_3` является главным трудным
подтипом.

Невырожденный выход из self-типа:

```text
из b_3*t=b_4 следует t=b_4*((b_3*b_4)*b_3)
```

Поэтому следующий структурный маршрут для self-типа:

```text
s=b_3*b_4
u=s*b_3
b_4*u=t
```

В текущем хвосте `case 45`, `t=4`, `q=6*6=6`, проверка `s=6*5` дала новую
классификацию: `s=b1` или `s=b2` переносит к старшим строкам, `s=t` делает
главным маркером `u=s*b3`, обычные `s` могут оставаться широкими. В ветке
`s=t=4` значения `u=0,4,5` противоречивы, а `u=3` сильно сжимает строку
`b4=5`, но не закрывается прямым поиском.

Самый широкий новый принцип записан в `inverse_edge_chain.md`:

```text
a*z=c  ==>  z=c*((a*c)*a)
```

То есть любое известное ребро порождает обратную цепочку
`a*c -> (a*c)*a -> c*((a*c)*a)`. Для текущего хвоста это дает маршрут:

```text
6*4=5 -> 6*5=s -> s*6=u -> 5*u=4
```

Последний результат перед остановкой: подхвост

```text
7*0=4, 6*6=6, 6*5=4, 4*6=3
```

закрыт полностью через следующий обратный шаг `5*4=v`:

```text
v=2,7 -> противоречие
v=1,3,8 -> status none
```

В ветке `6*5=4` теперь остаются значения `4*6=1,2,7,8`; значения
`4*6=0,4,5` противоречивы, `4*6=3` закрыто.

## Обновление 2026-05-20

Найден более сильный рабочий принцип для текущего хвоста: релейная обратная
цепочка.

Короткая карта этого этапа вынесена в `case45_relay_progress.md`.

```text
a*z=c и c*h=z  ==>  (a*c)*a=h
```

В текущей ветке

```text
7*0=4, 6*6=6, 6*5=4
```

это дает:

```text
4*6=u
5*u=4
v=5*4
v*5=6
p=v*6
p*v=4
```

Главный новый результат:

```text
4*6=u, 5*4=u, u in {1,2,7,8}
```

закрыт полностью. То есть все диагональные хвосты после `v=5*4` закрыты.

Дополнительно в ветке `4*6=1` закрыты все значения

```text
5*4=1,2,3,7,8
```

Остается особый хвост:

```text
4*6=1
5*4=0
```

Он не закрыт текущим коротким реле, потому что сразу возвращается в строку `0`
и старую лестницу `0*5=6`, `0*6=7`, `7*0=4`. Диагностика по строке `6`
оставляет 35 живых вариантов, поэтому следующий шаг должен быть не длинным
перебором, а поиском нового разреза для этого "возврата в ноль".

### Дополнение 2026-05-20: закрыты `4*6=1` и `4*6=2`

Возвратный хвост `4*6=1, 5*4=0` закрыт. Новый маркер:

```text
5*4=0
0*3=4
h=5*0
h*5=3
```

По `h=5*0` закрыты все значения `h=1,2,3,5,7,8`; для трудного `h=8`
дополнительно использован разрез `4*4`, и все значения `4*4=0,2,4,6,7,8`
закрылись. Значит:

```text
4*6=1 -> закрыто полностью
```

Дальше тем же релейным маршрутом закрыта вся ветка:

```text
4*6=2 -> закрыто полностью
```

После этого начата ветка `4*6=7`. В ней закрыты:

```text
5*4=0,1,2,3,7
```

Для `5*4=8` закрыты `p=8*6=1,2,8`. Текущая точка продолжения:

```text
7*0=4
6*6=6
6*5=4
4*6=7
5*4=8
8*5=6
8*6=p
p*8=4
p=3 или p=4
```

Подробный список живых строк `6` для `p=3` и `p=4` сохранен в
`case45_relay_progress.md`.

### Дополнение 2026-05-21: ветка `6*5=4` закрыта, реле локально

Текущий остаток

```text
4*6=7
5*4=8
8*6=p
p=3 или p=4
```

закрыт. После этого разобран последний средний шаг `4*6=8`. Все значения
`v=5*4` закрыты:

```text
v=0 -> zero-return через h=5*0, h*5=3
v=1,2,3 -> p=v*6, p*v=4, затем active-row collapse
v=7 -> все p противоречивы
v=8 -> diagonal через p=8*6, r=p*4, r*p=6
```

Итог:

```text
7*0=4
6*6=6
6*5=4
```

закрыт полностью.

Создана структурная карта `relay_graph_lemma.md`. Ее итог: релейная схема
является сильным локальным инструментом для self-хвоста `case 45`, но пока не
общей леммой для соседних верхних веток. Проверки `7*0=2`, `7*0=3` показали,
что подтип `s=6*5=t` оставляет строки `2` и `3` очень широкими; `7*0=5`
особая ветка с ранним включением строки `5`.

### Дополнение 2026-05-21: новый кандидат self-swap lemma

После проверки переносимости релейной схемы выделен более крупный структурный
кандидат: не просто `s=t`, а соседний обмен в активной строке:

```text
b3*b3=b3
b3*b4=b5
b3*b5=b4
```

В `case 45` это ровно закрытая ветка:

```text
6*6=6
6*5=4
6*4=5
```

Создана записка `self_swap_lemma.md`. Текущий статус: это еще не доказанная
лемма, но лучший найденный общий разрез после реле. Он объясняет, почему
`t=4=b5` сжимается сильнее, чем `t=2,3`: активная строка `6=b3` меняет местами
соседнюю пару `b4,b5`, а не дальний элемент цикла.

Короткая проверка в соседних длинах цикла:

```text
case 44: first row b3, domain 422, first 30 candidates: 22 dead
case 42: first row b3, domain 499, first 30 candidates: 27 dead
case 39: first row b3, domain 398, first 30 candidates: 30 dead
```

Уточнение: расширенная проверка `case 39` на первых 120 кандидатах дала
`63/120` мертвых и живые продолжения. Значит self-swap пока не универсальная
закрывающая лемма. Ее надежный смысл на текущий момент: она выделяет активную
строку `b3` и объясняет локальное сжатие `case 45`, но для общей леммы нужен
дополнительный инвариант, вероятно связанный именно с полным 9-циклом.

Следующий осмысленный шаг: выяснить, что полный 9-цикл добавляет к self-swap
узору, а не продолжать механически добивать отдельные хвосты `case 45`.

Дополнительная проверка дала новый инвариант-кандидат: `tail escape`. В
`case 39/42/44` нулевая строка имеет внешний хвост вне главного цикла, и
живые self-swap образцы используют эти хвостовые элементы. В `case 45`
нулевая строка - полный 9-цикл, хвоста нет. Поэтому более точная рабочая
формула:

```text
self-swap + no tail escape
```

Следующий этап: понять, можно ли доказать, что соседний self-swap в полном
нулевом цикле невозможен.

Контрольная поправка: в самом `case 45` self-swap не убивает первую строку
сразу (`45/80` мертвых в первом срезе, живые образцы остаются). Поэтому
рабочая гипотеза не "no tail сразу противоречит", а "no tail удерживает живые
варианты внутри одного релейного ядра, где они затем закрываются".

Уточнение уровня леммы: найден каскадный смысл значения `4*6=3=b6`.
Тогда из `5*(4*6)=4` получается `5*3=4`, то есть релейное ребро сдвигается
на шаг ниже по циклу. Новая крупная формула:

```text
self-swap запускает каскад соседних ребер;
в полном цикле у каскада нет tail-выхода;
поэтому он должен прийти к запрещенному плохому краю.
```

Новый прогресс: каскадный подузел `u=b6, v=b6` разобран как короткое дерево:

```text
4*6=3
5*3=4
5*4=3
```

Структурно выводятся:

```text
5*0=6
5*5=0
```

Дальше:

```text
5*6=8 -> contradiction
5*6=2 -> остается домен строки 6 размера 10
```

Последний разрез `6*8` закрывает остаток:

```text
6*8=0,2,7,8 -> contradiction
6*8=1 -> 4 variants, all dead
```

Это превращает один бывший вычислительный хвост в понятный структурный
подузел каскадной леммы.

Дополнение: весь узел `u=b6` теперь имеет компактную ролевую карту:

```text
v=5*4 in {1,2,3,7,8}
v=2=b7 -> contradiction
v=7=b2 -> contradiction
v=1=b8 -> row 5 domain 10, all dead
v=8=b1 -> last row-6 residue, all dead
v=3=b6 -> shifted cascade, closed via 5*6 and 6*8
```

То есть `4*6=3` уже можно считать не просто закрытым случаем, а оформленным
каскадным подузлом.

### Остановка 2026-05-21: сохраненная точка продолжения

Последняя незавершенная линия перед остановкой: сравнение оставшихся ролей
среднего шага `u=4*6` после оформленного узла `u=b6`.

Сохраненный результат:

```text
u=1=b8: row 5 domain 6487; first active row 6 domain 78; 31/50 dead
u=2=b7: row 6 domain 108; 32/50 dead; живые row 7, row 2, row 8
u=7=b2: row 6 domain 99; 33/50 dead; живые row 1, row 7
u=8=b1: row 6 domain 86; 33/50 dead; живые row 8, row 7, row 1
```

Вывод: `u=b6` уже стал понятным каскадным узлом. Остальные `u` пока являются
не каскадом вниз, а переносом в старшие/дальние строки. Следующий запуск лучше
начать с леммы о таком переносе, а не с повторного закрытия `4*6=1,2,7,8`.

### Дополнение 2026-05-21: senior/far transfer lemma candidate

Создана записка `senior_far_transfer_lemma.md`.

Новый общий принцип:

```text
для u in {b1,b2,b7,b8}
дальний u не является отдельным хвостом,
а передает давление в релейный узел:

v=b4*b5
v*b4=b3
p=v*b3
p*v=b5
```

В числах:

```text
v=5*4
v*5=6
p=v*6
p*v=4
```

Теперь четыре оставшихся `u` надо доказывать не отдельно. Следующая лемма
должна закрыть выход:

```text
v in {b1,b2,b7,b8} \ {u}
```

то есть senior/far transfer после первого переноса.

Появился следующий слой: параметр

```text
p=v*b3
p*v=b5
```

Representative-пара `u=b8, v=b1` показала:

```text
p=v=b1 -> contradiction
p=u=b8 -> active-row collapse
p in {b5,b6,b7} -> маленький остаток строки b3, затем row b8
```

Следующий осмысленный шаг: проверить эту p-классификацию на других
representative-парах senior/far transfer.

Найден ручной шаг, объясняющий активность строки `b3`: из `b4*u=b5` и
нулевой лестницы следует

```text
b3*0=u
```

В числах:

```text
5*u=4 -> 6*0=u
```

То есть far/senior `u` становится значением плохой колонки строки `b3`.
Это объясняет, почему диагностика постоянно возвращается к `row 6`, без
ссылки на перебор.

Еще один ручной маркер: если

```text
q=u*b3
```

то E677 при `x=0` дает

```text
b3*(0*q)=0
```

В числах: после `6*0=u`, значение `u*6=q` определяет, где в строке `6`
стоит ноль. Это может быть ключом к доказательству второго active-row collapse.

Проверена вторая representative-пара `u=b7, v=b2`. Она подтвердила общий вид:
после split по `p=v*b3` почти все умирает на строке `b3`; единственный остаток
ушел в `row 2` с доменом 23 и полностью умер. Это усиливает гипотезу:
senior/far transfer закрывается как active-row collapse второго уровня.

Проверена третья representative-пара `u=b1, v=b8`. В подветке `p=b7` первый
слой `row 6` имел домен 80 и оставил 9 живых строк; все 9 умерли вторым
слоем на `row 1` или `row 2` с доменами 9-23. Это подтверждает форму:

```text
senior/far transfer -> row b3 collapse -> small far-row residue -> contradiction
```

Уточнен механизм collapse: для той же ветки параметр `q=u*b3` имеет только
значения `{0,b8,b7}`. Он ставит ноль в строке `b3`:

```text
q=0  -> b3*b8=0
q=b8 -> b3*b7=0
q=b7 -> b3*b6=0
```

В числах:

```text
q=8*6 in {0,1,2}
q=0 -> 6*1=0, all dead
q=1 -> 6*2=0, small residues
q=2 -> 6*3=0, small residues
```

Это объясняет, почему второй collapse управляется положением нуля в строке
`b3`.

Вторая representative-пара подтвердила `q`-механизм:

```text
u=b7, v=b2, p=b8
q=u*b3 in {0,b8,b7,b2}
```

Split:

```text
q=0 -> contradiction
q=b8 -> row 2 domain 13, all dead
q=b7 -> row 6 domain 18, one small row 2 residue
q=b2 -> row 6 domain 16, all dead
```

Так что новый кандидат стал точнее: senior/far transfer закрывается через
`q=u*b3`, который задает положение нуля в строке `b3`.

Проверена q-карта по всем senior/far парам. Диагностический факт:

```text
q=u*b3 всегда лежит в {0,b8,b7,b2}
```

То есть запрещаются:

```text
q in {b1,b3,b4,b5,b6}
```

Если это удастся доказать вручную, senior/far transfer почти станет леммой:
эти четыре значения `q` ставят ноль в строке `b3` только в колонках
`{b8,b7,b6,b1}`, после чего остаются маленькие far-row residues.

Этот q-факт теперь почти доказан вручную. Запреты:

```text
q=b1,b4,b5,b6
```

следуют сразу из `q -> b3*(0*q)=0` и уже известных клеток строки `b3`.
Значение `q=b3` запрещается collision-следствием E677: если `u*b3=b3` и
`b3*b3=b3`, то получается `b3*u=b3`, что нарушает перестановочность строки
`b3`, так как `u != b3`.

Итоговая подлемма:

```text
q=u*b3 in {0,b8,b7,b2}
```

После выбора `q` строка `b3` имеет пять принудительных клеток:

```text
b3*0=u
b3*b3=b3
b3*b4=b5
b3*b5=b4
b3*(0*q)=0
```

Остается максимум:

```text
4! = 24
```

варианта строки `b3`. Это главный прогресс: senior/far transfer теперь сведен
к маленькой 24-вариантной строковой лемме.

Поправка после проверки пары `u=b8, v=b7`: одного `q`-маркера недостаточно
для полного закрытия. Нужен совместный слой `(p,q)`, где `p=v*b3`.

Для этой пары `(p,q)` уменьшает строку `b3` обычно до 10-16 вариантов; часть
комбинаций сразу противоречива или полностью мертва, а часть оставляет
маленькие far-row residues с доменами до 32.

Текущая точная форма:

```text
senior/far transfer
-> q-подлемма
-> (p,q)-collapse строки b3
-> small far-row residue
```

Проверен один трудный `(p,q)`-узел:

```text
u=b8, v=b7, p=b6, q=b7
```

Он закрылся полностью:

```text
row b3 domain 16
11 residues remain
каждый residue закрывается одной маленькой строкой
домены: 9..31
```

Это подтверждает форму последнего слоя: после `(p,q)` остается конечный
far-row residue, а не большой поиск.

## Остановка 2026-05-21: актуальная точка продолжения

Работа остановлена по просьбе пользователя. Фоновые субагенты были закрыты без
использования их незавершенных результатов.

Главная новая точка: senior/far transfer уже не выглядит большим перебором.
Representative-пара

```text
u=b8, v=b7
```

полностью закрыта короткой диагностикой после совместного слоя `(p,q)`:

```text
p in {b8,b7,b6,b5,b1}
q in {b8,b7}
```

В числах:

```text
u=1, v=2
p in {1,2,3,4,8}
q in {1,2}
```

Все 10 комбинаций `(p,q)` закрылись (`status: none`).

Трудный узел

```text
u=b8, v=b7, p=b6, q=b7
```

теперь понятнее: строка `b3` имеет 16 вариантов, и все 16 закрываются коротко.
Для большого остатка

```text
row b3 = 1 8 3 0 5 4 6 7 2
```

найдена контрольная клетка:

```text
b8*b5 = 1*4
```

Все ее возможные значения невозможны:

```text
1*4=0, 1*4=4, 1*4=8 -> contradiction
```

Текущая рабочая форма леммы:

```text
senior/far transfer
-> q-подлемма
-> совместный (p,q)-слой
-> малый домен строки b3
-> одно-клеточный far-row killer
```

Не начинать заново с `case 45` и не повторять уже закрытую пару `u=b8,v=b7`.
Следующий осмысленный шаг: доказать вручную, почему в контрольном остатке
клетка `1*4` не может принимать значения `0,4,8`, а затем обобщить это на все
16 вариантов строки `b3`.

## Обновление 2026-05-22: far-row killer выделен в отдельную микролемму

Создан файл `far_row_killer_lemma.md`.

В контрольном остатке

```text
u=b8, v=b7, p=b6, q=b7
row b3 = 1 8 3 0 5 4 6 7 2
```

клетка

```text
1*4
```

имеет только значения `0,4,8`.

Значения `1*4=0` и `1*4=8` уже получили ручные цепочки противоречий. Значение
`1*4=4` сведено к микролемме:

```text
4*3 in {0,2,3,4,5,6,8}
```

Подслучаи `4*3=0,5,6` уже имеют короткие ручные цепочки. Остаются для ручного
извлечения:

```text
4*3=2
4*3=3
4*3=4
4*3=8
```

Следующий запуск должен начинаться именно с этих четырех значений, а не с
повторной диагностики всей senior/far пары.

Дополнение: контрольный узел `u=b8,v=b7,p=b6,q=b7` теперь оформлен как
16-вариантный сертификат в `far_row_killer_lemma.md`. В рабочем смысле это
локальная лемма:

```text
в этом узле ни один вариант строки b3 не продолжается;
каждый вариант закрывается сразу или одной контрольной far-row клеткой.
```

Следующий более крупный шаг - понять, почему контрольные клетки лежат в
маленьком наборе `2*0, 1*4, 3*1, 3*0, 3*4, 1*2`.

Дополнение по всей representative-паре `u=b8,v=b7`: слой `(p,q)` имеет 10
комбинаций. Из них 3 противоречивы сразу, 3 полностью умирают на строке `b3`,
и 4 оставляют только маленький второй слой. То есть вся пара уже имеет
устойчивую форму:

```text
(p,q) -> b3-collapse -> optional one far-row killer
```

Следующий переносимый вопрос: доказать, что такая форма зависит от ролей
`u,v,p,q`, а не только от конкретной пары `u=b8,v=b7`.

Проверена соседняя пара `u=b7,v=b8` (`u=2,v=1`). Форма повторилась:

```text
(p,q) -> b3-collapse -> optional one far-row killer
```

Разница только количественная: домен строки `b3` местами доходит до `22`, но
первый активный слой остается строкой `b3`, а остатки уходят в одну far-строку.
Это усиливает кандидат-лемму senior/far transfer.

Проверена третья ориентация `u=b2,v=b8` (`u=7,v=1`). Форма снова повторилась:

```text
(p,q) -> b3-collapse -> optional one far-row killer
```

Теперь рабочая кандидат-лемма формулируется ролево: senior/far transfer в
self-swap ветке полного 9-цикла не порождает глубокого дерева; после
q-подлеммы и `(p,q)` слоя он сжимается строкой `b3`, а остатки уходят максимум
в одну far-строку.

Проверены еще две ориентации: `u=b1,v=b8` и `u=b8,v=b1`. Они тоже сохраняют
форму:

```text
(p,q) -> row b3 -> small far-row residues
```

На данный момент проверено пять живых ориентаций и одна сразу противоречивая.
Во всех живых ориентациях первый активный слой - строка `b3`. Это главный
новый структурный факт.

Две ориентации теперь закрыты полностью через `(p,q)`-слой:

```text
u=b7, v=b2  (числа u=2, v=7)
u=b1, v=b7  (числа u=8, v=2)
```

Во всех их `(p,q)` комбинациях получен `status: none`. Это подтверждает, что
найденный разрез не только диагностический, а реально закрывающий.

## Обновление 2026-05-22: senior/far transfer закрыт полностью

Для текущей self-swap ветки полностью закрыт тип:

```text
senior/far transfer
u in {b1,b2,b7,b8}
v in {b1,b2,b7,b8}
v != u
```

Одна ориентация `u=b1,v=b2` противоречива сразу. Остальные 11 ориентаций
закрыты через разрез:

```text
p=v*b3
q=u*b3
```

Во всех допустимых `(p,q)` узлах получен `status: none`.

Статус: это завершенная локальная лемма для senior/far transfer. Ее
доказательная форма смешанная: q-подлемма доказана вручную, финальный слой
сохранен как конечный `(p,q)` сертификат.

Поправка: это не следующий открытый тип.

```text
zero-return: v=b4*b5=0
```

В числах:

```text
5*4=0
```

уже закрыт раньше в `case45_relay_progress.md` через маркер:

```text
h=5*0
h*5=3
```

Senior/far больше не является открытым хвостом, а zero-return в этой же ветке
тоже закрыт. Следующий шаг должен быть уровнем выше: проверить, какие части
ветки `7*0=4, 6*6=6` еще не сведены к таким ролевым леммам.

## Остановка 2026-05-22: текущая точка продолжения

Актуальный фронт:

```text
case 45
7*0=4
6*6=6
6*5=s
s in {1,2,3,7,8}
```

Важно: ветка

```text
6*5=4
```

уже закрыта полностью. Не начинать ее заново.

Новый рабочий разрез:

```text
u=s*6
```

Он важен потому, что из E677 получается цепочка:

```text
6*4=5
6*5=s
s*6=u
=> 5*u=4
=> 6*0=u

q=u*6
=> 6*(0*q)=0
```

Рабочее название:

```text
u-transfer / no-tail trap
```

Проверено перед остановкой:

```text
s=1,u=2 -> закрыто по q=0,1,2,7
s=1,u=3 -> закрыто по q=0,1,2,7
```

Осталось продолжить:

```text
s=1,u=4
s=1,u=8
затем s=2,3,7,8 тем же протоколом
```

Главный новый файл:

```text
u_transfer_no_tail_trap_lemma.md
```
