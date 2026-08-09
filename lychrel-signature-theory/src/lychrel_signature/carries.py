"""
Carry vectors for one reverse-and-add step.

When adding ``n`` and ``rev(n)`` digit-wise from right to left, each position
produces a carry in ``{0, 1}`` (or rarely larger if an incoming carry is
already present; for base-10 digit pairs the outgoing carry is in ``{0, 1}``
before the final overflow digit).

Notation in the preprint
------------------------
``R_0`` denotes the carry-out string of the *first* reverse-and-add step,
written most-significant position first as a bit string (e.g. ``010``,
``111``, ``0110``).

The preprint does not fully axiomatize higher ``R_k``; this module implements
the first-step carry vector used in the published tables.
"""

from __future__ import annotations

from .signatures import digits


def carry_vector(n: int, width: int | None = None) -> tuple[int, ...]:
    """Return carry-outs from each digit position of ``n + rev(n)``.

    Ordering convention (preprint tables, inferred from 3D–5D strings):
    index ``0`` is the units place, then tens, hundreds, ... (LSD-first).
    Example: ``196`` yields ``(0, 1, 0)`` → string ``010``.

    The length-``m`` vector stores the carry *out of* each of the ``m``
    base positions. An overflow digit, if any, is exactly the carry out of
    the most-significant entry.
    """
    digs = digits(n)
    m = width if width is not None else len(digs)
    if width is not None:
        if len(digs) > m:
            raise ValueError(f"n={n} has more than {m} digits")
        digs = [0] * (m - len(digs)) + digs

    carry_outs_lsd_first: list[int] = []
    carry = 0
    for i in range(m):
        left = digs[m - 1 - i]  # digit of n at position i from the right
        right = digs[i]  # digit of rev(n) at the same position
        total = left + right + carry
        carry = total // 10
        carry_outs_lsd_first.append(carry)
    return tuple(carry_outs_lsd_first)


def carry_profile_string(n: int, width: int | None = None) -> str:
    """Return the preprint-style LSD-first carry string, e.g. ``010``, ``01111``."""
    return "".join(str(c) for c in carry_vector(n, width=width))


def classify_carry_profile(profile: tuple[int, ...]) -> str:
    """Classify a carry profile into a coarse regime label.

    Labels are descriptive only (not a theorem):

    - ``zero``: all carries zero
    - ``alternating``: strict 0101... or 1010... pattern
    - ``saturated``: all carries positive
    - ``mixed``: otherwise
    """
    if not profile:
        return "empty"
    if all(c == 0 for c in profile):
        return "zero"
    if all(c > 0 for c in profile):
        return "saturated"
    alt01 = all(profile[i] == (i % 2) for i in range(len(profile)))
    alt10 = all(profile[i] == ((i + 1) % 2) for i in range(len(profile)))
    if alt01 or alt10:
        return "alternating"
    return "mixed"
