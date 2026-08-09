#!/usr/bin/env python3
"""Re-export CSV tables from existing summary runs if present; else run 3D/4D."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    scripts = [
        ROOT / "scripts" / "run_3digits.py",
        ROOT / "scripts" / "run_4digits.py",
    ]
    for script in scripts:
        print(f"Running {script.name} ...")
        subprocess.check_call([sys.executable, str(script)], cwd=str(ROOT))
    print("CSV tables written under results/.")
    print("For five-digit tables, run: python scripts/run_5digits.py")


if __name__ == "__main__":
    main()
