"""Additional interview topics + new sections (Docker, Terraform, WCF, patterns, HTML/CSS)."""

from data.interview_content import InterviewItem, Phase, Section

# (section_id, phase_id) -> extra items to append
EXTRA_BY_PHASE: dict[tuple[str, str], list[InterviewItem]] = {
    ("dotnet", "foundation"): [
        InterviewItem(
            "logging",
            "How does logging work in ASP.NET Core?",
            "Built on `ILogger<T>` abstraction with providers (Console, Debug, EventSource, App Insights). "
            "Use **structured logging** with message templates — not string interpolation.",
            """public class OrderService(ILogger<OrderService> logger)
{
    public void PlaceOrder(int orderId, string customer)
    {
        logger.LogInformation("Order {OrderId} placed for {Customer}", orderId, customer);
        // Bad: logger.LogInformation($"Order {orderId}"); // not structured
    }
}""",
            key_points=["LogLevel: Trace→Critical", "Serilog popular for sinks/formatting", "Never log passwords or tokens"],
        ),
        InterviewItem(
            "garbage-collection",
            "Explain .NET garbage collection basics.",
            "Generational GC: Gen 0 (short-lived), Gen 1 buffer, Gen 2 (long-lived). "
            "GC pauses can affect latency — reduce allocations in hot paths.",
            """// IDisposable for unmanaged resources
await using var conn = new SqlConnection(connectionString);
await conn.OpenAsync();

// ArrayPool reduces GC pressure
var pool = ArrayPool<byte>.Shared;
var buffer = pool.Rent(4096);
try { /* use buffer */ }
finally { pool.Return(buffer); }""",
            key_points=["Large Object Heap (LOH) for objects ≥ 85KB", "GC.Collect() rarely needed in app code", "Use IDisposable/using for files, DB, HTTP"],
        ),
        InterviewItem(
            "string-handling",
            "How do you handle strings efficiently in C#?",
            "`string` is immutable — concatenation in loops creates many objects. Use `StringBuilder` or string interpolation for few parts.",
            """// Bad in a loop
string result = "";
foreach (var s in items) result += s;

// Good
var sb = new StringBuilder();
foreach (var s in items) sb.Append(s);
var result = sb.ToString();

// C# modern — string.Create, Span<char> for advanced scenarios
ReadOnlySpan<char> slice = "Hello World".AsSpan(6, 5); // "World" """,
            key_points=["string interning for literals", "Span<T> avoids allocations", "UTF-8 encoding for APIs"],
        ),
        InterviewItem(
            "interface-vs-abstract-rules",
            "What can an abstract class do that an interface cannot (and vice versa)?",
            "A class can inherit **only one** abstract class but **many** interfaces. "
            "Abstract classes can have **constructors**, **fields**, **protected members**, and **non-public** APIs. "
            "Interfaces define a **contract** — historically no state; from C# 8+ they may have default/static members but still no instance fields. "
            "You **cannot instantiate** either directly.",
            """public abstract class DocumentBase
{
    protected Guid Id { get; } = Guid.NewGuid();  // shared state
    public abstract void Save();

    public virtual void Print() => Console.WriteLine("Printing...");
}

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
    public DateTime CreatedAt { get; init; } = DateTime.UtcNow;
    public override void Save() => /* ... */;
    public void Audit(string action) => /* ... */;
    public byte[] Export() => /* ... */;
}""",
            key_points=[
                "Single inheritance for classes; multiple interfaces allowed",
                "Abstract class = 'is-a' with shared implementation",
                "Interface = capability contract (IPayable, ICacheable)",
            ],
        ),
        InterviewItem(
            "abstract-class-members",
            "Explain abstract, virtual, and sealed methods in an abstract class.",
            "**abstract** — no body; derived class **must** override. "
            "**virtual** — has default body; derived class **may** override. "
            "**sealed override** — stops further overriding down the chain. "
            "Use abstract methods when each child must provide its own behavior.",
            """public abstract class PaymentProcessor
{
    // Must implement
    public abstract Task<PaymentResult> ProcessAsync(decimal amount);

    // Optional override
    public virtual void Log(string message) =>
        Console.WriteLine($"[Payment] {message}");

    // Common concrete logic
    public bool IsValidAmount(decimal amount) => amount > 0;
}

public class StripeProcessor : PaymentProcessor
{
    public override async Task<PaymentResult> ProcessAsync(decimal amount)
    {
        Log($"Charging {amount} via Stripe");
        return new PaymentResult(true);
    }
}

public class PayPalProcessor : PaymentProcessor
{
    public override Task<PaymentResult> ProcessAsync(decimal amount) => /* ... */;
    public override void Log(string message) => /* custom logging */;
}""",
            key_points=[
                "abstract = forced customization",
                "virtual = optional customization",
                "Keep base class focused — don't become a god class",
            ],
        ),
    ],
    ("dotnet", "intermediate"): [
        InterviewItem(
            "delegates-events",
            "What are delegates, lambdas, and events?",
            "**Delegate** = typed function pointer. **Lambda** = inline delegate. **Event** = encapsulated delegate (pub/sub).",
            """public delegate int MathOp(int a, int b);

Func<int, int, int> add = (a, b) => a + b;
Action<string> log = msg => Console.WriteLine(msg);

public class StockTicker
{
    public event EventHandler<decimal>? PriceChanged;
    protected void OnPriceChanged(decimal price) =>
        PriceChanged?.Invoke(this, price);
}""",
            key_points=["Func<T> and Action<T> built-in delegates", "events prevent external Invoke", "LINQ uses delegates heavily"],
        ),
        InterviewItem(
            "explicit-interface-implementation",
            "What is explicit interface implementation? When would you use it?",
            "When a class implements two interfaces with the **same method signature**, or you want to **hide** an interface member from public API. "
            "Call it only through the interface reference.",
            """public interface IReadable { string Read(); }
public interface IWritable { void Write(string data); }

public class ConfigStore : IReadable, IWritable
{
    public string Read() => "public read";

    // Hidden unless cast to IWritable
    void IWritable.Write(string data) => File.WriteAllText("config.json", data);
}

var store = new ConfigStore();
store.Read();                        // OK
// store.Write("x");                 // compile error
((IWritable)store).Write("x");       // OK""",
            key_points=[
                "Resolves signature clashes between interfaces",
                "Useful for legacy API hiding",
                "No access modifier on explicit implementation",
            ],
        ),
        InterviewItem(
            "default-interface-methods",
            "What are default interface implementations in C# 8+?",
            "Interfaces can provide **default method bodies** so you can extend an interface without breaking existing implementers. "
            "Use sparingly — prefer extension methods or abstract base classes when sharing substantial logic.",
            """public interface INotifier
{
    void Send(string message);

    // Default implementation — implementers inherit it
    void SendWithPrefix(string message) =>
        Send($"[ALERT] {message}");
}

public class EmailNotifier : INotifier
{
    public void Send(string message) => Console.WriteLine($"Email: {message}");
    // SendWithPrefix inherited — no change needed
}

INotifier n = new EmailNotifier();
n.SendWithPrefix("Server down");""",
            key_points=[
                "Helps evolve APIs with less breaking change",
                "Diamond problem possible if multiple defaults clash",
                "Still no instance fields on interfaces",
            ],
        ),
        InterviewItem(
            "interface-for-di-testing",
            "Why do we prefer interfaces over concrete classes in DI and unit tests?",
            "DI containers register **abstractions** (`IOrderRepository`), not concrete types. "
            "Tests swap in **mocks/fakes** without touching production code. "
            "This follows the **Dependency Inversion Principle**.",
            """public interface IOrderRepository
{
    Task<Order?> GetAsync(int id);
}

public class SqlOrderRepository(AppDbContext db) : IOrderRepository
{
    public Task<Order?> GetAsync(int id) =>
        db.Orders.FirstOrDefaultAsync(o => o.Id == id);
}

// Unit test with fake
public class FakeOrderRepository : IOrderRepository
{
    private readonly Dictionary<int, Order> _data = new();
    public Task<Order?> GetAsync(int id) =>
        Task.FromResult(_data.GetValueOrDefault(id));
}

// Program.cs
builder.Services.AddScoped<IOrderRepository, SqlOrderRepository>();""",
            key_points=[
                "Depend on abstractions, not concretions",
                "Moq/NSubstitute mock interfaces easily",
                "Abstract class harder to mock if not interface-based",
            ],
        ),
        InterviewItem(
            "exception-handling",
            "Best practices for exception handling in .NET?",
            "Catch specific exceptions. Log context. Don't swallow errors. Use global middleware in APIs.",
            """try
{
    await _service.ProcessAsync();
}
catch (ValidationException ex)
{
    return BadRequest(ex.Message);
}
catch (Exception ex)
{
    _logger.LogError(ex, "Unexpected error processing order {Id}", orderId);
    throw; // preserve stack trace
}""",
            key_points=["finally for cleanup", "custom exceptions for domain errors", "ProblemDetails (RFC 7807) for APIs"],
        ),
        InterviewItem(
            "dotnet-cli",
            "Essential .NET CLI commands for interviews?",
            "Know restore, build, test, publish, and EF tools.",
            """dotnet restore
dotnet build -c Release
dotnet test --logger "console;verbosity=normal"
dotnet publish -c Release -o ./publish
dotnet ef migrations add InitialCreate
dotnet ef database update
dotnet user-secrets set "Jwt:Key" "dev-secret" --project Api""",
            "bash",
            key_points=["dotnet new webapi -n MyApi", "global.json pins SDK version", "watch mode: dotnet watch run"],
        ),
    ],
    ("dotnet", "advanced"): [
        InterviewItem(
            "covariance",
            "Explain covariance and contravariance in C#.",
            "**Covariant** `out` — return more derived type (`IEnumerable<string>` → `IEnumerable<object>`). "
            "**Contravariant** `in` — accept more base type (`Action<object>` → `Action<string>`).",
            """IEnumerable<string> names = new List<string>();
IEnumerable<object> objects = names; // covariant

Action<object> actObj = o => Console.WriteLine(o);
Action<string> actStr = actObj; // contravariant""",
            key_points=["in/out on generic interfaces", "Arrays are covariant but unsafe", "Func is covariant in TResult, contravariant in T"],
        ),
        InterviewItem(
            "interface-segregation",
            "Explain the Interface Segregation Principle (ISP) with an example.",
            "Clients should not depend on methods they don't use. Split **fat interfaces** into smaller, focused ones. "
            "Common in repository/service design and Angular service contracts too.",
            """// Bad — fat interface
public interface IWorker
{
    void Code();
    void Deploy();
    void WriteHrReport();
}

// Good — segregated
public interface IDeveloper { void Code(); }
public interface IDevOps { void Deploy(); }
public interface IHrReporter { void WriteHrReport(); }

public class FullStackEngineer : IDeveloper, IDevOps
{
    public void Code() => /* ... */;
    public void Deploy() => /* ... */;
}""",
            key_points=[
                "Part of SOLID — the I in SOLID",
                "Smaller interfaces = easier testing and mocking",
                "Avoid 'god interfaces' with 20+ members",
            ],
        ),
        InterviewItem(
            "abstract-factory-vs-strategy",
            "Abstract class vs interface — when to use Template Method vs Strategy pattern?",
            "**Template Method** (abstract class): base class defines algorithm skeleton; subclasses override steps. "
            "**Strategy** (interface): swap entire algorithm at runtime via DI.",
            """// Template Method — abstract class
public abstract class DataExporter
{
    public void Export()  // fixed workflow
    {
        var data = FetchData();
        var formatted = Format(data);
        Write(formatted);
    }
    protected abstract IEnumerable<Row> FetchData();
    protected abstract string Format(IEnumerable<Row> data);
    protected virtual void Write(string output) => Console.WriteLine(output);
}

// Strategy — interface
public interface ITaxCalculator { decimal Calculate(decimal amount); }
public class UsTaxCalculator : ITaxCalculator { /* ... */ }
public class UkTaxCalculator : ITaxCalculator { /* ... */ }

public class CheckoutService(ITaxCalculator tax)
{
    public decimal Total(decimal subtotal) => subtotal + tax.Calculate(subtotal);
}""",
            key_points=[
                "Abstract class when workflow is shared",
                "Interface when behavior is fully pluggable",
                "Both support Open/Closed Principle",
            ],
        ),
        InterviewItem(
            "static-interface-members",
            "Can interfaces have static members in modern C#?",
            "Yes — since **C# 8** interfaces can have `static` methods and properties, and **C# 11** added `static abstract` members "
            "for generic math-style patterns. Still no instance fields.",
            """public interface IParsable<T> where T : IParsable<T>
{
    static abstract T Parse(string s, IFormatProvider? provider);
}

public record OrderId(int Value) : IParsable<OrderId>
{
    public static OrderId Parse(string s, IFormatProvider? provider) =>
        new(int.Parse(s, provider));
}

// Static helper on interface
public interface ILogger
{
    static void Banner() => Console.WriteLine("=== App started ===");
    void Log(string message);
}""",
            key_points=[
                "static abstract used in generic math interfaces",
                "Don't overuse — keep interfaces readable",
                "Contrast with abstract class static methods",
            ],
        ),
    ],
    ("aspnet", "foundation"): [
        InterviewItem(
            "filters",
            "What are ASP.NET Core filters?",
            "Cross-cutting hooks: Authorization, Resource, Action, Exception, Result filters.",
            """public class ValidateModelAttribute : ActionFilterAttribute
{
    public override void OnActionExecuting(ActionExecutingContext context)
    {
        if (!context.ModelState.IsValid)
            context.Result = new BadRequestObjectResult(context.ModelState);
    }
}

[ServiceFilter(typeof(ValidateModelAttribute))]
[HttpPost]
public IActionResult Create(CreateOrderDto dto) => Ok();""",
            key_points=["IAsyncActionFilter for async", "Exception filters for logging", "Order: Authorization → Action → Exception"],
        ),
        InterviewItem(
            "environments",
            "How do ASP.NET Core environments work?",
            "`ASPNETCORE_ENVIRONMENT` controls config loading and behavior. Development shows detailed errors; Production is hardened.",
            """// Program.cs
if (app.Environment.IsDevelopment())
    app.UseSwagger();
else
    app.UseExceptionHandler("/error");

// appsettings.Development.json overrides appsettings.json""",
            key_points=["Development, Staging, Production", "Never enable Swagger in prod publicly", "Feature flags per environment"],
        ),
    ],
    ("aspnet", "intermediate"): [
        InterviewItem(
            "identity",
            "What is ASP.NET Core Identity?",
            "Membership system: users, roles, passwords, lockout, 2FA, external logins. Stores in EF or custom store.",
            """builder.Services.AddIdentity<ApplicationUser, IdentityRole>()
    .AddEntityFrameworkStores<AppDbContext>()
    .AddDefaultTokenProviders();

// Cookie or JWT integration
builder.Services.AddAuthentication()
    .AddJwtBearer(/* ... */);""",
            key_points=["Password hashing built-in", "Role and claim-based auth", "Separate from Entra ID (can integrate both)"],
        ),
    ],
    ("frontend", "foundation"): [
        InterviewItem(
            "var-let-const",
            "Difference between var, let, and const in JavaScript?",
            "`var` — function scoped, hoisted. `let`/`const` — block scoped. `const` prevents reassignment (object contents mutable).",
            """function demo() {
  if (true) {
    var a = 1;   // hoisted to function scope
    let b = 2;   // block scoped
    const c = 3; // block scoped, no reassignment
  }
  // console.log(b); // ReferenceError
}""",
            "javascript",
            key_points=["Always use const by default", "let when reassigning", "avoid var in modern code"],
        ),
        InterviewItem(
            "promises-async",
            "Promises vs async/await in JavaScript?",
            "Promise represents future value. async/await is syntactic sugar — cleaner error handling with try/catch.",
            """async function fetchOrders() {
  try {
    const res = await fetch('/api/orders');
    if (!res.ok) throw new Error(res.statusText);
    return await res.json();
  } catch (err) {
    console.error('Failed', err);
    return [];
  }
}""",
            "javascript",
            key_points=["Promise.all for parallel", "Promise.race for timeout patterns", "Angular HttpClient returns Observable not Promise"],
        ),
    ],
    ("frontend", "intermediate"): [
        InterviewItem(
            "angular-routing",
            "Explain Angular routing and lazy loading.",
            "Router maps URLs to components. Guards protect routes. Lazy loading splits bundles per feature module.",
            """const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'orders', loadChildren: () => import('./orders/orders.routes')
      .then(m => m.ORDER_ROUTES), canActivate: [authGuard] },
  { path: '**', redirectTo: '' }
];""",
            "typescript",
            key_points=["canActivate, canDeactivate guards", "Route params via ActivatedRoute", "Lazy loading improves initial load time"],
        ),
    ],
    ("database", "foundation"): [
        InterviewItem(
            "sql-groupby",
            "Explain GROUP BY and HAVING with an example.",
            "GROUP BY aggregates rows. HAVING filters groups (like WHERE for aggregates).",
            """SELECT Department, COUNT(*) AS HeadCount, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 5
ORDER BY AvgSalary DESC;""",
            "sql",
            key_points=["WHERE filters rows before grouping", "HAVING filters after aggregation", "Every non-aggregated column must be in GROUP BY"],
        ),
        InterviewItem(
            "sql-indexes",
            "What are database indexes and when do you add them?",
            "B-tree structure speeding lookups. Trade-off: faster SELECT, slower INSERT/UPDATE, storage cost.",
            """CREATE NONCLUSTERED INDEX IX_Orders_CustomerId
ON Orders (CustomerId)
INCLUDE (OrderDate, Total);

-- Covering index: query satisfied from index alone""",
            "sql",
            key_points=["Index foreign keys", "Avoid over-indexing write-heavy tables", "Check execution plans for scans"],
        ),
    ],
    ("database", "intermediate"): [
        InterviewItem(
            "dapper",
            "When would you use Dapper instead of EF Core?",
            "Dapper is a micro-ORM — raw SQL, manual mapping, minimal overhead. Use for read-heavy, tuned queries or legacy SQL.",
            """const string sql = @"
    SELECT Id, CustomerName, Total
    FROM Orders WHERE Total > @MinTotal";

var orders = await connection.QueryAsync<OrderDto>(sql, new { MinTotal = 100 });""",
            key_points=["EF for CRUD and migrations", "Dapper for performance-critical reads", "Can combine both in same app"],
        ),
        InterviewItem(
            "ef-migrations",
            "How do EF Core migrations work?",
            "Code-first model changes → migration files → `database update` applies SQL. Version-control schema like code.",
            """dotnet ef migrations add AddOrderStatusColumn
dotnet ef database update

// In migration Up():
migrationBuilder.AddColumn<string>(
    name: "Status", table: "Orders",
    nullable: false, defaultValue: "Pending");""",
            key_points=["Never edit applied migrations in prod", "Script migrations for DBA review: dotnet ef migrations script", "Idempotent deploy in CI/CD"],
        ),
    ],
    ("azure", "foundation"): [
        InterviewItem(
            "azure-functions",
            "What are Azure Functions?",
            "Serverless event-driven compute. Triggers: HTTP, Timer, Queue, Blob, Service Bus. Pay per execution.",
            """[Function(nameof(ProcessOrder))]
public async Task Run(
    [ServiceBusTrigger("orders", Connection = "ServiceBus")] string message,
    FunctionContext context)
{
    var order = JsonSerializer.Deserialize<OrderEvent>(message);
    await _processor.HandleAsync(order!);
}""",
            key_points=["Consumption vs Premium plan", "Durable Functions for workflows", "Cold start latency on consumption"],
        ),
        InterviewItem(
            "blob-storage",
            "Azure Blob Storage tiers and use cases?",
            "Object storage for files. Hot (frequent), Cool (infrequent), Archive (rare, cheap retrieval).",
            """BlobServiceClient client = new(connectionString);
var container = client.GetBlobContainerClient("uploads");
await container.UploadBlobAsync("invoice-1042.pdf", fileStream);""",
            key_points=["Block blobs for files", "SAS tokens for temporary client upload", "CDN in front for static assets"],
        ),
        InterviewItem(
            "cosmos-db",
            "What is Azure Cosmos DB? Partition key?",
            "Globally distributed NoSQL. **Partition key** determines data distribution — choose high cardinality key (tenantId, userId).",
            """// Bad partition key: status (only few values)
// Good: /customerId

var item = await container.ReadItemAsync<Order>(
    id: orderId.ToString(),
    partitionKey: new PartitionKey(customerId));""",
            key_points=["Request Unit (RU) billing", "SQL API for document queries", "Strong vs bounded staleness consistency"],
        ),
    ],
    ("azure", "intermediate"): [
        InterviewItem(
            "aks-basics",
            "What is Azure Kubernetes Service (AKS)?",
            "Managed Kubernetes — run containers at scale. Pods, Services, Deployments, Ingress.",
            """# Deployment manifest (simplified)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-api
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: api
        image: myregistry.azurecr.io/order-api:1.2.0
        ports:
        - containerPort: 8080""",
            "yaml",
            key_points=["ACR stores images", "Horizontal Pod Autoscaler", "App Service simpler if you don't need K8s"],
        ),
        InterviewItem(
            "redis-cache",
            "How do you use Azure Cache for Redis in .NET?",
            "Distributed cache, session state, pub/sub, rate limiting. Reduces database load.",
            """builder.Services.AddStackExchangeRedisCache(options =>
{
    options.Configuration = builder.Configuration["Redis:Connection"];
});

// IDistributedCache
await cache.SetStringAsync($"order:{id}", json,
    new DistributedCacheEntryOptions { AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5) });""",
            key_points=["Cache-aside pattern", "Set TTL on all keys", "Not a persistent database"],
        ),
    ],
    ("practices", "foundation"): [
        InterviewItem(
            "design-patterns",
            "Explain common design patterns used in .NET interviews.",
            "Know Singleton, Factory, Repository, Decorator, Observer, Strategy — tie to real use cases.",
            """// Strategy — swap algorithms at runtime
public interface IShippingCalculator { decimal Calculate(Order o); }
public class OrderCheckout(IShippingCalculator shipping) {
    public decimal Total(Order o) => o.Subtotal + shipping.Calculate(o);
}

// Repository — abstract data access
public interface IOrderRepository { Task<Order?> GetAsync(int id); }""",
            key_points=["Singleton for shared config (DI preferred)", "Decorator for cross-cutting (logging)", "Factory for object creation"],
        ),
        InterviewItem(
            "clean-code",
            "What is Clean Code? Give practical rules.",
            "Readable names, small functions, single responsibility, minimal nesting, meaningful comments only where needed.",
            """// Bad
public void P(Order o) { if(o!=null){ if(o.Lines.Count>0){ /* ... */ }}}

// Good
public async Task ProcessOrderAsync(Order order)
{
    if (order is null) throw new ArgumentNullException(nameof(order));
    if (order.Lines.Count == 0) throw new ValidationException("Empty order");
    await _validator.ValidateAsync(order);
}""",
            key_points=["KISS and DRY", "Boy Scout Rule — leave code cleaner", "Code reviews enforce standards"],
        ),
    ],
    ("practices", "intermediate"): [
        InterviewItem(
            "bdd-tdd",
            "What is TDD vs BDD?",
            "**TDD**: write failing test → minimal code → refactor. **BDD**: tests in business language (Given/When/Then), often SpecFlow.",
            """// TDD example (xUnit)
[Fact]
public void Discount_AppliesTenPercent_WhenSubtotalOver100()
{
    var order = new Order { Subtotal = 150m };
    var discount = new TenPercentDiscount();
    Assert.Equal(15m, discount.Apply(order));
}

// BDD style (SpecFlow Gherkin)
// Given an order with subtotal 150
// When a 10% discount is applied
// Then the discount amount is 15""",
            key_points=["Red-Green-Refactor cycle", "BDD bridges dev and business", "Don't chase 100% coverage"],
        ),
    ],
}

NEW_SECTIONS: dict[str, Section] = {
    "optional": Section(
        id="optional",
        title="Docker & DevOps",
        emoji="🐳",
        color="#2496ED",
        subtitle="Docker, Terraform, WCF, message brokers",
        phases=[
            Phase("foundation", "Foundation", [
                InterviewItem(
                    "docker-basics",
                    "What is Docker? Explain image vs container.",
                    "**Image** = immutable template (layers). **Container** = running instance of image. "
                    "Dockerfile defines build steps.",
                    """# Multi-stage Dockerfile for .NET 8 API
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY . .
RUN dotnet publish -c Release -o /app

FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app
COPY --from=build /app .
EXPOSE 8080
ENTRYPOINT ["dotnet", "OrderApi.dll"]""",
                    "dockerfile",
                    key_points=["Multi-stage keeps image small", "Don't run as root in prod", ".dockerignore excludes bin/obj"],
                ),
                InterviewItem(
                    "docker-compose",
                    "How does Docker Compose help local development?",
                    "Define multi-container apps (API + SQL + Redis) in one YAML file.",
                    """# docker-compose.yml
services:
  api:
    build: .
    ports: ["5000:8080"]
    environment:
      ConnectionStrings__Sql: "Server=db;Database=Orders;User=sa;Password=Your_password123"
    depends_on: [db]
  db:
    image: mcr.microsoft.com/mssql/server:2022-latest
    environment:
      ACCEPT_EULA: "Y"
      SA_PASSWORD: "Your_password123"
""",
                    "yaml",
                    key_points=["docker compose up -d", "Volume for DB persistence", "Matches prod topology locally"],
                ),
            ]),
            Phase("intermediate", "Intermediate", [
                InterviewItem(
                    "terraform",
                    "What is Terraform? How does it differ from ARM/Bicep?",
                    "Infrastructure as Code — declarative HCL, multi-cloud. State file tracks resources. "
                    "Azure-native alternative: Bicep (ARM).",
                    """# main.tf — Azure App Service
resource "azurerm_resource_group" "rg" {
  name     = "rg-order-app"
  location = "East US"
}

resource "azurerm_linux_web_app" "api" {
  name                = "order-api-prod"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.plan.id
  site_config { application_stack { dotnet_version = "8.0" } }
}""",
                    "hcl",
                    key_points=["terraform plan before apply", "Remote state in Azure Storage", "Modules for reuse"],
                ),
                InterviewItem(
                    "message-brokers",
                    "Compare RabbitMQ, Kafka, and Azure Service Bus.",
                    "**RabbitMQ**: traditional AMQP broker, queues/exchanges. **Kafka**: event streaming, replay, high throughput. **Service Bus**: Azure managed, enterprise features.",
                    """// Kafka producer concept (Confluent)
// producer.Produce("order-events", new Message<Null, string> { Value = json });

// Service Bus — see Azure section
// RabbitMQ — popular with MassTransit in .NET""",
                    "text",
                    key_points=["At-least-once delivery — design idempotent consumers", "Kafka for event sourcing/stream analytics", "MassTransit abstracts brokers in .NET"],
                ),
            ]),
            Phase("advanced", "Advanced", [
                InterviewItem(
                    "wcf-legacy",
                    "What is WCF? When do you still encounter it?",
                    "Windows Communication Foundation — SOAP services on .NET Framework. "
                    "Legacy enterprise integrations. Modern replacement: gRPC or REST APIs.",
                    """// Legacy WCF service contract
[ServiceContract]
public interface IOrderService
{
    [OperationContract]
    Order GetOrder(int id);
}

// Modern replacement — gRPC or minimal API
app.MapGet("/api/orders/{id}", async (int id, AppDbContext db) =>
    await db.Orders.FindAsync(id));""",
                    key_points=[".NET Core WCF client only — not server", "Migration path: expose REST alongside SOAP", "Know SOAP vs REST for integration interviews"],
                ),
                InterviewItem(
                    "cicd-docker",
                    "CI/CD pipeline building and pushing Docker images to ACR?",
                    "Build image in pipeline, push to Azure Container Registry, deploy to AKS or App Service for containers.",
                    """# Azure Pipeline step
- task: Docker@2
  inputs:
    containerRegistry: 'acr-connection'
    repository: 'order-api'
    command: 'buildAndPush'
    Dockerfile: '**/Dockerfile'
    tags: '$(Build.BuildId)'""",
                    "yaml",
                    key_points=["Tag images with build ID or git SHA", "Scan images for vulnerabilities", "Use managed identity for ACR pull"],
                ),
            ]),
        ],
    ),
    "htmlcss": Section(
        id="htmlcss",
        title="HTML & CSS",
        emoji="🎨",
        color="#E34F26",
        subtitle="Semantic HTML, Flexbox, Grid, responsive design",
        phases=[
            Phase("foundation", "Foundation", [
                InterviewItem(
                    "semantic-html",
                    "Why use semantic HTML?",
                    "Improves accessibility (screen readers), SEO, and maintainability. Use meaningful tags not div soup.",
                    """<header>
  <nav aria-label="Main">
    <a href="/">Home</a>
    <a href="/orders">Orders</a>
  </nav>
</header>
<main>
  <article>
    <h1>Order #1042</h1>
    <section aria-labelledby="summary-heading">
      <h2 id="summary-heading">Summary</h2>
    </section>
  </article>
</main>
<footer>&copy; 2026 My App</footer>""",
                    "html",
                    key_points=["<main>, <article>, <section>, <nav>", "aria-label for accessibility", "One <h1> per page"],
                ),
            ]),
            Phase("intermediate", "Intermediate", [
                InterviewItem(
                    "flexbox-grid",
                    "Flexbox vs CSS Grid — when to use each?",
                    "**Flexbox** — one-dimensional layouts (row OR column). **Grid** — two-dimensional (rows AND columns).",
                    """/* Flexbox — navbar */
.navbar { display: flex; justify-content: space-between; align-items: center; }

/* Grid — dashboard */
.dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}""",
                    "css",
                    key_points=["Flexbox for components", "Grid for page layouts", "Bootstrap/Tailwind build on these"],
                ),
                InterviewItem(
                    "responsive-design",
                    "How do you build responsive UIs?",
                    "Mobile-first CSS with media queries, flexible units (rem, %, fr), responsive images.",
                    """/* Mobile first */
.sidebar { display: none; }
.content { width: 100%; }

@media (min-width: 768px) {
  .layout { display: grid; grid-template-columns: 240px 1fr; }
  .sidebar { display: block; }
}""",
                    "css",
                    key_points=["Viewport meta tag in HTML", "Angular CDK BreakpointObserver", "Test on real devices"],
                ),
            ]),
            Phase("advanced", "Advanced", [
                InterviewItem(
                    "angular-material",
                    "How does Angular handle styling and component encapsulation?",
                    "Emulated encapsulation adds unique attributes to scope CSS. :host targets component root. ::ng-deep deprecated.",
                    """/* order-card.component.css */
:host { display: block; padding: 1rem; }
:host(.highlight) { border: 2px solid #512BD4; }
.title { font-weight: 600; } /* scoped to this component */""",
                    "css",
                    key_points=["ViewEncapsulation.Emulated default", "Global styles in styles.css", "CSS variables for theming"],
                ),
            ]),
        ],
    ),
    "react": Section(
        id="react",
        title="React",
        emoji="⚛️",
        color="#61DAFB",
        subtitle="Hooks, state management, performance, and modern React patterns",
        phases=[
            Phase("foundation", "Foundation", []),
            Phase("intermediate", "Intermediate", []),
            Phase("advanced", "Advanced", []),
        ],
    ),
    "aws": Section(
        id="aws",
        title="AWS",
        emoji="🟠",
        color="#FF9900",
        subtitle="EC2, S3, Lambda, IAM, and cloud architecture",
        phases=[
            Phase("foundation", "Foundation", []),
            Phase("intermediate", "Intermediate", []),
            Phase("advanced", "Advanced", []),
        ],
    ),
}


def apply_extras(sections: dict[str, Section]) -> None:
    """Merge extra items and new sections into the main catalog."""
    for (section_id, phase_id), items in EXTRA_BY_PHASE.items():
        section = sections.get(section_id)
        if not section:
            continue
        for phase in section.phases:
            if phase.id == phase_id:
                phase.items.extend(items)
                break
    sections.update(NEW_SECTIONS)
