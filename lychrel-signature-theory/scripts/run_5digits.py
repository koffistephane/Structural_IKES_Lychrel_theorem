#!/usr/bin/env python3
"""Enumerate five-digit experimental candidates (exploratory component count)."""

from __future__ import annotations

import argparse
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
from lychrel_signature.families import partition_nodes_into_components  # noqa: E402
from lychrel_signature.io_utils import results_dir, write_json  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-iter", type=int, default=500)
    parser.add_argument(
        "--component-follow",
        type=int,
        default=100,
        help="orbit window for exploratory component partition (default 100)",
    )
    parser.add_argument(
        "--skip-components",
        action="store_true",
        help="skip the expensive exploratory component partition",
    )
    args = parser.parse_args()

    start, stop, width = 10000, 100000, 5
    print(f"Enumerating 5D candidates with max_iter={args.max_iter} ...")
    candidates = enumerate_candidates(start, stop, max_iter=args.max_iter)
    print(f"Computing signature statistics ({len(candidates)} candidates) ...")
    rows = signature_statistics(start, stop, width, max_iter=args.max_iter)

    component_count = None
    if not args.skip_components:
        nodes = [r["canonical_node"] for r in rows]
        print(
            f"Partitioning {len(nodes)} nodes with follow={args.component_follow} ..."
        )
        comps = partition_nodes_into_components(nodes, max_follow=args.component_follow)
        component_count = len(comps)
        print(f"Observed components (exploratory): {component_count}")

    out = results_dir()
    export_candidate_list(candidates, out / "candidates_5d.csv")
    export_signature_table(rows, out / "signatures_5d.csv", include_candidate_list=False)
    write_json(
        {
            "width": width,
            "max_iter": args.max_iter,
            "test_after_first_step": True,
            "candidate_count": len(candidates),
            "signature_count": len(rows),
            "observed_component_count_exploratory": component_count,
            "component_follow": None if args.skip_components else args.component_follow,
            "top_signatures": [
                {
                    "signature": list(r["signature"]),
                    "candidate_count": r["candidate_count"],
                    "canonical_node": r["canonical_node"],
                    "R0": r["R0"],
                }
                for r in rows[:12]
            ],
        },
        out / "summary_5d.json",
    )
    print(f"5D candidates: {len(candidates)}")
    print(f"5D signatures: {len(rows)}")


if __name__ == "__main__":
    main()
