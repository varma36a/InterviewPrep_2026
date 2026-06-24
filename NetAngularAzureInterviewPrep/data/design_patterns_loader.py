"""Load C# source from DesignPatternsLearnignFolder (sibling repo folder)."""

from pathlib import Path

# InterviewPrep_2026/DesignPatternsLearnignFolder
PATTERNS_ROOT = Path(__file__).resolve().parents[2] / "DesignPatternsLearnignFolder"


def load_sources(relative_paths: list[str], max_chars: int = 12000) -> str:
    """Read and concatenate C# files; return placeholder if missing."""
    if not PATTERNS_ROOT.is_dir():
        return (
            f"// Source folder not found: {PATTERNS_ROOT}\n"
            "// Clone or place DesignPatternsLearnignFolder next to NetAngularAzureInterviewPrep."
        )

    parts: list[str] = []
    for rel in relative_paths:
        path = PATTERNS_ROOT / rel
        if not path.is_file():
            parts.append(f"// Missing: {rel}")
            continue
        header = f"// ── {rel} ──"
        body = path.read_text(encoding="utf-8").strip()
        parts.append(f"{header}\n{body}")

    code = "\n\n".join(parts)
    if len(code) > max_chars:
        code = code[: max_chars - 80] + "\n\n// ... (truncated — open full file in DesignPatternsLearnignFolder)"
    return code


def patterns_project_hint() -> str:
    return (
        f"**Runnable project:** `{PATTERNS_ROOT}` — "
        "`dotnet run --project DesignPatternsLearnign.csproj -- <pattern-name>`"
    )
