"""Tests for symmetric signatures."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lychrel_signature.signatures import (
    digits,
    projection_5d_to_4d,
    signature_3d,
    signature_4d,
    signature_5d,
    symmetric_signature,
)


def test_digits():
    assert digits(196) == [1, 9, 6]


def test_signature_3d_examples():
    assert signature_3d(196) == (7, 9)
    assert signature_3d(689) == (15, 8)
    assert signature_3d(879) == (17, 7)


def test_signature_4d_examples():
    assert signature_4d(8791) == signature_4d(8791)
    assert symmetric_signature(7436, width=4)  # smoke
    # 8791: 8+1=9, 7+9=16
    assert signature_4d(8791) == (9, 16)


def test_signature_5d_example():
    # Number with Sigma_5 = (9, 8, 7): digits a,b,7,d,e with a+e=9, b+d=8.
    assert signature_5d(10788) == (9, 8, 7)
    # Canonical node of that signature is not itself a (9,8,7)-number:
    assert signature_5d(99489) == (18, 17, 4)


def test_projection_5d_to_4d():
    assert projection_5d_to_4d((9, 8, 7)) == (9, 8)
