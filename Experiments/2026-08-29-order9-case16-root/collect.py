#!/usr/bin/env python3
"""Collect small per-job summaries for the order-9 form-16 experiment."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expected", type=int, required=True)
    args = parser.parse_args()

    records: list[dict[str, Any]] = []
    broken: list[str] = []
    for path in sorted(args.input.rglob("summary.json")):
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(record, dict):
                raise ValueError("summary is not an object")
            record["source_path"] = str(path)
            records.append(record)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            broken.append(f"{path}: {exc}")

    records.sort(key=lambda item: (str(item.get("mode", "")), str(item.get("solver", ""))))
    technical = sum(bool(item.get("technical_failure")) for item in records)
    models = sum(bool(item.get("model_found")) for item in records)
    all_unsat = sum(item.get("normalized_result") == "ALL_UNSAT" for item in records)
    bounded_unknown = sum(item.get("normalized_result") == "BOUNDED_UNKNOWN" for item in records)

    aggregate = {
        "expected_summary_count": args.expected,
        "summary_count": len(records),
        "broken_summaries": broken,
        "technical_failure_count": technical,
        "verified_model_count": models,
        "all_unsat_job_count": all_unsat,
        "bounded_unknown_job_count": bounded_unknown,
        "records": records,
    }

    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "run-summary.json").write_text(
        json.dumps(aggregate, indent=2) + "\n", encoding="utf-8"
    )

    columns = [
        "slot",
        "mode",
        "solver",
        "normalized_result",
        "raw_exit_code",
        "leaf_count",
        "sat_count",
        "unsat_count",
        "unknown_count",
        "elapsed_seconds",
        "conflicts",
        "technical_failure",
        "model_found",
        "cpu",
        "commit_sha",
    ]
    with (args.output / "run-summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for record in records:
            writer.writerow({key: record.get(key, "") for key in columns})

    lines = [
        "# Order-9 form-16 run report",
        "",
        f"- expected summaries: {args.expected}",
        f"- received summaries: {len(records)}",
        f"- broken summaries: {len(broken)}",
        f"- technical failures: {technical}",
        f"- verified complete counterexamples: {models}",
        f"- all-UNSAT jobs: {all_unsat}",
        f"- bounded-UNKNOWN jobs: {bounded_unknown}",
        "",
        "| mode | solver | result | UNSAT | UNKNOWN | SAT | seconds |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for record in records:
        lines.append(
            "| {mode} | {solver} | {result} | {unsat} | {unknown} | {sat} | {seconds} |".format(
                mode=record.get("mode", ""),
                solver=record.get("solver", ""),
                result=record.get("normalized_result", ""),
                unsat=record.get("unsat_count", ""),
                unknown=record.get("unknown_count", ""),
                sat=record.get("sat_count", ""),
                seconds=record.get("elapsed_seconds", ""),
            )
        )
    if broken:
        lines.extend(["", "## Broken summaries", "", *[f"- {item}" for item in broken]])
    (args.output / "RUN_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    ok = len(records) == args.expected and not broken and technical == 0
    print(json.dumps(aggregate, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
