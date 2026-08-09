# lychrel-signature-theory

Structural classification of **experimental** Lychrel candidates in base 10 via symmetric signatures and canonical nodes.

## Scope (read this first)

This project studies **experimental Lychrel candidates** under a **finite** reverse-and-add protocol (`max_iter = 500` by default).

It does **not** prove the existence of true base-10 Lychrel numbers. A number that survives 500 iterations may still become a palindrome later. Any statement about “candidates” in this repository is relative to the stated bound.

## Mathematical background

The reverse-and-add map is

\[
T(n) = n + \mathrm{rev}(n).
\]

An *experimental candidate* (bound \(B\)) is an integer whose iterates under \(T\) do not hit a palindrome within \(B\) applications of \(T\), under the protocol below.

### Protocol convention (important)

By default the code uses `test_after_first_step=True`:

1. Apply \(T\) once (the seed itself is **not** tested for being a palindrome).
2. After each of up to \(B\) applications of \(T\), test whether the current value is a palindrome.
3. If none appears, the seed is an experimental candidate.

This convention retains palindromic seeds such as `9999` when their post-\(T\) orbit does not hit a palindrome within the bound, matching the preprint tables.

## Definitions

| Symbol | Meaning |
|--------|---------|
| \(\Sigma_m(N)\) | Symmetric signature: paired digit sums (center kept if \(m\) odd) |
| \(K_\Sigma\) | Canonical node: common value \(T(N)\) for all \(N\) with signature \(\Sigma\) |
| \(R_0\) | Carry-out profile of the first reverse-and-add step |
| \(O(n)\) | Forward orbit of \(n\) under \(T\) |
| \(G\) | Designated seed / family representative |
| \(F(G)\) | Dynamic family: numbers whose orbits meet \(O(G)\) within a window |

Closed forms:

- \(K_3(x,b)=101x+20b\)
- \(K_4(x,y)=1001x+110y\)
- \(K_5(x,y,z)=10001x+1010y+200z\)

## Install

```bash
cd lychrel-signature-theory
python -m pip install -e ".[dev]"
```

Or with requirements only:

```bash
python -m pip install -r requirements.txt
```

## Reproduce results

Default iteration bound: **500**.

```bash
python scripts/run_3digits.py
python scripts/run_4digits.py
python scripts/run_5digits.py
pytest
```

Five-digit enumeration is slower. Component partitioning is exploratory and window-dependent:

```bash
python scripts/run_5digits.py --component-follow 100
# or skip components:
python scripts/run_5digits.py --skip-components
```

Slow five-digit regression test:

```bash
# Unix
RUN_SLOW=1 pytest tests/test_known_results.py -k five_digit
# Windows PowerShell
$env:RUN_SLOW=1; pytest tests/test_known_results.py -k five_digit
```

## Expected outputs

| Width | Candidates | Signatures | Notes |
|------:|-----------:|-----------:|-------|
| 3 | 13 | 3 | Exact: \(\{(7,9),(15,8),(17,7)\}\) |
| 4 | 236 | 12 | All pure; 5 observed families |
| 5 | 5842 | 248 | ~86 components (exploratory) |

Artifacts are written under `results/`:

- `candidates_{3,4,5}d.csv`
- `signatures_{3,4,5}d.csv`
- `summary_{3,4,5}d.json`

## Warning about finite bounds

Changing `max_iter` can change the candidate set. Results at bound 500 must not be quoted as proofs of infinite non-palindromicity. A genuine existence proof for a Lychrel number would require an invariant that forbids all future palindromes.

## Citation

```
IBOHN KOFFI E. Symmetric signatures and canonical nodes for the structural
classification of experimental Lychrel candidates. Preprint draft, 2026.
Software: lychrel-signature-theory (this repository).
```

## License

MIT License. See [LICENSE](LICENSE).

## Documentation

- [docs/methodology.md](docs/methodology.md)
- [docs/notation.md](docs/notation.md)
- [docs/reproducibility.md](docs/reproducibility.md)
- [docs/audit_report.md](docs/audit_report.md) — referee-style audit of the preprint drafts
