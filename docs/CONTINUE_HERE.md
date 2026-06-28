# Continue Here

## Current branch-closure update 2026-06-17

Read first:

```text
CURRENT_FRONTIER.md
```

Newest proved boundary reduction:

```text
pure_incoming_merge_target_swap_fan_lemma.md
```

Pure incoming first-merge vertices of degree at least three now relay, after
target swap `b -> z`, to a triple outgoing fan in `H_z`. The remaining local
boundary is the binary pure incoming sink:

```text
exactly two incoming branches,
no outgoing continuation,
no loop,
no third incoming incidence.
```

Next structural reduction:

```text
binary_sink_core_escape_lemma.md
```

The binary sink alone gives only one cycle. In the forced bicyclic core, the
second cycle must attach to the two-branch corridor before the sink. Continue
with the earliest side attachment to that corridor.

Newest classification:

```text
earliest_side_attachment_mixed_junction_lemma.md
```

An internal side attachment is automatically a mixed `2+1` junction, because
the active branch path already contributes one incoming and one outgoing edge
at that vertex. The binary sink is therefore not a separate obstruction type.

Stage summary:

```text
pure_incoming_boundary_stage_2026-06-17.md
```

Основная точка входа:

```text
CURRENT_FRONTIER.md
```

Прочитать ее целиком и взять только один указанный там активный фронт.

Текущая задача:

```text
доказать No-Free-Tail через полные сертификаты ребер
в смешанном ядровом узле 2+1 или тройном веере.
```

Последний общий доказанный результат:

```text
right_fixer_to_balanced_witness_lemma.md
```

Он устраняет необходимость отдельно искать `z`: достаточно доказать
существование `Y` с `Y*b=b`.

Подробная история старой точки продолжения сохранена:

```text
archive/CONTINUE_HERE_full_through_2026-06-09.md
```

Полный старый журнал:

```text
archive/research_log_full_through_2026-06-09.md
```

Не читать архив при обычном старте. Обращаться к нему только для проверки
конкретного старого вывода.
