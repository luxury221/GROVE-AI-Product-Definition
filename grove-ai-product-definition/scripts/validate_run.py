#!/usr/bin/env python3
"""Validate the minimum GROVE-AI run directory and CSV headers."""

from __future__ import annotations
import argparse
import csv
from pathlib import Path

REQUIRED_FILES = [
    "run_manifest.yaml",
    "02_evidence/evidence_ledger.csv",
    "03_market/product_benchmark.csv",
    "03_market/review_coding.csv",
    "04_jobs/opportunity_scores.csv",
    "07_backtest/predictions.csv",
    "07_backtest/observations.csv",
]

REQUIRED_COLUMNS = {
    "02_evidence/evidence_ledger.csv": {"evidence_id","claim_id","source_type","summary","statement_type","historical_eligible"},
    "03_market/product_benchmark.csv": {"product_id","brand","model","capacity_mah","max_wireless_w","weight_g"},
    "03_market/review_coding.csv": {"feedback_id","product_id","source_id","context_code","pain_code"},
    "04_jobs/opportunity_scores.csv": {"opportunity_id","opportunity_statement","importance","dissatisfaction","frequency","evidence_confidence","strategic_fit","technical_risk","business_risk"},
    "07_backtest/predictions.csv": {"case_id","predicted_pains_topk","predicted_tradeoffs","leakage_flag"},
    "07_backtest/observations.csv": {"case_id","observed_pains_topk","observed_tradeoffs"},
}

def headers(path: Path) -> set[str]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        try:
            return set(next(reader))
        except StopIteration:
            return set()

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    for rel in REQUIRED_FILES:
        path = args.run_dir / rel
        if not path.exists():
            errors.append(f"Missing file: {rel}")
            continue
        if rel.endswith(".csv"):
            missing = REQUIRED_COLUMNS.get(rel, set()) - headers(path)
            if missing:
                errors.append(f"{rel}: missing columns {sorted(missing)}")

    if errors:
        print("Validation failed:")
        for item in errors:
            print(f"- {item}")
        raise SystemExit(1)

    print("Validation passed: required files and headers are present.")

if __name__ == "__main__":
    main()
