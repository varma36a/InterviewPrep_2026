"""Market-relevant .NET and ASP.NET Core interview topics (2025/2026)."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("dotnet", "foundation"): [
        InterviewItem(
            "nullable-reference-types",
            "What are nullable reference types and how do you enable them?",
            "See detailed explanation.",
            """#nullable enable
string? maybeName = GetName(); // may be null
string definite = maybeName ?? "Unknown";""",
            key_points=["#nullable enable", "Annotations vs warnings", "Null-forgiving operator"],
        ),
        InterviewItem(
            "record-types",
            "What are C# record types and when should you use them?",
            "See detailed explanation.",
            """public record OrderDto(int Id, string Customer, decimal Total);
public record struct Point(int X, int Y);""",
            key_points=["Value-based equality", "with expressions", "Immutability by default"],
        ),
    ],
    ("dotnet", "intermediate"): [
        InterviewItem(
            "pattern-matching",
            "Explain modern C# pattern matching (switch, is, list patterns).",
            "See detailed explanation.",
            """var label = shape switch
{
    Circle { Radius: > 0 } => "circle",
    Rectangle { Width: var w, Height: var h } => $"{w}x{h}",
    _ => "unknown"
};""",
            key_points=["Switch expressions", "Property patterns", "List patterns in C# 11+"],
        ),
    ],
    ("dotnet", "advanced"): [
        InterviewItem(
            "span-memory",
            "What are Span<T> and Memory<T> and why use them?",
            "See detailed explanation.",
            """ReadOnlySpan<char> slice = input.AsSpan(0, 10);
stackalloc byte[] buffer = stackalloc byte[256];""",
            key_points=["Zero-allocation slicing", "stackalloc", "Not for async/fields"],
        ),
        InterviewItem(
            "source-generators",
            "What are C# source generators and common use cases?",
            "See detailed explanation.",
            """// [LoggerMessage] generates high-performance logging methods at compile time
[LoggerMessage(Level = LogLevel.Information, Message = "Order {OrderId} placed")]
partial void LogOrderPlaced(int orderId);""",
            key_points=["Compile-time code generation", "LoggerMessage", "Regex source generator"],
        ),
    ],
    ("aspnet", "foundation"): [
        InterviewItem(
            "minimal-apis",
            "What are Minimal APIs and when do you choose them over controllers?",
            "See detailed explanation.",
            """app.MapGet("/orders/{id}", async (int id, IOrderService svc) =>
    await svc.GetAsync(id) is { } o ? Results.Ok(o) : Results.NotFound());""",
            key_points=["Less ceremony", "Endpoint filters", "Good for microservices"],
        ),
        InterviewItem(
            "cors",
            "How do you configure CORS in ASP.NET Core?",
            "See detailed explanation.",
            """builder.Services.AddCors(o => o.AddPolicy("Spa", p =>
    p.WithOrigins("https://app.example.com").AllowAnyHeader().AllowAnyMethod()));
app.UseCors("Spa");""",
            key_points=["UseCors before auth", "Named policies", "Never AllowAnyOrigin with credentials"],
        ),
        InterviewItem(
            "openapi-swagger",
            "How do you expose OpenAPI/Swagger in ASP.NET Core?",
            "See detailed explanation.",
            """builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
if (app.Environment.IsDevelopment()) { app.UseSwagger(); app.UseSwaggerUI(); }""",
            key_points=["Swashbuckle or NSwag", "Dev-only by default", "Document auth schemes"],
        ),
        InterviewItem(
            "content-negotiation",
            "How does content negotiation work in ASP.NET Core APIs?",
            "See detailed explanation.",
            """app.MapGet("/orders/{id}", (int id) => Results.Ok(order))
   .Produces<OrderDto>(200, "application/json")
   .Produces(406);""",
            key_points=["Accept header", "406 Not Acceptable", "Formatters"],
        ),
        InterviewItem(
            "cookie-auth",
            "How does cookie authentication work in ASP.NET Core?",
            "See detailed explanation.",
            """builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
    .AddCookie(o => { o.LoginPath = "/login"; o.Cookie.HttpOnly = true; });""",
            key_points=["SameSite", "HttpOnly", "Sliding expiration"],
        ),
        InterviewItem(
            "problem-details",
            "What is RFC 7807 ProblemDetails and how do you use it?",
            "See detailed explanation.",
            """return Results.Problem(title: "Order not found", statusCode: 404, detail: $"No order {id}");""",
            key_points=["Standard error shape", "AddProblemDetails()", "type/title/status/detail"],
        ),
    ],
    ("aspnet", "intermediate"): [
        InterviewItem(
            "rate-limiting",
            "How do you implement rate limiting in ASP.NET Core 7+?",
            "See detailed explanation.",
            """builder.Services.AddRateLimiter(o => o.AddFixedWindowLimiter("api", c =>
    { c.Window = TimeSpan.FromMinutes(1); c.PermitLimit = 100; }));
app.UseRateLimiter();""",
            key_points=["Fixed/sliding/token bucket", "Partition by user/IP", "429 + Retry-After"],
        ),
        InterviewItem(
            "output-caching",
            "What is output caching and how does it differ from response caching?",
            "See detailed explanation.",
            """app.MapGet("/catalog", () => GetCatalog()).CacheOutput(p => p.Expire(TimeSpan.FromMinutes(5)));""",
            key_points=["Server-side store", "Cache profiles", "Vary by query/header"],
        ),
        InterviewItem(
            "api-versioning",
            "How do you version REST APIs in ASP.NET Core?",
            "See detailed explanation.",
            """builder.Services.AddApiVersioning(o => o.DefaultApiVersion = new ApiVersion(1, 0));""",
            key_points=["URL vs header vs query", "Deprecation headers", "Asp.Versioning.Http"],
        ),
        InterviewItem(
            "global-exception-handling",
            "How do you implement global exception handling in ASP.NET Core?",
            "See detailed explanation.",
            """app.UseExceptionHandler(app => app.Run(async ctx =>
    await Results.Problem("Unexpected error").ExecuteAsync(ctx)));""",
            key_points=["UseExceptionHandler", "IExceptionHandler (.NET 8+)", "Never leak stack traces"],
        ),
        InterviewItem(
            "endpoint-filters",
            "What are endpoint filters in Minimal APIs?",
            "See detailed explanation.",
            """app.MapPost("/orders", CreateOrder).AddEndpointFilter(async (ctx, next) =>
    { /* validate */ return await next(ctx); });""",
            key_points=["Replace some filters", "IEndpointFilter", "Validation/logging"],
        ),
        InterviewItem(
            "antiforgery",
            "How does antiforgery (CSRF) protection work in ASP.NET Core?",
            "See detailed explanation.",
            """builder.Services.AddAntiforgery(o => o.HeaderName = "X-CSRF-TOKEN");""",
            key_points=["Double-submit cookie", "Validate on state-changing requests", "SPA token header"],
        ),
        InterviewItem(
            "request-response-logging",
            "How do you log HTTP requests and responses safely?",
            "See detailed explanation.",
            """app.Use(async (ctx, next) =>
    { _log.LogInformation("{Method} {Path}", ctx.Request.Method, ctx.Request.Path); await next(ctx); });""",
            key_points=["Structured logging", "Redact secrets", "Serilog request logging"],
        ),
        InterviewItem(
            "api-security-headers",
            "Which security headers should ASP.NET Core APIs set?",
            "See detailed explanation.",
            """app.Use(async (ctx, next) =>
    { ctx.Response.Headers["X-Content-Type-Options"] = "nosniff"; await next(ctx); });""",
            key_points=["HSTS", "CSP", "X-Frame-Options"],
        ),
        InterviewItem(
            "websockets",
            "How do you use WebSockets in ASP.NET Core?",
            "See detailed explanation.",
            """app.Map("/ws", async ctx =>
    { if (ctx.WebSockets.IsWebSocketRequest) { var ws = await ctx.WebSockets.AcceptWebSocketAsync(); } });""",
            key_points=["Upgrade handshake", "UseWebSockets middleware", "Prefer SignalR for app logic"],
        ),
    ],
    ("aspnet", "advanced"): [
        InterviewItem(
            "grpc-aspnet",
            "How do you host gRPC services in ASP.NET Core?",
            "See detailed explanation.",
            """builder.Services.AddGrpc();
app.MapGrpcService<OrderGrpcService>();""",
            key_points=["HTTP/2 required", "Protobuf contracts", "Streaming RPC"],
        ),
        InterviewItem(
            "oauth-oidc",
            "How do you integrate OAuth 2.0 / OpenID Connect in ASP.NET Core?",
            "See detailed explanation.",
            """builder.Services.AddAuthentication()
    .AddOpenIdConnect("oidc", o => { o.Authority = "https://login.microsoftonline.com/tenant"; });""",
            key_points=["Authorization code + PKCE", "Entra ID / Auth0", "Map claims to roles"],
        ),
        InterviewItem(
            "signalr",
            "What is SignalR and when do you use it?",
            "See detailed explanation.",
            """builder.Services.AddSignalR();
app.MapHub<OrderHub>("/hubs/orders");""",
            key_points=["WebSocket fallback", "Groups", "Scale-out with Redis backplane"],
        ),
        InterviewItem(
            "background-services",
            "How do IHostedService and BackgroundService work?",
            "See detailed explanation.",
            """builder.Services.AddHostedService<OrderQueueWorker>();
public class OrderQueueWorker(ILogger<OrderQueueWorker> log) : BackgroundService
    { protected override async Task ExecuteAsync(CancellationToken ct) => /* loop */; }""",
            key_points=["Long-running tasks", "Graceful shutdown", "Channel<T> for work queues"],
        ),
        InterviewItem(
            "yarp-reverse-proxy",
            "What is YARP and how do you use it as a reverse proxy?",
            "See detailed explanation.",
            """builder.Services.AddReverseProxy().LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));
app.MapReverseProxy();""",
            key_points=["Route clusters", "Load balancing", "Transforms and auth"],
        ),
        InterviewItem(
            "opentelemetry-aspnet",
            "How do you add OpenTelemetry to ASP.NET Core?",
            "See detailed explanation.",
            """builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation().AddOtlpExporter());""",
            key_points=["Traces/metrics/logs", "OTLP exporter", "App Insights integration"],
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "nullable-reference-types": {
        "explanation": (
            "**Nullable reference types (NRTs)** are a C# 8+ feature that treats reference types as **non-null by default** "
            "when `#nullable enable` is on, surfacing potential **NullReferenceException** bugs at compile time instead of runtime. "
            "You annotate possibly-null values with `?` (e.g., `string?`) and the compiler warns on unsafe dereference or assignment. "
            "The **null-forgiving operator** (`!`) suppresses a warning when you have proven non-null (e.g., after `ArgumentNullException.ThrowIfNull`). "
            "Enable project-wide via `<Nullable>enable</Nullable>` in the `.csproj` — standard for new .NET 6/8 projects. "
            "**Why it matters:** APIs become self-documenting and teams catch null bugs during code review and CI builds. "
            "**Pitfall:** enabling NRT on legacy codebases produces thousands of warnings — migrate incrementally with `#nullable disable` regions or nullable annotations context."
        ),
        "code": """#nullable enable

public string FormatCustomer(string? name)
{
    // Compiler warns if you return name without null check
    ArgumentNullException.ThrowIfNull(name);
    return name.Trim().ToUpperInvariant();
}

public void ProcessOrder(Order? order)
{
    if (order is null) return; // flow analysis: order is non-null below

    _logger.LogInformation("Processing {Id}", order.Id);

    // Null-forgiving when you know better than the compiler (use sparingly)
    var cached = _cache.Get(order.Id)!;
}

// Project file — enable for entire assembly
// <PropertyGroup><Nullable>enable</Nullable></PropertyGroup>""",
        "language": "csharp",
        "key_points": [
            "Enable with #nullable enable or <Nullable>enable</Nullable>",
            "string? = may be null; string = should never be null",
            "Compiler flow analysis reduces need for redundant checks",
            "Null-forgiving (!) suppresses warnings — document why",
            "Migrate legacy code incrementally to avoid warning floods",
        ],
    },
    "record-types": {
        "explanation": (
            "**Records** (`record` / `record class` / `record struct`) are reference or value types optimized for **immutable data carriers** "
            "with **value-based equality** — two records with the same property values compare equal. "
            "They auto-generate `Equals`, `GetHashCode`, `ToString`, and **deconstructors**, reducing boilerplate vs manual classes. "
            "The **`with` expression** creates a copy with selected properties changed, ideal for DTOs and event messages. "
            "Use **record struct** for small immutable value types (like coordinates) with less allocation than class records. "
            "**When to use:** API DTOs, domain events, configuration snapshots — anywhere identity is defined by data, not reference. "
            "**Pitfall:** mutable `init` properties are fine, but avoid putting mutable collections without defensive copies; prefer `IReadOnlyList<T>`."
        ),
        "code": """// Positional record — concise DTO
public record OrderDto(int Id, string CustomerName, decimal Total);

// Mutable init-only properties with custom members
public record CustomerDto
{
    public required string Email { get init; }
    public string? Phone { get init; }

    public string Domain => Email.Split('@')[^1];
}

// Non-destructive mutation via `with`
var order = new OrderDto(1, "Alice", 99.99m);
var discounted = order with { Total = order.Total * 0.9m };

// Value semantics — equal if all properties match
Console.WriteLine(order == discounted); // false

// record struct — stack-friendly small values
public readonly record struct Money(decimal Amount, string Currency);""",
        "language": "csharp",
        "key_points": [
            "Value-based equality generated automatically",
            "with expressions for non-destructive updates",
            "Ideal for DTOs, events, and value objects",
            "record struct for small immutable value types",
            "Use required/init for safer construction",
        ],
    },
    "pattern-matching": {
        "explanation": (
            "**Pattern matching** lets you test the shape and values of data in `is`, `switch`, and `switch` expressions — "
            "replacing long if/else chains with declarative, exhaustive checks. "
            "**Property patterns** match on nested properties (`Person { Age: >= 18 }`), **relational patterns** compare values, "
            "and **list patterns** (C# 11+) match array/list structure (`[var first, .. var rest]`). "
            "Switch expressions return a value and support `_` discard for default cases; the compiler warns on non-exhaustive switches for enums and records. "
            "**Why it matters:** cleaner validation, parsing JSON/domain unions, and compiler-checked completeness. "
            "**Pitfall:** overly complex patterns harm readability — extract named helper methods when patterns exceed ~3 lines."
        ),
        "code": """public string DescribeShape(Shape shape) => shape switch
{
    Circle { Radius: <= 0 } => "invalid circle",
    Circle { Radius: var r } => $"circle r={r}",
    Rectangle { Width: var w, Height: var h } when w == h => $"square {w}",
    Rectangle { Width: var w, Height: var h } => $"rectangle {w}x{h}",
    null => "none",
    _ => "unknown"
};

// List patterns — parse HTTP API version segments
public bool IsV2Route(int[] segments) => segments switch
{
    [1, 2, ..] => true,
    [2, ..] => true,
    _ => false
};

// Type pattern with when guard
if (response is ErrorResponse { Code: var code } err when code >= 500)
    _logger.LogError("Server error: {Detail}", err.Detail);""",
        "language": "csharp",
        "key_points": [
            "Switch expressions return values; statements use switch { }",
            "Property, relational, and list patterns combine cleanly",
            "Compiler exhaustiveness checks reduce missed cases",
            "when guards add extra boolean conditions",
            "Keep patterns readable — refactor complex ones",
        ],
    },
    "span-memory": {
        "explanation": (
            "`Span<T>` and `ReadOnlySpan<T>` provide a **safe, stack-friendly view** over contiguous memory (arrays, strings, stack buffers) "
            "**without allocating** new arrays when slicing. "
            "`Memory<T>` is the **heap-friendly, async-safe** counterpart — you can store it in fields and use it across `await` boundaries. "
            "Common uses: parsing protocols, string tokenization, crypto, and high-throughput logging — anywhere allocations dominate profiles. "
            "`stackalloc` combined with `Span<byte>` avoids LOH/GC pressure for small temporary buffers. "
            "**Why it matters:** ASP.NET Core internals and modern APIs (`SequenceReader`, `Utf8JsonReader`) are Span-based for performance. "
            "**Pitfall:** `Span<T>` cannot be used in async methods or as instance fields; use `Memory<T>` instead. Never use `stackalloc` for large buffers."
        ),
        "code": """// Zero-allocation string slice — no Substring allocation
ReadOnlySpan<char> GetHost(ReadOnlySpan<char> url)
{
    var schemeEnd = url.IndexOf("://".AsSpan());
    if (schemeEnd < 0) return url;
    var hostStart = schemeEnd + 3;
    var pathStart = url[hostStart..].IndexOf('/');
    return pathStart < 0 ? url[hostStart..] : url[hostStart..(hostStart + pathStart)];
}

// stackalloc buffer for short-lived work
Span<byte> hashBuffer = stackalloc byte[32];
SHA256.HashData(sourceBytes, hashBuffer);

// Memory<T> for async pipelines
async Task ProcessAsync(ReadOnlyMemory<byte> payload, CancellationToken ct)
{
    await _stream.WriteAsync(payload, ct); // Span cannot cross await
}

// ArrayPool for larger reusable buffers
var pool = ArrayPool<byte>.Shared;
var rented = pool.Rent(4096);
try { /* parse into rented.AsSpan() */ }
finally { pool.Return(rented); }""",
        "language": "csharp",
        "key_points": [
            "Span = ref struct; stack-only, no async/fields",
            "Memory = async-safe; use in pipelines with await",
            "Avoid Substring/ToArray when slicing — use spans",
            "stackalloc + Span for small temp buffers",
            "ArrayPool for larger reusable byte buffers",
        ],
    },
    "source-generators": {
        "explanation": (
            "**Source generators** run at **compile time** and add C# source files to the compilation — zero runtime reflection cost. "
            "They power **`[LoggerMessage]`** (high-performance logging), **regex source generators**, **System.Text.Json** serializers, "
            "and third-party tools like **Mapperly** for mapping. "
            "Generators implement `ISourceGenerator` or the incremental `IIncrementalGenerator` API for better caching in large solutions. "
            "**Why it matters:** hot paths avoid boxing, string formatting, and reflection — critical for microservices and high-QPS APIs. "
            "**When to use:** repetitive boilerplate (logging, DTO mapping, options validation) that must stay in sync with attributes. "
            "**Pitfall:** debugging generated code requires inspecting `*.g.cs` under `obj/` — document generated APIs for teammates."
        ),
        "code": r"""// Compile-time generated logger — no params array allocation
public partial class OrderService(ILogger<OrderService> logger)
{
    [LoggerMessage(Level = LogLevel.Information, Message = "Order {OrderId} placed by {Customer}")]
    public partial void LogOrderPlaced(int orderId, string customer);

    public async Task PlaceAsync(Order order, CancellationToken ct)
    {
        await _repo.SaveAsync(order, ct);
        LogOrderPlaced(order.Id, order.CustomerName); // generated implementation
    }
}

// Regex source generator — optimized finite automaton at compile time
[GeneratedRegex(@"^[\w\.-]+@[\w\.-]+\.\w+$", RegexOptions.IgnoreCase)]
private static partial Regex EmailRegex();

public bool IsValidEmail(string email) => EmailRegex().IsMatch(email);

// Custom generator packages referenced like normal NuGet libs
// Analyzer + generator run during dotnet build""",
        "language": "csharp",
        "key_points": [
            "Code emitted at compile time — no runtime reflection",
            "LoggerMessage and GeneratedRegex are built-in examples",
            "IIncrementalGenerator for large solution performance",
            "Inspect generated *.g.cs under obj/ when debugging",
            "Ideal for repetitive, performance-critical boilerplate",
        ],
    },
    "minimal-apis": {
        "explanation": (
            "**Minimal APIs** map HTTP routes directly to delegate handlers in `Program.cs` — less ceremony than MVC controllers "
            "for small services, microservices, and prototypes. "
            "They support **dependency injection**, **model binding**, **validation**, **OpenAPI**, and **endpoint filters** (.NET 7+). "
            "Route groups (`app.MapGroup('/api/v1')`) organize endpoints; `TypedResults`/`Results` provide strongly typed status codes. "
            "**When to choose:** focused REST/gRPC gateways, BFF layers, or teams preferring top-level statements over controller classes. "
            "**When to avoid:** large CRUD apps with complex filter pipelines — MVC controllers may scale better organizationally. "
            "**Pitfall:** business logic bloating `Program.cs` — extract handlers to static classes or extension methods."
        ),
        "code": """var builder = WebApplication.CreateBuilder(args);
builder.Services.AddScoped<IOrderService, OrderService>();
var app = builder.Build();

var orders = app.MapGroup("/api/orders").WithTags("Orders");

orders.MapGet("/{id:int}", async (int id, IOrderService svc, CancellationToken ct) =>
{
    var order = await svc.GetByIdAsync(id, ct);
    return order is null ? Results.NotFound() : Results.Ok(order);
})
.Produces<OrderDto>(StatusCodes.Status200OK)
.Produces(StatusCodes.Status404NotFound);

orders.MapPost("/", async (CreateOrderDto dto, IOrderService svc, CancellationToken ct) =>
{
    var id = await svc.CreateAsync(dto, ct);
    return Results.Created($"/api/orders/{id}", new { id });
});

app.Run();""",
        "language": "csharp",
        "key_points": [
            "Less boilerplate than controllers for small APIs",
            "Full DI, binding, validation, and OpenAPI support",
            "MapGroup organizes routes with shared metadata",
            "Endpoint filters replace some MVC filter scenarios",
            "Extract handlers to keep Program.cs maintainable",
        ],
    },
    "cors": {
        "explanation": (
            "**CORS (Cross-Origin Resource Sharing)** lets browsers call your API from a **different origin** (scheme/host/port) "
            "by returning `Access-Control-*` headers on preflight `OPTIONS` and actual requests. "
            "Register named policies in `AddCors` and apply with `UseCors` **before** authentication/authorization middleware. "
            "Restrict **`WithOrigins`** to known frontends; avoid `AllowAnyOrigin()` when **`AllowCredentials()`** is required — the spec forbids that combination. "
            "**Why it matters:** SPAs on Azure Static Web Apps or localhost:4200 must call APIs on another port/domain. "
            "**Pitfall:** CORS is a browser-only policy — Postman and server-to-server calls ignore it; still enforce auth server-side."
        ),
        "code": """// Program.cs
builder.Services.AddCors(options =>
{
    options.AddPolicy("ProductionSpa", policy => policy
        .WithOrigins("https://app.contoso.com", "https://staging.contoso.com")
        .AllowAnyHeader()
        .AllowAnyMethod()
        .AllowCredentials()); // cookies / Authorization from browser

    options.AddPolicy("DevOpen", policy => policy
        .WithOrigins("http://localhost:4200")
        .AllowAnyHeader()
        .AllowAnyMethod());
});

var app = builder.Build();
app.UseCors(app.Environment.IsDevelopment() ? "DevOpen" : "ProductionSpa");
app.UseAuthentication();
app.UseAuthorization();

app.MapGet("/api/orders", () => Results.Ok(new[] { 1, 2, 3 }))
   .RequireAuthorization();""",
        "language": "csharp",
        "key_points": [
            "UseCors must run before UseAuthentication",
            "Named policies per environment/frontend",
            "AllowAnyOrigin incompatible with AllowCredentials",
            "Browsers send OPTIONS preflight for non-simple requests",
            "CORS does not replace authentication or authorization",
        ],
    },
    "openapi-swagger": {
        "explanation": (
            "**OpenAPI** describes your HTTP API contract (paths, schemas, auth) as JSON/YAML; **Swagger UI** renders it for developers and QA. "
            "ASP.NET Core uses **`AddEndpointsApiExplorer`** + **Swashbuckle** (`AddSwaggerGen`) or **NSwag** to generate specs from controllers or Minimal APIs. "
            "Annotate with `[ProducesResponseType]`, XML comments, and security schemes so consumers see accurate models. "
            "Expose Swagger UI **only in Development** or protect it behind auth in staging — public prod Swagger leaks attack surface. "
            "**Why it matters:** drives client codegen (TypeScript Angular services), contract tests, and API gateways. "
            "**Pitfall:** stale schemas when DTOs change — enable CI validation that OpenAPI matches implementation."
        ),
        "code": """builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options =>
{
    options.SwaggerDoc("v1", new OpenApiInfo { Title = "Order API", Version = "v1" });
    options.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
    {
        Name = "Authorization",
        Type = SecuritySchemeType.Http,
        Scheme = "bearer",
        BearerFormat = "JWT"
    });
});

var app = builder.Build();
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(c => c.SwaggerEndpoint("/swagger/v1/swagger.json", "Order API v1"));
}

// Minimal API metadata flows into OpenAPI
app.MapGet("/orders/{id}", (int id) => Results.Ok(new OrderDto(id, "Alice", 10)))
   .WithName("GetOrder")
   .Produces<OrderDto>(200)
   .ProducesProblem(404);""",
        "language": "csharp",
        "key_points": [
            "AddEndpointsApiExplorer required for Minimal APIs",
            "Swashbuckle or NSwag generates OpenAPI at runtime/build",
            "Document JWT/OAuth security schemes for clients",
            "Restrict or disable Swagger UI in production",
            "Use WithName/Produces for accurate Minimal API docs",
        ],
    },
    "content-negotiation": {
        "explanation": (
            "**Content negotiation** selects the **response format** based on the client's `Accept` header (JSON, XML, CSV) "
            "using ASP.NET Core **output formatters**. "
            "Returning `Results.Ok(dto)` typically serializes JSON via **System.Text.Json**; custom formatters handle XML or proprietary types. "
            "Return **406 Not Acceptable** when no formatter matches requested media types. "
            "For APIs, most teams **standardize on JSON** and ignore negotiation — but enterprise integrations still expect XML. "
            "**Why it matters:** interviewers test whether you know formatters vs ad-hoc string responses. "
            "**Pitfall:** returning raw strings bypasses negotiation and problem details — prefer typed results."
        ),
        "code": """builder.Services.AddControllers(o =>
{
    o.ReturnHttpNotAcceptable = true; // 406 when Accept cannot be satisfied
})
.AddXmlSerializerFormatters(); // optional XML support

// Controller — formatters pick JSON vs XML from Accept
[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase
{
    [HttpGet("{id}")]
    [Produces("application/json", "application/xml")]
    public ActionResult<OrderDto> Get(int id) =>
        Ok(new OrderDto(id, "Alice", 99.99m));
}

// Minimal API — explicit produces metadata
app.MapGet("/orders/{id}", (int id) => Results.Ok(new OrderDto(id, "Bob", 1)))
   .Produces<OrderDto>(200, "application/json");""",
        "language": "csharp",
        "key_points": [
            "Accept header drives formatter selection",
            "ReturnHttpNotAcceptable yields 406",
            "System.Text.Json is default JSON serializer",
            "AddXmlSerializerFormatters for legacy XML clients",
            "Prefer typed Results over manual Content-Type strings",
        ],
    },
    "cookie-auth": {
        "explanation": (
            "**Cookie authentication** stores an **encrypted auth ticket** in an HTTP cookie after login — ideal for **same-site web apps** "
            "and MVC/Razor, less common for pure SPAs than JWT + API. "
            "Configure **`AddCookie`** with `LoginPath`, `AccessDeniedPath`, **sliding expiration**, and **`Cookie.HttpOnly`** to block JavaScript theft. "
            "Set **`SameSite=Lax/Strict`** and **`Secure`** in production to mitigate CSRF and man-in-the-middle attacks. "
            "Works seamlessly with **ASP.NET Core Identity** and external providers. "
            "**Why it matters:** enterprise intranet apps and Blazor Server often use cookies; know tradeoffs vs bearer tokens. "
            "**Pitfall:** cross-domain SPAs need token-based auth or BFF pattern — cookies alone fail CORS credential complexity."
        ),
        "code": """builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
    .AddCookie(options =>
    {
        options.LoginPath = "/account/login";
        options.AccessDeniedPath = "/account/forbidden";
        options.SlidingExpiration = true;
        options.ExpireTimeSpan = TimeSpan.FromHours(8);
        options.Cookie.HttpOnly = true;
        options.Cookie.SecurePolicy = CookieSecurePolicy.Always;
        options.Cookie.SameSite = SameSiteMode.Lax;
    });

app.UseAuthentication();
app.UseAuthorization();

app.MapPost("/account/login", async (LoginDto dto, SignInManager<AppUser> signIn) =>
{
    var result = await signIn.PasswordSignInAsync(dto.Email, dto.Password, dto.RememberMe, lockoutOnFailure: true);
    return result.Succeeded ? Results.Ok() : Results.Unauthorized();
}).AllowAnonymous();

app.MapGet("/account/me", (ClaimsPrincipal user) => Results.Ok(user.Identity?.Name)).RequireAuthorization();""",
        "language": "csharp",
        "key_points": [
            "Encrypted auth ticket in HttpOnly cookie",
            "SameSite + Secure are mandatory in production",
            "Sliding expiration extends session on activity",
            "Common with Identity and server-rendered apps",
            "Cross-domain SPAs often prefer JWT or BFF",
        ],
    },
    "problem-details": {
        "explanation": (
            "**ProblemDetails** (RFC 7807) is a **standard JSON error shape** with `type`, `title`, `status`, `detail`, and optional `extensions` — "
            "replacing ad-hoc `{ error: \"...\" }` payloads. "
            "Call **`builder.Services.AddProblemDetails()`** and use **`Results.Problem()`** or **`TypedResults.Problem()`** in Minimal APIs; "
            "validation failures map to **400** with field-level extensions. "
            "Clients (Angular interceptors) can branch on `status` and `title` consistently across services. "
            "**Why it matters:** Microsoft APIs, Azure, and modern REST guidelines expect ProblemDetails — interviewers ask for global error consistency. "
            "**Pitfall:** leaking exception messages/stack traces in `detail` — log internally, return generic messages in production."
        ),
        "code": """builder.Services.AddProblemDetails(options =>
{
    options.CustomizeProblemDetails = ctx =>
    {
        ctx.ProblemDetails.Extensions["traceId"] = ctx.HttpContext.TraceIdentifier;
        if (ctx.HttpContext.Response.StatusCode >= 500)
            ctx.ProblemDetails.Detail = "An unexpected error occurred."; // hide internals
    };
});

app.UseExceptionHandler();
app.UseStatusCodePages();

app.MapGet("/orders/{id}", (int id) =>
{
    if (id <= 0)
        return Results.ValidationProblem(new Dictionary<string, string[]>
        {
            ["id"] = ["Must be positive."]
        });

    return id == 42
        ? Results.Ok(new { id })
        : Results.Problem(title: "Order not found", statusCode: 404, detail: $"No order {id}.");
});""",
        "language": "csharp",
        "key_points": [
            "RFC 7807 standard fields: type, title, status, detail",
            "AddProblemDetails() registers global configuration",
            "Results.Problem and ValidationProblem in Minimal APIs",
            "Include traceId extension for support correlation",
            "Never expose stack traces in production detail",
        ],
    },
    "rate-limiting": {
        "explanation": (
            "ASP.NET Core **7+** ships **`Microsoft.AspNetCore.RateLimiting`** middleware to protect APIs from abuse and accidental overload. "
            "Algorithms include **fixed window**, **sliding window**, **token bucket**, and **concurrency** limiters. "
            "Partition keys by **user id**, **IP**, or **API key** so one tenant cannot exhaust global capacity. "
            "On rejection, return **429 Too Many Requests** with **`Retry-After`** header. "
            "**Why it matters:** public APIs, login endpoints, and webhooks are common abuse targets — rate limiting complements WAF/API Management. "
            "**Pitfall:** overly aggressive limits break legitimate bulk clients — tune per endpoint and expose metrics."
        ),
        "code": """builder.Services.AddRateLimiter(options =>
{
    options.RejectionStatusCode = StatusCodes.Status429TooManyRequests;

    options.AddFixedWindowLimiter("fixed", opt =>
    {
        opt.Window = TimeSpan.FromMinutes(1);
        opt.PermitLimit = 100;
        opt.QueueLimit = 0;
    });

    options.GlobalLimiter = PartitionedRateLimiter.Create<HttpContext, string>(ctx =>
        RateLimitPartition.GetFixedWindowLimiter(
            partitionKey: ctx.User.Identity?.Name ?? ctx.Connection.RemoteIpAddress?.ToString() ?? "anon",
            factory: _ => new FixedWindowRateLimiterOptions
            {
                Window = TimeSpan.FromMinutes(1),
                PermitLimit = 60
            }));
});

var app = builder.Build();
app.UseRateLimiter();

app.MapGet("/api/orders", () => Results.Ok())
   .RequireRateLimiting("fixed");""",
        "language": "csharp",
        "key_points": [
            "Built-in middleware since ASP.NET Core 7",
            "Fixed, sliding, token bucket, and concurrency limiters",
            "Partition by user, IP, or custom key",
            "Return 429 with Retry-After on rejection",
            "Apply per-endpoint with RequireRateLimiting",
        ],
    },
    "output-caching": {
        "explanation": (
            "**Output caching** (.NET 7+) stores **entire HTTP responses** (status, headers, body) server-side and serves them "
            "for identical subsequent requests — faster than recomputing or hitting the database. "
            "Unlike deprecated **Response caching**, output caching supports **cache profiles**, **tag-based invalidation**, "
            "and pluggable stores (memory, Redis via community packages). "
            "Use **`CacheOutput`** on Minimal APIs or `[OutputCache]` on controllers; vary by query, route, headers, or auth. "
            "**When to use:** read-heavy, rarely changing catalog/reference data. "
            "**Pitfall:** caching personalized or authorized responses without **`VaryByUser`** leaks data across users."
        ),
        "code": """builder.Services.AddOutputCache(options =>
{
    options.AddBasePolicy(b => b.Expire(TimeSpan.FromSeconds(30)));
    options.AddPolicy("Catalog", b => b.Expire(TimeSpan.FromMinutes(5)).Tag("catalog"));
});

var app = builder.Build();
app.UseOutputCache();

app.MapGet("/catalog", async (ICatalogService svc, CancellationToken ct) =>
    Results.Ok(await svc.GetAllAsync(ct)))
   .CacheOutput("Catalog");

// Invalidate when catalog changes
app.MapPost("/catalog/refresh", async (IOutputCacheStore cache, CancellationToken ct) =>
{
    await cache.EvictByTagAsync("catalog", ct);
    return Results.NoContent();
}).RequireAuthorization();""",
        "language": "csharp",
        "key_points": [
            "Stores full response — faster than response caching",
            "CacheOutput / [OutputCache] with named policies",
            "Tag-based eviction for invalidation",
            "Vary by user/query when responses differ",
            "Never cache authorized data without user partition",
        ],
    },
    "api-versioning": {
        "explanation": (
            "**API versioning** lets you evolve contracts without breaking existing clients — common strategies: **URL path** (`/v2/orders`), "
            "**query string** (`?api-version=2.0`), **header** (`X-Api-Version`), or **media type**. "
            "Use **`Asp.Versioning.Http`** (formerly Microsoft.AspNetCore.Mvc.Versioning) with **`AddApiVersioning`** and **`AddApiExplorer`** for OpenAPI. "
            "Mark deprecated versions with **`Deprecated`** and **`Sunset`** headers so clients migrate. "
            "**Why it matters:** enterprise APIs commit to backward compatibility — versioning is a release discipline question. "
            "**Pitfall:** supporting too many versions indefinitely — publish a retirement policy."
        ),
        "code": """builder.Services.AddApiVersioning(options =>
{
    options.DefaultApiVersion = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions = true;
    options.ApiVersionReader = ApiVersionReader.Combine(
        new UrlSegmentApiVersionReader(),
        new HeaderApiVersionReader("X-Api-Version"));
})
.AddApiExplorer(options =>
{
    options.GroupNameFormat = "'v'VVV";
    options.SubstituteApiVersionInUrl = true;
});

// Minimal API version set
var v1 = app.NewVersionedApi().MapGroup("/api/v{version:apiVersion}")
    .HasApiVersion(1, 0);
v1.MapGet("/orders", () => Results.Ok(new[] { "legacy-order" }));

var v2 = app.NewVersionedApi().MapGroup("/api/v{version:apiVersion}")
    .HasApiVersion(2, 0);
v2.MapGet("/orders", () => Results.Ok(new[] { new { id = 1, total = 10m } }));""",
        "language": "csharp",
        "key_points": [
            "URL, header, query, or media-type version readers",
            "Asp.Versioning.Http is the modern package",
            "ReportApiVersions exposes supported versions",
            "Integrate with Swagger for per-version docs",
            "Deprecate old versions with sunset policy",
        ],
    },
    "global-exception-handling": {
        "explanation": (
            "**Global exception handling** centralizes unhandled errors into consistent **ProblemDetails** responses and structured logs — "
            "avoid try/catch in every action. "
            "Use **`UseExceptionHandler`** middleware or implement **`IExceptionHandler`** (.NET 8+) for pluggable handlers. "
            "Map exception types to status codes: **`ValidationException` → 400**, **`KeyNotFoundException` → 404**, unknown → **500**. "
            "Log full exception with **`ILogger`** and **`Activity`** trace id; return safe messages to clients. "
            "**Why it matters:** production APIs must never leak stack traces; observability requires one choke point. "
            "**Pitfall:** swallowing exceptions without rethrow/logging — always record before returning Problem response."
        ),
        "code": """// .NET 8+ — IExceptionHandler
public class GlobalExceptionHandler(ILogger<GlobalExceptionHandler> logger) : IExceptionHandler
{
    public async ValueTask<bool> TryHandleAsync(
        HttpContext ctx, Exception ex, CancellationToken ct)
    {
        logger.LogError(ex, "Unhandled exception {TraceId}", ctx.TraceIdentifier);

        var (status, title) = ex switch
        {
            ArgumentException => (400, "Bad request"),
            KeyNotFoundException => (404, "Not found"),
            UnauthorizedAccessException => (403, "Forbidden"),
            _ => (500, "Internal server error")
        };

        await Results.Problem(title: title, statusCode: status, extensions: new Dictionary<string, object?>
        {
            ["traceId"] = ctx.TraceIdentifier
        }).ExecuteAsync(ctx);

        return true; // exception handled
    }
}

builder.Services.AddExceptionHandler<GlobalExceptionHandler>();
builder.Services.AddProblemDetails();
var app = builder.Build();
app.UseExceptionHandler();""",
        "language": "csharp",
        "key_points": [
            "UseExceptionHandler catches unhandled pipeline exceptions",
            "IExceptionHandler (.NET 8+) for typed, testable handlers",
            "Map exception types to HTTP status codes",
            "Log full detail; return safe ProblemDetails to clients",
            "Combine with AddProblemDetails for consistent shape",
        ],
    },
    "endpoint-filters": {
        "explanation": (
            "**Endpoint filters** are Minimal API middleware scoped to a **single route or group** — like action filters but for delegates. "
            "Implement **`IEndpointFilter`** or use **`AddEndpointFilter`** with a lambda; filters run before/after the handler via **`next(context)`**. "
            "Use cases: **validation**, **logging**, **transaction scopes**, and **authorization shortcuts**. "
            "They replace some MVC filter scenarios with less overhead and clearer pipeline order. "
            "**Why it matters:** common 2025 interview question linking Minimal APIs to cross-cutting concerns. "
            "**Pitfall:** duplicating logic across many routes — apply filters at **`MapGroup`** level for DRY."
        ),
        "code": """public class ValidateOrderFilter : IEndpointFilter
{
    public async ValueTask<object?> InvokeAsync(
        EndpointFilterInvocationContext ctx, EndpointFilterDelegate next)
    {
        var dto = ctx.Arguments.OfType<CreateOrderDto>().FirstOrDefault();
        if (dto is null || dto.Quantity <= 0)
            return Results.ValidationProblem(new Dictionary<string, string[]>
            {
                ["quantity"] = ["Must be greater than zero."]
            });

        return await next(ctx);
    }
}

var orders = app.MapGroup("/api/orders");
orders.MapPost("/", async (CreateOrderDto dto, IOrderService svc) =>
{
    var id = await svc.CreateAsync(dto);
    return Results.Created($"/api/orders/{id}", new { id });
})
.AddEndpointFilter<ValidateOrderFilter>()
.AddEndpointFilter(async (ctx, next) =>
{
    // Simple logging filter
    var sw = Stopwatch.StartNew();
    var result = await next(ctx);
    app.Logger.LogInformation("Handler completed in {Ms}ms", sw.ElapsedMilliseconds);
    return result;
});""",
        "language": "csharp",
        "key_points": [
            "IEndpointFilter wraps Minimal API handlers",
            "AddEndpointFilter on route or MapGroup",
            "Use for validation, logging, auth checks",
            "Call next(ctx) to continue the pipeline",
            "Prefer group-level filters to avoid duplication",
        ],
    },
    "antiforgery": {
        "explanation": (
            "**Antiforgery** mitigates **CSRF** attacks by requiring a secret **request token** matching a **cookie token** on state-changing requests (POST/PUT/DELETE). "
            "Razor forms embed tokens automatically; **SPAs** fetch a token and send it via header (`X-CSRF-TOKEN` or `RequestVerificationToken`). "
            "Register with **`AddAntiforgery`** and validate using **`ValidateAntiForgeryToken`** or endpoint metadata. "
            "Pair with **`SameSite`** cookies and avoid cross-site cookie auth without additional protections. "
            "**Why it matters:** cookie-authenticated MVC/Blazor apps require antiforgery; APIs using JWT typically rely on CORS + no cookies instead. "
            "**Pitfall:** disabling antiforgery on cookie-auth endpoints opens CSRF — never skip for convenience."
        ),
        "code": """builder.Services.AddAntiforgery(options =>
{
    options.HeaderName = "X-CSRF-TOKEN";
    options.Cookie.Name = "__Host-XSRF";
    options.Cookie.SecurePolicy = CookieSecurePolicy.Always;
});

// SPA: GET token, POST with header
app.MapGet("/antiforgery/token", (IAntiforgery antiforgery, HttpContext ctx) =>
{
    var tokens = antiforgery.GetAndStoreTokens(ctx);
    return Results.Ok(new { token = tokens.RequestToken });
});

app.MapPost("/account/profile", async (ProfileDto dto, HttpContext ctx, IAntiforgery af) =>
{
    await af.ValidateRequestAsync(ctx); // throws if token invalid
    // update profile
    return Results.NoContent();
});""",
        "language": "csharp",
        "key_points": [
            "Double-submit cookie + request token pattern",
            "Required for cookie-auth state-changing requests",
            "SPAs send token via custom header",
            "AddAntiforgery configures cookie and header names",
            "JWT-only APIs often skip; cookie apps must not",
        ],
    },
    "request-response-logging": {
        "explanation": (
            "**Request/response logging middleware** captures HTTP metadata — method, path, status, duration — for troubleshooting and audit. "
            "Implement custom **`RequestDelegate`** middleware or use **Serilog.AspNetCore** `UseSerilogRequestLogging()` for structured logs. "
            "**Never log** bodies containing passwords, tokens, or PCI data; redact **`Authorization`** headers. "
            "Correlate with **`TraceIdentifier`** or OpenTelemetry **`Activity`** for distributed tracing. "
            "**Why it matters:** every production API needs observability; interviewers distinguish safe logging from compliance violations. "
            "**Pitfall:** logging full request bodies in production kills performance and violates GDPR — log hashes or sizes instead."
        ),
        "code": """public class SafeRequestLoggingMiddleware(RequestDelegate next, ILogger<SafeRequestLoggingMiddleware> log)
{
    public async Task InvokeAsync(HttpContext ctx)
    {
        var sw = Stopwatch.StartNew();
        try
        {
            await next(ctx);
        }
        finally
        {
            sw.Stop();
            log.LogInformation(
                "HTTP {Method} {Path} => {Status} in {ElapsedMs}ms trace={TraceId}",
                ctx.Request.Method,
                ctx.Request.Path.Value,
                ctx.Response.StatusCode,
                sw.ElapsedMilliseconds,
                ctx.TraceIdentifier);
        }
    }
}

// Serilog — preferred in many teams
// app.UseSerilogRequestLogging(o => o.EnrichDiagnosticContext = (diag, http) =>
//     diag.Set("User", http.User.Identity?.Name ?? "anonymous"));

app.UseMiddleware<SafeRequestLoggingMiddleware>();""",
        "language": "csharp",
        "key_points": [
            "Log method, path, status, duration, trace id",
            "Redact Authorization and sensitive body fields",
            "Serilog request logging is a common production choice",
            "Place early but after exception handler if needed",
            "Correlate logs with OpenTelemetry traces",
        ],
    },
    "api-security-headers": {
        "explanation": (
            "**Security headers** harden browsers against common attacks even when app code is correct. "
            "Set **`Strict-Transport-Security`** (HSTS) to force HTTPS, **`X-Content-Type-Options: nosniff`**, "
            "**`X-Frame-Options: DENY`** or **`Content-Security-Policy`**, and **`Referrer-Policy`**. "
            "Use **`UseHsts()`**, **`UseHttpsRedirection()`**, and middleware or **`NWebsec`** / reverse proxy (Front Door) for consistent headers. "
            "**Why it matters:** OWASP and security audits check headers; missing HSTS/CSP fails penetration tests. "
            "**Pitfall:** overly strict CSP breaks Swagger UI or SPA inline scripts — tune per environment."
        ),
        "code": """var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseHsts(); // Strict-Transport-Security
}

app.UseHttpsRedirection();

app.Use(async (ctx, next) =>
{
    ctx.Response.Headers["X-Content-Type-Options"] = "nosniff";
    ctx.Response.Headers["X-Frame-Options"] = "DENY";
    ctx.Response.Headers["Referrer-Policy"] = "strict-origin-when-cross-origin";
    ctx.Response.Headers["Content-Security-Policy"] =
        "default-src 'self'; frame-ancestors 'none';";
    await next(ctx);
});

// Or package: app.UseSecurityHeaders(policies => policies.AddDefaultSecurityHeaders());""",
        "language": "csharp",
        "key_points": [
            "HSTS forces HTTPS in supporting browsers",
            "X-Content-Type-Options prevents MIME sniffing",
            "X-Frame-Options / CSP reduce clickjacking",
            "Apply at middleware or reverse proxy layer",
            "Relax CSP in Development for Swagger/SPA tooling",
        ],
    },
    "websockets": {
        "explanation": (
            "**WebSockets** provide a **full-duplex persistent TCP** connection upgraded from HTTP — lower latency than polling for live data. "
            "Enable with **`UseWebSockets`** middleware, then accept connections in a branch or Minimal API delegate via **`HttpContext.WebSockets`**. "
            "Handle **receive/send loops**, **close handshakes**, and **CancellationToken** on disconnect. "
            "For app-level messaging, **SignalR** is preferred — it manages reconnect, groups, and fallback transports. "
            "**Why it matters:** interviews test raw WebSocket knowledge vs SignalR abstraction. "
            "**Pitfall:** WebSockets behind load balancers require **sticky sessions** or shared backplane; idle timeouts kill long connections."
        ),
        "code": """var app = builder.Build();
app.UseWebSockets(new WebSocketOptions { KeepAliveInterval = TimeSpan.FromSeconds(30) });

app.Map("/ws/chat", async (HttpContext ctx) =>
{
    if (!ctx.WebSockets.IsWebSocketRequest)
    {
        ctx.Response.StatusCode = StatusCodes.Status400BadRequest;
        return;
    }

    using var socket = await ctx.WebSockets.AcceptWebSocketAsync();
    var buffer = new byte[4096];

    while (socket.State == WebSocketState.Open)
    {
        var result = await socket.ReceiveAsync(buffer, ctx.RequestAborted);
        if (result.MessageType == WebSocketMessageType.Close)
            await socket.CloseAsync(WebSocketCloseStatus.NormalClosure, "bye", ctx.RequestAborted);
        else
        {
            var text = Encoding.UTF8.GetString(buffer, 0, result.Count);
            var reply = Encoding.UTF8.GetBytes($"echo: {text}");
            await socket.SendAsync(reply, WebSocketMessageType.Text, true, ctx.RequestAborted);
        }
    }
});""",
        "language": "csharp",
        "key_points": [
            "HTTP upgrade to full-duplex WebSocket",
            "UseWebSockets middleware required",
            "Handle close frames and CancellationToken",
            "Prefer SignalR for production real-time apps",
            "Load balancers need sticky sessions or backplane",
        ],
    },
    "grpc-aspnet": {
        "explanation": (
            "**gRPC** is a high-performance **RPC framework** using **HTTP/2** and **Protocol Buffers** — ideal for internal microservice communication. "
            "Add **`Grpc.AspNetCore`**, define `.proto` services, implement derived **`ServiceBase`** classes, and map with **`MapGrpcService<T>()`**. "
            "Supports **unary**, **server streaming**, **client streaming**, and **bidirectional** calls. "
            "Browsers need **gRPC-Web** via Envoy/YARP; native gRPC works service-to-service. "
            "**Why it matters:** .NET shops use gRPC for low-latency internal APIs; REST outward, gRPC inward is a common pattern. "
            "**Pitfall:** requires HTTP/2 end-to-end — TLS ALPN or h2c in dev; misconfigured Kestrel/IIS breaks silently."
        ),
        "code": """// order.proto → generated C# stubs
// service OrderService { rpc GetOrder (GetOrderRequest) returns (OrderReply); }

public class OrderGrpcService : Order.OrderBase
{
    public override async Task<OrderReply> GetOrder(
        GetOrderRequest request, ServerCallContext context)
    {
        var order = await _repo.GetAsync(request.Id, context.CancellationToken);
        return order is null
            ? throw new RpcException(new Status(StatusCode.NotFound, "Order not found"))
            : new OrderReply { Id = order.Id, Total = (double)order.Total };
    }
}

builder.Services.AddGrpc();
var app = builder.Build();
app.MapGrpcService<OrderGrpcService>();
// Client: channel = GrpcChannel.ForAddress("https://localhost:5001");""",
        "language": "csharp",
        "key_points": [
            "HTTP/2 + Protobuf binary contract",
            "MapGrpcService registers gRPC endpoints",
            "Streaming RPC for live feeds and bulk data",
            "gRPC-Web needed for browser clients",
            "Strong typing and codegen from .proto files",
        ],
    },
    "oauth-oidc": {
        "explanation": (
            "**OAuth 2.0** delegates authorization; **OpenID Connect (OIDC)** adds identity (`id_token`, `/userinfo`) on top. "
            "ASP.NET Core uses **`AddOpenIdConnect`** for interactive login and **`AddJwtBearer`** for API token validation — "
            "often against **Microsoft Entra ID**, Auth0, or Keycloak. "
            "Public clients (SPAs) must use **Authorization Code + PKCE**, never implicit flow. "
            "Map **`ClaimTypes.Role`** or custom claims to **`[Authorize(Roles = \"Admin\")]`** or policies. "
            "**Why it matters:** enterprise .NET roles expect Entra ID integration fluency. "
            "**Pitfall:** validating tokens without checking **issuer**, **audience**, and **lifetime** — always configure `TokenValidationParameters`."
        ),
        "code": """builder.Services.AddAuthentication(options =>
{
    options.DefaultScheme = CookieAuthenticationDefaults.AuthenticationScheme;
    options.DefaultChallengeScheme = OpenIdConnectDefaults.AuthenticationScheme;
})
.AddCookie()
.AddOpenIdConnect(OpenIdConnectDefaults.AuthenticationScheme, options =>
{
    options.Authority = "https://login.microsoftonline.com/{tenant-id}/v2.0";
    options.ClientId = builder.Configuration["AzureAd:ClientId"];
    options.ClientSecret = builder.Configuration["AzureAd:ClientSecret"];
    options.ResponseType = OpenIdConnectResponseType.Code;
    options.UsePkce = true;
    options.SaveTokens = true;
    options.Scope.Add("openid");
    options.Scope.Add("profile");
    options.Scope.Add("offline_access");
});

// API — validate access tokens from same authority
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(o =>
    {
        o.Authority = "https://login.microsoftonline.com/{tenant-id}/v2.0";
        o.Audience = "api://order-api-client-id";
    });""",
        "language": "csharp",
        "key_points": [
            "OIDC = OAuth2 + identity id_token",
            "Authorization Code + PKCE for SPAs and mobile",
            "AddOpenIdConnect for sign-in; JwtBearer for APIs",
            "Validate issuer, audience, signing keys, expiry",
            "Entra ID is the common enterprise identity provider",
        ],
    },
    "signalr": {
        "explanation": (
            "**SignalR** abstracts real-time messaging over **WebSockets**, **Server-Sent Events**, or **long polling** with automatic fallback. "
            "Define **`Hub`** classes with methods callable from clients; server pushes via **`Clients.All.SendAsync`**, **groups**, or **connection ids**. "
            "Scale out with **Redis**, **Azure SignalR Service**, or **Service Bus** backplane so multiple server instances share connection state. "
            "Authenticate hubs with **`[Authorize]`** and pass JWT via query string or headers during negotiate. "
            "**Why it matters:** dashboards, chat, live notifications — common full-stack interview scenario with Angular client. "
            "**Pitfall:** broadcasting to all clients (`Clients.All`) does not scale — use groups and targeted sends."
        ),
        "code": """public class OrderHub : Hub
{
    public async Task JoinWarehouse(string warehouseId) =>
        await Groups.AddToGroupAsync(Context.ConnectionId, warehouseId);

    public async Task NotifyOrderShipped(string warehouseId, int orderId) =>
        await Clients.Group(warehouseId).SendAsync("OrderShipped", orderId);
}

builder.Services.AddSignalR();
var app = builder.Build();
app.MapHub<OrderHub>("/hubs/orders");

// From a service after save
public class OrderNotifier(IHubContext<OrderHub> hub)
{
    public Task ShippedAsync(string warehouseId, int orderId) =>
        hub.Clients.Group(warehouseId).SendAsync("OrderShipped", orderId);
}

// Angular: new HubConnectionBuilder().withUrl('/hubs/orders').build()""",
        "language": "csharp",
        "key_points": [
            "Hubs abstract WebSocket transport and reconnect",
            "Groups target subsets of connected clients",
            "IHubContext for pushing from outside the hub",
            "Azure SignalR Service for managed scale-out",
            "Authorize hubs; avoid Clients.All at scale",
        ],
    },
    "background-services": {
        "explanation": (
            "**IHostedService** runs background work for the lifetime of the app; **`BackgroundService`** base class simplifies long-running loops with **`ExecuteAsync`**. "
            "Register via **`AddHostedService<T>()`** — ideal for queue consumers, cache warmers, and periodic sync jobs. "
            "Respect **`CancellationToken`** on shutdown so Kestrel drains gracefully in Kubernetes. "
            "Use **`Channel<T>`** or **Azure Service Bus** for producer/consumer patterns instead of blocking threads. "
            "**Why it matters:** not everything belongs in HTTP requests — interviews test hosted service vs Hangfire/Quartz choice. "
            "**Pitfall:** scoped services (DbContext) cannot be injected into singleton hosted services — create a scope with **`IServiceScopeFactory`**."
        ),
        "code": """public class OutboxDispatcher(
    IServiceScopeFactory scopeFactory,
    ILogger<OutboxDispatcher> logger) : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            try
            {
                await using var scope = scopeFactory.CreateAsyncScope();
                var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
                var pending = await db.OutboxMessages
                    .Where(m => m.ProcessedAt == null)
                    .Take(10)
                    .ToListAsync(stoppingToken);

                foreach (var msg in pending)
                {
                    // dispatch to Service Bus, etc.
                    msg.ProcessedAt = DateTime.UtcNow;
                }
                await db.SaveChangesAsync(stoppingToken);
            }
            catch (Exception ex) when (!stoppingToken.IsCancellationRequested)
            {
                logger.LogError(ex, "Outbox dispatch failed");
            }

            await Task.Delay(TimeSpan.FromSeconds(5), stoppingToken);
        }
    }
}

builder.Services.AddHostedService<OutboxDispatcher>();""",
        "language": "csharp",
        "key_points": [
            "BackgroundService implements IHostedService loop",
            "AddHostedService registers with DI container",
            "Use IServiceScopeFactory for scoped dependencies",
            "Honor CancellationToken on app shutdown",
            "Channel<T> or queues for backpressure",
        ],
    },
    "yarp-reverse-proxy": {
        "explanation": (
            "**YARP (Yet Another Reverse Proxy)** is a Microsoft **.NET reverse proxy** library — route incoming requests to backend clusters "
            "with load balancing, health checks, and transforms. "
            "Configure routes/clusters in **`appsettings.json`** or code via **`AddReverseProxy().LoadFromConfig()`** and **`MapReverseProxy()`**. "
            "Use as **API gateway**, **BFF**, or **canary routing** layer in front of microservices. "
            "Supports **pass-through auth**, **header transforms**, and **rate limiting** integration. "
            "**Why it matters:** replaces IIS ARR/nginx config with code-first routing in pure .NET shops. "
            "**Pitfall:** misconfigured cluster addresses cause silent 502s — always add **active health checks**."
        ),
        "code": """// appsettings.json
// "ReverseProxy": {
//   "Routes": { "orders-route": { "ClusterId": "orders", "Match": { "Path": "/api/orders/{**catch-all}" } } },
//   "Clusters": { "orders": { "Destinations": { "d1": { "Address": "https://orders.internal:5001/" } } } }
// }

builder.Services.AddReverseProxy()
    .LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));

var app = builder.Build();
app.MapReverseProxy();

// Optional transform — inject correlation id
builder.Services.AddReverseProxy()
    .LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"))
    .AddTransforms(builderContext =>
    {
        builderContext.AddRequestTransform(async transformContext =>
        {
            transformContext.ProxyRequest.Headers.TryAddWithoutValidation(
                "X-Correlation-Id", transformContext.HttpContext.TraceIdentifier);
        });
    });""",
        "language": "csharp",
        "key_points": [
            "Yet Another Reverse Proxy — Microsoft .NET library",
            "Routes and clusters from config or code",
            "Load balancing and health checks built-in",
            "Request/response transforms for headers/path",
            "Common as API gateway or BFF layer",
        ],
    },
    "opentelemetry-aspnet": {
        "explanation": (
            "**OpenTelemetry (OTel)** is the vendor-neutral standard for **traces**, **metrics**, and **logs** — replacing one-off App Insights SDK patterns. "
            "Add **`OpenTelemetry.Extensions.Hosting`** with **`AddAspNetCoreInstrumentation`**, **`AddHttpClientInstrumentation`**, "
            "and **`AddEntityFrameworkCoreInstrumentation`** for automatic spans. "
            "Export via **OTLP** to Azure Monitor, Grafana Tempo, Jaeger, or Datadog. "
            "Correlate **`Activity.TraceId`** with logs and **`ProblemDetails` extensions**. "
            "**Why it matters:** .NET 8+ templates and cloud-native interviews expect OTel over legacy telemetry APIs. "
            "**Pitfall:** missing **`UseRouting`**/middleware order can drop spans — register instrumentation before `Build()`."
        ),
        "code": """builder.Services.AddOpenTelemetry()
    .ConfigureResource(r => r.AddService("OrderApi"))
    .WithTracing(tracing => tracing
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddEntityFrameworkCoreInstrumentation()
        .AddOtlpExporter(o => o.Endpoint = new Uri("http://localhost:4317")))
    .WithMetrics(metrics => metrics
        .AddAspNetCoreInstrumentation()
        .AddRuntimeInstrumentation()
        .AddOtlpExporter());

// Logs — OpenTelemetry.Logs or ILogger bridge
builder.Logging.AddOpenTelemetry(o => o.IncludeFormattedMessage = true);

var app = builder.Build();
// Spans auto-created for HTTP requests and outgoing HttpClient calls""",
        "language": "csharp",
        "key_points": [
            "Vendor-neutral traces, metrics, and logs",
            "AddAspNetCoreInstrumentation for HTTP spans",
            "OTLP exporter to Azure Monitor / Grafana / Jaeger",
            "Correlate TraceId across logs and ProblemDetails",
            "Preferred telemetry approach in .NET 8+ cloud apps",
        ],
    },
}
