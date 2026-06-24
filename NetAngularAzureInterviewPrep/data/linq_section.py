"""Dedicated LINQ interview section — 40 top questions."""

from data.interview_content import InterviewItem, Phase, Section

LINQ_SECTION = Section(
    id="linq",
    title="LINQ Queries",
    emoji="🔶",
    color="#FF6B00",
    subtitle="LINQ to Objects, EF Core, query syntax + runnable LinqPractice project",
    phases=[
        Phase("foundation", "Foundation", [
            InterviewItem(
                "linq-introduction",
                "What is LINQ and why was it introduced in C#?",
                "See detailed explanation.",
                """// LINQ unifies querying across collections, XML, EF, etc.
var active = orders.Where(o => o.IsActive).OrderBy(o => o.Date).ToList();""",
                key_points=["Language Integrated Query", "Composable pipelines", "Strongly typed"],
            ),
            InterviewItem(
                "linq-query-vs-method-syntax",
                "What is the difference between LINQ query syntax and method syntax?",
                "See detailed explanation.",
                """// Method syntax
var q1 = orders.Where(o => o.Total > 100).Select(o => o.Id);

// Query syntax — compiler translates to method calls
var q2 = from o in orders where o.Total > 100 select o.Id;""",
                key_points=["Same IL output", "Method syntax more common", "Query syntax for joins"],
            ),
            InterviewItem(
                "linq-ienumerable",
                "What is IEnumerable<T> and how does LINQ use it?",
                "See detailed explanation.",
                """IEnumerable<Order> seq = orders.Where(o => o.IsActive);
foreach (var o in seq) Console.WriteLine(o.Id);""",
                key_points=["In-memory enumeration", "Func delegates", "Client-side evaluation"],
            ),
            InterviewItem(
                "linq-iqueryable",
                "What is IQueryable<T> and when should you use it?",
                "See detailed explanation.",
                """IQueryable<Order> query = db.Orders.Where(o => o.Status == "Open");
// Provider translates expression tree to SQL""",
                key_points=["Expression trees", "Remote execution", "EF Core queries"],
            ),
            InterviewItem(
                "linq-deferred-execution",
                "What is deferred execution in LINQ?",
                "See detailed explanation.",
                """var query = orders.Where(o => o.Total > 100); // not run yet
var list = query.ToList(); // executes now""",
                key_points=["Lazy evaluation", "Runs on enumeration", "Chainable without cost until terminal op"],
            ),
            InterviewItem(
                "linq-immediate-execution",
                "What LINQ operations execute immediately?",
                "See detailed explanation.",
                """int count = orders.Count();           // immediate
var list = orders.ToList();             // immediate
var first = orders.FirstOrDefault();    // immediate""",
                key_points=["Terminal operators", "Materialize results", "Count, ToList, First"],
            ),
            InterviewItem(
                "linq-where-filter",
                "How does Where filter collections in LINQ?",
                "See detailed explanation.",
                """var highValue = orders.Where(o => o.Total > 500 && o.IsActive);""",
                key_points=["Predicate Func<T,bool>", "Preserves order", "Deferred until enumeration"],
            ),
            InterviewItem(
                "linq-select",
                "How does Select project or transform elements?",
                "See detailed explanation.",
                """var ids = orders.Select(o => o.Id);
var dto = orders.Select(o => new { o.Id, o.Total });""",
                key_points=["Map/transform", "Anonymous types OK", "Select vs SelectMany"],
            ),
            InterviewItem(
                "linq-orderby-thenby",
                "How do OrderBy, ThenBy, and descending variants work?",
                "See detailed explanation.",
                """var sorted = orders
    .OrderBy(o => o.CustomerName)
    .ThenByDescending(o => o.Total);""",
                key_points=["Stable sort semantics", "ThenBy for secondary keys", "OrderBy returns IOrderedEnumerable"],
            ),
            InterviewItem(
                "linq-first-single",
                "When use First, Single, FirstOrDefault, and SingleOrDefault?",
                "See detailed explanation.",
                """var first = orders.First(o => o.Id == 5);       // throws if empty
var one = orders.Single(o => o.Id == 5);          // throws if not exactly one
var safe = orders.FirstOrDefault(o => o.Id == 5); // null/default if none""",
                key_points=["First = any match", "Single = exactly one", "OrDefault avoids exception"],
            ),
            InterviewItem(
                "linq-any-all",
                "How do Any and All test predicates on sequences?",
                "See detailed explanation.",
                """bool hasOpen = orders.Any(o => o.Status == "Open");
bool allPaid = orders.All(o => o.IsPaid);""",
                key_points=["Any short-circuits on first match", "All short-circuits on first false", "Empty: Any=false, All=true"],
            ),
            InterviewItem(
                "linq-count",
                "How does Count differ from LongCount and when use each?",
                "See detailed explanation.",
                """int n = orders.Count(o => o.IsActive);
long big = largeSet.LongCount(x => x > 0);""",
                key_points=["Immediate execution", "Predicate optional", "LongCount for huge sequences"],
            ),
            InterviewItem(
                "linq-take-skip",
                "How do Take, Skip, TakeWhile, and SkipWhile paginate data?",
                "See detailed explanation.",
                """var page = orders.OrderBy(o => o.Id).Skip(20).Take(10);
var afterHeader = lines.SkipWhile(l => l.StartsWith("#"));""",
                key_points=["Paging pattern", "Skip+Take on IQueryable for SQL OFFSET", "While variants use predicate"],
            ),
            InterviewItem(
                "linq-distinct",
                "How does Distinct remove duplicates?",
                "See detailed explanation.",
                """var uniqueCities = customers.Select(c => c.City).Distinct();
var uniqueByName = customers.DistinctBy(c => c.Name); // .NET 6+""",
                key_points=["Default equality comparer", "DistinctBy for key selector", "Deferred operator"],
            ),
        ]),
        Phase("intermediate", "Intermediate", [
            InterviewItem(
                "linq-groupby",
                "How does GroupBy partition and aggregate data?",
                "See detailed explanation.",
                """var byStatus = orders.GroupBy(o => o.Status);
foreach (var g in byStatus)
    Console.WriteLine($"{g.Key}: {g.Count()}");""",
                key_points=["IGrouping<TKey,TElement>", "Often followed by Select", "EF translates to GROUP BY"],
            ),
            InterviewItem(
                "linq-join",
                "How do inner joins work with Join?",
                "See detailed explanation.",
                """var result = customers.Join(
    orders,
    c => c.Id,
    o => o.CustomerId,
    (c, o) => new { c.Name, o.Total });""",
                key_points=["Inner join only", "Key selectors required", "Query syntax: join ... on ... equals"],
            ),
            InterviewItem(
                "linq-groupjoin",
                "How does GroupJoin implement left outer joins?",
                "See detailed explanation.",
                """var query = customers.GroupJoin(
    orders,
    c => c.Id,
    o => o.CustomerId,
    (c, orderGroup) => new { c.Name, Orders = orderGroup });""",
                key_points=["Left outer join pattern", "Second sequence is IGrouping", "DefaultIfEmpty for flat left join"],
            ),
            InterviewItem(
                "linq-selectmany",
                "What does SelectMany flatten and when use it?",
                "See detailed explanation.",
                """var allItems = orders.SelectMany(o => o.LineItems);
var pairs = seq1.SelectMany(a => seq2, (a, b) => (a, b));""",
                key_points=["Flatten nested collections", "Cartesian product variant", "One-to-many expansion"],
            ),
            InterviewItem(
                "linq-aggregate",
                "How does Aggregate fold a sequence into one value?",
                "See detailed explanation.",
                """var total = orders.Select(o => o.Total).Aggregate((a, b) => a + b);
var csv = names.Aggregate((a, b) => a + "," + b);""",
                key_points=["Seed overload for empty", "Custom fold logic", "Sum is specialized Aggregate"],
            ),
            InterviewItem(
                "linq-sum-avg-min-max",
                "How do Sum, Average, Min, and Max aggregate numeric sequences?",
                "See detailed explanation.",
                """decimal total = orders.Sum(o => o.Total);
double avg = orders.Average(o => o.Total);
decimal max = orders.Max(o => o.Total);""",
                key_points=["Throw on empty without selector nuance", "Nullable types for empty safety", "EF translates to SQL aggregates"],
            ),
            InterviewItem(
                "linq-oftype-cast",
                "What is the difference between OfType and Cast?",
                "See detailed explanation.",
                """var dogs = animals.OfType<Dog>();   // skips non-matching
var all = animals.Cast<Dog>();          // throws on wrong type""",
                key_points=["OfType filters safely", "Cast throws InvalidCastException", "Use with mixed collections"],
            ),
            InterviewItem(
                "linq-defaultifempty",
                "How does DefaultIfEmpty handle empty sequences?",
                "See detailed explanation.",
                """var firstOrZero = numbers.Take(0).DefaultIfEmpty(0);
var firstOrDefault = names.Where(n => n.StartsWith("Z")).DefaultIfEmpty();""",
                key_points=["Single default element if empty", "Useful after GroupJoin", "Parameter sets default value"],
            ),
            InterviewItem(
                "linq-zip",
                "How does Zip combine two sequences element-wise?",
                "See detailed explanation.",
                """var combined = names.Zip(scores, (name, score) => $"{name}: {score}");
// .NET 6+ — Zip without result selector pairs tuples""",
                key_points=["Stops at shorter sequence", "Result selector optional", "Not a SQL JOIN"],
            ),
            InterviewItem(
                "linq-chunk",
                "How does Chunk split sequences into fixed-size batches?",
                "See detailed explanation.",
                """foreach (var batch in items.Chunk(100))
{
    await ProcessBatchAsync(batch);
}""",
                key_points=[".NET 6+ operator", "Last chunk may be smaller", "Batch processing pattern"],
            ),
            InterviewItem(
                "linq-tolist-toarray",
                "When materialize with ToList vs ToArray?",
                "See detailed explanation.",
                """var list = query.ToList();   // List<T>, resizable
var arr = query.ToArray();     // T[], fixed size, slightly leaner""",
                key_points=["Force execution", "Snapshot data", "Avoid repeated enumeration"],
            ),
            InterviewItem(
                "linq-asenumerable",
                "What does AsEnumerable do and why use it?",
                "See detailed explanation.",
                """// Switch from IQueryable (SQL) to IEnumerable (memory)
var inMemory = db.Orders.AsEnumerable()
    .Where(o => ComplexClientFilter(o));""",
                key_points=["Breaks EF translation", "Client-side evaluation", "Use sparingly for performance"],
            ),
            InterviewItem(
                "linq-extension-methods",
                "How are LINQ operators implemented as extension methods?",
                "See detailed explanation.",
                """public static IEnumerable<T> MyWhere<T>(
    IEnumerable<T> source, Func<T, bool> predicate)
{
    foreach (var item in source)
        if (predicate(item)) yield return item;
}""",
                key_points=["System.Linq.Queryable / Enumerable", "static class + this param", "Custom operators same pattern"],
            ),
            InterviewItem(
                "linq-into-let",
                "What do into and let do in query syntax?",
                "See detailed explanation.",
                """var query = from o in orders
    let tax = o.Total * 0.2m
    where tax > 50
    select new { o.Id, tax };

var grouped = from o in orders
    group o by o.Status into g
    select new { g.Key, Count = g.Count() };""",
                key_points=["let introduces range variable", "into continues after group", "Compiler rewrites to methods"],
            ),
        ]),
        Phase("advanced", "Advanced", [
            InterviewItem(
                "linq-expression-trees",
                "What are expression trees and how do they relate to LINQ?",
                "See detailed explanation.",
                """Expression<Func<Order, bool>> expr = o => o.Total > 100;
// Inspected/translated by IQueryable providers""",
                key_points=["Code as data", "Not compiled delegates", "EF builds SQL from trees"],
            ),
            InterviewItem(
                "linq-providers",
                "What is a LINQ provider and how does it work?",
                "See detailed explanation.",
                """// IEnumerable provider — delegates compiled, runs in CLR
IEnumerable<T> mem = list.Where(x => x > 0);

// IQueryable provider — expression tree inspected
IQueryable<T> remote = dbSet.Where(x => x > 0);""",
                key_points=["IQueryProvider executes queries", "EF Core, LINQ to XML", "Provider-specific translation"],
            ),
            InterviewItem(
                "linq-to-objects-patterns",
                "What are common LINQ to Objects patterns in production code?",
                "See detailed explanation.",
                """var lookup = items.ToLookup(i => i.Category);
var dict = items.ToDictionary(i => i.Id);
var set = items.Select(i => i.Code).ToHashSet();""",
                key_points=["ToLookup for grouping", "ToDictionary needs unique keys", "Immutable collections"],
            ),
            InterviewItem(
                "linq-ef-core-sql",
                "How does EF Core translate LINQ to SQL?",
                "See detailed explanation.",
                """var q = db.Orders
    .Where(o => o.Total > 100)
    .OrderBy(o => o.Date)
    .Select(o => new { o.Id, o.Total });
// SELECT o.Id, o.Total FROM Orders WHERE Total > 100 ORDER BY Date""",
                key_points=["IQueryable stays in database", "Not all C# translates", "Log SQL for debugging"],
            ),
            InterviewItem(
                "linq-compiled-queries",
                "What are compiled queries in EF Core and when use them?",
                "See detailed explanation.",
                """var compiled = EF.CompileAsyncQuery((AppDbContext ctx, int id) =>
    ctx.Orders.Where(o => o.Id == id));

var order = await compiled(db, 42);""",
                key_points=["Cache query plan", "Micro-optimization", "Parameterized reuse"],
            ),
            InterviewItem(
                "linq-dynamic",
                "How do you build dynamic LINQ queries at runtime?",
                "See detailed explanation.",
                """// System.Linq.Dynamic.Core (popular package)
var q = db.Orders.Where("Total > @0", 100);

// Or build Expression trees manually for type safety""",
                key_points=["Dynamic.Core for string predicates", "Security: validate inputs", "Prefer strongly typed when possible"],
            ),
            InterviewItem(
                "linq-custom-operators",
                "How do you implement custom LINQ operators?",
                "See detailed explanation.",
                """public static IEnumerable<T> Batch<T>(
    this IEnumerable<T> source, int size)
{
    using var e = source.GetEnumerator();
    while (e.MoveNext())
    {
        var batch = new List<T> { e.Current };
        for (int i = 1; i < size && e.MoveNext(); i++)
            batch.Add(e.Current);
        yield return batch;
    }
}""",
                key_points=["Extension on IEnumerable", "yield return for deferred", "Follow naming conventions"],
            ),
            InterviewItem(
                "linq-performance",
                "What are LINQ performance best practices?",
                "See detailed explanation.",
                """// Prefer indexing over repeated Where
var byId = orders.ToDictionary(o => o.Id);
var order = byId.GetValueOrDefault(id);

// Use for loops for hot paths if profiling shows LINQ cost""",
                key_points=["Materialize once", "Filter early in IQueryable", "Avoid AsEnumerable early"],
            ),
            InterviewItem(
                "linq-multiple-enumeration",
                "What is the multiple enumeration trap?",
                "See detailed explanation.",
                """var query = orders.Where(o => ExpensiveCheck(o));
var count = query.Count();  // enumerates all
var list = query.ToList();  // enumerates again — double work!""",
                key_points=["Deferred queries re-run", "Materialize with ToList", " IEnumerable may be single-use stream"],
            ),
            InterviewItem(
                "linq-null-handling",
                "How should you handle nulls in LINQ queries?",
                "See detailed explanation.",
                """var names = orders
    .Where(o => o.Customer != null)
    .Select(o => o.Customer!.Name);

var safe = items.Where(x => x?.IsActive == true);""",
                key_points=["Null propagates in projections", "Where before Select", "FirstOrDefault returns default"],
            ),
            InterviewItem(
                "linq-plinq",
                "What is PLINQ and when should you use it?",
                "See detailed explanation.",
                """var results = items.AsParallel()
    .WithDegreeOfParallelism(4)
    .Where(x => CpuHeavyFilter(x))
    .ToList();""",
                key_points=["Parallel LINQ", "CPU-bound workloads", "Ordering not guaranteed by default"],
            ),
            InterviewItem(
                "linq-pitfalls",
                "What are common LINQ interview pitfalls and mistakes?",
                "See detailed explanation.",
                """// Pitfall: filtering after ToList on entire table
var bad = db.Orders.ToList().Where(o => o.Total > 100);

// Pitfall: modifying source during enumeration
foreach (var x in list.Where(...)) list.Remove(x); // invalid""",
                key_points=["Client eval pulls all rows", "Modify collection during iterate", "Assuming query syntax is different IL"],
            ),
        ]),
    ],
)

LINQ_DETAILED: dict[str, dict] = {
    "linq-introduction": {
        "explanation": (
            "**LINQ** (Language Integrated Query) brings **query capabilities directly into C#** so you can filter, sort, group, and join data with a consistent syntax. "
            "It was introduced in **C# 3.0** alongside **lambda expressions** and **extension methods** to replace verbose loops and disparate query APIs. "
            "LINQ works over **IEnumerable<T>** (in-memory objects), **IQueryable<T>** (remote providers like EF Core), XML, and more. "
            "Queries are **composable** — each operator returns a new sequence you can chain — and **strongly typed**, catching many errors at compile time. "
            "**Interview tip:** emphasize that LINQ is not a single library call but a **pattern** of extension methods plus optional query syntax sugar."
        ),
        "code": """// LINQ to Objects — filter, sort, project
var topOrders = orders
    .Where(o => o.IsActive && o.Total > 100)
    .OrderByDescending(o => o.Total)
    .Select(o => new OrderDto(o.Id, o.Total))
    .Take(10)
    .ToList();

// Same pipeline is readable and refactor-safe vs manual loops""",
        "language": "csharp",
        "key_points": [
            "Unified query model across data sources",
            "Introduced with C# 3.0 lambdas and extension methods",
            "Composable, strongly typed operator pipelines",
            "Works with IEnumerable and IQueryable",
            "Foundation for EF Core data access",
        ],
    },
    "linq-query-vs-method-syntax": {
        "explanation": (
            "**Method syntax** chains extension methods like `Where`, `Select`, and `OrderBy` — it is the style most C# developers use daily. "
            "**Query syntax** uses keywords `from`, `where`, `select`, `join`, `group` and reads closer to SQL. "
            "The compiler **translates query syntax into method calls** — they produce equivalent IL and there is no runtime difference. "
            "Query syntax shines for **multi-table joins** and **group continuations** (`into`); method syntax is often clearer for simple chains. "
            "Not every operator exists in query syntax (e.g., `Take`, `Zip`) — you mix both when needed."
        ),
        "code": """// Method syntax
var method = orders
    .Where(o => o.Total > 100)
    .OrderBy(o => o.Date)
    .Select(o => o.Id);

// Query syntax — compiler rewrites to Enumerable methods
var query = from o in orders
            where o.Total > 100
            orderby o.Date
            select o.Id;

// Join — query syntax often cleaner
var joined = from c in customers
             join o in orders on c.Id equals o.CustomerId
             select new { c.Name, o.Total };""",
        "language": "csharp",
        "key_points": [
            "Both syntaxes compile to the same method calls",
            "Method syntax is more common in production code",
            "Query syntax helps with complex joins and groups",
            "Some operators only exist as methods",
            "Mix styles — query for joins, methods for Take/Skip",
        ],
    },
    "linq-ienumerable": {
        "explanation": (
            "`IEnumerable<T>` is the core **pull-based enumeration** interface — `MoveNext` and `Current` (via iterator pattern). "
            "LINQ to Objects extension methods live in `System.Linq.Enumerable` and accept `IEnumerable<T>` with **compiled delegates** (`Func<T,bool>`). "
            "Evaluation happens **in memory** on the CLR as you enumerate — filters are not sent to a database. "
            "Many operators use **iterator blocks** (`yield return`) to stay lazy and avoid buffering entire sequences. "
            "**Interview angle:** anything after `AsEnumerable()` or on a `List<T>` uses IEnumerable semantics even if it started as IQueryable."
        ),
        "code": """IEnumerable<int> evens = Enumerable.Range(1, 10)
    .Where(n => n % 2 == 0); // deferred — Func<int,bool>

foreach (var n in evens)
    Console.WriteLine(n); // 2, 4, 6, 8, 10 — executes now

// IEnumerable uses delegates, not expression trees
Func<Order, bool> predicate = o => o.Total > 50;
var filtered = orders.Where(predicate);""",
        "language": "csharp",
        "key_points": [
            "Pull-based iteration with foreach",
            "LINQ to Objects uses Func delegates",
            "In-memory / client-side evaluation",
            "Deferred operators return new IEnumerable",
            "Foundation interface for LINQ extension methods",
        ],
    },
    "linq-iqueryable": {
        "explanation": (
            "`IQueryable<T>` extends `IEnumerable<T>` but adds **Expression**-based predicates and an **`IQueryProvider`**. "
            "Providers (EF Core, OData) inspect **expression trees** and translate them to **SQL** or another remote language. "
            "The query executes **remotely** — only matching rows cross the network — which is critical for performance. "
            "Once you call `AsEnumerable()` or operators that cannot translate, execution **switches to the client**. "
            "**Interview trap:** assigning `IQueryable` to `IEnumerable` or calling custom methods in predicates breaks translation."
        ),
        "code": """// EF Core — IQueryable stays in SQL until terminal op
IQueryable<Order> query = db.Orders
    .Where(o => o.Status == "Open")
    .OrderBy(o => o.Date);

// Provider builds: SELECT ... WHERE Status = 'Open' ORDER BY Date
var results = await query.ToListAsync();

// IQueryable exposes Expression, not just delegates
Expression body = query.Expression; // tree for provider""",
        "language": "csharp",
        "key_points": [
            "Expression trees instead of plain delegates",
            "Executed by IQueryProvider (EF Core, etc.)",
            "Remote execution — filter in database",
            "AsEnumerable breaks SQL translation",
            "Do not hide IQueryable behind IEnumerable too early",
        ],
    },
    "linq-deferred-execution": {
        "explanation": (
            "**Deferred execution** means a LINQ query does not run when you define it — it runs when you **enumerate** or call a **terminal operator**. "
            "Operators like `Where`, `Select`, and `OrderBy` build a **pipeline** that wraps the source iterator. "
            "This enables **lazy** processing: elements flow one at a time without allocating a full intermediate list. "
            "The trade-off is that **multiple enumerations re-execute** the entire pipeline unless you materialize. "
            "**Interview tip:** contrast with `ToList`, `Count`, `First` which force immediate execution."
        ),
        "code": """var source = GetOrders(); // IEnumerable<Order>

var pipeline = source
    .Where(o => o.Total > 100)   // deferred
    .Select(o => o.Id);          // deferred

// Nothing executed yet — no DB call, no loop

var ids = pipeline.ToList();     // NOW Where + Select run once""",
        "language": "csharp",
        "key_points": [
            "Query defined ≠ query executed",
            "Pipeline runs on foreach or terminal op",
            "Memory-efficient lazy streaming",
            "Re-enumeration re-runs the pipeline",
            "Materialize when you need a stable snapshot",
        ],
    },
    "linq-immediate-execution": {
        "explanation": (
            "**Immediate execution** operators run the query **right away** and return a scalar, collection, or single element. "
            "Examples include `ToList`, `ToArray`, `Count`, `Sum`, `First`, `Single`, and `Aggregate`. "
            "They **consume** the underlying sequence (or send one SQL command) at the call site. "
            "`ToList`/`ToArray` **materialize** results — useful for caching and avoiding double enumeration. "
            "**Interview angle:** know which calls hit the database once vs accidentally twice (`Count()` then `ToList()` on same IQueryable still runs two queries)."
        ),
        "code": """var query = db.Orders.Where(o => o.IsActive);

// Each terminal operator triggers execution
int count = query.Count();           // SQL COUNT
var list = query.ToList();         // SQL SELECT — second round-trip!
var first = query.FirstOrDefault(); // third round-trip — inefficient

// Better: materialize once
var materialized = query.ToList();
int count2 = materialized.Count;
var first2 = materialized.FirstOrDefault();""",
        "language": "csharp",
        "key_points": [
            "Terminal operators force execution immediately",
            "ToList/ToArray snapshot the sequence",
            "Scalars: Count, Sum, First, Any",
            "Multiple terminals on IQueryable = multiple queries",
            "Materialize once when reusing results",
        ],
    },
    "linq-where-filter": {
        "explanation": (
            "`Where` filters a sequence using a **predicate** `Func<T,bool>` (or `Expression<Func<T,bool>>` for IQueryable). "
            "It is **deferred** — it returns a new iterator that pulls from the source and yields matching elements. "
            "Order of elements that pass the filter is **preserved** relative to the source. "
            "On EF Core, `Where` translates to SQL `WHERE` — push filters as early as possible in the pipeline. "
            "**Tip:** combine conditions in one `Where` vs chaining two `Where` calls — similar SQL, slightly less iterator overhead in memory."
        ),
        "code": """// In-memory filter
var bigActive = orders.Where(o => o.IsActive && o.Total >= 500);

// Query syntax equivalent
var q = from o in orders
        where o.IsActive && o.Total >= 500
        select o;

// EF Core — becomes WHERE IsActive = 1 AND Total >= 500
var dbQuery = db.Orders.Where(o => o.IsActive && o.Total >= 500);""",
        "language": "csharp",
        "key_points": [
            "Predicate filters elements — deferred operator",
            "Preserves relative order of survivors",
            "IQueryable Where → SQL WHERE clause",
            "Filter early in pipeline for performance",
            "Index-friendly predicates help SQL side",
        ],
    },
    "linq-select": {
        "explanation": (
            "`Select` **projects** each element to a new shape — map, transform, or flatten via a selector `Func<T,TResult>`. "
            "It is lazy and returns one output element per input element (unless you later use `SelectMany`). "
            "Anonymous types and tuples are common for ad-hoc projections without defining DTO classes. "
            "In EF Core, `Select` controls which **columns** are fetched — prefer projecting only needed fields over loading full entities. "
            "Do not confuse `Select` with `Where` — `Select` changes type/shape; `Where` removes elements."
        ),
        "code": """// Project to anonymous type
var summaries = orders.Select(o => new
{
    o.Id,
    o.Total,
    Tax = o.Total * 0.2m
});

// Map to DTO — EF translates column list
var dtoQuery = db.Orders.Select(o => new OrderListDto
{
    Id = o.Id,
    Total = o.Total
});

// Select with index
var indexed = items.Select((item, index) => $"{index}: {item}");""",
        "language": "csharp",
        "key_points": [
            "Transforms each element — one-to-one projection",
            "Anonymous types and DTOs common in projections",
            "EF Select limits columns in SQL SELECT",
            "Select vs SelectMany — flat vs nested",
            "Deferred until enumeration",
        ],
    },
    "linq-orderby-thenby": {
        "explanation": (
            "`OrderBy` and `OrderByDescending` sort by a **key selector** and return `IOrderedEnumerable<T>`. "
            "`ThenBy` / `ThenByDescending` apply **secondary keys** when primary keys compare equal. "
            "LINQ sorting is **stable** — equal keys retain original relative order. "
            "On `IQueryable`, ordering translates to SQL `ORDER BY`; required for reliable `Skip`/`Take` paging. "
            "**Trap:** calling `OrderBy` again replaces prior sort — use `ThenBy` for multi-column sorts."
        ),
        "code": """var sorted = orders
    .OrderBy(o => o.CustomerName)       // primary key
    .ThenByDescending(o => o.Total)     // secondary key
    .ThenBy(o => o.Id);                 // tertiary

// Query syntax
var q = from o in orders
        orderby o.CustomerName, o.Total descending
        select o;

// Paging requires OrderBy on IQueryable for deterministic pages
var page = db.Orders.OrderBy(o => o.Id).Skip(20).Take(10);""",
        "language": "csharp",
        "key_points": [
            "OrderBy returns IOrderedEnumerable for ThenBy",
            "Stable sort preserves equal-key order",
            "ThenBy for multi-column sorting",
            "SQL ORDER BY for IQueryable",
            "Required before Skip/Take paging in EF",
        ],
    },
    "linq-first-single": {
        "explanation": (
            "`First` returns the **first** matching element or throws if the sequence is empty; `FirstOrDefault` returns **default** instead. "
            "`Single` requires **exactly one** match — throws if empty or more than one; `SingleOrDefault` allows zero but not multiple. "
            "These are **immediate** operators — they stop as soon as the answer is known (short-circuit). "
            "Use `Single` when duplicates indicate a **data integrity** problem (unique key expected). "
            "**EF tip:** `First` without ordering on SQL may return arbitrary row — add `OrderBy` when determinism matters."
        ),
        "code": """var first = orders.First(o => o.Total > 1000); // throws if none

var safe = orders.FirstOrDefault(o => o.Id == 99); // null if missing

var unique = users.Single(u => u.Email == email); // throws if 0 or 2+

// EF — add OrderBy for deterministic First
var latest = db.Orders
    .Where(o => o.CustomerId == id)
    .OrderByDescending(o => o.Date)
    .FirstOrDefault();""",
        "language": "csharp",
        "key_points": [
            "First = first match; Single = exactly one",
            "OrDefault variants avoid exception on empty",
            "Single throws on duplicates — data guard",
            "Immediate execution with short-circuit",
            "Add OrderBy with First on SQL sources",
        ],
    },
    "linq-any-all": {
        "explanation": (
            "`Any` returns **true** if at least one element exists (or matches the predicate); it **short-circuits** on first match. "
            "`All` returns **true** only if **every** element matches; it short-circuits on first failure. "
            "On an **empty** sequence: `Any()` is **false**, `All(predicate)` is **true** (vacuous truth). "
            "Prefer `Any(predicate)` over `Count(predicate) > 0` — clearer intent and can stop early. "
            "EF translates both to efficient SQL `EXISTS` / boolean expressions."
        ),
        "code": """bool hasVip = orders.Any(o => o.Total > 10_000);

bool allShipped = orders.All(o => o.Status == "Shipped");

// Empty sequence behavior
var empty = Enumerable.Empty<int>();
Console.WriteLine(empty.Any());           // false
Console.WriteLine(empty.All(x => x > 0)); // true

// Prefer Any over Count
if (orders.Any(o => o.IsLate)) { /* ... */ }""",
        "language": "csharp",
        "key_points": [
            "Any — exists; All — every element matches",
            "Short-circuit for performance",
            "Empty: Any=false, All=true",
            "Prefer Any over Count() > 0",
            "EF maps to EXISTS and AND predicates",
        ],
    },
    "linq-count": {
        "explanation": (
            "`Count` returns the number of elements as **int**; with a predicate, counts matches only. "
            "`LongCount` returns **long** for sequences that may exceed `int.MaxValue`. "
            "Both execute **immediately** — on EF they become `SELECT COUNT(*)`. "
            "Unlike `Any`, `Count` must scan the full matching set (unless provider optimizes). "
            "**Trap:** `Count()` on deferred IEnumerable after expensive `Where` runs the filter for every element."
        ),
        "code": """int total = orders.Count();
int active = orders.Count(o => o.IsActive);

long huge = bigData.LongCount(x => x > 0);

// EF — single COUNT query
int dbCount = db.Orders.Count(o => o.Status == "Open");

// Expensive if pipeline is heavy and you only need existence
bool exists = orders.Any(o => o.Id == id); // better than Count > 0""",
        "language": "csharp",
        "key_points": [
            "Immediate execution — full scan typically",
            "LongCount for very large sequences",
            "Predicate overload counts matches only",
            "EF translates to SQL COUNT",
            "Use Any when you only need existence",
        ],
    },
    "linq-take-skip": {
        "explanation": (
            "`Skip(n)` bypasses the first **n** elements; `Take(n)` returns at most **n** elements — together they implement **pagination**. "
            "`SkipWhile` / `TakeWhile` use predicates instead of fixed counts. "
            "On **IQueryable**, `Skip`/`Take` translate to SQL `OFFSET`/`FETCH` (or equivalent). "
            "Always pair paging with a **stable OrderBy** — without it, pages can shift between requests. "
            "`TakeWhile`/`SkipWhile` are mainly LINQ to Objects — EF support is limited."
        ),
        "code": """int page = 3, pageSize = 20;

var pageData = db.Orders
    .OrderBy(o => o.Id)           // deterministic sort
    .Skip((page - 1) * pageSize)
    .Take(pageSize)
    .ToList();

// TakeWhile — in memory
var headerLines = lines.TakeWhile(l => l.StartsWith("#"));

// SkipWhile — drop prefix until predicate fails
var body = lines.SkipWhile(l => string.IsNullOrWhiteSpace(l));""",
        "language": "csharp",
        "key_points": [
            "Skip + Take = pagination pattern",
            "SQL OFFSET/FETCH on IQueryable",
            "Always OrderBy before paging",
            "While variants predicate-based",
            "Take(1) alternative to FirstOrDefault in some cases",
        ],
    },
    "linq-distinct": {
        "explanation": (
            "`Distinct` removes **duplicate** elements using the default equality comparer (or overload with `IEqualityComparer<T>`). "
            "It is **deferred** and typically uses a **hash set** internally — O(n) average time. "
            ".NET 6+ adds `DistinctBy(keySelector)` to dedupe by a key without projecting away other fields first. "
            "EF Core translates `Distinct` to SQL `DISTINCT` — can be expensive on wide rows. "
            "For custom equality (e.g., case-insensitive names), pass a comparer or normalize in `Select` before `Distinct`."
        ),
        "code": """var cities = customers.Select(c => c.City).Distinct();

// .NET 6+ — distinct by key
var uniqueByEmail = users.DistinctBy(u => u.Email);

// Custom comparer
var distinctNames = names.Distinct(StringComparer.OrdinalIgnoreCase);

// EF
var statuses = db.Orders.Select(o => o.Status).Distinct().ToList();""",
        "language": "csharp",
        "key_points": [
            "Removes duplicates — uses equality comparer",
            "DistinctBy (.NET 6+) dedupes by key",
            "Deferred but buffers keys in hash set",
            "EF → SQL DISTINCT",
            "Custom comparer for non-default equality",
        ],
    },
    "linq-groupby": {
        "explanation": (
            "`GroupBy` partitions a sequence into **IGrouping<TKey,TElement>** buckets sharing the same key. "
            "Each group exposes `.Key` and enumerates its elements — often followed by `Select` for aggregates per group. "
            "Query syntax uses `group o by o.Status` and optional `into g` for continuations. "
            "EF Core translates to SQL `GROUP BY` when aggregation is translatable. "
            "**Trap:** client-side `GroupBy` after `ToList()` on huge tables — group in SQL when possible."
        ),
        "code": """// Method syntax
var groups = orders.GroupBy(o => o.Status);

foreach (var g in groups)
    Console.WriteLine($"{g.Key}: {g.Sum(o => o.Total)}");

// Projection per group
var summary = orders.GroupBy(o => o.CustomerId)
    .Select(g => new { CustomerId = g.Key, Total = g.Sum(o => o.Total) });

// Query syntax with into
var q = from o in orders
        group o by o.Status into statusGroup
        select new { statusGroup.Key, Count = statusGroup.Count() };""",
        "language": "csharp",
        "key_points": [
            "Partitions into IGrouping by key",
            "Often paired with aggregate Select",
            "EF translates to SQL GROUP BY",
            "into continues query after group",
            "Client GroupBy after ToList is costly",
        ],
    },
    "linq-join": {
        "explanation": (
            "`Join` performs an **inner join** — only pairs with matching keys on both sides appear in the result. "
            "You supply **outer key**, **inner key**, and **result selector** `(outer, inner) => result`. "
            "Query syntax: `join o in orders on c.Id equals o.CustomerId` — note **`equals`** not `==`. "
            "There is no built-in inner join that preserves unmatched outer rows — use `GroupJoin` + `DefaultIfEmpty` for left join. "
            "EF Core translates joins to SQL `INNER JOIN` when relationships and keys are clear."
        ),
        "code": """var inner = customers.Join(
    orders,
    c => c.Id,
    o => o.CustomerId,
    (c, o) => new { c.Name, o.Total, o.Id });

// Query syntax
var q = from c in customers
        join o in orders on c.Id equals o.CustomerId
        select new { c.Name, o.Total };

// EF — navigation properties often avoid manual Join
var viaNav = db.Customers.Select(c => new { c.Name, Orders = c.Orders });""",
        "language": "csharp",
        "key_points": [
            "Inner join — matches only on both sides",
            "Three lambdas: outer key, inner key, result",
            "Query syntax uses equals keyword",
            "Left outer needs GroupJoin pattern",
            "EF prefers navigation properties when possible",
        ],
    },
    "linq-groupjoin": {
        "explanation": (
            "`GroupJoin` correlates two sequences and groups matching inner elements **per outer element** — the basis for **left outer joins** in LINQ. "
            "The result selector receives `(outer, IEnumerable<inner>)` — the inner sequence may be **empty** if no matches. "
            "To flatten into a left join, use `SelectMany` with `DefaultIfEmpty()`. "
            "Query syntax: `join o in orders on c.Id equals o.CustomerId into orderGroup`. "
            "EF Core supports `GroupJoin` translation but shape affects generated SQL complexity."
        ),
        "code": """// GroupJoin — each customer with their orders (or empty)
var grouped = customers.GroupJoin(
    orders,
    c => c.Id,
    o => o.CustomerId,
    (c, orderGroup) => new { c.Name, Orders = orderGroup });

// Left outer join flatten
var leftJoin = customers.GroupJoin(
    orders,
    c => c.Id,
    o => o.CustomerId,
    (c, og) => new { c, og })
    .SelectMany(x => x.og.DefaultIfEmpty(),
        (x, o) => new { x.c.Name, OrderId = o?.Id });""",
        "language": "csharp",
        "key_points": [
            "Outer element paired with group of inners",
            "Empty inner group = no matches — left join base",
            "DefaultIfEmpty + SelectMany flattens",
            "Query syntax uses join ... into",
            "EF translation depends on query shape",
        ],
    },
    "linq-selectmany": {
        "explanation": (
            "`SelectMany` **flattens** nested collections — each outer element maps to a sequence, and all sequences concatenate into one. "
            "Classic use: orders with line items → all line items across orders. "
            "Overload with **result selector** `(outer, inner) => result` builds pairs without a separate `Join`. "
            "Cartesian products are possible when the inner selector ignores the outer element. "
            "EF Core translates many `SelectMany` patterns via SQL joins or subqueries."
        ),
        "code": """// Flatten line items from all orders
var allLines = orders.SelectMany(o => o.LineItems);

// Pair cities with countries (cartesian if misused)
var pairs = cities.SelectMany(
    c => countries,
    (city, country) => new { city.Name, country.Name });

// Left join flatten pattern
var flat = customers
    .SelectMany(c => c.Orders.DefaultIfEmpty(),
        (c, o) => new { c.Name, Total = o?.Total });""",
        "language": "csharp",
        "key_points": [
            "Maps each to sequence then flattens",
            "One-to-many expansion pattern",
            "Result selector overload pairs elements",
            "Can produce cartesian product if careless",
            "EF translates to JOIN or subquery shapes",
        ],
    },
    "linq-aggregate": {
        "explanation": (
            "`Aggregate` **folds** a sequence into a single value using a **func(accumulator, element) => accumulator**. "
            "Without a seed, the **first element** is the initial accumulator — empty sequence throws. "
            "With a seed, empty sequence returns the seed — useful for sums and string builds. "
            "Built-in `Sum`, `Min`, `Max` are optimized aggregates; use `Aggregate` for custom logic (e.g., product, formatted string). "
            "Not all `Aggregate` lambdas translate to SQL — complex folds may force client evaluation."
        ),
        "code": """// Sum without Sum() — seed 0
var total = orders.Select(o => o.Total).Aggregate(0m, (acc, t) => acc + t);

// Build comma-separated string
var csv = names.Aggregate((a, b) => $"{a},{b}");

// Empty behavior
var emptySum = Enumerable.Empty<int>().Aggregate(0, (a, b) => a + b); // 0

// Custom — product
var product = factors.Aggregate(1, (acc, n) => acc * n);""",
        "language": "csharp",
        "key_points": [
            "Fold sequence to single value",
            "Seed overload handles empty sequences",
            "No seed uses first element — throws if empty",
            "Custom logic when Sum/Min not enough",
            "Complex Aggregate may not translate to SQL",
        ],
    },
    "linq-sum-avg-min-max": {
        "explanation": (
            "`Sum`, `Average`, `Min`, and `Max` are **standard numeric aggregates** with immediate execution. "
            "They accept optional selectors to aggregate a property (`Sum(o => o.Total)`). "
            "Empty sequence behavior: `Sum` returns **0** for numeric types; `Min`/`Max`/`Average` **throw** on empty non-nullable sequences. "
            "Nullable overloads (`Average` on `int?`) return **null** when empty. "
            "EF Core maps these directly to SQL aggregate functions — always prefer SQL-side aggregation over client `ToList().Sum()`."
        ),
        "code": """decimal total = orders.Sum(o => o.Total);
double average = orders.Average(o => o.Total);
decimal max = orders.Max(o => o.Total);
int minId = orders.Min(o => o.Id);

// Empty throws for Min on non-nullable
try { Enumerable.Empty<int>().Min(); } catch (InvalidOperationException) { }

// EF — one query with multiple aggregates
var stats = db.Orders
    .GroupBy(o => o.Status)
    .Select(g => new
    {
        g.Key,
        Total = g.Sum(o => o.Total),
        Avg = g.Average(o => o.Total)
    });""",
        "language": "csharp",
        "key_points": [
            "Immediate numeric aggregates",
            "Selector overload projects property first",
            "Empty Min/Max/Average throw (non-nullable)",
            "Sum returns zero for empty numeric",
            "EF → SQL SUM, AVG, MIN, MAX",
        ],
    },
    "linq-oftype-cast": {
        "explanation": (
            "`OfType<T>` filters elements **assignable to T**, skipping incompatible types **without throwing**. "
            "`Cast<T>` assumes **every** element is `T` and throws `InvalidCastException` on the first mismatch. "
            "Common with **non-generic** collections, `object[]`, or UI element trees mixing types. "
            "`OfType` is safer for **heterogeneous** sequences; `Cast` is fine when you know the exact runtime type. "
            "Neither is needed often with generic `IEnumerable<T>` — mainly legacy APIs and polymorphic lists."
        ),
        "code": """object[] mixed = { 1, "two", 3, "four" };

var intsSafe = mixed.OfType<int>();   // 1, 3
var intsStrict = mixed.Cast<int>();   // throws on "two"

// Polymorphic collection
List<Animal> animals = new() { new Dog(), new Cat(), new Dog() };
var dogs = animals.OfType<Dog>().ToList();""",
        "language": "csharp",
        "key_points": [
            "OfType filters matching types — no throw",
            "Cast requires all elements compatible",
            "Use OfType on heterogeneous sequences",
            "Common with object[] and legacy APIs",
            "Generic IEnumerable<T> rarely needs either",
        ],
    },
    "linq-defaultifempty": {
        "explanation": (
            "`DefaultIfEmpty` returns the original sequence if it has elements; if **empty**, returns a **single-element** sequence containing `default(T)` or a provided **default value**. "
            "Essential in **left outer join** flattening — when `GroupJoin` yields an empty inner group, `DefaultIfEmpty` supplies one null placeholder for `SelectMany`. "
            "For reference types, default is **null**; for value types, **0/false** unless you pass a custom default. "
            "Do not use expecting to replace null **elements** inside a non-empty sequence — only handles **empty** sequences."
        ),
        "code": """// Empty sequence → single default
var zeroOrValues = numbers.Where(n => n > 100).DefaultIfEmpty(0);

// Left join flatten
var leftJoin = customers.GroupJoin(orders,
    c => c.Id, o => o.CustomerId,
    (c, og) => new { c, og })
    .SelectMany(x => x.og.DefaultIfEmpty(),
        (x, o) => new
        {
            x.c.Name,
            OrderTotal = o?.Total ?? 0m
        });

var first = names.Where(n => n.StartsWith("Z")).DefaultIfEmpty("none").First();""",
        "language": "csharp",
        "key_points": [
            "Empty sequence → one default element",
            "Critical for left outer join pattern",
            "Optional default value parameter",
            "Does not replace nulls inside sequence",
            "Reference types default to null",
        ],
    },
    "linq-zip": {
        "explanation": (
            "`Zip` pairs elements from **two sequences by position** — first with first, second with second — not by key like `Join`. "
            "Stops when **either** sequence ends — length is `min(count1, count2)`. "
            ".NET 6+ adds overload returning `(TFirst, TSecond)` tuples without a result selector. "
            "Use for **parallel arrays**, aligning streams, or combining indexed data — not relational joins. "
            "No EF SQL equivalent for general Zip — typically in-memory."
        ),
        "code": """var names = new[] { "Alice", "Bob", "Carol" };
var scores = new[] { 95, 87, 92 };

// Classic Zip with result selector
var report = names.Zip(scores, (name, score) => $"{name}: {score}");

// .NET 6+ tuple Zip
foreach (var (name, score) in names.Zip(scores))
    Console.WriteLine($"{name} {score}");

// Third sequence shorter — Zip stops at 2 pairs
var short = names.Zip(new[] { 1, 2 });""",
        "language": "csharp",
        "key_points": [
            "Pairs by index position — not key",
            "Length = shorter of two sequences",
            "Result selector builds combined shape",
            ".NET 6+ tuple Zip overload",
            "In-memory — not a SQL JOIN",
        ],
    },
    "linq-chunk": {
        "explanation": (
            "`Chunk` (.NET 6+) splits a sequence into **batches** of at most `size` elements — the last chunk may be smaller. "
            "Ideal for **batch processing**: bulk inserts, API calls with size limits, parallel workers per batch. "
            "Deferred — chunks are `IEnumerable<T>` views, not copies until enumerated (except materialization of each array chunk). "
            "Returns `IEnumerable<T[]>` — each chunk is an **array**. "
            "Alternative before Chunk: manual loops or custom `Batch` extension."
        ),
        "code": """var ids = Enumerable.Range(1, 250);

foreach (var batch in ids.Chunk(100))
{
  // batch is int[] — length 100, 100, 50
  await db.BulkInsertAsync(batch);
}

// Process orders in batches to limit memory
foreach (var batch in orders.Chunk(50))
{
    foreach (var order in batch)
        Process(order);
}""",
        "language": "csharp",
        "key_points": [
            ".NET 6+ Chunk operator",
            "Splits into arrays of max size",
            "Last chunk may be smaller",
            "Batch processing and bulk APIs",
            "Deferred enumeration of chunks",
        ],
    },
    "linq-tolist-toarray": {
        "explanation": (
            "`ToList` and `ToArray` **materialize** a sequence into a concrete collection — execution happens **immediately**. "
            "`List<T>` is resizable and slightly heavier; `T[]` is fixed-size and can be slightly more efficient for known-size storage. "
            "Use materialization to **avoid multiple enumeration**, snapshot mutable sources, or pass to APIs requiring `List<T>`. "
            "On EF, `ToListAsync` triggers **one SQL query** and closes the data reader. "
            "**Trap:** `ToList()` before `Where` on IQueryable pulls **all rows** — filter first."
        ),
        "code": """// Correct — filter in SQL, then materialize
var openOrders = db.Orders
    .Where(o => o.Status == "Open")
    .OrderBy(o => o.Date)
    .ToList();

// BAD — pulls entire table
var bad = db.Orders.ToList().Where(o => o.Total > 100);

var arr = Enumerable.Range(1, 5).ToArray(); // int[5]
var list = arr.ToList(); // copy to List<int>""",
        "language": "csharp",
        "key_points": [
            "Terminal operators — immediate execution",
            "Snapshot sequence — stable for reuse",
            "ToList vs ToArray — resize vs fixed",
            "EF ToListAsync = one database round-trip",
            "Never ToList before Where on IQueryable",
        ],
    },
    "linq-asenumerable": {
        "explanation": (
            "`AsEnumerable()` returns `IEnumerable<T>` wrapping the source — it is a **no-op** for in-memory collections but signals **switch from IQueryable to IEnumerable** extension methods. "
            "After `AsEnumerable`, subsequent operators use **LINQ to Objects** — predicates compile to delegates and run **in CLR memory**. "
            "Use when you need **non-translatable** logic (custom C# methods) on data already partially filtered in SQL. "
            "**Danger:** calling `AsEnumerable()` too early on `IQueryable` forces **client evaluation** of everything after it — can load millions of rows. "
            "Prefer translating filters to SQL; use `AsEnumerable` only after narrowing in the database."
        ),
        "code": """// Filter in SQL first, then client-only logic
var result = db.Orders
    .Where(o => o.Status == "Open")     // SQL
    .AsEnumerable()
    .Where(o => ComplexRules(o))        // CLR — not translatable
    .ToList();

// Without AsEnumerable, ComplexRules in SQL Where throws at runtime

// IEnumerable.AsEnumerable is identity — no copy
var list = new List<int> { 1, 2, 3 };
var same = list.AsEnumerable(); // same reference iteration""",
        "language": "csharp",
        "key_points": [
            "Switches IQueryable pipeline to in-memory",
            "Enables non-translatable predicates",
            "Calling too early pulls excessive data",
            "Filter in SQL before AsEnumerable",
            "Identity on plain IEnumerable",
        ],
    },
    "linq-extension-methods": {
        "explanation": (
            "LINQ operators are **static extension methods** on `Enumerable` (IEnumerable) and `Queryable` (IQueryable) in `System.Linq`. "
            "Signature pattern: `public static IEnumerable<T> Op<T>(this IEnumerable<T> source, ...)`. "
            "The `this` on the first parameter enables `source.Where(...)` call syntax. "
            "Custom operators follow the same pattern — extend `IEnumerable<T>` with deferred `yield return` iterators. "
            "**Interview:** extension methods require `using System.Linq` and a static class — they do not modify the original type."
        ),
        "code": """// How Where is conceptually implemented (simplified)
public static class EnumerableExtensions
{
    public static IEnumerable<T> MyWhere<T>(
        this IEnumerable<T> source,
        Func<T, bool> predicate)
    {
        foreach (var item in source)
            if (predicate(item))
                yield return item;
    }
}

// Usage — extension call
var evens = Enumerable.Range(1, 10).MyWhere(n => n % 2 == 0);

// Queryable mirrors Enumerable with Expression parameters""",
        "language": "csharp",
        "key_points": [
            "Static classes Enumerable and Queryable",
            "this parameter enables dot syntax",
            "Custom operators use same pattern",
            "yield return for deferred custom ops",
            "Queryable uses Expression<Func<>> variants",
        ],
    },
    "linq-into-let": {
        "explanation": (
            "`let` in query syntax introduces an **intermediate range variable** — like assigning a subexpression reused in `where` or `select`. "
            "Compiler rewrites `let` to a **Select** that projects an anonymous type carrying the new value. "
            "`into` after `group` or `join` **renames** the group/join result and continues the query with a new scope. "
            "Example: `group o by o.Status into g` lets you `select g.Count()` where `g` is the group. "
            "Method syntax equivalent often uses anonymous types or nested queries — `let`/`into` improve readability."
        ),
        "code": """// let — computed value in pipeline
var q1 = from o in orders
         let tax = o.Total * 0.2m
         where tax > 50
         select new { o.Id, o.Total, tax };

// into — continue after group
var q2 = from o in orders
         group o by o.Status into g
         where g.Count() > 5
         select new { Status = g.Key, Count = g.Count() };

// join into
var q3 = from c in customers
         join o in orders on c.Id equals o.CustomerId into customerOrders
         select new { c.Name, OrderCount = customerOrders.Count() };""",
        "language": "csharp",
        "key_points": [
            "let assigns intermediate range variable",
            "into continues query after group/join",
            "Compiler rewrites to method calls",
            "Improves readability for complex queries",
            "where after into filters groups",
        ],
    },
    "linq-expression-trees": {
        "explanation": (
            "An **expression tree** is a **data structure** representing code (nodes for parameters, constants, method calls) rather than compiled IL. "
            "`Expression<Func<T,bool>>` looks like a lambda but is **inspectable** — EF Core walks the tree to build SQL. "
            "`Func<T,bool>` is a **compiled delegate** — opaque to providers, runs only in memory. "
            "You can **compose** expression trees manually with `Expression.Parameter`, `Expression.Property`, etc. "
            "**Trap:** assigning expression lambda to `Func<>` or calling `Compile()` before the provider sees it loses translatability."
        ),
        "code": """// Expression tree — code as data
Expression<Func<Order, bool>> expr = o => o.Total > 100 && o.IsActive;

// Inspect nodes
Console.WriteLine(expr.Body); // (o.Total > 100) AndAlso o.IsActive

// Func — compiled, not translatable by EF
Func<Order, bool> func = o => o.Total > 100;
// db.Orders.Where(func) — may throw or client-eval depending on provider

// Manual composition
var param = Expression.Parameter(typeof(Order), "o");
var prop = Expression.Property(param, nameof(Order.Total));
var gt = Expression.GreaterThan(prop, Expression.Constant(100m));
var lambda = Expression.Lambda<Func<Order, bool>>(gt, param);""",
        "language": "csharp",
        "key_points": [
            "Expression<T> is code as data structure",
            "IQueryable providers parse trees to SQL",
            "Func delegates are compiled IL — opaque",
            "Do not Compile() before provider translation",
            "Manual composition for dynamic type-safe queries",
        ],
    },
    "linq-providers": {
        "explanation": (
            "A **LINQ provider** implements `IQueryProvider` and `IQueryable` to execute queries against a **specific data store**. "
            "`EnumerableQuery` (LINQ to Objects) compiles expression trees to delegates and runs in memory. "
            "**EF Core** provider translates to SQL and executes on the database. "
            "Providers differ in **what expressions they can translate** — unsupported ops throw or silently client-evaluate (older EF). "
            "**Interview:** mention provider-specific behavior — same LINQ syntax, different execution semantics."
        ),
        "code": """// LINQ to Objects — EnumerableQuery provider
IEnumerable<int> mem = new[] { 1, 2, 3 }.Where(x => x > 1);

// EF Core — relational provider
await using var db = new AppDbContext();
IQueryable<Order> remote = db.Orders.Where(o => o.Total > 100);

// Provider executes on ToListAsync
var orders = await remote.ToListAsync();

// IQueryable exposes Provider
IQueryProvider provider = remote.Provider;""",
        "language": "csharp",
        "key_points": [
            "IQueryProvider executes expression trees",
            "EF Core, XML, OData are different providers",
            "Translation capabilities vary per provider",
            "Same syntax — different execution backends",
            "Enumerable provider compiles to delegates",
        ],
    },
    "linq-to-objects-patterns": {
        "explanation": (
            "Beyond basic operators, production code uses **terminal conversions** that build useful data structures. "
            "`ToLookup` groups into **ILookup** — multiple values per key, always safe for missing keys. "
            "`ToDictionary` requires **unique keys** — throws on duplicates unless you handle conflicts. "
            "`ToHashSet` dedupes with set semantics; **immutable** collections (`ToImmutableList`) for thread-safe snapshots. "
            "These materialize — run once after filtering, not on every access."
        ),
        "code": """var orders = GetOrders();

// Lookup — group by customer, O(1) key access
ILookup<int, Order> byCustomer = orders.ToLookup(o => o.CustomerId);
var customerOrders = byCustomer[42]; // empty if none — no throw

// Dictionary — unique key required
var byId = orders.ToDictionary(o => o.Id);

// HashSet for distinct codes
var codes = orders.Select(o => o.Code).ToHashSet();

// Immutable snapshot
var snapshot = orders.ToImmutableList();""",
        "language": "csharp",
        "key_points": [
            "ToLookup — safe multi-value per key",
            "ToDictionary — unique keys required",
            "ToHashSet for distinct set semantics",
            "Immutable collections for snapshots",
            "Materialize after filtering source",
        ],
    },
    "linq-ef-core-sql": {
        "explanation": (
            "EF Core's **IQueryable provider** parses expression trees into a **SQL model**, then generates provider-specific SQL (SQL Server, PostgreSQL, etc.). "
            "Operators like `Where`, `Select`, `OrderBy`, `Join`, `GroupBy`, and aggregates usually translate when expressions use **mapped properties**. "
            "**Not everything translates** — arbitrary C# methods, `string.Format` in some cases, or `Include` misuse cause exceptions or client eval. "
            "Use **`ToQueryString()`** (EF5+) or logging (`LogTo`) to inspect generated SQL during development. "
            "**Interview:** push work to SQL — filter, project, aggregate server-side; minimize `ToList()` early."
        ),
        "code": """var query = db.Orders
    .Where(o => o.Total > 100 && o.Status == "Open")
    .OrderByDescending(o => o.Date)
    .Select(o => new { o.Id, o.Total });

// Inspect SQL without executing
var sql = query.ToQueryString();
Console.WriteLine(sql);

// Execute — one round-trip
var results = await query.ToListAsync();

// Navigation — translated join
var withCustomer = db.Orders
    .Select(o => new { o.Id, o.Customer.Name });""",
        "language": "csharp",
        "key_points": [
            "Expression trees → SQL via EF provider",
            "Filter and project in SQL for performance",
            "Not all C# expressions translate",
            "ToQueryString / logging for debugging",
            "Avoid premature ToList on DbSet",
        ],
    },
    "linq-compiled-queries": {
        "explanation": (
            "**Compiled queries** cache the **query expression** and delegate generation so repeated execution skips re-parsing the tree. "
            "EF Core: `EF.CompileAsyncQuery` / `EF.CompileQuery` returns a func `(DbContext, params) => IQueryable or result`. "
            "Benefit is **micro-optimization** — meaningful in hot paths with simple repeated queries, not a substitute for SQL tuning. "
            "Compiled queries are **static** — typically stored in static readonly fields; parameters must be arguments to the compiled func. "
            "Modern EF Core with proper DbContext pooling already optimizes many scenarios — profile before relying on compiled queries."
        ),
        "code": """// Static compiled async query
private static readonly Func<AppDbContext, int, IAsyncEnumerable<Order>> GetOrdersByCustomer =
    EF.CompileAsyncQuery((AppDbContext ctx, int customerId) =>
        ctx.Orders.Where(o => o.CustomerId == customerId));

// Usage
await foreach (var order in GetOrdersByCustomer(db, 42))
    Process(order);

// CompileQuery for synchronous
private static readonly Func<AppDbContext, int, Order?> GetById =
    EF.CompileQuery((AppDbContext ctx, int id) =>
        ctx.Orders.FirstOrDefault(o => o.Id == id));""",
        "language": "csharp",
        "key_points": [
            "Caches query expression processing",
            "EF.CompileQuery / CompileAsyncQuery",
            "Static fields for hot repeated queries",
            "Micro-optimization — profile first",
            "Parameters via compiled func arguments",
        ],
    },
    "linq-dynamic": {
        "explanation": (
            "**Dynamic LINQ** builds predicates or projections from **runtime strings** — common for admin grids with user-chosen filters and sort columns. "
            "Popular package **System.Linq.Dynamic.Core** extends `IQueryable` with `Where('Total > @0', 100)` and dynamic `OrderBy`. "
            "Risks: **injection** if raw user strings hit the parser — whitelist fields and use parameters. "
            "Alternative: manually build **Expression trees** for type-safe dynamic filters (more code, safer). "
            "EF Core does not ship dynamic string LINQ in the box — requires library or custom expressions."
        ),
        "code": """// System.Linq.Dynamic.Core (NuGet)
var field = "Total"; // validate against whitelist!
var q = db.Orders.Where($"{field} > @0", 100);

var sortField = "Date"; // whitelist
var sorted = q.OrderBy(sortField);

// Type-safe dynamic — predicate builder pattern
Expression<Func<Order, bool>> pred = o => o.Status == "Open";
if (minTotal.HasValue)
    pred = pred.And(o => o.Total >= minTotal.Value); // PredicateBuilder lib
var safe = db.Orders.Where(pred);""",
        "language": "csharp",
        "key_points": [
            "String predicates for runtime filters",
            "System.Linq.Dynamic.Core common package",
            "Whitelist fields — injection risk",
            "Expression trees for type-safe alternative",
            "Not built into EF Core natively",
        ],
    },
    "linq-custom-operators": {
        "explanation": (
            "Custom LINQ operators are **extension methods** on `IEnumerable<T>` (or `IQueryable<T>` for advanced cases) following `System.Linq` conventions. "
            "Use **iterator blocks** (`yield return`) for deferred operators that stream without buffering entire input. "
            "Name clearly (`WhereNotNull`, `Batch`, `DistinctBy` before it existed) and document whether execution is deferred or immediate. "
            "For `IQueryable`, custom operators need **`IQueryable` provider support** or they won't translate — usually wrap `AsEnumerable` first. "
            "**Interview:** show you understand LINQ is not magic — it's extensible methods."
        ),
        "code": """public static class LinqExtensions
{
    // Deferred custom Where for non-null
    public static IEnumerable<T> WhereNotNull<T>(
        this IEnumerable<T?> source) where T : class
    {
        foreach (var item in source)
            if (item is not null)
                yield return item;
    }

    // Immediate operator
    public static bool IsEmpty<T>(this IEnumerable<T> source) =>
        !source.Any();
}

// Usage
var names = new List<string?> { "a", null, "b" };
var valid = names.WhereNotNull().ToList();""",
        "language": "csharp",
        "key_points": [
            "Extension methods on IEnumerable",
            "yield return for deferred streaming",
            "Name and document execution mode",
            "IQueryable custom ops rarely translate",
            "Follow System.Linq naming patterns",
        ],
    },
    "linq-performance": {
        "explanation": (
            "LINQ performance hinges on **where** work runs — SQL server vs CLR — and **how often** sequences enumerate. "
            "Filter and project early on `IQueryable`; avoid `ToList()` before filters. "
            "Materialize once when reusing; prefer **dictionaries/lookups** over repeated `FirstOrDefault` in loops. "
            "LINQ adds small delegate overhead — in **hot paths** profile; plain `for` loops may win for tight numeric code. "
            "Use **`ValueTask`/`Span`** outside LINQ for allocation-sensitive paths — LINQ is clarity-first, not always max speed."
        ),
        "code": """// BAD — loads all orders
var bad = db.Orders.ToList().Where(o => o.Total > 1000);

// GOOD — SQL filter
var good = db.Orders.Where(o => o.Total > 1000).ToList();

// Avoid O(n²) — build lookup once
var orderLookup = orders.ToLookup(o => o.CustomerId);
foreach (var c in customers)
{
    var custOrders = orderLookup[c.Id]; // O(1) key
}

// Profile hot path — loop may beat LINQ
decimal sum = 0;
for (int i = 0; i < values.Length; i++)
    sum += values[i];""",
        "language": "csharp",
        "key_points": [
            "Filter in database before materialize",
            "Materialize once — avoid double enumeration",
            "Lookup/Dictionary beats repeated scans",
            "Profile hot paths — loops may win",
            "Do not call AsEnumerable early",
        ],
    },
    "linq-multiple-enumeration": {
        "explanation": (
            "A **deferred** LINQ query **re-runs** every time you enumerate — `foreach`, `ToList`, `Count`, etc. "
            "If the pipeline is expensive (database, network, heavy CPU filter), **double enumeration doubles cost**. "
            "Fix: **materialize** with `ToList`/`ToArray` once, or cache in a field. "
            "Special case: **`IEnumerator` from GetEnumerator()`** is single-pass — second foreach on some custom iterators may fail or skip. "
            "**IQueryable:** `Count()` then `ToList()` issues **two SQL queries** — materialize or use one query."
        ),
        "code": """var query = orders.Where(o => ExpensiveCheck(o)); // deferred

// DOUBLE WORK
int n = query.Count();    // full pass 1
var list = query.ToList(); // full pass 2

// FIX — materialize once
var materialized = orders.Where(o => ExpensiveCheck(o)).ToList();
int n2 = materialized.Count;
var copy = materialized.ToList(); // cheap — already list

// IQueryable double round-trip
var q = db.Orders.Where(o => o.IsActive);
var c = q.Count();       // SQL 1
var all = q.ToList();    // SQL 2 — use ToList once instead""",
        "language": "csharp",
        "key_points": [
            "Deferred queries re-execute each enumeration",
            "Expensive pipelines need materialization",
            "IQueryable multiple terminals = multiple SQL",
            "ToList once then reuse collection",
            "Some iterators are single-pass only",
        ],
    },
    "linq-null-handling": {
        "explanation": (
            "LINQ operators generally **do not filter nulls** unless your predicate does — `Select` may propagate null references. "
            "Use **`Where(x => x is not null)`** or custom `WhereNotNull` before operations that reject nulls. "
            "`FirstOrDefault` returns **default** (null for references) — distinguish missing from found via null check. "
            "Nullable value types (`int?`) work in projections; `Where` on nullable needs explicit `HasValue` checks when required. "
            "EF Core null semantics mirror SQL **three-valued logic** — `== null` translates to `IS NULL`."
        ),
        "code": """List<string?> tags = new() { "a", null, "b" };

// Filter nulls before use
var clean = tags.Where(t => t is not null).Select(t => t!.ToUpper());

// FirstOrDefault — null means not found
var order = orders.FirstOrDefault(o => o.Id == id);
if (order is null) return NotFound();

// Nullable value type
int? maybe = orders.Select(o => o.Discount).FirstOrDefault();
if (maybe.HasValue) ApplyDiscount(maybe.Value);

// EF null check
var q = db.Orders.Where(o => o.ShipDate == null); // IS NULL""",
        "language": "csharp",
        "key_points": [
            "LINQ does not auto-exclude null elements",
            "WhereNotNull before dependent operations",
            "FirstOrDefault null = not found",
            "Nullable types use HasValue checks",
            "EF null compares translate to IS NULL",
        ],
    },
    "linq-plinq": {
        "explanation": (
            "**PLINQ** (Parallel LINQ) partitions work across threads via `AsParallel()` on `IEnumerable<T>`. "
            "Best for **CPU-bound** operations on large in-memory collections — not for I/O or small data sets. "
            "`WithDegreeOfParallelism` caps thread count; `AsOrdered()` preserves order at a cost. "
            "Operators run **concurrently** — side effects and non-thread-safe collections are dangerous. "
            "Default `AsParallel()` does **not** guarantee original order; merging is faster without ordering."
        ),
        "code": """var results = Enumerable.Range(1, 1_000_000)
    .AsParallel()
    .WithDegreeOfParallelism(Environment.ProcessorCount)
    .Where(n => IsPrime(n))           // CPU-heavy
    .Take(100)
    .ToList();

// Preserve order — slower
var ordered = items.AsParallel().AsOrdered().Select(Transform).ToList();

// PLINQ on EF query — must materialize first
var scored = db.Orders.ToList() // SQL once
    .AsParallel()
    .Select(o => Score(o))
    .ToList();""",
        "language": "csharp",
        "key_points": [
            "AsParallel for CPU-bound in-memory work",
            "Not for I/O or EF — materialize first",
            "WithDegreeOfParallelism controls threads",
            "AsOrdered preserves order at cost",
            "Thread safety required for shared state",
        ],
    },
    "linq-pitfalls": {
        "explanation": (
            "Top interview traps: **client evaluation** after `ToList()` pulls entire tables; **multiple enumeration** doubles work; "
            "modifying a collection **during iteration**; using `Single` when duplicates exist; `First` without `OrderBy` on SQL. "
            "Assuming **query syntax** is more efficient than methods — identical IL. "
            "Hidden **` IEnumerable` assignment** on `IQueryable` loses SQL optimizations. "
            "Calling **non-translatable** methods in EF predicates causes runtime exceptions or silent perf disasters in older stacks."
        ),
        "code": """// Pitfall 1 — client eval loads everything
var pit1 = db.Orders.ToList().Where(o => o.Total > 100);

// Pitfall 2 — modify while iterating
foreach (var o in list.Where(x => x.Invalid))
    list.Remove(o); // InvalidOperationException

// Pitfall 3 — Single when duplicates possible
// users.Single(u => u.Email == email) — throws if duplicates

// Pitfall 4 — IQueryable hidden as IEnumerable
IEnumerable<Order> hidden = db.Orders.Where(o => o.IsActive);
// Next Where runs client-side if not IQueryable

// Fix pitfalls
var fix = db.Orders.Where(o => o.Total > 100).ToList();
var toRemove = list.Where(x => x.Invalid).ToList();
foreach (var x in toRemove) list.Remove(x);""",
        "language": "csharp",
        "key_points": [
            "ToList before filter — client eval trap",
            "Never modify collection during foreach",
            "Single vs First — know throw conditions",
            "Do not hide IQueryable as IEnumerable",
            "Query vs method syntax — same performance",
        ],
    },
}


def apply_linq_section(sections: dict, detailed: dict) -> None:
    """Register the LINQ section, project topics, and merge detailed content."""
    from data.linq_project_topics import extend_linq_section

    sections["linq"] = LINQ_SECTION
    detailed.update(LINQ_DETAILED)
    extend_linq_section(LINQ_SECTION, detailed)

