"""Tests for reverse-and-add primitives."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lychrel_signature.reverse_add import (
    first_palindrome_time,
    is_experimental_candidate,
    is_palindrome,
    orbit,
    reverse_add,
    reverse_digits,
)


def test_reverse_digits_basic():
    assert reverse_digits(196) == 691
    assert reverse_digits(100) == 1
    assert reverse_digits(1234) == 4321


def test_reverse_add_196():
    assert reverse_add(196) == 887


def test_is_palindrome():
    assert is_palindrome(121)
    assert is_palindrome(9999)
    assert not is_palindrome(196)


def test_orbit_length():
    seq = orbit(196, 3)
    assert len(seq) == 4
    assert seq[0] == 196
    assert seq[1] == reverse_add(196)


def test_first_palindrome_time_known():
    # 89 is famous for a long but finite path; with small bound may be None.
    assert first_palindrome_time(23, 20) is not None
    assert first_palindrome_time(196, 10) is None


def test_9999_is_candidate_under_default_protocol():
    """Palindromic seeds are allowed when testing starts after the first T."""
    assert is_experimental_candidate(9999, max_iter=500, test_after_first_step=True)
    assert not is_experimental_candidate(9999, max_iter=500, test_after_first_step=False)


def test_196_is_candidate():
    assert is_experimental_candidate(196, max_iter=500)
