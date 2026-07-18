#!/usr/bin/env python3
"""Calculate simple GROVE-AI backtest metrics from predictions and observations CSVs."""

from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

def split_set(value: str | None) -> set[str]:
    if not value:
        return set()
    return {x.strip() for x in value.split(";") if x.strip()}

def recall(predicted: set[str], observed: set[str]) -> float | None:
    if not observed:
        return None
    return len(predicted & observed) / len(observed)

def precision(predicted: set[str], observed: set[str]) -> float | None:
    if not predicted:
        return None
    return len(predicted & observed) / len(predicted)

def mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None

def load(path: Path) -> dict[str, dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return {row["case_id"]: row for row in csv.DictReader(f)}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions_csv", type=Path)
    parser.add_argument("observations_csv", type=Path)
    parser.add_argument("output_json", type=Path)
    args = parser.parse_args()

    preds = load(args.predictions_csv)
    obs = load(args.observations_csv)
    case_ids = sorted(set(preds) & set(obs))
    if not case_ids:
        raise SystemExit("No shared case_id values.")

    pain_recalls: list[float] = []
    pain_precisions: list[float] = []
    tradeoff_recalls: list[float] = []
    leakage = 0
    details = []

    for case_id in case_ids:
        p, o = preds[case_id], obs[case_id]
        pp = split_set(p.get("predicted_pains_topk"))
        op = split_set(o.get("observed_pains_topk"))
        pt = split_set(p.get("predicted_tradeoffs"))
        ot = split_set(o.get("observed_tradeoffs"))

        pr = recall(pp, op)
        ppv = precision(pp, op)
        tr = recall(pt, ot)
        if pr is not None:
            pain_recalls.append(pr)
        if ppv is not None:
            pain_precisions.append(ppv)
        if tr is not None:
            tradeoff_recalls.append(tr)

        leak = str(p.get("leakage_flag", "")).strip().lower() in {"1","true","yes","y"}
        leakage += int(leak)
        details.append({
            "case_id": case_id,
            "pain_recall": pr,
            "pain_precision": ppv,
            "tradeoff_recall": tr,
            "leakage": leak,
        })

    result = {
        "cases": len(case_ids),
        "pain_recall_mean": mean(pain_recalls),
        "pain_precision_mean": mean(pain_precisions),
        "tradeoff_detection_mean": mean(tradeoff_recalls),
        "leakage_rate": leakage / len(case_ids),
        "details": details,
        "notes": [
            "These set-overlap metrics are diagnostic, not proof of market success.",
            "Add human coding reliability and source-quality audits for formal evaluation."
        ]
    }

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote metrics for {len(case_ids)} cases to {args.output_json}")

if __name__ == "__main__":
    main()
