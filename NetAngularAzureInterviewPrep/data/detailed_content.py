"""Merge enhanced explanations and code into interview catalog items."""

from dataclasses import replace

from data.detailed_content_part1 import DETAILED_PART1
from data.detailed_content_part2 import DETAILED_PART2
from data.detailed_content_part3 import DETAILED_PART3
from data.interview_content import InterviewItem, Section

DETAILED: dict[str, dict] = {**DETAILED_PART1, **DETAILED_PART2, **DETAILED_PART3}


def apply_all_content(sections: dict[str, Section]) -> None:
    """Load market topics, merge detailed content, and enhance all catalog items."""
    from data.market_topics import apply_market_topics

    apply_market_topics(sections, DETAILED)
    from data.linq_section import LINQ_DETAILED, LINQ_SECTION, apply_linq_section

    apply_linq_section(sections, DETAILED)
    from data.design_patterns_section import apply_design_patterns_section

    apply_design_patterns_section(sections, DETAILED)
    from data.dsa_section import apply_dsa_section

    apply_dsa_section(sections, DETAILED)
    from data.hld_section import apply_hld_section

    apply_hld_section(sections, DETAILED)
    from data.cs_fundamentals_section import apply_cs_section

    apply_cs_section(sections, DETAILED)
    from data.market_detailed_gaps import MARKET_DETAILED_GAPS
    DETAILED.update(MARKET_DETAILED_GAPS)
    apply_detailed_content(sections)


def apply_detailed_content(sections: dict[str, Section]) -> None:
    """Replace explanation, code, and key_points with detailed versions where available."""
    for section in sections.values():
        for phase in section.phases:
            phase.items = [_enhance_item(item) for item in phase.items]


def _enhance_item(item: InterviewItem) -> InterviewItem:
    detail = DETAILED.get(item.id)
    if not detail:
        return item

    updates: dict = {}
    if "explanation" in detail:
        updates["explanation"] = detail["explanation"]
    if detail.get("code", "").strip():
        updates["code"] = detail["code"]
    if "language" in detail:
        updates["language"] = detail["language"]
    if detail.get("key_points"):
        updates["key_points"] = detail["key_points"]

    return replace(item, **updates) if updates else item
