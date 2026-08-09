#!/usr/bin/env python3
"""Enumerate four-digit experimental candidates and classify dynamic families."""

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
from lychrel_signature.families import (  # noqa: E402
    DEFAULT_4D_FAMILY_SEEDS,
    classify_signature_family,
)
from lychrel_signature.io_utils import results_dir, write_json  # noqa: E402


def main() -> None:
    max_iter = 500
    start, stop, width = 1000, 10000, 4
    candidates = enumerate_candidates(start, stop, max_iter=max_iter)
    rows = signature_statistics(start, stop, width, max_iter=max_iter)

    family_counts: dict[int, int] = {g: 0 for g in DEFAULT_4D_FAMILY_SEEDS}
    enriched = []
    for r in rows:
        fam = classify_signature_family(
            r["signature"],
            width=width,
            seeds=DEFAULT_4D_FAMILY_SEEDS,
            max_follow=max_iter,
        )
        family_seed = fam["family_seed"] if fam else None
        if family_seed is not None:
            family_counts[family_seed] = family_counts.get(family_seed, 0) + r[
                "candidate_count"
            ]
        enriched.append(
            {
                **{k: v for k, v in r.items() if k != "candidates"},
                "candidates": r["candidates"],
                "family_seed": family_seed,
                "join_value": None if fam is None else fam["join_value"],
            }
        )

    out = results_dir()
    export_candidate_list(candidates, out / "candidates_4d.csv")
    export_signature_table(rows, out / "signatures_4d.csv")
    write_json(
        {
            "width": width,
            "max_iter": max_iter,
            "test_after_first_step": True,
            "candidate_count": len(candidates),
            "signature_count": len(rows),
            "all_pure": all(r["is_pure"] for r in rows),
            "family_candidate_counts": {str(k): v for k, v in family_counts.items()},
            "signatures": [
                {
                    "signature": list(r["signature"]),
                    "candidate_count": r["candidate_count"],
                    "canonical_node": r["canonical_node"],
                    "R0": r["R0"],
                    "is_pure": r["is_pure"],
                    "family_seed": e["family_seed"],
                }
                for r, e in zip(rows, enriched)
            ],
        },
        out / "summary_4d.json",
    )
    print(f"4D candidates: {len(candidates)}")
    print(f"4D signatures: {len(rows)}")
    print(f"all pure: {all(r['is_pure'] for r in rows)}")
    print("family counts (by candidate membership of signatures):")
    for g, c in family_counts.items():
        print(f"  {g}: {c}")


if __name__ == "__main__":
    main()
