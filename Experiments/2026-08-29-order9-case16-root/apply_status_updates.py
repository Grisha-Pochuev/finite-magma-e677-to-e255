#!/usr/bin/env python3
"""Apply the exact repository status updates for the form-16 certificate."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one replacement target, found {count}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def replace_section(path: Path, start_header: str, end_header: str, body: str) -> None:
    text = path.read_text(encoding="utf-8")
    start = text.find(start_header)
    if start < 0:
        raise RuntimeError(f"{path}: missing section {start_header!r}")
    end = text.find(end_header, start + len(start_header))
    if end < 0:
        raise RuntimeError(f"{path}: missing section boundary {end_header!r}")
    replacement = start_header + "\n" + body.rstrip() + "\n\n"
    path.write_text(text[:start] + replacement + text[end:], encoding="utf-8")


def update_root_readme() -> None:
    path = ROOT / "README.md"
    old = """- exactly three Bad elements reduce to 24 normalized forms; 15 were UNSAT in
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
    new = """- exactly three Bad elements reduce to 24 normalized forms; 15 were UNSAT in
  the first exact scan, and normalized forms 2, 3, and 16 have now been
  independently excluded, so 18/24 forms are closed;
- form 2 is covered by fourteen exhaustive leaves; forms 3 and 16 each have
  six exhaustive canonical root outcomes.  The form-16 aggregate CaDiCaL
  UNKNOWN is completely discharged by its unique exact Good-product
  representative, UNSAT in both CaDiCaL195 and Glucose42.

The complete certificates are the
[form-2 exclusion](lemmas/e677_order9_three_bad_root_and_case2_reduction.md),
the [form-3 exclusion](lemmas/e677_order9_three_bad_case3_exclusion.md), and
the [form-16 exclusion](lemmas/e677_order9_three_bad_case16_exclusion.md).
The remaining indices are `11,15,18,21,23,24`.  These are finite reductions
only: the HIT branch and the remaining no-HIT forms still prevent a complete
order-9 certificate.
"""
    replace_once(path, old, new)

    old_repro = """.\\verify_order9_terminal_zero.ps1
.\\verify_order9_two_bad_no_hit.ps1
.\\verify_order9_three_bad_case2.ps1
.\\verify_order9_three_bad_case3.ps1
```

The third command checks all fourteen exhaustive leaves of normalized form 2.
The fourth checks the six exhaustive canonical root outcomes of normalized
form 3 and the four finer Good-product representatives, independently in
CaDiCaL195 and Glucose42.
"""
    new_repro = """.\\verify_order9_terminal_zero.ps1
.\\verify_order9_two_bad_no_hit.ps1
.\\verify_order9_three_bad_case2.ps1
.\\verify_order9_three_bad_case3.ps1
.\\verify_order9_three_bad_case16.ps1
```

The third command checks all fourteen exhaustive leaves of normalized form 2.
The fourth checks the six canonical outcomes of form 3 and its four finer
Good-product representatives.  The fifth checks the six canonical outcomes
of form 16 and its two exact Good-product representatives.  Both newest
certificates use CaDiCaL195 and Glucose42 independently.
"""
    replace_once(path, old_repro, new_repro)


def update_active_frontier() -> None:
    path = ROOT / "docs" / "ACTIVE_FRONTIER_MIN.md"
    replace_once(
        path,
        """The remaining three-Bad forms are exactly

```text
11,15,16,18,21,23,24.
```
""",
        """The remaining three-Bad forms after forms 2 and 3 were

```text
11,15,16,18,21,23,24.
```
""",
    )

    old_next = """The next finite step should compare these seven forms by their exact
canonical-root orbit count.  Form `16` has only two Good-product
representatives after the six-outcome split and is the smallest immediate
candidate; do not rerun any unsplit top-form cube.
"""
    new_next = """Top form `16` is now also completely certified.  It has

```text
B={0,2,3}; D: 0->2->3->0;
0*0=1; 1*0=2; 2*0=2.
```

Its canonical strict extra roots are `(0,2)` and `(0,3)`.  For each root the
product is exhaustively Good, row value `0`, or the third Bad point, giving
six aggregate leaves.  Glucose42 proves all `6/6 UNSAT`.  CaDiCaL195 proves
`5/6 UNSAT` at the fixed aggregate boundary; its sole UNKNOWN is
`(0,2)` with Good product.  Residual Good relabelling gives that leaf the
single representative `0*2=4`, and the two exact Good representatives are
independently `2/2 UNSAT` in both engines.  Therefore all six orbits are
excluded and form `16` is UNSAT.

The total closed count is now

```text
18/24.
```

The remaining three-Bad forms are exactly

```text
11,15,18,21,23,24.
```

Exact proof, checker, record, and verifier:

```text
lemmas/e677_order9_three_bad_case16_exclusion.md;
tools/e677_order9_no_hit_bad_count_sat.py;
Experiments/2026-08-29-order9-case16-root/RESULTS.md;
verify_order9_three_bad_case16.ps1.
```

The two smallest next splits are forms `11` and `18`, each with six aggregate
root outcomes.  Form `11` is the next selected finite target.  Do not rerun
forms 2, 3, or 16, and do not rerun any unsplit top-form cube.
"""
    replace_once(path, old_next, new_next)

    old_progress = """order-9 |Bad|=3 subsequent form-2 closure:                1/1 (100%).
order-9 |Bad|=3 subsequent form-3 closure:                1/1 (100%).
order-9 |Bad|=3 total top forms closed:                17/24 (70.8%).
order-9 |Bad|=3 form-2 root outcomes excluded:           9/9 (100%).
order-9 |Bad|=3 form-3 root outcomes excluded:           6/6 (100%).
"""
    new_progress = """order-9 |Bad|=3 subsequent form-2 closure:                1/1 (100%).
order-9 |Bad|=3 subsequent form-3 closure:                1/1 (100%).
order-9 |Bad|=3 subsequent form-16 closure:               1/1 (100%).
order-9 |Bad|=3 total top forms closed:                18/24 (75.0%).
order-9 |Bad|=3 form-2 root outcomes excluded:           9/9 (100%).
order-9 |Bad|=3 form-3 root outcomes excluded:           6/6 (100%).
order-9 |Bad|=3 form-16 root outcomes excluded:          6/6 (100%).
"""
    replace_once(path, old_progress, new_progress)


def update_experiments_readme() -> None:
    path = ROOT / "Experiments" / "README.md"
    old = """## Последний завершенный прогон

- `2026-08-29-order9-case3-root/` — exact order-9 three-Bad form-3
  canonical-root certificate.  Six of six aggregate root outcomes and four
  of four Good-product representatives are UNSAT in both engines; form 3 is
  excluded and the top-form count is `17/24`.  Runs: smoke `33268344813`,
  full `33268434711`.

Previous completed runs:

- `2026-08-29-order9-case2-paused/` — exact form-2 continuation; form 2 is
"""
    new = """## Последний завершенный прогон

- `2026-08-29-order9-case16-root/` — exact order-9 three-Bad form-16
  canonical-root certificate.  The six aggregate outcomes are completely
  excluded after the sole bounded CaDiCaL Good-UNKNOWN is refined to its
  unique labelled representative; the two Good representatives are `2/2
  UNSAT` in both engines.  Form 16 is excluded and the count is `18/24`.
  Runs: smoke `33269622554`, full `33269852847`.

Previous completed runs:

- `2026-08-29-order9-case3-root/` — exact form-3 certificate; six aggregate
  outcomes and four Good representatives are UNSAT in both engines.  Form 3
  raised the count to `17/24`.  Runs: smoke `33268344813`, full
  `33268434711`.

- `2026-08-29-order9-case2-paused/` — exact form-2 continuation; form 2 is
"""
    replace_once(path, old, new)


def update_start_here() -> None:
    path = ROOT / "Experiments" / "START_HERE_WEB.md"

    current = """Активная конечная ветвь — порядок `9`, no-HIT, ровно три Bad-точки.
Терминальная ZERO-ветвь и случай `|Bad|=2` закрыты.  Три-Bad классификация
содержит 24 нормальные формы.  Первый точный прогон закрыл 15; отдельные
сертификаты затем полностью исключили формы 2, 3 и 16.  Теперь закрыто
`18/24`.

Для формы 16 канонические корни — `(0,2)` и `(0,3)`, по три исхода
произведения на каждый.  Glucose42 исключил все шесть.  CaDiCaL195 оставил
неопределённым только широкий исход `(0,2)/Good`, но остаточная перенумерация
сводит его к единственной клетке `0*2=4`; она UNSAT в обоих решателях.
Полной таблицы-контрпримера нет.

Остаются формы

```text
11, 15, 18, 21, 23, 24,
```

а также большие мощности Bad и ветвь HIT.  Следующая компактная цель — форма
11; как и форма 18, она имеет шесть основных корневых исходов.
"""
    replace_section(
        path,
        "## Текущее математическое состояние\n",
        "## Последний завершенный прогон\n",
        current,
    )

    last_run = """Папка:

```text
Experiments/2026-08-29-order9-case16-root/
```

GitHub Actions:

```text
smoke: 33269622554
full:  33269852847
```

Итог полного прогона:

- базовый SAT-каркас закреплён Git blob
  `efe356acd0047eef8ae5645b2cb04ac2a493632d`;
- Glucose42: все шесть канонических исходов формы 16 UNSAT;
- CaDiCaL195: пять из шести широких исходов UNSAT, один Good-исход достиг
  заданной границы;
- два точных Good-представителя: `2/2 UNSAT` в каждом решателе;
- единственный широкий UNKNOWN полностью закрыт своим единственным
  представителем `0*2=4`;
- SAT-моделей и полных контрпримеров: 0;
- технических ошибок: 0;
- форма 16 полностью закрыта;
- общий счёт трёх-Bad форм: `18/24` закрыто.

Компактные результаты находятся в `RESULTS.md`, `run-summary.csv`,
`run-summary.json`, `RUN_REPORT.md` и `closure-summary.json` той же папки.
"""
    replace_section(
        path,
        "## Последний завершенный прогон\n",
        "## Ретроспектива завершенной цепочки\n",
        last_run,
    )

    retrospective = """Что сработало хорошо:

- вместо повторного полного куба использован доказанный канонический разрез;
- короткая проверка сразу локализовала трудность в двух Good-исходах;
- точная разбивка по остаточной симметрии свела их к двум клеткам;
- один широкий предел CaDiCaL не был ошибочно принят за открытый случай:
  единственный представитель этого случая отдельно дал UNSAT;
- любой SAT-ответ должен был быть полной таблицей 9x9 и пройти все 81
  подстановку E677;
- результат сохранён в одной датированной папке вместе с точными сценариями,
  журналами, сводкой, леммой и справкой Codex.

Новый общий технический урок не требуется: короткая проверка, затем точный
запуск, затем обезвреживание активных сценариев остаются рабочей схемой.
"""
    replace_section(
        path,
        "## Ретроспектива завершенной цепочки\n",
        "## Следующий шаг\n",
        retrospective,
    )

    next_step = """Не повторять формы 2, 3 и 16: они закрыты.

Следующий конечный шаг — форма 11.  Использовать тот же исчерпывающий разрез
корня `Good / row / third-Bad`; сначала коротко проверить оба решателя, затем
разбить только оставшиеся Good-исходы на точные представители.  Форма 18
имеет такой же размер основного разреза и остаётся запасной следующей целью.
"""
    replace_section(
        path,
        "## Следующий шаг\n",
        "## Что обновлять после каждого существенного прогона\n",
        next_step,
    )


def validate_experiment_files() -> None:
    folder = ROOT / "Experiments" / "2026-08-29-order9-case16-root"
    required = {
        "README.md": "all six exhaustive outcomes are excluded",
        "RESULTS.md": "18/24 closed",
        "CODEX_HANDOFF.md": "Top form `16` is exactly excluded",
        "closure-summary.json": '"mathematical_result": "FORM16_UNSAT"',
    }
    for name, marker in required.items():
        text = (folder / name).read_text(encoding="utf-8")
        if marker not in text:
            raise RuntimeError(f"{name}: missing marker {marker!r}")


def main() -> int:
    validate_experiment_files()
    update_root_readme()
    update_active_frontier()
    update_experiments_readme()
    update_start_here()
    print("Applied order-9 form-16 status updates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
