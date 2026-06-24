"""Additional Best Practices interview topics — expands practices section to 50+."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("practices", "foundation"): [
        InterviewItem(
            "factory-method-pattern",
            "What is the Factory Method pattern?",
            "Defers object creation to subclasses or dedicated factory types.",
            "",
        ),
        InterviewItem(
            "builder-pattern",
            "What is the Builder pattern and when use it?",
            "Constructs complex objects step-by-step with a fluent API.",
            "",
        ),
        InterviewItem(
            "adapter-pattern",
            "Explain the Adapter pattern with a .NET example.",
            "Wraps an incompatible interface so existing code can use it.",
            "",
        ),
        InterviewItem(
            "facade-pattern",
            "What is the Facade pattern?",
            "Provides a simplified interface over a complex subsystem.",
            "",
        ),
        InterviewItem(
            "proxy-pattern",
            "What is the Proxy pattern? Compare to Decorator.",
            "Controls access to another object — lazy load, cache, security.",
            "",
        ),
        InterviewItem(
            "observer-pattern",
            "Explain the Observer pattern in .NET.",
            "One-to-many notification when subject state changes.",
            "",
        ),
        InterviewItem(
            "command-pattern",
            "What is the Command pattern?",
            "Encapsulates a request as an object — undo, queue, MediatR.",
            "",
        ),
        InterviewItem(
            "null-object-pattern",
            "What is the Null Object pattern?",
            "Replace null checks with a do-nothing implementation.",
            "",
        ),
        InterviewItem(
            "chain-of-responsibility-pattern",
            "Explain the Chain of Responsibility pattern.",
            "Pass requests along a chain of handlers until one handles it.",
            "",
        ),
    ],
    ("practices", "intermediate"): [
        InterviewItem(
            "hexagonal-architecture",
            "What is Hexagonal (Ports and Adapters) architecture?",
            "Domain at the center; infrastructure plugs in via ports.",
            "",
        ),
        InterviewItem(
            "clean-architecture",
            "Explain Clean Architecture layers and dependency rule.",
            "Entities → use cases → adapters → frameworks; deps point inward.",
            "",
        ),
        InterviewItem(
            "vertical-slice-architecture",
            "What is Vertical Slice architecture?",
            "Organize by feature/use case instead of technical layers.",
            "",
        ),
        InterviewItem(
            "bff-pattern",
            "What is the Backend for Frontend (BFF) pattern?",
            "Dedicated API per client type — web, mobile, partner.",
            "",
        ),
        InterviewItem(
            "yagni-dry-kiss",
            "Explain YAGNI, DRY, and KISS with practical examples.",
            "Balance simplicity, reuse, and avoiding premature abstraction.",
            "",
        ),
        InterviewItem(
            "law-of-demeter",
            "What is the Law of Demeter (Principle of Least Knowledge)?",
            "Objects should only talk to immediate friends, not strangers.",
            "",
        ),
    ],
    ("practices", "advanced"): [
        InterviewItem(
            "saga-pattern",
            "What is the Saga pattern for distributed transactions?",
            "Sequence of local transactions with compensating actions on failure.",
            "",
        ),
        InterviewItem(
            "outbox-pattern",
            "Explain the Outbox pattern.",
            "Atomically save domain changes and outbound messages in one DB transaction.",
            "",
        ),
        InterviewItem(
            "strangler-fig-pattern",
            "What is the Strangler Fig pattern?",
            "Incrementally replace legacy system by routing traffic to new modules.",
            "",
        ),
        InterviewItem(
            "anti-corruption-layer",
            "What is an Anti-Corruption Layer in DDD?",
            "Translation boundary between bounded contexts or legacy integrations.",
            "",
        ),
    ],
}

for _items in MARKET_ITEMS.values():
    for item in _items:
        if not item.code.strip():
            item.code = "// See detailed code example below"

MARKET_DETAILED: dict[str, dict] = {
    "factory-method-pattern": {
        "explanation": (
            "The **Factory Method** pattern defines an interface for creating objects but lets **subclasses or "
            "registered factories** decide which concrete type to instantiate. It removes `new ConcreteType()` "
            "scattered through business code and supports **Open/Closed** — add new product types without "
            "changing callers. In .NET interviews, contrast with **Simple Factory** (one static method) and "
            "**Abstract Factory** (families of related objects). Use when creation logic varies by context "
            "(payment provider, notification channel) or when you need test doubles."
        ),
        "code": """public interface INotificationSender
{
    Task SendAsync(string to, string message);
}

public interface INotificationSenderFactory
{
    INotificationSender Create(string channel); // "email" | "sms" | "push"
}

public class NotificationSenderFactory(IEnumerable<INotificationSender> senders)
    : INotificationSenderFactory
{
    public INotificationSender Create(string channel) =>
        senders.FirstOrDefault(s => s.Channel == channel)
        ?? throw new NotSupportedException(channel);
}

// Usage — caller depends on factory, not concrete types
await _factory.Create(order.PreferredChannel).SendAsync(order.Email, body);""",
        "language": "csharp",
        "key_points": [
            "Factory Method defers instantiation to specialized creators",
            "Prefer DI + IEnumerable<T> over switch/new in services",
            "Open/Closed: add new sender without editing OrderService",
            "Not the same as Abstract Factory (product families)",
            "Common in plugin architectures and strategy selection",
        ],
    },
    "builder-pattern": {
        "explanation": (
            "The **Builder** pattern constructs a **complex object step-by-step**, separating construction from "
            "representation. Callers use a fluent API (`WithX().WithY().Build()`) instead of telescoping "
            "constructors with many optional parameters. In modern C#, **records with `with`**, **named arguments**, "
            "and **`IConfiguration` binding** often replace hand-rolled builders — but interviewers still expect "
            "you to know when builders shine: many optional fields, immutable results, validation at `Build()`, "
            "and readable test data setup (`OrderBuilder.Default().WithTotal(99m).Build()`)."
        ),
        "code": """public sealed class EmailMessage
{
    public required string To { get; init; }
    public required string Subject { get; init; }
    public string? Body { get; init; }
    public IReadOnlyList<string> Cc { get; init; } = [];
}

public class EmailMessageBuilder
{
    private string? _to, _subject, _body;
    private readonly List<string> _cc = [];

    public EmailMessageBuilder To(string to) { _to = to; return this; }
    public EmailMessageBuilder Subject(string s) { _subject = s; return this; }
    public EmailMessageBuilder Body(string b) { _body = b; return this; }
    public EmailMessageBuilder Cc(string c) { _cc.Add(c); return this; }

    public EmailMessage Build() =>
        new() { To = _to ?? throw new InvalidOperationException("To required"),
                Subject = _subject ?? throw new InvalidOperationException("Subject required"),
                Body = _body, Cc = _cc };
}

// Fluent usage
var msg = new EmailMessageBuilder()
    .To("user@example.com").Subject("Order shipped").Body("Tracking: ABC123").Build();""",
        "language": "csharp",
        "key_points": [
            "Builder separates step-by-step construction from final object",
            "Validate required fields in Build(), not in each With* method",
            "Great for test fixtures and complex DTOs",
            "C# init/named args reduce need for simple cases",
            "Director class optional — orchestrates build steps for variants",
        ],
    },
    "adapter-pattern": {
        "explanation": (
            "The **Adapter** pattern converts the interface of a **legacy or third-party class** into one your "
            "application expects, without modifying the original code. It is essential in **hexagonal architecture** "
            "where domain ports (`IOrderRepository`) are implemented by adapters wrapping EF Core, REST clients, "
            "or SOAP services. Two forms: **class adapter** (inheritance) and **object adapter** (composition — "
            "preferred in .NET). Interview tip: mention **Anti-Corruption Layer** when the external model is "
            "messy and must be translated before entering your domain."
        ),
        "code": """// Legacy SOAP client we cannot change
public class LegacyBillingClient
{
    public LegacyInvoice GetInvoice(string legacyId) => /* ... */;
}

// Port our domain expects
public interface IBillingService
{
    Task<InvoiceDto> GetInvoiceAsync(Guid orderId, CancellationToken ct);
}

// Adapter — translates legacy model + sync → async
public class LegacyBillingAdapter(LegacyBillingClient legacy) : IBillingService
{
    public async Task<InvoiceDto> GetInvoiceAsync(Guid orderId, CancellationToken ct)
    {
        var legacyId = MapOrderIdToLegacy(orderId);
        var inv = await Task.Run(() => legacy.GetInvoice(legacyId), ct);
        return new InvoiceDto(inv.Number, inv.Amount, inv.Currency);
    }
}""",
        "language": "csharp",
        "key_points": [
            "Adapter wraps incompatible API behind your interface",
            "Composition over inheritance in .NET adapters",
            "Core of ports-and-adapters / hexagonal design",
            "Translate external DTOs — don't leak legacy shapes",
            "Enables swapping vendors without domain changes",
        ],
    },
    "facade-pattern": {
        "explanation": (
            "The **Facade** pattern provides a **unified, simplified interface** to a set of interfaces in a "
            "subsystem. It does not add new behavior — it **orchestrates** calls so clients avoid knowing "
            "five services and their order. Common in .NET: `CheckoutFacade` coordinating inventory, payment, "
            "and notification services. Do not confuse with **BFF** (per-client API) or **MediatR** (per use-case "
            "handler). Facade reduces coupling for **internal** modules; keep facades thin and avoid turning "
            "them into god classes."
        ),
        "code": """public class CheckoutFacade(
    IInventoryService inventory,
    IPaymentGateway payment,
    IOrderRepository orders,
    INotificationService notify)
{
    public async Task<CheckoutResult> CheckoutAsync(CheckoutRequest req, CancellationToken ct)
    {
        await inventory.ReserveAsync(req.Sku, req.Qty, ct);
        var charge = await payment.ChargeAsync(req.CardToken, req.Amount, ct);
        var order = await orders.CreateAsync(req, charge.Id, ct);
        await notify.SendOrderConfirmationAsync(order, ct);
        return new CheckoutResult(order.Id, charge.Id);
    }
}

// Controller calls one facade — not four services
[HttpPost("checkout")]
public Task<CheckoutResult> Checkout(CheckoutRequest req)
    => _checkout.CheckoutAsync(req, HttpContext.RequestAborted);""",
        "language": "csharp",
        "key_points": [
            "Facade simplifies access to a complex subsystem",
            "Orchestrates existing services — not a new domain layer",
            "Reduces coupling for callers (controllers, jobs)",
            "Keep thin — delegate to specialized services",
            "Different from BFF (client-specific) and MediatR (CQRS)",
        ],
    },
    "proxy-pattern": {
        "explanation": (
            "A **Proxy** provides a **surrogate or placeholder** that controls access to another object. "
            "Types: **virtual proxy** (lazy loading), **protection proxy** (authorization), **remote proxy** "
            "(RPC/gRPC stub), **caching proxy**. In .NET, **`DispatchProxy`**, **HttpClient** handlers, and "
            "**EF lazy loading proxies** are real-world examples. Contrast with **Decorator**: both wrap objects, "
            "but Proxy controls **access**; Decorator adds **responsibilities** (logging, compression) without "
            "changing when the core object is invoked."
        ),
        "code": """public interface IReportService
{
    Task<Report> GenerateAsync(int id);
}

// Caching proxy — same interface, adds cache behavior
public class CachingReportProxy(IReportService inner, IMemoryCache cache) : IReportService
{
    public async Task<Report> GenerateAsync(int id)
    {
        var key = $"report:{id}";
        if (cache.TryGetValue(key, out Report? cached)) return cached!;
        var report = await inner.GenerateAsync(id);
        cache.Set(key, report, TimeSpan.FromMinutes(10));
        return report;
    }
}

// DI registration
services.AddScoped<ReportService>();
services.AddScoped<IReportService>(sp =>
    new CachingReportProxy(sp.GetRequiredService<ReportService>(), sp.GetRequiredService<IMemoryCache>()));""",
        "language": "csharp",
        "key_points": [
            "Proxy controls access — lazy, cache, security, remote",
            "Same interface as real subject — transparent to caller",
            "Decorator adds behavior; Proxy manages access/lifecycle",
            "HttpClient delegating handlers are proxy-like",
            "Use DI decorators or Scrutor for cross-cutting proxies",
        ],
    },
    "observer-pattern": {
        "explanation": (
            "The **Observer** pattern defines a **one-to-many dependency**: when one object (subject) changes "
            "state, all dependents (observers) are notified. In .NET: **`IObservable<T>` / `IObserver<T>`**, "
            "events (`event EventHandler`), **MediatR notifications**, and **domain events**. Modern apps often "
            "prefer **message buses** (Service Bus, MassTransit) for cross-service observers, but in-process "
            "domain events keep aggregates decoupled. Pitfall: synchronous observers blocking the publisher — "
            "use background dispatch or outbox for side effects."
        ),
        "code": """// Domain event + in-process observer (MediatR notification)
public record OrderPlacedEvent(int OrderId, decimal Total) : INotification;

public class OrderPlacedHandler(IEmailSender email, IAnalytics analytics)
    : INotificationHandler<OrderPlacedEvent>
{
    public async Task Handle(OrderPlacedEvent e, CancellationToken ct)
    {
        await email.SendAsync(/* ... */);
        await analytics.TrackAsync("order_placed", e.OrderId);
    }
}

// Publish after save
await _repo.SaveAsync(order, ct);
await _mediator.Publish(new OrderPlacedEvent(order.Id, order.Total), ct);""",
        "language": "csharp",
        "key_points": [
            "Subject notifies observers on state change",
            "MediatR INotification is Observer in CQRS apps",
            "Domain events decouple side effects from aggregate",
            "Cross-service: use message broker, not in-proc events",
            "Avoid heavy work in synchronous event handlers",
        ],
    },
    "command-pattern": {
        "explanation": (
            "The **Command** pattern encapsulates a **request as an object**, letting you parameterize clients, "
            "queue operations, support undo, and log actions. In .NET enterprise apps, **MediatR `IRequest`** "
            "is the dominant Command pattern implementation — one handler per use case. Benefits: **single "
            "responsibility**, testable handlers, pipeline behaviors (validation, logging, transactions). "
            "Contrast with **Command** in CQRS (write side) vs generic Gang-of-Four command (UI undo/redo)."
        ),
        "code": """public record CancelOrderCommand(int OrderId, string Reason) : IRequest<Result>;

public class CancelOrderHandler(IOrderRepository repo, IUnitOfWork uow)
    : IRequestHandler<CancelOrderCommand, Result>
{
    public async Task<Result> Handle(CancelOrderCommand cmd, CancellationToken ct)
    {
        var order = await repo.GetByIdAsync(cmd.OrderId, ct)
            ?? return Result.NotFound();
        order.Cancel(cmd.Reason);
        await uow.SaveChangesAsync(ct);
        return Result.Ok();
    }
}

// Pipeline behavior — cross-cutting validation
public class ValidationBehavior<TReq, TRes>(IEnumerable<IValidator<TReq>> validators)
    : IPipelineBehavior<TReq, TRes> where TReq : IRequest<TRes> { /* ... */ }""",
        "language": "csharp",
        "key_points": [
            "Command = request object + dedicated handler",
            "MediatR is standard Command pattern in .NET",
            "Pipeline behaviors for validation, logging, UoW",
            "Enables undo/redo in UI; audit log in backends",
            "One handler per use case — not god service methods",
        ],
    },
    "null-object-pattern": {
        "explanation": (
            "The **Null Object** pattern provides a **do-nothing implementation** of an interface instead of "
            "returning `null`, eliminating null checks and **`NullReferenceException`** risk. Example: "
            "`NullLogger`, `NullNotificationSender`, or `EmptyDiscountStrategy` returning 0. Prefer over "
            "nullable returns when **no-op is valid behavior**. In C# 11+, nullable reference types help, but "
            "Null Object still simplifies callers (`logger.Log(...)` always safe). Don't overuse — sometimes "
            "`null` meaning 'not found' is clearer than a null object."
        ),
        "code": """public interface IDiscountStrategy
{
    decimal Apply(Order order);
}

public class TenPercentDiscount : IDiscountStrategy
{
    public decimal Apply(Order order) => order.Subtotal * 0.10m;
}

public class NoDiscount : IDiscountStrategy
{
    public static readonly NoDiscount Instance = new();
    public decimal Apply(Order order) => 0m; // null object — safe default
}

public class OrderPricing(IDiscountStrategy? discount = null)
{
    private readonly IDiscountStrategy _discount = discount ?? NoDiscount.Instance;

    public decimal Total(Order order) => order.Subtotal - _discount.Apply(order);
}

// Caller never checks if discount is null
var total = new OrderPricing().Total(order);""",
        "language": "csharp",
        "key_points": [
            "Null Object implements interface with no-op behavior",
            "Eliminates repetitive null checks in callers",
            "NullLogger / NoDiscount are classic examples",
            "Use when absent behavior is valid, not exceptional",
            "Nullable reference types complement but don't replace pattern",
        ],
    },
    "chain-of-responsibility-pattern": {
        "explanation": (
            "The **Chain of Responsibility** passes a request along a **chain of handlers** until one handles it "
            "or all pass. Each handler decides to process or forward. In ASP.NET Core: **middleware pipeline** "
            "is the canonical example. Also: validation pipelines, authorization checks, and logging enrichment. "
            "Benefits: **decouple sender from receivers**, add/reorder handlers dynamically. Pitfall: debugging "
            "long chains and ensuring every request is handled (fall-through handler at end)."
        ),
        "code": """public interface IOrderValidator
{
    IOrderValidator? Next { get; set; }
    ValidationResult Validate(Order order);
}

public abstract class OrderValidatorBase : IOrderValidator
{
    public IOrderValidator? Next { get; set; }
    public ValidationResult Validate(Order order)
    {
        var result = ValidateCore(order);
        if (!result.IsValid) return result;
        return Next?.Validate(order) ?? ValidationResult.Ok();
    }
    protected abstract ValidationResult ValidateCore(Order order);
}

public class StockValidator : OrderValidatorBase
{
    protected override ValidationResult ValidateCore(Order o) =>
        o.Lines.All(l => l.Qty > 0) ? ValidationResult.Ok() : ValidationResult.Fail("Invalid qty");
}

// Chain: stock → payment → fraud
var chain = new StockValidator { Next = new PaymentValidator { Next = new FraudValidator() } };
var result = chain.Validate(order);""",
        "language": "csharp",
        "key_points": [
            "Request passes through linked handlers until handled",
            "ASP.NET Core middleware is Chain of Responsibility",
            "Add/remove handlers without changing sender",
            "Always terminate chain or handle unhandled case",
            "MediatR pipeline behaviors are a variant",
        ],
    },
    "hexagonal-architecture": {
        "explanation": (
            "**Hexagonal Architecture** (Ports and Adapters, Alistair Cockburn) puts the **domain at the center** "
            "and treats UI, DB, messaging, and external APIs as **pluggable adapters** connected through **ports** "
            "(interfaces). Inbound ports = use cases (`IPlaceOrderUseCase`); outbound ports = repositories, "
            "gateways. The domain has **zero dependencies** on EF, ASP.NET, or Azure SDKs. Interview answer: "
            "draw hexagon with domain inside, adapters outside; explain testability by swapping adapters with fakes."
        ),
        "code": """// Domain — no infrastructure references
public class Order
{
    public void Place() { /* business rules */ }
}

// Port (outbound)
public interface IOrderRepository
{
    Task SaveAsync(Order order, CancellationToken ct);
}

// Adapter (inbound) — ASP.NET controller
[ApiController]
public class OrdersController(PlaceOrderHandler handler) : ControllerBase
{
    [HttpPost]
    public Task<IActionResult> Place(PlaceOrderRequest req)
        => handler.HandleAsync(req);
}

// Adapter (outbound) — EF Core
public class EfOrderRepository(AppDbContext db) : IOrderRepository
{
    public Task SaveAsync(Order order, CancellationToken ct) =>
        db.Orders.AddAsync(Map(order), ct).AsTask();
}""",
        "language": "csharp",
        "key_points": [
            "Domain at center — infrastructure is pluggable",
            "Ports = interfaces; adapters = implementations",
            "Inbound adapters: controllers, consumers, CLI",
            "Outbound adapters: EF, HTTP clients, message bus",
            "Enables testing domain without database or web host",
        ],
    },
    "clean-architecture": {
        "explanation": (
            "**Clean Architecture** (Robert C. Martin) organizes code in **concentric rings**: Entities (enterprise "
            "rules) → Use Cases (application rules) → Interface Adapters → Frameworks/Drivers. The **Dependency "
            "Rule**: source code dependencies only point **inward**. Outer layers know about inner; never the reverse. "
            "In .NET solutions: `Domain` → `Application` → `Infrastructure` → `WebApi`. Compare to hexagonal "
            "(similar intent) and **onion architecture**. Interview: explain why `DbContext` must not leak into "
            "domain entities."
        ),
        "code": """/*
  Clean Architecture layers (.NET solution):

  OrderApp.Domain/          — entities, value objects, domain events
  OrderApp.Application/     — use cases, DTOs, interfaces (IOrderRepo)
  OrderApp.Infrastructure/ — EF, email, Service Bus implementations
  OrderApp.WebApi/          — controllers, DI composition root

  Dependency Rule:
  WebApi → Infrastructure → Application → Domain
  Domain references NOTHING external
*/

// Application use case — depends only on domain + abstractions
public class PlaceOrderUseCase(IOrderRepository repo, IUnitOfWork uow)
{
    public async Task<int> ExecuteAsync(PlaceOrderCommand cmd, CancellationToken ct)
    {
        var order = Order.Create(cmd.CustomerId, cmd.Lines);
        await repo.AddAsync(order, ct);
        await uow.SaveChangesAsync(ct);
        return order.Id;
    }
}""",
        "language": "csharp",
        "key_points": [
            "Dependency Rule — dependencies point inward only",
            "Domain has no EF, HTTP, or framework references",
            "Use cases orchestrate domain + port interfaces",
            "Infrastructure implements ports; WebApi is composition root",
            "Test application layer with in-memory fakes",
        ],
    },
    "vertical-slice-architecture": {
        "explanation": (
            "**Vertical Slice Architecture** (Jimmy Bogard) organizes code by **feature/use case** instead of "
            "horizontal layers (`Controllers/`, `Services/`, `Repositories/`). Each slice contains everything "
            "needed for one capability: `Features/Orders/PlaceOrder/` with request, handler, validator, and "
            "endpoint. Pairs naturally with **MediatR** and **Minimal APIs**. Benefits: high cohesion, less "
            "cross-feature coupling, easier navigation. Tradeoff: shared infrastructure still needed; avoid "
            "duplicating validation across slices."
        ),
        "code": """// Feature folder — one vertical slice
// Features/Orders/CancelOrder/CancelOrderEndpoint.cs
public static class CancelOrderEndpoint
{
    public static void Map(IEndpointRouteBuilder app) =>
        app.MapPost("/orders/{id}/cancel", async (int id, ISender mediator) =>
            await mediator.Send(new CancelOrderCommand(id)));
}

// Features/Orders/CancelOrder/CancelOrderHandler.cs
public record CancelOrderCommand(int OrderId) : IRequest;

public class CancelOrderHandler(AppDbContext db) : IRequestHandler<CancelOrderCommand>
{
    public async Task Handle(CancelOrderCommand cmd, CancellationToken ct)
    {
        var order = await db.Orders.FindAsync([cmd.OrderId], ct)
            ?? throw new NotFoundException();
        order.Status = OrderStatus.Cancelled;
        await db.SaveChangesAsync(ct);
    }
}""",
        "language": "csharp",
        "key_points": [
            "Organize by feature, not technical layer",
            "Each slice: endpoint + handler + validation + tests",
            "MediatR + feature folders is common in .NET",
            "Reduces shotgun surgery across layers",
            "Shared kernel for cross-cutting utilities only",
        ],
    },
    "bff-pattern": {
        "explanation": (
            "**Backend for Frontend (BFF)** is a **dedicated API layer per client type** (web SPA, mobile app, "
            "partner integration) that aggregates and shapes backend microservices for that client's needs. "
            "The web BFF might combine user profile + orders + recommendations in one response; mobile BFF "
            "returns lighter payloads. Implemented with ASP.NET Core BFF project, **YARP reverse proxy**, or "
            "GraphQL gateway. Avoid a single BFF for all clients — it becomes a monolith gateway. Security: BFF "
            "holds session/cookies; microservices use service-to-service tokens."
        ),
        "code": """// Web BFF — aggregates three microservices for dashboard
[ApiController]
[Route("bff/web/dashboard")]
public class WebDashboardBff(
    IUserApi users, IOrderApi orders, IRecommendationApi recs) : ControllerBase
{
    [HttpGet]
    public async Task<DashboardVm> Get(CancellationToken ct)
    {
        var userId = User.GetUserId();
        var userTask = users.GetProfileAsync(userId, ct);
        var ordersTask = orders.GetRecentAsync(userId, 5, ct);
        var recsTask = recs.GetForUserAsync(userId, ct);
        await Task.WhenAll(userTask, ordersTask, recsTask);
        return new DashboardVm(userTask.Result, ordersTask.Result, recsTask.Result);
    }
}

// Mobile BFF — separate project, lighter DTOs, different aggregation""",
        "language": "csharp",
        "key_points": [
            "One BFF per client type — web, mobile, partner",
            "Aggregates microservices; shapes DTOs for UI needs",
            "BFF handles auth session; backends use service tokens",
            "YARP or dedicated ASP.NET Core BFF project",
            "Don't let BFF become shared god API for all clients",
        ],
    },
    "yagni-dry-kiss": {
        "explanation": (
            "**YAGNI** (You Aren't Gonna Need It) — don't build features until required; avoids speculative "
            "abstraction. **DRY** (Don't Repeat Yourself) — single source of truth for knowledge; but "
            "**premature DRY** creates wrong abstractions. **KISS** (Keep It Simple, Stupid) — simplest "
            "solution that works. Together they balance **speed vs maintainability**. Interview story: "
            "refactor duplication when you see the **third** similar case (Rule of Three), not the second. "
            "Violating YAGNI: generic plugin framework for one export format."
        ),
        "code": """// YAGNI violation — over-engineered before need
public interface IExportStrategyFactory { IExportStrategy Create(ExportType t); }
// ... 5 classes for CSV only requirement

// KISS + YAGNI — ship CSV export directly
public class CsvOrderExporter
{
    public byte[] Export(IEnumerable<Order> orders) =>
        Encoding.UTF8.GetBytes(string.Join("\\n",
            orders.Select(o => $"{o.Id},{o.Total}")));
}

// DRY — extract when pattern repeats (third similar exporter)
public static class CsvWriter
{
    public static byte[] WriteRows(IEnumerable<string[]> rows) => /* shared logic */;
}""",
        "language": "csharp",
        "key_points": [
            "YAGNI — implement only what the story requires",
            "DRY — share knowledge, not just duplicated lines",
            "KISS — prefer readable code over clever abstractions",
            "Rule of Three before abstracting duplication",
            "Conscious tradeoffs beat dogmatic application",
        ],
    },
    "law-of-demeter": {
        "explanation": (
            "The **Law of Demeter** (LoD) / **Principle of Least Knowledge**: a method should only call methods on "
            "**itself**, its **parameters**, objects it **creates**, or its **direct components** — not "
            "`order.Customer.Address.ZipCode` through a chain of strangers. Violations create **fragile code** "
            "when intermediate objects change. Fix with **Tell, Don't Ask** and **encapsulation**: "
            "`order.ShipToZipCode()` instead of reaching through customer. In C#, auto-properties and rich "
            "domain models help; anemic DTOs encourage LoD violations."
        ),
        "code": """// LoD violation — train wreck / excessive coupling
var zip = order.Customer.Address.ZipCode; // knows too much about graph

// Better — Tell, Don't Ask; encapsulate in domain
public class Order
{
    public Customer Customer { get; private set; } = null!;
    public string ShipToZipCode() => Customer.ShippingZip(); // delegate to friend
}

public class Customer
{
    public Address ShippingAddress { get; private set; } = null!;
    public string ShippingZip() => ShippingAddress.ZipCode;
}

// Caller
var zip = order.ShipToZipCode();""",
        "language": "csharp",
        "key_points": [
            "Only talk to immediate friends, not object graphs",
            "Avoid train wrecks: a.GetB().GetC().DoThing()",
            "Tell, Don't Ask — behavior on owning object",
            "Reduces ripple when intermediate types change",
            "Rich domain models enforce better boundaries",
        ],
    },
    "saga-pattern": {
        "explanation": (
            "The **Saga** pattern manages **distributed transactions** as a sequence of **local transactions**, "
            "each with a **compensating action** if a later step fails. Two styles: **choreography** (each "
            "service publishes events, others react) vs **orchestration** (central saga coordinator). Use when "
            "2PC/acid across services is impossible. Example: PlaceOrder → ReserveInventory → ChargePayment; "
            "if payment fails, **compensate** by releasing inventory. Implement with **MassTransit**, "
            "**NServiceBus**, or Azure Durable Functions. Pair with **idempotent** consumers."
        ),
        "code": """// Orchestrated saga state machine (conceptual)
public enum SagaState { Started, InventoryReserved, PaymentCaptured, Completed, Failed }

public class PlaceOrderSaga : MassTransitStateMachine<PlaceOrderSagaState>
{
    public PlaceOrderSaga()
    {
        Initially(
            When(OrderPlaced)
                .Then(ctx => ctx.ReserveInventory())
                .TransitionTo(InventoryReserved));

        During(InventoryReserved,
            When(PaymentFailed)
                .Then(ctx => ctx.ReleaseInventory()) // compensating action
                .TransitionTo(Failed),
            When(PaymentSucceeded)
                .TransitionTo(Completed));
    }
}

// Each step is a local transaction + event; no distributed lock""",
        "language": "csharp",
        "key_points": [
            "Saga = local txs + compensations, not 2PC",
            "Choreography vs orchestration tradeoffs",
            "Compensating actions must be idempotent",
            "MassTransit/NServiceBus provide saga infrastructure",
            "Business must accept eventual consistency",
        ],
    },
    "outbox-pattern": {
        "explanation": (
            "The **Outbox pattern** solves **dual-write** problem: saving to DB and publishing to message bus "
            "atomically. Write domain changes and an **outbox message row** in the **same DB transaction**. "
            "A separate **relay process** reads outbox and publishes to broker, marking rows sent. Guarantees "
            "**at-least-once delivery** without losing messages if crash after commit. EF Core supports this via "
            "library (e.g. **Marten**, **MassTransit EF outbox**, custom `OutboxMessage` table). Critical for "
            "reliable microservice integration."
        ),
        "code": """public class OutboxMessage
{
    public Guid Id { get; set; }
    public string Type { get; set; } = "";
    public string Payload { get; set; } = "";
    public DateTime CreatedAt { get; set; }
    public DateTime? ProcessedAt { get; set; }
}

// Same transaction as domain save
await using var tx = await _db.Database.BeginTransactionAsync(ct);
_db.Orders.Add(order);
_db.Outbox.Add(new OutboxMessage
{
    Id = Guid.NewGuid(),
    Type = nameof(OrderPlacedEvent),
    Payload = JsonSerializer.Serialize(new OrderPlacedEvent(order.Id)),
    CreatedAt = DateTime.UtcNow
});
await _db.SaveChangesAsync(ct);
await tx.CommitAsync(ct);

// Background worker publishes outbox rows to Service Bus""",
        "language": "csharp",
        "key_points": [
            "Outbox row written in same DB transaction as domain",
            "Relay worker publishes and marks processed",
            "Fixes dual-write: DB commit vs message publish",
            "Consumers must be idempotent (at-least-once)",
            "MassTransit EF outbox automates pattern in .NET",
        ],
    },
    "strangler-fig-pattern": {
        "explanation": (
            "The **Strangler Fig** pattern (Martin Fowler) **incrementally replaces** a legacy system by routing "
            "traffic to new modules while the old system still runs. Start at edges (read-only APIs, new features), "
            "proxy/gateway routes `%` of requests to new stack, grow until legacy can be decommissioned. "
            "Reduces **big-bang rewrite** risk. Tools: **API gateway**, **YARP**, **Azure Front Door** path rules, "
            "feature flags. Often paired with **Anti-Corruption Layer** when new domain talks to legacy DB."
        ),
        "code": """// YARP reverse proxy — route new endpoints to modern API
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddReverseProxy()
    .LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));

// appsettings.json
// "ReverseProxy": {
//   "Routes": {
//     "new-orders": { "ClusterId": "modern", "Match": { "Path": "/api/v2/orders/{**catch-all}" } },
//     "legacy-fallback": { "ClusterId": "legacy", "Match": { "Path": "/api/{**catch-all}" } }
//   }
// }

// Gradually add v2 routes; legacy handles remainder until strangled""",
        "language": "csharp",
        "key_points": [
            "Incremental migration — no big-bang rewrite",
            "Proxy routes traffic to new vs legacy modules",
            "Start with leaf features or read-only paths",
            "Feature flags control rollout percentage",
            "Anti-corruption layer protects new domain from legacy",
        ],
    },
    "anti-corruption-layer": {
        "explanation": (
            "An **Anti-Corruption Layer (ACL)** in DDD is a **translation boundary** between your bounded context "
            "and an external/legacy system whose model would **corrupt** your domain if imported raw. The ACL "
            "maps external DTOs/schemas to your domain language and hides legacy quirks (odd field names, "
            "status codes, batch APIs). Often implemented as dedicated **adapter service** or module. Distinct "
            "from generic Adapter when translation is **semantic**, not just interface mismatch."
        ),
        "code": """// Legacy ERP model — do NOT leak into domain
public class ErpSalesOrder
{
    public string SO_NUM { get; set; } = "";
    public decimal AMT_USD { get; set; }
    public string STAT_CD { get; set; } = ""; // "SH", "OP", "CN"
}

// ACL — translates to domain Order
public class ErpAntiCorruptionLayer(ErpClient erp)
{
    public async Task<Order> GetOrderAsync(string erpId, CancellationToken ct)
    {
        var raw = await erp.FetchSalesOrderAsync(erpId, ct);
        return new Order(
            id: ParseOrderId(raw.SO_NUM),
            total: Money.Usd(raw.AMT_USD),
            status: MapStatus(raw.STAT_CD)); // SH → Shipped, etc.
    }

    private static OrderStatus MapStatus(string code) => code switch
    {
        "SH" => OrderStatus.Shipped,
        "OP" => OrderStatus.Open,
        "CN" => OrderStatus.Cancelled,
        _ => OrderStatus.Unknown
    };
}""",
        "language": "csharp",
        "key_points": [
            "ACL translates external/legacy models to your domain",
            "Prevents corrupt terminology entering bounded context",
            "Heavier than simple adapter — semantic mapping",
            "Common in strangler fig migrations",
            "Isolate in dedicated module or integration service",
        ],
    },
}
