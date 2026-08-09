"""
Canonical nodes associated with symmetric signatures.

Proposition (preprint 3.1): for fixed digit length ``m``, the value
``T(N) = N + rev(N)`` depends only on ``Sigma_m(N)``. The common value is the
*canonical node* ``K_Sigma``.

Closed forms used in the preprint:

- ``K_3(x, b) = 101*x + 20*b``
- ``K_4(x, y) = 1001*x + 110*y``
- ``K_5(x, y, z) = 10001*x + 1010*y + 200*z``
"""

from __future__ import annotations

from .reverse_add import reverse_add
from .signatures import symmetric_signature


def canonical_node_3d(sig: tuple[int, int]) -> int:
    """Return ``K_3(x, b) = 101*x + 20*b`` for ``sig = (x, b)``."""
    if len(sig) != 2:
        raise ValueError("3D signature must be a pair (x, b)")
    x, b = sig
    return 101 * x + 20 * b


def canonical_node_4d(sig: tuple[int, int]) -> int:
    """Return ``K_4(x, y) = 1001*x + 110*y`` for ``sig = (x, y)``."""
    if len(sig) != 2:
        raise ValueError("4D signature must be a pair (x, y)")
    x, y = sig
    return 1001 * x + 110 * y


def canonical_node_5d(sig: tuple[int, int, int]) -> int:
    """Return ``K_5(x, y, z) = 10001*x + 1010*y + 200*z``."""
    if len(sig) != 3:
        raise ValueError("5D signature must be a triple (x, y, z)")
    x, y, z = sig
    return 10001 * x + 1010 * y + 200 * z


def canonical_node_from_number(n: int, width: int | None = None) -> int:
    """Return the canonical node of ``n`` via the closed-form for its width.

    Equivalent to ``reverse_add(n)`` for any ``m``-digit ``n``, by the
    signature principle.
    """
    from .signatures import digits

    digs = digits(n)
    m = width if width is not None else len(digs)
    if width is not None and len(digs) != width:
        raise ValueError(f"expected a {width}-digit number, got {n}")

    sig = symmetric_signature(n, width=m)
    if m == 3:
        return canonical_node_3d((sig[0], sig[1]))
    if m == 4:
        return canonical_node_4d((sig[0], sig[1]))
    if m == 5:
        return canonical_node_5d((sig[0], sig[1], sig[2]))
    # General fallback: T(n) itself (always valid; closed form not specialized).
    return reverse_add(n)


def verify_canonical_node_formula(n: int, width: int | None = None) -> bool:
    """Return True if the closed-form node equals ``T(n)`` for width 3, 4, or 5."""
    from .signatures import digits

    digs = digits(n)
    m = width if width is not None else len(digs)
    if m not in (3, 4, 5):
        raise ValueError("formula verification is implemented only for widths 3, 4, 5")
    return canonical_node_from_number(n, width=m) == reverse_add(n)
