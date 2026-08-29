"""Find a non-power row-label family passing the exact E677 base reach test.

A family S of at most five permutations of the order-five base labels is
admissible when, for every alpha,beta in S and every base pair a,b, some
gamma in S can be the intermediate row-label permutation and return the
E677 base coordinate to a.  The six cyclic power families are excluded.
"""

from __future__ import annotations

import argparse
import itertools
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "vendor" / "python_sat311"))
from pysat.solvers import Solver  # type: ignore


def exactly_one(clauses: list[list[int]], literals: list[int]) -> None:
    clauses.append(literals)
    for left, right in itertools.combinations(literals, 2):
        clauses.append([-left, -right])


def load_table(path: Path) -> list[list[int]]:
    return [[int(value) for value in line.split()] for line in path.read_text().splitlines() if line.strip()]


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[x]] for x in range(len(left)))


def inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(permutation)
    for source, value in enumerate(permutation):
        result[value] = source
    return tuple(result)


def power_family(theta: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    identity = tuple(range(len(theta)))
    values = [identity]
    for _ in range(1, len(theta)):
        values.append(compose(theta, values[-1]))
    return frozenset(values)


def cycle_type(permutation: tuple[int, ...]) -> tuple[int, ...]:
    seen: set[int] = set()
    lengths = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        value, length = start, 0
        while value not in seen:
            seen.add(value)
            value = permutation[value]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def at_most(clauses: list[list[int]], literals: list[int], bound: int, next_variable: int) -> int:
    # Deterministic prefix counter with states 0,...,bound.
    states = []
    for _ in range(len(literals) + 1):
        row = list(range(next_variable, next_variable + bound + 1))
        next_variable += bound + 1
        exactly_one(clauses, row)
        states.append(row)
    clauses.append([states[0][0]])
    for count in range(1, bound + 1):
        clauses.append([-states[0][count]])
    for index, literal in enumerate(literals):
        for count in range(bound + 1):
            clauses.append([-states[index][count], literal, states[index + 1][count]])
            if count < bound:
                clauses.append([-states[index][count], -literal, states[index + 1][count + 1]])
            else:
                clauses.append([-states[index][count], -literal])
    return next_variable


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--solutions", type=int, default=3)
    parser.add_argument("--unanchored", action="store_true")
    parser.add_argument("--count-only", action="store_true")
    parser.add_argument("--full-test", action="store_true")
    parser.add_argument("--full-seconds", type=float, default=5.0)
    args = parser.parse_args()
    base = load_table(ROOT / "cache" / "eq677-db" / "5" / "0")
    permutations = list(itertools.permutations(range(5)))
    index = {permutation: position for position, permutation in enumerate(permutations)}
    selected = [position + 1 for position in range(len(permutations))]
    identity = tuple(range(5))

    reach_clauses: list[list[int]] = []
    for alpha_index, alpha in enumerate(permutations):
        for beta_index, beta in enumerate(permutations):
            for a in range(5):
                for b in range(5):
                    u = base[beta[b]][a]
                    good = []
                    for gamma_index, gamma in enumerate(permutations):
                        v = base[gamma[u]][b]
                        w = base[alpha[a]][v]
                        if base[beta[b]][w] == a:
                            good.append(selected[gamma_index])
                    reach_clauses.append([-selected[alpha_index], -selected[beta_index], *good])

    cyclic_families = {
        power_family(theta)
        for theta in permutations
        if cycle_type(theta) == (5,)
    }
    exclusions = [
        [-selected[index[permutation]] for permutation in family]
        for family in cyclic_families
    ]
    automorphisms = [
        permutation
        for permutation in permutations
        if all(
            permutation[base[x][y]] == base[permutation[x]][permutation[y]]
            for x in range(5)
            for y in range(5)
        )
    ]

    for bound in range(1 if args.unanchored else 2, 6):
        clauses = [*reach_clauses, *exclusions]
        if args.unanchored:
            clauses.append([-selected[index[identity]]])
            clauses.append([selected[position] for position, permutation in enumerate(permutations) if permutation != identity])
        else:
            clauses.append([selected[index[identity]]])
            clauses.append([selected[position] for position, permutation in enumerate(permutations) if permutation != identity])
        next_variable = at_most(clauses, selected, bound, len(selected) + 1)
        with Solver(name="glucose42", bootstrap_with=clauses) as solver:
            if not solver.solve():
                print(f"bound={bound}: UNSAT", flush=True)
                continue
            found = 0
            full_unsat = 0
            full_good = 0
            full_unknown: list[str] = []
            while args.solutions == 0 or found < args.solutions:
                model = {literal for literal in solver.get_model() if literal > 0}
                family = [permutation for literal, permutation in zip(selected, permutations) if literal in model]
                if len(family) > bound or (identity in family) == args.unanchored:
                    raise RuntimeError("bad decoded family")
                for alpha in family:
                    for beta in family:
                        for a in range(5):
                            for b in range(5):
                                u = base[beta[b]][a]
                                if not any(
                                    base[beta[b]][base[alpha[a]][base[gamma[u]][b]]] == a
                                    for gamma in family
                                ):
                                    raise RuntimeError("decoded family fails base reach")
                found += 1
                if not args.count_only:
                    print(
                        f"bound={bound}: SAT solution={found}; selected={len(family)}; "
                        f"variables={next_variable-1}; clauses={len(clauses)}"
                    )
                full_family = (
                    list(family)
                    if args.unanchored
                    else [identity, *[permutation for permutation in family if permutation != identity]]
                )
                while len(full_family) < 5:
                    full_family.append(full_family[0])
                encoded_full = "/".join("".join(map(str, permutation)) for permutation in full_family)
                if not args.count_only:
                    print("FULL=" + encoded_full)
                if args.full_test:
                    runtime = tempfile.gettempdir() + r"\e677_sat_runtime"
                    source = (
                        "import sys,runpy; "
                        f"sys.path[:0]=[{runtime!r}]; "
                        "sys.argv=['tools/e677_skew_rowlabel_counterexample_sat.py',"
                        f"'--fibre','5','--row-maps',{encoded_full!r},'--allow-good',"
                        f"'--seconds',{str(args.full_seconds)!r}]; "
                        "runpy.run_path(r'tools/e677_skew_rowlabel_counterexample_sat.py',run_name='__main__')"
                    )
                    completed = subprocess.run(
                        [sys.executable, "-c", source],
                        cwd=ROOT,
                        capture_output=True,
                        text=True,
                        timeout=args.full_seconds + 15,
                    )
                    output = completed.stdout + completed.stderr
                    if "UNSAT" in output:
                        full_unsat += 1
                    elif "VERIFIED E677 MODEL" in output:
                        if "bad=[]" not in output:
                            print(output)
                            print(f"FULL TEST FOUND COUNTEREXAMPLE FAMILY={encoded_full}")
                            return 0
                        full_good += 1
                        print(f"Good E677 survivor family={encoded_full}", flush=True)
                    else:
                        full_unknown.append(encoded_full)
                    if found % 10 == 0:
                        print(
                            f"full-progress={found}; unsat={full_unsat}; good={full_good}; "
                            f"unknown={len(full_unknown)}",
                            flush=True,
                        )

                family_set = frozenset(family)
                orbit = set()
                for automorphism in automorphisms:
                    automorphism_inverse = inverse(automorphism)
                    orbit.add(
                        frozenset(
                            compose(compose(automorphism, permutation), automorphism_inverse)
                            for permutation in family_set
                        )
                    )
                for conjugate_family in orbit:
                    solver.add_clause([-selected[index[permutation]] for permutation in conjugate_family])
                if not args.count_only:
                    print(f"orbit-size={len(orbit)}", flush=True)
                if not solver.solve():
                    print(f"complete-orbit-count={found}; bound={bound}")
                    if args.full_test:
                        print(
                            f"full-complete: unsat={full_unsat}; good={full_good}; "
                            f"unknown={len(full_unknown)}"
                        )
                        if full_unknown:
                            print("full-unknown=" + ",".join(full_unknown))
                    break
            return 0
    print("UNSAT: no non-power family of at most five permutations")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
