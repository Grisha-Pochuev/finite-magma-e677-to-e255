#!/usr/bin/env python3
"""Synchronize public status files after the certified closure of form 2."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one old block, found {count}")
    return text.replace(old, new, 1)


def replace_section(text: str, start: str, end: str, body: str, label: str) -> str:
    start_count = text.count(start)
    end_count = text.count(end)
    if start_count != 1 or end_count != 1:
        raise RuntimeError(
            f"{label}: marker counts are start={start_count}, end={end_count}"
        )
    left, tail = text.split(start, 1)
    _, right = tail.split(end, 1)
    return left + start + body + end + right


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    old = """- exactly three Bad elements reduce to 24 normalized forms, 15 of which are
  already UNSAT in the first exact scan;
- in normalized three-Bad form 2, eight of nine canonical root leaves are
  independently UNSAT, leaving one explicitly stated companion case.

The last statement and its exact restart point are in the
[order-9 three-Bad reduction](lemmas/e677_order9_three_bad_root_and_case2_reduction.md).
These are finite reductions only: the HIT branch and the remaining no-HIT
forms still prevent a complete order-9 certificate.
"""
    new = """- exactly three Bad elements reduce to 24 normalized forms; 15 were UNSAT in
  the first exact scan, and normalized form 2 has now been independently
  excluded, so 16/24 forms are closed;
- form 2 is covered by fourteen exhaustive leaves: the earlier eight root
  outcomes and the final six companion leaves are UNSAT in both CaDiCaL195
  and Glucose42.

The complete form-2 certificate and the remaining indices
`3,11,15,16,18,21,23,24` are in the
[order-9 three-Bad exclusion](lemmas/e677_order9_three_bad_root_and_case2_reduction.md).
These are finite reductions only: the HIT branch and the remaining no-HIT
forms still prevent a complete order-9 certificate.
"""
    text = replace_once(text, old, new, "README order-9 status")

    old = """The third command is the short newest certificate: it checks the same eight
three-Bad leaves independently with CaDiCaL195 and Glucose42.
"""
    new = """The third command checks all fourteen exhaustive leaves of normalized
three-Bad form 2: the earlier eight root outcomes and the final six companion
leaves, independently in CaDiCaL195 and Glucose42.
"""
    text = replace_once(text, old, new, "README verifier description")
    write(path, text)


def update_frontier() -> None:
    path = "docs/ACTIVE_FRONTIER_MIN.md"
    text = read(path)
    start = "That three-Bad pattern is now normalized exactly."
    end = "The size-free active structural question remains the simultaneous G-CROSS\nnetwork."
    body = """That three-Bad pattern is now normalized exactly.  Select one strict extra
Omega-root before naming the labels.  The fixed-point-free map `D` on three
Bad points is either a 3-cycle or a 2-cycle with one tail.  After setting
`0*0=1`, the square colour, the value `D(0)`, and the chain
`f(t)=t*0` give exactly `24` top forms:

```text
family A (square Bad, D(0)=1): 3 D-types * 3 f-chains = 9;
family B (square Bad, D(0)=2): 3 D-types * 2 f-chains = 6;
family C (square Good,D(0)=2): 3 D-types * 3 f-chains = 9.
```

The first exact CaDiCaL scan closed `15/24`; the nine bounded UNKNOWN forms
were indices `2,3,11,15,16,18,21,23,24`.  Fixing only the root position gave
`15/15 UNKNOWN` before an intentional stop and is retired.  Splitting the
canonical root by Good/row/third-Bad product closed `23/66` small cubes;
naming the Good product up to residual symmetry closed `6/37` further cubes.
These counts locate the boundary and do not close all three-Bad models.

Top form `2` is now completely certified.  It has

```text
B={0,1,2}; D: 0->1->2->0;
0*0=1; 1*0=2; 2*0=1.
```

The first reduction excludes eight canonical root/companion outcomes in both
CaDiCaL195 and Glucose42 and forces the selected extra root to be

```text
(0,2), with 0*2=3 Good.
```

Put `a=0*3`, `k=a*0`; E677 forces `3*k=2`.  Row injectivity and residual
relabelling leave exactly

```text
(a,k)=(0,1),(2,1),(4,1),(4,3),(4,4),(4,5).
```

All six leaves are independently UNSAT in both engines.  The sole nontrivial
leaf `(a,k)=(0,1)` was closed in `3.501s / 63138` conflicts by CaDiCaL195 and
`3.391s / 62888` conflicts by Glucose42.  There was no SAT model, UNKNOWN, or
technical failure.  Hence form `2` is UNSAT and the total closed count is now

```text
16/24.
```

The remaining three-Bad forms are exactly

```text
3,11,15,16,18,21,23,24.
```

Exact proof, base checker, pinned continuation wrapper, record, and verifier:

```text
lemmas/e677_order9_three_bad_root_and_case2_reduction.md;
tools/e677_order9_no_hit_bad_count_sat.py;
Experiments/2026-08-29-order9-case2-paused/run_case2_paused.py;
logs/e677_order9_three_bad_case2_complete_2026-08-29.txt;
verify_order9_three_bad_case2.ps1.
```

The next finite question is form `3`, which keeps the same three-cycle
D-pattern and replaces the first-column chain by `1*0=3, 3*0=1`.  Reuse the
canonical-root split and companion word; do not rerun the unsplit cube.

"""
    text = replace_section(text, start, end, body, "ACTIVE_FRONTIER order-9 three-Bad")

    old = """order-9 |Bad|=3 top forms initially closed:          15/24 (62.5%).
order-9 |Bad|=3 form-2 root outcomes excluded:         8/9 (88.9%).
order-9 remaining no-HIT Bad cardinalities:             0/7 (0%).
"""
    new = """order-9 |Bad|=3 initial exact scan:                 15/24 (62.5%).
order-9 |Bad|=3 subsequent form-2 closure:              1/9 (11.1%).
order-9 |Bad|=3 total top forms closed:                16/24 (66.7%).
order-9 |Bad|=3 form-2 root outcomes excluded:           9/9 (100%).
order-9 remaining no-HIT Bad cardinalities:             0/7 (0%).
"""
    text = replace_once(text, old, new, "ACTIVE_FRONTIER progress table")
    write(path, text)


def update_web_memory() -> None:
    path = "Experiments/START_HERE_WEB.md"
    text = read(path)

    current = """

Активная конечная ветвь — порядок `9`, no-HIT, ровно три Bad-точки.
Терминальная ZERO-ветвь и случай `|Bad|=2` уже закрыты.  Три-Bad классификация
содержит 24 нормальные формы.  Первый точный прогон закрыл 15; новый
сертификат полностью исключил форму 2, поэтому закрыто `16/24`.

Для формы 2 проверены все четырнадцать исчерпывающих листьев: прежние восемь
исходов корня и последние шесть companion-листьев.  CaDiCaL195 и Glucose42
независимо дали UNSAT во всех случаях.  Полной таблицы-контрпримера нет.

Остаются формы

```text
3, 11, 15, 16, 18, 21, 23, 24,
```

а также большие мощности Bad и ветвь HIT.  Следующая наиболее близкая цель —
форма 3 с тем же D-трёхциклом и цепочкой `1*0=3, 3*0=1`.

"""
    text = replace_section(
        text,
        "## Текущее математическое состояние",
        "## Последний завершенный прогон",
        current,
        "START_HERE current mathematics",
    )

    latest = """

Папка:

```text
Experiments/2026-08-29-order9-case2-paused/
```

GitHub Actions:

```text
smoke: 33267460851
full:  33267614227
```

Итог полного прогона:

- точный базовый SAT-каркас закреплён Git blob
  `efe356acd0047eef8ae5645b2cb04ac2a493632d`;
- шесть из шести paused-листьев UNSAT в CaDiCaL195;
- шесть из шести paused-листьев UNSAT в Glucose42;
- UNKNOWN: 0;
- SAT-моделей и полных контрпримеров: 0;
- технических ошибок и отсутствующих сводок: 0;
- форма 2 полностью закрыта;
- общий счёт трёх-Bad форм: `16/24` закрыто.

Компактные результаты находятся в `RESULTS.md`, `run-summary.json`,
`run-summary.csv` и `RUN_REPORT.md` той же папки.

"""
    text = replace_section(
        text,
        "## Последний завершенный прогон",
        "## Ретроспектива завершенной цепочки",
        latest,
        "START_HERE latest run",
    )

    retrospective = """

Что сработало хорошо:

- продолжение началось ровно с остановленной формулы (19), без повтора старых
  15/24 и 8/9 прогонов;
- шесть листьев были исчерпывающими, а не эвристическими;
- любой SAT-ответ по-прежнему обязан был декодироваться в полную таблицу 9x9
  и пройти все 81 подстановку E677;
- короткий тест сначала сузил остаток до одного листа;
- полный тест затем независимо закрыл этот лист двумя движками;
- результат сохранён в одной датированной папке вместе с точным workflow,
  журналами, сводками и справкой Codex.

Общий технический урок не изменился: сначала короткий сквозной тест, затем
отдельный полный запуск, после чего в Git сохраняется компактный проверенный
результат.

"""
    text = replace_section(
        text,
        "## Ретроспектива завершенной цепочки",
        "## Следующий шаг",
        retrospective,
        "START_HERE retrospective",
    )

    next_step = """

Не повторять форму 2: она закрыта.

Следующий конечный шаг — форма 3 среди трёх-Bad моделей.  Сначала применить к
ней исчерпывающий канонический split корня (Good / row / third-Bad), затем к
оставшимся Good-исходам — companion word и нормализацию новых Good-меток.
Начинать с короткой проверки обоих SAT-движков; длинный прогон открывать только
для общего остатка, если он останется.

"""
    text = replace_section(
        text,
        "## Следующий шаг",
        "## Что обновлять после каждого существенного прогона",
        next_step,
        "START_HERE next step",
    )
    text = text.replace(
        "Дата последнего обновления: 13 июля 2026",
        "Дата последнего обновления: 29 августа 2026",
        1,
    )
    write(path, text)


def update_experiments_index() -> None:
    path = "Experiments/README.md"
    text = read(path)
    body = """

- `2026-08-29-order9-case2-paused/` — exact order-9 three-Bad form-2
  continuation.  Six of six paused leaves are UNSAT in both CaDiCaL195 and
  Glucose42; form 2 is fully excluded and the top-form count is `16/24`.
  Runs: smoke `33267460851`, full `33267614227`.

Previous completed runs:

- `2026-07-13-fixed-eta-zba-bridge/` — 20 jobs on five fixed-eta targets;
  all ended by timeout without a proof or model.  Final commit:
  `9a02d03c0603cd40b9dc0ba54593bad64d58b0c5`.
- `2026-07-11-fixed-eta/` — first large fixed-eta run and runner/memory
  diagnostics.

There is no active full run.

"""
    text = replace_section(
        text,
        "## Последний завершенный прогон",
        "## Главное правило структуры",
        body,
        "Experiments index latest run",
    )
    write(path, text)


def main() -> None:
    update_readme()
    update_frontier()
    update_web_memory()
    update_experiments_index()
    print("updated README.md")
    print("updated docs/ACTIVE_FRONTIER_MIN.md")
    print("updated Experiments/START_HERE_WEB.md")
    print("updated Experiments/README.md")


if __name__ == "__main__":
    main()
