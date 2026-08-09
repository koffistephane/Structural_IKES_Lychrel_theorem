# Methodology

## Finite protocol

Fix an iteration bound \(B\) (default \(B = 500\)).

With `test_after_first_step=True` (repository default and preprint convention):

1. Set \(x_0 = n\).
2. For \(k = 1,\ldots,B\): set \(x_k = T(x_{k-1})\). If \(x_k\) is a palindrome, stop and classify \(n\) as **not** an experimental candidate.
3. If no palindrome appears, classify \(n\) as an **experimental candidate** at bound \(B\).

The seed \(n\) itself is never tested. Consequently a palindrome such as \(9999\) may still be a candidate if its post-\(T\) orbit avoids palindromes for \(B\) steps.

## Signature compression

1. Enumerate all \(m\)-digit experimental candidates.
2. Group by \(\Sigma_m\).
3. Attach the canonical node \(K_\Sigma = T(N)\) (independent of the representative).
4. Optionally classify nodes by joining known seed orbits within a follow window.

## Purity

A candidate signature is **pure** (at bound \(B\)) if every \(m\)-digit integer realizing that signature is an experimental candidate.

## Families and components

Family membership and component counts are **window-dependent**. The four-digit family table uses seeds

\[
\{196, 879, 1997, 7059, 9999\}
\]

and a follow window of length \(B\). Five-digit component counts produced by `partition_nodes_into_components` are exploratory and must be reported with the follow parameter.
