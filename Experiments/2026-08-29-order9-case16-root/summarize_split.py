#!/usr/bin/env python3
"""Normalize one exact order-9 three-Bad form-16 split run."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path


PATTERN = re.compile(
    r"bad3 case 16/24 split (?P<ordinal>\d+)/(?P<total>\d+) (?P<name>.*): "
    r"(?P<status>SAT|UNSAT|UNKNOWN); elapsed=(?P<elapsed>[0-9.]+)s; "
    r"conflicts=(?P<conflicts>\d+)"
)


def cpu_model() -> str:
    try:
        for line in Path("/proc/cpuinfo").read_text(encoding="utf-8", errors="replace").splitlines():
            if line.lower().startswith("model name"):
                return line.split(":", 1)[1].strip()
    except OSError:
        pass
    return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True)
    parser.add_argument("--solver", required=True)
    parser.add_argument("--expected", type=int, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--exit-code", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    text = args.log.read_text(encoding="utf-8", errors="replace")
    leaves = [
        {
            "ordinal": int(match.group("ordinal")),
            "reported_total": int(match.group("total")),
            "name": match.group("name"),
            "status": match.group("status"),
            "elapsed_seconds": float(match.group("elapsed")),
            "conflicts": int(match.group("conflicts")),
        }
        for match in PATTERN.finditer(text)
    ]

    counts = {
        status: sum(leaf["status"] == status for leaf in leaves)
        for status in ("SAT", "UNSAT", "UNKNOWN")
    }
    verified = "status: VERIFIED NO-HIT COUNTEREXAMPLE" in text
    reason = ""

    if args.exit_code not in (0, 2, 3):
        result = "TECHNICAL_FAILURE"
        reason = f"unexpected exit code {args.exit_code}"
    elif len(leaves) != args.expected:
        result = "TECHNICAL_FAILURE"
        reason = f"expected {args.expected} leaves, found {len(leaves)}"
    elif any(leaf["reported_total"] != args.expected for leaf in leaves):
        result = "TECHNICAL_FAILURE"
        reason = "reported split total is inconsistent"
    elif counts["SAT"]:
        if args.exit_code == 0 and verified:
            result = "VERIFIED_NO_HIT_COUNTEREXAMPLE"
        else:
            result = "TECHNICAL_FAILURE"
            reason = "SAT leaf lacks the complete-table verifier marker"
    elif counts["UNSAT"] == args.expected and args.exit_code == 2:
        result = "ALL_UNSAT"
    elif counts["UNKNOWN"] and args.exit_code == 3:
        result = "BOUNDED_UNKNOWN"
    else:
        result = "TECHNICAL_FAILURE"
        reason = "leaf statuses and exit code disagree"

    record = {
        "slot": f"{args.mode}-{args.solver}",
        "problem": "order9-three-bad-form16",
        "target": args.mode,
        "profile": args.solver,
        "mode": args.mode,
        "solver": args.solver,
        "expected_leaf_count": args.expected,
        "raw_result": f"checker-exit-{args.exit_code}",
        "normalized_result": result,
        "final_status": result,
        "raw_exit_code": args.exit_code,
        "termination_reason": reason or result,
        "technical_failure": result == "TECHNICAL_FAILURE",
        "model_found": result == "VERIFIED_NO_HIT_COUNTEREXAMPLE",
        "verified_model_marker": verified,
        "leaf_count": len(leaves),
        "sat_count": counts["SAT"],
        "unsat_count": counts["UNSAT"],
        "unknown_count": counts["UNKNOWN"],
        "elapsed_seconds": round(sum(float(leaf["elapsed_seconds"]) for leaf in leaves), 3),
        "conflicts": sum(int(leaf["conflicts"]) for leaf in leaves),
        "cpu": cpu_model(),
        "commit_sha": os.environ.get("GITHUB_SHA", "unknown"),
        "leaves": leaves,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2))
    return 1 if result == "TECHNICAL_FAILURE" else 0


if __name__ == "__main__":
    raise SystemExit(main())
