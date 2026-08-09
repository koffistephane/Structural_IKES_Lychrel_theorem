"""
Symmetric signatures for fixed digit length.

For an ``m``-digit integer ``N = d_1 d_2 ... d_m`` (most-significant digit
first), the symmetric signature is

    Sigma_m(N) = (d_1 + d_m, d_2 + d_{m-1}, ..., )
                with the unpaired central digit kept when ``m`` is odd.

Examples
--------
- 3 digits: Sigma_3(abc) = (a+c, b)
- 4 digits: Sigma_4(abcd) = (a+d, b+c)
- 5 digits: Sigma_5(abcde) = (a+e, b+d, c)
"""

from __future__ import annotations


def digits(n: int) -> list[int]:
    """Return decimal digits of ``n`` as a list (most-significant first)."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return [int(ch) for ch in str(n)]


def _require_width(n: int, width: int) -> list[int]:
    digs = digits(n)
    if len(digs) != width:
        raise ValueError(f"expected a {width}-digit number, got {n}")
    return digs


def symmetric_signature(n: int, width: int | None = None) -> tuple[int, ...]:
    """Return the symmetric signature of ``n``.

    If ``width`` is given, ``n`` must have exactly that many digits.
    Otherwise the natural digit length of ``n`` is used.
    """
    digs = digits(n)
    m = width if width is not None else len(digs)
    if width is not None and len(digs) != width:
        raise ValueError(f"expected a {width}-digit number, got {n}")
    half = m // 2
    pairs = tuple(digs[i] + digs[m - 1 - i] for i in range(half))
    if m % 2 == 1:
        return pairs + (digs[half],)
    return pairs


def signature_3d(n: int) -> tuple[int, int]:
    """Sigma_3 for a three-digit integer."""
    sig = symmetric_signature(n, width=3)
    return (sig[0], sig[1])


def signature_4d(n: int) -> tuple[int, int]:
    """Sigma_4 for a four-digit integer."""
    sig = symmetric_signature(n, width=4)
    return (sig[0], sig[1])


def signature_5d(n: int) -> tuple[int, int, int]:
    """Sigma_5 for a five-digit integer."""
    sig = symmetric_signature(n, width=5)
    return (sig[0], sig[1], sig[2])


def projection_5d_to_4d(sig5: tuple[int, int, int]) -> tuple[int, int]:
    """Project a 5D signature ``(x, y, z)`` to the outer pair ``(x, y)``.

    This drops the center digit, matching the preprint heuristic
    ``5D = 4D + center + bifurcation``.
    """
    if len(sig5) != 3:
        raise ValueError("sig5 must be a length-3 signature")
    return (sig5[0], sig5[1])
