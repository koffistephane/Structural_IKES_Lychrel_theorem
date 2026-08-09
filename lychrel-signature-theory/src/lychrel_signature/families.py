"""
Dynamic families, basins, and coarse orbit-joining heuristics.

Definitions used here are *computational* and window-dependent. They are not
claims of infinite dynamical structure.

- A *seed* ``G`` is a designated experimental representative (e.g. 196).
- The *dynamic family* ``F(G)`` (within a follow window) consists of numbers
  whose forward orbit meets the forward orbit of ``G``.
- Observed *components* are equivalence classes of nodes that merge within a
  finite follow window.
"""

from __future__ import annotations

from typing import Any

from .canonical_nodes import canonical_node_from_number
from .reverse_add import reverse_add
from .signatures import symmetric_signature


def build_orbit_index(seed: int, steps: int) -> dict[int, int]:
    """Map each value in ``{seed, T(seed), ..., T^steps(seed)}`` to first time."""
    index: dict[int, int] = {}
    x = seed
    for t in range(steps + 1):
        if x not in index:
            index[x] = t
        x = reverse_add(x)
    return index


def classify_node_by_known_families(
    node: int,
    seeds: list[int],
    max_follow: int = 500,
) -> dict[str, Any] | None:
    """Follow ``node`` up to ``max_follow`` steps and detect a join with a seed orbit.

    Returns ``None`` if no join is detected within the window.
    """
    seed_indices = {g: build_orbit_index(g, max_follow) for g in seeds}
    x = node
    path: list[int] = [x]
    for step in range(max_follow + 1):
        for g in seeds:
            if x in seed_indices[g]:
                return {
                    "family_seed": g,
                    "join_value": x,
                    "join_step_from_node": step,
                    "join_step_on_seed_orbit": seed_indices[g][x],
                    "path_prefix": path[: min(len(path), 6)],
                }
        x = reverse_add(x)
        path.append(x)
    return None


def classify_signature_family(
    signature: tuple[int, ...],
    width: int,
    seeds: list[int],
    max_follow: int = 500,
) -> dict[str, Any] | None:
    """Classify a signature via its canonical node against known family seeds."""
    rep = _representative_from_signature(signature, width)
    node = canonical_node_from_number(rep, width=width)
    result = classify_node_by_known_families(node, seeds, max_follow=max_follow)
    if result is None:
        return None
    return {
        "signature": signature,
        "representative": rep,
        "canonical_node": node,
        **result,
    }


def _representative_from_signature(signature: tuple[int, ...], width: int) -> int:
    """Return one ``width``-digit integer realizing ``signature``."""
    start = 10 ** (width - 1)
    stop = 10 ** width
    for n in range(start, stop):
        if symmetric_signature(n, width=width) == signature:
            return n
    raise ValueError(f"no {width}-digit representative for signature {signature}")


DEFAULT_4D_FAMILY_SEEDS: list[int] = [196, 879, 1997, 7059, 9999]


def partition_nodes_into_components(
    nodes: list[int],
    max_follow: int = 200,
) -> list[list[int]]:
    """Partition nodes into observed components by pairwise orbit intersection.

    Exploratory only: quadratic in ``len(nodes)`` and window-dependent.
    """
    orbits = {n: set(build_orbit_index(n, max_follow)) for n in nodes}
    parent = {n: n for n in nodes}

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i, a in enumerate(nodes):
        for b in nodes[i + 1 :]:
            if orbits[a].intersection(orbits[b]):
                union(a, b)

    comps: dict[int, list[int]] = {}
    for n in nodes:
        comps.setdefault(find(n), []).append(n)
    return [sorted(v) for v in comps.values()]
