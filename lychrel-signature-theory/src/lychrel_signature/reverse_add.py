"""
Reverse-and-add map and experimental-candidate protocol.

Protocol convention
-------------------
By default ``is_experimental_candidate`` uses
``test_after_first_step=True``:

1. Apply ``T`` once (the seed itself is never tested for being a palindrome).
2. After each subsequent application of ``T``, test whether the value is a
   palindrome.
3. If no palindrome appears within ``max_iter`` applications of ``T``, the
   integer is an *experimental candidate*.

This convention is required for consistency with the preprint tables: the
palindromic seed ``9999`` is retained as a four-digit experimental candidate
(and as a dynamic-family representative) because its post-``T`` orbit does not
hit a palindrome within the finite bound.

None of these notions proves infinite non-palindromicity.
"""

from __future__ import annotations


def reverse_digits(n: int) -> int:
    """Return the integer obtained by reversing the decimal digits of ``n``.

    Trailing zeros of ``n`` become leading zeros of the reverse and are
    therefore dropped (e.g. ``reverse_digits(100) == 1``).
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return int(str(n)[::-1])


def reverse_add(n: int) -> int:
    """Apply the reverse-and-add map ``T(n) = n + rev(n)``."""
    return n + reverse_digits(n)


def is_palindrome(n: int) -> bool:
    """Return True if the decimal representation of ``n`` is a palindrome."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    s = str(n)
    return s == s[::-1]


def orbit(n: int, steps: int) -> list[int]:
    """Return ``[n, T(n), ..., T^steps(n)]`` (length ``steps + 1``)."""
    if steps < 0:
        raise ValueError("steps must be non-negative")
    seq = [n]
    x = n
    for _ in range(steps):
        x = reverse_add(x)
        seq.append(x)
    return seq


def first_palindrome_time(n: int, max_iter: int) -> int | None:
    """Return the least ``k`` in ``1..max_iter`` with ``T^k(n)`` a palindrome.

    The seed ``n`` itself is never tested. Returns ``None`` if no palindrome
    appears within ``max_iter`` applications of ``T``.
    """
    if max_iter < 1:
        raise ValueError("max_iter must be >= 1")
    x = n
    for k in range(1, max_iter + 1):
        x = reverse_add(x)
        if is_palindrome(x):
            return k
    return None


def is_experimental_candidate(
    n: int,
    max_iter: int = 500,
    test_after_first_step: bool = True,
) -> bool:
    """Return True if ``n`` is an experimental candidate under the protocol.

    Parameters
    ----------
    n:
        Non-negative integer seed.
    max_iter:
        Maximum number of applications of ``T`` examined after the protocol
        start (default ``500``, matching the preprint).
    test_after_first_step:
        If True (default), skip testing whether ``n`` itself is a palindrome
        and begin checking only after the first application of ``T``.
        If False, a palindromic seed is immediately rejected as a candidate.

    Notes
    -----
    This is a *finite* experimental predicate. It does not prove that the
    infinite orbit avoids palindromes.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if max_iter < 1:
        raise ValueError("max_iter must be >= 1")

    if not test_after_first_step and is_palindrome(n):
        return False

    x = n
    for _ in range(max_iter):
        x = reverse_add(x)
        if is_palindrome(x):
            return False
    return True
