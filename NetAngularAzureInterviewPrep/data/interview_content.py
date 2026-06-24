"""Structured .NET + Angular + Azure interview Q&A content — phase-wise."""

from dataclasses import dataclass, field


@dataclass
class InterviewItem:
    id: str
    question: str
    explanation: str
    code: str = ""
    language: str = "csharp"
    key_points: list[str] = field(default_factory=list)


@dataclass
class Phase:
    id: str
    label: str
    items: list[InterviewItem]


@dataclass
class Section:
    id: str
    title: str
    emoji: str
    color: str
    subtitle: str
    phases: list[Phase]


SECTIONS: dict[str, Section] = {
    "dotnet": Section(
        id="dotnet",
        title="Core .NET",
        emoji="🟣",
        color="#512BD4",
        subtitle="C# fundamentals from beginner to expert",
        phases=[
            Phase("foundation", "Foundation", [
                InterviewItem(
                    "dotnet-core-vs-framework",
                    "What is the difference between .NET Core and .NET Framework?",
                    "**.NET Framework** (4.x) is Windows-only, monolithic, and in maintenance mode. "
                    "**.NET (5/6/7/8+)** is cross-platform, modular, open-source, faster, and supports "
                    "side-by-side installs. New greenfield apps should target **.NET 8 LTS**. "
                    "Use Framework only for legacy apps (WCF, Web Forms, old libraries).",
                    """// Modern .NET 8 minimal API
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/health", () => Results.Ok(new { status = "healthy" }));
app.Run();""",
                    key_points=[
                        ".NET 8 = current LTS for production",
                        "Cross-platform: Windows, Linux, macOS",
                        ".NET Standard bridged old libs — less needed today",
                    ],
                ),
                InterviewItem(
                    "di-lifetimes",
                    "Explain Dependency Injection and service lifetimes in ASP.NET Core.",
                    "DI implements **Inversion of Control** — classes receive dependencies instead of using `new`. "
                    "Register services in `Program.cs`. Lifetimes matter for correctness and performance.",
                    """// Program.cs
builder.Services.AddSingleton<ICacheService, MemoryCacheService>();
builder.Services.AddScoped<IOrderRepository, OrderRepository>();
builder.Services.AddTransient<IEmailSender, SmtpEmailSender>();

// Constructor injection in a service
public class OrderService(IOrderRepository repo, IEmailSender email)
{
    public async Task PlaceOrderAsync(Order order)
    {
        await repo.SaveAsync(order);
        await email.SendAsync(order.CustomerEmail, "Order confirmed");
    }
}""",
                    key_points=[
                        "Singleton — one instance per application",
                        "Scoped — one per HTTP request (ideal for DbContext)",
                        "Transient — new instance every injection",
                    ],
                ),
                InterviewItem(
                    "ref-vs-value",
                    "What is the difference between reference types and value types?",
                    "Value types (`int`, `struct`, `enum`) store data directly; copying copies the value. "
                    "Reference types (`class`, `string`, arrays) store a reference to heap memory; "
                    "copying copies the reference (both point to same object).",
                    """int a = 10, b = a;   // b = 10 (copy)
b = 20;              // a still 10

var list1 = new List<int> { 1, 2 };
var list2 = list1;   // same reference
list2.Add(3);        // list1 also has 3

// Use struct for small immutable value objects
public readonly record struct Money(decimal Amount, string Currency);""",
                    key_points=[
                        "struct = value type on stack (usually)",
                        "class = reference type on heap",
                        "string is immutable reference type",
                    ],
                ),
                InterviewItem(
                    "abstract-vs-interface",
                    "When do you use an abstract class vs an interface?",
                    "Use an **interface** for a capability contract (multiple inheritance). "
                    "Use an **abstract class** when you share base state or default behavior. "
                    "Prefer interfaces for DI and testability.",
                    """public interface IPaymentGateway
{
    Task<PaymentResult> ChargeAsync(decimal amount);
}

public abstract class EntityBase
{
    public Guid Id { get; protected set; }
    public DateTime CreatedAt { get; protected set; }
}

public class Order : EntityBase { /* ... */ }""",
                    key_points=[
                        "Interface: can implement many",
                        "Abstract class: single inheritance",
                        "C# 8+ interfaces can have default implementations",
                    ],
                ),
                InterviewItem(
                    "collections",
                    "Which .NET collection would you use and when?",
                    "Choose by access pattern: indexed list, key lookup, uniqueness, or ordering.",
                    """var list = new List<string> { "a", "b" };       // ordered, indexable
var dict = new Dictionary<int, string> { [1] = "one" }; // O(1) lookup
var set = new HashSet<int> { 1, 2, 2 };             // unique: {1,2}
var queue = new Queue<string>();                    // FIFO
var stack = new Stack<int>();                       // LIFO""",
                    key_points=[
                        "Dictionary for key-value lookups",
                        "HashSet for duplicate detection",
                        "List<T> is the default ordered collection",
                    ],
                ),
            ]),
            Phase("intermediate", "Intermediate", [
                InterviewItem(
                    "async-await",
                    "Explain async/await. When should you use it?",
                    "Use `async/await` for **I/O-bound** work (HTTP, DB, files) — frees threads while waiting. "
                    "Do NOT wrap purely CPU-bound work in fake async. Avoid `.Result` and `.Wait()` — they cause deadlocks.",
                    """// Good: I/O-bound
public async Task<Order?> GetOrderAsync(int id, CancellationToken ct)
{
    return await _db.Orders.AsNoTracking()
        .FirstOrDefaultAsync(o => o.Id == id, ct);
}

// CPU-bound offload
public Task<int> ComputeHashAsync(byte[] data) =>
    Task.Run(() => SHA256.HashData(data));

// Controller — CancellationToken auto-bound from client disconnect
[HttpGet("{id}")]
public async Task<IActionResult> Get(int id, CancellationToken ct)
    => Ok(await _service.GetOrderAsync(id, ct));""",
                    key_points=[
                        "async doesn't create a thread — it releases one",
                        "Always pass CancellationToken in long operations",
                        "ConfigureAwait(false) in library code",
                    ],
                ),
                InterviewItem(
                    "options-pattern",
                    "What is the Options pattern in ASP.NET Core?",
                    "Binds configuration sections to strongly-typed POCOs. Supports validation and `IOptions<T>`, "
                    "`IOptionsSnapshot<T>` (per-request reload), `IOptionsMonitor<T>` (change notifications).",
                    """// appsettings.json: "Smtp": { "Host": "smtp.example.com", "Port": 587 }

public class SmtpSettings
{
    public const string Section = "Smtp";
    public string Host { get; set; } = "";
    public int Port { get; set; }
}

// Program.cs
builder.Services.Configure<SmtpSettings>(
    builder.Configuration.GetSection(SmtpSettings.Section));

// Usage
public class MailService(IOptions<SmtpSettings> options)
{
    private readonly SmtpSettings _smtp = options.Value;
}""",
                    key_points=[
                        "Prefer IOptions<T> for singleton config",
                        "IOptionsSnapshot for scoped reload per request",
                        "Validate with DataAnnotations or IValidateOptions<T>",
                    ],
                ),
                InterviewItem(
                    "generics",
                    "What are generics and why use them?",
                    "Generics provide type-safe, reusable code without boxing for value types. "
                    "Constraints limit type parameters.",
                    """public interface IRepository<T> where T : class
{
    Task<T?> GetByIdAsync(int id);
    Task AddAsync(T entity);
}

public static T Max<T>(T a, T b) where T : IComparable<T>
    => a.CompareTo(b) > 0 ? a : b;""",
                    key_points=[
                        "Avoid object casting and boxing",
                        "Constraints: class, struct, new(), base class, interface",
                        "Used everywhere: List<T>, IEnumerable<T>, Task<T>",
                    ],
                ),
            ]),
            Phase("advanced", "Advanced", [
                InterviewItem(
                    "thread-sync",
                    "Compare lock, SemaphoreSlim, and Mutex.",
                    "`lock` (Monitor) — mutual exclusion in-process. "
                    "`SemaphoreSlim` — limit N concurrent threads (e.g. throttle API calls). "
                    "`Mutex` — cross-process synchronization (rare).",
                    """private readonly object _gate = new();
private int _count;

public void Increment()
{
    lock (_gate) { _count++; }  // thread-safe
}

// SemaphoreSlim: max 3 concurrent
private readonly SemaphoreSlim _sem = new(3);

public async Task ThrottledCallAsync()
{
    await _sem.WaitAsync();
    try { await CallExternalApiAsync(); }
    finally { _sem.Release(); }
}""",
                    key_points=[
                        "Prefer async + SemaphoreSlim over lock for I/O",
                        "lock is re-entrant for same thread",
                        "Avoid locking on `this` or public objects",
                    ],
                ),
                InterviewItem(
                    "task-cancellation",
                    "How does task cancellation work?",
                    "Use `CancellationTokenSource` to signal cancellation. Pass `CancellationToken` through async chain. "
                    "Cooperative cancellation — code must check the token.",
                    """var cts = new CancellationTokenSource(TimeSpan.FromSeconds(30));

try
{
    await ProcessBatchAsync(items, cts.Token);
}
catch (OperationCanceledException)
{
    _logger.LogWarning("Batch cancelled");
}

public async Task ProcessBatchAsync(IEnumerable<Item> items, CancellationToken ct)
{
    foreach (var item in items)
    {
        ct.ThrowIfCancellationRequested();
        await ProcessOneAsync(item, ct);
    }
}""",
                    key_points=[
                        "Cancellation is cooperative, not forced",
                        "ASP.NET Core passes token to action methods",
                        "Link tokens with CancellationTokenSource.CreateLinkedTokenSource",
                    ],
                ),
            ]),
        ],
    ),
    "aspnet": Section(
        id="aspnet",
        title="ASP.NET Core",
        emoji="🔵",
        color="#0078D4",
        subtitle="REST APIs, middleware, auth, and security",
        phases=[
            Phase("foundation", "Foundation", [
                InterviewItem(
                    "rest-principles",
                    "What are REST principles?",
                    "REST uses **resources** (nouns), **HTTP verbs**, **statelessness**, and **standard status codes**. "
                    "URLs represent resources; body carries representation (usually JSON).",
                    """// RESTful routes
GET    /api/orders          → list
GET    /api/orders/42       → get one
POST   /api/orders          → create (201)
PUT    /api/orders/42       → full replace
PATCH  /api/orders/42       → partial update
DELETE /api/orders/42       → delete (204)""",
                    "text",
                    key_points=[
                        "200 OK, 201 Created, 400 Bad Request, 401 Unauthorized",
                        "404 Not Found, 409 Conflict, 500 Internal Server Error",
                        "Use nouns not verbs in URLs",
                    ],
                ),
                InterviewItem(
                    "middleware",
                    "Explain the ASP.NET Core middleware pipeline.",
                    "Middleware forms a chain — each can run code before and after `next()`. "
                    "Order matters: Exception handling → HTTPS → Routing → Auth → Authorization → Endpoints.",
                    """public class RequestTimingMiddleware(RequestDelegate next, ILogger<RequestTimingMiddleware> log)
{
    public async Task InvokeAsync(HttpContext context)
    {
        var sw = Stopwatch.StartNew();
        await next(context);
        sw.Stop();
        log.LogInformation("{Method} {Path} => {Status} in {Ms}ms",
            context.Request.Method, context.Request.Path,
            context.Response.StatusCode, sw.ElapsedMilliseconds);
    }
}

// Program.cs
app.UseMiddleware<RequestTimingMiddleware>();""",
                    key_points=[
                        "UseAuthentication before UseAuthorization",
                        "Terminal middleware doesn't call next",
                        "Built-in: UseCors, UseStaticFiles, UseRouting",
                    ],
                ),
                InterviewItem(
                    "model-validation",
                    "How does model binding and validation work?",
                    "`[ApiController]` enables automatic 400 on validation failure. "
                    "Data annotations on DTOs; custom `IValidatableObject` for complex rules.",
                    """public record CreateOrderDto(
    [Required] string CustomerName,
    [Range(1, 100)] int Quantity,
    [EmailAddress] string Email);

[HttpPost]
public async Task<IActionResult> Create([FromBody] CreateOrderDto dto)
{
    // With [ApiController], invalid ModelState returns 400 automatically
    var order = await _service.CreateAsync(dto);
    return CreatedAtAction(nameof(Get), new { id = order.Id }, order);
}""",
                    key_points=[
                        "[FromBody], [FromQuery], [FromRoute] control binding source",
                        "FluentValidation is a popular alternative",
                        "Never trust client input — validate server-side",
                    ],
                ),
            ]),
            Phase("intermediate", "Intermediate", [
                InterviewItem(
                    "jwt-auth",
                    "How does JWT authentication work in ASP.NET Core?",
                    "Client sends `Authorization: Bearer <token>`. Server validates signature, issuer, audience, expiry. "
                    "Claims carry identity and roles. Stateless — no server session store.",
                    """// Program.cs
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
            IssuerSigningKey = new SymmetricSecurityKey(
                Encoding.UTF8.GetBytes(builder.Configuration["Jwt:Key"]!))
        };
    });

app.UseAuthentication();
app.UseAuthorization();

[Authorize]
[HttpGet("me")]
public IActionResult Me() => Ok(User.Identity?.Name);""",
                    key_points=[
                        "Access token short-lived; refresh token for renewal",
                        "Store secrets in Azure Key Vault, not appsettings in prod",
                        "HTTPS required in production",
                    ],
                ),
                InterviewItem(
                    "health-checks",
                    "What are health checks and why use them?",
                    "Expose `/health` for load balancers and Kubernetes. "
                    "Verify DB, Redis, downstream APIs — return Healthy/Degraded/Unhealthy.",
                    """builder.Services.AddHealthChecks()
    .AddSqlServer(connectionString, name: "sql")
    .AddRedis(redisConnection, name: "redis");

app.MapHealthChecks("/health", new HealthCheckOptions
{
    ResponseWriter = UIResponseWriter.WriteHealthCheckUIResponse
});""",
                    key_points=[
                        "Liveness vs readiness probes in Kubernetes",
                        "Degraded = app runs but dependency slow",
                        "Don't expose detailed errors publicly",
                    ],
                ),
            ]),
            Phase("advanced", "Advanced", [
                InterviewItem(
                    "authorization-policies",
                    "Compare role-based vs policy-based authorization.",
                    "Roles are simple but coarse. Policies combine requirements (claims, roles, custom handlers) — more flexible.",
                    """builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("CanManageOrders", policy =>
        policy.RequireRole("Admin", "Manager"));

    options.AddPolicy("SameCompany", policy =>
        policy.Requirements.Add(new SameCompanyRequirement()));
});

[Authorize(Policy = "CanManageOrders")]
[HttpDelete("{id}")]
public async Task<IActionResult> Delete(int id) => Ok();""",
                    key_points=[
                        "Resource-based auth: user can edit own record only",
                        "IAuthorizationHandler for custom logic",
                        "Fail closed — deny by default",
                    ],
                ),
            ]),
        ],
    ),
    "frontend": Section(
        id="frontend",
        title="Angular & TypeScript",
        emoji="🔴",
        color="#DD0031",
        subtitle="JavaScript, TypeScript, Angular, HTML/CSS",
        phases=[
            Phase("foundation", "Foundation", [
                InterviewItem(
                    "js-closures",
                    "What is a closure in JavaScript?",
                    "A function that remembers variables from its lexical scope even after the outer function returns.",
                    """function createCounter() {
  let count = 0;
  return {
    increment: () => ++count,
    getCount: () => count
  };
}

const counter = createCounter();
counter.increment(); // 1
counter.getCount();  // 1 — closure kept `count` alive""",
                    "javascript",
                    key_points=[
                        "Common in callbacks and event handlers",
                        "Watch for stale closures in loops — use let or IIFE",
                        "Angular services use closures for private state",
                    ],
                ),
                InterviewItem(
                    "ts-interfaces",
                    "Interfaces vs types in TypeScript?",
                    "Interfaces are extendable and mergeable. Types support unions, intersections, primitives. "
                    "Use interfaces for object shapes; types for unions/utility types.",
                    """interface User {
  id: number;
  name: string;
}

interface Admin extends User {
  permissions: string[];
}

type Result<T> = { success: true; data: T } | { success: false; error: string };

type PartialUser = Partial<User>;""",
                    "typescript",
                    key_points=[
                        "strict mode catches null/undefined bugs",
                        "generics: ApiResponse<T>",
                        "Angular heavily uses interfaces for models",
                    ],
                ),
            ]),
            Phase("intermediate", "Intermediate", [
                InterviewItem(
                    "angular-di",
                    "How does Dependency Injection work in Angular?",
                    "Angular's injector creates and provides services. `providedIn: 'root'` = app-wide singleton. "
                    "Component providers create instance per component subtree.",
                    """@Injectable({ providedIn: 'root' })
export class OrderService {
  constructor(private http: HttpClient) {}

  getOrders(): Observable<Order[]> {
    return this.http.get<Order[]>('/api/orders');
  }
}

@Component({
  selector: 'app-orders',
  template: `<ul><li *ngFor="let o of orders$ | async">{{ o.id }}</li></ul>`
})
export class OrdersComponent {
  orders$ = inject(OrderService).getOrders();
}""",
                    "typescript",
                    key_points=[
                        "inject() function (Angular 14+) vs constructor DI",
                        "Hierarchical injectors — child can override parent",
                        "Use services for shared state and HTTP",
                    ],
                ),
                InterviewItem(
                    "rxjs-operators",
                    "Explain common RxJS operators used in Angular.",
                    "Observables stream values over time. Operators transform streams. "
                    "Critical for HTTP, forms, and real-time UI.",
                    """// switchMap — cancel previous request (search box)
this.search$.pipe(
  debounceTime(300),
  distinctUntilChanged(),
  switchMap(term => this.api.search(term))
).subscribe(results => this.results = results);

// catchError — handle HTTP errors
this.http.get<Order[]>('/api/orders').pipe(
  catchError(err => {
    this.toast.error('Failed to load orders');
    return of([]);
  })
);

// takeUntil — unsubscribe on destroy
private destroy$ = new Subject<void>();
ngOnDestroy() { this.destroy$.next(); this.destroy$.complete(); }""",
                    "typescript",
                    key_points=[
                        "switchMap vs mergeMap vs concatMap — concurrency differs",
                        "Always unsubscribe or use async pipe",
                        "BehaviorSubject for shared state",
                    ],
                ),
                InterviewItem(
                    "reactive-forms",
                    "Reactive vs template-driven forms?",
                    "Reactive forms are model-driven, testable, synchronous access to values. "
                    "Template-driven are simpler for basic forms. Prefer reactive for complex validation.",
                    """this.form = this.fb.group({
  email: ['', [Validators.required, Validators.email]],
  quantity: [1, [Validators.required, Validators.min(1)]]
});

onSubmit() {
  if (this.form.invalid) return;
  const value = this.form.value as OrderForm;
  this.orderService.create(value).subscribe();
}""",
                    "typescript",
                    key_points=[
                        "FormBuilder, FormGroup, FormControl",
                        "Custom validators for business rules",
                        "Typed forms in Angular 14+",
                    ],
                ),
            ]),
            Phase("advanced", "Advanced", [
                InterviewItem(
                    "change-detection",
                    "How does Angular change detection work? How do you optimize it?",
                    "Default strategy checks entire component tree on events. "
                    "`ChangeDetectionStrategy.OnPush` checks only on @Input reference change, events, or async pipe.",
                    """@Component({
  selector: 'app-order-row',
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `<span>{{ order.id }} — {{ order.total | currency }}</span>`
})
export class OrderRowComponent {
  @Input({ required: true }) order!: Order;
}

// Immutable updates trigger OnPush
this.orders = [...this.orders, newOrder];""",
                    "typescript",
                    key_points=[
                        "async pipe triggers CD when Observable emits",
                        "Avoid mutating @Input objects in place with OnPush",
                        "Signals (Angular 16+) simplify reactivity",
                    ],
                ),
            ]),
        ],
    ),
    "database": Section(
        id="database",
        title="Database & EF Core",
        emoji="🟢",
        color="#059669",
        subtitle="SQL, Entity Framework, Dapper, performance",
        phases=[
            Phase("foundation", "Foundation", [
                InterviewItem(
                    "sql-joins",
                    "Explain SQL JOIN types with an example.",
                    "JOINs combine rows from tables based on related keys.",
                    """-- Customers and their orders (INNER — only customers WITH orders)
SELECT c.Name, o.OrderDate, o.Total
FROM Customers c
INNER JOIN Orders o ON o.CustomerId = c.Id;

-- All customers, even without orders (LEFT)
SELECT c.Name, COUNT(o.Id) AS OrderCount
FROM Customers c
LEFT JOIN Orders o ON o.CustomerId = c.Id
GROUP BY c.Id, c.Name;""",
                    "sql",
                    key_points=[
                        "INNER = intersection",
                        "LEFT = all from left + matching right",
                        "Always index foreign key columns",
                    ],
                ),
                InterviewItem(
                    "ef-core-basics",
                    "What is Entity Framework Core? Code First vs Database First?",
                    "**EF Core** is an ORM mapping C# classes to tables. **Code First**: define models → migrations → DB. "
                    "**Database First**: scaffold from existing DB. Code First is standard for new apps.",
                    """public class Order
{
    public int Id { get; set; }
    public string CustomerName { get; set; } = "";
    public List<OrderLine> Lines { get; set; } = [];
}

public class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options)
{
    public DbSet<Order> Orders => Set<Order>();

    protected override void OnModelCreating(ModelBuilder model)
    {
        model.Entity<Order>()
            .HasMany(o => o.Lines)
            .WithOne()
            .HasForeignKey("OrderId");
    }
}""",
                    key_points=[
                        "DbContext is Scoped per request in web apps",
                        "Migrations version-control schema",
                        "Fluent API for complex mappings",
                    ],
                ),
            ]),
            Phase("intermediate", "Intermediate", [
                InterviewItem(
                    "linq-queries",
                    "Write efficient LINQ queries in EF Core.",
                    "Prefer `IQueryable` composition so SQL runs on DB, not in memory. "
                    "Use projection to select only needed columns.",
                    """// Bad — loads entire table into memory
var all = await _db.Orders.ToListAsync();
var filtered = all.Where(o => o.Total > 100);

// Good — SQL WHERE on server
var orders = await _db.Orders
    .AsNoTracking()
    .Where(o => o.Total > 100)
    .Select(o => new OrderSummary(o.Id, o.CustomerName, o.Total))
    .ToListAsync();""",
                    key_points=[
                        "AsNoTracking for read-only queries",
                        "Select DTO projection avoids over-fetching",
                        "ToListAsync only when materializing",
                    ],
                ),
                InterviewItem(
                    "n-plus-one",
                    "What is the N+1 query problem? How do you fix it?",
                    "Loading N parent records then 1 query per child = N+1 total queries. "
                    "Fix with `.Include()`, `.ThenInclude()`, or explicit projection.",
                    """// N+1 problem
var orders = await _db.Orders.ToListAsync();
foreach (var o in orders)
    Console.WriteLine(o.Lines.Count); // lazy-loads each time!

// Fix with Include
var orders = await _db.Orders
    .Include(o => o.Lines)
    .AsNoTracking()
    .ToListAsync();

// Or projection (single query, no tracking overhead)
var dtos = await _db.Orders
    .Select(o => new { o.Id, LineCount = o.Lines.Count })
    .ToListAsync();""",
                    key_points=[
                        "Enable SQL logging in Development to spot N+1",
                        "Split queries in EF 5+ for large includes",
                        "Dapper for hand-tuned SQL when needed",
                    ],
                ),
            ]),
            Phase("advanced", "Advanced", [
                InterviewItem(
                    "transactions",
                    "How do you handle transactions in EF Core?",
                    "Use `BeginTransactionAsync` for multiple SaveChanges or raw SQL in one atomic unit. "
                    "Understand isolation levels for concurrency.",
                    """await using var transaction = await _db.Database.BeginTransactionAsync();
try
{
    var order = new Order { CustomerName = "Alice" };
    _db.Orders.Add(order);
    await _db.SaveChangesAsync();

    await _db.Database.ExecuteSqlRawAsync(
        "UPDATE Inventory SET Qty = Qty - 1 WHERE ProductId = {0}", productId);

    await transaction.CommitAsync();
}
catch
{
    await transaction.RollbackAsync();
    throw;
}""",
                    "sql",
                    key_points=[
                        "SaveChanges is already a transaction by default",
                        "Serializable prevents phantom reads — slower",
                        "Use optimistic concurrency with RowVersion",
                    ],
                ),
            ]),
        ],
    ),
    "azure": Section(
        id="azure",
        title="Microsoft Azure",
        emoji="☁️",
        color="#0078D4",
        subtitle="Cloud services, DevOps, and architecture",
        phases=[
            Phase("foundation", "Foundation", [
                InterviewItem(
                    "app-service",
                    "What is Azure App Service? When do you use it?",
                    "PaaS for hosting web apps and APIs without managing VMs. "
                    "Built-in scaling, deployment slots, custom domains, TLS.",
                    """# Deploy .NET API to App Service
az webapp up --name my-order-api --resource-group rg-prod --runtime "DOTNET:8"

# Deployment slots for blue-green
az webapp deployment slot create --name my-order-api --slot staging
az webapp deployment slot swap --name my-order-api --slot staging""",
                    "bash",
                    key_points=[
                        "Deployment slots: swap staging → production",
                        "Scale out (more instances) vs scale up (bigger VM)",
                        "Pair with Application Insights",
                    ],
                ),
                InterviewItem(
                    "key-vault",
                    "Why use Azure Key Vault?",
                    "Centralized secrets, keys, certificates. Apps use **Managed Identity** — no secrets in code or config files.",
                    """// Program.cs — load secrets from Key Vault
var keyVaultUrl = builder.Configuration["KeyVault:Url"];
builder.Configuration.AddAzureKeyVault(
    new Uri(keyVaultUrl!),
    new DefaultAzureCredential());

// Access in code like any config
var sqlConnection = builder.Configuration["SqlConnectionString"];""",
                    key_points=[
                        "Managed Identity eliminates stored credentials",
                        "Rotate secrets without redeploying code",
                        "RBAC controls who accesses vault",
                    ],
                ),
                InterviewItem(
                    "app-insights",
                    "What does Application Insights provide?",
                    "APM: request rates, failures, dependency calls (SQL, HTTP), distributed tracing, custom metrics, live metrics.",
                    """// Custom telemetry
public class OrderService(TelemetryClient telemetry)
{
    public async Task PlaceOrderAsync(Order order)
    {
        using var op = telemetry.StartOperation<RequestTelemetry>("PlaceOrder");
        telemetry.TrackEvent("OrderPlaced", new Dictionary<string, string>
        {
            ["OrderId"] = order.Id.ToString()
        });
    }
}""",
                    key_points=[
                        "Correlate requests across microservices",
                        "Alerts on failure rate spikes",
                        "Integrated with ASP.NET Core OpenTelemetry",
                    ],
                ),
            ]),
            Phase("intermediate", "Intermediate", [
                InterviewItem(
                    "azure-devops-cicd",
                    "Describe a CI/CD pipeline for .NET + Angular on Azure.",
                    "PR triggers build + tests. Main branch deploys to staging slot, runs smoke tests, swaps to production.",
                    """# azure-pipelines.yml (simplified)
trigger:
  - main

stages:
  - stage: Build
    jobs:
      - job: BuildApi
        steps:
          - task: DotNetCoreCLI@2
            inputs: { command: 'test', projects: '**/*Tests.csproj' }
          - task: DotNetCoreCLI@2
            inputs: { command: 'publish', publishWebProjects: true }
      - job: BuildWeb
        steps:
          - script: npm ci && npm run build --prefix ClientApp

  - stage: Deploy
    jobs:
      - deployment: DeployApi
        environment: production
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs: { appName: 'my-order-api' }""",
                    "yaml",
                    key_points=[
                        "Run unit + integration tests before deploy",
                        "Use deployment slots for zero-downtime",
                        "Store pipeline secrets in variable groups / Key Vault",
                    ],
                ),
                InterviewItem(
                    "service-bus",
                    "Azure Service Bus vs Storage Queue?",
                    "Service Bus: enterprise messaging, topics/subscriptions, transactions, dead-letter. "
                    "Storage Queue: simple, cheap, high throughput for basic queueing.",
                    """// Sender
await using var client = new ServiceBusClient(connectionString);
var sender = client.CreateSender("order-placed");
await sender.SendMessageAsync(new ServiceBusMessage(JsonSerializer.Serialize(orderEvent)));

// Azure Function trigger
[Function(nameof(ProcessOrder))]
public async Task ProcessOrder(
    [ServiceBusTrigger("order-placed", Connection = "ServiceBus")]
    ServiceBusReceivedMessage message) { /* ... */ }""",
                    key_points=[
                        "Use topics for pub/sub (multiple subscribers)",
                        "Dead-letter queue for failed messages",
                        "Idempotent consumers — messages may duplicate",
                    ],
                ),
            ]),
            Phase("advanced", "Advanced", [
                InterviewItem(
                    "full-architecture",
                    "Design a full-stack .NET + Angular system on Azure.",
                    "Classic interview architecture question — tie services together with security and observability.",
                    """/*
  User Browser
      │
      ▼
  Azure Front Door / CDN  ──► Angular (Static Web Apps)
      │
      ▼
  API Management (rate limit, JWT validation)
      │
      ▼
  App Service / AKS (.NET 8 API)
      ├── Azure SQL (orders)
      ├── Redis Cache (session / cache)
      ├── Service Bus (async events)
      ├── Azure Functions (notifications)
      └── Key Vault (connection strings)

  Entra ID (Azure AD) ── JWT ──► API
  Application Insights ── all telemetry
*/""",
                    "text",
                    key_points=[
                        "Managed Identity between Azure services",
                        "Redis reduces DB load for hot data",
                        "Async processing via Service Bus + Functions",
                    ],
                ),
            ]),
        ],
    ),
    "practices": Section(
        id="practices",
        title="Best Practices",
        emoji="⭐",
        color="#F59E0B",
        subtitle="SOLID, testing, CI/CD, design patterns",
        phases=[
            Phase("foundation", "Foundation", [
                InterviewItem(
                    "solid",
                    "Explain SOLID principles with examples.",
                    "Five principles for maintainable OOP design — frequently asked at L3+.",
                    """// S — Single Responsibility: one class, one job
public class OrderValidator { public bool IsValid(Order o) => ... }
public class OrderRepository { public Task SaveAsync(Order o) => ... }

// D — Dependency Inversion: depend on abstractions
public class OrderService(IOrderRepository repo) { /* ... */ }

// O — Open/Closed: extend via new classes, not editing existing
public interface IDiscountStrategy { decimal Apply(Order o); }
public class TenPercentDiscount : IDiscountStrategy { ... }""",
                    key_points=[
                        "L — Liskov: subclasses must honor base contract",
                        "I — Interface Segregation: small focused interfaces",
                        "Don't memorize — explain with real refactoring story",
                    ],
                ),
            ]),
            Phase("intermediate", "Intermediate", [
                InterviewItem(
                    "unit-testing",
                    "How do you unit test ASP.NET Core services?",
                    "Use xUnit + Moq. Test business logic in isolation. WebApplicationFactory for integration tests.",
                    """public class OrderServiceTests
{
    [Fact]
    public async Task PlaceOrder_SavesAndSendsEmail()
    {
        var repo = new Mock<IOrderRepository>();
        var email = new Mock<IEmailSender>();
        var sut = new OrderService(repo.Object, email.Object);

        await sut.PlaceOrderAsync(new Order { CustomerEmail = "a@b.com" });

        repo.Verify(r => r.SaveAsync(It.IsAny<Order>()), Times.Once);
        email.Verify(e => e.SendAsync("a@b.com", It.IsAny<string>()), Times.Once);
    }
}""",
                    key_points=[
                        "Arrange-Act-Assert pattern",
                        "Test behavior not implementation details",
                        "Integration tests use Testcontainers for real SQL",
                    ],
                ),
                InterviewItem(
                    "test-pyramid",
                    "What is the test pyramid?",
                    "Many fast unit tests at base, fewer integration tests, minimal E2E UI tests at top. "
                    "Balances confidence vs speed and maintenance cost.",
                    """Unit Tests       ████████████  (70%) — ms each
Integration      ██████        (20%) — seconds
E2E / UI         ██            (10%) — minutes""",
                    "text",
                    key_points=[
                        "Don't test framework code",
                        "Mock external dependencies in unit tests",
                        "CI must run tests on every PR",
                    ],
                ),
            ]),
            Phase("advanced", "Advanced", [
                InterviewItem(
                    "microservices",
                    "When would you choose microservices over a monolith?",
                    "Microservices: independent deploy, scale, tech per service. Cost: distributed complexity, "
                    "network latency, eventual consistency. Start monolith; split when team/scale demands.",
                    """Monolith (modular)          Microservices
┌─────────────────┐         ┌──────┐ ┌──────┐ ┌──────┐
│ Orders │ Users  │         │Orders│ │Users │ │Notify│
│ Payments        │         └──┬───┘ └──┬───┘ └──┬───┘
└────────┬────────┘            └──────┴────────┘
         │                         Service Bus
    Single DB                   DB per service""",
                    "text",
                    key_points=[
                        "Bounded contexts from DDD guide service boundaries",
                        "API Gateway + Service Bus for communication",
                        "Observability is mandatory (correlation IDs)",
                    ],
                ),
            ]),
        ],
    ),
}


def get_all_sections() -> list[Section]:
    return list(SECTIONS.values())


def get_section(section_id: str) -> Section | None:
    return SECTIONS.get(section_id)


def count_items() -> int:
    return sum(len(p.items) for s in SECTIONS.values() for p in s.phases)


@dataclass
class SearchResult:
    section: Section
    phase: Phase
    item: InterviewItem


def iter_all_items() -> list[SearchResult]:
    results: list[SearchResult] = []
    for section in SECTIONS.values():
        for phase in section.phases:
            for item in phase.items:
                results.append(SearchResult(section, phase, item))
    return results


def search_items(
    query: str = "",
    section_ids: list[str] | None = None,
    phase_ids: list[str] | None = None,
) -> list[SearchResult]:
    query = query.strip().lower()
    results = iter_all_items()

    if section_ids:
        allowed = set(section_ids)
        results = [r for r in results if r.section.id in allowed]

    if phase_ids:
        allowed_phases = set(phase_ids)
        results = [r for r in results if r.phase.id in allowed_phases]

    if not query:
        return results

    filtered: list[SearchResult] = []
    for r in results:
        blob = " ".join([
            r.item.question,
            r.item.explanation,
            " ".join(r.item.key_points),
            r.item.code,
            r.section.title,
            r.phase.label,
        ]).lower()
        if query in blob or all(word in blob for word in query.split()):
            filtered.append(r)
    return filtered


# Load additional topics (Docker, Terraform, WCF, HTML/CSS, roadmap extras)
from data.extra_content import apply_extras  # noqa: E402
from data.detailed_content import apply_all_content  # noqa: E402

apply_extras(SECTIONS)
apply_all_content(SECTIONS)
