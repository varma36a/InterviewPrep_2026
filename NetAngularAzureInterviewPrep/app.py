import streamlit as st

from data.interview_content import (
    SECTIONS,
    SearchResult,
    count_items,
    get_all_sections,
    get_section,
    search_items,
)

LANG_MAP = {
    "csharp": "csharp",
    "typescript": "typescript",
    "javascript": "javascript",
    "sql": "sql",
    "bash": "bash",
    "yaml": "yaml",
    "html": "html",
    "css": "css",
    "dockerfile": "dockerfile",
    "hcl": "hcl",
    "text": "text",
}


def _set_search_query(term: str) -> None:
    """Set search text before widgets bind — safe for on_click callbacks."""
    st.session_state["search_query"] = term


def _sidebar_search() -> None:
    q = st.session_state.get("sidebar_search", "").strip()
    if not q:
        return
    st.session_state["nav"] = "Search & Filter"
    st.session_state["search_query"] = q


def _go_to_page(page_name: str) -> None:
    """Update nav — must use same key as the top selectbox (key='nav')."""
    st.session_state["nav"] = page_name


def get_pages() -> list[str]:
    pages = ["Home", "Search & Filter", "Roadmap", "Mock Interview"]
    pages.extend(s.title for s in get_all_sections())
    return pages


def render_top_nav(pages: list[str]) -> str:
    """Always-visible nav — primary on mobile, works on desktop too."""
    if st.session_state.get("nav") not in pages:
        st.session_state["nav"] = "Home"

    st.markdown('<div class="top-nav-container">', unsafe_allow_html=True)
    col_nav, col_meta = st.columns([4, 1])
    with col_nav:
        selected = st.selectbox(
            "📚 Navigate to",
            pages,
            key="nav",
        )
    with col_meta:
        st.markdown(
            f'<p class="top-nav-meta">{count_items()}<br><span>topics</span></p>',
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    return selected


def inject_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        :root {
            /* 2026 trending zinc dark-first palette (Vercel / shadcn / Linear) */
            --blog-bg: #09090b;
            --blog-bg-glow: radial-gradient(ellipse 80% 50% at 50% -20%, rgba(34,211,238,0.08), transparent);
            --blog-surface: #18181b;
            --blog-surface-2: #27272a;
            --blog-elevated: #3f3f46;
            --blog-border: rgba(255,255,255,0.08);
            --blog-border-strong: #3f3f46;
            --blog-text: #fafafa;
            --blog-muted: #a1a1aa;
            --blog-muted-2: #71717a;
            /* Trending 2026 accents: cyan salience + violet secondary + emerald meta */
            --blog-accent: #22d3ee;
            --blog-accent-2: #8b5cf6;
            --blog-green: #34d399;
            --blog-amber: #fbbf24;
            --blog-cta: #fafafa;
            --blog-cta-text: #09090b;
        }

        html, body, .stApp {
            background-color: var(--blog-bg) !important;
            background-image: var(--blog-bg-glow) !important;
            background-attachment: fixed !important;
            font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        }

        #MainMenu, footer {
            visibility: hidden;
            height: 0;
        }

        /* Keep header visible — required for mobile sidebar ☰ button */
        header[data-testid="stHeader"] {
            visibility: visible !important;
            height: auto !important;
            background: var(--blog-surface) !important;
            border-bottom: 1px solid var(--blog-border);
        }
        header[data-testid="stHeader"] button {
            color: var(--blog-accent) !important;
        }
        [data-testid="stSidebarCollapsedControl"],
        [data-testid="stSidebarCollapseButton"],
        button[kind="headerNoPadding"] {
            visibility: visible !important;
            min-width: 44px !important;
            min-height: 44px !important;
        }

        /* Sticky top navigation (mobile-friendly) */
        .top-nav-container {
            position: sticky;
            top: 3.25rem;
            z-index: 998;
            background: var(--blog-bg);
            padding: 0.5rem 0 0.75rem;
            margin-bottom: 0.5rem;
            border-bottom: 1px solid var(--blog-border);
        }
        .top-nav-meta {
            text-align: right;
            font-size: 1.1rem;
            font-weight: 800;
            color: var(--blog-accent);
            margin: 0.5rem 0 0;
            line-height: 1.2;
        }
        .top-nav-meta span {
            font-size: 0.65rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: var(--blog-muted);
        }
        .mobile-nav-hint {
            display: none;
            font-size: 0.78rem;
            color: var(--blog-muted);
            margin: 0 0 1rem;
            padding: 0.5rem 0.75rem;
            background: var(--blog-surface);
            border: 1px solid var(--blog-border);
            border-radius: 8px;
        }

        .block-container {
            max-width: 920px;
            padding-top: 0.75rem;
            padding-bottom: 4rem;
        }

        /* ── Blog chrome ── */
        .blog-topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.75rem 0 1.5rem;
            border-bottom: 1px solid var(--blog-border);
            margin-bottom: 2rem;
        }
        .blog-logo {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--blog-text);
            letter-spacing: -0.02em;
        }
        .blog-logo span {
            background: linear-gradient(135deg, var(--blog-accent), var(--blog-accent-2));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .blog-topbar-tag {
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: var(--blog-accent);
        }

        .blog-back {
            display: inline-block;
            color: var(--blog-muted);
            font-size: 0.875rem;
            margin-bottom: 1.25rem;
            text-decoration: none;
        }

        .blog-meta-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.25rem;
        }
        .blog-meta-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.3rem 0.75rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 500;
            border: 1px solid var(--blog-border);
            background: var(--blog-surface);
            color: var(--blog-muted);
        }
        .blog-meta-pill.purple { color: var(--blog-accent-2); border-color: rgba(139,92,246,0.35); background: rgba(139,92,246,0.08); }
        .blog-meta-pill.green  { color: var(--blog-green);  border-color: rgba(52,211,153,0.35);  background: rgba(52,211,153,0.08); }
        .blog-meta-pill.blue   { color: var(--blog-accent); border-color: rgba(34,211,238,0.35);  background: rgba(34,211,238,0.08); }
        .blog-meta-pill.amber  { color: var(--blog-amber);  border-color: rgba(251,191,36,0.35);  background: rgba(251,191,36,0.08); }

        .blog-hero-title {
            font-size: clamp(1.85rem, 4vw, 2.65rem);
            font-weight: 800;
            line-height: 1.15;
            letter-spacing: -0.03em;
            background: linear-gradient(135deg, #fafafa 0%, #a1a1aa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 0 1rem 0;
        }
        .blog-hero-lead {
            font-size: 1.1rem;
            line-height: 1.7;
            color: var(--blog-muted);
            margin-bottom: 1.75rem;
            max-width: 680px;
        }
        .blog-author {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 1rem 0 2rem;
            border-bottom: 1px solid var(--blog-border);
            margin-bottom: 2rem;
        }
        .blog-author-avatar {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: linear-gradient(135deg, #512BD4, #0078D4);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1rem;
        }
        .blog-author-name { font-weight: 600; color: var(--blog-text); font-size: 0.95rem; }
        .blog-author-role { font-size: 0.82rem; color: var(--blog-muted); }

        /* ── Section headers ── */
        .blog-section-label {
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: var(--blog-accent);
            margin-bottom: 0.5rem;
        }
        .blog-section-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--blog-text);
            letter-spacing: -0.02em;
            margin-bottom: 0.35rem;
        }
        .blog-section-desc {
            color: var(--blog-muted);
            font-size: 0.95rem;
            margin-bottom: 1.5rem;
        }

        /* ── Stat cards ── */
        .stat-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 0.75rem;
            margin-bottom: 2rem;
        }
        @media (max-width: 700px) {
            .stat-grid { grid-template-columns: repeat(2, 1fr); }
        }
        .stat-card {
            background: var(--blog-surface);
            border: 1px solid var(--blog-border);
            border-radius: 14px;
            padding: 1.1rem 0.75rem;
            text-align: center;
            transition: border-color 0.2s, box-shadow 0.2s;
        }
        .stat-card:hover {
            border-color: rgba(34,211,238,0.25);
            box-shadow: 0 0 24px rgba(34,211,238,0.06);
        }
        .stat-card h2 {
            font-size: 1.75rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--blog-accent), var(--blog-accent-2));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
            letter-spacing: -0.03em;
        }
        .stat-card p {
            font-size: 0.78rem;
            font-weight: 500;
            color: var(--blog-muted);
            margin: 0.25rem 0 0;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        /* ── Skill area cards ── */
        .skill-card {
            background: var(--blog-surface);
            border: 1px solid var(--blog-border);
            border-radius: 14px;
            padding: 1.25rem 1.35rem;
            margin-bottom: 0.75rem;
            transition: border-color 0.2s;
        }
        .skill-card:hover {
            border-color: rgba(34,211,238,0.3);
            box-shadow: 0 4px 24px rgba(0,0,0,0.25);
        }
        .skill-card h3 {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--blog-text);
            margin: 0 0 0.35rem;
        }
        .skill-card .caption {
            font-size: 0.85rem;
            color: var(--blog-muted);
            line-height: 1.5;
            margin-bottom: 0.5rem;
        }
        .skill-card .count {
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--blog-accent);
        }

        /* ── Phase pills ── */
        .phase-pill {
            display: inline-block;
            padding: 0.22rem 0.7rem;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            border: 1px solid transparent;
        }
        .pill-foundation   { background: rgba(52,211,153,0.1);  color: #34d399; border-color: rgba(52,211,153,0.3); }
        .pill-intermediate { background: rgba(34,211,238,0.1);  color: #22d3ee; border-color: rgba(34,211,238,0.3); }
        .pill-advanced     { background: rgba(139,92,246,0.1);  color: #a78bfa; border-color: rgba(139,92,246,0.3); }
        .pill-default      { background: rgba(251,191,36,0.1);  color: #fbbf24; border-color: rgba(251,191,36,0.3); }

        .result-meta {
            color: var(--blog-muted);
            font-size: 0.82rem;
            margin-bottom: 0.6rem;
        }

        /* ── Streamlit component overrides ── */
        div[data-testid="stSidebar"] {
            background: var(--blog-surface) !important;
            border-right: 1px solid var(--blog-border);
        }
        div[data-testid="stSidebar"] * { color: var(--blog-text) !important; }
        div[data-testid="stSidebar"] [data-testid="stMetricValue"] {
            color: var(--blog-accent) !important;
        }
        div[data-testid="stSidebar"] .stRadio label {
            font-size: 0.875rem !important;
            padding: 0.35rem 0 !important;
        }

        div[data-testid="stExpander"] {
            background: var(--blog-surface) !important;
            border: 1px solid var(--blog-border) !important;
            border-radius: 12px !important;
            margin-bottom: 0.65rem !important;
            overflow: hidden;
        }
        div[data-testid="stExpander"] summary {
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            color: var(--blog-text) !important;
            padding: 0.85rem 1rem !important;
        }
        div[data-testid="stExpander"] summary:hover {
            color: var(--blog-accent) !important;
        }
        div[data-testid="stExpander"] .streamlit-expanderContent {
            border-top: 1px solid var(--blog-border) !important;
            padding: 1rem 1.1rem !important;
        }

        div[data-testid="stTabs"] button {
            background: transparent !important;
            color: var(--blog-muted) !important;
            border-bottom: 2px solid transparent !important;
            font-weight: 600 !important;
            font-size: 0.85rem !important;
        }
        div[data-testid="stTabs"] button[aria-selected="true"] {
            color: var(--blog-accent) !important;
            border-bottom-color: var(--blog-accent) !important;
        }

        .stButton > button[kind="primary"] {
            background: var(--blog-cta) !important;
            color: var(--blog-cta-text) !important;
            border: none !important;
            border-radius: 999px !important;
            font-weight: 700 !important;
            padding: 0.55rem 1.4rem !important;
            box-shadow: 0 0 20px rgba(250,250,250,0.08) !important;
        }
        .stButton > button[kind="primary"]:hover {
            background: var(--blog-accent) !important;
            color: var(--blog-cta-text) !important;
            box-shadow: 0 0 24px rgba(34,211,238,0.25) !important;
        }
        .stButton > button[kind="secondary"],
        .stButton > button:not([kind="primary"]) {
            background: var(--blog-surface) !important;
            color: var(--blog-text) !important;
            border: 1px solid var(--blog-border) !important;
            border-radius: 999px !important;
            font-size: 0.8rem !important;
        }

        h1, h2, h3, h4 {
            color: var(--blog-text) !important;
            letter-spacing: -0.02em;
        }
        p, li, span, label { color: var(--blog-muted); }
        strong { color: var(--blog-text) !important; }

        hr {
            border-color: var(--blog-border) !important;
            margin: 2rem 0 !important;
        }

        div[data-testid="stCodeBlock"] {
            border: 1px solid var(--blog-border) !important;
            border-radius: 10px !important;
        }

        .stAlert {
            background: var(--blog-surface) !important;
            border: 1px solid var(--blog-border) !important;
            border-radius: 10px !important;
        }

        /* Inputs & selects */
        div[data-testid="stTextInput"] input,
        div[data-baseweb="select"] > div {
            background: var(--blog-surface) !important;
            border-color: var(--blog-border-strong) !important;
            color: var(--blog-text) !important;
            border-radius: 10px !important;
        }
        div[data-testid="stTextInput"] input:focus {
            border-color: var(--blog-accent) !important;
            box-shadow: 0 0 0 1px rgba(34,211,238,0.3) !important;
        }

        /* Markdown tables */
        .stMarkdown table {
            border-color: var(--blog-border-strong) !important;
        }
        .stMarkdown th {
            background: var(--blog-surface-2) !important;
            color: var(--blog-text) !important;
        }
        .stMarkdown td {
            border-color: var(--blog-border) !important;
            color: var(--blog-muted) !important;
        }

        /* Article prose inside expanders */
        div[data-testid="stExpander"] h4 {
            font-size: 0.85rem !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.07em !important;
            color: var(--blog-accent) !important;
            margin-top: 1.25rem !important;
        }
        div[data-testid="stExpander"] h4:first-of-type { margin-top: 0 !important; }

        .blog-divider {
            border: none;
            border-top: 1px solid var(--blog-border);
            margin: 2.5rem 0;
        }

        .blog-chapter-header {
            padding-bottom: 1.5rem;
            border-bottom: 1px solid var(--blog-border);
            margin-bottom: 1.75rem;
        }
        .blog-chapter-title {
            font-size: 1.85rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            margin: 0 0 0.4rem;
            background: linear-gradient(135deg, #fafafa 0%, #d4d4d8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .blog-chapter-sub {
            color: var(--blog-muted);
            font-size: 1rem;
            line-height: 1.6;
        }

        /* ── Mobile responsive ── */
        @media (max-width: 768px) {
            .block-container {
                max-width: 100%;
                padding-left: 0.85rem !important;
                padding-right: 0.85rem !important;
            }
            .blog-hero-title {
                font-size: 1.65rem !important;
            }
            .blog-hero-lead {
                font-size: 1rem;
            }
            .blog-topbar {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.35rem;
            }
            .stat-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 0.5rem;
            }
            .stat-card h2 {
                font-size: 1.35rem;
            }
            /* Stack main-content columns only — not sidebar */
            section[data-testid="stMain"] [data-testid="column"] {
                width: 100% !important;
                flex: 1 1 100% !important;
                min-width: 100% !important;
            }
            /* Touch-friendly buttons */
            .stButton > button {
                min-height: 44px !important;
                padding: 0.5rem 0.75rem !important;
            }
            /* Quick search: 2 per row */
            .quick-search-row [data-testid="column"] {
                flex: 1 1 48% !important;
                min-width: 48% !important;
                width: 48% !important;
            }
            /* Horizontal scroll for section tabs */
            div[data-testid="stTabs"] > div:first-child {
                overflow-x: auto !important;
                flex-wrap: nowrap !important;
                -webkit-overflow-scrolling: touch;
            }
            div[data-testid="stTabs"] button {
                white-space: nowrap !important;
                font-size: 0.78rem !important;
                padding: 0.5rem 0.65rem !important;
            }
            /* Code blocks scroll horizontally */
            div[data-testid="stCodeBlock"] pre {
                overflow-x: auto !important;
                font-size: 0.78rem !important;
            }
            /* Wider sidebar when open on mobile */
            section[data-testid="stSidebar"] {
                min-width: min(85vw, 320px) !important;
            }
            .top-nav-container {
                top: 3rem;
            }
            .mobile-nav-hint {
                display: block !important;
            }
        }
        @media (min-width: 769px) {
            .mobile-nav-hint {
                display: none !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def blog_topbar() -> None:
    st.markdown(
        """
        <div class="blog-topbar">
            <div class="blog-logo"><span>📚</span> Interview Prep Lab</div>
            <div class="blog-topbar-tag">Interview Blog</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def blog_meta_pills(*pills: tuple[str, str]) -> None:
    html = '<div class="blog-meta-row">'
    for label, css_class in pills:
        html += f'<span class="blog-meta-pill {css_class}">{label}</span>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def phase_pill(phase_id: str) -> str:
    css = {
        "foundation": "pill-foundation",
        "intermediate": "pill-intermediate",
        "advanced": "pill-advanced",
    }.get(phase_id, "pill-default")
    return f'<span class="phase-pill {css}">{phase_id.capitalize()}</span>'


def render_item(item, expanded: bool = False) -> None:
    with st.expander(f"❓ {item.question}", expanded=expanded):
        st.markdown("#### Detailed explanation")
        st.markdown(item.explanation)
        if item.key_points:
            st.markdown("#### Key points")
            for point in item.key_points:
                st.markdown(f"- ✅ {point}")
        if item.code.strip():
            st.markdown("#### Code example")
            st.code(item.code, language=LANG_MAP.get(item.language, "text"))
            st.caption("Copy and run in your IDE — examples use production-style patterns.")


def render_search_result(result: SearchResult, expanded: bool = False) -> None:
    st.markdown(
        f'<div class="result-meta">{result.section.emoji} {result.section.title} · '
        f'{phase_pill(result.phase.id)}</div>',
        unsafe_allow_html=True,
    )
    render_item(result.item, expanded=expanded)


def render_home() -> None:
    blog_topbar()
    blog_meta_pills(
        ("722+ Topics", "purple"),
        ("15 Sections", "blue"),
        ("Interview Prep", "green"),
        ("Updated 2026", "green"),
    )
    st.markdown(
        '<h1 class="blog-hero-title">.NET + Angular + Azure Interview Lab</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="blog-hero-lead">Phase-wise interview Q&A with <strong>722+ topics</strong> '
        "(50 React, 50 AWS, 50 DSA, 40 HLD, 40 CS Fundamentals, Design Patterns), "
        "<strong>detailed explanations</strong>, and <strong>code examples</strong> "
        "— plus <strong>search</strong> across all topics.</p>",
        unsafe_allow_html=True,
    )

    n_sections = len(SECTIONS)
    st.markdown(
        f"""
        <div class="stat-grid">
            <div class="stat-card"><h2>{n_sections}</h2><p>Sections</p></div>
            <div class="stat-card"><h2>{count_items()}</h2><p>Topics</p></div>
            <div class="stat-card"><h2>3</h2><p>Phases</p></div>
            <div class="stat-card"><h2>🔍</h2><p>Search</p></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.button(
        "🔍 Open Search & Filter",
        type="primary",
        use_container_width=True,
        on_click=_go_to_page,
        args=("Search & Filter",),
    )

    st.markdown('<div class="blog-section-title">Skill areas</div>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i, section in enumerate(get_all_sections()):
        total = sum(len(p.items) for p in section.phases)
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="skill-card">
                    <h3>{section.emoji} {section.title}</h3>
                    <div class="caption">{section.subtitle}</div>
                    <div class="count">{total} topics</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.button(
                f"Explore {section.title}",
                key=f"go_{section.id}",
                on_click=_go_to_page,
                args=(section.title,),
                use_container_width=True,
            )

    st.markdown('<hr class="blog-divider">', unsafe_allow_html=True)
    st.markdown('<div class="blog-section-title">Career level guide</div>', unsafe_allow_html=True)
    st.markdown(
        """
        | Level | Experience | Focus |
        |---|---|---|
        | **L1–L2** | 0–2 years | Foundation — definitions, syntax, examples |
        | **L3** | 3–5 years | Intermediate — auth, EF, RxJS, Azure services |
        | **L4–L5** | 5+ years | Advanced — architecture, K8s, Terraform, microservices |
        """
    )


def render_search() -> None:
    blog_topbar()
    st.markdown('<span class="blog-back">← Search the blog</span>', unsafe_allow_html=True)
    blog_meta_pills(("Search", "purple"), (f"{count_items()} topics", "blue"))
    st.markdown('<h1 class="blog-hero-title">🔍 Search & Filter</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="blog-hero-lead">Find any interview topic by keyword, section, or phase.</p>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        query = st.text_input(
            "Search keywords",
            placeholder="e.g. JWT, async, Docker...",
            key="search_query",
        )
    with col2:
        section_options = {s.title: s.id for s in get_all_sections()}
        selected_sections = st.multiselect(
            "Filter by section",
            options=list(section_options.keys()),
            default=[],
            key="search_sections",
        )
    with col3:
        phase_options = ["Foundation", "Intermediate", "Advanced"]
        selected_phases = st.multiselect(
            "Filter by phase",
            options=phase_options,
            default=[],
            key="search_phases",
        )

    section_ids = [section_options[s] for s in selected_sections] or None
    phase_ids = [p.lower() for p in selected_phases] or None

    st.markdown('<div class="quick-search-row">', unsafe_allow_html=True)
    quick_terms = ["CAP theorem", "Sharding", "OAuth", "TCP vs UDP", "URL Shortener",
                   "ACID", "Microservices", "JWT", "Binary Search", "Load Balancer"]
    for row_start in (0, 5):
        cols = st.columns(5)
        for col, term in zip(cols, quick_terms[row_start:row_start + 5]):
            with col:
                st.button(
                    term,
                    key=f"q_{term.replace(' ', '_')}",
                    on_click=_set_search_query,
                    args=(term,),
                    use_container_width=True,
                )
    st.markdown("</div>", unsafe_allow_html=True)

    results = search_items(query, section_ids, phase_ids)
    st.markdown(f"**{len(results)}** result(s)")

    if not results:
        st.warning("No topics match. Try a broader keyword like `API`, `SQL`, or `Angular`.")
        return

    expand_first = len(results) == 1
    for i, result in enumerate(results):
        render_search_result(result, expanded=expand_first and i == 0)
        st.divider()


def render_section(section_id: str) -> None:
    section = get_section(section_id)
    if not section:
        st.error("Section not found")
        return

    blog_topbar()
    total = sum(len(p.items) for p in section.phases)
    blog_meta_pills(
        (section.title, "purple"),
        (f"{total} topics", "blue"),
        (f"{len(section.phases)} phases", "green"),
    )
    st.markdown(
        f"""
        <div class="blog-chapter-header">
            <h1 class="blog-chapter-title">{section.emoji} {section.title}</h1>
            <p class="blog-chapter-sub">{section.subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    phase_labels = [p.label for p in section.phases]
    tabs = st.tabs(phase_labels)

    for tab, phase in zip(tabs, section.phases):
        with tab:
            st.markdown(phase_pill(phase.id), unsafe_allow_html=True)
            st.markdown(f"**{len(phase.items)} topics** in **{phase.label}**.")
            st.divider()
            for item in phase.items:
                render_item(item)


def render_roadmap() -> None:
    blog_topbar()
    blog_meta_pills(("Roadmap", "purple"), (f"{count_items()} topics", "blue"))
    st.markdown('<h1 class="blog-hero-title">🗺️ Full roadmap overview</h1>', unsafe_allow_html=True)
    for section in get_all_sections():
        total = sum(len(p.items) for p in section.phases)
        with st.expander(f"{section.emoji} {section.title} ({total} topics)", expanded=False):
            for phase in section.phases:
                st.markdown(f"**{phase.label}** ({len(phase.items)})")
                for item in phase.items:
                    st.markdown(f"- {item.question}")


def render_mock_flow() -> None:
    blog_topbar()
    blog_meta_pills(("Mock Interview", "purple"), ("Full-stack", "blue"))
    st.markdown('<h1 class="blog-hero-title">🎯 Full-stack mock interview</h1>', unsafe_allow_html=True)
    st.markdown("**How does user login and call a protected API?**")

    steps = [
        ("1. Angular", "Login → AuthService POSTs `/api/auth/login`", "typescript",
         """this.auth.login(email, password).subscribe({
  next: res => {
    localStorage.setItem('token', res.accessToken);
    this.router.navigate(['/dashboard']);
  }
});"""),
        ("2. ASP.NET Core", "Validate user, issue JWT", "csharp",
         """[HttpPost("login")]
public async Task<IActionResult> Login(LoginDto dto)
{
    var user = await _userManager.FindByEmailAsync(dto.Email);
    if (user is null || !await _userManager.CheckPasswordAsync(user, dto.Password))
        return Unauthorized();
    return Ok(new { accessToken = _jwtService.GenerateToken(user) });
}"""),
        ("3. Interceptor", "Attach Bearer token", "typescript",
         """req = req.clone({ setHeaders: { Authorization: `Bearer ${token}` } });"""),
        ("4. Authorization", "JWT + policy", "csharp",
         """[Authorize(Policy = "CanViewOrders")]
[HttpGet] public async Task<IActionResult> Get() => Ok(await _db.Orders.ToListAsync());"""),
        ("5. Azure", "Deploy stack", "text",
         """Angular → Static Web Apps / CDN
API → App Service or AKS (Docker)
DB → Azure SQL | Secrets → Key Vault
Auth → Entra ID | Logs → App Insights"""),
    ]
    for title, desc, lang, code in steps:
        st.markdown(f"### {title}")
        st.markdown(desc)
        st.code(code, language=lang)
        st.divider()


def build_sidebar() -> None:
    """Sidebar search + section navigation."""
    st.sidebar.markdown("### 🔍 Search & Navigation")

    st.sidebar.markdown("**Quick search**")
    st.sidebar.text_input("Keyword", key="sidebar_search", placeholder="JWT, Docker...")
    st.sidebar.button("Search topics", on_click=_sidebar_search, use_container_width=True)

    st.sidebar.divider()
    st.sidebar.markdown("**Pages**")
    for label in ("Home", "Search & Filter", "Roadmap", "Mock Interview"):
        st.sidebar.button(
            label,
            key=f"sb_page_{label.replace(' ', '_')}",
            use_container_width=True,
            on_click=_go_to_page,
            args=(label,),
        )

    st.sidebar.divider()
    st.sidebar.markdown("**Sections**")
    for s in get_all_sections():
        total = sum(len(p.items) for p in s.phases)
        st.sidebar.button(
            f"{s.emoji} {s.title} ({total})",
            key=f"sb_{s.id}",
            use_container_width=True,
            on_click=_go_to_page,
            args=(s.title,),
        )

    st.sidebar.divider()
    st.sidebar.metric("Topics", count_items())
    st.sidebar.metric("Sections", len(SECTIONS))


def main() -> None:
    st.set_page_config(
        page_title=".NET Angular Azure Interview Prep",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="auto",
    )
    inject_css()
    pages = get_pages()
    build_sidebar()
    page = render_top_nav(pages)

    st.markdown(
        '<p class="mobile-nav-hint">☰ Tap the menu icon (top-left) for sidebar · '
        'or use the <strong>Navigate to</strong> dropdown above.</p>',
        unsafe_allow_html=True,
    )

    if page == "Home":
        render_home()
    elif page == "Search & Filter":
        render_search()
    elif page == "Roadmap":
        render_roadmap()
    elif page == "Mock Interview":
        render_mock_flow()
    else:
        section_id = next(s.id for s in get_all_sections() if s.title == page)
        render_section(section_id)


if __name__ == "__main__":
    main()
