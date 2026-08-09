#!/usr/bin/env python3
"""Enumerate three-digit experimental candidates (max_iter=500)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from lychrel_signature.classification import (  # noqa: E402
    enumerate_candidates,
    export_candidate_list,
    export_signature_table,
    signature_statistics,
)
from lychrel_signature.io_utils import results_dir, write_json  # noqa: E402


def main() -> None:
    max_iter = 500
    start, stop, width = 100, 1000, 3
    candidates = enumerate_candidates(start, stop, max_iter=max_iter)
    rows = signature_statistics(start, stop, width, max_iter=max_iter)
    out = results_dir()
    export_candidate_list(candidates, out / "candidates_3d.csv")
    export_signature_table(rows, out / "signatures_3d.csv")
    summary = {
        "width": width,
        "max_iter": max_iter,
        "test_after_first_step": True,
        "candidate_count": len(candidates),
        "signature_count": len(rows),
        "signatures": {
            " ".join(map(str, r["signature"])): r["candidate_count"] for r in rows
        },
        "all_pure": all(r["is_pure"] for r in rows),
    }
    write_json(summary, out / "summary_3d.json")
    print(f"3D candidates: {len(candidates)}")
    print(f"3D signatures: {len(rows)}")
    for r in rows:
        print(f"  {r['signature']}: {r['candidate_count']} (pure={r['is_pure']})")


if __name__ == "__main__":
    main()
