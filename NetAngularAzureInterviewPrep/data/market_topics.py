"""Apply market-relevant interview topics (50+ per skill area) to the catalog."""

from dataclasses import replace

from data.interview_content import InterviewItem, Section

# (MARKET_ITEMS, MARKET_DETAILED) modules — order matters for readability only
_MARKET_MODULES = [
    "data.market_angular_extra",
    "data.market_angular_interview_extra",
    "data.market_dotnet_aspnet",
    "data.market_dotnet_extra",
    "data.market_aspnet_extra",
    "data.market_frontend_database",
    "data.market_database_extra",
    "data.market_azure_practices",
    "data.market_azure_extra",
    "data.market_practices_extra",
    "data.market_devops_htmlcss",
    "data.market_devops_extra",
    "data.market_htmlcss_extra",
    "data.market_react_extra",
    "data.market_aws_extra",
]


def _merge_items(sections: dict[str, Section], market_items: dict[tuple[str, str], list[InterviewItem]]) -> None:
    for (section_id, phase_id), items in market_items.items():
        section = sections.get(section_id)
        if not section:
            continue
        for phase in section.phases:
            if phase.id == phase_id:
                phase.items.extend(items)
                break


def _merge_detailed(detailed: dict[str, dict], market_detailed: dict[str, dict]) -> None:
    detailed.update(market_detailed)


def apply_market_topics(sections: dict[str, Section], detailed: dict[str, dict]) -> None:
    """Load and merge all market topic modules."""
    import importlib

    for module_path in _MARKET_MODULES:
        try:
            mod = importlib.import_module(module_path)
        except ImportError:
            continue
        items = getattr(mod, "MARKET_ITEMS", None)
        md = getattr(mod, "MARKET_DETAILED", None)
        if items:
            _merge_items(sections, items)
        if md:
            _merge_detailed(detailed, md)


def _apply_detail(item: InterviewItem, detailed: dict[str, dict]) -> InterviewItem:
    detail = detailed.get(item.id)
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
