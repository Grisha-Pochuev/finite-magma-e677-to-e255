"""Classify the complete-mapping T2 absorber family against tuple 6."""

from __future__ import annotations

import collections
import itertools


N = 7
CANONICAL_D = tuple(
    tuple(map(int, text))
    for text in ("0125634", "0145236", "1023546", "1024356")
)


def inverse(permutation):
    result = [0] * N
    for inp, value in enumerate(permutation):
        result[value] = inp
    return tuple(result)


def candidate_P():
    result = []
    for P in itertools.permutations(range(N)):
        difference = tuple((P[h] - h) % N for h in range(N))
        if len(set(difference)) != N:
            continue
        if any((P[h] + h) % N == 0 for h in range(N)):
            continue
        O7 = tuple(
            tuple((P[(z + s) % N] + s) % N for z in range(N))
            for s in range(N)
        )
        if len(set(O7)) != N:
            continue
        result.append((P, O7))
    return tuple(result)


def tuple6_kernel_failure(D, O7):
    inverse_O7 = tuple(inverse(row) for row in O7)
    # This absorber has A=id.  Equality of the forced H values is equality
    # of rho=D(q-t)-q; B is injective and therefore irrelevant.
    for s in range(N):
        by_z = {}
        by_rho = {}
        for t in range(N):
            q = O7[t][s]
            z = inverse_O7[t][s]
            rho = (D[(q - t) % N] - q) % N
            if z in by_z and by_z[z] != rho:
                return "cell-conflict"
            if rho in by_rho and by_rho[rho] != z:
                return "value-collision"
            by_z[z] = rho
            by_rho[rho] = z
    return None


def main() -> int:
    candidates = candidate_P()
    if len(candidates) != 42:
        raise AssertionError(f"complete-mapping P count is {len(candidates)}")
    expected = {
        "0125634": {"value-collision": 11, "cell-conflict": 31},
        "0145236": {"cell-conflict": 32, "value-collision": 10},
        "1023546": {"value-collision": 23, "cell-conflict": 19},
        "1024356": {"value-collision": 20, "cell-conflict": 22},
    }
    print(f"complete-mapping-P={len(candidates)}")
    total_survivors = 0
    for D in CANONICAL_D:
        reasons = collections.Counter()
        survivors = []
        for P, O7 in candidates:
            reason = tuple6_kernel_failure(D, O7)
            if reason is None:
                survivors.append(P)
            else:
                reasons[reason] += 1
        name = "".join(map(str, D))
        if dict(reasons) != expected[name] or survivors:
            raise AssertionError(
                f"unexpected classification for D={name}: "
                f"reasons={dict(reasons)}, survivors={survivors}"
            )
        total_survivors += len(survivors)
        print(
            f"D={name}; survivors={len(survivors)}; "
            f"reasons={dict(reasons)}"
        )
    print(
        f"pairs={len(candidates)*len(CANONICAL_D)}; "
        f"tuple6-survivors={total_survivors}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
