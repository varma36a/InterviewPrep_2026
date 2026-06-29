"""Optional: import DSA problems from a public Google Sheet CSV export.

To use your sheet:
1. Google Sheets -> File -> Share -> Anyone with the link (Viewer)
2. File -> Download -> Comma Separated Values (.csv) for the target tab
3. Save as data/dsa_sheet.csv OR set DSA_SHEET_CSV env var to the file path
4. Expected columns (flexible headers): Topic, Problem, Difficulty, Pattern,
   Time Complexity, Space Complexity, LeetCode #, Notes

Until a CSV is provided, the app uses the built-in 50-problem catalog with
detailed complexity from data/dsa_complexity.py.
"""

from __future__ import annotations

import csv
from pathlib import Path

_APP_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = _APP_ROOT / "data" / "dsa_sheet.csv"


def load_sheet_csv(path: Path | None = None) -> list[dict[str, str]]:
    """Load rows from a downloaded sheet CSV if the file exists."""
    csv_path = path or DEFAULT_CSV
    if not csv_path.is_file():
        return []
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))
