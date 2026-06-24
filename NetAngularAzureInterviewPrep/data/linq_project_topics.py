"""Runnable LinqPractice project topics — loads code from ../Linq folder."""

from data.interview_content import InterviewItem, Phase
from data.linq_loader import load_sources, run_hint

_SCENARIO_DEFS: list[dict] = [
    {
        "id": "linq-project-overview",
        "question": "How do I run the LinqPractice .NET 8 console project?",
        "files": ["Program.cs"],
        "run": None,
        "explanation": (
            "**LinqPractice** is a runnable **.NET 8 console app** in the `Linq/` folder with solved LINQ "
            "interview scenarios and hands-on exercises. It uses sample **employees, products, orders, "
            "customers, and students** so every query prints real output. "
            "**Run all scenarios:** `dotnet run` from `Linq/LinqPractice`. "
            "**Practice mode:** `dotnet run -- --practice` to implement queries yourself in `PracticeExercises.cs`. "
            "**Single category:** `dotnet run -- --category filtering` (or joins, grouping, nplus1, etc.). "
            "Categories map directly to files under `Scenarios/` — open the matching file while studying this app."
        ),
        "key_points": [
            "Project path: Linq/LinqPractice (sibling to NetAngularAzureInterviewPrep)",
            "dotnet run — all solved scenarios",
            "dotnet run -- --practice — DIY exercises",
            "dotnet run -- --category <name> — one topic",
            "Sample data in Data/SampleData.cs",
        ],
    },
    {
        "id": "linq-practice-filtering",
        "question": "[Runnable] LINQ filtering — Where, Distinct, and basic queries",
        "files": ["Scenarios/FilteringScenarios.cs"],
        "run": "filtering",
        "explanation": (
            "From **LinqPractice/Scenarios/FilteringScenarios.cs** — phone-screen classics: filter employees "
            "by department and salary, find out-of-stock products, active electronics under $100, hire dates, "
            "distinct cities, duplicate words, and divisibility filters. Each example prints the LINQ expression "
            "and result to the console. Study **deferred execution** — queries run when `.ToList()` is called."
        ),
        "key_points": [
            "Where for predicates — chain with &&",
            "Distinct after Select for unique values",
            "GroupBy + Where for duplicates",
            "Always materialize with ToList in demos",
            "Run: --category filtering",
        ],
    },
    {
        "id": "linq-practice-projection",
        "question": "[Runnable] LINQ projection — Select, anonymous types, DTOs",
        "files": ["Scenarios/ProjectionScenarios.cs"],
        "run": "projection",
        "explanation": (
            "**ProjectionScenarios.cs** demonstrates **Select** to shape results — anonymous types, "
            "string formatting, nested projections, and selecting into DTOs. Projection runs at query time "
            "and avoids loading full entities when you only need a few fields (same idea as EF Core `.Select()` "
            "for SQL column pruning)."
        ),
        "key_points": [
            "Select transforms each element",
            "Anonymous types for ad-hoc shapes",
            "Project early to reduce data moved",
            "Select many properties in one lambda",
            "Run: --category projection",
        ],
    },
    {
        "id": "linq-practice-sorting",
        "question": "[Runnable] LINQ sorting — OrderBy, ThenBy, descending",
        "files": ["Scenarios/SortingScenarios.cs"],
        "run": "sorting",
        "explanation": (
            "**SortingScenarios.cs** covers **OrderBy**, **OrderByDescending**, **ThenBy** for secondary sorts, "
            "and sorting by multiple keys. Common interview tasks: top N earners, products by price then name, "
            "stable multi-level ordering."
        ),
        "key_points": [
            "OrderBy returns IOrderedEnumerable",
            "ThenBy for secondary sort keys",
            "Descending variants flip comparer",
            "Take after OrderBy for top N",
            "Run: --category sorting",
        ],
    },
    {
        "id": "linq-practice-grouping",
        "question": "[Runnable] LINQ GroupBy — aggregates per group",
        "files": ["Scenarios/GroupingScenarios.cs"],
        "run": "grouping",
        "explanation": (
            "**GroupingScenarios.cs** shows **GroupBy** with **Count**, **Sum**, **Average**, **Max**, and "
            "projecting group keys. Mirrors SQL `GROUP BY` — employees per department, revenue per category, "
            "orders per customer."
        ),
        "key_points": [
            "GroupBy returns IGrouping<TKey, TElement>",
            "Aggregate per group with Count/Sum/Avg",
            "Select after GroupBy to flatten results",
            "SQL GROUP BY equivalent",
            "Run: --category grouping",
        ],
    },
    {
        "id": "linq-practice-joins",
        "question": "[Runnable] LINQ joins — Join, GroupJoin, left join, self-join",
        "files": ["Scenarios/JoinScenarios.cs"],
        "run": "joins",
        "explanation": (
            "**JoinScenarios.cs** is essential interview prep: **inner join** (orders + customers), "
            "**GroupJoin + SelectMany** for **left join** (all customers including zero orders), "
            "multi-table enrollment joins, and **self-join** for employee/manager names."
        ),
        "key_points": [
            "Join = inner join on key equality",
            "GroupJoin + SelectMany = left join pattern",
            "Join order items to products",
            "Self-join on ManagerId",
            "Run: --category joins",
        ],
    },
    {
        "id": "linq-practice-aggregation",
        "question": "[Runnable] LINQ aggregation — Sum, Average, Min, Max, Aggregate",
        "files": ["Scenarios/AggregationScenarios.cs"],
        "run": "aggregation",
        "explanation": (
            "**AggregationScenarios.cs** covers terminal aggregate operators and custom **Aggregate** "
            "folds — total order value, average salary by implicit grouping, min/max prices, and building "
            "strings or accumulators across sequences."
        ),
        "key_points": [
            "Sum/Average/Min/Max execute immediately",
            "Aggregate for custom folds",
            "Nullable averages when empty sequence",
            "Combine with Where before aggregate",
            "Run: --category aggregation",
        ],
    },
    {
        "id": "linq-practice-quantifiers",
        "question": "[Runnable] LINQ quantifiers — Any, All, Contains",
        "files": ["Scenarios/QuantifierScenarios.cs"],
        "run": "quantifiers",
        "explanation": (
            "**QuantifierScenarios.cs** demonstrates **Any** (exists?), **All** (every?), and **Contains**. "
            "Short-circuiting makes these efficient — prefer `Any()` over `Count() > 0`. Common in validation "
            "and business rules."
        ),
        "key_points": [
            "Any() faster than Count() > 0",
            "All returns true on empty sequence",
            "Contains checks value membership",
            "Combine with predicates: Any(x => ...)",
            "Run: --category quantifiers",
        ],
    },
    {
        "id": "linq-practice-sets",
        "question": "[Runnable] LINQ set operations — Union, Intersect, Except, Distinct",
        "files": ["Scenarios/SetOperationScenarios.cs"],
        "run": "sets",
        "explanation": (
            "**SetOperationScenarios.cs** covers **Union**, **Intersect**, **Except**, and **Distinct** — "
            "set algebra on sequences. Useful for comparing collections (customers who ordered vs didn't), "
            "deduplication, and merging lists."
        ),
        "key_points": [
            "Union merges distinct elements",
            "Intersect = elements in both",
            "Except = in first but not second",
            "Distinct removes duplicates",
            "Run: --category sets",
        ],
    },
    {
        "id": "linq-practice-advanced",
        "question": "[Runnable] Advanced LINQ — SelectMany, Zip, Chunk, DefaultIfEmpty",
        "files": ["Scenarios/AdvancedScenarios.cs"],
        "run": "advanced",
        "explanation": (
            "**AdvancedScenarios.cs** covers **SelectMany** (flatten nested collections), **Zip** (pair sequences), "
            "**Chunk** (.NET 6+ batching), **DefaultIfEmpty**, and other operators that appear in senior interviews."
        ),
        "key_points": [
            "SelectMany flattens nested lists",
            "Zip pairs elements by index",
            "Chunk splits into batches",
            "DefaultIfEmpty avoids empty sequence issues",
            "Run: --category advanced",
        ],
    },
    {
        "id": "linq-practice-nplus1",
        "question": "[Runnable] N+1 problem — bad pattern and three fixes",
        "files": [
            "Scenarios/NPlusOneScenarios.cs",
            "Data/SimulatedEmployeeRepository.cs",
        ],
        "run": "nplus1",
        "explanation": (
            "**NPlusOneScenarios.cs** is a must-know EF/LINQ interview topic. Demonstrates the **bad loop** "
            "(1 query for employees + N department lookups), then **Fix 1:** dictionary lookup, **Fix 2:** join, "
            "**Fix 3:** eager loading pattern. Includes query counter to prove N+1 vs fixed query counts."
        ),
        "key_points": [
            "N+1 = 1 + N queries in a loop",
            "Fix with ToDictionary lookup",
            "Fix with Join / Include in EF",
            "SimulatedEmployeeRepository counts queries",
            "Run: --category nplus1",
        ],
    },
    {
        "id": "linq-practice-querysyntax",
        "question": "[Runnable] LINQ query syntax vs method syntax",
        "files": ["Scenarios/QuerySyntaxScenarios.cs"],
        "run": "querysyntax",
        "explanation": (
            "**QuerySyntaxScenarios.cs** shows **query syntax** (`from`/`where`/`select`/`join`/`group`) "
            "alongside equivalent **method syntax**. Compiler translates query syntax to method calls — "
            "same IL. Query syntax shines for **joins** and **group joins**."
        ),
        "key_points": [
            "from/where/select compiles to extension methods",
            "join and group easier in query syntax",
            "Method syntax more common in production",
            "Mix both — know translation",
            "Run: --category querysyntax",
        ],
    },
    {
        "id": "linq-practice-exercises",
        "question": "[Runnable] Hands-on LINQ practice exercises (implement yourself)",
        "files": ["Scenarios/PracticeExercises.cs", "Data/SampleData.cs"],
        "run": "practice",
        "explanation": (
            "**PracticeExercises.cs** is your **DIY interview prep** — uncomment and implement queries in "
            "`TryExercise1` through `TryExercise8`, then run `dotnet run -- --practice`. "
            "Peek at solved scenarios in other files only after attempting. Uses the same **SampleData** "
            "employees, products, and orders."
        ),
        "key_points": [
            "Implement queries in PracticeExercises.cs",
            "Run: dotnet run -- --practice",
            "8 exercises — Seattle employees, top products, etc.",
            "Compare with solved Scenarios/ files after",
            "Best way to prepare for live coding",
        ],
    },
]


def _build_item(defn: dict) -> InterviewItem:
    code = load_sources(defn["files"])
    run = defn.get("run")
    if run == "practice":
        code += run_hint(practice=True)
    elif run:
        code += run_hint(category=run)
    else:
        code += run_hint()
    return InterviewItem(
        id=defn["id"],
        question=defn["question"],
        explanation=defn["explanation"],
        code=code,
        language="csharp",
        key_points=defn["key_points"],
    )


def _build_detailed(defn: dict) -> dict:
    item = _build_item(defn)
    return {
        "explanation": defn["explanation"],
        "code": item.code,
        "language": "csharp",
        "key_points": defn["key_points"],
    }


LINQ_PROJECT_ITEMS: list[InterviewItem] = [_build_item(d) for d in _SCENARIO_DEFS]
LINQ_PROJECT_DETAILED: dict[str, dict] = {d["id"]: _build_detailed(d) for d in _SCENARIO_DEFS}


def extend_linq_section(section, detailed: dict) -> None:
    """Append Runnable Project phase and merge detailed content."""
    runnable_phase = Phase(
        "runnable",
        "Runnable Project (LinqPractice)",
        LINQ_PROJECT_ITEMS,
    )
    section.phases.append(runnable_phase)
    detailed.update(LINQ_PROJECT_DETAILED)
