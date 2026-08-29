"""Classify the base-coordinate reachability of skew row-label extensions.

For base action row(a,i)=theta^i(a), E677 can hold for a full pair only if
some intermediate fibre value t makes the base-coordinate path return to a.
This script checks that necessary condition exactly for every theta.
"""

from __future__ import annotations

import argparse
import itertools
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_table(path: Path) -> list[list[int]]:
    return [[int(value) for value in line.split()] for line in path.read_text().splitlines() if line.strip()]


def powers(permutation: tuple[int, ...], count: int) -> list[tuple[int, ...]]:
    result = [tuple(range(len(permutation)))]
    for _ in range(1, count):
        result.append(tuple(permutation[result[-1][x]] for x in range(len(permutation))))
    return result


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


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[x]] for x in range(len(left)))


def inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(permutation)
    for source, value in enumerate(permutation):
        result[value] = source
    return tuple(result)


def first_failure(base: list[list[int]], fibre: int, theta: tuple[int, ...]):
    m = len(base)
    theta_powers = powers(theta, fibre)

    def row_label(left_base: int, left_fibre: int) -> int:
        return theta_powers[left_fibre][left_base]

    for a in range(m):
        for b in range(m):
            for i in range(fibre):
                for j in range(fibre):
                    u = base[row_label(b, j)][a]
                    reachable = []
                    for t in range(fibre):
                        v = base[row_label(u, t)][b]
                        w = base[row_label(a, i)][v]
                        reachable.append(base[row_label(b, j)][w])
                    if a not in reachable:
                        return a, b, i, j, u, tuple(reachable)
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, default=ROOT / "cache" / "eq677-db" / "5" / "0")
    parser.add_argument("--fibre", type=int, default=5)
    args = parser.parse_args()
    base = load_table(args.base)
    m = len(base)
    survivors = []
    failures: Counter[tuple[int, ...]] = Counter()
    examples = {}
    for theta in itertools.permutations(range(m)):
        failure = first_failure(base, args.fibre, theta)
        kind = cycle_type(theta)
        if failure is None:
            survivors.append(theta)
        else:
            failures[kind] += 1
            examples.setdefault(kind, (theta, failure))

    print(f"complete: theta={math_factorial(m)}; survivors={len(survivors)}")
    for theta in survivors:
        print(f"survivor={theta}; cycle-type={cycle_type(theta)}")
    print("failed-by-cycle-type=" + ", ".join(f"{kind}:{count}" for kind, count in sorted(failures.items())))
    for kind, (theta, failure) in sorted(examples.items()):
        print(f"failure-example type={kind}; theta={theta}; data={failure}")
    permutations = list(itertools.permutations(range(m)))
    automorphisms = [
        permutation
        for permutation in permutations
        if all(
            permutation[base[x][y]] == base[permutation[x]][permutation[y]]
            for x in range(m)
            for y in range(m)
        )
    ]
    remaining = {theta for theta in survivors if cycle_type(theta) == (5,)}
    orbit_sizes = []
    orbit_representatives = []
    while remaining:
        theta = next(iter(remaining))
        orbit = {
            compose(compose(automorphism, theta), inverse(automorphism))
            for automorphism in automorphisms
        } & remaining
        orbit_sizes.append(len(orbit))
        orbit_representatives.append(theta)
        remaining -= orbit
    print(f"automorphisms={len(automorphisms)}; fivecycle-orbits={orbit_sizes}")
    print(f"fivecycle-representatives={orbit_representatives}")
    return 0 if survivors else 2


def math_factorial(value: int) -> int:
    result = 1
    for factor in range(2, value + 1):
        result *= factor
    return result


if __name__ == "__main__":
    raise SystemExit(main())
