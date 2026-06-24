"""Enhanced interview-prep content for Core .NET and ASP.NET Core topics (part 1)."""

DETAILED_PART1: dict[str, dict] = {
    # ── Core .NET ──────────────────────────────────────────────────────────────
    "dotnet-core-vs-framework": {
        "explanation": (
            "**.NET Framework 4.x** is the original Windows-only runtime shipped with IIS and full WinForms/WCF support; "
            "it is in **maintenance mode** and receives security fixes only. **Modern .NET** (5/6/7/8+) is **cross-platform**, "
            "**open-source**, modular, and significantly faster — it is the only path for new development. "
            "The runtime ships as a **self-contained or framework-dependent** deployable, supports **side-by-side** SDK installs, "
            "and unifies console, web, mobile, and cloud workloads under one toolchain. "
            "Choose **.NET 8 LTS** for production greenfield apps; stay on Framework only when blocked by legacy APIs "
            "(Web Forms, WCF server, COM interop). "
            "**Pitfall:** assuming .NET Standard is still the primary bridge — today you target .NET directly and reference "
            "NuGet packages built for it; migration usually means retargeting projects and replacing Windows-specific APIs."
        ),
        "code": """// Program.cs — .NET 8 minimal API (cross-platform, Kestrel)
var builder = WebApplication.CreateBuilder(args);

// Built-in DI, config, logging — no Global.asax or web.config ceremony
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

// Health endpoint for load balancers / Kubernetes probes
app.MapGet("/health", () => Results.Ok(new { status = "healthy", runtime = Environment.Version }));

app.MapGet("/orders/{id:int}", (int id) =>
    Results.Ok(new { id, customer = "Alice", total = 99.99m }));

app.Run();

// Run locally:
//   dotnet run
// Publish self-contained Linux binary:
//   dotnet publish -c Release -r linux-x64 --self-contained""",
        "language": "csharp",
        "key_points": [
            ".NET 8 LTS is the current production default (support until Nov 2026)",
            "Cross-platform: Windows, Linux, macOS, containers, Azure",
            ".NET Framework = legacy; modern .NET = all new work",
            "Side-by-side SDK installs via global.json",
            "Performance and startup time are major upgrade drivers",
        ],
    },
    "di-lifetimes": {
        "explanation": (
            "**Dependency Injection (DI)** implements **Inversion of Control** — classes declare dependencies via constructor "
            "parameters instead of calling `new`, which makes code testable and loosely coupled. "
            "ASP.NET Core ships a built-in **IServiceCollection** container configured in `Program.cs`. "
            "Three lifetimes matter: **Singleton** (one instance for the app lifetime), **Scoped** (one per HTTP request or scope), "
            "and **Transient** (new instance every time it is resolved). "
            "Use **Scoped** for `DbContext` and request-specific state, **Singleton** for caches and stateless services, "
            "and **Transient** for lightweight stateless helpers. "
            "**Why it matters:** wrong lifetimes cause subtle bugs — e.g., injecting a Scoped service into a Singleton "
            "creates a **captive dependency** that outlives its intended scope. "
            "**Pitfall:** resolving Scoped services from Singleton constructors; use `IServiceScopeFactory` instead."
        ),
        "code": """// Program.cs — register services with correct lifetimes
builder.Services.AddSingleton<ICacheService, MemoryCacheService>();   // app-wide cache
builder.Services.AddScoped<IOrderRepository, OrderRepository>();      // per-request DB access
builder.Services.AddTransient<IEmailSender, SmtpEmailSender>();       // stateless, cheap to create

// Constructor injection — dependencies supplied by the container
public class OrderService(
    IOrderRepository repo,
    IEmailSender email,
    ILogger<OrderService> logger)
{
    public async Task<int> PlaceOrderAsync(Order order, CancellationToken ct)
    {
        logger.LogInformation("Placing order for {Customer}", order.CustomerName);
        var id = await repo.SaveAsync(order, ct);
        await email.SendAsync(order.CustomerEmail, $"Order #{id} confirmed", ct);
        return id;
    }
}

// Minimal API — container resolves OrderService per request (Scoped by default for scoped deps)
app.MapPost("/orders", async (Order order, OrderService svc, CancellationToken ct) =>
{
    var id = await svc.PlaceOrderAsync(order, ct);
    return Results.Created($"/orders/{id}", new { id });
});""",
        "language": "csharp",
        "key_points": [
            "Singleton — one instance per application",
            "Scoped — one per HTTP request; ideal for DbContext",
            "Transient — new instance on every injection",
            "Never inject Scoped into Singleton directly",
            "Prefer constructor injection over service locator",
        ],
    },
    "ref-vs-value": {
        "explanation": (
            "**Value types** (`struct`, `int`, `bool`, `enum`, `record struct`) store their data **directly**; "
            "assignment copies the entire value, so changes to the copy do not affect the original. "
            "**Reference types** (`class`, `interface`, `delegate`, arrays) store a **reference** (pointer) to heap memory; "
            "assignment copies the reference, so two variables can point to the **same object**. "
            "Value types usually live on the **stack** (or inline in objects); reference type objects live on the **heap** "
            "and are managed by the GC. "
            "Use **`struct`** / **`readonly record struct`** for small, immutable value objects (coordinates, money amounts). "
            "**`string`** is a reference type but **immutable** — concatenation creates new instances. "
            "**Pitfall:** mutating a struct through a boxed reference or accidentally sharing mutable reference-type state "
            "inside a struct causes confusing bugs."
        ),
        "code": """// Value type — copy is independent
int a = 10;
int b = a;   // b gets its own copy
b = 20;
Console.WriteLine(a); // 10 — unchanged

// Reference type — both variables share the same list
var list1 = new List<int> { 1, 2 };
var list2 = list1;   // copies reference, not elements
list2.Add(3);
Console.WriteLine(list1.Count); // 3 — same object

// Small immutable value object — ideal struct use case
public readonly record struct Money(decimal Amount, string Currency)
{
    public Money Add(Money other)
    {
        if (Currency != other.Currency)
            throw new InvalidOperationException("Currency mismatch");
        return new Money(Amount + other.Amount, Currency);
    }
}

var price = new Money(19.99m, "USD");
var tax   = new Money(2.00m, "USD");
var total = price.Add(tax); // new struct, originals unchanged""",
        "language": "csharp",
        "key_points": [
            "struct / int = value type; class = reference type",
            "Copying a reference type copies the pointer, not the object",
            "string is immutable despite being a reference type",
            "Use readonly record struct for small value objects",
            "Nullable value types (int?) add a null layer over structs",
        ],
    },
    "abstract-vs-interface": {
        "explanation": (
            "An **interface** defines a **capability contract** — a type can implement **many** interfaces, "
            "enabling polymorphism without shared implementation. "
            "An **abstract class** provides a **partial implementation** with shared fields, constructors, and concrete methods; "
            "a class can inherit **only one** abstract class. "
            "Prefer **interfaces** for DI, mocking, and defining service boundaries (`IPaymentGateway`, `IRepository<T>`). "
            "Use **abstract classes** when subclasses share real state or a fixed algorithm skeleton (Template Method pattern). "
            "Since **C# 8**, interfaces can have default and static members, blurring the line — but abstract classes still "
            "own constructors and protected state. "
            "**Pitfall:** choosing abstract class for DI when you need multiple inheritance of behavior — interfaces scale better."
        ),
        "code": """// Interface — capability contract, multiple allowed
public interface IPaymentGateway
{
    Task<PaymentResult> ChargeAsync(decimal amount, CancellationToken ct = default);
}

public interface IRefundable
{
    Task RefundAsync(string transactionId, CancellationToken ct = default);
}

// Abstract class — shared state + partial implementation
public abstract class EntityBase
{
    public Guid Id { get; protected set; } = Guid.NewGuid();
    public DateTime CreatedAt { get; protected set; } = DateTime.UtcNow;

    public abstract void Validate(); // each entity defines rules
}

public class Order : EntityBase, IPaymentGateway, IRefundable
{
    public decimal Total { get; set; }

    public override void Validate()
    {
        if (Total <= 0) throw new ValidationException("Total must be positive");
    }

    public Task<PaymentResult> ChargeAsync(decimal amount, CancellationToken ct = default)
        => Task.FromResult(new PaymentResult(true, Guid.NewGuid().ToString()));

    public Task RefundAsync(string transactionId, CancellationToken ct = default)
        => Task.CompletedTask;
}""",
        "language": "csharp",
        "key_points": [
            "Interface = many; abstract class = single inheritance",
            "Interfaces excel at DI and unit-test mocking",
            "Abstract class when shared state or base workflow exists",
            "C# 8+ default interface methods reduce breaking changes",
            "Favor composition + interfaces over deep inheritance trees",
        ],
    },
    "collections": {
        "explanation": (
            "The **System.Collections.Generic** namespace provides type-safe collections — choose based on **access pattern**, "
            "not habit. **`List<T>`** gives ordered, indexable storage with O(1) append and O(n) search. "
            "**`Dictionary<TKey,TValue>`** provides O(1) average key lookup — ideal for caches and indexes. "
            "**`HashSet<T>`** enforces uniqueness with O(1) add/contains — perfect for deduplication. "
            "**`Queue<T>`** (FIFO) and **`Stack<T>`** (LIFO) model pipeline and undo scenarios. "
            "**`SortedDictionary`** and **`PriorityQueue<T>`** (.NET 6+) cover ordering needs. "
            "**When to use:** profile hot paths — unnecessary `List.Contains` in a loop is O(n²); a `HashSet` fixes it. "
            "**Pitfall:** modifying a collection while iterating it — use `ToList()` snapshot or iterate backwards."
        ),
        "code": """using System.Collections.Generic;

// List<T> — default ordered collection, index access
var orders = new List<string> { "ORD-001", "ORD-002" };
orders.Add("ORD-003");
Console.WriteLine(orders[0]); // "ORD-001"

// Dictionary<TKey,TValue> — fast lookup by key
var prices = new Dictionary<int, decimal>
{
    [101] = 9.99m,
    [102] = 14.50m,
};
prices.TryGetValue(101, out var price); // 9.99m

// HashSet<T> — unique values, O(1) membership test
var seen = new HashSet<string> { "alice@x.com", "bob@x.com" };
seen.Add("alice@x.com"); // ignored — duplicate
Console.WriteLine(seen.Count); // 2

// Queue<T> — FIFO processing pipeline
var queue = new Queue<string>();
queue.Enqueue("job-1");
queue.Enqueue("job-2");
var next = queue.Dequeue(); // "job-1"

// PriorityQueue<TElement,TPriority> — .NET 6+ min-heap
var pq = new PriorityQueue<string, int>();
pq.Enqueue("urgent", priority: 1);
pq.Enqueue("normal", priority: 5);
Console.WriteLine(pq.Dequeue()); // "urgent\"""",
        "language": "csharp",
        "key_points": [
            "List<T> for ordered, indexable sequences",
            "Dictionary for key→value lookups",
            "HashSet for uniqueness and fast Contains",
            "Queue/Stack for FIFO/LIFO workflows",
            "Choose collection to match Big-O of your hot path",
        ],
    },
    "async-await": {
        "explanation": (
            "**`async`/`await`** enables non-blocking execution for **I/O-bound** work — database queries, HTTP calls, file reads — "
            "by releasing the thread back to the pool while waiting for external resources. "
            "It does **not** create a new thread; the state machine resumes on a thread-pool thread when the I/O completes. "
            "Use **`Task`/`Task<T>`** as the return type; avoid `async void` except in event handlers. "
            "For **CPU-bound** work, offload with `Task.Run` or `Parallel` — do not fake async with `Task.FromResult` on heavy compute. "
            "Always propagate **`CancellationToken`** through your call chain so clients can abort long operations. "
            "**Pitfall:** calling `.Result` or `.Wait()` on async code — this **blocks** and causes **deadlocks** in ASP.NET "
            "because the sync context cannot resume. Use `ConfigureAwait(false)` in library code."
        ),
        "code": """// Good — I/O-bound database call frees the thread while waiting
public async Task<Order?> GetOrderAsync(int id, CancellationToken ct)
{
    return await _db.Orders
        .AsNoTracking()
        .FirstOrDefaultAsync(o => o.Id == id, ct);
}

// CPU-bound — offload to thread pool explicitly
public Task<byte[]> ComputeHashAsync(byte[] data) =>
    Task.Run(() => SHA256.HashData(data));

// Controller — CancellationToken auto-bound from client disconnect
[ApiController]
[Route("api/orders")]
public class OrdersController(IOrderService service) : ControllerBase
{
    [HttpGet("{id:int}")]
    public async Task<IActionResult> Get(int id, CancellationToken ct)
    {
        var order = await service.GetOrderAsync(id, ct);
        return order is null ? NotFound() : Ok(order);
    }
}

// Library code — ConfigureAwait(false) avoids capturing sync context
public async Task<string> FetchDataAsync(HttpClient http, CancellationToken ct)
{
    var response = await http.GetAsync("/api/data", ct).ConfigureAwait(false);
    return await response.Content.ReadAsStringAsync(ct).ConfigureAwait(false);
}""",
        "language": "csharp",
        "key_points": [
            "async/await is for I/O-bound work, not CPU parallelism",
            "Never use .Result or .Wait() in ASP.NET — deadlocks",
            "Pass CancellationToken through the entire async chain",
            "ConfigureAwait(false) in reusable library code",
            "async void only in UI/event handlers",
        ],
    },
    "options-pattern": {
        "explanation": (
            "The **Options pattern** binds **configuration** (appsettings.json, environment variables, Key Vault) "
            "to strongly typed **POCO classes**, eliminating magic strings and enabling compile-time safety. "
            "Register with `services.Configure<TOptions>(configuration.GetSection(...))` and inject "
            "`IOptions<T>`, **`IOptionsSnapshot<T>`**, or **`IOptionsMonitor<T>`**. "
            "**`IOptions<T>`** is a singleton snapshot at startup — good for static config. "
            "**`IOptionsSnapshot<T>`** reloads per **scope/request** when config changes. "
            "**`IOptionsMonitor<T>`** supports **change callbacks** for singleton services that need live updates. "
            "Add validation via **DataAnnotations** or **`IValidateOptions<T>`** to fail fast on bad config. "
            "**Pitfall:** injecting `IOptions<T>` into a Singleton and expecting hot reload — use `IOptionsMonitor<T>` instead."
        ),
        "code": """// appsettings.json
// {
//   "Smtp": { "Host": "smtp.example.com", "Port": 587, "From": "noreply@example.com" }
// }

public class SmtpSettings
{
    public const string Section = "Smtp";
    public string Host { get; set; } = "";
    public int Port { get; set; }
    public string From { get; set; } = "";
}

// Program.cs — bind, validate, register
builder.Services
    .AddOptions<SmtpSettings>()
    .Bind(builder.Configuration.GetSection(SmtpSettings.Section))
    .ValidateDataAnnotations()
    .ValidateOnStart(); // fail at startup if invalid

// Consumer — IOptions<T> for stable singleton config
public class MailService(IOptions<SmtpSettings> options, ILogger<MailService> logger)
{
    private readonly SmtpSettings _smtp = options.Value;

    public void Send(string to, string subject, string body)
    {
        logger.LogInformation("Sending via {Host}:{Port} from {From}",
            _smtp.Host, _smtp.Port, _smtp.From);
        // SmtpClient or MailKit call here
    }
}

// IOptionsMonitor<T> — react to config reload in a singleton
public class FeatureFlagService(IOptionsMonitor<FeatureFlags> monitor)
{
    public bool IsEnabled(string flag) => monitor.CurrentValue.Flags.GetValueOrDefault(flag, false);
}""",
        "language": "csharp",
        "key_points": [
            "IOptions<T> — singleton snapshot at startup",
            "IOptionsSnapshot<T> — per-request reload",
            "IOptionsMonitor<T> — change notifications for singletons",
            "Validate with DataAnnotations or IValidateOptions<T>",
            "ValidateOnStart catches misconfiguration before traffic",
        ],
    },
    "generics": {
        "explanation": (
            "**Generics** let you write type-safe, reusable code without casting or **boxing** value types into `object`. "
            "A generic type or method declares **type parameters** (`T`, `TKey`, `TValue`) resolved at compile time. "
            "**Constraints** (`where T : class`, `where T : IComparable<T>`, `where T : new()`) restrict which types can "
            "be substituted and unlock specific operations. "
            "Generics power the entire BCL — `List<T>`, `Dictionary<TKey,TValue>`, `Task<T>`, `IEnumerable<T>`, EF `DbSet<T>`. "
            "Use generics for repositories, result wrappers, and algorithm reuse. "
            "**Pitfall:** over-constraining (`where T : class, new()` when an interface suffices) or creating generic "
            "types that should simply be two concrete classes — not everything needs abstraction."
        ),
        "code": """// Generic repository interface with constraint
public interface IRepository<T> where T : class
{
    Task<T?> GetByIdAsync(int id, CancellationToken ct = default);
    Task AddAsync(T entity, CancellationToken ct = default);
    Task<IReadOnlyList<T>> GetAllAsync(CancellationToken ct = default);
}

// Generic method with IComparable constraint
public static T Max<T>(T a, T b) where T : IComparable<T>
    => a.CompareTo(b) > 0 ? a : b;

// Generic result wrapper — avoids duplicate ApiResponse classes
public record ApiResponse<T>(bool Success, T? Data, string? Error = null)
{
    public static ApiResponse<T> Ok(T data) => new(true, data);
    public static ApiResponse<T> Fail(string error) => new(false, default, error);
}

// Usage
var repo = new OrderRepository(db); // implements IRepository<Order>
var bigger = Max(42, 17);           // T inferred as int
var response = ApiResponse<Order>.Ok(new Order { Id = 1 });""",
        "language": "csharp",
        "key_points": [
            "Generics eliminate casts and boxing for value types",
            "Constraints: class, struct, new(), base class, interface",
            "Type inference works for most method calls",
            "Used everywhere: List<T>, Task<T>, IEnumerable<T>",
            "Avoid generic over-engineering for one-off types",
        ],
    },
    "thread-sync": {
        "explanation": (
            "When multiple threads access **shared mutable state**, you need **synchronization** to prevent race conditions. "
            "**`lock`** (built on `Monitor`) provides **mutual exclusion** — only one thread enters the critical section at a time; "
            "it is re-entrant for the same thread. "
            "**`SemaphoreSlim`** limits **N concurrent** threads — ideal for throttling API calls or parallel downloads. "
            "**`Mutex`** works **across processes** but is heavier and rarely needed in web apps. "
            "Prefer **`Interlocked`** for simple atomic increments and **`ConcurrentDictionary`** for lock-free collections. "
            "For I/O-bound throttling, use **`SemaphoreSlim.WaitAsync`** instead of blocking `lock`. "
            "**Pitfall:** locking on `this`, `typeof(T)`, or string literals — always lock on a **private readonly object**."
        ),
        "code": """// lock — in-process mutual exclusion
public class Counter
{
    private readonly object _gate = new(); // private lock object — never lock(this)
    private int _count;

    public void Increment()
    {
        lock (_gate) { _count++; } // thread-safe
    }

    public int Value
    {
        get { lock (_gate) { return _count; } }
    }
}

// SemaphoreSlim — limit concurrent async operations (e.g., max 3 API calls)
public class ApiThrottler
{
    private readonly SemaphoreSlim _sem = new(initialCount: 3, maxCount: 3);
    private readonly HttpClient _http = new();

    public async Task<string> CallAsync(string url, CancellationToken ct)
    {
        await _sem.WaitAsync(ct); // wait for a slot
        try
        {
            return await _http.GetStringAsync(url, ct);
        }
        finally
        {
            _sem.Release(); // always release in finally
        }
    }
}

// Interlocked — lock-free atomic increment (no lock object needed)
Interlocked.Increment(ref _count);""",
        "language": "csharp",
        "key_points": [
            "lock (Monitor) for in-process critical sections",
            "SemaphoreSlim for async throttling (max N concurrent)",
            "Mutex for cross-process — rare in web apps",
            "Interlocked for simple atomic operations",
            "Never lock on this or public objects",
        ],
    },
    "task-cancellation": {
        "explanation": (
            "**.NET cancellation is cooperative** — nothing forcibly kills a thread; code must periodically check a "
            "**`CancellationToken`** and stop gracefully. "
            "Create a **`CancellationTokenSource`**, pass its `.Token` into async methods, and call `.Cancel()` or set a "
            "**timeout** via `new CancellationTokenSource(TimeSpan.FromSeconds(30))`. "
            "Inside loops and long operations, call **`ct.ThrowIfCancellationRequested()`** or pass the token to "
            "async APIs (`ReadAsync`, `Delay`, EF queries). "
            "ASP.NET Core automatically supplies a token tied to **client disconnect** in controller actions. "
            "Link multiple sources with **`CancellationTokenSource.CreateLinkedTokenSource`**. "
            "**Pitfall:** catching `OperationCanceledException` too broadly and swallowing real errors — "
            "distinguish user-initiated cancel from failure."
        ),
        "code": """// Timeout cancellation — auto-cancel after 30 seconds
using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(30));

try
{
    await ProcessBatchAsync(items, cts.Token);
}
catch (OperationCanceledException) when (cts.IsCancellationRequested)
{
    _logger.LogWarning("Batch cancelled or timed out");
}

// Cooperative cancellation inside a loop
public async Task ProcessBatchAsync(IEnumerable<Item> items, CancellationToken ct)
{
    foreach (var item in items)
    {
        ct.ThrowIfCancellationRequested(); // stop between items

        await ProcessOneAsync(item, ct);   // pass token to downstream calls
    }
}

// ASP.NET Core — token bound to client disconnect
[HttpGet("report")]
public async Task<IActionResult> GenerateReport(CancellationToken ct)
{
    var data = await _service.BuildReportAsync(ct); // aborts if client closes tab
    return Ok(data);
}

// Link tokens — cancel if EITHER source fires
using var linked = CancellationTokenSource.CreateLinkedTokenSource(userToken, timeoutToken);
await WorkAsync(linked.Token);""",
        "language": "csharp",
        "key_points": [
            "Cancellation is cooperative — code must check the token",
            "CancellationTokenSource controls cancellation and timeouts",
            "ASP.NET passes token on client disconnect",
            "Use CreateLinkedTokenSource to combine tokens",
            "Catch OperationCanceledException only when appropriate",
        ],
    },
    "logging": {
        "explanation": (
            "ASP.NET Core logging is built on **`ILogger<T>`** — a category-based abstraction decoupled from the sink. "
            "Providers include **Console**, **Debug**, **EventSource**, **Azure App Insights**, and third-party like **Serilog**. "
            "Use **structured logging** with message templates: `LogInformation(\"Order {OrderId} placed\", id)` — "
            "not string interpolation (`$\"Order {id}\"`), which loses searchable properties. "
            "Respect **LogLevel** hierarchy: Trace → Debug → Information → Warning → Error → Critical. "
            "Production typically runs at **Information** or **Warning**; Development at **Debug**. "
            "**Why it matters:** structured logs enable filtering and alerting in observability platforms. "
            "**Pitfall:** logging PII, passwords, JWT tokens, or full credit card numbers — scrub sensitive data."
        ),
        "code": """public class OrderService(ILogger<OrderService> logger, IOrderRepository repo)
{
    public async Task PlaceOrderAsync(Order order, CancellationToken ct)
    {
        // Structured logging — {OrderId} becomes a searchable property
        logger.LogInformation("Placing order for {Customer} with {LineCount} lines",
            order.CustomerName, order.Lines.Count);

        try
        {
            await repo.SaveAsync(order, ct);
            logger.LogInformation("Order {OrderId} saved successfully", order.Id);
        }
        catch (DbUpdateException ex)
        {
            // Include exception for stack trace; add context properties
            logger.LogError(ex, "Failed to save order for {Customer}", order.CustomerName);
            throw;
        }

        // Bad — loses structured properties, harder to query in App Insights
        // logger.LogInformation($"Order {order.Id} saved");
    }
}

// Program.cs — configure minimum level and providers
builder.Logging.ClearProviders();
builder.Logging.AddConsole();
builder.Logging.AddFilter("Microsoft.EntityFrameworkCore", LogLevel.Warning);""",
        "language": "csharp",
        "key_points": [
            "Use ILogger<T> with message templates, not interpolation",
            "LogLevel: Trace < Debug < Information < Warning < Error < Critical",
            "Serilog popular for sinks, enrichers, and formatting",
            "Never log secrets, tokens, or passwords",
            "Filter noisy framework categories in production",
        ],
    },
    "garbage-collection": {
        "explanation": (
            "The **.NET GC** automatically reclaims heap memory for objects no longer reachable. "
            "It uses a **generational** model: **Gen 0** (short-lived, collected frequently), **Gen 1** (buffer), "
            "**Gen 2** (long-lived, full collections — expensive). "
            "Objects **≥ 85 KB** go to the **Large Object Heap (LOH)**, which is collected less often and can fragment memory. "
            "Reduce allocations in hot paths to minimize **GC pauses** that cause latency spikes. "
            "Use **`IDisposable`** / **`await using`** for unmanaged resources (files, DB connections, HTTP responses) — "
            "the GC does not know about native handles. "
            "**Pitfall:** calling `GC.Collect()` in application code — it fights the tuned GC and usually hurts performance."
        ),
        "code": """// IDisposable — deterministic cleanup of unmanaged resources
await using var conn = new SqlConnection(connectionString);
await conn.OpenAsync();
// conn disposed automatically at end of scope

// ArrayPool — reuse byte buffers instead of allocating every request
var pool = ArrayPool<byte>.Shared;
var buffer = pool.Rent(minimumLength: 4096);
try
{
    var bytesRead = await stream.ReadAsync(buffer.AsMemory(0, 4096));
    Process(buffer, bytesRead);
}
finally
{
    pool.Return(buffer, clearArray: true); // always return to pool
}

// Span<T> — stack-friendly slice without heap allocation
ReadOnlySpan<char> email = "user@example.com".AsSpan();
var atIndex = email.IndexOf('@');

// IDisposable pattern for custom types holding native handles
public class FileProcessor : IDisposable
{
    private readonly FileStream _stream;
    public FileProcessor(string path) => _stream = File.OpenRead(path);
    public void Dispose() => _stream.Dispose();
}""",
        "language": "csharp",
        "key_points": [
            "Generational GC: Gen 0 (fast) → Gen 2 (full, slow)",
            "LOH for objects ≥ 85 KB — avoid frequent large allocations",
            "GC.Collect() almost never belongs in app code",
            "IDisposable/await using for files, DB, HTTP",
            "ArrayPool and Span<T> reduce allocation pressure",
        ],
    },
    "string-handling": {
        "explanation": (
            "In C#, **`string` is immutable** — every modification creates a new object on the heap. "
            "Repeated concatenation in a loop (`result += s`) generates **O(n²) allocations** and GC pressure. "
            "Use **`StringBuilder`** for many append operations in a single method. "
            "For a few parts, **string interpolation** (`$\"Hello {name}\"`) or **`string.Join`** is fine and readable. "
            "Modern APIs expose **`ReadOnlySpan<char>`** and **`Memory<char>`** for zero-allocation slicing and parsing. "
            "**`string.Create`** builds strings without intermediate allocations for advanced scenarios. "
            "For HTTP APIs, prefer **UTF-8** encoding (`Encoding.UTF8`) consistently. "
            "**Pitfall:** using `+` or `$\"\"` inside tight loops processing thousands of rows — profile and switch to StringBuilder."
        ),
        "code": """// Bad — O(n²) allocations in a loop
string bad = "";
foreach (var item in items)
    bad += item + ","; // new string object every iteration

// Good — StringBuilder for repeated appends
var sb = new StringBuilder(capacity: items.Count * 16); // pre-size if known
foreach (var item in items)
    sb.Append(item).Append(',');
var good = sb.ToString();

// string.Join — clean for simple separators
var joined = string.Join(", ", items);

// Span<char> — zero-allocation slice (no new string until needed)
ReadOnlySpan<char> full = "Hello, World!".AsSpan();
var greeting = full[..5];   // "Hello" — slice, no allocation
var world  = full[7..];     // "World!"

// string.Create — build without intermediate strings (advanced)
var result = string.Create(10, 42, (span, value) =>
{
    value.TryFormat(span, out _);
});""",
        "language": "csharp",
        "key_points": [
            "string is immutable — each change allocates a new object",
            "StringBuilder for many concatenations in loops",
            "string.Join and interpolation for small, readable cases",
            "Span<char> avoids allocations for parsing/slicing",
            "Use UTF-8 consistently in web APIs",
        ],
    },
    "interface-vs-abstract-rules": {
        "explanation": (
            "A class inherits **one** base class (abstract or concrete) but may implement **many** interfaces. "
            "**Abstract classes** can have **constructors**, **fields**, **protected members**, and mix abstract + concrete methods. "
            "**Interfaces** define a **public contract** — historically no state; since C# 8 they allow **default** and **static** "
            "members but still **no instance fields**. "
            "Neither can be **instantiated directly** — you always create a concrete derived class. "
            "Use abstract class for **\"is-a\"** relationships with shared implementation; interfaces for **\"can-do\"** capabilities. "
            "**When to use:** if two unrelated types share a capability (`IExportable`), use an interface; if they share lifecycle "
            "and state (`DocumentBase`), use abstract class. "
            "**Pitfall:** putting implementation in an abstract class that only one subclass needs — violates ISP."
        ),
        "code": """// Abstract class — shared state + forced + optional overrides
public abstract class DocumentBase
{
    protected Guid Id { get; } = Guid.NewGuid();       // instance state
    public DateTime CreatedAt { get; protected set; } = DateTime.UtcNow;

    public abstract void Save();                         // must implement
    public virtual void Print() =>                      // optional override
        Console.WriteLine($"Printing document {Id}");
}

// Interfaces — capability contracts, no shared state
public interface IAuditable
{
    DateTime CreatedAt { get; }
    void Audit(string action);
}

public interface IExportable
{
    byte[] Export();
}

// One base class + multiple interfaces
public class Invoice : DocumentBase, IAuditable, IExportable
{
    public override void Save() =>
        Console.WriteLine($"Saving invoice {Id}");

    public void Audit(string action) =>
        Console.WriteLine($"[{CreatedAt:u}] {action} on {Id}");

    public byte[] Export() =>
        System.Text.Encoding.UTF8.GetBytes($"Invoice-{Id}");
}""",
        "language": "csharp",
        "key_points": [
            "Single class inheritance; multiple interface implementation",
            "Abstract class: constructors, fields, protected members",
            "Interface: contract only; no instance fields",
            "Neither can be instantiated directly",
            "Abstract = is-a; interface = can-do capability",
        ],
    },
    "abstract-class-members": {
        "explanation": (
            "Abstract classes support three override patterns that control how subclasses customize behavior. "
            "**`abstract` methods** have no body — every non-abstract derived class **must** override them. "
            "**`virtual` methods** provide a **default implementation** that subclasses **may** override optionally. "
            "**`sealed override`** on a virtual/abstract method **stops further overriding** down the inheritance chain. "
            "Concrete methods with no modifier are **not overridable** — subclasses cannot change them. "
            "Use **abstract** when each child must define unique behavior (e.g., `ProcessPayment`). "
            "Use **virtual** when a sensible default exists but customization is welcome. "
            "**Pitfall:** bloated abstract base classes with dozens of virtual methods — prefer composition and interfaces."
        ),
        "code": """public abstract class PaymentProcessor
{
    // abstract — derived class MUST implement
    public abstract Task<PaymentResult> ProcessAsync(decimal amount, CancellationToken ct);

    // virtual — default provided; MAY override
    public virtual void Log(string message) =>
        Console.WriteLine($"[Payment] {message}");

    // concrete — NOT overridable
    public bool IsValidAmount(decimal amount) => amount > 0;
}

public class StripeProcessor : PaymentProcessor
{
    public override async Task<PaymentResult> ProcessAsync(decimal amount, CancellationToken ct)
    {
        Log($"Charging {amount:C} via Stripe");
        await Task.Delay(100, ct); // simulate API call
        return new PaymentResult(Success: true, TransactionId: Guid.NewGuid().ToString());
    }
}

public class PayPalProcessor : PaymentProcessor
{
    public override Task<PaymentResult> ProcessAsync(decimal amount, CancellationToken ct) =>
        Task.FromResult(new PaymentResult(true, "PP-" + Guid.NewGuid()));

    public override void Log(string message) =>
        Console.WriteLine($"[PayPal] {DateTime.UtcNow:O} — {message}");
}

public record PaymentResult(bool Success, string TransactionId);""",
        "language": "csharp",
        "key_points": [
            "abstract = forced override in every concrete child",
            "virtual = optional override with default behavior",
            "sealed override blocks further overriding",
            "Concrete non-virtual methods cannot be overridden",
            "Keep base classes focused — avoid god-class bases",
        ],
    },
    "delegates-events": {
        "explanation": (
            "A **delegate** is a **type-safe function pointer** — it defines a method signature that can reference one or more methods. "
            "**Lambdas** (`(a, b) => a + b`) and **anonymous methods** are inline delegate implementations. "
            "Built-in generic delegates **`Func<T>`** (returns value), **`Action<T>`** (void), and **`Predicate<T>`** (bool) "
            "cover most scenarios without declaring custom delegate types. "
            "**Events** wrap delegates with **add/remove** accessors, preventing external callers from invoking or replacing "
            "the handler list — classic **pub/sub** pattern. "
            "LINQ, callbacks, and UI frameworks rely heavily on delegates. "
            "**Pitfall:** failing to unsubscribe from events causes **memory leaks** when the publisher outlives the subscriber."
        ),
        "code": """// Custom delegate type
public delegate int MathOp(int a, int b);

// Built-in generic delegates — prefer these
Func<int, int, int> add = (a, b) => a + b;
Action<string> log = msg => Console.WriteLine(msg);
Predicate<int> isEven = n => n % 2 == 0;

Console.WriteLine(add(3, 4));    // 7
log("Hello");                   // Hello
Console.WriteLine(isEven(10));  // True

// Event — encapsulated pub/sub
public class StockTicker
{
    private decimal _price;

    // Only this class can raise the event
    public event EventHandler<decimal>? PriceChanged;

    public void UpdatePrice(decimal newPrice)
    {
        _price = newPrice;
        OnPriceChanged(newPrice); // notify subscribers
    }

    protected virtual void OnPriceChanged(decimal price) =>
        PriceChanged?.Invoke(this, price); // safe null-conditional invoke
}

// Subscribe
var ticker = new StockTicker();
ticker.PriceChanged += (sender, price) => Console.WriteLine($"New price: {price:C}");
ticker.UpdatePrice(150.25m);""",
        "language": "csharp",
        "key_points": [
            "Delegate = typed method reference",
            "Func<T>, Action<T>, Predicate<T> are built-in delegates",
            "Events prevent external Invoke — pub/sub pattern",
            "Unsubscribe events to avoid memory leaks",
            "LINQ methods accept Func/Action delegates",
        ],
    },
    "explicit-interface-implementation": {
        "explanation": (
            "**Explicit interface implementation** lets a class implement an interface member **without exposing it publicly** "
            "on the class itself — you access it only through the **interface reference**. "
            "Use it when two interfaces define the **same method signature** and you need different implementations, "
            "or when you want to **hide** an interface method from the public API. "
            "Syntax: `void IInterfaceName.Method()` — no access modifier allowed. "
            "The member is **not callable** on the concrete type directly — you must cast: `((IWritable)obj).Write(...)`. "
            "**When to use:** resolving naming conflicts or implementing legacy/internal APIs without polluting the public surface. "
            "**Pitfall:** overusing explicit implementation makes APIs confusing — prefer distinct method names when possible."
        ),
        "code": """public interface IReadable
{
    string Read();
}

public interface IWritable
{
    void Write(string data);
}

public class ConfigStore : IReadable, IWritable
{
    private string _content = "{}";

    // Public API — visible on ConfigStore directly
    public string Read() => _content;

    // Explicit — hidden unless cast to IWritable
    void IWritable.Write(string data)
    {
        File.WriteAllText("config.json", data);
        _content = data;
    }
}

// Usage
var store = new ConfigStore();
Console.WriteLine(store.Read());           // OK — public method

// store.Write("x");                       // COMPILE ERROR — not on public API
((IWritable)store).Write("{ \"key\": 1 }"); // OK — via interface cast

IWritable writable = store;
writable.Write("{ \"updated\": true }");   // OK — interface reference""",
        "language": "csharp",
        "key_points": [
            "Resolves signature clashes between interfaces",
            "Hides interface members from public class API",
            "Access only via interface cast or reference",
            "No access modifier on explicit implementation",
            "Use sparingly — prefer distinct method names",
        ],
    },
    "default-interface-methods": {
        "explanation": (
            "Since **C# 8**, interfaces can provide **default method bodies**, allowing you to **extend an interface** "
            "with new methods without breaking existing implementers. "
            "Implementers **inherit** the default unless they explicitly override it. "
            "This mirrors Java default methods and helps evolve library APIs gracefully. "
            "Use sparingly — substantial shared logic belongs in **abstract base classes** or **extension methods**. "
            "If a class implements two interfaces with **conflicting default methods**, the class must **explicitly override** "
            "to resolve the **diamond problem**. "
            "Interfaces still **cannot have instance fields** — defaults are behavior only. "
            "**Pitfall:** hiding complex logic in interface defaults makes debugging harder than a well-named base class."
        ),
        "code": """public interface INotifier
{
    // Required — every implementer must provide
    void Send(string message);

    // Default implementation — existing implementers get this for free
    void SendWithPrefix(string message) =>
        Send($"[ALERT] {message}");

    // Default with more logic
    void SendBatch(IEnumerable<string> messages)
    {
        foreach (var msg in messages)
            SendWithPrefix(msg);
    }
}

public class EmailNotifier : INotifier
{
    public void Send(string message) =>
        Console.WriteLine($"Email: {message}");
    // SendWithPrefix and SendBatch inherited automatically
}

public class SmsNotifier : INotifier
{
    public void Send(string message) =>
        Console.WriteLine($"SMS: {message}");

    // Override default if SMS needs different prefix logic
    void INotifier.SendWithPrefix(string message) =>
        Send($"URGENT: {message}");
}

// Usage
INotifier email = new EmailNotifier();
email.SendWithPrefix("Server down");  // Email: [ALERT] Server down""",
        "language": "csharp",
        "key_points": [
            "C# 8+ — extend interfaces without breaking implementers",
            "Diamond problem if multiple defaults clash",
            "Still no instance fields on interfaces",
            "Prefer extension methods for utility behavior",
            "Override defaults when behavior must differ",
        ],
    },
    "interface-for-di-testing": {
        "explanation": (
            "The **Dependency Inversion Principle** states high-level modules should depend on **abstractions**, not concretions. "
            "Register **`IOrderRepository`**, not `SqlOrderRepository`, in the DI container — the implementation is a "
            "deployment detail swapped via configuration. "
            "In **unit tests**, inject **fakes or mocks** (`Moq`, `NSubstitute`) that implement the same interface "
            "without hitting a real database or SMTP server. "
            "Interfaces define a **stable contract**; you can add new implementations (Redis cache, in-memory store) "
            "without changing consumers. "
            "Abstract classes work for DI but are **harder to mock** if they contain concrete logic you don't want to run. "
            "**When to use:** always for external dependencies — DB, HTTP, email, file system, clock. "
            "**Pitfall:** creating an interface for every class \"just because\" — interface only when you need polymorphism or testing seams."
        ),
        "code": """// Abstraction — stable contract
public interface IOrderRepository
{
    Task<Order?> GetAsync(int id, CancellationToken ct = default);
    Task<int> SaveAsync(Order order, CancellationToken ct = default);
}

// Production implementation
public class SqlOrderRepository(AppDbContext db) : IOrderRepository
{
    public Task<Order?> GetAsync(int id, CancellationToken ct) =>
        db.Orders.AsNoTracking().FirstOrDefaultAsync(o => o.Id == id, ct);

    public async Task<int> SaveAsync(Order order, CancellationToken ct)
    {
        db.Orders.Add(order);
        await db.SaveChangesAsync(ct);
        return order.Id;
    }
}

// Test fake — no database needed
public class FakeOrderRepository : IOrderRepository
{
    private readonly Dictionary<int, Order> _data = new();
    public Task<Order?> GetAsync(int id, CancellationToken ct) =>
        Task.FromResult(_data.GetValueOrDefault(id));
    public Task<int> SaveAsync(Order order, CancellationToken ct)
    {
        order.Id = _data.Count + 1;
        _data[order.Id] = order;
        return Task.FromResult(order.Id);
    }
}

// Program.cs — swap implementation via one line
builder.Services.AddScoped<IOrderRepository, SqlOrderRepository>();""",
        "language": "csharp",
        "key_points": [
            "Depend on abstractions (interfaces), not concretions",
            "Moq/NSubstitute mock interfaces in unit tests",
            "One registration line swaps production vs test impl",
            "Interface = stable contract across implementations",
            "Don't interface-wrap every class without reason",
        ],
    },
    "exception-handling": {
        "explanation": (
            "Effective exception handling in .NET balances **recoverability**, **observability**, and **API contract clarity**. "
            "Catch **specific exceptions** (`ValidationException`, `DbUpdateConcurrencyException`) — never bare `catch (Exception)` "
            "unless you log and rethrow. "
            "Use **`throw;`** (not `throw ex;`) to **preserve the stack trace** when rethrowing. "
            "Put cleanup in **`finally`** blocks or prefer **`await using`** for deterministic disposal. "
            "In ASP.NET Core APIs, return **ProblemDetails** (RFC 7807) via `Results.Problem()` or a global exception middleware "
            "instead of leaking stack traces to clients. "
            "Define **domain-specific exceptions** for business rule violations distinguishable from infrastructure failures. "
            "**Pitfall:** using exceptions for normal control flow (e.g., \"not found\" on every lookup) — use return values or `Result<T>`."
        ),
        "code": """// API controller — catch specific, return proper status codes
[HttpPost("{id:int}/process")]
public async Task<IActionResult> Process(int id, CancellationToken ct)
{
    try
    {
        await _service.ProcessAsync(id, ct);
        return NoContent();
    }
    catch (ValidationException ex)
    {
        return BadRequest(new ProblemDetails
        {
            Title = "Validation failed",
            Detail = ex.Message,
            Status = StatusCodes.Status400BadRequest,
        });
    }
    catch (OrderNotFoundException ex)
    {
        return NotFound(new ProblemDetails { Title = ex.Message, Status = 404 });
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Unexpected error processing order {OrderId}", id);
        throw; // let global handler return 500 without exposing internals
    }
}

// Global exception middleware (Program.cs)
app.UseExceptionHandler(errorApp =>
{
    errorApp.Run(async context =>
    {
        context.Response.StatusCode = 500;
        context.Response.ContentType = "application/problem+json";
        await context.Response.WriteAsJsonAsync(new ProblemDetails
        {
            Title = "An unexpected error occurred",
            Status = 500,
        });
    });
});""",
        "language": "csharp",
        "key_points": [
            "Catch specific exceptions; avoid swallowing errors",
            "throw; preserves stack trace — throw ex; does not",
            "ProblemDetails (RFC 7807) for API error responses",
            "Domain exceptions for business rule violations",
            "Don't use exceptions for expected control flow",
        ],
    },
    "dotnet-cli": {
        "explanation": (
            "The **.NET CLI** (`dotnet`) is the cross-platform toolchain for creating, building, testing, and publishing projects. "
            "**`dotnet new`** scaffolds project templates (webapi, classlib, xunit). "
            "**`dotnet restore`** downloads NuGet packages; **`dotnet build`** compiles; **`dotnet test`** runs test projects. "
            "**`dotnet publish`** produces deployable output (framework-dependent or self-contained). "
            "**`dotnet ef`** (global tool) manages EF Core migrations. "
            "**`dotnet user-secrets`** stores dev-only secrets outside source control. "
            "**`dotnet watch run`** enables hot reload during development. "
            "Pin SDK version with **`global.json`** in CI for reproducible builds. "
            "**Pitfall:** forgetting `-c Release` in publish pipelines — Debug builds are slower and larger."
        ),
        "code": """# Create a new Web API project
dotnet new webapi -n OrderApi -o ./src/OrderApi --no-openapi false

# Restore packages and build
dotnet restore
dotnet build -c Release

# Run unit tests with normal verbosity
dotnet test --logger "console;verbosity=normal" --no-build

# Publish for Linux deployment (framework-dependent)
dotnet publish ./src/OrderApi/OrderApi.csproj -c Release -o ./publish

# Publish self-contained (includes runtime — no dotnet install needed on server)
dotnet publish -c Release -r linux-x64 --self-contained -o ./publish/sc

# EF Core migrations
dotnet tool install --global dotnet-ef
dotnet ef migrations add InitialCreate --project ./src/OrderApi
dotnet ef database update --project ./src/OrderApi

# Dev secrets (never commit these)
dotnet user-secrets init --project ./src/OrderApi
dotnet user-secrets set "Jwt:Key" "dev-only-secret-key" --project ./src/OrderApi

# Hot reload during development
dotnet watch run --project ./src/OrderApi""",
        "language": "bash",
        "key_points": [
            "dotnet new / restore / build / test / publish workflow",
            "Always publish with -c Release for production",
            "global.json pins SDK version in CI",
            "dotnet ef for migrations; user-secrets for dev config",
            "dotnet watch run for hot reload",
        ],
    },
    "covariance": {
        "explanation": (
            "**Variance** controls whether generic type arguments can be substituted with **more derived** (covariant) "
            "or **more base** (contravariant) types. "
            "**Covariance (`out T`)** — you can assign `IEnumerable<string>` to `IEnumerable<object>` because you only "
            "**read** (produce) `T`; strings are objects. "
            "**Contravariance (`in T`)** — you can assign `Action<object>` to `Action<string>` because you only "
            "**write** (consume) `T`; an action accepting any object can accept a string argument. "
            "C# supports variance on **interfaces and delegates** with `in`/`out` modifiers — not on classes like `List<T>`. "
            "**Arrays are covariant** but **unsafe** — storing a string[] as object[] then inserting an int throws at runtime. "
            "**Pitfall:** assuming `List<string>` is assignable to `List<object>` — it is not (List is invariant)."
        ),
        "code": """// Covariance — out T: producer (read-only position)
IEnumerable<string> names = new List<string> { "Alice", "Bob" };
IEnumerable<object> objects = names; // OK — covariant out

foreach (object item in objects)
    Console.WriteLine(item);

// Contravariance — in T: consumer (write-only position)
Action<object> printObject = obj => Console.WriteLine(obj);
Action<string> printString = printObject; // OK — contravariant in

printString("Hello"); // Action<object> can handle any string

// Func variance: contravariant in params, covariant in return
Func<object, string> objectToString = o => o.ToString()!;
Func<string, string> stringToString = objectToString; // in T contravariant

// UNSAFE — arrays are covariant but can fail at runtime
object[] objArray = new string[1];
// objArray[0] = 42; // ArrayTypeMismatchException at runtime!

// List<T> is INVARIANT — this does NOT compile:
// List<object> list = new List<string>(); // compile error""",
        "language": "csharp",
        "key_points": [
            "out T = covariant (producer/read position)",
            "in T = contravariant (consumer/write position)",
            "IEnumerable<out T>, Action<in T>, Func<in T,out TResult>",
            "Arrays are covariant but unsafe at runtime",
            "List<T> is invariant — no string→object assignment",
        ],
    },
    "interface-segregation": {
        "explanation": (
            "The **Interface Segregation Principle (ISP)** — the **I** in SOLID — states clients should not be forced to "
            "depend on methods they do not use. "
            "Split **fat interfaces** with many unrelated methods into **small, focused** ones aligned to specific roles. "
            "This improves **testability** (mock only what you need), **maintainability** (changes are localized), "
            "and **clarity** (interface name describes one responsibility). "
            "In DI, register and inject the **smallest interface** that satisfies the consumer. "
            "The same principle applies to Angular service contracts and API surface design. "
            "**When to use:** whenever you see empty stub implementations or `NotImplementedException` in a class. "
            "**Pitfall:** 50 one-method interfaces — balance segregation with pragmatism; group truly cohesive operations."
        ),
        "code": """// Bad — fat interface forces unused implementations
public interface IWorker
{
    void Code();
    void Deploy();
    void WriteHrReport();
}

// Good — segregated by role
public interface IDeveloper
{
    void Code();
}

public interface IDevOps
{
    void Deploy();
}

public interface IHrReporter
{
    void WriteHrReport();
}

// Classes implement only what they need
public class FullStackEngineer : IDeveloper, IDevOps
{
    public void Code() => Console.WriteLine("Writing C# API");
    public void Deploy() => Console.WriteLine("Deploying to Azure");
}

public class BackendDeveloper : IDeveloper
{
    public void Code() => Console.WriteLine("Writing service layer");
    // No empty Deploy() or WriteHrReport() stubs needed
}

// DI — inject smallest interface
public class CodeReviewService(IDeveloper developer)
{
    public void Review() => developer.Code(); // only depends on IDeveloper
}""",
        "language": "csharp",
        "key_points": [
            "I in SOLID — no client depends on unused methods",
            "Split fat interfaces into role-focused ones",
            "Eliminates empty stub / NotImplementedException",
            "Inject smallest interface in DI",
            "Balance granularity — don't over-fragment",
        ],
    },
    "abstract-factory-vs-strategy": {
        "explanation": (
            "These patterns solve different problems and map naturally to **abstract classes** vs **interfaces**. "
            "The **Template Method** pattern (abstract class) defines an **algorithm skeleton** in the base class "
            "with **abstract/overridable steps** — subclasses customize specific steps while the workflow stays fixed. "
            "The **Strategy** pattern (interface) encapsulates a **swappable algorithm** injected at runtime — "
            "the entire behavior changes without inheritance. "
            "Use Template Method when the **process is stable** but steps vary (export pipeline: fetch → format → write). "
            "Use Strategy when algorithms are **fully interchangeable** (tax calculation, shipping, discount rules). "
            "Both honor the **Open/Closed Principle** — extend via new classes, not by editing existing ones. "
            "**Pitfall:** using inheritance for Strategy when composition + DI is simpler and more testable."
        ),
        "code": """// Template Method — abstract class defines fixed workflow
public abstract class DataExporter
{
    // Algorithm skeleton — cannot be overridden
    public void Export()
    {
        var data = FetchData();
        var formatted = Format(data);
        Write(formatted);
    }

    protected abstract IEnumerable<string> FetchData();
    protected abstract string Format(IEnumerable<string> data);
    protected virtual void Write(string output) => Console.WriteLine(output);
}

public class CsvExporter : DataExporter
{
    protected override IEnumerable<string> FetchData() => ["Alice,100", "Bob,200"];
    protected override string Format(IEnumerable<string> data) => string.Join("\\n", data);
}

// Strategy — interface swapped via DI
public interface ITaxCalculator
{
    decimal Calculate(decimal amount);
}

public class UsTaxCalculator : ITaxCalculator
{
    public decimal Calculate(decimal amount) => amount * 0.08m;
}

public class UkTaxCalculator : ITaxCalculator
{
    public decimal Calculate(decimal amount) => amount * 0.20m;
}

public class CheckoutService(ITaxCalculator tax)
{
    public decimal Total(decimal subtotal) => subtotal + tax.Calculate(subtotal);
}

// Program.cs — swap strategy without changing CheckoutService
// builder.Services.AddScoped<ITaxCalculator, UsTaxCalculator>();""",
        "language": "csharp",
        "key_points": [
            "Template Method (abstract class) = fixed workflow, variable steps",
            "Strategy (interface) = fully swappable algorithm via DI",
            "Both support Open/Closed Principle",
            "Prefer Strategy + composition over deep inheritance",
            "Abstract factory creates families; Strategy selects behavior",
        ],
    },
    "static-interface-members": {
        "explanation": (
            "Since **C# 8**, interfaces can define **`static` methods and properties** as helpers tied to the interface type. "
            "**C# 11** added **`static abstract`** and **`static virtual`** members, enabling generic math-style patterns "
            "where the compiler resolves the correct static implementation per type argument. "
            "Example: **`IParsable<T>`** requires each `T` to implement `static T Parse(string, IFormatProvider?)`. "
            "Static interface members are called on the **interface or type**, not on an instance — "
            "`OrderId.Parse(\"42\", null)`, not `instance.Parse(...)`. "
            "Interfaces still **cannot have instance fields** — static members are behavior, not state. "
            "**When to use:** generic constraints needing static factory methods; utility methods logically belonging to the contract. "
            "**Pitfall:** overloading interfaces with static helpers — keep them minimal and readable."
        ),
        "code": """// C# 11 — static abstract for generic parsing pattern
public interface IParsable<TSelf> where TSelf : IParsable<TSelf>
{
    static abstract TSelf Parse(string s, IFormatProvider? provider);
    static virtual TSelf Parse(string s) => TSelf.Parse(s, provider: null);
}

public readonly record struct OrderId(int Value) : IParsable<OrderId>
{
    public static OrderId Parse(string s, IFormatProvider? provider) =>
        new(int.Parse(s, provider));

    public override string ToString() => Value.ToString(provider: null);
}

// Usage — static method on the type
var id = OrderId.Parse("1042");
Console.WriteLine(id); // 1042

// C# 8 — static helper on interface (non-abstract)
public interface IAppLogger
{
    static void PrintBanner() =>
        Console.WriteLine("=== Application Started ===");

    void Log(string message);
}

// Call static member on interface
IAppLogger.PrintBanner();""",
        "language": "csharp",
        "key_points": [
            "C# 8: static methods/properties on interfaces",
            "C# 11: static abstract/virtual for generic patterns",
            "IParsable<T>, INumber<T> use static abstract members",
            "Still no instance fields on interfaces",
            "Use sparingly — keep interfaces readable",
        ],
    },
    # ── ASP.NET Core ─────────────────────────────────────────────────────────
    "rest-principles": {
        "explanation": (
            "**REST (Representational State Transfer)** is an architectural style for designing networked APIs around **resources** "
            "(nouns), not actions (verbs in URLs). "
            "Each resource has a **URI** (`/api/orders/42`); clients manipulate representations (usually **JSON**) via standard "
            "**HTTP methods**: GET (read), POST (create), PUT (replace), PATCH (partial update), DELETE (remove). "
            "REST is **stateless** — each request carries all context (auth token, data); the server stores no session between calls. "
            "Use **standard status codes**: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, "
            "403 Forbidden, 404 Not Found, 409 Conflict, 422 Unprocessable Entity, 500 Internal Server Error. "
            "**When to use:** public APIs, CRUD services, microservice boundaries. "
            "**Pitfall:** RPC-style URLs like `/api/createOrder` or `/api/getUserById` — use nouns and HTTP verbs instead."
        ),
        "code": """// RESTful route design — nouns + HTTP verbs
// GET    /api/orders          → list orders (200 OK, paginated body)
// GET    /api/orders/42       → get one order (200 OK or 404)
// POST   /api/orders          → create order (201 Created + Location header)
// PUT    /api/orders/42       → full replace (200 OK or 204)
// PATCH  /api/orders/42       → partial update (200 OK)
// DELETE /api/orders/42       → delete (204 No Content)

[ApiController]
[Route("api/orders")]
public class OrdersController(IOrderService service) : ControllerBase
{
    [HttpGet]
    public async Task<ActionResult<PagedResult<Order>>> List([FromQuery] int page = 1)
        => Ok(await service.ListAsync(page));

    [HttpGet("{id:int}")]
    public async Task<ActionResult<Order>> Get(int id)
        => await service.GetAsync(id) is { } order ? Ok(order) : NotFound();

    [HttpPost]
    public async Task<ActionResult<Order>> Create([FromBody] CreateOrderDto dto)
    {
        var order = await service.CreateAsync(dto);
        return CreatedAtAction(nameof(Get), new { id = order.Id }, order);
    }

    [HttpDelete("{id:int}")]
    public async Task<IActionResult> Delete(int id)
    {
        await service.DeleteAsync(id);
        return NoContent(); // 204
    }
}""",
        "language": "csharp",
        "key_points": [
            "Resources = nouns; HTTP verbs = actions",
            "Stateless — no server-side session between requests",
            "201 Created with Location header for POST",
            "204 No Content for successful DELETE",
            "Avoid verb-based URLs like /createOrder",
        ],
    },
    "middleware": {
        "explanation": (
            "ASP.NET Core processes every request through a **middleware pipeline** — a chain of `RequestDelegate` components. "
            "Each middleware can execute code **before** and **after** calling `next(context)`, forming an onion model. "
            "The **order is critical**: Exception handling → HTTPS redirection → Static files → Routing → CORS → "
            "**Authentication** → **Authorization** → Endpoints. "
            "Terminal middleware (e.g., endpoint routing) does not call `next`. "
            "Built-in middleware handles common concerns: **`UseExceptionHandler`**, **`UseHttpsRedirection`**, "
            "`UseAuthentication`, `UseAuthorization`, `UseCors`. "
            "Custom middleware is ideal for cross-cutting concerns: request timing, correlation IDs, tenant resolution. "
            "**Pitfall:** calling `UseAuthorization` before `UseAuthentication` — auth middleware must run first."
        ),
        "code": """// Custom middleware — measure request duration
public class RequestTimingMiddleware(RequestDelegate next, ILogger<RequestTimingMiddleware> log)
{
    public async Task InvokeAsync(HttpContext context)
    {
        var sw = Stopwatch.StartNew();

        await next(context); // call the next middleware in the pipeline

        sw.Stop();
        log.LogInformation("{Method} {Path} => {StatusCode} in {ElapsedMs}ms",
            context.Request.Method,
            context.Request.Path,
            context.Response.StatusCode,
            sw.ElapsedMilliseconds);
    }
}

// Program.cs — order matters!
var app = builder.Build();

app.UseExceptionHandler("/error");     // 1. catch unhandled exceptions
app.UseHttpsRedirection();               // 2. redirect HTTP → HTTPS
app.UseRouting();                          // 3. match route
app.UseAuthentication();                   // 4. who are you?
app.UseAuthorization();                    // 5. what can you do?
app.UseMiddleware<RequestTimingMiddleware>(); // 6. custom timing
app.MapControllers();                      // 7. terminal — endpoints

app.Run();""",
        "language": "csharp",
        "key_points": [
            "Pipeline = chain of RequestDelegate components",
            "Order: Exception → HTTPS → Routing → Auth → Authorization → Endpoints",
            "UseAuthentication BEFORE UseAuthorization",
            "Custom middleware for cross-cutting concerns",
            "Terminal middleware does not call next()",
        ],
    },
    "model-validation": {
        "explanation": (
            "**Model binding** maps HTTP request data (body, query, route, headers) to action parameters and DTOs automatically. "
            "**Validation** checks that bound data meets rules before your business logic runs. "
            "Apply **DataAnnotations** (`[Required]`, `[Range]`, `[EmailAddress]`, `[StringLength]`) on DTOs/records. "
            "`[ApiController]` automatically returns **400 Bad Request** with `ModelState` errors when validation fails — "
            "no manual `if (!ModelState.IsValid)` needed. "
            "Control binding source with **`[FromBody]`**, `[FromQuery]`, `[FromRoute]`, `[FromHeader]`. "
            "For complex cross-field rules, implement **`IValidatableObject`** or use **FluentValidation**. "
            "**Why it matters:** never trust client input — always validate server-side. "
            "**Pitfall:** validating entity models instead of DTOs — exposes internal schema and couples API to DB."
        ),
        "code": """public record CreateOrderDto(
    [Required(ErrorMessage = "Customer name is required")]
    [StringLength(100, MinimumLength = 2)]
    string CustomerName,

    [Range(1, 1000, ErrorMessage = "Quantity must be 1–1000")]
    int Quantity,

    [Required, EmailAddress]
    string Email
) : IValidatableObject
{
    // Cross-field validation
    public IEnumerable<ValidationResult> Validate(ValidationContext ctx)
    {
        if (Quantity > 100 && string.IsNullOrEmpty(CustomerName))
            yield return new ValidationResult(
                "Bulk orders require a customer name",
                [nameof(CustomerName), nameof(Quantity)]);
    }
}

[ApiController]
[Route("api/orders")]
public class OrdersController(IOrderService service) : ControllerBase
{
    [HttpPost]
    public async Task<IActionResult> Create([FromBody] CreateOrderDto dto)
    {
        // [ApiController] auto-returns 400 if ModelState invalid
        var order = await service.CreateAsync(dto);
        return CreatedAtAction(nameof(Get), new { id = order.Id }, order);
    }

    [HttpGet("{id:int}")]
    public async Task<IActionResult> Get([FromRoute] int id) => Ok(await service.GetAsync(id));
}""",
        "language": "csharp",
        "key_points": [
            "[ApiController] auto-returns 400 on validation failure",
            "DataAnnotations on DTOs, not entity models",
            "[FromBody], [FromQuery], [FromRoute] control binding",
            "IValidatableObject for cross-field rules",
            "FluentValidation is a popular alternative",
        ],
    },
    "jwt-auth": {
        "explanation": (
            "**JWT (JSON Web Token)** authentication is **stateless** — the server validates a signed token on each request "
            "without storing session state. "
            "After login, the server issues a token containing **claims** (user ID, roles, email) signed with a secret or private key. "
            "Clients send `Authorization: Bearer <token>` on subsequent requests. "
            "The server validates **signature**, **issuer**, **audience**, and **expiry** before granting access. "
            "Use **short-lived access tokens** (15–60 min) plus **refresh tokens** for renewal without re-login. "
            "In ASP.NET Core, configure **`AddJwtBearer`** and call `UseAuthentication()` before `UseAuthorization()`. "
            "**Pitfall:** storing JWT secrets in source control — use **Azure Key Vault** or environment variables in production."
        ),
        "code": """// appsettings.json (dev only — use Key Vault in prod)
// "Jwt": { "Key": "...", "Issuer": "https://myapp.com", "Audience": "myapp-api" }

// Program.cs — JWT bearer authentication
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidIssuer = builder.Configuration["Jwt:Issuer"],
            ValidateAudience = true,
            ValidAudience = builder.Configuration["Jwt:Audience"],
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            IssuerSigningKey = new SymmetricSecurityKey(
                Encoding.UTF8.GetBytes(builder.Configuration["Jwt:Key"]!)),
            ClockSkew = TimeSpan.FromMinutes(1),
        };
    });

builder.Services.AddAuthorization();
var app = builder.Build();
app.UseAuthentication();  // must come before UseAuthorization
app.UseAuthorization();

// Protected endpoint
[Authorize]
[HttpGet("api/me")]
public IActionResult Me() => Ok(new
{
    Name = User.Identity?.Name,
    Roles = User.Claims.Where(c => c.Type == ClaimTypes.Role).Select(c => c.Value),
});""",
        "language": "csharp",
        "key_points": [
            "Bearer token in Authorization header",
            "Validate signature, issuer, audience, expiry",
            "Short-lived access token + refresh token pattern",
            "Stateless — no server session store needed",
            "Store signing keys in Key Vault, not appsettings",
        ],
    },
    "health-checks": {
        "explanation": (
            "**Health checks** expose an endpoint (typically `/health`) reporting whether the app and its dependencies are operational. "
            "Load balancers, **Kubernetes probes**, and Azure App Service use them to route traffic or restart unhealthy instances. "
            "Register checks with **`AddHealthChecks()`** — built-in providers for SQL Server, Redis, Azure Blob, HTTP endpoints. "
            "Each check returns **Healthy**, **Degraded**, or **Unhealthy**. "
            "**Liveness** probe — is the process alive? (restart if not). "
            "**Readiness** probe — can it accept traffic? (remove from load balancer if not). "
            "Use **Degraded** when non-critical dependencies are slow but the app still functions. "
            "**Pitfall:** exposing detailed exception messages on public `/health` — keep public responses minimal; use a secured detailed endpoint."
        ),
        "code": """// Program.cs — register health checks
builder.Services.AddHealthChecks()
    .AddSqlServer(
        connectionString: builder.Configuration.GetConnectionString("Sql")!,
        name: "sqlserver",
        tags: ["db", "ready"])
    .AddRedis(
        redisConnectionString: builder.Configuration["Redis:Connection"]!,
        name: "redis",
        tags: ["cache", "ready"])
    .AddCheck("self", () => HealthCheckResult.Healthy("App is running"));

var app = builder.Build();

// Public liveness — minimal response
app.MapHealthChecks("/health/live", new HealthCheckOptions
{
    Predicate = _ => false, // no dependency checks — just "am I alive?"
});

// Readiness — checks tagged dependencies
app.MapHealthChecks("/health/ready", new HealthCheckOptions
{
    Predicate = check => check.Tags.Contains("ready"),
    ResponseWriter = UIResponseWriter.WriteHealthCheckUIResponse,
});

app.Run();

// Kubernetes probe config (reference):
// livenessProbe:  GET /health/live
// readinessProbe: GET /health/ready""",
        "language": "csharp",
        "key_points": [
            "Healthy / Degraded / Unhealthy status values",
            "Liveness = process alive; Readiness = can serve traffic",
            "Built-in checks for SQL, Redis, HTTP, Azure services",
            "Kubernetes and load balancers consume /health",
            "Don't expose stack traces on public health endpoints",
        ],
    },
    "authorization-policies": {
        "explanation": (
            "ASP.NET Core **authorization** determines what an authenticated user **can do**. "
            "**Role-based** auth (`[Authorize(Roles = \"Admin\")]`) is simple but coarse — roles rarely capture real business rules. "
            "**Policy-based** auth combines requirements: roles, claims, custom **`IAuthorizationHandler`** logic. "
            "Register policies in `AddAuthorization()` and apply with `[Authorize(Policy = \"CanManageOrders\")]`. "
            "**Resource-based** auth checks ownership — e.g., a user can edit only their own orders via "
            "`IAuthorizationService.AuthorizeAsync(user, order, \"EditPolicy\")`. "
            "Follow **fail-closed** design — deny by default, grant explicitly. "
            "**Pitfall:** checking roles in business logic instead of declarative policies — scatters auth rules and makes testing harder."
        ),
        "code": """// Program.cs — define authorization policies
builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("CanManageOrders", policy =>
        policy.RequireRole("Admin", "Manager"));

    options.AddPolicy("SameCompany", policy =>
        policy.Requirements.Add(new SameCompanyRequirement()));

    options.AddPolicy("MinimumAge", policy =>
        policy.RequireClaim("age", "18", "19", "20")); // claim-based
});

builder.Services.AddSingleton<IAuthorizationHandler, SameCompanyHandler>();

// Custom requirement + handler
public record SameCompanyRequirement : IAuthorizationRequirement;

public class SameCompanyHandler : AuthorizationHandler<SameCompanyRequirement, Order>
{
    protected override Task HandleRequirementAsync(
        AuthorizationHandlerContext context,
        SameCompanyRequirement requirement,
        Order resource)
    {
        var userCompany = context.User.FindFirst("company_id")?.Value;
        if (userCompany == resource.CompanyId.ToString())
            context.Succeed(requirement);
        return Task.CompletedTask;
    }
}

[Authorize(Policy = "CanManageOrders")]
[HttpDelete("api/orders/{id:int}")]
public async Task<IActionResult> Delete(int id) => NoContent();""",
        "language": "csharp",
        "key_points": [
            "Roles = simple; policies = flexible combinations",
            "IAuthorizationHandler for custom business rules",
            "Resource-based auth for ownership checks",
            "Fail closed — deny by default",
            "Use [Authorize(Policy)] not inline role checks",
        ],
    },
    "filters": {
        "explanation": (
            "**Filters** are ASP.NET Core's extensibility points for **cross-cutting MVC concerns** that run around action execution. "
            "Filter types (in execution order): **Authorization filters** → **Resource filters** → **Action filters** → "
            "**Exception filters** → **Result filters**. "
            "**Action filters** (`IActionFilter`, `IAsyncActionFilter`) run before/after the action method — "
            "ideal for model validation, logging, or injecting context. "
            "**Exception filters** handle unhandled exceptions at the action level (global middleware is often preferred). "
            "Apply via attributes (`[ServiceFilter]`, `[TypeFilter]`), global registration, or base controller. "
            "**When to use:** validation shortcuts, audit logging, performance timing on specific controllers. "
            "**Pitfall:** duplicating middleware logic in filters — middleware runs for all requests; filters only for MVC actions."
        ),
        "code": """// Custom action filter — validate model before action runs
public class ValidateModelAttribute : ActionFilterAttribute
{
    public override void OnActionExecuting(ActionExecutingContext context)
    {
        if (!context.ModelState.IsValid)
        {
            context.Result = new BadRequestObjectResult(new ValidationProblemDetails(
                context.ModelState));
        }
    }
}

// Async action filter — preferred for I/O
public class AuditLogFilter(ILogger<AuditLogFilter> logger) : IAsyncActionFilter
{
    public async Task OnActionExecutionAsync(
        ActionExecutingContext context,
        ActionExecutionDelegate next)
    {
        var user = context.HttpContext.User.Identity?.Name ?? "anonymous";
        logger.LogInformation("User {User} calling {Action}", user,
            context.ActionDescriptor.DisplayName);

        var executed = await next(); // run the action

        logger.LogInformation("Action returned {StatusCode}",
            context.HttpContext.Response.StatusCode);
    }
}

// Apply to controller or action
[ServiceFilter(typeof(AuditLogFilter))]
[ValidateModel]
[HttpPost("api/orders")]
public IActionResult Create([FromBody] CreateOrderDto dto) => Ok();""",
        "language": "csharp",
        "key_points": [
            "Order: Authorization → Resource → Action → Exception → Result",
            "IAsyncActionFilter preferred for async work",
            "ServiceFilter resolves from DI container",
            "Filters run only for MVC/minimal with filter support",
            "Middleware for all requests; filters for action-specific logic",
        ],
    },
    "environments": {
        "explanation": (
            "ASP.NET Core uses the **`ASPNETCORE_ENVIRONMENT`** variable to select behavior and configuration per deployment target. "
            "Built-in names: **Development**, **Staging**, **Production** — you can define custom names. "
            "Configuration loads in order: `appsettings.json` → `appsettings.{Environment}.json` → environment variables → "
            "command-line args (later sources override earlier). "
            "**Development** enables detailed error pages, Swagger, and verbose logging. "
            "**Production** should use generic error handlers, disable Swagger publicly, and enforce HTTPS/HSTS. "
            "Check environment with **`IWebHostEnvironment`** or `app.Environment.IsDevelopment()`. "
            "**Pitfall:** leaving Swagger UI publicly accessible in Production — a common security finding."
        ),
        "code": """// launchSettings.json sets ASPNETCORE_ENVIRONMENT locally
// "ASPNETCORE_ENVIRONMENT": "Development"

// Program.cs — environment-specific behavior
var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
    app.UseDeveloperExceptionPage(); // detailed stack traces — dev only
}
else
{
    app.UseExceptionHandler("/error");  // generic error page
    app.UseHsts();                       // strict transport security
}

// appsettings.Production.json overrides appsettings.json
// {
//   "Logging": { "LogLevel": { "Default": "Warning" } },
//   "AllowedHosts": "api.mycompany.com"
// }

// Access environment in a service
public class FeatureService(IWebHostEnvironment env)
{
    public bool ShowDebugInfo => env.IsDevelopment();
    public string EnvironmentName => env.EnvironmentName;
}

// Set in Azure App Service: Configuration → ASPNETCORE_ENVIRONMENT = Production""",
        "language": "csharp",
        "key_points": [
            "ASPNETCORE_ENVIRONMENT drives config and behavior",
            "Development / Staging / Production built-in names",
            "appsettings.{Environment}.json overrides base config",
            "Never expose Swagger or detailed errors in Production",
            "Use feature flags for finer-grained toggles",
        ],
    },
    "identity": {
        "explanation": (
            "**ASP.NET Core Identity** is a membership system providing **user management**, **password hashing**, "
            "**role and claim** storage, **lockout**, **two-factor authentication**, and **external login** providers. "
            "It ships with **`UserManager<TUser>`**, **`SignInManager<TUser>`**, and **`RoleManager<TRole>`** APIs. "
            "Default storage uses **EF Core** (`AddEntityFrameworkStores<AppDbContext>()`), but you can plug custom stores. "
            "Identity handles **cookie-based** auth for MVC/Razor and integrates with **JWT** for SPAs and mobile clients. "
            "It is **separate from Entra ID (Azure AD)** — Identity is app-local users; Entra ID is organizational SSO "
            "(though they can coexist). "
            "**When to use:** apps needing registration, login, password reset, and role management out of the box. "
            "**Pitfall:** rolling your own password hashing — always use Identity's built-in `PasswordHasher`."
        ),
        "code": """// Program.cs — configure ASP.NET Core Identity
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("Sql")));

builder.Services.AddIdentity<ApplicationUser, IdentityRole>(options =>
{
    options.Password.RequiredLength = 12;
    options.Password.RequireDigit = true;
    options.Lockout.MaxFailedAccessAttempts = 5;
    options.User.RequireUniqueEmail = true;
})
.AddEntityFrameworkStores<AppDbContext>()
.AddDefaultTokenProviders(); // password reset, email confirmation tokens

// For API + SPA — combine Identity with JWT
builder.Services.AddAuthentication(options =>
{
    options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
    options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
})
.AddJwtBearer(/* token validation parameters */);

// Account controller usage
public class AccountController(UserManager<ApplicationUser> users, SignInManager<ApplicationUser> signIn) : ControllerBase
{
    [HttpPost("register")]
    public async Task<IActionResult> Register([FromBody] RegisterDto dto)
    {
        var user = new ApplicationUser { UserName = dto.Email, Email = dto.Email };
        var result = await users.CreateAsync(user, dto.Password);
        return result.Succeeded ? Ok() : BadRequest(result.Errors);
    }
}""",
        "language": "csharp",
        "key_points": [
            "UserManager, SignInManager, RoleManager are core APIs",
            "EF Core stores by default; custom stores supported",
            "Built-in password hashing, lockout, 2FA, external logins",
            "Cookie auth for MVC; JWT for SPA/API clients",
            "Separate from Entra ID — can integrate both",
        ],
    },
}
