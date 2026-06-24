"""Additional Core .NET interview topics (2025/2026) — expands dotnet section."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("dotnet", "foundation"): [
        InterviewItem(
            "boxing-unboxing",
            "What is boxing and unboxing in C# and why does it matter?",
            "See detailed explanation.",
            """int n = 42;
object boxed = n;   // boxing — heap allocation
int unboxed = (int)boxed;""",
            key_points=["Value type → object on heap", "Avoid in hot loops", "Generics avoid boxing"],
        ),
        InterviewItem(
            "stack-vs-heap",
            "Explain stack vs heap memory in .NET.",
            "See detailed explanation.",
            """int x = 10;              // stack
var order = new Order();   // object on heap, reference on stack""",
            key_points=["Stack = value types + frames", "Heap = GC-managed objects", "ref struct stack-only"],
        ),
        InterviewItem(
            "readonly-const",
            "What is the difference between const and readonly in C#?",
            "See detailed explanation.",
            """public const int MaxItems = 100;
public readonly DateTime Created = DateTime.UtcNow;""",
            key_points=["const compile-time", "readonly set once", "static readonly for static fields"],
        ),
        InterviewItem(
            "primary-constructors",
            "What are C# 12 primary constructors and when use them?",
            "See detailed explanation.",
            """public class OrderService(IOrderRepository repo, ILogger<OrderService> log)
{
    public async Task<Order?> GetAsync(int id) => await repo.GetByIdAsync(id);
}""",
            key_points=["C# 12 feature", "DI-friendly", "Records had them earlier"],
        ),
        InterviewItem(
            "attributes",
            "What are C# attributes and common use cases?",
            "See detailed explanation.",
            """[Authorize(Roles = "Admin")]
[HttpGet("{id}")]
public IActionResult Get(int id) => Ok();""",
            key_points=["Metadata via reflection", "Validation attributes", "Source generators read them"],
        ),
        InterviewItem(
            "top-level-statements",
            "What are top-level statements in modern C#?",
            "See detailed explanation.",
            """// Program.cs — no explicit Main required
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.MapGet("/", () => "Hello");
app.Run();""",
            key_points=["C# 9+", "Compiler generates Main", "One file per project"],
        ),
        InterviewItem(
            "global-usings",
            "How do global usings work in C#?",
            "See detailed explanation.",
            """// GlobalUsings.cs
global using System.Collections.Generic;
global using Microsoft.Extensions.Logging;""",
            key_points=["Reduce boilerplate", "Implicit usings in SDK", "Project-wide scope"],
        ),
    ],
    ("dotnet", "intermediate"): [
        InterviewItem(
            "linq-deferred-execution",
            "What is LINQ deferred execution?",
            "See detailed explanation.",
            """var query = orders.Where(o => o.Total > 100); // not executed yet
var list = query.ToList(); // executes now""",
            key_points=["IEnumerable pipeline", "Executes on enumeration", "Multiple enumerations re-run"],
        ),
        InterviewItem(
            "ienumerable-vs-iqueryable",
            "IEnumerable<T> vs IQueryable<T> — when use each?",
            "See detailed explanation.",
            """IQueryable<Order> q = db.Orders.Where(o => o.Status == "Open");
IEnumerable<Order> mem = orders.Where(o => o.Total > 50);""",
            key_points=["IQueryable = expression trees", "Remote vs in-memory", "EF Core uses IQueryable"],
        ),
        InterviewItem(
            "yield-return",
            "How does yield return work in C#?",
            "See detailed explanation.",
            """IEnumerable<int> GetNumbers()
{
    for (int i = 0; i < 10; i++)
        yield return i;
}""",
            key_points=["Lazy iteration", "State machine codegen", "Avoid materializing large lists"],
        ),
        InterviewItem(
            "json-serialization",
            "How does System.Text.Json compare to Newtonsoft.Json?",
            "See detailed explanation.",
            """var json = JsonSerializer.Serialize(dto, new JsonSerializerOptions
{
    PropertyNamingPolicy = JsonNamingPolicy.CamelCase
});""",
            key_points=["Built-in and fast", "Source generators", "Newtonsoft for legacy features"],
        ),
        InterviewItem(
            "init-only-setters",
            "What are init-only setters in C#?",
            "Init-only setters (C# 9) assign properties only during object initialization, then become read-only.",
            """public class OrderDto
{
    public int Id { get; init; }
    public string Customer { get; init; } = "";
    public decimal Total { get; init; }
}

var order = new OrderDto { Id = 1, Customer = "Alice", Total = 99.99m };
// order.Total = 50; // COMPILE ERROR — init-only after construction""",
            key_points=[
                "C# 9 — set only during initialization",
                "Works with object initializers and constructors",
                "init vs readonly vs set — know the difference",
                "Ideal for DTOs, records, immutable domain models",
                "Compiler-enforced; reflection may bypass",
            ],
        ),
        InterviewItem(
            "required-members",
            "What are required members in C# 11+?",
            "See detailed explanation.",
            """public class CreateOrderDto
{
    public required string CustomerName { get; init; }
    public required int Quantity { get; init; }
}""",
            key_points=["Compiler enforces init", "Object initializer required", "API contract clarity"],
        ),
        InterviewItem(
            "configuration-binding",
            "How does IOptions and configuration binding work?",
            "See detailed explanation.",
            """builder.Services.Configure<JwtOptions>(builder.Configuration.GetSection("Jwt"));
public class AuthService(IOptions<JwtOptions> options) { }""",
            key_points=["IOptions vs IOptionsSnapshot", "ValidateOnStart", "Bind POCOs from appsettings"],
        ),
    ],
    ("dotnet", "advanced"): [
        InterviewItem(
            "expression-trees",
            "What are expression trees in C#?",
            "See detailed explanation.",
            """Expression<Func<Order, bool>> expr = o => o.Total > 100;
// EF Core translates to SQL""",
            key_points=["Code as data", "IQueryable provider", "Not same as delegates"],
        ),
        InterviewItem(
            "reflection",
            "When and how do you use reflection in .NET?",
            "See detailed explanation.",
            """var method = typeof(OrderService).GetMethod("Process");
method?.Invoke(instance, [orderId]);""",
            key_points=["Runtime type inspection", "Performance cost", "Prefer source generators"],
        ),
        InterviewItem(
            "parallel-linq",
            "What is Parallel LINQ (PLINQ) and when use it?",
            "See detailed explanation.",
            """var results = items.AsParallel()
    .Where(x => HeavyFilter(x))
    .ToList();""",
            key_points=["CPU-bound parallelism", "WithDegreeOfParallelism", "Order not guaranteed"],
        ),
        InterviewItem(
            "concurrent-dictionary",
            "How does ConcurrentDictionary<TKey,TValue> work?",
            "See detailed explanation.",
            """var cache = new ConcurrentDictionary<string, byte[]>();
cache.GetOrAdd(key, k => LoadBytes(k));""",
            key_points=["Thread-safe without locks", "GetOrAdd atomic", "Fine-grained locking"],
        ),
        InterviewItem(
            "interlocked",
            "What is Interlocked and when use it over lock?",
            "See detailed explanation.",
            """Interlocked.Increment(ref _counter);
Interlocked.CompareExchange(ref _flag, 1, 0);""",
            key_points=["Atomic primitives", "Counters and flags", "Faster than lock for simple ops"],
        ),
        InterviewItem(
            "memory-cache",
            "How do you use IMemoryCache in .NET?",
            "See detailed explanation.",
            """cache.Set("catalog", data, new MemoryCacheEntryOptions
{
    AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5)
});""",
            key_points=["AddMemoryCache()", "Expiration policies", "IDistributedCache for scale-out"],
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "boxing-unboxing": {
        "explanation": (
            "**Boxing** converts a **value type** (int, struct) into a **reference type** (`object` or interface) by copying the value onto the **heap** and wrapping it. "
            "**Unboxing** extracts the value back with an explicit cast, which throws **InvalidCastException** if the type is wrong. "
            "Boxing causes **heap allocations** and hurts performance in tight loops — a common interview trap with non-generic collections like `ArrayList`. "
            "**Generics** (`List<int>`) eliminate boxing for value types because the JIT generates specialized code. "
            "Modern APIs prefer `Span<T>`, generics, and interfaces constrained to structs (`where T : struct`) to stay allocation-free. "
            "**Interview tip:** mention that `object.Equals` on value types may box when comparing through interfaces."
        ),
        "code": """// Boxing — implicit conversion value → object (heap alloc)
int count = 42;
object boxed = count;

// Unboxing — explicit cast back to value type
int restored = (int)boxed;

// BAD — boxing in a hot loop with non-generic collection
var list = new ArrayList();
for (int i = 0; i < 1_000_000; i++)
    list.Add(i); // each Add boxes int

// GOOD — generics avoid boxing
var generic = new List<int>();
for (int i = 0; i < 1_000_000; i++)
    generic.Add(i); // no boxing""",
        "language": "csharp",
        "key_points": [
            "Boxing copies value type to heap as object",
            "Unboxing requires correct type cast",
            "Generics eliminate boxing for value types",
            "Avoid non-generic collections in performance paths",
            "Nullable value types (int?) also box when cast to object",
        ],
    },
    "stack-vs-heap": {
        "explanation": (
            "The **stack** stores **value types**, method parameters, and return addresses — allocated in **LIFO** order and freed automatically when a method returns. "
            "The **heap** stores **reference type** instances; variables on the stack hold **references** (pointers) to heap objects managed by the **GC**. "
            "Value types declared as **fields of a class** live on the heap with the object; **local value types** typically live on the stack. "
            "`ref struct` types (e.g., `Span<T>`) are **stack-only** and cannot be boxed or stored on the heap — critical for high-performance code. "
            "**Interview angle:** large structs copied by value can be expensive; prefer `readonly struct` or `ref`/`in` parameters. "
            "Understanding stack vs heap explains **GC pressure**, **allocation patterns**, and why `stackalloc` avoids heap for small buffers."
        ),
        "code": """// Local value type — typically stack-allocated
int total = 0;

// Reference type — object on heap, reference on stack
var order = new Order { Id = 1, Total = 99.99m };

// Value type as class field — lives on heap with the object
public class Cart
{
    public int ItemCount; // on heap as part of Cart instance
}

// stackalloc — buffer on stack (no GC)
Span<byte> buffer = stackalloc byte[256];

// ref struct — must stay on stack
public readonly ref struct Point
{
    public Point(int x, int y) { X = x; Y = y; }
    public int X { get; }
    public int Y { get; }
}""",
        "language": "csharp",
        "key_points": [
            "Stack = automatic, fast, per-thread frames",
            "Heap = GC-managed reference type instances",
            "Class fields (even value types) live on heap",
            "ref struct is stack-only — no boxing",
            "Reduce heap allocations to lower GC pauses",
        ],
    },
    "readonly-const": {
        "explanation": (
            "`const` fields are **compile-time constants** — the value is **inlined** at every use site and must be a type the compiler can evaluate (primitives, strings, null). "
            "`readonly` instance fields are set **once** — in the field initializer or constructor — and evaluated at **runtime**. "
            "`static readonly` is the static equivalent; common for `DateTime.UtcNow` or configuration loaded at startup. "
            "**Key difference:** changing a `const` requires **recompiling all consumers** because values are baked in; `readonly` changes affect only the declaring assembly at runtime. "
            "Use `const` for true mathematical constants (`Math.PI` pattern); use `readonly` for instance-specific or runtime values. "
            "**Pitfall:** `const string` in a public API is part of the binary contract — changing it is a breaking change for callers."
        ),
        "code": """public class PricingRules
{
    // Compile-time constant — inlined wherever used
    public const int MaxDiscountPercent = 50;

    // Runtime constant — set once per instance
    public readonly DateTime EffectiveFrom;

  public PricingRules(DateTime effectiveFrom)
    {
        EffectiveFrom = effectiveFrom;
    }

    // static readonly — set once per type
    public static readonly string DefaultCurrency = "USD";
}

// const must be compile-time evaluable
public const double TaxRate = 0.08;
// public const DateTime Now = DateTime.Now; // ERROR — not compile-time""",
        "language": "csharp",
        "key_points": [
            "const = compile-time, inlined into callers",
            "readonly = set once at runtime (ctor or initializer)",
            "static readonly for per-type runtime constants",
            "Changing const requires recompiling dependents",
            "Use readonly for values not known at compile time",
        ],
    },
    "primary-constructors": {
        "explanation": (
            "**Primary constructors** (C# 12) declare constructor parameters **directly on the type** — for classes, structs, and records — reducing boilerplate field assignments. "
            "Parameters are **in scope throughout the type body** and can be captured by methods; the compiler generates a constructor that assigns them if needed. "
            "They pair naturally with **dependency injection** — `public class OrderService(IOrderRepository repo)` is equivalent to manual constructor injection. "
            "For **records**, primary constructors have existed since C# 9 and also generate positional properties. "
            "**Caution:** primary constructor parameters on classes are **not automatically exposed as properties** unless you declare them — unlike records. "
            "**Interview tip:** distinguish class primary constructors (DI sugar) from record positional syntax (DTOs with value equality)."
        ),
        "code": """// C# 12 — class with primary constructor (DI-friendly)
public class OrderService(IOrderRepository repo, ILogger<OrderService> log)
{
    public async Task<Order?> GetAsync(int id)
    {
        log.LogInformation("Fetching order {Id}", id);
        return await repo.GetByIdAsync(id);
    }
}

// Record — primary ctor creates positional properties
public record OrderDto(int Id, string Customer, decimal Total);

// Explicit property from primary ctor parameter (class)
public class CustomerService(string connectionString)
{
    private readonly string _connectionString = connectionString;
    public string ConnectionString => _connectionString;
}""",
        "language": "csharp",
        "key_points": [
            "C# 12 for classes/structs; records since C# 9",
            "Parameters in scope for entire type body",
            "Ideal for constructor injection in services",
            "Records auto-generate properties from parameters",
            "Class parameters are not public properties by default",
        ],
    },
    "attributes": {
        "explanation": (
            "**Attributes** attach **metadata** to assemblies, types, members, or parameters — consumed at **compile time** (source generators, analyzers) or **runtime** (reflection). "
            "Common examples: `[Serializable]`, `[Obsolete]`, validation (`[Required]`, `[Range]`), ASP.NET (`[HttpGet]`, `[Authorize]`), and EF (`[Key]`, `[Column]`). "
            "Attribute classes inherit from `System.Attribute` and use `[AttributeUsage]` to restrict valid targets. "
            "**Data annotations** drive model validation in ASP.NET Core — invalid models return 400 automatically with `[ApiController]`. "
            "Modern .NET favors **compile-time** attributes (`[LoggerMessage]`, `[JsonSerializable]`) processed by source generators for zero-reflection performance. "
            "**Interview tip:** know the difference between declarative metadata (attributes) and imperative logic (validators, middleware)."
        ),
        "code": """// Custom attribute definition
[AttributeUsage(AttributeTargets.Property)]
public class SensitiveAttribute : Attribute { }

// Usage on DTO — ASP.NET validates automatically
public class CreateUserDto
{
    [Required, EmailAddress]
    public string Email { get; init; } = "";

    [Range(18, 120)]
    public int Age { get; init; }

    [Sensitive]
    public string? Ssn { get; init; }
}

// Controller — routing + auth attributes
[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase
{
    [HttpGet("{id}")]
    [Authorize(Roles = "Admin")]
  public ActionResult<OrderDto> Get(int id) => Ok();
}""",
        "language": "csharp",
        "key_points": [
            "Metadata for compile-time and runtime consumers",
            "Data annotations drive API model validation",
            "Custom attributes via AttributeUsage targets",
            "Source generators read attributes at compile time",
            "Reflection-based attribute lookup has performance cost",
        ],
    },
    "top-level-statements": {
        "explanation": (
            "**Top-level statements** (C# 9+) let you write executable code **without** an explicit `Program` class and `static void Main` — the compiler generates an entry point behind the scenes. "
            "ASP.NET Core **minimal hosting** (`WebApplication.CreateBuilder`) is the canonical example — `Program.cs` is often just top-level statements. "
            "Only **one file per project** may contain top-level statements; mixing with other `Main` methods causes compile errors. "
            "`args`, `return`, and `await` are supported at the top level — `return 0;` sets the process exit code. "
            "**Why it matters:** less ceremony for scripts, tools, and microservices; the same project system and DI work as traditional `Main`. "
            "**Interview tip:** you can still use `partial Program` for testability (integration tests referencing `WebApplicationFactory`)."
        ),
        "code": """// Program.cs — top-level statements (no explicit Main)
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddScoped<IOrderService, OrderService>();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.MapGet("/health", () => Results.Ok(new { status = "healthy" }));
app.MapGet("/orders/{id}", async (int id, IOrderService svc) =>
    await svc.GetAsync(id) is { } o ? Results.Ok(o) : Results.NotFound());

app.Run();

// Compiler generates equivalent of:
// internal class Program { static async Task Main(string[] args) { ... } }""",
        "language": "csharp",
        "key_points": [
            "C# 9 — compiler generates Main entry point",
            "One file per project with top-level statements",
            "Standard for ASP.NET Core minimal hosting",
            "Supports args, return exit codes, and await",
            "Use partial Program class for advanced scenarios",
        ],
    },
    "global-usings": {
        "explanation": (
            "**Global usings** (C# 10) apply `using` directives **project-wide** so every file shares common namespaces without repetition. "
            "SDK-style projects enable **implicit usings** (`<ImplicitUsings>enable</ImplicitUsings>`) — auto-including `System`, `System.Linq`, `Microsoft.AspNetCore.Builder`, etc. "
            "Add a `GlobalUsings.cs` file with `global using` lines for team-wide aliases or shared namespaces. "
            "`global using static` imports static members (e.g., `global using static System.Math`). "
            "**Trade-off:** too many global usings obscure where types originate — balance convenience with clarity in large solutions. "
            "**Interview tip:** `global using` aliases resolve naming conflicts (`global using OrderSvc = MyApp.Services.OrderService`)."
        ),
        "code": """// GlobalUsings.cs — shared across entire project
global using System;
global using System.Collections.Generic;
global using System.Linq;
global using System.Threading.Tasks;
global using Microsoft.Extensions.Logging;
global using MyApp.Contracts;

// Alias to disambiguate types
global using OrderDto = MyApp.Contracts.Orders.OrderResponse;

// csproj implicit usings (enabled by default for web/console)
// <PropertyGroup>
//   <ImplicitUsings>enable</ImplicitUsings>
// </PropertyGroup>

// Any file can now use ILogger<T> without explicit using
public class OrderService(ILogger<OrderService> log)
{
    public void Process(OrderDto order) => log.LogInformation("Processing {Id}", order.Id);
}""",
        "language": "csharp",
        "key_points": [
            "global using applies namespace project-wide",
            "ImplicitUsings in SDK-style csproj",
            "GlobalUsings.cs centralizes team conventions",
            "global using static imports static members",
            "Aliases resolve type name collisions",
        ],
    },
    "linq-deferred-execution": {
        "explanation": (
            "LINQ operators on **IEnumerable<T>** use **deferred execution** — they build a **pipeline** that runs only when you **enumerate** (foreach, ToList, Count, First). "
            "Nothing hits the database or allocates a result list until terminal execution. "
            "Each full enumeration **re-executes** the entire pipeline — a common bug when calling `Count()` then `foreach` on the same query (double work). "
            "Materialize with `ToList()`, `ToArray()`, or `ToDictionary()` when you need a **stable snapshot** or multiple passes. "
            "**IQueryable** also defers but builds **expression trees** translated by the provider (EF Core → SQL). "
            "**Interview tip:** side effects in `Where`/`Select` run every enumeration — keep predicates pure."
        ),
        "code": """var orders = GetOrders(); // IEnumerable<Order>

// Deferred — no filtering yet, just builds iterator chain
var query = orders
    .Where(o => o.Total > 100)
    .OrderByDescending(o => o.CreatedAt)
    .Select(o => new { o.Id, o.Total });

// Still deferred — foreach triggers ONE execution
foreach (var o in query)
    Console.WriteLine(o.Id);

// Materialize once if you need multiple passes
var list = query.ToList();
var count = list.Count;   // no re-query
var first = list[0];

// BUG — enumerates twice
var q = orders.Where(o => ExpensiveCheck(o));
var n = q.Count();    // full pass 1
var items = q.ToList(); // full pass 2""",
        "language": "csharp",
        "key_points": [
            "LINQ chains execute on enumeration, not construction",
            "Terminal operators trigger execution",
            "Multiple enumerations re-run the pipeline",
            "Materialize with ToList/ToArray for snapshots",
            "Keep LINQ predicates free of side effects",
        ],
    },
    "ienumerable-vs-iqueryable": {
        "explanation": (
            "**IEnumerable<T>** is for **in-memory** enumeration — LINQ to Objects compiles delegates and runs them in process. "
            "**IQueryable<T>** extends IEnumerable with **expression trees** — providers (EF Core, NHibernate) **translate** predicates to SQL or other remote queries. "
            "Filtering with `Where` on `IQueryable` pushes work to the **database**; on `IEnumerable` pulls all rows first then filters in memory. "
            "Calling `AsEnumerable()` switches from `IQueryable` to `IEnumerable` — often a performance trap that forces **client-side evaluation**. "
            "**Interview classic:** `IQueryable` = composable remote query; `IEnumerable` = local iteration. "
            "Use `ToListAsync()` on EF queries to execute once and release the DbContext scope appropriately."
        ),
        "code": """// IQueryable — EF Core translates to SQL
IQueryable<Order> queryable = db.Orders
    .Where(o => o.Status == "Open")   // → WHERE clause
    .OrderBy(o => o.CreatedAt);       // → ORDER BY

var sql = queryable.ToQueryString(); // inspect generated SQL
var page = await queryable.Take(20).ToListAsync();

// IEnumerable — in-memory LINQ
IEnumerable<Order> inMemory = GetCachedOrders()
    .Where(o => o.Total > 500);       // runs in CLR

// TRAP — AsEnumerable() forces client evaluation
var bad = db.Orders
    .AsEnumerable()                  // now IEnumerable
    .Where(o => CustomLogic(o));      // loads ALL rows first

// GOOD — keep IQueryable until last moment
var good = await db.Orders
    .Where(o => o.Status == "Open")
    .ToListAsync();""",
        "language": "csharp",
        "key_points": [
            "IEnumerable = in-memory delegate-based LINQ",
            "IQueryable = expression trees for providers",
            "EF Core translates IQueryable to SQL",
            "AsEnumerable() may load entire table",
            "Execute with ToListAsync to run query once",
        ],
    },
    "yield-return": {
        "explanation": (
            "`yield return` implements **iterator methods** — the compiler generates a **state machine** that produces values **lazily** one at a time. "
            "Memory stays **O(1)** for streaming large sequences instead of building a `List<T>` upfront. "
            "Execution **pauses** at each `yield return` and resumes when the caller requests the next item. "
            "`yield break` ends iteration early. Iterator methods return `IEnumerable<T>` or `IAsyncEnumerable<T>` (with `await foreach`). "
            "**Caution:** the method body runs **fresh** on each enumeration — don't assume single execution. "
            "**Interview tip:** `yield return` cannot appear in `try/catch` with `yield` in catch (language restriction); use helper methods."
        ),
        "code": """// Lazy sequence — no list allocated
public static IEnumerable<int> ReadBatches(int total, int batchSize)
{
    for (int i = 0; i < total; i += batchSize)
    {
        int size = Math.Min(batchSize, total - i);
        yield return size; // pause here until next MoveNext()
    }
}

// Consumer — executes incrementally
foreach (var batch in ReadBatches(1_000_000, 1000))
    ProcessBatch(batch);

// Async iterator — C# 8+
public async IAsyncEnumerable<Order> StreamOrdersAsync(
    [EnumeratorCancellation] CancellationToken ct = default)
{
    await foreach (var page in _repo.PagesAsync(ct))
    {
        foreach (var order in page)
            yield return order;
    }
}

// await foreach consumes async streams
await foreach (var order in StreamOrdersAsync(ct))
    Handle(order);""",
        "language": "csharp",
        "key_points": [
            "Compiler generates iterator state machine",
            "Lazy — values produced on demand",
            "Memory-efficient for large sequences",
            "IAsyncEnumerable for async streaming",
            "Re-enumerating restarts the method",
        ],
    },
    "json-serialization": {
        "explanation": (
            "**System.Text.Json** is the **built-in**, high-performance serializer in modern .NET — default for ASP.NET Core and designed for UTF-8 and minimal allocations. "
            "**Newtonsoft.Json** (Json.NET) remains common in legacy apps for features like **reference loop handling**, **JSONPath**, and flexible contract resolution. "
            "Configure naming (`CamelCase`), enums, dates, and polymorphism via `JsonSerializerOptions` or **source generators** (`[JsonSerializable]`) for AOT/trimming. "
            "`[JsonPropertyName]`, `[JsonIgnore]`, and `required` properties control serialization shape. "
            "**Interview tip:** `System.Text.Json` is stricter by default — property name case sensitivity and trailing commas differ from Newtonsoft. "
            "Use `JsonSerializerContext` source generators in .NET 8+ for faster startup and Native AOT compatibility."
        ),
        "code": """// Serialize with camelCase (ASP.NET Core default)
var options = new JsonSerializerOptions
{
    PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
    WriteIndented = true,
    DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull
};

string json = JsonSerializer.Serialize(order, options);
var dto = JsonSerializer.Deserialize<OrderDto>(json, options);

// Source generator — compile-time metadata (AOT-friendly)
[JsonSerializable(typeof(OrderDto))]
[JsonSerializable(typeof(List<OrderDto>))]
public partial class AppJsonContext : JsonSerializerContext { }

var aotJson = JsonSerializer.Serialize(order, AppJsonContext.Default.OrderDto);

// ASP.NET Core — configure globally
builder.Services.ConfigureHttpJsonOptions(o =>
{
    o.SerializerOptions.PropertyNamingPolicy = JsonNamingPolicy.CamelCase;
});""",
        "language": "csharp",
        "key_points": [
            "System.Text.Json is default in ASP.NET Core",
            "JsonSerializerOptions control naming and behavior",
            "Source generators for AOT and performance",
            "Newtonsoft for legacy/advanced scenarios",
            "Stricter defaults than Json.NET — test migrations",
        ],
    },
    "init-only-setters": {
        "explanation": (
            "**Init-only setters** (`init` accessor, **C# 9.0**) support **immutable objects** without forcing every value "
            "through a large constructor. Think of it as: *\"This property can be set when creating the object, but never "
            "modified afterward.\"* "
            "**Before C# 9** you had two awkward choices: **`get`-only** (immutable but huge constructors) or **`set`** "
            "(mutable — objects could become invalid after creation). **`init`** bridges both: readable object initializers "
            "and read-only behavior after construction. "
            "**When is `init` allowed?** (1) object initializer, (2) constructor in the same type, (3) another `init` "
            "accessor during initialization, (4) record types (very common). "
            "**After initialization** any `obj.Prop = value` assignment is a **compile error**. "
            "**`init` vs `readonly`:** `readonly` applies to **fields** and only in constructor/declaration; "
            "`init` applies to **properties** and also object initializers. "
            "**Runtime note:** enforcement is primarily **compile-time**; reflection or some serializers can bypass it. "
            "**Use for:** configuration objects, API DTOs, immutable domain state, and records."
        ),
        "code": """// ── Before C# 9: two limited options ─────────────────────────────────────

// 1. Read-only — immutable but constructor grows with every property
public class OrderReadOnly
{
    public int Id { get; }
    public string Customer { get; }
    public OrderReadOnly(int id, string customer) { Id = id; Customer = customer; }
}

// 2. Public setter — mutable; state can change accidentally later
public class OrderMutable
{
    public int Id { get; set; }
    public string Customer { get; set; }
}

// ── C# 9: init-only setters ────────────────────────────────────────────────

public class OrderDto
{
    public int Id { get; init; }
    public string Customer { get; init; } = "";
    public decimal Total { get; init; }
}

// ✅ 1. Object initializer
var order = new OrderDto
{
    Id = 1,
    Customer = "Alice",
    Total = 99.99m
};

// ✅ 2. Constructor in same type can assign init properties
public class OrderFactory
{
    public int Id { get; init; }
    public OrderFactory(int id) => Id = id;
}

// ❌ After initialization — compile error
// order.Total = 50;

// ── Why init? Order stays valid after creation ─────────────────────────

public class Order
{
    public int Id { get; init; }
    public decimal Total { get; init; }
    public string Status { get; init; } = "Placed";
}

var placed = new Order { Id = 42, Total = 150m };
// placed.Status = "Cancelled"; // ❌ prevents accidental invalid state

// ── Real-world API DTO (ASP.NET Core model binding) ───────────────────

public class CreateOrderRequest
{
    public required string CustomerName { get; init; }
    public required int Quantity { get; init; }
    public string? Notes { get; init; }
}

// POST JSON binds into init properties; object stays immutable in controller
[HttpPost]
public IActionResult Create([FromBody] CreateOrderRequest request)
{
    // request.CustomerName = "hack"; // ❌ compile error
    return Ok(new { request.CustomerName, request.Quantity });
}

// ── init with records (most common modern pattern) ─────────────────────

public record ProductDto(int Id, string Name, decimal Price);

var p1 = new ProductDto(1, "Margherita", 12.99m);

// Non-destructive copy — original unchanged
var p2 = p1 with { Price = 14.99m };

// ── Comparison: set vs init vs readonly ────────────────────────────────
// set      → mutable anytime after construction
// init     → assign during initialization only (initializer OR ctor)
// readonly → field only; ctor or declaration; NOT object initializer""",
        "language": "csharp",
        "key_points": [
            "C# 9 — immutable after construction without giant ctors",
            "Allowed: object initializer, ctor, init chain, records",
            "init = properties; readonly = fields (different rules)",
            "set = mutable; init = fixed after creation",
            "Use for DTOs, config, domain models; compiler enforced",
        ],
    },
    "required-members": {
        "explanation": (
            "**Required members** (C# 11) mark properties or fields that **must** be set during object construction — enforced by the **compiler**. "
            "Callers must use an **object initializer** or constructor that assigns every `required` member. "
            "Works with `init` accessors — the standard pattern for modern immutable DTOs in ASP.NET Core model binding. "
            "System.Text.Json and ASP.NET Core deserialization **respect** required modifiers — missing JSON properties cause validation errors. "
            "**Why it matters:** replaces constructor boilerplate for many-parameter DTOs while keeping compile-time safety. "
            "**Pitfall:** required members in base classes must be set by derived class initializers too — plan inheritance carefully."
        ),
        "code": """public class CreateOrderDto
{
    public required string CustomerName { get; init; }
    public required int Quantity { get; init; }
    public string? Notes { get; init; } // optional
}

// Compiler requires all required members
var dto = new CreateOrderDto
{
    CustomerName = "Alice",
    Quantity = 3
};

// Missing required — compile error:
// var bad = new CreateOrderDto { Quantity = 1 };

// ASP.NET Core binds JSON and validates required
// POST body missing customerName → 400 validation error

// Required on record
public record ProductDto(int Id, required string Sku, decimal Price);""",
        "language": "csharp",
        "key_points": [
            "Compiler enforces initialization of required members",
            "Use object initializer or matching constructor",
            "Standard for modern API request DTOs",
            "JSON deserializer validates required properties",
            "Combine with init for immutable request models",
        ],
    },
    "configuration-binding": {
        "explanation": (
            "**.NET configuration** layers JSON, environment variables, Key Vault, and command-line into `IConfiguration`. "
            "**Options pattern** binds sections to **strongly typed POCOs** via `services.Configure<T>(configuration.GetSection(\"Key\"))`. "
            "Inject `IOptions<T>` (singleton snapshot), `IOptionsSnapshot<T>` (scoped, reloads per request), or `IOptionsMonitor<T>` (singleton with change callbacks). "
            "`IOptions<T>.Value` is read at first access — use **Snapshot** when config reloads at runtime (`reloadOnChange: true`). "
            "**ValidateOnStart** and `IValidateOptions<T>` fail fast on bad config at startup — critical for production. "
            "**Interview tip:** environment variables use `__` or `:` for nesting (`Jwt__Key` maps to `Jwt:Key`)."
        ),
        "code": """// appsettings.json: { "Jwt": { "Issuer": "...", "Key": "..." } }

public class JwtOptions
{
    public const string SectionName = "Jwt";
    public string Issuer { get; init; } = "";
    public string Key { get; init; } = "";
}

// Program.cs — bind and validate at startup
builder.Services
    .AddOptions<JwtOptions>()
    .Bind(builder.Configuration.GetSection(JwtOptions.SectionName))
    .ValidateDataAnnotations()
    .ValidateOnStart();

// Inject options
public class TokenService(IOptions<JwtOptions> options)
{
    private readonly JwtOptions _jwt = options.Value;
    public string CreateToken() => /* use _jwt.Issuer, _jwt.Key */;
}

// Environment variable override: Jwt__Key=secret""",
        "language": "csharp",
        "key_points": [
            "Configure<T> binds IConfiguration sections to POCOs",
            "IOptions vs Snapshot vs Monitor lifetimes",
            "ValidateOnStart fails fast on bad config",
            "Environment variables override JSON settings",
            "Use IOptionsSnapshot when config reloads",
        ],
    },
    "expression-trees": {
        "explanation": (
            "An **expression tree** represents code as a **data structure** (tree of nodes) rather than compiled IL — enabling **analysis and translation**. "
            "`Expression<Func<T, bool>>` looks like a lambda but builds a tree EF Core can translate to **SQL WHERE** clauses. "
            "Regular `Func<T, bool>` delegates are **opaque** — providers cannot inspect them. "
            "Expression trees power **IQueryable** providers, dynamic predicates, and some ORMs. "
            "You can **compile** expressions to delegates with `.Compile()` when in-memory execution is needed — but compilation has cost. "
            "**Interview tip:** `AsQueryable()` on in-memory collections uses LINQ to Objects — no SQL translation despite IQueryable type."
        ),
        "code": """// Delegate — compiled, opaque to EF
Func<Order, bool> func = o => o.Total > 100;

// Expression tree — inspectable structure
Expression<Func<Order, bool>> expr = o => o.Total > 100;

// EF Core uses expression trees
IQueryable<Order> query = db.Orders.Where(o => o.Status == "Open");
// → SELECT * FROM Orders WHERE Status = 'Open'

// Dynamic predicate building
ParameterExpression param = Expression.Parameter(typeof(Order), "o");
MemberExpression total = Expression.Property(param, nameof(Order.Total));
ConstantExpression hundred = Expression.Constant(100m);
BinaryExpression body = Expression.GreaterThan(total, hundred);
var lambda = Expression.Lambda<Func<Order, bool>>(body, param);

var filtered = db.Orders.Where(lambda);

// Compile for in-memory use
Func<Order, bool> compiled = lambda.Compile();""",
        "language": "csharp",
        "key_points": [
            "Expression trees represent code as data",
            "IQueryable providers translate trees to SQL",
            "Func delegates cannot be translated remotely",
            "Expression<T> for building dynamic filters",
            "Compile() converts tree to delegate for memory",
        ],
    },
    "reflection": {
        "explanation": (
            "**Reflection** inspects and manipulates types, methods, and properties at **runtime** via `System.Reflection` — `typeof`, `GetType()`, `GetMethod`, `Invoke`. "
            "Use cases: serialization frameworks, DI containers, mapping libraries, and plugin architectures. "
            "Reflection is **slow** and can break with **trimming/AOT** — modern .NET prefers **source generators** and compile-time metadata. "
            "`Activator.CreateInstance` and `MethodInfo.Invoke` are common interview topics — both are orders of magnitude slower than direct calls. "
            "**Attributes** are often read via reflection — cache `PropertyInfo`/`MethodInfo` results when used in hot paths. "
            "**Interview tip:** .NET 8+ Native AOT requires `[DynamicallyAccessedMembers]` annotations or reflection-free alternatives."
        ),
        "code": """// Inspect type metadata
Type type = typeof(OrderService);
Console.WriteLine(type.Name);

foreach (var prop in type.GetProperties())
    Console.WriteLine($"  {prop.Name}: {prop.PropertyType.Name}");

// Invoke method by name — flexible but slow
var instance = Activator.CreateInstance(type);
var method = type.GetMethod("ProcessOrder");
method?.Invoke(instance, [42]);

// Read custom attribute
var attr = type.GetCustomAttribute<ApiControllerAttribute>();
if (attr is not null)
    Console.WriteLine("Is API controller");

// Modern alternative — source generator avoids reflection
// [LoggerMessage] generates LogOrderPlaced at compile time

// AOT warning — reflection may be trimmed
[DynamicallyAccessedMembers(DynamicallyAccessedMemberTypes.PublicMethods)]
public class Plugin { }""",
        "language": "csharp",
        "key_points": [
            "Runtime inspection via System.Reflection",
            "Invoke and CreateInstance are performance-heavy",
            "Prefer source generators over hot-path reflection",
            "Native AOT limits reflection — annotate or avoid",
            "Cache reflection metadata when reuse is needed",
        ],
    },
    "parallel-linq": {
        "explanation": (
            "**PLINQ** (`ParallelEnumerable`, `AsParallel()`) partitions **in-memory** sequences and processes elements on **multiple threads** from the thread pool. "
            "Ideal for **CPU-bound** work on large collections — image processing, complex calculations, batch transforms. "
            "Use `WithDegreeOfParallelism(n)` to cap threads; `AsOrdered()` preserves source order at a performance cost. "
            "**Not for I/O** — blocking threads on network/DB calls wastes pool threads; use `Task.WhenAll` or async instead. "
            "Order is **not guaranteed** unless `AsOrdered()` is specified. "
            "**Interview tip:** PLINQ has overhead — small collections may be slower parallel than sequential."
        ),
        "code": """var numbers = Enumerable.Range(1, 10_000_000);

// CPU-bound parallel filter + map
var results = numbers
    .AsParallel()
    .WithDegreeOfParallelism(Environment.ProcessorCount)
    .Where(n => IsPrime(n))           // runs on multiple cores
    .Select(n => n * n)
    .ToList();

// Preserve order (slower)
var ordered = numbers.AsParallel()
    .AsOrdered()
    .Select(Transform)
    .ToList();

// PLINQ aggregates
var sum = numbers.AsParallel().Sum();

// NOT for I/O — blocks thread pool threads
// BAD:
// files.AsParallel().Select(f => File.ReadAllText(f));

// GOOD for I/O:
// await Task.WhenAll(files.Select(f => ReadFileAsync(f)));""",
        "language": "csharp",
        "key_points": [
            "AsParallel() for CPU-bound in-memory work",
            "Uses thread pool — not for I/O-bound tasks",
            "WithDegreeOfParallelism controls thread count",
            "Order not guaranteed without AsOrdered()",
            "Overhead makes it wrong for small collections",
        ],
    },
    "concurrent-dictionary": {
        "explanation": (
            "`ConcurrentDictionary<TKey, TValue>` provides **thread-safe** dictionary operations without locking the entire structure for every read. "
            "It uses **fine-grained locking** and lock-free techniques for high-concurrency caches, registries, and deduplication maps. "
            "`GetOrAdd` and `AddOrUpdate` are **atomic** — critical for cache-aside patterns where multiple threads may miss simultaneously. "
            "Enumeration is a **snapshot** — it may not reflect concurrent modifications exactly. "
            "Unlike `Dictionary` + `lock`, reads scale better under contention. "
            "**Interview tip:** `GetOrAdd` factory may run **multiple times** for the same key — only one result is stored; make factory idempotent."
        ),
        "code": """var cache = new ConcurrentDictionary<string, byte[]>();

// Thread-safe read
if (cache.TryGetValue("logo", out var bytes))
    return bytes;

// Atomic get-or-add — factory may run concurrently for same key
bytes = cache.GetOrAdd("logo", key =>
{
    // Expensive load — only one value wins per key
    return File.ReadAllBytes($"assets/{key}.png");
});

// Update atomically
cache.AddOrUpdate("counter", 1, (_, old) => old + 1);

// TryRemove for invalidation
cache.TryRemove("logo", out _);

// Parallel safe — no external lock needed
Parallel.ForEach(urls, url =>
{
    cache.GetOrAdd(url, LoadFromRemote);
});""",
        "language": "csharp",
        "key_points": [
            "Thread-safe dictionary without global lock",
            "GetOrAdd and AddOrUpdate are atomic",
            "Factory in GetOrAdd may execute multiple times",
            "Ideal for in-memory concurrent caches",
            "Enumeration is snapshot, not live view",
        ],
    },
    "interlocked": {
        "explanation": (
            "`Interlocked` provides **atomic** operations on single variables — `Increment`, `Decrement`, `Add`, `CompareExchange`, `Exchange`. "
            "Hardware guarantees **no torn reads/writes** without explicit `lock` — faster for simple counters and flags. "
            "`CompareExchange` implements **lock-free** patterns — read current value, compute new value, swap only if unchanged (retry loop). "
            "Use for **metrics**, reference counting, and one-time initialization flags — not for multi-field invariants (use `lock`). "
            "**Interview contrast:** `lock` protects **critical sections** with multiple statements; `Interlocked` is for **single-variable** atomicity. "
            "`Interlocked.CompareExchange` underpins many concurrent data structures and lazy initialization patterns."
        ),
        "code": """private int _requestCount;
private int _initialized; // 0 = no, 1 = yes

public void TrackRequest()
{
    Interlocked.Increment(ref _requestCount);
}

public int GetCount() => Interlocked.CompareExchange(ref _requestCount, 0, 0);

// One-time initialization flag (lock-free)
public void EnsureInitialized()
{
    if (Interlocked.CompareExchange(ref _initialized, 1, 0) == 0)
    {
        // Only one thread enters here
        LoadExpensiveResources();
    }
}

// Atomic swap
object? _latest = null;
public void Publish(object snapshot) =>
    Interlocked.Exchange(ref _latest, snapshot);

// CompareExchange loop — lock-free increment with max cap
void IncrementCapped(ref int field, int max)
{
    int current, next;
    do
    {
        current = field;
        if (current >= max) return;
        next = current + 1;
    } while (Interlocked.CompareExchange(ref field, next, current) != current);
}""",
        "language": "csharp",
        "key_points": [
            "Atomic ops without lock for single variables",
            "Increment/CompareExchange for counters and flags",
            "CompareExchange enables lock-free algorithms",
            "Not for multi-field consistency — use lock",
            "Faster than lock for simple numeric updates",
        ],
    },
    "memory-cache": {
        "explanation": (
            "`IMemoryCache` is the built-in **in-process** cache for .NET — register with `AddMemoryCache()` and inject `IMemoryCache` or use `IDistributedCache` for **multi-instance** scenarios. "
            "Set entries with `Set`, `GetOrCreate`, or `GetOrCreateAsync` and control lifetime via `MemoryCacheEntryOptions` — **absolute**, **sliding**, or **token** expiration. "
            "**Size limits** and `Size` on entries prevent unbounded memory growth — configure `SizeLimit` on the cache options. "
            "Register **callbacks** (`RegisterPostEvictionCallback`) for cleanup when entries expire. "
            "**Interview contrast:** `IMemoryCache` is per-server; **Redis** (`AddStackExchangeRedisCache`) shares cache across scaled-out ASP.NET Core instances. "
            "Cache-aside: check cache → on miss load from DB → store with TTL; invalidate on writes."
        ),
        "code": """// Program.cs
builder.Services.AddMemoryCache(o => o.SizeLimit = 10_000);

public class CatalogService(IMemoryCache cache, ICatalogRepository repo)
{
    public async Task<Catalog> GetCatalogAsync(CancellationToken ct)
    {
        return await cache.GetOrCreateAsync("catalog:v1", async entry =>
        {
            entry.AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(10);
            entry.SlidingExpiration = TimeSpan.FromMinutes(2);
            entry.Size = 1; // required when SizeLimit set
            entry.RegisterPostEvictionCallback((key, value, reason, state) =>
            {
                // Log eviction, cleanup, etc.
            });
            return await repo.LoadCatalogAsync(ct);
        }) ?? throw new InvalidOperationException("Cache miss failed");
    }

    public void Invalidate() => cache.Remove("catalog:v1");
}""",
        "language": "csharp",
        "key_points": [
            "AddMemoryCache for in-process caching",
            "Absolute vs sliding expiration policies",
            "SizeLimit prevents unbounded memory use",
            "IDistributedCache for multi-server scale-out",
            "GetOrCreateAsync for cache-aside pattern",
        ],
    },
}
