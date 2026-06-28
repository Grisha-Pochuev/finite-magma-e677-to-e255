# Top Branch Row-6 Transfer Plan

Дата: 2026-05-24.

## Зачем создан файл

После закрытия ветки:

```text
case45
7*0=4
```

следующий фронт находится выше:

```text
7*0=2
7*0=3
7*0=5
```

Цель - не начинать их перебором, а проверить переносимость найденной
row-6 / low-to-low relay структуры.

## Общий верхний факт

В `case45` строка `0` - полный 9-цикл, и:

```text
b1=8
b2=7
b3=6
b4=5
b5=4
b6=3
b7=2
b8=1
```

Для оставшихся верхних веток:

```text
7*0=t
```

лестница дает:

```text
6*t=5
```

То есть активная строка снова должна быть:

```text
row 6 = row b3
```

## Ветки

### `7*0=2`

```text
t=2=b7
6*2=5=b4
```

Значит:

```text
6*6 != 5
```

Первый разрез снова:

```text
6*6
```

### `7*0=3`

```text
t=3=b6
6*3=5=b4
```

Первый разрез:

```text
6*6
```

### `7*0=5`

```text
t=5=b4
6*5=5=b4
```

Это особая ветка: строка `6` уже фиксирует `5` в собственной колонке `5`.
По старой диагностике здесь раньше включается строка `5`.

Поэтому `7*0=5` не смешивать сразу с `7*0=2,3`.

## Перенос из закрытой ветки `7*0=4`

Закрытая ветка `7*0=4` использовала:

```text
6*4=5
s=6*5
u=s*6=6*0
q=u*6
6*(0*q)=0
```

Для общей ветки `7*0=t` естественный аналог:

```text
6*t=5
s=6*5
u=s*6
5*u=t
```

Вопрос: когда из этого снова получается:

```text
6*0=u
```

Для `t=4` это работало из-за полного 9-цикла и связи:

```text
0*4=5
```

В общем случае:

```text
0*t=t+1
```

поэтому прямое повторение требует осторожности. Нельзя автоматически переносить
формулу `6*0=u` без проверки.

## Главный структурный вопрос

Для `7*0=t`, `t in {2,3,5}`, нужно найти правильный аналог маркера:

```text
u=s*6
```

и понять, в какую клетку строки `6` он переносится:

```text
6*k=u
```

В ветке `t=4` это была клетка:

```text
k=0
6*0=u
```

В других ветках `k` может зависеть от `t`.

## Поправка после ручного анализа

В закрытой ветке `t=4` произошло специальное совпадение двух маркеров:

```text
s=6*5
u=s*6
w=6*0
```

и оказалось:

```text
u=w
```

Причина: при `t=4` есть совпадение:

```text
0*4=5
```

а также из обратной цепочки:

```text
5*u=4
```

Релейная форма тогда дает:

```text
6*0=u
```

Для `t=2` и `t=3` такого совпадения с row `0` нет:

```text
0*2=3
0*3=4
```

поэтому нельзя ожидать, что:

```text
s*6 = 6*0
```

сохранится автоматически.

Более правильный следующий объект:

```text
u=s*6
w=6*0
```

то есть не один маркер, а пара маркеров `(u,w)`.

Роль закрытой ветки `t=4`:

```text
это диагональный подслучай u=w.
```

Для `t=2,3` нужно сначала понять, какие пары `(u,w)` допустимы и какие из них
являются аналогами endpoint/interior split.

## Следующий безопасный шаг

Не запускать длинный поиск.

Сначала сделать короткую диагностику для:

```text
7*0=2
7*0=3
```

только чтобы увидеть:

```text
после 6*t=5 и первого split 6*6
какая клетка строки 6 играет роль старого 6*0
```

Проверять не закрытие ветки, а перенос маркера.

Уточнение: проверять не только возможный `6*k=u`, а прежде всего пару:

```text
u=s*6
w=6*0
```

и смотреть, остается ли старый случай `u=w` особым диагональным подтипом.

`7*0=5` держать отдельно как особый случай, потому что там:

```text
6*5=5
```

## Update 2026-05-24: marker bridge transfer

The previous object `(u,w)=(s*6,6*0)` was too narrow.  The closed branch
`t=4` is better understood as a bridge case.

General bridge form:

```text
6*t=5
6*5=s
a*t=5
a*5=6
```

Then inverse-edge transfer gives:

```text
5*(s*6)=t
5*(6*a)=t
```

Since row `5` is injective:

```text
6*a=s*6
```

For `t=4`, the bridge row was `a=0`:

```text
0*4=5
0*5=6
```

So the old formula `6*0=s*6` is only the special bridge `a=0`.

For `t=2,3`, row `0` is not the same bridge.  The next structural task is:

```text
classify possible bridge rows a with a*t=5 and a*5=6
```

Short diagnostics suggested `a=8` as a candidate bridge in the self layer
`6*6=6, 6*5=t` for both `t=2` and `t=3`.  Details are recorded in:

```text
marker_bridge_transfer_lemma.md
```

Further diagnostics in that self layer showed the role pattern:

```text
t=2: possible a in {1,3,4,7,8}; impossible {0,2,5,6}
t=3: possible a in {1,2,4,7,8}; impossible {0,3,5,6}
```

So locally possible bridges are exactly outside:

```text
{0,t,5,6}
```

But two different bridges cannot coexist, because each bridge forces the same
row-6 value:

```text
6*a=s*6
```

The next question is therefore:

```text
is bridge existence forced, or is there a meaningful no-bridge branch?
```

Answer after pair-forbid diagnostics:

```text
no-bridge branch is meaningful and alive
```

Forbidding all possible bridges gives:

```text
t=2: status ok, row6 domain 486
t=3: status ok, row6 domain 468
```

So bridge-transfer is conditional, not the full top-branch lemma.

The fallback marker in the no-bridge branch is:

```text
6*8 = 6*b1
```

Thus the next structural split is:

```text
bridge branch:
  6*a=s*6

no-bridge branch:
  split by 6*b1
```
