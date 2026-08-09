"""
lychrel_signature
=================

Structural classification tools for *experimental* Lychrel candidates
under a finite reverse-and-add protocol.

This package does **not** claim to prove the existence of base-10 Lychrel
numbers. All candidate classifications are relative to a finite iteration
bound (default ``max_iter=500``).
"""

from .reverse_add import (
    first_palindrome_time,
    is_experimental_candidate,
    is_palindrome,
    orbit,
    reverse_add,
    reverse_digits,
)
from .signatures import (
    digits,
    projection_5d_to_4d,
    signature_3d,
    signature_4d,
    signature_5d,
    symmetric_signature,
)
from .canonical_nodes import (
    canonical_node_3d,
    canonical_node_4d,
    canonical_node_5d,
    canonical_node_from_number,
    verify_canonical_node_formula,
)

__all__ = [
    "reverse_digits",
    "reverse_add",
    "is_palindrome",
    "orbit",
    "first_palindrome_time",
    "is_experimental_candidate",
    "digits",
    "symmetric_signature",
    "signature_3d",
    "signature_4d",
    "signature_5d",
    "projection_5d_to_4d",
    "canonical_node_from_number",
    "canonical_node_3d",
    "canonical_node_4d",
    "canonical_node_5d",
    "verify_canonical_node_formula",
]

__version__ = "0.1.0"
