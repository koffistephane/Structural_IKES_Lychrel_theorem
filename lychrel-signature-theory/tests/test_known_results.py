"""
Regression tests for the empirical claims of the preprint (max_iter=500).

Three-digit and four-digit enumerations are fast enough for default CI.
Five-digit full enumeration is marked as slow and skipped unless
explicitly requested via RUN_SLOW=1.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lychrel_signature.canonical_nodes import canonical_node_4d, canonical_node_5d
from lychrel_signature.classification import (
    enumerate_candidates,
    group_by_signature,
    signature_statistics,
)
from lychrel_signature.families import DEFAULT_4D_FAMILY_SEEDS, classify_signature_family
from lychrel_signature.signatures import signature_3d


MAX_ITER = 500


def test_three_digit_candidate_count_and_signatures():
    candidates = enumerate_candidates(100, 1000, max_iter=MAX_ITER)
    assert len(candidates) == 13
    groups = group_by_signature(candidates, width=3)
    assert set(groups) == {(7, 9), (15, 8), (17, 7)}
    assert len(groups[(7, 9)]) == 7
    assert len(groups[(15, 8)]) == 4
    assert len(groups[(17, 7)]) == 2
    assert sorted(groups[(7, 9)]) == [196, 295, 394, 493, 592, 691, 790]
    assert sorted(groups[(15, 8)]) == [689, 788, 887, 986]
    assert sorted(groups[(17, 7)]) == [879, 978]
    for n in candidates:
        assert signature_3d(n) in {(7, 9), (15, 8), (17, 7)}


def test_four_digit_compression():
    candidates = enumerate_candidates(1000, 10000, max_iter=MAX_ITER)
    assert len(candidates) == 236
    rows = signature_statistics(1000, 10000, width=4, max_iter=MAX_ITER)
    assert len(rows) == 12
    assert all(r["is_pure"] for r in rows)

    assert canonical_node_4d((6, 13)) == 7436
    assert canonical_node_4d((8, 13)) == 9438
    assert canonical_node_4d((18, 18)) == 19998

    family_counts = {g: 0 for g in DEFAULT_4D_FAMILY_SEEDS}
    for r in rows:
        fam = classify_signature_family(
            r["signature"],
            width=4,
            seeds=DEFAULT_4D_FAMILY_SEEDS,
            max_follow=MAX_ITER,
        )
        assert fam is not None, f"unclassified signature {r['signature']}"
        family_counts[fam["family_seed"]] += r["candidate_count"]

    assert family_counts[196] == 102
    assert family_counts[879] == 70
    assert family_counts[1997] == 30
    assert family_counts[7059] == 33
    assert family_counts[9999] == 1
    assert sum(family_counts.values()) == 236


def test_five_digit_canonical_examples():
    assert canonical_node_5d((9, 8, 7)) == 99489


@pytest.mark.skipif(
    os.environ.get("RUN_SLOW") != "1",
    reason="5D full enumeration is slow; set RUN_SLOW=1 to enable",
)
def test_five_digit_candidate_and_signature_counts():
    candidates = enumerate_candidates(10000, 100000, max_iter=MAX_ITER)
    assert len(candidates) == 5842
    groups = group_by_signature(candidates, width=5)
    assert len(groups) == 248
