#!/usr/bin/env python3
"""Generate DSA 450 catalog from ScalerRevision.xlsx (Final_450 sheet).

Run from repo root:
    python scripts/build_dsa_450.py
"""

from __future__ import annotations

import json
import sys
import textwrap
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import pandas as pd

from data.dsa_450_infer import (
    build_explanation,
    get_phase_order,
    get_topic_guides,
    infer_complexity,
    key_points_from_meta,
    slugify,
    topic_to_phase,
)
from data.dsa_450_code import generate_csharp

XLSX = ROOT / "data" / "ScalerRevision.xlsx"
OUT_CATALOG = ROOT / "data" / "dsa_450_catalog.py"
OUT_DETAILED = ROOT / "data" / "dsa_450_detailed.py"


def load_problems() -> list[dict]:
    df = pd.read_excel(XLSX, sheet_name="Final_450", skiprows=3)
    df.columns = ["topic", "problem", "done"]
    df = df[df["problem"].notna() & (df["problem"] != "Problem:")]
    df["topic"] = df["topic"].replace("", pd.NA).ffill()
    rows: list[dict] = []
    for _, r in df.iterrows():
        problem = normalize_text(str(r["problem"]).strip())
        topic = normalize_text(str(r["topic"]).strip())
        if not problem or topic == "nan":
            continue
        rows.append({"topic": topic, "problem": problem})
    return rows


def make_id(phase_id: str, index: int, problem: str) -> str:
    return f"dsa-450-{phase_id}-{index:03d}-{slugify(problem)}"


def py_str(s: str) -> str:
    return json.dumps(normalize_text(s), ensure_ascii=True)


def normalize_text(s: str) -> str:
    """Normalize punctuation from Excel exports to ASCII-friendly text."""
    if not s:
        return ""
    s = unicodedata.normalize("NFKC", s)
    return (
        s.replace("\u2014", "-")
        .replace("\u2013", "-")
        .replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u00a0", " ")
        .strip()
    )


def generate() -> tuple[int, int]:
    problems = load_problems()
    by_phase: dict[str, list[dict]] = defaultdict(list)
    phase_labels: dict[str, str] = {}

    for row in problems:
        phase_id = topic_to_phase(row["topic"])
        by_phase[phase_id].append(row)
        phase_labels[phase_id] = row["topic"]

    guides = get_topic_guides()
    detailed_entries: dict[str, dict] = {}
    catalog_phases: list[str] = []

    for phase_id in get_phase_order():
        if phase_id not in by_phase:
            continue
        items = by_phase[phase_id]
        label = guides.get(phase_id, {}).get("title") or phase_labels.get(phase_id, phase_id)
        guide = guides.get(phase_id)
        phase_lines: list[str] = []

        if guide:
            guide_id = f"dsa-guide-{phase_id}"
            guide_title = f"[Guide] {guide['title']} - Time & Space Complexity"
            detailed_entries[guide_id] = {
                "explanation": guide["explanation"],
                "key_points": guide["key_points"],
            }
            phase_lines.append(
                f'            InterviewItem(\n'
                f'                {py_str(guide_id)},\n'
                f'                {py_str(guide_title)},\n'
                f'                {py_str(guide["explanation"])},\n'
                f'                "",\n'
                f'                "text",\n'
                f'                key_points={guide["key_points"]!r},\n'
                f'            ),'
            )

        for i, row in enumerate(items, start=1):
            pid = make_id(phase_id, i, row["problem"])
            meta = infer_complexity(row["problem"], row["topic"])
            explanation = build_explanation(row["problem"], meta)
            kps = key_points_from_meta(meta)
            code = generate_csharp(row["problem"], row["topic"], meta)
            detailed_entries[pid] = {
                "explanation": explanation,
                "key_points": kps,
                "code": code,
                "language": "csharp",
            }
            phase_lines.append(
                f'            InterviewItem(\n'
                f'                {py_str(pid)},\n'
                f'                {py_str(row["problem"])},\n'
                f'                "See detailed explanation.",\n'
                f'                {py_str("// C# solution below")},\n'
                f'                "csharp",\n'
                f'                key_points={kps!r},\n'
                f'            ),'
            )

        catalog_phases.append(
            f'        Phase({py_str(phase_id)}, {py_str(label)}, [\n'
            + "\n".join(phase_lines)
            + "\n        ]),"
        )

    catalog_src = textwrap.dedent(
        f'''\
        """Love Babbar 450 DSA catalog — auto-generated from data/ScalerRevision.xlsx.

        Regenerate: python scripts/build_dsa_450.py
        """
        from data.interview_content import InterviewItem, Phase, Section

        DSA_450_SECTION = Section(
            id="dsa",
            title="DSA Coding",
            emoji="🧮",
            color="#059669",
            subtitle="Love Babbar 450 DSA — topic-wise with detailed time & space complexity",
            phases=[
        {chr(10).join(catalog_phases)}
            ],
        )

        DSA_450_COUNT = {len(problems)}
        DSA_450_PHASE_COUNT = {len(catalog_phases)}
        '''
    )

    detailed_lines = ["DSA_450_DETAILED: dict[str, dict] = {"]
    for pid, entry in detailed_entries.items():
        detailed_lines.append(f"    {py_str(pid)}: {{")
        detailed_lines.append(f"        'explanation': {py_str(entry['explanation'])},")
        detailed_lines.append(f"        'key_points': {entry['key_points']!r},")
        if entry.get("code"):
            detailed_lines.append(f"        'code': {py_str(entry['code'])},")
            detailed_lines.append(f"        'language': 'csharp',")
        detailed_lines.append("    },")
    detailed_lines.append("}")
    detailed_src = (
        '"""Love Babbar 450 detailed explanations — auto-generated."""\n\n'
        + "\n".join(detailed_lines)
        + "\n"
    )

    OUT_CATALOG.write_text(catalog_src, encoding="utf-8")
    OUT_DETAILED.write_text(detailed_src, encoding="utf-8")
    return len(problems), len(detailed_entries)


if __name__ == "__main__":
    n_problems, n_entries = generate()
    print(f"Generated {n_problems} problems, {n_entries} detailed entries")
    print(f"  -> {OUT_CATALOG}")
    print(f"  -> {OUT_DETAILED}")
