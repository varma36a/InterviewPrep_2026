"""Additional ASP.NET Core interview topics (2025/2026) — expands aspnet section."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("aspnet", "foundation"): [
        InterviewItem(
            "iactionresult-types",
            "What IActionResult types should you return from ASP.NET Core APIs?",
            "See detailed explanation.",
            """return Ok(order);
return CreatedAtAction(nameof(Get), new { id }, order);
return NotFound();
return Results.Problem(statusCode: 400);""",
            key_points=["Ok/Created/NoContent", "TypedResults in minimal APIs", "ProblemDetails for errors"],
        ),
        InterviewItem(
            "httpclient-factory",
            "Why use IHttpClientFactory instead of new HttpClient()?",
            "See detailed explanation.",
            """builder.Services.AddHttpClient<IWeatherClient, WeatherClient>();
public class WeatherClient(HttpClient http) { }""",
            key_points=["DNS refresh", "Handler lifetime", "Named/typed clients"],
        ),
        InterviewItem(
            "static-files",
            "How do you serve static files in ASP.NET Core?",
            "See detailed explanation.",
            """app.UseDefaultFiles();
app.UseStaticFiles();""",
            key_points=["wwwroot default", "UseStaticFiles order", "MapStaticAssets in .NET 9+"],
        ),
        InterviewItem(
            "data-protection",
            "What is ASP.NET Core Data Protection?",
            "See detailed explanation.",
            """builder.Services.AddDataProtection()
    .PersistKeysToAzureBlobStorage(connectionString, container, blob);""",
            key_points=["Encrypt cookies/tokens", "Key ring persistence", "Shared keys in farm"],
        ),
        InterviewItem(
            "forwarded-headers",
            "How do you configure forwarded headers behind a reverse proxy?",
            "See detailed explanation.",
            """builder.Services.Configure<ForwardedHeadersOptions>(o =>
{
    o.ForwardedHeaders = ForwardedHeaders.XForwardedFor | ForwardedHeaders.XForwardedProto;
});""",
            key_points=["X-Forwarded-For/Proto", "Known proxies", "HTTPS redirect correctness"],
        ),
        InterviewItem(
            "api-conventions",
            "What are ASP.NET Core API conventions?",
            "See detailed explanation.",
            """[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase { }""",
            key_points=["Automatic 400 on validation", "Attribute routing", "ProblemDetails defaults"],
        ),
        InterviewItem(
            "api-controller-attributes",
            "Explain common API controller attributes ([FromBody], [FromQuery], etc.).",
            "See detailed explanation.",
            """public IActionResult Search([FromQuery] string q, [FromBody] FilterDto filter)""",
            key_points=["Binding source attributes", "[FromRoute] for route params", "[FromServices] for DI"],
        ),
    ],
    ("aspnet", "intermediate"): [
        InterviewItem(
            "fluentvalidation",
            "How do you integrate FluentValidation in ASP.NET Core?",
            "See detailed explanation.",
            """public class CreateOrderValidator : AbstractValidator<CreateOrderDto>
{
    public CreateOrderValidator() => RuleFor(x => x.Quantity).GreaterThan(0);
}""",
            key_points=["AbstractValidator<T>", "Auto validation filter", "Separate from DTOs"],
        ),
        InterviewItem(
            "serilog-aspnet",
            "How do you configure Serilog in ASP.NET Core?",
            "See detailed explanation.",
            """Log.Logger = new LoggerConfiguration()
    .WriteTo.Console()
    .CreateLogger();
builder.Host.UseSerilog();""",
            key_points=["Structured sinks", "Request logging", "Replace default ILogger"],
        ),
        InterviewItem(
            "polly-resilience",
            "How do you add Polly resilience with HttpClient in .NET?",
            "See detailed explanation.",
            """builder.Services.AddHttpClient<IApiClient, ApiClient>()
    .AddStandardResilienceHandler();""",
            key_points=["Retry + circuit breaker", "AddStandardResilienceHandler", "Timeout policies"],
        ),
        InterviewItem(
            "mediatr-aspnet",
            "What is MediatR and how does it fit ASP.NET Core?",
            "See detailed explanation.",
            """public record GetOrderQuery(int Id) : IRequest<OrderDto?>;
public class Handler : IRequestHandler<GetOrderQuery, OrderDto?> { }""",
            key_points=["CQRS mediator", "Thin controllers", "Pipeline behaviors"],
        ),
        InterviewItem(
            "model-binders",
            "How do custom model binders work in ASP.NET Core?",
            "See detailed explanation.",
            """[ModelBinder(BinderType = typeof(DateOnlyModelBinder))]
public DateOnly ShipDate { get; init; }""",
            key_points=["IModelBinder", "Complex binding", "[ModelBinder] attribute"],
        ),
        InterviewItem(
            "claims-based-auth",
            "How does claims-based authentication work in ASP.NET Core?",
            "See detailed explanation.",
            """var identity = new ClaimsIdentity(claims, "Bearer");
var principal = new ClaimsPrincipal(identity);""",
            key_points=["ClaimsIdentity/Principal", "Map inbound claims", "User.FindFirst"],
        ),
        InterviewItem(
            "refresh-tokens",
            "How do you implement refresh tokens in ASP.NET Core?",
            "See detailed explanation.",
            """// Short-lived access JWT + opaque refresh token stored server-side
app.MapPost("/auth/refresh", RefreshTokenHandler);""",
            key_points=["Rotate refresh tokens", "HttpOnly cookie storage", "Revocation store"],
        ),
    ],
    ("aspnet", "advanced"): [
        InterviewItem(
            "middleware-order",
            "What is the correct ASP.NET Core middleware order?",
            "See detailed explanation.",
            """app.UseExceptionHandler();
app.UseHttpsRedirection();
app.UseRouting();
app.UseAuthentication();
app.UseAuthorization();""",
            key_points=["Exception handling first", "Auth before endpoints", "CORS early if needed"],
        ),
        InterviewItem(
            "hsts-aspnet",
            "How do you enable HSTS in ASP.NET Core?",
            "See detailed explanation.",
            """if (!app.Environment.IsDevelopment())
    app.UseHsts();""",
            key_points=["Strict-Transport-Security", "Production only", "IncludeSubDomains"],
        ),
        InterviewItem(
            "kestrel-config",
            "How do you configure Kestrel limits and endpoints?",
            "See detailed explanation.",
            """builder.WebHost.ConfigureKestrel(o =>
{
    o.Limits.MaxRequestBodySize = 10 * 1024 * 1024;
});""",
            key_points=["Limits and timeouts", "Listen options", "HTTP/2 and TLS"],
        ),
        InterviewItem(
            "iis-integration",
            "How does ASP.NET Core run behind IIS?",
            "See detailed explanation.",
            """builder.WebHost.UseIISIntegration();""",
            key_points=["ASP.NET Core Module", "In-process vs out-of-process", "web.config"],
        ),
        InterviewItem(
            "resource-authorization",
            "How do you implement resource-based authorization?",
            "See detailed explanation.",
            """await _authService.AuthorizeAsync(User, order, "CanEditOrder");""",
            key_points=["IAuthorizationService", "Resource handlers", "Owner-only access"],
        ),
        InterviewItem(
            "razor-pages-vs-api",
            "When choose Razor Pages vs Web API controllers?",
            "See detailed explanation.",
            """// Razor Pages — server-rendered HTML
// Web API — JSON for SPA/mobile clients""",
            key_points=["Razor = server UI", "API = JSON clients", "Can coexist in one app"],
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "iactionresult-types": {
        "explanation": (
            "ASP.NET Core controllers return **`IActionResult`** or **`ActionResult<T>`** — typed wrappers that translate to HTTP status codes and bodies. "
            "Common helpers: **`Ok()`** (200), **`CreatedAtAction()`** (201 with Location), **`NoContent()`** (204), **`BadRequest()`** (400), **`NotFound()`** (404), **`Unauthorized()`** (401). "
            "**Minimal APIs** use static **`Results`** (`Results.Ok`, `Results.Problem`) and **`TypedResults`** for OpenAPI-friendly response types. "
            "`ActionResult<T>` lets you return the type directly or an error result — useful for consistent swagger schemas. "
            "Use **`ProblemDetails`** (RFC 7807) for machine-readable errors instead of ad-hoc JSON shapes. "
            "**Interview tip:** returning raw objects without `IActionResult` still works but limits control over status codes and headers."
        ),
        "code": """[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase
{
    [HttpGet("{id}")]
    public ActionResult<OrderDto> Get(int id)
    {
        var order = _repo.Find(id);
        if (order is null) return NotFound();      // 404
        return Ok(order);                           // 200 + body
    }

    [HttpPost]
    public ActionResult<OrderDto> Create(CreateOrderDto dto)
    {
        var created = _repo.Add(dto);
        return CreatedAtAction(nameof(Get), new { id = created.Id }, created); // 201
    }

    [HttpDelete("{id}")]
    public IActionResult Delete(int id)
    {
        if (!_repo.Delete(id)) return NotFound();
        return NoContent();                         // 204
    }
}

// Minimal API equivalent
app.MapGet("/orders/{id}", (int id) =>
    repo.Find(id) is { } o ? Results.Ok(o) : Results.NotFound());""",
        "language": "csharp",
        "key_points": [
            "IActionResult maps to HTTP response",
            "CreatedAtAction for 201 with Location header",
            "ActionResult<T> for typed OpenAPI schemas",
            "Results/TypedResults in minimal APIs",
            "ProblemDetails for standardized errors",
        ],
    },
    "httpclient-factory": {
        "explanation": (
            "Creating `new HttpClient()` repeatedly causes **socket exhaustion** — disposed clients leave connections in **TIME_WAIT**. "
            "**`IHttpClientFactory`** manages **`HttpMessageHandler`** lifetimes (typically 2 minutes) while allowing short-lived `HttpClient` instances. "
            "Register **typed clients** (`AddHttpClient<IApi, ApiImpl>`) or **named clients** for different downstream services with distinct policies. "
            "Integrates with **Polly** resilience handlers — retry, circuit breaker, timeout — via `AddStandardResilienceHandler()`. "
            "Configure default headers, base address, and timeouts per client in DI registration. "
            "**Interview tip:** inject `HttpClient` only via typed client constructor — never `new HttpClient()` in services."
        ),
        "code": """// Program.cs — typed client with base address
builder.Services.AddHttpClient<IWeatherClient, WeatherClient>(client =>
{
    client.BaseAddress = new Uri("https://api.weather.example/");
    client.Timeout = TimeSpan.FromSeconds(30);
})
.AddStandardResilienceHandler(); // .NET 8+ Polly integration

// Implementation — HttpClient injected by factory
public class WeatherClient(HttpClient http, ILogger<WeatherClient> log) : IWeatherClient
{
    public async Task<Forecast?> GetAsync(string city, CancellationToken ct)
    {
        var response = await http.GetAsync($"forecast?city={city}", ct);
        response.EnsureSuccessStatusCode();
        return await response.Content.ReadFromJsonAsync<Forecast>(ct);
    }
}

// Named client for multiple APIs
builder.Services.AddHttpClient("payments", c =>
    c.BaseAddress = new Uri(builder.Configuration["Payments:BaseUrl"]!));""",
        "language": "csharp",
        "key_points": [
            "Avoid new HttpClient() — socket exhaustion",
            "Factory manages handler lifetime and DNS",
            "Typed clients pair interface with HttpClient DI",
            "AddStandardResilienceHandler for Polly policies",
            "Named clients for multiple downstream APIs",
        ],
    },
    "static-files": {
        "explanation": (
            "**Static files middleware** serves files from **`wwwroot`** (default) or custom `IFileProvider` paths — CSS, JS, images, SPA `index.html`. "
            "Call **`UseDefaultFiles()`** before **`UseStaticFiles()`** to serve `index.html` for directory requests. "
            "Middleware order matters — static files usually run **before** routing/auth for performance (no MVC pipeline for assets). "
            "**.NET 9+** introduces **`MapStaticAssets()`** for fingerprinted assets in Blazor and optimized caching headers. "
            "For SPAs, `UseSpaStaticFiles` or reverse proxy (nginx/CDN) often serves the frontend in production. "
            "**Security:** static files bypass authorization by default — never place secrets in `wwwroot`."
        ),
        "code": """var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Serve index.html, default.htm, etc. for /
app.UseDefaultFiles();

// Serve files from wwwroot (ContentRoot/wwwroot)
app.UseStaticFiles();

// Custom provider — e.g., uploaded files (validate paths!)
app.UseStaticFiles(new StaticFileOptions
{
    FileProvider = new PhysicalFileProvider(
        Path.Combine(builder.Environment.ContentRootPath, "uploads")),
    RequestPath = "/uploads"
});

app.UseRouting();
app.MapControllers();

// Production SPA fallback (optional)
app.MapFallbackToFile("index.html");""",
        "language": "csharp",
        "key_points": [
            "UseStaticFiles serves wwwroot by default",
            "UseDefaultFiles before UseStaticFiles for index",
            "Place before auth for public assets",
            "Never store secrets in wwwroot",
            "CDN/reverse proxy common in production",
        ],
    },
    "data-protection": {
        "explanation": (
            "The **Data Protection API** (`Microsoft.AspNetCore.DataProtection`) provides **cryptographic APIs** for encrypting/decrypting short-lived payloads — auth cookies, anti-forgery tokens, OAuth state. "
            "Keys are stored in a **key ring** — by default ephemeral (dev only); production must **persist** keys (file share, Azure Blob, Redis, registry). "
            "All servers in a **web farm** must share the same key ring or cookies encrypted on one node fail on another. "
            "`IDataProtector` with purpose strings (`CreateProtector('Orders.V1')`) isolates cryptographic contexts. "
            "**Interview tip:** Data Protection is not a general secrets vault — use **Key Vault** for connection strings and API keys. "
            "Set `applicationName` consistently across instances so keys are compatible."
        ),
        "code": """builder.Services.AddDataProtection()
    .SetApplicationName("OrderPortal") // same across all instances
    .PersistKeysToAzureBlobStorage(blobConnection, "keys", "keyring.xml")
    .ProtectKeysWithAzureKeyVault(new Uri(keyVaultKeyId), new DefaultAzureCredential());

// Use protector in a service
public class TicketService(IDataProtectionProvider provider)
{
    private readonly IDataProtector _protector =
        provider.CreateProtector("OrderPortal.Tickets.V1");

    public string Protect(string plain) => _protector.Protect(plain);
    public string Unprotect(string cipher) => _protector.Unprotect(cipher);
}

// Built-in consumers: cookie auth, antiforgery, OAuth correlation""",
        "language": "csharp",
        "key_points": [
            "Encrypts cookies, tokens, and antiforgery data",
            "Key ring must persist in production",
            "Shared key ring required for web farms",
            "IDataProtector with purpose strings",
            "Not a substitute for Key Vault secrets",
        ],
    },
    "forwarded-headers": {
        "explanation": (
            "Behind **reverse proxies** (nginx, Azure Front Door, ALB), Kestrel sees the proxy's IP — not the client. "
            "**Forwarded Headers Middleware** reads `X-Forwarded-For`, `X-Forwarded-Proto`, and `X-Forwarded-Host` to restore the original client IP and scheme. "
            "Must run **early** in the pipeline — before `UseHttpsRedirection` and rate limiting — or redirects and logs use wrong values. "
            "Configure **KnownProxies** / **KnownNetworks** to prevent clients from spoofing forwarded headers. "
            "Without correct `X-Forwarded-Proto`, apps generate **http** links behind TLS-terminated proxies. "
            "**Interview tip:** in Azure App Service, forwarded headers are often pre-configured; self-hosted Kestrel behind nginx requires explicit setup."
        ),
        "code": """builder.Services.Configure<ForwardedHeadersOptions>(options =>
{
    options.ForwardedHeaders =
        ForwardedHeaders.XForwardedFor |
        ForwardedHeaders.XForwardedProto |
        ForwardedHeaders.XForwardedHost;

    // Trust only your reverse proxy IPs
    options.KnownProxies.Add(IPAddress.Parse("10.0.0.100"));
    // Or KnownNetworks for CIDR ranges
});

var app = builder.Build();

// FIRST — before UseHttpsRedirection, auth, logging
app.UseForwardedHeaders();

if (!app.Environment.IsDevelopment())
{
    app.UseHttpsRedirection(); // now respects X-Forwarded-Proto
}

app.UseRouting();
app.UseAuthentication();
app.UseAuthorization();""",
        "language": "csharp",
        "key_points": [
            "Restores client IP and HTTPS scheme behind proxy",
            "UseForwardedHeaders early in pipeline",
            "Configure KnownProxies to prevent spoofing",
            "Required for correct HTTPS redirects",
            "X-Forwarded-For, Proto, Host headers",
        ],
    },
    "api-conventions": {
        "explanation": (
            "ASP.NET Core **API conventions** standardize REST controller behavior via **`[ApiController]`** and **`[Route]`** attributes. "
            "`[ApiController]` enables **automatic 400** responses when model validation fails — no manual `ModelState.IsValid` checks. "
            "It infers binding sources: complex types from body, simple types from route/query by parameter name matching route tokens. "
            "**Problem details** integration returns consistent error shapes for client consumption. "
            "Apply **`[ProducesResponseType]`** for OpenAPI documentation of status codes. "
            "**Interview tip:** conventions apply to controllers inheriting `ControllerBase`, not MVC views (`Controller` with views)."
        ),
        "code": """[ApiController]                    // enables API behaviors
[Route("api/[controller]")]          // api/orders
[Produces("application/json")]
public class OrdersController : ControllerBase
{
    // [ApiController] binds complex type from body automatically
    [HttpPost]
    [ProducesResponseType(typeof(OrderDto), StatusCodes.Status201Created)]
    [ProducesResponseType(typeof(ValidationProblemDetails), StatusCodes.Status400BadRequest)]
    public ActionResult<OrderDto> Create(CreateOrderDto dto)
    {
        // No if (!ModelState.IsValid) — automatic 400
        var order = _service.Create(dto);
        return CreatedAtAction(nameof(Get), new { id = order.Id }, order);
    }

    // Simple type id matches route token {id}
    [HttpGet("{id}")]
    public ActionResult<OrderDto> Get(int id) => /* ... */;
}""",
        "language": "csharp",
        "key_points": [
            "[ApiController] enables automatic 400 on validation",
            "Infers [FromBody] and route binding sources",
            "Route template api/[controller] convention",
            "ProducesResponseType for OpenAPI docs",
            "Applies to ControllerBase, not view controllers",
        ],
    },
    "api-controller-attributes": {
        "explanation": (
            "**Binding source attributes** tell the model binder where to read values: **`[FromBody]`** (JSON body), **`[FromQuery]`** (query string), **`[FromRoute]`** (URL segment), **`[FromHeader]`**, **`[FromForm]`** (multipart). "
            "`[FromServices]` injects a service directly into an action parameter — alternative to constructor injection for one-off dependencies. "
            "HTTP verb attributes (`[HttpGet]`, `[HttpPost]`, `[HttpPut]`, `[HttpPatch]`, `[HttpDelete]`) map actions to routes. "
            "`[Authorize]` and `[AllowAnonymous]` control authentication requirements per action. "
            "With `[ApiController]`, many bindings are **inferred** — explicit attributes override inference for ambiguous cases. "
            "**Interview tip:** `[AsParameters]` in minimal APIs binds multiple parameters from query/route in one DTO."
        ),
        "code": """[HttpGet("search")]
public IActionResult Search(
    [FromQuery] string q,                    // ?q=term
    [FromQuery] int page = 1,
    [FromHeader(Name = "X-Tenant-Id")] Guid tenantId)
{
    return Ok(_svc.Search(tenantId, q, page));
}

[HttpPost]
public IActionResult Create(
    [FromBody] CreateOrderDto dto,           // JSON body
    [FromServices] IAuditService audit)      // DI into parameter
{
    audit.Log("create", dto);
    return Ok();
}

[HttpPut("{id}")]
public IActionResult Update(
    [FromRoute] int id,                      // route segment
    [FromBody] UpdateOrderDto dto) => Ok();

// Override inference when needed
[HttpPost("upload")]
public IActionResult Upload([FromForm] IFormFile file) => Ok();""",
        "language": "csharp",
        "key_points": [
            "FromBody/Query/Route/Header/Form binding sources",
            "FromServices injects DI into action parameters",
            "Http* attributes define routes and verbs",
            "Authorize/AllowAnonymous per action",
            "ApiController infers sources — override when needed",
        ],
    },
    "fluentvalidation": {
        "explanation": (
            "**FluentValidation** defines validation rules in separate **`AbstractValidator<T>`** classes — keeping DTOs free of data annotation clutter. "
            "Register with **`AddValidatorsFromAssemblyContaining<>()`** and enable automatic validation via **`AddFluentValidationAutoValidation()`**. "
            "Rules are expressive: `RuleFor(x => x.Email).EmailAddress().NotEmpty()`, `Must()`, `When()`, async rules with `MustAsync`. "
            "Validation failures integrate with **`ValidationProblemDetails`** — same 400 shape as data annotations. "
            "Prefer FluentValidation for **complex cross-field rules** and reusable rule sets. "
            "**Interview tip:** validate at the **application boundary** (API input) — never trust client-side validation alone."
        ),
        "code": """public class CreateOrderValidator : AbstractValidator<CreateOrderDto>
{
    public CreateOrderValidator()
    {
        RuleFor(x => x.CustomerName)
            .NotEmpty().MaximumLength(100);

        RuleFor(x => x.Quantity)
            .GreaterThan(0).LessThanOrEqualTo(1000);

        RuleFor(x => x.ShipDate)
            .GreaterThan(DateOnly.FromDateTime(DateTime.UtcNow))
            .When(x => x.ExpressShipping);
    }
}

// Program.cs
builder.Services.AddValidatorsFromAssemblyContaining<CreateOrderValidator>();
builder.Services.AddFluentValidationAutoValidation();

// Invalid POST → automatic 400 with field errors
// { "errors": { "Quantity": ["'Quantity' must be greater than '0'."] } }""",
        "language": "csharp",
        "key_points": [
            "Validators in separate AbstractValidator classes",
            "AddFluentValidationAutoValidation for 400 responses",
            "Expressive RuleFor/Must/When syntax",
            "Async validation with MustAsync",
            "Keeps DTOs clean of validation attributes",
        ],
    },
    "serilog-aspnet": {
        "explanation": (
            "**Serilog** is a popular structured logging sink for ASP.NET Core — replaces default providers with rich **JSON/console** output and dozens of **sinks** (Seq, Elasticsearch, Application Insights). "
            "Configure early in **`Program.cs`** with `UseSerilog()` on the host — captures startup failures default logging misses. "
            "**`UseSerilogRequestLogging()`** logs HTTP method, path, status, and duration with one middleware line. "
            "Use **message templates** (`Log.Information('Order {OrderId} placed', id)`) — not interpolation — for searchable structured properties. "
            "Enrich with **`FromLogContext`**, machine name, correlation IDs from `Activity`. "
            "**Interview tip:** redact PII and secrets in production sinks; configure log levels per namespace in `appsettings`."
        ),
        "code": """// Program.cs — bootstrap Serilog before host
Log.Logger = new LoggerConfiguration()
    .ReadFrom.Configuration(builder.Configuration)
    .Enrich.FromLogContext()
    .Enrich.WithProperty("Application", "OrderApi")
    .WriteTo.Console(new JsonFormatter())
    .WriteTo.Seq("http://localhost:5341")
    .CreateLogger();

builder.Host.UseSerilog();

var app = builder.Build();

// One-line HTTP request logging
app.UseSerilogRequestLogging(options =>
{
    options.EnrichDiagnosticContext = (ctx, http) =>
    {
        ctx.Set("User", http.User.Identity?.Name ?? "anonymous");
    };
});

// In services — same ILogger<T> abstraction
public class OrderService(ILogger<OrderService> log)
{
    public void Place(int id) =>
        log.LogInformation("Order {OrderId} placed", id); // structured
}""",
        "language": "csharp",
        "key_points": [
            "UseSerilog on host for startup + request logs",
            "Structured message templates, not interpolation",
            "Sinks: Console, Seq, Elasticsearch, App Insights",
            "UseSerilogRequestLogging middleware",
            "Redact secrets and PII in production",
        ],
    },
    "polly-resilience": {
        "explanation": (
            "**Polly** implements resilience patterns — **retry**, **circuit breaker**, **timeout**, **hedging** — for transient HTTP and service failures. "
            ".NET 8+ ships **`Microsoft.Extensions.Http.Resilience`** with **`AddStandardResilienceHandler()`** — opinionated defaults for HttpClient. "
            "Retry handles transient 5xx/408; circuit breaker **opens** after consecutive failures to let downstream recover. "
            "Combine with **`IHttpClientFactory`** so policies attach per named/typed client. "
            "Configure attempt counts, backoff, and which status codes trigger retry in `appsettings.json`. "
            "**Interview tip:** retry **idempotent** operations only — POST retries may duplicate side effects without idempotency keys."
        ),
        "code": """builder.Services.AddHttpClient<IPaymentClient, PaymentClient>(client =>
{
    client.BaseAddress = new Uri(builder.Configuration["Payments:Url"]!);
})
.AddStandardResilienceHandler(options =>
{
    // Customize defaults
    options.Retry.MaxRetryAttempts = 3;
    options.CircuitBreaker.SamplingDuration = TimeSpan.FromSeconds(30);
    options.TotalRequestTimeout.Timeout = TimeSpan.FromSeconds(10);
});

// Or manual Polly v8 pipeline
builder.Services.AddHttpClient<IApi, Api>()
    .AddResilienceHandler("api-pipeline", builder =>
    {
        builder.AddRetry(new HttpRetryStrategyOptions
        {
            MaxRetryAttempts = 3,
            BackoffType = DelayBackoffType.Exponential
        });
        builder.AddCircuitBreaker(new HttpCircuitBreakerStrategyOptions());
    });

// Idempotent GET — safe to retry; POST needs idempotency key""",
        "language": "csharp",
        "key_points": [
            "AddStandardResilienceHandler for HttpClient defaults",
            "Retry, circuit breaker, timeout patterns",
            "Integrates with IHttpClientFactory",
            "Only retry idempotent operations safely",
            "Configure via appsettings or code",
        ],
    },
    "mediatr-aspnet": {
        "explanation": (
            "**MediatR** implements the **mediator pattern** — controllers send **commands/queries** to handlers, keeping endpoints thin and logic testable. "
            "A command (`IRequest<T>`) mutates state; a query reads — classic **CQRS** separation without mandatory Event Sourcing. "
            "Register with **`AddMediatR(cfg => cfg.RegisterServicesFromAssembly(...))`** and inject **`IMediator`** into controllers or minimal API delegates. "
            "**Pipeline behaviors** wrap handlers for cross-cutting concerns — validation, logging, transactions, caching. "
            "Pairs well with **FluentValidation** via `ValidationBehavior<TRequest,TResponse>`. "
            "**Interview tip:** MediatR adds indirection — justify it for complex domains, not trivial CRUD."
        ),
        "code": """// Query + handler
public record GetOrderQuery(int Id) : IRequest<OrderDto?>;

public class GetOrderHandler(IOrderRepository repo)
    : IRequestHandler<GetOrderQuery, OrderDto?>
{
    public async Task<OrderDto?> Handle(GetOrderQuery q, CancellationToken ct) =>
        await repo.GetDtoAsync(q.Id, ct);
}

// Command
public record PlaceOrderCommand(CreateOrderDto Dto) : IRequest<int>;

// Program.cs
builder.Services.AddMediatR(cfg =>
    cfg.RegisterServicesFromAssembly(typeof(GetOrderHandler).Assembly));

// Controller — one line
[HttpGet("{id}")]
public async Task<ActionResult<OrderDto>> Get(int id, IMediator mediator)
{
    var result = await mediator.Send(new GetOrderQuery(id));
    return result is null ? NotFound() : Ok(result);
}""",
        "language": "csharp",
        "key_points": [
            "IMediator dispatches IRequest to handlers",
            "CQRS-style commands and queries",
            "Pipeline behaviors for cross-cutting logic",
            "Thin controllers — logic in handlers",
            "Justify for complex domains, not trivial CRUD",
        ],
    },
    "model-binders": {
        "explanation": (
            "**Model binders** convert HTTP request data into action parameters — built-in binders handle primitives, collections, and complex types from JSON/form. "
            "Implement **`IModelBinder`** (or **`IModelBinderProvider`**) for custom types — `DateOnly`, encrypted IDs, composite keys. "
            "Apply with **`[ModelBinder(BinderType = typeof(MyBinder))]`** on parameters or properties. "
            "Binding runs **before** validation — failed binding may skip FluentValidation unless configured. "
            "**FromBody** uses **`BodyModelBinder`** + System.Text.Json; form files use **`IFormFile`** binder. "
            "**Interview tip:** prefer type converters or `JsonConverter` for JSON-only custom types; model binders when multiple sources (route + query) combine."
        ),
        "code": """// Custom binder for DateOnly from query string
public class DateOnlyModelBinder : IModelBinder
{
    public Task BindModelAsync(ModelBindingContext bindingContext)
    {
        var value = bindingContext.ValueProvider
            .GetValue(bindingContext.ModelName).FirstValue;

        if (DateOnly.TryParse(value, out var date))
        {
            bindingContext.Result = ModelBindingResult.Success(date);
            return Task.CompletedTask;
        }

        bindingContext.ModelState.TryAddModelError(
            bindingContext.ModelName, "Invalid date format.");
        bindingContext.Result = ModelBindingResult.Failed();
        return Task.CompletedTask;
    }
}

// Usage on DTO property
public class SearchDto
{
    [ModelBinder(BinderType = typeof(DateOnlyModelBinder))]
    public DateOnly FromDate { get; init; }
}""",
        "language": "csharp",
        "key_points": [
            "IModelBinder converts request data to parameters",
            "ModelBinderProvider selects binders by type",
            "Custom binders for non-standard formats",
            "Binding runs before validation",
            "JsonConverter alternative for JSON-only types",
        ],
    },
    "claims-based-auth": {
        "explanation": (
            "**Claims-based identity** represents the user as a **`ClaimsPrincipal`** — a collection of **`Claim`** objects (type + value pairs) like `sub`, `email`, `role`. "
            "JWT bearer tokens, cookie auth, and OpenID Connect all populate `HttpContext.User` with claims after authentication middleware runs. "
            "Read claims via **`User.FindFirst(ClaimTypes.NameIdentifier)`** or **`User.IsInRole('Admin')`** — roles are claims with type `role`. "
            "Map inbound JWT claim names with **`TokenValidationParameters`** / **`MapInboundClaims`** when issuers use short names (`sub` vs `NameIdentifier`). "
            "Authorization policies can **`RequireClaim`** or use custom **`IAuthorizationHandler`** for claim-based rules. "
            "**Interview tip:** prefer **policy-based** auth over hard-coded role strings scattered in controllers."
        ),
        "code": """// JWT populates HttpContext.User after UseAuthentication
[Authorize]
[HttpGet("me")]
public IActionResult Me()
{
    var userId = User.FindFirstValue(ClaimTypes.NameIdentifier)
        ?? User.FindFirstValue("sub");
    var email = User.FindFirstValue(ClaimTypes.Email);
    var isAdmin = User.IsInRole("Admin");

    return Ok(new { userId, email, isAdmin });
}

// Policy requiring specific claim
builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("CanViewReports", policy =>
        policy.RequireClaim("permission", "reports:read"));
});

[Authorize(Policy = "CanViewReports")]
[HttpGet("reports")]
public IActionResult Reports() => Ok();

// Manual principal (rare — tests or custom auth)
var identity = new ClaimsIdentity(new[]
{
    new Claim(ClaimTypes.Name, "alice"),
    new Claim(ClaimTypes.Role, "Admin")
}, authenticationType: "Bearer");""",
        "language": "csharp",
        "key_points": [
            "ClaimsPrincipal holds Claim type-value pairs",
            "JWT/cookie/OIDC populate HttpContext.User",
            "FindFirst and IsInRole for authorization checks",
            "Map inbound claims for JWT short names",
            "Prefer policies over scattered role checks",
        ],
    },
    "refresh-tokens": {
        "explanation": (
            "**Access tokens** (JWT) should be **short-lived** (5–15 minutes) to limit exposure; **refresh tokens** obtain new access tokens without re-login. "
            "Store refresh tokens **server-side** (database/Redis) with user ID, expiry, and rotation metadata — or in **HttpOnly Secure cookies** for SPAs. "
            "Implement **rotation**: each refresh invalidates the old token and issues a new pair — detects theft if old token reused. "
            "Endpoint `POST /auth/refresh` validates refresh token, checks revocation, returns new access (+ optional new refresh). "
            "Never store refresh tokens in **localStorage** — XSS can steal them; HttpOnly cookies mitigate. "
            "**Interview tip:** combine with **refresh token families** to revoke all sessions on compromise detection."
        ),
        "code": """// Issue tokens on login
public async Task<TokenPair> LoginAsync(string email, string password)
{
    var user = await ValidateUserAsync(email, password);
    var access = _jwt.CreateAccessToken(user, TimeSpan.FromMinutes(15));
    var refresh = _tokens.CreateRefreshToken(user.Id, TimeSpan.FromDays(7));
    await _db.SaveRefreshTokenAsync(refresh);
    return new TokenPair(access, refresh.Token);
}

// Refresh endpoint
app.MapPost("/auth/refresh", async (RefreshRequest req, ITokenService tokens) =>
{
    var stored = await tokens.ValidateRefreshTokenAsync(req.RefreshToken);
    if (stored is null) return Results.Unauthorized();

    await tokens.RevokeAsync(req.RefreshToken); // rotation
    var newPair = await tokens.IssueNewPairAsync(stored.UserId);
    return Results.Ok(newPair);
});

// SPA: refresh token in HttpOnly cookie; access token in memory""",
        "language": "csharp",
        "key_points": [
            "Short-lived access JWT + long-lived refresh token",
            "Store refresh tokens server-side with revocation",
            "Rotate refresh tokens on each use",
            "HttpOnly Secure cookies for browser clients",
            "Revoke token family on reuse detection",
        ],
    },
    "middleware-order": {
        "explanation": (
            "ASP.NET Core middleware forms a **pipeline** — order determines which components see the request first and whether later middleware runs at all. "
            "Recommended order: **Exception handling** → **HTTPS redirection** → **Static files** → **Routing** → **CORS** → **Authentication** → **Authorization** → **Endpoints**. "
            "`UseAuthentication` must precede **`UseAuthorization`** — authorization needs an authenticated `HttpContext.User`. "
            "**CORS** must run before endpoints execute but after routing in some setups; misplaced CORS causes confusing browser errors. "
            "**Forwarded headers** run before HTTPS redirection behind proxies. "
            "**Interview tip:** terminal middleware (that doesn't call `next`) short-circuits the pipeline — e.g., auth challenge responses."
        ),
        "code": """var app = builder.Build();

// 1. Exception handling — outermost catch
app.UseExceptionHandler("/error");
if (!app.Environment.IsDevelopment())
    app.UseHsts();

// 2. Forwarded headers (behind proxy) — very early
app.UseForwardedHeaders();

// 3. HTTPS + static files
app.UseHttpsRedirection();
app.UseStaticFiles();

// 4. Routing must precede auth
app.UseRouting();

// 5. CORS — after routing, before auth/endpoints
app.UseCors("SpaPolicy");

// 6. Auth — authentication BEFORE authorization
app.UseAuthentication();
app.UseAuthorization();

// 7. Custom middleware — usually after auth
app.UseMiddleware<RequestTimingMiddleware>();

// 8. Endpoints
app.MapControllers();
app.MapHealthChecks("/health");""",
        "language": "csharp",
        "key_points": [
            "Exception handling outermost in pipeline",
            "UseRouting before UseAuthentication",
            "Authentication before Authorization",
            "CORS placement critical for browser clients",
            "Forwarded headers before HTTPS redirection",
        ],
    },
    "hsts-aspnet": {
        "explanation": (
            "**HTTP Strict Transport Security (HSTS)** tells browsers to **only** access the site over HTTPS for a configured period — preventing SSL-stripping attacks. "
            "Enable with **`UseHsts()`** — typically **production only** (HSTS in dev breaks local HTTP testing). "
            "The middleware adds header `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`. "
            "Configure options via **`services.AddHsts()`** — `MaxAge`, `IncludeSubDomains`, `Preload` (submit to browser preload lists). "
            "HSTS complements **`UseHttpsRedirection()`** — redirection handles first visit; HSTS enforces on subsequent visits. "
            "**Interview tip:** ensure HTTPS works fully before enabling long `max-age` — mistakes are hard to undo until expiry."
        ),
        "code": """builder.Services.AddHsts(options =>
{
    options.MaxAge = TimeSpan.FromDays(365);
    options.IncludeSubDomains = true;
    options.Preload = true; // only if entire zone supports HTTPS
});

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseDeveloperExceptionPage();
}
else
{
    app.UseHsts();              // Strict-Transport-Security header
    app.UseHttpsRedirection();  // redirect HTTP → HTTPS
}

// Response header example:
// Strict-Transport-Security: max-age=31536000; includeSubDomains; preload""",
        "language": "csharp",
        "key_points": [
            "UseHsts adds Strict-Transport-Security header",
            "Enable in production, not development",
            "max-age enforces HTTPS for duration",
            "IncludeSubDomains covers subdomains",
            "Pair with UseHttpsRedirection",
        ],
    },
    "kestrel-config": {
        "explanation": (
            "**Kestrel** is the cross-platform web server at the heart of ASP.NET Core — handles HTTP/1.1, HTTP/2, and HTTP/3 (where supported). "
            "Configure via **`ConfigureKestrel`** — set **`Limits`** (`MaxRequestBodySize`, `KeepAliveTimeout`, `MaxConcurrentConnections`) to prevent abuse. "
            "**`Listen`** / **`ListenAnyIP`** bind endpoints with optional HTTPS certificate configuration. "
            "Behind **IIS** or nginx, Kestrel often listens on loopback — reverse proxy terminates public TLS. "
            "Tune **`MinRequestBodyDataRate`** to detect slowloris-style attacks. "
            "**Interview tip:** `MaxRequestBodySize` defaults to ~28MB — lower for APIs that never accept large uploads."
        ),
        "code": """builder.WebHost.ConfigureKestrel(options =>
{
    // Request limits
    options.Limits.MaxRequestBodySize = 10 * 1024 * 1024; // 10 MB
    options.Limits.KeepAliveTimeout = TimeSpan.FromMinutes(2);
    options.Limits.MaxConcurrentConnections = 1000;

    // Listen on specific port with TLS
    options.ListenAnyIP(5001, listen =>
    {
        listen.UseHttps("cert.pfx", "password");
        listen.Protocols = HttpProtocols.Http1AndHttp2;
    });

    options.ListenAnyIP(5000); // HTTP (dev or behind proxy)
});

// appsettings.json alternative
// "Kestrel": { "Limits": { "MaxRequestBodySize": 10485760 } }

// IIS in-process — IIS handles public binding, Kestrel in worker process""",
        "language": "csharp",
        "key_points": [
            "Kestrel is default cross-platform server",
            "ConfigureKestrel sets limits and endpoints",
            "MaxRequestBodySize prevents large uploads",
            "Listen/ListenAnyIP for ports and TLS",
            "Often behind IIS/nginx in production",
        ],
    },
    "iis-integration": {
        "explanation": (
            "ASP.NET Core on Windows can host via the **ASP.NET Core Module (ANCM)** inside **IIS** — bridging IIS's Windows auth, central cert management, and existing infra. "
            "**In-process** hosting runs Kestrel inside the IIS worker process (`w3wp.exe`) — lowest latency. "
            "**Out-of-process** runs Kestrel as a separate process; IIS forwards requests via reverse proxy. "
            "`UseIISIntegration()` configures the app for IIS — reads port from **ASP.NETCORE_PORT** env variable set by ANCM. "
            "**`web.config`** points IIS to your app DLL and configures logging stdout for startup failures. "
            "**Interview tip:** Linux containers and Azure App Service Linux skip IIS — use Kestrel + reverse proxy directly."
        ),
        "code": """// Program.cs — IIS integration (Windows hosting)
builder.WebHost.UseIISIntegration();

var app = builder.Build();
app.Run();

// web.config (published output) — ANCM entry point
// <aspNetCore processPath="dotnet"
//             arguments=".\\MyApp.dll"
//             hostingModel="inprocess"
//             stdoutLogEnabled="true" />

// csproj for in-process
// <PropertyGroup>
//   <AspNetCoreHostingModel>InProcess</AspNetCoreHostingModel>
// </PropertyGroup>

// Out-of-process: hostingModel="outofprocess"
// Kestrel listens on loopback; IIS proxies""",
        "language": "csharp",
        "key_points": [
            "ASP.NET Core Module bridges IIS and Kestrel",
            "In-process = Kestrel inside w3wp.exe",
            "Out-of-process = separate Kestrel process",
            "web.config required for IIS deployment",
            "Linux/containers use Kestrel without IIS",
        ],
    },
    "resource-authorization": {
        "explanation": (
            "**Resource-based authorization** checks whether the current user may act on a **specific resource instance** — e.g., edit only their own order. "
            "Role-based auth is insufficient when permissions depend on **ownership**, **tenant**, or **resource state**. "
            "Use **`IAuthorizationService.AuthorizeAsync(user, resource, policyName)`** in controllers or handlers. "
            "Implement **`IAuthorizationHandler`** + **`AuthorizationHandler<TRequirement, TResource>`** for custom logic. "
            "Register policies with **`AddAuthorization`** and **`AddSingleton<IAuthorizationHandler, ...>`**. "
            "**Interview tip:** fail closed — default deny; return **403 Forbidden** (authenticated but not allowed) vs **401 Unauthorized**."
        ),
        "code": """// Requirement + handler
public class OrderOwnerRequirement : IAuthorizationRequirement { }

public class OrderOwnerHandler : AuthorizationHandler<OrderOwnerRequirement, Order>
{
    protected override Task HandleRequirementAsync(
        AuthorizationHandlerContext context,
        OrderOwnerRequirement requirement,
        Order order)
    {
        var userId = context.User.FindFirstValue(ClaimTypes.NameIdentifier);
        if (userId == order.OwnerId || context.User.IsInRole("Admin"))
            context.Succeed(requirement);
        return Task.CompletedTask;
    }
}

// Registration
builder.Services.AddAuthorization(o =>
    o.AddPolicy("OwnOrder", p => p.Requirements.Add(new OrderOwnerRequirement())));
builder.Services.AddSingleton<IAuthorizationHandler, OrderOwnerHandler>();

// Controller check
var auth = await _authService.AuthorizeAsync(User, order, "OwnOrder");
if (!auth.Succeeded) return Forbid();""",
        "language": "csharp",
        "key_points": [
            "AuthorizeAsync checks user against specific resource",
            "IAuthorizationHandler for custom ownership logic",
            "Roles insufficient for per-resource permissions",
            "403 Forbidden vs 401 Unauthorized",
            "Fail closed — deny by default",
        ],
    },
    "razor-pages-vs-api": {
        "explanation": (
            "**Razor Pages** (`PageModel` + `.cshtml`) suit **server-rendered HTML** — forms, admin portals, SEO-friendly content with minimal JavaScript. "
            "**Web API controllers** (or Minimal APIs) return **JSON** for SPAs (Angular/React), mobile apps, and microservice consumers. "
            "Both coexist in one project — Razor for marketing/admin, API for SPA frontend. "
            "Razor uses **model binding + validation** with HTML helpers; APIs use JSON + ProblemDetails. "
            "Choose Razor when **server-side rendering** and simplicity matter; APIs when **multiple clients** share backend logic. "
            "**Interview tip:** Blazor Server/WASM is a third path — component-based UI with .NET instead of Razor Pages or SPA+API split."
        ),
        "code": """// Razor Page — server-rendered HTML
// Pages/Orders/Index.cshtml.cs
public class IndexModel(IOrderService svc) : PageModel
{
    public IList<Order> Orders { get; private set; } = [];
    public async Task OnGetAsync() => Orders = await svc.ListAsync();
}

// Web API — JSON for Angular SPA
[ApiController]
[Route("api/[controller]")]
public class OrdersController(IOrderService svc) : ControllerBase
{
    [HttpGet]
    public async Task<ActionResult<IList<OrderDto>>> List() =>
        Ok(await svc.ListDtosAsync());
}

// Program.cs — both in one app
builder.Services.AddRazorPages();
builder.Services.AddControllers();
app.MapRazorPages();
app.MapControllers();""",
        "language": "csharp",
        "key_points": [
            "Razor Pages = server-rendered HTML UI",
            "Web API = JSON for SPA/mobile clients",
            "Both can coexist in one ASP.NET Core app",
            "Choose based on client architecture",
            "Blazor is alternative component-based UI",
        ],
    },
}
