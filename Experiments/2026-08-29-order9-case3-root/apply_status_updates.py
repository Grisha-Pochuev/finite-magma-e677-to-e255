#!/usr/bin/env python3
"""Synchronize public status files after the exact exclusion of form 3."""

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
    if text.count(start) != 1 or text.count(end) != 1:
        raise RuntimeError(f"{label}: section markers are not unique")
    left, tail = text.split(start, 1)
    _, right = tail.split(end, 1)
    return left + start + body + end + right


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    old = """- exactly three Bad elements reduce to 24 normalized forms; 15 were UNSAT in
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
    new = """- exactly three Bad elements reduce to 24 normalized forms; 15 were UNSAT in
  the first exact scan, and normalized forms 2 and 3 have now been
  independently excluded, so 17/24 forms are closed;
- form 2 is covered by fourteen exhaustive leaves, while form 3 is covered by
  six exhaustive canonical root outcomes; both certificates agree in
  CaDiCaL195 and Glucose42.

The complete certificates are the
[form-2 exclusion](lemmas/e677_order9_three_bad_root_and_case2_reduction.md)
and the [form-3 exclusion](lemmas/e677_order9_three_bad_case3_exclusion.md).
The remaining indices are `11,15,16,18,21,23,24`.  These are finite
reductions only: the HIT branch and the remaining no-HIT forms still prevent
a complete order-9 certificate.
"""
    text = replace_once(text, old, new, "README finite status")

    old = """.\\verify_order9_terminal_zero.ps1
.\\verify_order9_two_bad_no_hit.ps1
.\\verify_order9_three_bad_case2.ps1
```

The third command checks all fourteen exhaustive leaves of normalized
three-Bad form 2: the earlier eight root outcomes and the final six companion
leaves, independently in CaDiCaL195 and Glucose42.
"""
    new = """.\\verify_order9_terminal_zero.ps1
.\\verify_order9_two_bad_no_hit.ps1
.\\verify_order9_three_bad_case2.ps1
.\\verify_order9_three_bad_case3.ps1
```

The third command checks all fourteen exhaustive leaves of normalized form 2.
The fourth checks the six exhaustive canonical root outcomes of normalized
form 3 and the four finer Good-product representatives, independently in
CaDiCaL195 and Glucose42.
"""
    text = replace_once(text, old, new, "README reproducibility")
    write(path, text)


def update_frontier() -> None:
    path = "docs/ACTIVE_FRONTIER_MIN.md"
    text = read(path)
    old = """The remaining three-Bad forms are exactly

```text
3,11,15,16,18,21,23,24.
```
"""
    new = """After the form-2 exclusion, the remaining three-Bad forms were

```text
3,11,15,16,18,21,23,24.
```
"""
    text = replace_once(text, old, new, "frontier historical remainder")

    old = """The next finite question is form `3`, which keeps the same three-cycle
D-pattern and replaces the first-column chain by `1*0=3, 3*0=1`.  Reuse the
canonical-root split and companion word; do not rerun the unsplit cube.

"""
    new = """Top form `3` is now also completely certified.  It has

```text
B={0,1,2}; D: 0->1->2->0;
0*0=1; 1*0=3; 3*0=1.
```

Its canonical strict extra roots are `(0,1)` and `(0,2)`.  For each root the
product is exhaustively Good, row value `0`, or the third Bad point, giving
six aggregate leaves.  Both engines independently prove

```text
CaDiCaL195: 6/6 UNSAT;
Glucose42:  6/6 UNSAT.
```

The difficult Good leaves were independently refined by residual Good
relabelling to four exact representatives, all `4/4 UNSAT` in both engines.
There was no SAT model, UNKNOWN, or technical failure.  Hence form `3` is
UNSAT and the total closed count is now

```text
17/24.
```

The remaining three-Bad forms are exactly

```text
11,15,16,18,21,23,24.
```

Exact proof, checker, record, and verifier:

```text
lemmas/e677_order9_three_bad_case3_exclusion.md;
tools/e677_order9_no_hit_bad_count_sat.py;
Experiments/2026-08-29-order9-case3-root/RESULTS.md;
verify_order9_three_bad_case3.ps1.
```

The next finite step should compare these seven forms by their exact
canonical-root orbit count.  Form `16` has only two Good-product
representatives after the six-outcome split and is the smallest immediate
candidate; do not rerun any unsplit top-form cube.

"""
    text = replace_once(text, old, new, "frontier form3 closure")

    old = """order-9 |Bad|=3 initial exact scan:                 15/24 (62.5%).
order-9 |Bad|=3 subsequent form-2 closure:              1/9 (11.1%).
order-9 |Bad|=3 total top forms closed:                16/24 (66.7%).
order-9 |Bad|=3 form-2 root outcomes excluded:           9/9 (100%).
"""
    new = """order-9 |Bad|=3 initial exact scan:                 15/24 (62.5%).
order-9 |Bad|=3 subsequent form-2 closure:                1/1 (100%).
order-9 |Bad|=3 subsequent form-3 closure:                1/1 (100%).
order-9 |Bad|=3 total top forms closed:                17/24 (70.8%).
order-9 |Bad|=3 form-2 root outcomes excluded:           9/9 (100%).
order-9 |Bad|=3 form-3 root outcomes excluded:           6/6 (100%).
"""
    text = replace_once(text, old, new, "frontier progress table")
    write(path, text)


def update_web_memory() -> None:
    path = "Experiments/START_HERE_WEB.md"
    text = read(path)

    current = """

Активная конечная ветвь — порядок `9`, no-HIT, ровно три Bad-точки.
Терминальная ZERO-ветвь и случай `|Bad|=2` закрыты.  Три-Bad классификация
содержит 24 нормальные формы.  Первый точный прогон закрыл 15; отдельные
сертификаты затем полностью исключили формы 2 и 3.  Теперь закрыто `17/24`.

Для формы 3 два независимых решателя проверили все шесть исчерпывающих
канонических исходов корня и дали `6/6 UNSAT`.  Два сложных Good-исхода
дополнительно разбиты на четыре точных представителя; снова `4/4 UNSAT` в
обоих решателях.  Полной таблицы-контрпримера нет.

Остаются формы

```text
11, 15, 16, 18, 21, 23, 24,
```

а также большие мощности Bad и ветвь HIT.  Следующая наиболее компактная
цель — форма 16: после канонического split у неё только два представителя
Good-продукта.

"""
    text = replace_section(
        text,
        "## Текущее математическое состояние",
        "## Последний завершенный прогон",
        current,
        "START_HERE current",
    )

    latest = """

Папка:

```text
Experiments/2026-08-29-order9-case3-root/
```

GitHub Actions:

```text
smoke: 33268344813
full:  33268434711
```

Итог полного прогона:

- базовый SAT-каркас закреплён Git blob
  `efe356acd0047eef8ae5645b2cb04ac2a493632d`;
- шесть из шести канонических исходов формы 3 UNSAT в CaDiCaL195;
- шесть из шести канонических исходов формы 3 UNSAT в Glucose42;
- четыре из четырёх Good-представителей UNSAT в каждом решателе;
- UNKNOWN: 0;
- SAT-моделей и полных контрпримеров: 0;
- технических ошибок: 0;
- форма 3 полностью закрыта;
- общий счёт трёх-Bad форм: `17/24` закрыто.

Компактные результаты находятся в `RESULTS.md`, `run-summary.json` и
`RUN_REPORT.md` той же папки.

"""
    text = replace_section(
        text,
        "## Последний завершенный прогон",
        "## Ретроспектива завершенной цепочки",
        latest,
        "START_HERE latest",
    )

    retrospective = """

Что сработало хорошо:

- вместо повторного unsplit-куба использован доказанный канонический split;
- короткая проверка сразу показала, что общий трудный остаток лежит в двух
  Good-исходах;
- полный запуск независимо закрыл все шесть исходов двумя решателями;
- отдельная разбивка Good-продуктов дала дополнительную проверку `4/4`;
- любой SAT-ответ должен был быть полной таблицей 9x9 и пройти все 81
  подстановку E677;
- результат сохранён в одной датированной папке вместе с точными workflow,
  журналами, сводкой, леммой и справкой Codex.

Общий технический урок прежний: короткая проверка сначала, полный точный
запуск затем, после чего активный workflow удаляется.

"""
    text = replace_section(
        text,
        "## Ретроспектива завершенной цепочки",
        "## Следующий шаг",
        retrospective,
        "START_HERE retrospective",
    )

    next_step = """

Не повторять формы 2 и 3: они закрыты.

Следующий конечный шаг — форма 16.  Использовать тот же исчерпывающий split
корня `Good / row / third-Bad`; у этой формы после остаточной перенумерации
только два представителя Good-продукта.  Сначала короткая проверка обоих
решателей, затем более сильный запуск только для общего остатка.

"""
    text = replace_section(
        text,
        "## Следующий шаг",
        "## Что обновлять после каждого существенного прогона",
        next_step,
        "START_HERE next",
    )
    write(path, text)


def update_experiments_index() -> None:
    path = "Experiments/README.md"
    text = read(path)
    old = """- `2026-08-29-order9-case2-paused/` — exact order-9 three-Bad form-2
  continuation.  Six of six paused leaves are UNSAT in both CaDiCaL195 and
  Glucose42; form 2 is fully excluded and the top-form count is `16/24`.
  Runs: smoke `33267460851`, full `33267614227`.

Previous completed runs:
"""
    new = """- `2026-08-29-order9-case3-root/` — exact order-9 three-Bad form-3
  canonical-root certificate.  Six of six aggregate root outcomes and four
  of four Good-product representatives are UNSAT in both engines; form 3 is
  excluded and the top-form count is `17/24`.  Runs: smoke `33268344813`,
  full `33268434711`.

Previous completed runs:

- `2026-08-29-order9-case2-paused/` — exact form-2 continuation; form 2 is
  fully excluded and raised the count from `15/24` to `16/24`.  Runs: smoke
  `33267460851`, full `33267614227`.
"""
    text = replace_once(text, old, new, "Experiments index")
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
