#!/usr/bin/env python3
"""Print a compact console summary of available results/*.json files."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def main() -> None:
    if not RESULTS.exists():
        print("No results/ directory found. Run the run_*digits.py scripts first.")
        sys.exit(1)
    files = sorted(RESULTS.glob("summary_*.json"))
    if not files:
        print("No summary_*.json files found.")
        sys.exit(1)
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        print(f"== {path.name} ==")
        for key in (
            "width",
            "max_iter",
            "candidate_count",
            "signature_count",
            "all_pure",
            "observed_component_count_exploratory",
        ):
            if key in data:
                print(f"  {key}: {data[key]}")
        print()


if __name__ == "__main__":
    main()
