"""Tests for canonical-node formulas."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lychrel_signature.canonical_nodes import (
    canonical_node_3d,
    canonical_node_4d,
    canonical_node_5d,
    canonical_node_from_number,
    verify_canonical_node_formula,
)
from lychrel_signature.reverse_add import reverse_add


def test_canonical_node_3d_formula():
    assert canonical_node_3d((7, 9)) == reverse_add(196) == 887


def test_canonical_node_4d_known_examples():
    assert canonical_node_4d((6, 13)) == 7436
    assert canonical_node_4d((8, 13)) == 9438
    assert canonical_node_4d((18, 18)) == 19998


def test_canonical_node_5d_known_example():
    assert canonical_node_5d((9, 8, 7)) == 99489


def test_formula_matches_t_for_all_3_digit():
    for n in range(100, 1000):
        assert verify_canonical_node_formula(n, width=3)
        assert canonical_node_from_number(n, width=3) == reverse_add(n)


def test_formula_matches_t_for_all_4_digit():
    for n in range(1000, 10000):
        assert verify_canonical_node_formula(n, width=4)


def test_formula_matches_t_sample_5_digit():
    for n in range(10000, 10100):
        assert verify_canonical_node_formula(n, width=5)
    assert verify_canonical_node_formula(99489, width=5)
