#!/usr/bin/env python3
"""Collect solver summaries into JSON, CSV, and a short Markdown report."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expected", type=int, default=2)
    args = parser.parse_args()

    records = []
    for path in sorted(args.input.rglob("summary.json")):
        records.append(json.loads(path.read_text(encoding="utf-8")))

    args.output.mkdir(parents=True, exist_ok=True)
    missing = max(0, args.expected - len(records))
    aggregate = {
        "expected_summaries": args.expected,
        "found_summaries": len(records),
        "missing_summaries": missing,
        "all_six_unsat_engines": sum(
            item.get("normalized_result") == "ALL_SIX_UNSAT" for item in records
        ),
        "verified_counterexamples": sum(
            item.get("normalized_result") == "VERIFIED_NO_HIT_COUNTEREXAMPLE"
            for item in records
        ),
        "bounded_unknown_engines": sum(
            item.get("normalized_result") == "BOUNDED_UNKNOWN" for item in records
        ),
        "technical_failures": sum(
            item.get("normalized_result") == "TECHNICAL_FAILURE" for item in records
        )
        + missing,
        "records": records,
    }
    (args.output / "run-summary.json").write_text(
        json.dumps(aggregate, indent=2) + "\n", encoding="utf-8"
    )

    fields = [
        "phase",
        "solver",
        "normalized_result",
        "raw_exit_code",
        "leaf_count",
        "sat_count",
        "unsat_count",
        "unknown_count",
        "base_checker_git_blob",
        "commit_sha",
        "cpu",
        "technical_reason",
    ]
    with (args.output / "run-summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in records:
            writer.writerow({field: item.get(field, "") for field in fields})

    lines = [
        "# Run report",
        "",
        f"- Expected summaries: {args.expected}",
        f"- Found summaries: {len(records)}",
        f"- Missing summaries: {missing}",
        f"- Engines proving all six leaves UNSAT: {aggregate['all_six_unsat_engines']}",
        f"- Verified no-HIT counterexamples: {aggregate['verified_counterexamples']}",
        f"- Engines with bounded UNKNOWN leaves: {aggregate['bounded_unknown_engines']}",
        f"- Technical failures: {aggregate['technical_failures']}",
        "",
        "| Phase | Solver | Result | UNSAT | UNKNOWN | SAT |",
        "| --- | --- | --- | ---: | ---: | ---: |",
    ]
    for item in records:
        lines.append(
            f"| {item.get('phase')} | {item.get('solver')} | "
            f"{item.get('normalized_result')} | {item.get('unsat_count')} | "
            f"{item.get('unknown_count')} | {item.get('sat_count')} |"
        )
    (args.output / "RUN_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines))
    return 1 if aggregate["technical_failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
