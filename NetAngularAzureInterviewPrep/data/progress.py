"""Interview topic progress tracking."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import streamlit as st
import streamlit.components.v1 as components

from data.interview_content import SECTIONS, count_items, get_all_sections

PROGRESS_KEY = "completed_topics"
PROGRESS_VERSION_KEY = "progress_version"
STORAGE_KEY = "interviewPrepProgressV1"


def init_progress() -> None:
    if PROGRESS_KEY not in st.session_state:
        st.session_state[PROGRESS_KEY] = set()
    if PROGRESS_VERSION_KEY not in st.session_state:
        st.session_state[PROGRESS_VERSION_KEY] = 0


def get_completed() -> set[str]:
    init_progress()
    val = st.session_state[PROGRESS_KEY]
    if isinstance(val, list):
        val = set(val)
        st.session_state[PROGRESS_KEY] = val
    return val


def checkbox_key(topic_id: str) -> str:
    version = st.session_state.get(PROGRESS_VERSION_KEY, 0)
    return f"prog_cb_{topic_id}_v{version}"


def _checkbox_key(topic_id: str) -> str:
    return checkbox_key(topic_id)


def _clear_checkbox_keys() -> None:
    for key in list(st.session_state.keys()):
        if str(key).startswith("prog_cb_"):
            del st.session_state[key]


def sync_topic(topic_id: str) -> None:
    done = get_completed()
    if st.session_state.get(_checkbox_key(topic_id)):
        done.add(topic_id)
    else:
        done.discard(topic_id)
    persist_browser(done)


def set_completed(ids: set[str]) -> None:
    st.session_state[PROGRESS_KEY] = set(ids)
    st.session_state[PROGRESS_VERSION_KEY] = st.session_state.get(PROGRESS_VERSION_KEY, 0) + 1
    _clear_checkbox_keys()
    persist_browser(ids)


def mark_section(section_id: str, completed: bool) -> None:
    section = SECTIONS.get(section_id)
    if not section:
        return
    done = get_completed()
    for phase in section.phases:
        for item in phase.items:
            if completed:
                done.add(item.id)
            else:
                done.discard(item.id)
    set_completed(done)


def reset_all() -> None:
    set_completed(set())


def overall_stats() -> tuple[int, int]:
    total = count_items()
    done = len(get_completed())
    return done, total


def section_stats(section_id: str) -> tuple[int, int]:
    section = SECTIONS.get(section_id)
    if not section:
        return 0, 0
    completed = get_completed()
    items = [item for phase in section.phases for item in phase.items]
    done = sum(1 for item in items if item.id in completed)
    return done, len(items)


def export_payload() -> dict:
    done, total = overall_stats()
    return {
        "version": 1,
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "completed": sorted(get_completed()),
        "stats": {"done": done, "total": total},
    }


def import_payload(raw: str) -> tuple[int, str | None]:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return 0, "Invalid JSON file."

    completed = data.get("completed")
    if not isinstance(completed, list):
        return 0, "File must contain a 'completed' list of topic IDs."

    valid_ids = {
        item.id
        for section in SECTIONS.values()
        for phase in section.phases
        for item in phase.items
    }
    cleaned = {topic_id for topic_id in completed if topic_id in valid_ids}
    set_completed(cleaned)
    return len(cleaned), None


def persist_browser(ids: set[str]) -> None:
    payload = json.dumps(sorted(ids))
    components.html(
        f"""<script>
        localStorage.setItem({json.dumps(STORAGE_KEY)}, {json.dumps(payload)});
        </script>""",
        height=0,
    )


def progress_summary_by_section() -> list[tuple[str, str, str, int, int]]:
    rows: list[tuple[str, str, str, int, int]] = []
    for section in get_all_sections():
        done, total = section_stats(section.id)
        rows.append((section.id, section.emoji, section.title, done, total))
    return rows
