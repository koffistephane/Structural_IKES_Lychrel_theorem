"""
Enumeration and signature-level classification of experimental candidates.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from .canonical_nodes import canonical_node_from_number
from .carries import carry_profile_string
from .reverse_add import is_experimental_candidate
from .signatures import symmetric_signature


def enumerate_candidates(
    start: int,
    stop: int,
    max_iter: int = 500,
    test_after_first_step: bool = True,
) -> list[int]:
    """Return experimental candidates ``n`` with ``start <= n < stop``.

    Uses the finite protocol of ``is_experimental_candidate``.
    """
    out: list[int] = []
    for n in range(start, stop):
        if is_experimental_candidate(
            n,
            max_iter=max_iter,
            test_after_first_step=test_after_first_step,
        ):
            out.append(n)
    return out


def group_by_signature(
    numbers: list[int],
    width: int,
) -> dict[tuple[int, ...], list[int]]:
    """Group integers by ``Sigma_width``."""
    groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for n in numbers:
        groups[symmetric_signature(n, width=width)].append(n)
    return dict(groups)


def count_numbers_with_signature(sig: tuple[int, ...], width: int) -> int:
    """Count all ``width``-digit integers realizing ``sig`` (leading digit ≠ 0)."""
    start = 10 ** (width - 1)
    stop = 10 ** width
    count = 0
    for n in range(start, stop):
        if symmetric_signature(n, width=width) == sig:
            count += 1
    return count


def _signature_population_counts(width: int) -> dict[tuple[int, ...], int]:
    """Single-pass histogram of all signatures among ``width``-digit integers."""
    start = 10 ** (width - 1)
    stop = 10 ** width
    counts: dict[tuple[int, ...], int] = defaultdict(int)
    for n in range(start, stop):
        counts[symmetric_signature(n, width=width)] += 1
    return dict(counts)


def signature_statistics(
    start: int,
    stop: int,
    width: int,
    max_iter: int = 500,
    test_after_first_step: bool = True,
) -> list[dict[str, Any]]:
    """Compute per-signature statistics for experimental candidates in range.

    Each record contains:

    - ``signature``
    - ``candidates`` (sorted list)
    - ``candidate_count``
    - ``total_with_signature`` (all width-digit numbers with that signature)
    - ``is_pure`` (True iff every width-digit realization is a candidate)
    - ``canonical_node``
    - ``R0`` (carry-profile string of the least candidate)
    """
    candidates = enumerate_candidates(
        start,
        stop,
        max_iter=max_iter,
        test_after_first_step=test_after_first_step,
    )
    groups = group_by_signature(candidates, width=width)
    population = _signature_population_counts(width)
    rows: list[dict[str, Any]] = []
    for sig, nums in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        nums_sorted = sorted(nums)
        total = population.get(sig, 0)
        node = canonical_node_from_number(nums_sorted[0], width=width)
        rows.append(
            {
                "signature": sig,
                "candidates": nums_sorted,
                "candidate_count": len(nums_sorted),
                "total_with_signature": total,
                "is_pure": len(nums_sorted) == total,
                "canonical_node": node,
                "R0": carry_profile_string(nums_sorted[0], width=width),
            }
        )
    return rows


def export_signature_table(
    rows: list[dict[str, Any]],
    path: str | Path,
    include_candidate_list: bool = True,
) -> Path:
    """Write signature statistics to CSV."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "signature",
        "candidate_count",
        "total_with_signature",
        "is_pure",
        "canonical_node",
        "R0",
    ]
    if include_candidate_list:
        fieldnames.append("candidates")

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            out = {
                "signature": " ".join(map(str, row["signature"])),
                "candidate_count": row["candidate_count"],
                "total_with_signature": row["total_with_signature"],
                "is_pure": row["is_pure"],
                "canonical_node": row["canonical_node"],
                "R0": row["R0"],
            }
            if include_candidate_list:
                out["candidates"] = " ".join(map(str, row["candidates"]))
            writer.writerow(out)
    return path


def export_candidate_list(numbers: Iterable[int], path: str | Path) -> Path:
    """Write a one-column CSV of candidate integers."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["n"])
        for n in numbers:
            writer.writerow([n])
    return path
