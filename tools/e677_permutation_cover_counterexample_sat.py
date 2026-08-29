"""Exact permutation-cover counterexample search over a verified base magma.

For a fibre of size k, the lifted operation has the form

    (a,i) * (b,j) = (a*b, P[a,i,b](j)),

where every P[a,i,b] is a permutation of the fibre.  The script encodes all
E677 instances, forces one lifted point to violate E255, and verifies every
cell of any decoded finite table.
"""

from __future__ import annotations

import argparse
import itertools
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "vendor" / "python_sat311"))
from pysat.solvers import Solver  # type: ignore


def exactly_one(clauses: list[list[int]], literals: list[int]) -> None:
    clauses.append(literals)
    for left, right in itertools.combinations(literals, 2):
        clauses.append([-left, -right])


def load_table(path: Path) -> list[list[int]]:
    table = [[int(value) for value in line.split()] for line in path.read_text().splitlines() if line.strip()]
    n = len(table)
    if n == 0 or any(len(row) != n for row in table):
        raise RuntimeError(f"malformed table: {path}")
    return table


def load_local_seed(path: Path, fibre: int) -> dict[str, list[list[int]]]:
    seed: dict[str, list[list[int]]] = {}
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        name, encoded = line.split("=", 1)
        permutations = [[int(value) for value in word] for word in encoded.split("/")]
        if len(permutations) != fibre or any(sorted(permutation) != list(range(fibre)) for permutation in permutations):
            raise RuntimeError(f"bad local seed family {name}")
        seed[name] = permutations
    if set(seed) != set("ABCFG"):
        raise RuntimeError(f"local seed must contain A,B,C,F,G: {sorted(seed)}")
    return seed


def verify_e677(table: list[list[int]]) -> None:
    n = len(table)
    if any(sorted(row) != list(range(n)) for row in table):
        raise RuntimeError("a left row is not a permutation")
    for x in range(n):
        for y in range(n):
            value = table[y][table[x][table[table[y][x]][y]]]
            if value != x:
                raise RuntimeError(f"E677 failure at x={x}, y={y}: {value}")


def bad_points(table: list[list[int]]) -> list[int]:
    return [x for x in range(len(table)) if table[table[table[x][x]][x]][x] != x]


def build_formula(base: list[list[int]], fibre: int) -> tuple[list[list[int]], callable, int]:
    n = len(base)

    def cell(left_base: int, left_fibre: int, right_base: int, right_fibre: int, out_fibre: int) -> int:
        return 1 + (((((left_base * fibre + left_fibre) * n + right_base) * fibre + right_fibre) * fibre) + out_fibre)

    clauses: list[list[int]] = []
    for left_base in range(n):
        for left_fibre in range(fibre):
            for right_base in range(n):
                for right_fibre in range(fibre):
                    exactly_one(
                        clauses,
                        [cell(left_base, left_fibre, right_base, right_fibre, value) for value in range(fibre)],
                    )
                for value in range(fibre):
                    exactly_one(
                        clauses,
                        [cell(left_base, left_fibre, right_base, right_fibre, value) for right_fibre in range(fibre)],
                    )

    next_variable = n * n * fibre ** 3 + 1
    for x in range(n):
        for x_fibre in range(fibre):
            for y in range(n):
                u = base[y][x]
                v = base[u][y]
                w = base[x][v]
                if base[y][w] != x:
                    raise RuntimeError(f"base fails E677 at x={x}, y={y}")
                for y_fibre in range(fibre):
                    v_aux = list(range(next_variable, next_variable + fibre))
                    next_variable += fibre
                    w_aux = list(range(next_variable, next_variable + fibre))
                    next_variable += fibre
                    exactly_one(clauses, v_aux)
                    exactly_one(clauses, w_aux)
                    for u_fibre in range(fibre):
                        for v_fibre in range(fibre):
                            clauses.append(
                                [
                                    -cell(y, y_fibre, x, x_fibre, u_fibre),
                                    -cell(u, u_fibre, y, y_fibre, v_fibre),
                                    v_aux[v_fibre],
                                ]
                            )
                    for v_fibre in range(fibre):
                        for w_fibre in range(fibre):
                            clauses.append(
                                [
                                    -v_aux[v_fibre],
                                    -cell(x, x_fibre, v, v_fibre, w_fibre),
                                    w_aux[w_fibre],
                                ]
                            )
                    for w_fibre in range(fibre):
                        clauses.append([-w_aux[w_fibre], cell(y, y_fibre, w, w_fibre, x_fibre)])
    return clauses, cell, next_variable - 1


def bad_target_clauses(
    base: list[list[int]], fibre: int, cell: callable, x: int, x_fibre: int
) -> list[list[int]]:
    first_base = base[x][x]
    second_base = base[first_base][x]
    if base[second_base][x] != x:
        raise RuntimeError(f"base point {x} is already Bad")
    clauses = []
    for first_fibre in range(fibre):
        for second_fibre in range(fibre):
            clauses.append(
                [
                    -cell(x, x_fibre, x, x_fibre, first_fibre),
                    -cell(first_base, first_fibre, x, x_fibre, second_fibre),
                    -cell(second_base, second_fibre, x, x_fibre, x_fibre),
                ]
            )
    return clauses


def decode_table(base: list[list[int]], fibre: int, cell: callable, model: set[int]) -> list[list[int]]:
    n = len(base)
    order = n * fibre
    table = [[0] * order for _ in range(order)]
    for left_base in range(n):
        for left_fibre in range(fibre):
            left = fibre * left_base + left_fibre
            for right_base in range(n):
                for right_fibre in range(fibre):
                    values = [
                        value
                        for value in range(fibre)
                        if cell(left_base, left_fibre, right_base, right_fibre, value) in model
                    ]
                    if len(values) != 1:
                        raise RuntimeError("bad decoded fibre cell")
                    right = fibre * right_base + right_fibre
                    table[left][right] = fibre * base[left_base][right_base] + values[0]
    return table


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, default=ROOT / "cache" / "eq677-db" / "11" / "0")
    parser.add_argument("--fibre", type=int, default=3)
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--seconds-per-target", type=float, default=30.0)
    parser.add_argument("--target-base", type=int)
    parser.add_argument("--target-fibre", type=int)
    parser.add_argument("--fix-q-fibre", type=Path)
    parser.add_argument("--fix-idempotent-base", type=int)
    parser.add_argument("--fix-idempotent-fibre", type=Path)
    parser.add_argument("--fix-local-seed", type=Path)
    args = parser.parse_args()
    if args.fibre < 2:
        raise SystemExit("fibre must be at least two")

    base = load_table(args.base)
    verify_e677(base)
    if bad_points(base):
        raise RuntimeError("base must satisfy E255")
    clauses, cell, variables = build_formula(base, args.fibre)
    if args.fix_q_fibre is not None:
        if args.target_base is None:
            raise SystemExit("--fix-q-fibre requires --target-base")
        fibre_table = load_table(args.fix_q_fibre)
        if len(fibre_table) != args.fibre:
            raise SystemExit("fixed q-fibre table has the wrong order")
        verify_e677(fibre_table)
        x = args.target_base
        p = base[x][x]
        q = base[p][x]
        if base[q][q] != q:
            raise SystemExit("the target fixer q is not idempotent in the base")
        for left_fibre in range(args.fibre):
            for right_fibre in range(args.fibre):
                clauses.append(
                    [cell(q, left_fibre, q, right_fibre, fibre_table[left_fibre][right_fibre])]
                )
        print(f"fixed q-fibre: q={q}; table={args.fix_q_fibre}", flush=True)
    if (args.fix_idempotent_base is None) != (args.fix_idempotent_fibre is None):
        raise SystemExit("--fix-idempotent-base and --fix-idempotent-fibre must be used together")
    if args.fix_idempotent_base is not None and args.fix_idempotent_fibre is not None:
        e = args.fix_idempotent_base
        if not 0 <= e < len(base) or base[e][e] != e:
            raise SystemExit("selected base point is not idempotent")
        fibre_table = load_table(args.fix_idempotent_fibre)
        if len(fibre_table) != args.fibre:
            raise SystemExit("fixed idempotent-fibre table has the wrong order")
        verify_e677(fibre_table)
        for left_fibre in range(args.fibre):
            for right_fibre in range(args.fibre):
                clauses.append(
                    [cell(e, left_fibre, e, right_fibre, fibre_table[left_fibre][right_fibre])]
                )
        print(f"fixed idempotent fibre: e={e}; table={args.fix_idempotent_fibre}", flush=True)
    if args.fix_local_seed is not None:
        if args.target_base is None:
            raise SystemExit("--fix-local-seed requires --target-base")
        seed = load_local_seed(args.fix_local_seed, args.fibre)
        x = args.target_base
        p = base[x][x]
        q = base[p][x]
        r = base[x][q]
        if len({x, p, q, r}) != 4:
            raise SystemExit("fixed local seed currently requires four distinct base roles")
        blocks = {
            "A": (q, x),
            "B": (x, q),
            "C": (x, r),
            "F": (x, x),
            "G": (p, x),
        }
        for name, (left_base, right_base) in blocks.items():
            for left_fibre, permutation in enumerate(seed[name]):
                for right_fibre, value in enumerate(permutation):
                    clauses.append([cell(left_base, left_fibre, right_base, right_fibre, value)])
        print(f"fixed local seed: x={x}, p={p}, q={q}, r={r}; file={args.fix_local_seed}", flush=True)
    print(
        f"encoding: base-order={len(base)}; fibre={args.fibre}; lift-order={len(base)*args.fibre}; "
        f"variables={variables}; clauses={len(clauses)}",
        flush=True,
    )

    if args.target_base is not None and not 0 <= args.target_base < len(base):
        raise SystemExit("target base is out of range")
    if args.target_fibre is not None and not 0 <= args.target_fibre < args.fibre:
        raise SystemExit("target fibre is out of range")
    target_bases = range(len(base)) if args.target_base is None else (args.target_base,)
    target_fibres = range(args.fibre) if args.target_fibre is None else (args.target_fibre,)

    unsat = 0
    unknown: list[int] = []
    for x in target_bases:
        for x_fibre in target_fibres:
            target = args.fibre * x + x_fibre
            target_clauses = bad_target_clauses(base, args.fibre, cell, x, x_fibre)
            with Solver(name=args.solver, bootstrap_with=[*clauses, *target_clauses]) as solver:
                timer = threading.Timer(args.seconds_per_target, solver.interrupt)
                timer.start()
                started = time.time()
                try:
                    result = solver.solve_limited(expect_interrupt=True)
                finally:
                    timer.cancel()
                if result is None:
                    unknown.append(target)
                    solver.clear_interrupt()
                    print(f"target={target}: UNKNOWN ({time.time()-started:.3f}s)", flush=True)
                    continue
                if result is False:
                    unsat += 1
                    continue
                model = {literal for literal in solver.get_model() if literal > 0}
            table = decode_table(base, args.fibre, cell, model)
            verify_e677(table)
            bad = bad_points(table)
            if target not in bad:
                raise RuntimeError(f"target {target} is not Bad after decoding")
            print(f"VERIFIED COUNTEREXAMPLE: target={target}; bad={bad}")
            for row in table:
                print(" ".join(map(str, row)))
            return 0
    status = "UNSAT" if not unknown else "INCOMPLETE"
    print(f"{status}: unsat-targets={unsat}; unknown-targets={unknown}")
    return 2 if not unknown else 3


if __name__ == "__main__":
    raise SystemExit(main())
