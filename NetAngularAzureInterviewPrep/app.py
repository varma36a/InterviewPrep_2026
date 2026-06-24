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


def inject_css() -> None:
    st.markdown(
        """
        <style>
        .main-header {
            font-size: 2.2rem;
            font-weight: 700;
            background: linear-gradient(90deg, #512BD4, #0078D4, #DD0031);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.25rem;
        }
        .phase-pill {
            display: inline-block;
            padding: 0.2rem 0.75rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        .pill-foundation { background: #14532d; color: #bbf7d0; }
        .pill-intermediate { background: #1e3a8a; color: #bfdbfe; }
        .pill-advanced { background: #831843; color: #fbcfe8; }
        .stat-card {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            color: #f1f5f9;
        }
        .stat-card h2, .stat-card p {
            color: #f1f5f9;
        }
        .result-meta {
            color: #94a3b8;
            font-size: 0.85rem;
            margin-bottom: 0.5rem;
        }
        div[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        }
        div[data-testid="stSidebar"] * {
            color: #e2e8f0 !important;
        }
        .stApp {
            background-color: #0f172a;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def phase_pill(phase_id: str) -> str:
    css = {
        "foundation": "pill-foundation",
        "intermediate": "pill-intermediate",
        "advanced": "pill-advanced",
    }.get(phase_id, "pill-foundation")
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
    st.markdown('<p class="main-header">.NET + Angular + Azure Interview Lab</p>', unsafe_allow_html=True)
    st.markdown(
        "Phase-wise interview Q&A with **622+ topics** (50 DSA, 40 HLD, 40 CS Fundamentals, Design Patterns), "
        "**detailed explanations**, and **code examples** — plus **search** across all topics."
    )

    n_sections = len(SECTIONS)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="stat-card"><h2>{n_sections}</h2><p>Sections</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-card"><h2>{count_items()}</h2><p>Topics</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><h2>3</h2><p>Phases</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="stat-card"><h2>🔍</h2><p>Search</p></div>', unsafe_allow_html=True)

    st.divider()
    if st.button("🔍 Open Search & Filter", type="primary", use_container_width=True):
        st.session_state["nav"] = "Search & Filter"
        st.rerun()

    st.subheader("Skill areas")
    cols = st.columns(2)
    for i, section in enumerate(get_all_sections()):
        total = sum(len(p.items) for p in section.phases)
        with cols[i % 2]:
            st.markdown(f"### {section.emoji} {section.title}")
            st.caption(section.subtitle)
            st.markdown(f"**{total} topics**")
            if st.button(f"Explore {section.title}", key=f"go_{section.id}"):
                st.session_state["nav"] = section.title
                st.rerun()

    st.divider()
    st.subheader("Career level guide")
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
    st.title("🔍 Search & Filter")
    st.markdown("Find any interview topic by keyword, section, or phase.")

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        query = st.text_input(
            "Search keywords",
            placeholder="e.g. JWT, async, Docker, N+1, RxJS...",
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

    quick = st.columns(10)
    quick_terms = ["CAP theorem", "Sharding", "OAuth", "TCP vs UDP", "URL Shortener", "ACID", "Microservices", "JWT", "Binary Search", "Load Balancer"]
    for col, term in zip(quick, quick_terms):
        with col:
            if st.button(term, key=f"q_{term}"):
                st.session_state["search_query"] = term
                st.rerun()

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

    st.markdown(f"## {section.emoji} {section.title}")
    st.caption(section.subtitle)

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
    st.title("🗺️ Full roadmap overview")
    for section in get_all_sections():
        total = sum(len(p.items) for p in section.phases)
        with st.expander(f"{section.emoji} {section.title} ({total} topics)", expanded=False):
            for phase in section.phases:
                st.markdown(f"**{phase.label}** ({len(phase.items)})")
                for item in phase.items:
                    st.markdown(f"- {item.question}")


def render_mock_flow() -> None:
    st.title("🎯 Full-stack mock interview")
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


def build_sidebar() -> str:
    st.sidebar.title("📚 Navigation")
    pages = ["Home", "Search & Filter", "Roadmap", "Mock Interview"]
    for s in get_all_sections():
        pages.append(s.title)

    default = st.session_state.get("nav", "Home")
    if default not in pages:
        default = "Home"

    page = st.sidebar.radio("Go to", pages, index=pages.index(default))
    st.session_state["nav"] = page

    st.sidebar.divider()
    st.sidebar.markdown("**Quick search**")
    sidebar_q = st.sidebar.text_input("Keyword", key="sidebar_search", placeholder="JWT, Docker...")
    if sidebar_q and st.sidebar.button("Search"):
        st.session_state["nav"] = "Search & Filter"
        st.session_state["search_query"] = sidebar_q
        st.rerun()

    st.sidebar.divider()
    st.sidebar.metric("Topics", count_items())
    st.sidebar.metric("Sections", len(SECTIONS))

    return page


def main() -> None:
    st.set_page_config(
        page_title=".NET Angular Azure Interview Prep",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()
    page = build_sidebar()

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
