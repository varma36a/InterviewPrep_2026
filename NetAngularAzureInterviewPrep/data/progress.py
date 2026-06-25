"""Interview topic progress tracking — one isolated tracker per user (no login)."""

from __future__ import annotations

import json
import secrets
from datetime import datetime, timezone

import streamlit as st
import streamlit.components.v1 as components

from data.interview_content import SECTIONS, count_items, get_all_sections

PROGRESS_KEY = "completed_topics"
PROGRESS_VERSION_KEY = "progress_version"
TRACKER_ID_KEY = "active_tracker_id"
TRACKER_NAME_KEY = "active_tracker_name"
TRACKERS_DB_KEY = "trackers_db"
BROWSER_LOADED_KEY = "progress_browser_loaded"
BROWSER_STORE_KEY = "interviewPrepTrackersV2"


def generate_tracker_id() -> str:
    """Human-friendly tracker code, e.g. IP-A7F3-K9M2."""
    token = secrets.token_hex(4).upper()
    return f"IP-{token[:4]}-{token[4:8]}"


def _valid_tracker_id(tracker_id: str) -> bool:
    tid = tracker_id.strip().upper()
    parts = tid.split("-")
    return (
        len(parts) == 3
        and parts[0] == "IP"
        and len(parts[1]) == 4
        and len(parts[2]) == 4
        and all(c in "0123456789ABCDEF" for c in parts[1] + parts[2])
    )


def _normalize_tracker_id(tracker_id: str) -> str:
    return tracker_id.strip().upper()


def _tracker_record(tracker_id: str) -> dict:
    db = st.session_state.setdefault(TRACKERS_DB_KEY, {})
    if tracker_id not in db:
        db[tracker_id] = {
            "name": "",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "completed": [],
        }
    return db[tracker_id]


def get_active_tracker_id() -> str | None:
    return st.session_state.get(TRACKER_ID_KEY)


def get_active_tracker_name() -> str:
    tracker_id = get_active_tracker_id()
    if not tracker_id:
        return ""
    db = st.session_state.get(TRACKERS_DB_KEY, {})
    return db.get(tracker_id, {}).get("name", "")


def _apply_tracker_to_session(tracker_id: str) -> None:
    record = _tracker_record(tracker_id)
    st.session_state[TRACKER_ID_KEY] = tracker_id
    st.session_state[TRACKER_NAME_KEY] = record.get("name", "")
    completed = set(record.get("completed", []))
    st.session_state[PROGRESS_KEY] = completed
    st.session_state[PROGRESS_VERSION_KEY] = st.session_state.get(PROGRESS_VERSION_KEY, 0) + 1
    _clear_checkbox_keys()


def create_tracker(name: str = "") -> str:
    tracker_id = generate_tracker_id()
    db = st.session_state.setdefault(TRACKERS_DB_KEY, {})
    db[tracker_id] = {
        "name": name.strip(),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "completed": [],
    }
    _apply_tracker_to_session(tracker_id)
    _save_browser_store()
    return tracker_id


def switch_tracker(tracker_id: str) -> str | None:
    tid = _normalize_tracker_id(tracker_id)
    if not _valid_tracker_id(tid):
        return "Invalid tracker ID. Use format IP-XXXX-XXXX."
    _sync_current_tracker_to_db()
    _apply_tracker_to_session(tid)
    _save_browser_store()
    return None


def set_tracker_name(name: str) -> None:
    tracker_id = get_active_tracker_id()
    if not tracker_id:
        return
    record = _tracker_record(tracker_id)
    record["name"] = name.strip()
    st.session_state[TRACKER_NAME_KEY] = record["name"]
    _save_browser_store()


def _sync_current_tracker_to_db() -> None:
    tracker_id = get_active_tracker_id()
    if not tracker_id:
        return
    record = _tracker_record(tracker_id)
    record["completed"] = sorted(get_completed())


def init_progress() -> None:
    if TRACKERS_DB_KEY not in st.session_state:
        st.session_state[TRACKERS_DB_KEY] = {}
    if PROGRESS_VERSION_KEY not in st.session_state:
        st.session_state[PROGRESS_VERSION_KEY] = 0

    query_tid = _query_tracker_id()
    if query_tid and not get_active_tracker_id():
        switch_tracker(query_tid)

    if BROWSER_LOADED_KEY not in st.session_state:
        _load_browser_store_once()
        return

    if not get_active_tracker_id():
        st.session_state[PROGRESS_KEY] = set()


def _query_tracker_id() -> str | None:
    try:
        raw = st.query_params.get("tracker")
    except Exception:
        return None
    if not raw:
        return None
    tid = _normalize_tracker_id(str(raw))
    return tid if _valid_tracker_id(tid) else None


def _load_browser_store_once() -> None:
    """Read multi-user tracker store from browser localStorage (one JS round-trip)."""
    try:
        from streamlit_javascript import st_javascript
    except ImportError:
        st.session_state[BROWSER_LOADED_KEY] = True
        return

    if BROWSER_LOADED_KEY in st.session_state:
        return

    raw = st_javascript(f"localStorage.getItem({json.dumps(BROWSER_STORE_KEY)})")
    if raw is None:
        return

    st.session_state[BROWSER_LOADED_KEY] = True
    if not raw or raw == "null":
        return

    try:
        store = json.loads(raw)
    except json.JSONDecodeError:
        return

    trackers = store.get("trackers", {})
    if isinstance(trackers, dict):
        st.session_state[TRACKERS_DB_KEY] = trackers

    active = store.get("active_tracker")
    if active and _valid_tracker_id(str(active)):
        _apply_tracker_to_session(_normalize_tracker_id(str(active)))


def _browser_store_payload() -> dict:
    _sync_current_tracker_to_db()
    return {
        "version": 2,
        "active_tracker": get_active_tracker_id(),
        "trackers": st.session_state.get(TRACKERS_DB_KEY, {}),
    }


def _save_browser_store() -> None:
    payload = json.dumps(_browser_store_payload())
    components.html(
        f"""<script>
        localStorage.setItem({json.dumps(BROWSER_STORE_KEY)}, {json.dumps(payload)});
        </script>""",
        height=0,
    )


def get_completed() -> set[str]:
    init_progress()
    if not get_active_tracker_id():
        return set()
    val = st.session_state.get(PROGRESS_KEY, set())
    if isinstance(val, list):
        val = set(val)
        st.session_state[PROGRESS_KEY] = val
    return val


def checkbox_key(topic_id: str) -> str:
    version = st.session_state.get(PROGRESS_VERSION_KEY, 0)
    tracker = get_active_tracker_id() or "none"
    return f"prog_cb_{tracker}_{topic_id}_v{version}"


def _checkbox_key(topic_id: str) -> str:
    return checkbox_key(topic_id)


def _clear_checkbox_keys() -> None:
    for key in list(st.session_state.keys()):
        if str(key).startswith("prog_cb_"):
            del st.session_state[key]


def sync_topic(topic_id: str) -> None:
    if not get_active_tracker_id():
        return
    done = get_completed()
    if st.session_state.get(_checkbox_key(topic_id)):
        done.add(topic_id)
    else:
        done.discard(topic_id)
    st.session_state[PROGRESS_KEY] = done
    _sync_current_tracker_to_db()
    _save_browser_store()


def set_completed(ids: set[str]) -> None:
    st.session_state[PROGRESS_KEY] = set(ids)
    st.session_state[PROGRESS_VERSION_KEY] = st.session_state.get(PROGRESS_VERSION_KEY, 0) + 1
    _clear_checkbox_keys()
    _sync_current_tracker_to_db()
    _save_browser_store()


def mark_section(section_id: str, completed: bool) -> None:
    if not get_active_tracker_id():
        return
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
    tracker_id = get_active_tracker_id()
    return {
        "version": 2,
        "tracker_id": tracker_id,
        "tracker_name": get_active_tracker_name(),
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

    tracker_id = data.get("tracker_id")
    if tracker_id and _valid_tracker_id(str(tracker_id)):
        tid = _normalize_tracker_id(str(tracker_id))
        db = st.session_state.setdefault(TRACKERS_DB_KEY, {})
        db[tid] = {
            "name": str(data.get("tracker_name", "")),
            "created_at": datetime.now(timezone.utc).isoformat(),
            "completed": sorted(cleaned),
        }
        _apply_tracker_to_session(tid)
    else:
        if not get_active_tracker_id():
            return 0, "Create or select a tracker before importing."
        set_completed(cleaned)

    _save_browser_store()
    return len(cleaned), None


def progress_summary_by_section() -> list[tuple[str, str, str, int, int]]:
    rows: list[tuple[str, str, str, int, int]] = []
    for section in get_all_sections():
        done, total = section_stats(section.id)
        rows.append((section.id, section.emoji, section.title, done, total))
    return rows


def tracker_bookmark_query(tracker_id: str) -> str:
    return f"?tracker={tracker_id}"
