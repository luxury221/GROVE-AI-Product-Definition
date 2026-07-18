#!/usr/bin/env python3
"""Score GROVE-AI opportunities from a CSV file using only the Python standard library."""

from __future__ import annotations
import argparse
import csv
from pathlib import Path

NUMERIC_FIELDS = [
    "importance",
    "dissatisfaction",
    "frequency",
    "evidence_confidence",
    "strategic_fit",
    "technical_risk",
    "business_risk",
]

def parse_score(row: dict[str, str], field: str) -> float:
    try:
        value = float(row[field])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"Invalid or missing {field!r} in {row.get('opportunity_id', '<unknown>')}") from exc
    if not 1 <= value <= 5:
        raise ValueError(f"{field} must be between 1 and 5, got {value}")
    return value

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()

    with args.input_csv.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        raise SystemExit("Input CSV has no data rows.")

    raw_scores = []
    for row in rows:
        vals = {field: parse_score(row, field) for field in NUMERIC_FIELDS}
        raw = (
            vals["importance"]
            * vals["dissatisfaction"]
            * vals["frequency"]
            * vals["evidence_confidence"]
            * vals["strategic_fit"]
        ) / max(vals["technical_risk"] * vals["business_risk"], 1.0)
        row["raw_score"] = f"{raw:.6f}"
        raw_scores.append(raw)

    lo, hi = min(raw_scores), max(raw_scores)
    for row, raw in zip(rows, raw_scores):
        normalized = 100.0 if hi == lo else (raw - lo) / (hi - lo) * 100.0
        row["normalized_score"] = f"{normalized:.2f}"

    fieldnames = list(rows[0].keys())
    for required in ("raw_score", "normalized_score"):
        if required not in fieldnames:
            fieldnames.append(required)

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: float(r["normalized_score"]), reverse=True))

    print(f"Wrote {len(rows)} scored opportunities to {args.output_csv}")

if __name__ == "__main__":
    main()
