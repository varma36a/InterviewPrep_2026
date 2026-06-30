"""Import DSA problems from ScalerRevision.xlsx (Love Babbar Final_450 sheet).

Source file: data/ScalerRevision.xlsx (sheet: Final_450)
Regenerate catalog: python scripts/build_dsa_450.py

The Excel lists 448 problems across 15 topics. Time/space complexity is inferred
per problem via data/dsa_450_infer.py and baked into data/dsa_450_detailed.py.
"""

from __future__ import annotations

from pathlib import Path

_APP_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_XLSX = _APP_ROOT / "data" / "ScalerRevision.xlsx"


def xlsx_available(path: Path | None = None) -> bool:
    """Return True if the Scaler revision workbook is present."""
    return (path or DEFAULT_XLSX).is_file()
