"""Load C# source from the LinqPractice project (sibling folder)."""

from pathlib import Path

# InterviewPrep_2026/Linq
LINQ_ROOT = Path(__file__).resolve().parents[2] / "Linq"
LINQ_PROJECT = LINQ_ROOT / "LinqPractice"


def load_sources(relative_paths: list[str], max_chars: int = 14000) -> str:
    """Read and concatenate C# files from LinqPractice."""
    if not LINQ_PROJECT.is_dir():
        return (
            f"// Source folder not found: {LINQ_PROJECT}\n"
            "// Place the Linq folder next to NetAngularAzureInterviewPrep."
        )

    parts: list[str] = []
    for rel in relative_paths:
        path = LINQ_PROJECT / rel
        if not path.is_file():
            parts.append(f"// Missing: {rel}")
            continue
        parts.append(f"// ── {rel} ──\n{path.read_text(encoding='utf-8').strip()}")

    code = "\n\n".join(parts)
    if len(code) > max_chars:
        code = code[: max_chars - 80] + "\n\n// ... (truncated — open full file in Linq/LinqPractice)"
    return code


def run_hint(category: str | None = None, practice: bool = False) -> str:
    base = "dotnet run --project Linq/LinqPractice/LinqPractice.csproj"
    if practice:
        return f"\n\n// Run practice mode:\n// cd ../Linq/LinqPractice && {base} -- --practice"
    if category:
        return f"\n\n// Run this category:\n// cd ../Linq/LinqPractice && {base} -- --category {category}"
    return f"\n\n// Run all scenarios:\n// cd ../Linq/LinqPractice && {base}"
