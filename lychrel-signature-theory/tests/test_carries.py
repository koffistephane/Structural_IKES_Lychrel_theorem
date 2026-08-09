"""Tests for carry vectors."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lychrel_signature.carries import (
    carry_profile_string,
    carry_vector,
    classify_carry_profile,
)


def test_carry_196_is_010():
    assert carry_profile_string(196) == "010"
    assert carry_vector(196) == (0, 1, 0)


def test_carry_689_is_111():
    assert carry_profile_string(689) == "111"


def test_carry_879_is_111():
    assert carry_profile_string(879) == "111"


def test_classify_carry_profile():
    assert classify_carry_profile((0, 0, 0)) == "zero"
    assert classify_carry_profile((1, 1, 1)) == "saturated"
    assert classify_carry_profile((0, 1, 0)) == "alternating"
    assert classify_carry_profile((1, 0, 1, 1)) == "mixed"
