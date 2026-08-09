# Reproducibility

## Environment

- Python ≥ 3.10
- `pytest` for tests
- No mandatory scientific stack (NumPy/SciPy not required)

## Determinism

All enumerations are deterministic loops over integer ranges. There is no randomness.

## Commands

```bash
python -m pip install -e ".[dev]"
python scripts/run_3digits.py
python scripts/run_4digits.py
python scripts/run_5digits.py --skip-components
pytest
```

## Bound disclosure

Every exported CSV/JSON records or implies `max_iter=500` unless overridden by CLI flags. Publications must state:

> Enumeration bound \(B=500\), protocol `test_after_first_step=True`.

## What is and is not reproducible as a theorem

| Claim | Status |
|-------|--------|
| \(\Sigma_m \mapsto K_\Sigma\) closed forms for \(m=3,4,5\) | Algebraic identity (proven by digit pairing) |
| 13 three-digit candidates / 3 signatures at \(B=500\) | Finite exhaustive computation |
| 236 / 12 / 5 four-digit compression at \(B=500\) | Finite exhaustive computation |
| 5842 / 248 five-digit counts at \(B=500\) | Finite exhaustive computation |
| “≈86 components” in 5D | Exploratory; depends on merge window |
| Recursive signature grammar for all \(m\) | Conjecture |

## Artifact layout

```
results/
  candidates_3d.csv
  signatures_3d.csv
  summary_3d.json
  ...
```
