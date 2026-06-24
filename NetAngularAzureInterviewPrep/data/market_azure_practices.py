"""Market-relevant Azure and Best Practices interview topics (2025/2026)."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("azure", "foundation"): [
        InterviewItem(
            "azure-entra-id",
            "What is Microsoft Entra ID (Azure AD) and how does it secure APIs?",
            "**Entra ID** is Azure's cloud identity platform — user directory, SSO, MFA, conditional access, and OAuth2/OIDC for apps.",
            """builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddMicrosoftIdentityWebApi(builder.Configuration.GetSection("AzureAd"));

builder.Services.AddAuthorization();""",
            key_points=["OAuth2/OIDC for SPA + API", "App registrations and scopes", "Conditional Access enforces MFA/location"],
        ),
        InterviewItem(
            "azure-vnet",
            "What is an Azure Virtual Network (VNet)?",
            "A private network in Azure — subnets, route tables, peering, and service endpoints isolate workloads.",
            """# Bicep — VNet with two subnets
resource vnet 'Microsoft.Network/virtualNetworks@2023-05-01' = {
  name: 'vnet-prod'
  location: location
  properties: {
    addressSpace: { addressPrefixes: ['10.0.0.0/16'] }
    subnets: [
      { name: 'web', properties: { addressPrefix: '10.0.1.0/24' } }
      { name: 'data', properties: { addressPrefix: '10.0.2.0/24' } }
    ]
  }
}""",
            "bicep",
            key_points=["Subnets segment tiers (web/app/data)", "VNet peering connects networks", "Private endpoints keep traffic off public internet"],
        ),
        InterviewItem(
            "azure-nsg",
            "What are Network Security Groups (NSGs)?",
            "Stateful firewall rules at subnet or NIC level — allow/deny by port, protocol, source/destination.",
            """# Allow HTTPS inbound to web subnet; deny all else by default
{
  "name": "Allow-HTTPS",
  "properties": {
    "priority": 100,
    "direction": "Inbound",
    "access": "Allow",
    "protocol": "Tcp",
    "sourceAddressPrefix": "*",
    "destinationPortRange": "443"
  }
}""",
            "json",
            key_points=["Lower priority number = higher precedence", "Default rules allow VNet traffic", "Combine with Azure Firewall for central policy"],
        ),
        InterviewItem(
            "azure-sql-database",
            "What is Azure SQL Database? How does it differ from SQL on a VM?",
            "Fully managed PaaS SQL — automatic backups, patching, scaling. No OS/VM management.",
            """builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("AzureSql")));

// Connection string uses *.database.windows.net
// Enable AAD auth + Managed Identity in production""",
            key_points=["DTU vs vCore pricing models", "Geo-replication for DR", "Always Encrypted for sensitive columns"],
        ),
        InterviewItem(
            "azure-storage-accounts",
            "Explain Azure Storage account types and services.",
            "Storage accounts provide Blob (files), Queue, Table, and File shares — tiered by performance and redundancy.",
            """BlobServiceClient client = new(
    new Uri("https://mystorage.blob.core.windows.net"),
    new DefaultAzureCredential());

var container = client.GetBlobContainerClient("uploads");
await container.UploadBlobAsync("report.pdf", stream);""",
            key_points=["LRS/ZRS/GRS redundancy options", "Hot/Cool/Archive blob tiers", "Managed Identity over account keys"],
        ),
        InterviewItem(
            "azure-managed-identity",
            "Explain Managed Identity in Azure — system-assigned vs user-assigned.",
            "Azure-managed service principals — apps authenticate to Azure resources without storing credentials.",
            """// System-assigned: tied to one resource (App Service, VM, Function)
// User-assigned: shared across multiple resources

var credential = new DefaultAzureCredential();
var secretClient = new SecretClient(
    new Uri("https://myvault.vault.azure.net/"),
    credential);
KeyVaultSecret secret = await secretClient.GetSecretAsync("SqlConnection");""",
            key_points=["DefaultAzureCredential chains local + Azure auth", "Grant least-privilege RBAC roles", "No secrets in appsettings in prod"],
        ),
        InterviewItem(
            "azure-cost-optimization",
            "How do you optimize Azure costs?",
            "Right-size resources, reserved instances, auto-shutdown dev, storage tiering, and FinOps tagging.",
            """# Azure CLI — resize underused App Service plan
az appservice plan update --name plan-prod --sku S1

# Tag resources for cost allocation
az tag create --resource-id $ID --tags Environment=Prod Team=Orders""",
            "bash",
            key_points=["Azure Cost Management + budgets/alerts", "Reserved capacity for predictable workloads", "Delete unused resources (dev/test RG)"],
        ),
    ],
    ("azure", "intermediate"): [
        InterviewItem(
            "azure-load-balancer",
            "Compare Azure Load Balancer, Application Gateway, and Front Door.",
            "**Load Balancer** (L4) distributes TCP/UDP. **App Gateway** (L7) adds SSL termination, WAF, path routing.",
            """# Standard Load Balancer — health probe on /health
resource lb 'Microsoft.Network/loadBalancers@2023-05-01' = {
  name: 'lb-api'
  properties: {
    frontendIPConfigurations: [ { name: 'fe', properties: { /* ... */ } } ]
    backendAddressPools: [ { name: 'api-pool' } ]
    probes: [ { name: 'health', properties: { protocol: 'Http', path: '/health' } } ]
  }
}""",
            "bicep",
            key_points=["Public vs internal LB", "Health probes remove unhealthy nodes", "App Gateway for web apps needing WAF"],
        ),
        InterviewItem(
            "azure-api-management",
            "What is Azure API Management (APIM)?",
            "Gateway for APIs — rate limiting, JWT validation, versioning, developer portal, and analytics.",
            """<!-- policy.xml — validate JWT at gateway -->
<inbound>
  <validate-jwt header-name="Authorization" require-scheme="Bearer">
    <openid-config url="https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration" />
    <audiences><audience>api://my-order-api</audience></audiences>
  </validate-jwt>
  <rate-limit calls="100" renewal-period="60" />
</inbound>""",
            "xml",
            key_points=["Decouple clients from backend URLs", "Products and subscriptions for partners", "Self-hosted gateway for hybrid"],
        ),
        InterviewItem(
            "azure-monitor-log-analytics",
            "What is Azure Monitor and Log Analytics?",
            "Central observability — metrics, logs, traces, workbooks, and KQL queries across Azure and on-prem.",
            """// KQL — failed requests in last hour
requests
| where timestamp > ago(1h)
| where success == false
| summarize count() by resultCode, name
| order by count_ desc

// .NET — OpenTelemetry exporter to Azure Monitor
builder.Services.AddOpenTelemetry()
    .UseAzureMonitor();""",
            key_points=["Log Analytics workspace stores queryable logs", "KQL is essential for interviews", "Integrates with App Insights"],
        ),
        InterviewItem(
            "azure-event-grid",
            "What is Azure Event Grid?",
            "Serverless event routing — pub/sub with topics, event subscriptions, and push delivery to handlers.",
            """// Publish custom event
var client = new EventGridPublisherClient(
    new Uri(topicEndpoint), new AzureKeyCredential(topicKey));

await client.SendEventAsync(new EventGridEvent(
    subject: "orders/1042",
    eventType: "Order.Placed",
    dataVersion: "1.0",
    data: orderPayload));""",
            key_points=["Event-driven, not polling", "Dead-letter for failed deliveries", "System topics for Azure resource events"],
        ),
        InterviewItem(
            "azure-event-hubs",
            "What is Azure Event Hubs vs Service Bus?",
            "**Event Hubs** = high-throughput event streaming (Kafka-compatible). **Service Bus** = enterprise messaging with transactions.",
            """await using var producer = new EventHubProducerClient(connectionString, "order-events");
using EventDataBatch batch = await producer.CreateBatchAsync();
batch.TryAdd(new EventData(Encoding.UTF8.GetBytes(json)));
await producer.SendAsync(batch);""",
            key_points=["Partitions enable parallel consumers", "Capture to Blob for replay/analytics", "Use Service Bus for ordered workflows"],
        ),
        InterviewItem(
            "azure-container-instances",
            "When do you use Azure Container Instances (ACI)?",
            "Run containers without managing Kubernetes — quick jobs, burst workloads, CI agents.",
            """az container create \\
  --resource-group rg-prod \\
  --name order-processor \\
  --image myregistry.azurecr.io/processor:1.0 \\
  --cpu 1 --memory 1.5 \\
  --registry-login-server myregistry.azurecr.io""",
            "bash",
            key_points=["No cluster overhead", "Per-second billing", "AKS for long-running orchestration at scale"],
        ),
        InterviewItem(
            "azure-front-door",
            "What is Azure Front Door?",
            "Global L7 load balancer + CDN + WAF — anycast edge, SSL offload, path routing, health probes.",
            """/*
  User → Front Door (edge PoP)
           ├── WAF rules (OWASP)
           ├── Cache static assets
           └── Route /api/* → App Service (origin)
               Route /*     → Static Web Apps
*/""",
            "text",
            key_points=["Active-active multi-region failover", "Rules engine for URL redirects", "Premium tier adds private link origins"],
        ),
        InterviewItem(
            "azure-monitor-alerts",
            "How do Azure Monitor alerts work?",
            "Metric or log-based rules trigger action groups — email, SMS, webhook, Logic App, or auto-scale.",
            """# Metric alert — CPU > 80% for 5 min
az monitor metrics alert create \\
  --name high-cpu \\
  --resource /subscriptions/.../my-api \\
  --condition \"avg Percentage CPU > 80\" \\
  --window-size 5m \\
  --action email admins@company.com""",
            "bash",
            key_points=["Alert vs alert rule vs action group", "Log alerts use KQL scheduled queries", "Smart detection in App Insights"],
        ),
    ],
    ("azure", "advanced"): [
        InterviewItem(
            "bicep-vs-arm",
            "Compare Bicep vs ARM templates vs Terraform on Azure.",
            "**Bicep** compiles to ARM — Azure-native, idempotent, no state file. **Terraform** is multi-cloud with remote state.",
            """// main.bicep — App Service + plan
param location string = resourceGroup().location

resource plan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: 'plan-orders'
  location: location
  sku: { name: 'S1', tier: 'Standard' }
}

resource app 'Microsoft.Web/sites@2022-09-01' = {
  name: 'order-api-prod'
  location: location
  properties: { serverFarmId: plan.id }
}""",
            "bicep",
            key_points=["Bicep modules for reuse", "What-if deployment preview", "Terraform for multi-cloud; Bicep for Azure-only"],
        ),
        InterviewItem(
            "azure-devops-boards-pipelines",
            "How do Azure DevOps Boards and Pipelines work together?",
            "Boards track work items (User Stories, Bugs); Pipelines CI/CD linked to branches and work item state.",
            """# azure-pipelines.yml
trigger:
  branches: [main]

stages:
  - stage: Build
    jobs:
      - job: BuildTest
        steps:
          - task: DotNetCoreCLI@2
            inputs: { command: test, projects: '**/*Tests.csproj' }
  - stage: Deploy
    dependsOn: Build
    jobs:
      - deployment: Prod
        environment: production
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1""",
            "yaml",
            key_points=["Work items link to commits and PRs", "Branch policies enforce reviews", "Variable groups + Key Vault for secrets"],
        ),
        InterviewItem(
            "azure-disaster-recovery",
            "Design disaster recovery and backup on Azure.",
            "RPO/RTO drive strategy — geo-redundant storage, SQL geo-replication, paired regions, Azure Backup.",
            """/*
  Primary (East US)              Secondary (West US)
  ├── App Service (active)       ├── App Service (standby / slots)
  ├── Azure SQL (primary)   ──►  ├── SQL geo-replica (readable)
  └── Storage GRS           ──►  └── Automatic secondary region

  Azure Backup: VM, SQL, file shares — retention policies
  Site Recovery: VM replication for full DR
*/""",
            "text",
            key_points=["Define RPO (data loss) and RTO (downtime)", "Test failover annually", "Backup != DR — need runbook + DNS failover"],
        ),
        InterviewItem(
            "azure-ad-b2c",
            "What is Azure AD B2C?",
            "Customer identity — social logins, custom branded sign-up/sign-in, user flows, and token issuance for consumer apps.",
            """builder.Services.AddAuthentication(OpenIdConnectDefaults.AuthenticationScheme)
    .AddMicrosoftIdentityWebApp(builder.Configuration.GetSection("AzureAdB2C"));

// User flow: Sign up / Sign in (built-in UI)
// Custom policies (Identity Experience Framework) for complex scenarios""",
            key_points=["Separate tenant from workforce Entra ID", "Social IdPs (Google, Facebook)", "Custom attributes and MFA for customers"],
        ),
    ],
    ("practices", "foundation"): [
        InterviewItem(
            "cqrs-pattern",
            "What is CQRS?",
            "**Command Query Responsibility Segregation** — separate models for writes (commands) and reads (queries).",
            """// Command side
public record PlaceOrderCommand(int CustomerId, List<LineItem> Lines);
public class PlaceOrderHandler : IRequestHandler<PlaceOrderCommand, int> { /* write DB */ }

// Query side — optimized read model
public record OrderSummaryDto(int Id, string Customer, decimal Total);
public class GetOrdersHandler : IRequestHandler<GetOrdersQuery, List<OrderSummaryDto>> { /* read DB / cache */ }""",
            key_points=["Scales read and write independently", "Often paired with Event Sourcing", "Don't use CQRS for simple CRUD"],
        ),
        InterviewItem(
            "event-sourcing",
            "What is Event Sourcing?",
            "Store state changes as an append-only event log — current state is rebuilt by replaying events.",
            """public record OrderPlaced(Guid OrderId, int CustomerId, decimal Total);
public record OrderShipped(Guid OrderId, string TrackingNumber);

// Event store (simplified)
public class OrderAggregate
{
    private readonly List<object> _events = [];
    public void Apply(object e) { _events.Add(e); /* mutate state */ }
    public IReadOnlyList<object> GetUncommittedEvents() => _events;
}""",
            key_points=["Audit trail built-in", "Projections build read models", "Snapshots improve replay performance"],
        ),
        InterviewItem(
            "ddd-bounded-contexts",
            "What are DDD bounded contexts?",
            "Explicit boundaries where a domain model and ubiquitous language are consistent — guides microservice splits.",
            """/*
  Orders Context          Billing Context
  ─────────────────       ─────────────────
  Order, OrderLine        Invoice, Payment
  PlaceOrder              ChargeCustomer

  Integration via events or anti-corruption layer — not shared DB tables
*/""",
            "text",
            key_points=["One bounded context = one cohesive model", "Context map shows relationships", "Anti-corruption layer translates external models"],
        ),
        InterviewItem(
            "repository-pattern",
            "Explain the Repository pattern.",
            "Abstraction over data access — domain code depends on `IRepository<T>`, not EF or SQL directly.",
            """public interface IOrderRepository
{
    Task<Order?> GetByIdAsync(int id, CancellationToken ct);
    Task AddAsync(Order order, CancellationToken ct);
    Task SaveChangesAsync(CancellationToken ct);
}

public class OrderRepository(AppDbContext db) : IOrderRepository
{
    public Task<Order?> GetByIdAsync(int id, CancellationToken ct) =>
        db.Orders.FirstOrDefaultAsync(o => o.Id == id, ct);
}""",
            key_points=["Enables unit testing with mocks", "Don't leak IQueryable everywhere", "Generic repo often too coarse — prefer specific repos"],
        ),
        InterviewItem(
            "mediator-pattern-mediatr",
            "What is the Mediator pattern? How is MediatR used in .NET?",
            "Decouples request senders from handlers — one object per use case, pipeline behaviors for cross-cutting.",
            """// Command
public record CancelOrderCommand(int OrderId) : IRequest;

public class CancelOrderHandler : IRequestHandler<CancelOrderCommand>
{
    public async Task Handle(CancelOrderCommand cmd, CancellationToken ct) { /* ... */ }
}

// Controller — thin, no fat services
[HttpPost("{id}/cancel")]
public async Task<IActionResult> Cancel(int id)
    => Ok(await _mediator.Send(new CancelOrderCommand(id)));""",
            key_points=["One handler per command/query", "Pipeline behaviors for logging/validation", "Keeps controllers thin"],
        ),
        InterviewItem(
            "cap-theorem",
            "Explain the CAP theorem.",
            "In a partition, choose **Consistency** or **Availability** — not both. **Partition tolerance** is mandatory in distributed systems.",
            """/*
  CP — Azure SQL (strong consistency, may reject writes during partition)
  AP — Cosmos DB (session/eventual consistency, stays available)

  Interview: "We chose eventual consistency for the catalog read model
  because stale product descriptions for 30s is acceptable."
*/""",
            "text",
            key_points=["Partition = network split between nodes", "PACELC extends CAP for normal operation", "Match consistency to business requirement"],
        ),
        InterviewItem(
            "idempotency",
            "What is idempotency and why does it matter in APIs?",
            "Repeating the same request produces the same result — critical for retries, webhooks, and message consumers.",
            """[HttpPost]
public async Task<IActionResult> CreateOrder(
    [FromBody] CreateOrderDto dto,
    [FromHeader(Name = "Idempotency-Key")] string? idempotencyKey)
{
    if (idempotencyKey is not null &&
        await _store.TryGetResponseAsync(idempotencyKey) is { } cached)
        return cached; // return same 201 as first call

    var order = await _service.CreateAsync(dto);
    await _store.SaveAsync(idempotencyKey, CreatedAtAction(...));
    return CreatedAtAction(...);
}""",
            key_points=["Use Idempotency-Key header for POST", "Message consumers must handle duplicates", "PUT/DELETE are naturally idempotent"],
        ),
        InterviewItem(
            "rest-api-design",
            "What are REST API design best practices?",
            "Resource nouns, proper HTTP verbs/status codes, versioning, pagination, HATEOAS optional, consistent error format.",
            """GET    /api/v1/orders?page=2&pageSize=20
POST   /api/v1/orders              → 201 + Location header
GET    /api/v1/orders/42
PATCH  /api/v1/orders/42           → partial update (JSON Merge Patch)
DELETE /api/v1/orders/42           → 204

// Problem Details (RFC 7807)
{ "type": "...", "title": "Validation failed", "status": 400, "errors": { "email": ["Invalid"] } }""",
            "text",
            key_points=["Version via URL (/v1/) or header", "Cursor pagination for large datasets", "Never expose internal IDs inconsistently"],
        ),
    ],
    ("practices", "intermediate"): [
        InterviewItem(
            "api-security-best-practices",
            "What are API security best practices?",
            "HTTPS, OAuth2/OIDC, least privilege, input validation, rate limiting, no secrets in responses.",
            """builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(/* validate issuer, audience, signing key */);

builder.Services.AddRateLimiter(options =>
    options.AddFixedWindowLimiter("api", o => { o.Window = TimeSpan.FromMinutes(1); o.PermitLimit = 100; }));

app.UseHttpsRedirection();
app.UseAuthentication();
app.UseAuthorization();
app.UseRateLimiter();""",
            key_points=["Validate all input server-side", "CORS allowlist — not * in prod", "Security headers (HSTS, CSP)"],
        ),
        InterviewItem(
            "owasp-top-10",
            "Summarize the OWASP Top 10 relevant to .NET APIs.",
            "Broken access control, cryptographic failures, injection, insecure design, misconfiguration, vulnerable components, auth failures, integrity failures, logging failures, SSRF.",
            """// Prevent injection — parameterized queries (EF Core does this)
await _db.Orders.FromSqlInterpolated($"SELECT * FROM Orders WHERE Id = {id}");

// Prevent broken access control
[Authorize(Policy = "OwnerOnly")]
[HttpGet("{id}")]
public async Task<IActionResult> Get(int id)
{
    var order = await _repo.GetAsync(id);
    if (order.UserId != User.GetUserId()) return Forbid();
    return Ok(order);
}""",
            key_points=["A01 Broken Access Control is #1", "Never log passwords/tokens", "Keep NuGet packages updated (Dependabot)"],
        ),
        InterviewItem(
            "caching-strategies",
            "Compare cache-aside, write-through, and write-behind caching.",
            "**Cache-aside**: app reads cache, on miss loads DB and populates. **Write-through**: write cache + DB together.",
            """// Cache-aside
public async Task<Order?> GetOrderAsync(int id)
{
    var cached = await _cache.GetStringAsync($"order:{id}");
    if (cached is not null) return JsonSerializer.Deserialize<Order>(cached);

    var order = await _db.Orders.FindAsync(id);
    if (order is not null)
        await _cache.SetStringAsync($"order:{id}", JsonSerializer.Serialize(order),
            new DistributedCacheEntryOptions { AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5) });
    return order;
}""",
            key_points=["Always set TTL", "Cache invalidation on write", "Redis for distributed; IMemoryCache for single instance"],
        ),
        InterviewItem(
            "feature-flags",
            "What are feature flags and how do you use them?",
            "Toggle features at runtime without redeploy — gradual rollout, A/B tests, kill switches.",
            """// Microsoft.FeatureManagement
builder.Services.AddFeatureManagement(builder.Configuration);

[HttpGet("beta-report")]
public async Task<IActionResult> BetaReport()
{
    if (await _featureManager.IsEnabledAsync("BetaReporting"))
        return Ok(await _reportService.GenerateBetaAsync());
    return NotFound();
}

// appsettings: "FeatureManagement": { "BetaReporting": true }""",
            key_points=["Azure App Configuration for centralized flags", "Percentage filters for canary", "Remove stale flags after launch"],
        ),
        InterviewItem(
            "observability-three-pillars",
            "Explain observability — logs, metrics, and traces.",
            "**Logs** = discrete events. **Metrics** = aggregated numbers over time. **Traces** = request path across services.",
            """// OpenTelemetry in ASP.NET Core
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddSqlClientInstrumentation())
    .WithMetrics(m => m.AddAspNetCoreInstrumentation());

// Structured log with trace correlation
_logger.LogInformation("Order {OrderId} placed", orderId);""",
            key_points=["Correlation ID links logs across services", "RED method: Rate, Errors, Duration", "USE method for resources: Utilization, Saturation, Errors"],
        ),
        InterviewItem(
            "git-workflow",
            "Compare trunk-based development vs GitFlow.",
            "**Trunk-based**: short-lived branches, frequent merges to main, feature flags. **GitFlow**: long-lived develop/release/hotfix branches.",
            """# Trunk-based (recommended for CI/CD)
git checkout -b feat/order-cancel
# small PR, merge within 1-2 days
git push && gh pr create

# GitFlow
main ← release/1.2 ← develop ← feature/order-cancel
hotfix/1.1.1 → main + develop""",
            "bash",
            key_points=["Trunk-based enables continuous delivery", "GitFlow suits scheduled releases", "Protect main with branch policies"],
        ),
        InterviewItem(
            "code-review-best-practices",
            "What makes an effective code review?",
            "Small PRs, constructive feedback, check correctness/security/tests, approve when ready — not nitpick style.",
            """/*
  Reviewer checklist:
  □ Does it solve the right problem?
  □ Tests cover happy path + edge cases?
  □ No secrets, SQL injection, or N+1 queries?
  □ Naming clear? Functions small?
  □ Breaking API changes documented?

  Author: keep PRs < 400 lines, link work item, self-review first
*/""",
            "text",
            key_points=["Review for learning, not gatekeeping", "Automate style with linters", "SLA: review within 24 hours"],
        ),
        InterviewItem(
            "circuit-breaker-pattern",
            "What is the Circuit Breaker pattern?",
            "Stop calling a failing dependency after threshold — fail fast, allow recovery, then half-open retry.",
            """// Polly circuit breaker
var pipeline = new ResiliencePipelineBuilder()
    .AddCircuitBreaker(new CircuitBreakerStrategyOptions
    {
        FailureRatio = 0.5,
        MinimumThroughput = 10,
        BreakDuration = TimeSpan.FromSeconds(30)
    })
    .Build();

await pipeline.ExecuteAsync(async ct => await _httpClient.GetAsync("/api/orders", ct));""",
            key_points=["Closed → Open → Half-Open states", "Combine with retry and timeout", "Polly v8 ResiliencePipeline in .NET 8"],
        ),
    ],
    ("practices", "advanced"): [
        InterviewItem(
            "twelve-factor-app",
            "What is the Twelve-Factor App methodology?",
            "Cloud-native app principles — config in env, stateless processes, disposability, dev/prod parity, logs as streams.",
            """/*
  III. Config  — store in environment / Key Vault, not code
  VI.  Processes — share nothing; session in Redis
  IX.  Disposability — fast startup, graceful SIGTERM shutdown
  XII. Admin processes — migrations as one-off release tasks

  dotnet run --environment Production
  ConnectionStrings__Sql from env var (double underscore)
*/""",
            "text",
            key_points=["One codebase, many deploys", "Backing services as attached resources", "Port binding — self-contained Kestrel"],
        ),
        InterviewItem(
            "blue-green-deployment",
            "Explain blue-green deployment.",
            "Two identical environments — deploy to idle (green), test, switch traffic, keep blue for rollback.",
            """# Azure App Service deployment slots
az webapp deployment slot create --name order-api --slot green
az webapp deployment source config-zip --slot green --src api.zip
# smoke test green slot URL
az webapp deployment slot swap --name order-api --slot green
# instant rollback: swap back to blue""",
            "bash",
            key_points=["Zero-downtime when swap is instant", "Database migrations need backward compatibility", "Slots share App Service plan"],
        ),
        InterviewItem(
            "canary-releases",
            "What is a canary release?",
            "Route a small % of traffic to new version — monitor errors/latency, gradually increase or rollback.",
            """// Azure Front Door / App Gateway weighted routing
// 95% → v1 (stable), 5% → v2 (canary)

// Feature flag alternative
if (await _flags.IsEnabledAsync("NewCheckoutFlow"))
    return await _checkoutV2.ProcessAsync(order);
return await _checkoutV1.ProcessAsync(order);""",
            key_points=["Monitor golden signals during canary", "Automate rollback on SLO breach", "Combine with feature flags for app-level canary"],
        ),
        InterviewItem(
            "technical-debt-management",
            "How do you manage technical debt?",
            "Track in backlog, allocate sprint capacity (e.g. 20%), boy scout rule, refactor when touching code.",
            """/*
  Strategies:
  1. Debt register — link to work items with impact/effort
  2. "Cleanup Fridays" or 1 story per sprint
  3. Refactor during feature work (same PR if small)
  4. Strangler fig for legacy modules

  Avoid: big-bang rewrite without business buy-in
*/""",
            "text",
            key_points=["Not all debt is bad — conscious tradeoffs", "Measure: code churn, bug rate, lead time", "Communicate debt cost to stakeholders"],
        ),
        InterviewItem(
            "agile-scrum",
            "Explain Agile/Scrum ceremonies and artifacts.",
            "Sprints (2 weeks), Daily Standup, Sprint Planning, Review, Retrospective. Artifacts: Product Backlog, Sprint Backlog, Increment.",
            """/*
  Sprint Planning: team commits to sprint goal + stories
  Daily Standup: 15 min — what I did, will do, blockers
  Review: demo working software to stakeholders
  Retro: what went well, improve, action items

  Definition of Done: tested, reviewed, deployed to staging, docs updated
*/""",
            "text",
            key_points=["User stories: As a [role], I want [goal], so that [benefit]", "Story points estimate complexity not hours", "Scrum Master removes impediments"],
        ),
        InterviewItem(
            "pair-programming",
            "What are the benefits and styles of pair programming?",
            "Driver writes, navigator reviews/thinks ahead — knowledge sharing, fewer bugs, faster onboarding.",
            """/*
  Styles:
  - Driver-Navigator (classic)
  - Ping-Pong TDD (one writes test, other makes it pass)
  - Mob programming (whole team, one driver rotates)

  Remote: VS Code Live Share, screen share + timer swap every 25 min
  Use for: complex features, onboarding, critical bug fixes
*/""",
            "text",
            key_points=["Not 2x cost — often faster with higher quality", "Rotate roles frequently", "Pair on interviews / tough design decisions"],
        ),
        InterviewItem(
            "sre-practices",
            "What are Site Reliability Engineering (SRE) practices?",
            "Error budgets, SLIs/SLOs/SLAs, toil reduction, blameless postmortems, automation.",
            """/*
  SLI: request latency p99 < 500ms
  SLO: 99.9% of requests meet SLI over 30 days
  Error budget: 0.1% = ~43 min downtime/month

  If error budget exhausted → freeze features, focus on reliability
  Postmortem: timeline, root cause, action items (no blame)
*/""",
            "text",
            key_points=["SLO drives engineering priorities", "Automate toil (manual ops work)", "On-call runbooks and escalation paths"],
        ),
        InterviewItem(
            "retry-policies-polly",
            "How do retry policies work? Explain Polly in .NET.",
            "Retry transient failures with backoff — 429, 503, timeouts. Avoid retrying non-idempotent ops blindly.",
            """var pipeline = new ResiliencePipelineBuilder<HttpResponseMessage>()
    .AddRetry(new RetryStrategyOptions<HttpResponseMessage>
    {
        MaxRetryAttempts = 3,
        Delay = TimeSpan.FromSeconds(2),
        BackoffType = DelayBackoffType.Exponential,
        ShouldHandle = new PredicateBuilder<HttpResponseMessage>()
            .HandleResult(r => (int)r.StatusCode >= 500)
            .Handle<HttpRequestException>()
    })
    .AddTimeout(TimeSpan.FromSeconds(10))
    .Build();""",
            key_points=["Exponential backoff + jitter", "Retry only idempotent operations", "Combine retry + circuit breaker + timeout"],
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "azure-entra-id": {
        "explanation": (
            "**Microsoft Entra ID** (formerly Azure Active Directory) is the cloud **identity and access management (IAM)** "
            "platform for workforce and application identities. It provides a **user/group directory**, **Single Sign-On (SSO)**, "
            "**Multi-Factor Authentication (MFA)**, **Conditional Access** (policy-based access: location, device compliance, risk), "
            "and **OAuth 2.0 / OpenID Connect (OIDC)** for securing APIs and SPAs. In a typical .NET + Angular stack, the SPA "
            "uses **MSAL.js** to obtain access tokens; the API validates JWTs via **Microsoft.Identity.Web**. "
            "**App registrations** define API scopes (`api://my-api/Orders.Read`) and redirect URIs. "
            "**Service principals** represent automated workloads (CI/CD, background jobs). "
            "Interview tip: distinguish **Entra ID (workforce)** from **Entra External ID / B2C (customers)**."
        ),
        "code": """// Program.cs — protect API with Entra ID JWT
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddMicrosoftIdentityWebApi(builder.Configuration.GetSection("AzureAd"));

builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("OrdersWrite", policy =>
        policy.RequireClaim("scope", "Orders.Write"));
});

// appsettings.json
// "AzureAd": {
//   "Instance": "https://login.microsoftonline.com/",
//   "TenantId": "<tenant-guid>",
//   "ClientId": "<api-app-id>",
//   "Audience": "api://my-order-api"
// }

[Authorize(Policy = "OrdersWrite")]
[HttpPost]
public async Task<IActionResult> Create([FromBody] CreateOrderDto dto)
    => Ok(await _service.CreateAsync(dto));""",
        "language": "csharp",
        "key_points": [
            "OAuth2/OIDC — authorization code flow for SPAs with PKCE",
            "Conditional Access enforces MFA, compliant devices, trusted locations",
            "App roles vs scopes — roles for RBAC, scopes for delegated permissions",
            "Managed identities are Entra service principals — no secrets",
            "Microsoft.Identity.Web simplifies JWT validation in ASP.NET Core",
        ],
    },
    "azure-vnet": {
        "explanation": (
            "An **Azure Virtual Network (VNet)** is a logically isolated private network in Azure with your own **IP address space**, "
            "**subnets**, **route tables**, and **DNS settings**. Subnets segment workloads (web tier, app tier, data tier) and attach "
            "**NSGs** for traffic filtering. **VNet peering** connects VNets privately without public internet. "
            "**Service endpoints** and **Private Endpoints** let PaaS services (SQL, Storage, Key Vault) be reached over private IP. "
            "**Azure Firewall** or **NVAs** provide centralized egress/ingress control. "
            "In interviews, explain how you place App Service (VNet integration), AKS nodes, and Azure SQL private endpoint in a hub-spoke topology."
        ),
        "code": """// main.bicep — production VNet with tiered subnets
param location string = resourceGroup().location

resource vnet 'Microsoft.Network/virtualNetworks@2023-05-01' = {
  name: 'vnet-prod-eastus'
  location: location
  properties: {
    addressSpace: { addressPrefixes: ['10.10.0.0/16'] }
    subnets: [
      {
        name: 'snet-web'
        properties: {
          addressPrefix: '10.10.1.0/24'
          delegations: []
        }
      }
      {
        name: 'snet-data'
        properties: {
          addressPrefix: '10.10.2.0/24'
          privateEndpointNetworkPolicies: 'Disabled'
        }
      }
    ]
  }
}

// App Service VNet Integration — route outbound to private SQL endpoint
// AKS: assign nodes to snet-app with NSG allowing only required ports""",
        "language": "bicep",
        "key_points": [
            "Plan IP space carefully — peering requires non-overlapping CIDRs",
            "Private Endpoints preferred over service endpoints for PaaS",
            "Hub-spoke: shared services (Firewall, VPN Gateway) in hub",
            "NSGs applied at subnet or NIC level",
            "DNS private zones resolve *.privatelink.database.windows.net",
        ],
    },
    "azure-nsg": {
        "explanation": (
            "**Network Security Groups (NSGs)** contain **security rules** that allow or deny inbound/outbound traffic based on "
            "**priority**, **source/destination**, **port**, and **protocol**. Rules are **stateful** — return traffic for allowed "
            "connections is automatically permitted. Apply NSGs to **subnets** (all NICs in subnet) or individual **NICs**. "
            "Default rules (65000+) allow VNet traffic and deny inbound internet. Lower priority number = evaluated first. "
            "Combine NSGs with **Azure Firewall** for centralized, FQDN-based rules and threat intelligence. "
            "**Pitfall:** overly permissive `*` source on management ports (22, 3389) — use Bastion or VPN instead."
        ),
        "code": """// Bicep — NSG for web subnet: HTTPS in, deny rest
resource nsgWeb 'Microsoft.Network/networkSecurityGroups@2023-05-01' = {
  name: 'nsg-web'
  location: location
  properties: {
    securityRules: [
      {
        name: 'Allow-HTTPS-Inbound'
        properties: {
          priority: 100
          direction: 'Inbound'
          access: 'Allow'
          protocol: 'Tcp'
          sourceAddressPrefix: 'Internet'
          destinationAddressPrefix: '10.10.1.0/24'
          destinationPortRange: '443'
        }
      }
      {
        name: 'Deny-All-Inbound'
        properties: {
          priority: 4096
          direction: 'Inbound'
          access: 'Deny'
          protocol: '*'
          sourceAddressPrefix: '*'
          destinationAddressPrefix: '*'
          destinationPortRange: '*'
        }
      }
    ]
  }
}""",
        "language": "bicep",
        "key_points": [
            "Priority 100–4096; lower number wins",
            "Stateful — return traffic auto-allowed",
            "Use Application Security Groups (ASGs) to group VMs by role",
            "NSG flow logs → Traffic Analytics for auditing",
            "Deny explicit rules rarely needed — default deny inbound from Internet",
        ],
    },
    "azure-sql-database": {
        "explanation": (
            "**Azure SQL Database** is a fully managed **PaaS** relational database — Microsoft handles patching, backups, "
            "and high availability. No VM or SQL Server licensing to manage. **Service tiers**: General Purpose (balanced), "
            "Business Critical (low latency, readable secondaries), Hyperscale (100+ TB). Pricing via **DTUs** (bundled) or "
            "**vCores** (more control). **Automatic backups** with point-in-time restore (7–35 days). "
            "**Active geo-replication** and **failover groups** for DR. **Entra ID authentication** + **Managed Identity** "
            "eliminate SQL logins in connection strings. **Always Encrypted** protects sensitive columns client-side."
        ),
        "code": """// Program.cs — Azure SQL with Managed Identity (no password)
var connectionString =
    "Server=tcp:myserver.database.windows.net,1433;" +
    "Database=OrdersDb;Authentication=Active Directory Managed Identity;";

builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(connectionString));

// Failover group connection (read/write listener)
// Server=tcp:orders-fog.database.windows.net,1433;...

// Index for interview performance question
// CREATE INDEX IX_Orders_CustomerId ON Orders(CustomerId) INCLUDE (Total, OrderDate);""",
        "language": "csharp",
        "key_points": [
            "PaaS — no OS patching; automatic backups",
            "DTU vs vCore — vCore for predictable performance tuning",
            "Failover groups: automatic DR with RPO ~5 sec",
            "Elastic pools share resources across many small DBs",
            "Query Store and Intelligent Insights for performance tuning",
        ],
    },
    "azure-storage-accounts": {
        "explanation": (
            "An **Azure Storage account** is a namespace for **Blob** (object/files), **Queue** (simple messaging), "
            "**Table** (NoSQL key-value), and **Azure Files** (SMB/NFS shares). Choose **performance tier** "
            "(Standard vs Premium) and **redundancy** (LRS, ZRS, GRS, GZRS). **Blob tiers**: Hot (frequent access), "
            "Cool (infrequent), Archive (rare, high retrieval latency). **Managed Identity** and **RBAC** replace "
            "shared access keys in production. **SAS tokens** grant time-limited delegated access for client uploads. "
            "**Lifecycle management** auto-tiers or deletes blobs by age."
        ),
        "code": """// Upload with Managed Identity — no account key
var blobServiceClient = new BlobServiceClient(
    new Uri("https://orderstorage.blob.core.windows.net"),
    new DefaultAzureCredential());

var container = blobServiceClient.GetBlobContainerClient("invoices");
await container.CreateIfNotExistsAsync();

// Generate user-delegation SAS for browser upload (server-side)
var sasBuilder = new BlobSasBuilder
{
    BlobContainerName = "invoices",
    Resource = "c",
    ExpiresOn = DateTimeOffset.UtcNow.AddHours(1)
};
sasBuilder.SetPermissions(BlobContainerSasPermissions.Write);
var sasUri = container.GenerateUserDelegationSasUri(sasBuilder);""",
        "language": "csharp",
        "key_points": [
            "Blob for files; Queue for simple async; Files for lift-and-shift shares",
            "GRS replicates to paired region for DR",
            "Disable public blob access at account level",
            "Lifecycle rules move to Cool/Archive after N days",
            "CDN + Blob for static Angular assets",
        ],
    },
    "azure-managed-identity": {
        "explanation": (
            "**Managed Identity** gives Azure resources an automatically managed **Entra ID service principal** — "
            "no credentials to rotate or leak. **System-assigned**: one identity per resource, deleted with resource. "
            "**User-assigned**: standalone identity shared across VMs, App Services, Functions. "
            "**DefaultAzureCredential** chains: environment variables → Managed Identity → Azure CLI → VS credentials — "
            "same code works locally and in Azure. Grant **RBAC roles** (e.g., Key Vault Secrets User, Storage Blob Data Contributor) "
            "at resource scope with least privilege. Essential interview topic: how API on App Service reads Key Vault without secrets."
        ),
        "code": """// Any Azure SDK client — DefaultAzureCredential
var credential = new DefaultAzureCredential();

// Key Vault
var secretClient = new SecretClient(
    new Uri("https://kv-orders-prod.vault.azure.net/"),
    credential);
KeyVaultSecret connStr = await secretClient.GetSecretAsync("SqlConnection");

// Storage Blob
var blobClient = new BlobServiceClient(
    new Uri("https://storders.blob.core.windows.net"),
    credential);

// Enable system-assigned identity on App Service (Portal or Bicep):
// identity: { type: 'SystemAssigned' }
// Then assign role: Key Vault Secrets User on the vault""",
        "language": "csharp",
        "key_points": [
            "System-assigned vs user-assigned tradeoffs",
            "DefaultAzureCredential for local dev + prod parity",
            "RBAC over access policies for Key Vault (modern approach)",
            "No secrets in appsettings, env vars, or pipeline YAML",
            "Managed Identity works with SQL, Storage, Service Bus, Cosmos",
        ],
    },
    "azure-cost-optimization": {
        "explanation": (
            "**Azure cost optimization** (FinOps) combines technical and organizational practices. **Right-size** VMs and App Service "
            "plans using Azure Advisor recommendations. **Reserved Instances / Savings Plans** (1–3 year) cut compute costs 30–70% "
            "for steady workloads. **Spot VMs** for fault-tolerant batch jobs. **Auto-shutdown** dev/test resources nights/weekends. "
            "**Storage lifecycle** moves blobs to Cool/Archive. **Tagging** (Environment, CostCenter, Owner) enables chargeback. "
            "**Azure Cost Management** budgets alert before overspend. Delete orphaned disks, IPs, and unused App Service plans."
        ),
        "code": """# Azure CLI — cost management examples

# List top spending resources this month
az consumption usage list --start-date 2026-06-01 --query "[].{Resource:instanceName, Cost:pretaxCost}"

# Create budget alert at 80% of $5000/month
az consumption budget create \\
  --budget-name prod-monthly \\
  --amount 5000 \\
  --time-grain Monthly \\
  --category Cost \\
  --notifications '[{"enabled":true,"operator":"GreaterThan","threshold":80,"contactEmails":["finops@co.com"]}]'

# Resize underutilized App Service plan
az appservice plan update --name plan-prod --sku S1

# Tag for allocation
az resource tag --ids $RESOURCE_ID --tags Environment=Prod Team=Platform CostCenter=IT-001""",
        "language": "bash",
        "key_points": [
            "Advisor flags idle/oversized resources",
            "Reserved capacity for predictable baseline load",
            "Dev/test pricing and auto-shutdown schedules",
            "FinOps: engineers own cost of their resources",
            "Review Cost Management + Advisor monthly",
        ],
    },
    "azure-load-balancer": {
        "explanation": (
            "**Azure Load Balancer** operates at **Layer 4 (TCP/UDP)** — distributes traffic across VMSS, VMs, or AKS nodes "
            "using **frontend IP**, **backend pool**, **health probes**, and **load-balancing rules**. "
            "**Standard LB** supports multi-dimensional scaling, HA ports, and outbound SNAT. "
            "**Application Gateway** is **Layer 7** — URL routing, SSL termination, cookie affinity, **WAF**. "
            "**Front Door** is global L7 with CDN. Choose LB for internal TCP services; App Gateway for web apps needing WAF; "
            "Front Door for global user-facing apps. Health probes remove unhealthy backends automatically."
        ),
        "code": """// Bicep — Standard Load Balancer with HTTP health probe
resource lb 'Microsoft.Network/loadBalancers@2023-05-01' = {
  name: 'lb-order-api'
  location: location
  sku: { name: 'Standard' }
  properties: {
    frontendIPConfigurations: [
      { name: 'fe-public', properties: { publicIPAddress: { id: pip.id } } }
    ]
    backendAddressPools: [{ name: 'api-pool' }]
    probes: [
      {
        name: 'health-probe'
        properties: {
          protocol: 'Http'
          port: 8080
          requestPath: '/health'
          intervalInSeconds: 15
          numberOfProbes: 2
        }
      }
    ]
    loadBalancingRules: [
      {
        name: 'rule-https'
        properties: {
          frontendIPConfiguration: { id: resourceId('Microsoft.Network/loadBalancers/frontendIPConfigurations', 'lb-order-api', 'fe-public') }
          backendAddressPool: { id: resourceId('Microsoft.Network/loadBalancers/backendAddressPools', 'lb-order-api', 'api-pool') }
          probe: { id: resourceId('Microsoft.Network/loadBalancers/probes', 'lb-order-api', 'health-probe') }
          protocol: 'Tcp'
          frontendPort: 443
          backendPort: 8080
        }
      }
    ]
  }
}""",
        "language": "bicep",
        "key_points": [
            "L4 LB vs L7 App Gateway vs global Front Door",
            "Health probes — /health endpoint required",
            "Internal LB for private-only APIs",
            "Outbound rules prevent SNAT port exhaustion",
            "AKS uses Azure CNI + Standard LB by default",
        ],
    },
    "azure-api-management": {
        "explanation": (
            "**Azure API Management (APIM)** is a managed **API gateway** — single entry point for internal and external consumers. "
            "Features: **rate limiting/throttling**, **JWT/OAuth validation**, **request/response transformation**, "
            "**API versioning**, **developer portal**, **analytics**, and **mock APIs**. Policies are XML applied inbound/outbound/backend. "
            "Tiers: Developer (non-prod), Basic/Standard/ Premium (VNet, multi-region). "
            "**Self-hosted gateway** runs in your network for hybrid. In architecture interviews, APIM sits between Angular SPA and "
            "microservices — validates Entra tokens, enforces quotas, hides backend URLs."
        ),
        "code": """<!-- APIM inbound policy — JWT + rate limit + CORS -->
<policies>
  <inbound>
    <cors allow-credentials="true">
      <allowed-origins><origin>https://orders.example.com</origin></allowed-origins>
      <allowed-methods><method>GET</method><method>POST</method></allowed-methods>
    </cors>
    <validate-jwt header-name="Authorization" require-scheme="Bearer"
                  failed-validation-httpcode="401">
      <openid-config url="https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration" />
      <audiences><audience>api://order-api</audience></audiences>
    </validate-jwt>
    <rate-limit calls="200" renewal-period="60" />
    <set-header name="X-Correlation-Id" exists-action="skip">
      <value>@(Guid.NewGuid().ToString())</value>
    </set-header>
  </inbound>
  <backend><forward-request /></backend>
  <outbound><base /></outbound>
</policies>""",
        "language": "xml",
        "key_points": [
            "Gateway decouples clients from backend URLs",
            "Products/subscriptions for partner API access",
            "Validate JWT at gateway — backend trusts gateway network",
            "Revision-based API versioning",
            "Premium tier: VNet injection, self-hosted gateway",
        ],
    },
    "azure-monitor-log-analytics": {
        "explanation": (
            "**Azure Monitor** is the umbrella observability platform — **metrics** (time-series), **logs** (Log Analytics workspace), "
            "**traces** (Application Insights / distributed tracing), **alerts**, and **workbooks**. "
            "**Log Analytics** stores structured log data queryable with **KQL (Kusto Query Language)**. "
            "Instrument .NET apps with **OpenTelemetry** + **Azure Monitor exporter** or Application Insights SDK. "
            "Correlate App Service, SQL, Service Bus, and custom logs in one workspace. "
            "Interview must-know: write a KQL query for failed requests or slow dependencies."
        ),
        "code": """// Program.cs — OpenTelemetry → Azure Monitor
builder.Services.AddOpenTelemetry()
    .UseAzureMonitor(options =>
        options.ConnectionString = builder.Configuration["ApplicationInsights:ConnectionString"]);

// KQL — top 5 slowest API operations last 24h
/*
requests
| where timestamp > ago(24h)
| summarize avgDuration=avg(duration), p95=percentile(duration, 95), count() by name
| top 5 by p95 desc
*/

// KQL — exceptions grouped by type
/*
exceptions
| where timestamp > ago(1h)
| summarize count() by type, outerMessage
| order by count_ desc
*/

// KQL — join requests with traces (end-to-end)
/*
requests
| where id == "abc-123"
| join kind=inner traces on operation_Id""",
        "language": "csharp",
        "key_points": [
            "Log Analytics workspace centralizes logs",
            "KQL essential — requests, traces, exceptions tables",
            "OpenTelemetry is the modern instrumentation standard",
            "Diagnostic settings export resource logs to workspace",
            "Workbooks for dashboards; Grafana alternative",
        ],
    },
    "azure-event-grid": {
        "explanation": (
            "**Azure Event Grid** is a fully managed **event routing** service using a **publish-subscribe** model. "
            "Publishers emit **events** to **topics**; **event subscriptions** push to subscribers (Azure Functions, "
            "Logic Apps, webhooks, Service Bus, Event Hubs). **System topics** react to Azure resource changes "
            "(Blob created, VM deleted). **Custom topics** for application domain events (`Order.Placed`). "
            "Event Grid is **push-based** and **serverless** — near-real-time delivery with retry and dead-letter. "
            "Differs from Event Hubs (streaming at scale) and Service Bus (enterprise messaging)."
        ),
        "code": """// Publish domain event to custom topic
var client = new EventGridPublisherClient(
    new Uri("https://order-events.eastus-1.eventgrid.azure.net/api/events"),
    new AzureKeyCredential(topicAccessKey));

var egEvent = new EventGridEvent(
    subject: $"orders/{order.Id}",
    eventType: "Order.Placed",
    dataVersion: "1.0",
    data: new { order.Id, order.CustomerId, order.Total });

await client.SendEventAsync(egEvent);

// Azure Function subscriber
[Function(nameof(OnOrderPlaced))]
public async Task OnOrderPlaced(
    [EventGridTrigger] EventGridEvent egEvent)
{
    var order = egEvent.Data.ToObjectFromJson<OrderPlacedPayload>();
    await _notificationService.SendConfirmationAsync(order!);
}""",
        "language": "csharp",
        "key_points": [
            "Event-driven push — not polling",
            "CloudEvents schema supported",
            "Dead-letter storage for failed deliveries",
            "Filter subscriptions by eventType or subject prefix",
            "Use for reactive workflows; Event Hubs for high-volume streams",
        ],
    },
    "azure-event-hubs": {
        "explanation": (
            "**Azure Event Hubs** is a **big data streaming platform** and **event ingestion** service — millions of events/sec. "
            "Events are written to **partitions** (ordered streams within a partition). Consumer groups allow independent readers. "
            "**Capture** auto-writes to Blob/ADLS for replay and analytics. **Kafka protocol** support enables existing Kafka clients. "
            "Compare: **Event Hubs** = throughput + replay + analytics pipeline; **Service Bus** = transactions, sessions, dead-letter, "
            "complex routing; **Event Grid** = discrete event notification. Use Event Hubs for telemetry, IoT, log ingestion, "
            "and event sourcing read side projections."
        ),
        "code": """// Producer — send batch of order events
await using var producer = new EventHubProducerClient(
    fullyQualifiedNamespace: "orders-ns.servicebus.windows.net",
    eventHubName: "order-stream",
    credential: new DefaultAzureCredential());

using EventDataBatch batch = await producer.CreateBatchAsync();
foreach (var order in orders)
{
    var json = JsonSerializer.Serialize(order);
    if (!batch.TryAdd(new EventData(Encoding.UTF8.GetBytes(json))))
    {
        await producer.SendAsync(batch);
        batch.Dispose();
        batch = await producer.CreateBatchAsync();
        batch.TryAdd(new EventData(Encoding.UTF8.GetBytes(json)));
    }
}
await producer.SendAsync(batch);

// Processor — EventProcessorClient with blob checkpoint store""",
        "language": "csharp",
        "key_points": [
            "Partitions enable parallel throughput — choose key wisely",
            "Capture to Data Lake for replay and ML pipelines",
            "Kafka endpoint for ecosystem compatibility",
            "Checkpointing tracks consumer progress",
            "Premium tier for dedicated throughput units",
        ],
    },
    "azure-container-instances": {
        "explanation": (
            "**Azure Container Instances (ACI)** runs containers **without managing VMs or Kubernetes** — fastest path to run a "
            "container in Azure. Billed per second for vCPU and memory. Ideal for **batch jobs**, **CI/CD agents**, **burst workloads**, "
            "and **simple APIs** that don't need orchestration features. Supports **Linux and Windows** containers, "
            "**Managed Identity**, **VNet integration**, and **GPU** (select regions). "
            "Use **AKS** when you need auto-scaling, rolling updates, service mesh, and multi-container pods. "
            "ACI can be triggered from Azure Functions or Logic Apps for event-driven processing."
        ),
        "code": """# Deploy container from Azure Container Registry
az container create \\
  --resource-group rg-prod \\
  --name invoice-processor \\
  --image acrorders.azurecr.io/invoice-processor:2.1.0 \\
  --registry-login-server acrorders.azurecr.io \\
  --assign-identity \\
  --cpu 2 --memory 4 \\
  --restart-policy OnFailure \\
  --environment-variables JOB_ID=1042 \\
  --secure-environment-variables API_KEY=@Microsoft.KeyVault(SecretUri=...) \\
  --subnet /subscriptions/.../subnets/snet-aci

# View logs
az container logs --resource-group rg-prod --name invoice-processor""",
        "language": "bash",
        "key_points": [
            "No cluster management — per-second billing",
            "Managed Identity for ACR pull and Key Vault",
            "VNet injection for private resource access",
            "AKS for production orchestration at scale",
            "Container Groups run multi-container sidecar patterns",
        ],
    },
    "azure-front-door": {
        "explanation": (
            "**Azure Front Door** is a **global Layer 7 load balancer** and **CDN** — traffic enters at the nearest **edge PoP** "
            "(anycast IP). Features: **SSL termination**, **URL/path routing**, **caching**, **compression**, **WAF** (OWASP rules), "
            "**health probes**, and **active-active failover** across origins. **Standard/Premium** tiers; Premium adds "
            "**Private Link** to origins and enhanced WAF. Use Front Door for globally distributed users hitting Angular SPA + API. "
            "Combine with **Static Web Apps** (SPA) and **App Service** (API) as origins. **Pitfall:** cache rules on dynamic API responses."
        ),
        "code": """/*
  Architecture:
  User (global) → Front Door (edge)
                    ├── WAF: block SQL injection, rate limit
                    ├── Rule: /api/* → origin-group-api (App Service East + West)
                    ├── Rule: /*     → origin-group-spa (Static Web Apps)
                    └── Cache: static assets (/*.js, /*.css) TTL 1 day

  Health probe: GET /health every 30s
  Failover: if East origin unhealthy → route 100% to West

  Bicep: Microsoft.Cdn/profiles + afdEndpoints + originGroups
*/

// SPA should use relative /api paths so Front Door routes correctly
// environment.prod.ts: apiUrl: '/api'  (same host, path-based routing)""",
        "language": "text",
        "key_points": [
            "Global anycast — low latency worldwide",
            "WAF at edge — block before origin",
            "Weighted routing for canary releases",
            "Don't cache authenticated API responses",
            "Custom domain + managed certificate",
        ],
    },
    "azure-monitor-alerts": {
        "explanation": (
            "**Azure Monitor alerts** notify teams when metrics or logs cross thresholds. **Metric alerts** evaluate platform "
            "or custom metrics (CPU, HTTP 5xx rate). **Log alert rules** run scheduled **KQL queries** on Log Analytics. "
            "**Activity log alerts** track administrative events. **Action groups** define notification channels: email, SMS, "
            "webhook, Azure Function, Logic App, ITSM ticket. **Smart detection** in Application Insights auto-detects anomalies. "
            "Tie alerts to **SRE error budgets** — alert on SLO burn rate, not every blip."
        ),
        "code": """// KQL-based alert — HTTP 5xx rate > 5% over 15 min
/*
requests
| where timestamp > ago(15m)
| summarize total=count(), failed=countif(success == false) by bin(timestamp, 5m)
| extend failRate = 100.0 * failed / total
| where failRate > 5
*/

# Metric alert via CLI
az monitor metrics alert create \\
  --name api-high-error-rate \\
  --resource-group rg-prod \\
  --scopes /subscriptions/.../providers/Microsoft.Web/sites/order-api \\
  --condition \"avg requests/failed > 10\" \\
  --window-size 5m \\
  --evaluation-frequency 1m \\
  --action-group /subscriptions/.../actionGroups/oncall-pager \\
  --description \"Order API error spike — page on-call\"

# Action group webhook → PagerDuty / Teams""",
        "language": "bash",
        "key_points": [
            "Metric vs log vs activity log alerts",
            "Action groups reusable across alerts",
            "Avoid alert fatigue — meaningful thresholds",
            "Multi-resource alerts for AKS/App Service scale",
            "Alert processing rules suppress maintenance windows",
        ],
    },
    "bicep-vs-arm": {
        "explanation": (
            "**ARM (Azure Resource Manager) templates** are JSON declarative IaC for Azure — idempotent deployments via "
            "`az deployment`. Verbose and hard to maintain. **Bicep** is a domain-specific language that **transpiles to ARM** — "
            "cleaner syntax, modules, type safety, and `what-if` preview. **Terraform** uses HCL, supports multi-cloud, "
            "requires **remote state** management (Azure Storage backend). Choose **Bicep** for Azure-only teams wanting "
            "native integration (no state file, free). Choose **Terraform** for multi-cloud or existing HashiCorp toolchain. "
            "All three support CI/CD deployment from Azure DevOps or GitHub Actions."
        ),
        "code": """// main.bicep — modular, readable vs equivalent ARM JSON
targetScope = 'resourceGroup'

@description('Environment name')
param env string = 'prod'

module appService 'modules/appService.bicep' = {
  name: 'deploy-app-${env}'
  params: {
    appName: 'order-api-${env}'
    sku: env == 'prod' ? 'S1' : 'B1'
  }
}

module keyVault 'modules/keyVault.bicep' = {
  name: 'deploy-kv-${env}'
  params: {
    vaultName: 'kv-orders-${env}'
    appPrincipalId: appService.outputs.identityPrincipalId
  }
}

// Deploy: az deployment group create --template-file main.bicep
// Preview: az deployment group what-if --template-file main.bicep""",
        "language": "bicep",
        "key_points": [
            "Bicep compiles to ARM — same deployment engine",
            "No state file (unlike Terraform) — Azure is source of truth",
            "Modules for reuse across environments",
            "what-if shows changes before apply",
            "Terraform for multi-cloud; Bicep for Azure-native",
        ],
    },
    "azure-devops-boards-pipelines": {
        "explanation": (
            "**Azure DevOps** combines **Boards** (Agile work tracking), **Repos** (Git), **Pipelines** (CI/CD), "
            "**Test Plans**, and **Artifacts**. **Boards** manage backlogs, sprints, Kanban, and queries — work items "
            "(User Story, Bug, Task) link to commits and PRs. **Pipelines** YAML defines build/test/deploy stages; "
            "**environments** add approval gates for production. **Branch policies** require PR reviews and passing builds. "
            "**Variable groups** and **Key Vault task** inject secrets. In interviews, describe PR → build → test → "
            "deploy staging → smoke test → swap slot → close work item."
        ),
        "code": """# azure-pipelines.yml — linked to Azure Boards work items
trigger:
  branches: { include: [main] }

pr:
  branches: { include: [main] }

variables:
  - group: prod-secrets  # linked to Key Vault

stages:
  - stage: Build
    jobs:
      - job: BuildAndTest
        steps:
          - task: DotNetCoreCLI@2
            displayName: Test
            inputs: { command: test, projects: '**/*Tests.csproj' }
          - task: DotNetCoreCLI@2
            displayName: Publish API
            inputs: { command: publish, publishWebProjects: true, arguments: '-c Release -o $(Build.ArtifactStagingDirectory)' }
          - publish: $(Build.ArtifactStagingDirectory)
            artifact: api

  - stage: Deploy
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployProduction
        environment: production  # approval gate configured in DevOps UI
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: prod-service-connection
                    appName: order-api-prod
                    package: $(Pipeline.Workspace)/api/*.zip""",
        "language": "yaml",
        "key_points": [
            "Work items trace requirements to code and releases",
            "Branch policies: min reviewers, build validation",
            "Environments with manual approvals for prod",
            "Multi-stage YAML for build → deploy separation",
            "Service connections use service principal or workload identity",
        ],
    },
    "azure-disaster-recovery": {
        "explanation": (
            "**Disaster recovery (DR)** on Azure starts with **RPO** (acceptable data loss) and **RTO** (acceptable downtime). "
            "**Azure Backup** protects VMs, SQL, file shares with retention policies. **Azure SQL failover groups** provide "
            "automatic geo-failover with ~5 sec RPO. **Geo-redundant storage (GRS/GZRS)** replicates blobs to paired region. "
            "**Site Recovery** replicates VMs for full DR orchestration. **Front Door / Traffic Manager** route DNS to healthy region. "
            "Run **failover tests** annually. **Backup ≠ DR** — backups help restore data; DR requires runbooks, DNS, and app config "
            "for secondary region readiness."
        ),
        "code": """/*
  DR Architecture — active-passive (paired regions)

  Primary: East US                    Secondary: West US
  ┌─────────────────────┐            ┌─────────────────────┐
  │ App Service (active)│            │ App Service (standby)│
  │ Azure SQL (primary) │──geo rep──►│ SQL (secondary RO)   │
  │ Storage GRS         │──async────►│ Secondary blob region│
  │ Key Vault (primary) │            │ Key Vault (replicated)│
  └─────────────────────┘            └─────────────────────┘
           ▲                                      ▲
           └──── Azure Front Door / Traffic Manager ────┘
                 (health probe failover)

  Runbook:
  1. Confirm primary region outage
  2. Initiate SQL failover group switch
  3. Scale up West US App Service
  4. Update Front Door origin priority
  5. Validate smoke tests
  6. Communicate to stakeholders
*/""",
        "language": "text",
        "key_points": [
            "Define RPO/RTO with business stakeholders",
            "SQL failover groups for automated DB DR",
            "Test failover — untested DR is wishful thinking",
            "Backups: point-in-time restore; DR: regional outage",
            "Infrastructure as code makes secondary region reproducible",
        ],
    },
    "azure-ad-b2c": {
        "explanation": (
            "**Azure AD B2C** (now part of **Microsoft Entra External ID**) is a **customer identity and access management (CIAM)** "
            "solution — separate from workforce Entra ID. Supports **social identity providers** (Google, Facebook, Apple), "
            "**local accounts** (email/password), **custom branded UI**, and **user flows** (built-in sign-up/sign-in/password reset). "
            "**Custom policies** (Identity Experience Framework) handle complex scenarios. Issues JWT access tokens your API validates. "
            "Use for consumer-facing Angular apps; use Entra ID for employees/partners with organizational accounts."
        ),
        "code": """// Program.cs — ASP.NET Core with B2C
builder.Services.AddAuthentication(OpenIdConnectDefaults.AuthenticationScheme)
    .AddMicrosoftIdentityWebApp(options =>
    {
        builder.Configuration.Bind("AzureAdB2C", options);
        options.ResponseType = OpenIdConnectResponseType.CodeIdToken;
    });

// appsettings.json
// "AzureAdB2C": {
//   "Instance": "https://mytenant.b2clogin.com/",
//   "Domain": "mytenant.onmicrosoft.com",
//   "ClientId": "<spa-or-api-client-id>",
//   "SignUpSignInPolicyId": "B2C_1_SignUpSignIn",
//   "CallbackPath": "/signin-oidc"
// }

// Angular — MSAL.js with B2C authority:
// authority: 'https://mytenant.b2clogin.com/mytenant.onmicrosoft.com/B2C_1_SignUpSignIn'""",
        "language": "csharp",
        "key_points": [
            "Separate tenant from workforce Entra ID",
            "User flows for standard scenarios; custom policies for complex",
            "Social IdP federation reduces password fatigue",
            "Custom HTML/CSS branding on login pages",
            "MFA and conditional access for consumer apps",
        ],
    },
    "cqrs-pattern": {
        "explanation": (
            "**CQRS (Command Query Responsibility Segregation)** splits **write operations (commands)** from **read operations (queries)** "
            "into separate models and often separate data stores. Commands enforce business rules and mutate state; queries are optimized "
            "for display (denormalized DTOs, read replicas, Elasticsearch). Benefits: **independent scaling**, **optimized schemas**, "
            "clearer code (one handler per use case). Often combined with **Event Sourcing** on the write side. "
            "**Don't overuse** — simple CRUD apps don't need CQRS. Good fit: complex domains, high read/write ratio mismatch, "
            "or when read models need different shape than write model."
        ),
        "code": """// MediatR CQRS — commands and queries separated
public record PlaceOrderCommand(int CustomerId, List<LineItemDto> Lines) : IRequest<int>;
public record GetOrderSummaryQuery(int OrderId) : IRequest<OrderSummaryDto?>;
public record GetOrdersByCustomerQuery(int CustomerId, int Page) : IRequest<PagedResult<OrderSummaryDto>>;

// Command handler — write model, transactional
public class PlaceOrderHandler(AppDbContext db) : IRequestHandler<PlaceOrderCommand, int>
{
    public async Task<int> Handle(PlaceOrderCommand cmd, CancellationToken ct)
    {
        var order = Order.Create(cmd.CustomerId, cmd.Lines);
        db.Orders.Add(order);
        await db.SaveChangesAsync(ct);
        return order.Id;
    }
}

// Query handler — read-optimized projection, AsNoTracking
public class GetOrderSummaryHandler(AppDbContext db) : IRequestHandler<GetOrderSummaryQuery, OrderSummaryDto?>
{
    public Task<OrderSummaryDto?> Handle(GetOrderSummaryQuery q, CancellationToken ct) =>
        db.Orders.AsNoTracking()
            .Where(o => o.Id == q.OrderId)
            .Select(o => new OrderSummaryDto(o.Id, o.CustomerName, o.Total, o.Status))
            .FirstOrDefaultAsync(ct);
}""",
        "language": "csharp",
        "key_points": [
            "Separate models for read vs write",
            "MediatR IRequest/IRequestHandler per use case",
            "Scale reads independently (replicas, cache, Elasticsearch)",
            "Pairs well with Event Sourcing",
            "Avoid for simple CRUD — adds complexity",
        ],
    },
    "event-sourcing": {
        "explanation": (
            "**Event Sourcing** stores application state as a sequence of **domain events** (append-only log) rather than "
            "updating rows in place. Current state is derived by **replaying events**. Benefits: complete **audit trail**, "
            "temporal queries (\"what was the balance on date X?\"), **event-driven integrations** (publish events to Service Bus). "
            "**Projections** build read models asynchronously. **Snapshots** prevent replaying thousands of events. "
            "Challenges: eventual consistency on read side, schema evolution of events, storage growth. "
            "Use with CQRS — event store on write, projections on read."
        ),
        "code": """// Domain events
public record OrderCreated(Guid OrderId, int CustomerId, decimal Total, DateTime At);
public record OrderLineAdded(Guid OrderId, string Sku, int Qty, decimal Price);
public record OrderCancelled(Guid OrderId, string Reason, DateTime At);

// Aggregate — applies events to mutate state
public class OrderAggregate
{
    public Guid Id { get; private set; }
    public OrderStatus Status { get; private set; }
    private readonly List<object> _uncommitted = [];

    public void Cancel(string reason)
    {
        if (Status == OrderStatus.Cancelled) throw new InvalidOperationException("Already cancelled");
        Apply(new OrderCancelled(Id, reason, DateTime.UtcNow));
    }

    private void Apply(object e)
    {
        _uncommitted.Add(e);
        switch (e) // mutate state
        {
            case OrderCreated c: Id = c.OrderId; Status = OrderStatus.Active; break;
            case OrderCancelled: Status = OrderStatus.Cancelled; break;
        }
    }

    public IReadOnlyList<object> GetUncommittedEvents() => _uncommitted;
}

// Event store append + projection worker updates read DB""",
        "language": "csharp",
        "key_points": [
            "Append-only event log — never update/delete events",
            "Replay rebuilds state; snapshots for performance",
            "Projections build CQRS read models",
            "Event schema versioning (upcasters) required",
            "Natural audit trail and integration point",
        ],
    },
    "ddd-bounded-contexts": {
        "explanation": (
            "In **Domain-Driven Design (DDD)**, a **bounded context** is an explicit boundary where a particular domain model "
            "and **ubiquitous language** apply consistently. The same word (\"Customer\") may mean different things in "
            "**Sales** vs **Support** contexts. Bounded contexts guide **microservice decomposition** — one service per context, "
            "each with its own database. Contexts integrate via **domain events**, **ACL (Anti-Corruption Layer)**, or "
            "**published language**. Draw a **context map** showing relationships: upstream/downstream, shared kernel, conformist."
        ),
        "code": """/*
  Context Map (interview whiteboard)

  ┌─────────────────┐     events      ┌─────────────────┐
  │  Orders Context │ ──────────────► │ Billing Context │
  │  Order, Line    │  OrderPlaced    │ Invoice, Payment│
  │  PlaceOrder     │                 │ ChargeCustomer  │
  └────────┬────────┘                 └─────────────────┘
           │ ACL (anti-corruption layer)
           ▼
  ┌─────────────────┐
  │ Legacy ERP      │  ← translate ERP model to Order model
  │ (external)      │     don't leak ERP concepts into Orders
  └─────────────────┘

  Rules:
  - One database per bounded context (no shared tables)
  - Ubiquitous language within context only
  - Integration via events or API + ACL
*/

// Orders service knows nothing about Invoice entity
public record OrderPlacedIntegrationEvent(int OrderId, decimal Total, int CustomerId);""",
        "language": "text",
        "key_points": [
            "Explicit boundary for consistent domain model",
            "Same term, different meaning across contexts",
            "Microservice boundaries align with bounded contexts",
            "Anti-corruption layer protects your model",
            "Context map documents integration relationships",
        ],
    },
    "repository-pattern": {
        "explanation": (
            "The **Repository pattern** mediates between the **domain layer** and **data mapping layer** — presents a "
            "collection-like interface for domain objects. Domain/services depend on `IOrderRepository`, not `DbContext` directly. "
            "Benefits: **testability** (mock repos), **swappable persistence**, **centralized query logic**. "
            "**Pitfalls:** generic `IRepository<T>` with 20 methods becomes a leaky abstraction; "
            "exposing `IQueryable` defeats encapsulation. Prefer **specific repositories** with meaningful methods "
            "(`GetOpenOrdersForCustomerAsync`). With EF Core, repository is thin — mostly wraps DbSet operations."
        ),
        "code": """// Specific repository — meaningful methods, not generic CRUD god-interface
public interface IOrderRepository
{
    Task<Order?> GetByIdAsync(int id, CancellationToken ct);
    Task<IReadOnlyList<Order>> GetOpenByCustomerAsync(int customerId, CancellationToken ct);
    Task AddAsync(Order order, CancellationToken ct);
    Task SaveChangesAsync(CancellationToken ct);
}

public class OrderRepository(AppDbContext db) : IOrderRepository
{
    public Task<Order?> GetByIdAsync(int id, CancellationToken ct) =>
        db.Orders.Include(o => o.Lines).FirstOrDefaultAsync(o => o.Id == id, ct);

    public async Task<IReadOnlyList<Order>> GetOpenByCustomerAsync(int customerId, CancellationToken ct) =>
        await db.Orders.AsNoTracking()
            .Where(o => o.CustomerId == customerId && o.Status == OrderStatus.Open)
            .ToListAsync(ct);

    public Task AddAsync(Order order, CancellationToken ct)
    {
        db.Orders.Add(order);
        return Task.CompletedTask;
    }

    public Task SaveChangesAsync(CancellationToken ct) => db.SaveChangesAsync(ct);
}

// Unit test — mock IOrderRepository, not DbContext
var repo = new Mock<IOrderRepository>();
repo.Setup(r => r.GetByIdAsync(1, It.IsAny<CancellationToken>())).ReturnsAsync(testOrder);""",
        "language": "csharp",
        "key_points": [
            "Abstraction over data access for testability",
            "Specific repos over generic IRepository<T>",
            "Don't expose IQueryable to callers",
            "Unit of Work pattern often pairs with Repository",
            "With EF Core, keep repos thin — don't re-implement ORM",
        ],
    },
    "mediator-pattern-mediatr": {
        "explanation": (
            "The **Mediator pattern** decouples request senders from handlers — objects don't reference each other directly. "
            "**MediatR** is the popular .NET library implementing mediator + CQRS. Each command/query is a record; one **handler** "
            "per request. **Pipeline behaviors** wrap handlers for cross-cutting concerns: validation, logging, transactions, caching. "
            "Controllers become thin — `_mediator.Send(command)`. Benefits: **single responsibility**, **easy testing** (test handler in isolation), "
            "organized use cases. Register with `AddMediatR(cfg => cfg.RegisterServicesFromAssembly(...))`."
        ),
        "code": """// Install: MediatR + MediatR.Extensions.Microsoft.DependencyInjection

// Command + handler
public record CancelOrderCommand(int OrderId, string Reason) : IRequest;

public class CancelOrderHandler(IOrderRepository repo, ILogger<CancelOrderHandler> log)
    : IRequestHandler<CancelOrderCommand>
{
    public async Task Handle(CancelOrderCommand cmd, CancellationToken ct)
    {
        var order = await repo.GetByIdAsync(cmd.OrderId, ct)
            ?? throw new NotFoundException(cmd.OrderId);
        order.Cancel(cmd.Reason);
        await repo.SaveChangesAsync(ct);
        log.LogInformation("Order {OrderId} cancelled", cmd.OrderId);
    }
}

// Pipeline behavior — validation before handler
public class ValidationBehavior<TRequest, TResponse>(IEnumerable<IValidator<TRequest>> validators)
    : IPipelineBehavior<TRequest, TResponse> where TRequest : notnull
{
    public async Task<TResponse> Handle(TRequest req, RequestHandlerDelegate<TResponse> next, CancellationToken ct)
    {
        var failures = validators.Select(v => v.Validate(req)).SelectMany(r => r.Errors).Where(f => f is not null);
        if (failures.Any()) throw new ValidationException(failures);
        return await next();
    }
}

// Controller
[HttpPost("{id}/cancel")]
public async Task<IActionResult> Cancel(int id, [FromBody] CancelRequest body)
{
    await _mediator.Send(new CancelOrderCommand(id, body.Reason));
    return NoContent();
}""",
        "language": "csharp",
        "key_points": [
            "One handler per command/query — single responsibility",
            "Pipeline behaviors for validation, logging, transactions",
            "Controllers/services call _mediator.Send()",
            "Pairs naturally with CQRS",
            "Test handlers directly without HTTP layer",
        ],
    },
    "cap-theorem": {
        "explanation": (
            "The **CAP theorem** states a distributed system during a **network partition** must choose between "
            "**Consistency** (all nodes see same data) and **Availability** (every request gets a response). "
            "**Partition tolerance** is non-negotiable in distributed/cloud systems — networks fail. "
            "**CP systems** (e.g., Azure SQL with strong consistency) may reject writes during partition. "
            "**AP systems** (e.g., Cosmos DB with eventual consistency) stay available but reads may be stale. "
            "**PACELC** extends: else (no partition), choose Latency vs Consistency. Interview: justify your "
            "consistency choice for a catalog vs payment system."
        ),
        "code": """/*
  Interview examples:

  Payment service (CP):
  - Strong consistency required — never double-charge
  - Azure SQL with SERIALIZABLE or optimistic concurrency (RowVersion)
  - Accept brief unavailability over wrong balance

  Product catalog (AP):
  - Eventual consistency OK — stale price for 30s acceptable
  - Cosmos DB session consistency + Redis cache
  - Always available for browsing

  Order status read model (PC/EL):
  - Event sourcing projection — eventually consistent with write side
  - Display "Processing..." until projection catches up

  Partition scenario:
  East and West regions lose network link
  CP: one side stops accepting writes (split-brain prevention)
  AP: both accept writes → conflict resolution needed later
*/""",
        "language": "text",
        "key_points": [
            "Partition tolerance is mandatory in cloud",
            "CP vs AP — pick based on business requirement",
            "PACELC: else choose latency vs consistency",
            "Payments = consistency; catalog = availability",
            "Don't claim 'CA' — partitions happen",
        ],
    },
    "idempotency": {
        "explanation": (
            "**Idempotency** means performing the same operation multiple times produces the same result as once. "
            "Critical for **HTTP retries**, **message queue consumers** (at-least-once delivery), and **webhook handlers**. "
            "GET, PUT, DELETE are naturally idempotent; **POST is not** — use **Idempotency-Key** header. "
            "Store processed keys with response in Redis/SQL; return cached response on duplicate. "
            "Message consumers check processed message IDs. Database **upserts** and **unique constraints** prevent duplicates."
        ),
        "code": """// Idempotent POST with Idempotency-Key header
[HttpPost]
public async Task<IActionResult> CreateOrder(
    [FromBody] CreateOrderDto dto,
    [FromHeader(Name = "Idempotency-Key")] string idempotencyKey,
    CancellationToken ct)
{
    if (string.IsNullOrWhiteSpace(idempotencyKey))
        return BadRequest("Idempotency-Key header required");

    var cacheKey = $"idempotency:{idempotencyKey}";
    var cached = await _cache.GetStringAsync(cacheKey, ct);
    if (cached is not null)
    {
        var prior = JsonSerializer.Deserialize<CachedResponse>(cached)!;
        return StatusCode(prior.StatusCode, prior.Body);
    }

    var order = await _service.CreateAsync(dto, ct);
    var response = new { order.Id, order.Status };
    await _cache.SetStringAsync(cacheKey,
        JsonSerializer.Serialize(new CachedResponse(201, response)),
        new DistributedCacheEntryOptions { AbsoluteExpirationRelativeToNow = TimeSpan.FromHours(24) }, ct);

    return CreatedAtAction(nameof(Get), new { id = order.Id }, response);
}

// Message consumer — deduplicate by MessageId
if (await _processedStore.ExistsAsync(message.MessageId)) return;
await _handler.HandleAsync(message);
await _processedStore.MarkProcessedAsync(message.MessageId);""",
        "language": "csharp",
        "key_points": [
            "POST needs Idempotency-Key for safe retries",
            "At-least-once messaging requires idempotent consumers",
            "Store key + response; return same result on replay",
            "Unique DB constraints as last line of defense",
            "Stripe and payment APIs mandate idempotency keys",
        ],
    },
    "rest-api-design": {
        "explanation": (
            "**REST API design** best practices for production .NET APIs: use **resource nouns** (not verbs), correct **HTTP methods** "
            "and **status codes**, **consistent versioning** (/v1/ or Accept header), **pagination** (cursor preferred for large sets), "
            "**filtering/sorting** via query params, **RFC 7807 Problem Details** for errors, **HATEOAS** optional. "
            "Use **DTOs** not entity models in responses. Support **PATCH** for partial updates. "
            "Document with **OpenAPI/Swagger**. Enforce **rate limiting** and **CORS** allowlists."
        ),
        "code": """// Well-designed REST controller
[ApiController]
[Route("api/v1/orders")]
public class OrdersController(IOrderService service) : ControllerBase
{
    [HttpGet]
    public async Task<ActionResult<PagedResult<OrderSummaryDto>>> List(
        [FromQuery] int page = 1,
        [FromQuery] int pageSize = 20,
        [FromQuery] string? status = null)
        => Ok(await service.ListAsync(page, pageSize, status));

    [HttpGet("{id:int}")]
    [ProducesResponseType(typeof(OrderDetailDto), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(ProblemDetails), StatusCodes.Status404NotFound)]
    public async Task<ActionResult<OrderDetailDto>> Get(int id)
        => await service.GetAsync(id) is { } order ? Ok(order) : NotFound();

    [HttpPost]
    [ProducesResponseType(typeof(OrderDetailDto), StatusCodes.Status201Created)]
    [ProducesResponseType(typeof(ValidationProblemDetails), StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<OrderDetailDto>> Create([FromBody] CreateOrderDto dto)
    {
        var order = await service.CreateAsync(dto);
        return CreatedAtAction(nameof(Get), new { id = order.Id }, order);
    }

    [HttpPatch("{id:int}")]
    public async Task<ActionResult<OrderDetailDto>> Patch(int id, [FromBody] JsonPatchDocument<UpdateOrderDto> patch)
        => Ok(await service.PatchAsync(id, patch));
}

// Error response (RFC 7807) — automatic with [ApiController] + ProblemDetails""",
        "language": "csharp",
        "key_points": [
            "Nouns in URLs; HTTP verbs for actions",
            "201 Created + Location header on POST",
            "Cursor pagination for large datasets",
            "Problem Details (RFC 7807) for consistent errors",
            "Version via URL path or header — be consistent",
        ],
    },
    "api-security-best-practices": {
        "explanation": (
            "**API security** layers: **transport** (HTTPS/TLS 1.2+), **authentication** (OAuth2/OIDC JWT, API keys for internal), "
            "**authorization** (RBAC, policies, resource-based), **input validation**, **rate limiting**, **CORS allowlist**, "
            "**security headers** (HSTS, X-Content-Type-Options). Never expose stack traces. Store secrets in Key Vault. "
            "Validate JWT issuer/audience/signature/expiry. Use **least privilege** scopes. Log security events without logging tokens. "
            "**OWASP API Security Top 10** is the checklist interviewers expect."
        ),
        "code": """// Program.cs — security middleware stack
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(o =>
    {
        o.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            ClockSkew = TimeSpan.FromMinutes(1)
        };
    });

builder.Services.AddRateLimiter(o =>
{
    o.AddFixedWindowLimiter("api", f =>
    {
        f.Window = TimeSpan.FromMinutes(1);
        f.PermitLimit = 100;
        f.QueueLimit = 0;
    });
});

builder.Services.AddHsts(o => o.MaxAge = TimeSpan.FromDays(365));

var app = builder.Build();
app.UseHsts();
app.UseHttpsRedirection();
app.UseAuthentication();
app.UseAuthorization();
app.UseRateLimiter();

// CORS — explicit allowlist, never * with credentials
app.UseCors(p => p.WithOrigins("https://app.example.com").AllowAnyHeader().AllowAnyMethod());""",
        "language": "csharp",
        "key_points": [
            "HTTPS everywhere; HSTS in production",
            "Validate JWT fully — issuer, audience, expiry",
            "Rate limiting prevents abuse",
            "CORS allowlist — not wildcard in prod",
            "Never log tokens, passwords, or PII unnecessarily",
        ],
    },
    "owasp-top-10": {
        "explanation": (
            "The **OWASP Top 10** lists the most critical web application security risks. For .NET APIs, focus on: "
            "**A01 Broken Access Control** — verify user owns resource; **A02 Cryptographic Failures** — TLS, hash passwords with bcrypt/Argon2; "
            "**A03 Injection** — parameterized queries (EF Core default); **A05 Security Misconfiguration** — disable debug in prod; "
            "**A06 Vulnerable Components** — Dependabot/NuGet audit; **A07 Auth Failures** — MFA, secure session; "
            "**A09 Logging Failures** — audit security events. Demonstrate concrete mitigations in code, not just names."
        ),
        "code": """// A01 — Broken Access Control: verify ownership
[Authorize]
[HttpGet("{id}")]
public async Task<IActionResult> GetOrder(int id)
{
    var order = await _repo.GetAsync(id);
    if (order is null) return NotFound();
    if (order.CustomerId != User.GetCustomerId()) return Forbid(); // not 404 — avoid enumeration
    return Ok(order);
}

// A03 — Injection: EF Core parameterized (never string concat SQL)
var orders = await _db.Orders
    .Where(o => o.CustomerName == customerName) // safe
    .ToListAsync();
// BAD: _db.Database.ExecuteSqlRaw($"SELECT * FROM Orders WHERE Name = '{name}'");

// A02 — Secrets: Key Vault, not appsettings
var key = builder.Configuration["Jwt:SigningKey"]; // from Key Vault provider

// A06 — vulnerable packages: dotnet list package --vulnerable""",
        "language": "csharp",
        "key_points": [
            "A01 Access Control — #1 risk; check every endpoint",
            "A03 Injection — parameterized queries always",
            "A06 Vulnerable components — automate dependency scanning",
            "A05 Misconfiguration — secure defaults, no debug in prod",
            "A09 Logging — audit auth failures and admin actions",
        ],
    },
    "caching-strategies": {
        "explanation": (
            "Common **caching strategies**: **Cache-aside (lazy loading)** — app checks cache, on miss reads DB and populates cache; "
            "most common pattern. **Read-through** — cache layer loads from DB transparently. **Write-through** — write to cache and DB "
            "synchronously. **Write-behind (write-back)** — write cache first, async flush to DB (risky). **Cache invalidation** on "
            "updates prevents stale data. Use **TTL** on all keys. **Redis** for distributed; **IMemoryCache** for single instance. "
            "Watch **cache stampede** — use locking or probabilistic early expiration."
        ),
        "code": """// Cache-aside pattern with IDistributedCache (Redis)
public class OrderQueryService(AppDbContext db, IDistributedCache cache)
{
    public async Task<OrderDto?> GetOrderAsync(int id, CancellationToken ct)
    {
        var key = $"order:{id}";
        var cached = await cache.GetStringAsync(key, ct);
        if (cached is not null)
            return JsonSerializer.Deserialize<OrderDto>(cached);

        var order = await db.Orders.AsNoTracking()
            .Where(o => o.Id == id)
            .Select(o => new OrderDto(o.Id, o.CustomerName, o.Total))
            .FirstOrDefaultAsync(ct);

        if (order is not null)
        {
            await cache.SetStringAsync(key, JsonSerializer.Serialize(order),
                new DistributedCacheEntryOptions
                {
                    AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5)
                }, ct);
        }
        return order;
    }

    // Invalidate on update
    public async Task UpdateOrderAsync(int id, UpdateOrderDto dto, CancellationToken ct)
    {
        await /* ... update DB ... */;
        await cache.RemoveAsync($"order:{id}", ct);
    }
}""",
        "language": "csharp",
        "key_points": [
            "Cache-aside most common — app manages cache",
            "Always set TTL to prevent unbounded growth",
            "Invalidate or update cache on writes",
            "Redis for multi-instance; IMemoryCache for single node",
            "Cache stampede: lock or stagger expiration",
        ],
    },
    "feature-flags": {
        "explanation": (
            "**Feature flags (feature toggles)** decouple **deployment from release** — ship code dark, enable for users when ready. "
            "Use cases: **gradual rollout** (5% → 100%), **A/B testing**, **kill switches** for bad features, **tenant-specific** features. "
            "**Microsoft.FeatureManagement** integrates with ASP.NET Core and **Azure App Configuration** for centralized, "
            "dynamic flags without redeploy. Remove stale flags after full rollout to avoid technical debt."
        ),
        "code": """// NuGet: Microsoft.FeatureManagement.AspNetCore
builder.Services.AddFeatureManagement(builder.Configuration);
// Or: AddFeatureManagement().AddFeatureFilter<PercentageFilter>();

[HttpGet("reports/advanced")]
public async Task<IActionResult> AdvancedReport()
{
    if (await _featureManager.IsEnabledAsync("AdvancedReporting"))
        return Ok(await _reportService.GenerateAdvancedAsync());
    return NotFound();
}

// Feature gate attribute
[FeatureGate("BetaCheckout")]
[HttpPost("checkout/v2")]
public async Task<IActionResult> CheckoutV2([FromBody] CheckoutDto dto)
    => Ok(await _checkoutV2.ProcessAsync(dto));

// appsettings.json
// "FeatureManagement": {
//   "AdvancedReporting": true,
//   "BetaCheckout": { "EnabledFor": [{ "Name": "Percentage", "Parameters": { "Value": 10 } }] }
// }

// Azure App Configuration — refresh flags without restart
builder.Configuration.AddAzureAppConfiguration(o => o.Connect(connStr).UseFeatureFlags());""",
        "language": "csharp",
        "key_points": [
            "Decouple deploy from release",
            "Percentage rollout for canary at app level",
            "Azure App Configuration for centralized management",
            "Kill switch disables bad features instantly",
            "Remove flags after 100% rollout — avoid debt",
        ],
    },
    "observability-three-pillars": {
        "explanation": (
            "**Observability** is the ability to understand system internal state from external outputs. Three pillars: "
            "**Logs** — discrete timestamped events (structured JSON preferred); **Metrics** — numeric aggregates over time "
            "(request rate, error rate, latency histograms); **Traces** — request journey across services with **spans** and "
            "**correlation IDs**. OpenTelemetry is the vendor-neutral standard; export to Azure Monitor, Jaeger, or Grafana. "
            "**RED method** for services: Rate, Errors, Duration. **USE method** for resources: Utilization, Saturation, Errors."
        ),
        "code": """// OpenTelemetry — logs, metrics, traces unified
builder.Logging.AddOpenTelemetry(o => o.IncludeFormattedMessage = true);

builder.Services.AddOpenTelemetry()
    .WithTracing(t => t
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddEntityFrameworkCoreInstrumentation()
        .AddSource("OrderService"))
    .WithMetrics(m => m
        .AddAspNetCoreInstrumentation()
        .AddRuntimeInstrumentation())
    .UseAzureMonitor();

// Structured log — auto-correlated with trace
public class OrderService(ILogger<OrderService> logger, ActivitySource activitySource)
{
    public async Task PlaceOrderAsync(Order order)
    {
        using var activity = activitySource.StartActivity("PlaceOrder");
        activity?.SetTag("order.id", order.Id);

        logger.LogInformation("Placing order {OrderId} for {CustomerId}", order.Id, order.CustomerId);
        // TraceId and SpanId injected into log scope automatically
    }
}

// Propagate correlation ID in HTTP calls
client.DefaultRequestHeaders.Add("X-Correlation-Id", Activity.Current?.Id ?? Guid.NewGuid().ToString());""",
        "language": "csharp",
        "key_points": [
            "Logs + Metrics + Traces — not just logging",
            "Structured logging (message templates, not interpolation)",
            "Correlation ID links logs across microservices",
            "RED: Rate, Errors, Duration for every service",
            "OpenTelemetry → Azure Monitor / Grafana / Jaeger",
        ],
    },
    "git-workflow": {
        "explanation": (
            "**Trunk-based development** — developers merge small changes to `main` frequently (daily) via short-lived feature "
            "branches (< 2 days). Requires **feature flags** and strong CI. Enables **continuous delivery**. "
            "**GitFlow** — long-lived `develop`, `release/*`, `hotfix/*` branches; suits scheduled releases but slower feedback. "
            "**GitHub Flow** — simpler: main + feature branches + PR. Use **branch policies**: require PR reviews, passing builds, "
            "no direct push to main. **Conventional commits** aid changelog generation."
        ),
        "code": """# Trunk-based (recommended for CI/CD)
git checkout main && git pull
git checkout -b feat/order-cancel
# small focused change, < 400 lines
git commit -m "feat(orders): add cancel endpoint with validation"
git push -u origin feat/order-cancel
gh pr create --title "Add order cancel endpoint" --body "Closes #1042"

# After review + green CI → squash merge to main
# Deploy pipeline triggers on main

# GitFlow (scheduled releases)
git checkout develop
git checkout -b feature/order-cancel
# merge to develop → release/1.4 branch → merge to main + develop

# Conventional commits: feat|fix|docs|refactor|test|chore(scope): message""",
        "language": "bash",
        "key_points": [
            "Trunk-based enables continuous delivery",
            "Short-lived branches (< 2 days) reduce merge pain",
            "Protect main with branch policies and required reviews",
            "GitFlow for scheduled release trains",
            "Conventional commits for automated changelogs",
        ],
    },
    "code-review-best-practices": {
        "explanation": (
            "Effective **code reviews** improve quality, spread knowledge, and catch bugs early. **Authors**: keep PRs small "
            "(< 400 lines), self-review first, link work item, add context in description. **Reviewers**: check correctness, "
            "security, tests, naming — not bike-shedding style. Ask questions; suggest, don't demand (unless blocking). "
            "Review within **24 hours**. Use **automated checks** (linters, SAST, tests) so humans focus on design and logic. "
            "Approve when you'd be comfortable maintaining the code."
        ),
        "code": """/*
  PR Description template:
  ## What
  Add order cancellation endpoint with refund trigger

  ## Why
  Closes #1042 — customers need to cancel within 30 min

  ## How to test
  1. POST /api/v1/orders/42/cancel with Idempotency-Key
  2. Verify refund event published to Service Bus

  ## Checklist
  - [x] Unit tests added
  - [x] No secrets in code
  - [x] Swagger updated

  Reviewer checklist:
  □ Business logic correct? Edge cases (already shipped, expired window)?
  □ Authorization — can user cancel this order?
  □ Tests cover happy path + failure cases?
  □ Database migration backward compatible?
  □ Performance — N+1 queries? Missing indexes?

  Feedback style:
  ✅ "Consider extracting validation to OrderValidator — reused in PlaceOrder too"
  ❌ "Wrong indentation on line 42"
     (let linter handle formatting)
*/""",
        "language": "text",
        "key_points": [
            "Small PRs review faster and merge safer",
            "Automate style/formatting — focus on logic and design",
            "Review within 24h SLA",
            "Ask questions; be constructive not gatekeeping",
            "Security + authorization checks on every endpoint",
        ],
    },
    "circuit-breaker-pattern": {
        "explanation": (
            "The **Circuit Breaker** prevents cascading failures when a downstream dependency is unhealthy. States: "
            "**Closed** (normal — requests pass through), **Open** (fail fast — don't call failing service), "
            "**Half-Open** (probe with limited requests to test recovery). After N failures in window, circuit opens for "
            "cooldown period. Combine with **timeout** and **retry** (retry only when circuit closed). "
            "**Polly v8** uses `ResiliencePipeline` with circuit breaker, retry, timeout, hedging strategies."
        ),
        "code": """// Polly v8 — ResiliencePipeline for HttpClient
builder.Services.AddHttpClient<IPaymentGateway, StripeGateway>()
    .AddResilienceHandler("stripe", builder =>
    {
        builder.AddRetry(new RetryStrategyOptions<HttpResponseMessage>
        {
            MaxRetryAttempts = 2,
            Delay = TimeSpan.FromSeconds(1),
            BackoffType = DelayBackoffType.Exponential,
            ShouldHandle = new PredicateBuilder<HttpResponseMessage>()
                .HandleResult(r => (int)r.StatusCode >= 500)
        });
        builder.AddCircuitBreaker(new CircuitBreakerStrategyOptions<HttpResponseMessage>
        {
            FailureRatio = 0.5,
            MinimumThroughput = 10,
            BreakDuration = TimeSpan.FromSeconds(30),
            ShouldHandle = new PredicateBuilder<HttpResponseMessage>()
                .HandleResult(r => (int)r.StatusCode >= 500)
                .Handle<HttpRequestException>()
        });
        builder.AddTimeout(TimeSpan.FromSeconds(10));
    });

// When circuit open — fail fast, return fallback or cached response
// Half-open: allow 1 probe request; success → closed, failure → open again""",
        "language": "csharp",
        "key_points": [
            "Closed → Open → Half-Open state machine",
            "Fail fast when dependency is down — protect your service",
            "Combine circuit breaker + retry + timeout",
            "Polly v8 ResiliencePipeline in .NET 8",
            "Return graceful degradation when circuit open",
        ],
    },
    "twelve-factor-app": {
        "explanation": (
            "The **Twelve-Factor App** methodology defines best practices for **cloud-native SaaS apps**. Key factors for .NET on Azure: "
            "**I. Codebase** — one repo per app; **II. Dependencies** — explicit in csproj/NuGet; **III. Config** — environment variables / "
            "Key Vault, not appsettings secrets; **IV. Backing services** — SQL/Redis as attached resources; **VI. Processes** — stateless, "
            "share nothing (session in Redis); **IX. Disposability** — fast startup, graceful shutdown on SIGTERM; "
            "**XI. Logs** — stdout streams collected by Azure Monitor; **XII. Admin processes** — EF migrations as release task."
        ),
        "code": """/*
  Twelve-Factor mapping for .NET on Azure App Service:

  III. Config — Key Vault references, not hardcoded
  "ConnectionStrings__Sql": "@Microsoft.KeyVault(SecretUri=...)"

  VI. Processes — stateless API instances
  // Session in Redis, not in-memory
  builder.Services.AddStackExchangeRedisCache(...);
  builder.Services.AddSession();

  IX. Disposability — handle SIGTERM gracefully
  builder.Services.Configure<HostOptions>(o => o.ShutdownTimeout = TimeSpan.FromSeconds(30));
  // Finish in-flight requests before shutdown (Kestrel default)

  XI. Logs — structured to stdout → App Insights
  builder.Logging.AddConsole(); // Azure collects stdout

  XII. Admin — migration as pipeline step
  # azure-pipelines.yml
  - script: dotnet ef database update --connection "$(SqlConnection)"
    displayName: Run EF migrations
*/

// Port binding — Kestrel binds PORT env var in containers
// EXPOSE 8080 in Dockerfile; App Service sets PORT automatically""",
        "language": "text",
        "key_points": [
            "Config in environment / Key Vault — not source code",
            "Stateless processes — externalize session state",
            "Logs as event streams to stdout / Azure Monitor",
            "Disposability — fast startup, graceful SIGTERM handling",
            "Dev/prod parity — same containers, same services",
        ],
    },
    "blue-green-deployment": {
        "explanation": (
            "**Blue-green deployment** maintains two identical production environments. **Blue** serves live traffic; deploy new version to "
            "**Green**, run smoke/integration tests, then **switch traffic** (instant cutover). Rollback = switch back to Blue. "
            "On Azure: **App Service deployment slots** (staging = green), **AKS** with two deployments + service selector, "
            "**Front Door** origin switch. Requires **backward-compatible database migrations** (expand-contract pattern) "
            "since both versions may run briefly during transition."
        ),
        "code": """# Azure App Service blue-green with slots
# Blue = production slot, Green = staging slot

# 1. Deploy to staging (green)
az webapp deployment source config-zip \\
  --resource-group rg-prod \\
  --name order-api \\
  --slot staging \\
  --src ./publish.zip

# 2. Smoke test staging URL
curl -f https://order-api-staging.azurewebsites.net/health
curl -f https://order-api-staging.azurewebsites.net/api/v1/orders/1

# 3. Swap — instant traffic switch (zero downtime)
az webapp deployment slot swap \\
  --resource-group rg-prod \\
  --name order-api \\
  --slot staging \\
  --target-slot production

# 4. Rollback if issues — swap again (seconds)
az webapp deployment slot swap --name order-api --slot staging

# Slot settings: stick to slot (DB connection for green testing) vs swap""",
        "language": "bash",
        "key_points": [
            "Two identical environments — instant switch",
            "App Service slots are built-in blue-green",
            "Smoke test green before swap",
            "Rollback is another swap — seconds not hours",
            "DB migrations must be backward compatible",
        ],
    },
    "canary-releases": {
        "explanation": (
            "**Canary releases** route a **small percentage of traffic** to the new version while the majority stays on stable. "
            "Monitor **error rate, latency, and business metrics** on the canary; gradually increase traffic (5% → 25% → 100%) "
            "or **automatic rollback** on SLO breach. Implement via **Front Door weighted routing**, **App Gateway**, "
            "**Istio/Linkerd** in AKS, or **feature flags** at application level. Safer than big-bang deploy — limits blast radius."
        ),
        "code": """// Application-level canary with feature flags + metrics
public class CheckoutController(IFeatureManager flags, IMetrics metrics) : ControllerBase
{
    [HttpPost("checkout")]
    public async Task<IActionResult> Checkout([FromBody] CheckoutDto dto)
    {
        var useV2 = await flags.IsEnabledAsync("CheckoutV2");
        var sw = Stopwatch.StartNew();
        try
        {
            var result = useV2
                ? await _checkoutV2.ProcessAsync(dto)
                : await _checkoutV1.ProcessAsync(dto);

            metrics.Record("checkout.success", 1, new TagList { { "version", useV2 ? "v2" : "v1" } });
            return Ok(result);
        }
        catch (Exception ex)
        {
            metrics.Record("checkout.error", 1, new TagList { { "version", useV2 ? "v2" : "v1" } });
            throw;
        }
        finally
        {
            metrics.Record("checkout.duration_ms", sw.ElapsedMilliseconds,
                new TagList { { "version", useV2 ? "v2" : "v1" } });
        }
    }
}

// Infrastructure canary: Front Door origin weights 95/5
// Alert if canary error rate > 2x stable → auto-set weight to 0""",
        "language": "csharp",
        "key_points": [
            "Small traffic % limits blast radius",
            "Monitor golden signals on canary vs stable",
            "Automated rollback on SLO breach",
            "Feature flags OR traffic routing — both valid",
            "Combine with blue-green for infra-level canary",
        ],
    },
    "technical-debt-management": {
        "explanation": (
            "**Technical debt** is the implied cost of future rework from choosing an easy solution now. "
            "Not all debt is bad — **conscious tradeoffs** for speed can be correct if tracked and repaid. "
            "Manage via: **debt register** in backlog (impact/effort), **allocate capacity** (10–20% sprint), "
            "**boy scout rule** (leave code cleaner), **strangler fig pattern** for legacy modules. "
            "Measure impact: increased bug rate, slower lead time, developer frustration. Communicate cost to stakeholders in business terms."
        ),
        "code": """/*
  Technical Debt Register (Azure Boards / Jira)

  | ID   | Description                    | Impact | Effort | Priority |
  |------|--------------------------------|--------|--------|----------|
  | TD-1 | OrderService god class 800 LOC | High   | 3 pts  | Sprint+1 |
  | TD-2 | No integration tests for pay   | High   | 5 pts  | Sprint+2 |
  | TD-3 | Deprecated Newtonsoft.Json     | Low    | 1 pt   | Backlog  |

  Strategies:
  1. 20% sprint capacity for debt (1 story per sprint minimum)
  2. Boy Scout Rule — improve one thing per PR touch
  3. Strangler fig — wrap legacy WCF, migrate endpoint by endpoint
  4. Definition of Done includes "no new debt without ticket"

  Refactoring during feature work:
  // Touching OrderService for cancel feature?
  // Extract CancelOrderHandler while you're there (same PR if < 50 lines)
*/

// SonarQube / CodeQL in CI — fail on new critical issues""",
        "language": "text",
        "key_points": [
            "Track debt explicitly — don't hide it",
            "Allocate 10–20% sprint capacity for repayment",
            "Boy Scout Rule on every touch",
            "Strangler fig for legacy migration",
            "Measure: bugs, lead time, code churn",
        ],
    },
    "agile-scrum": {
        "explanation": (
            "**Agile** values working software, customer collaboration, and responding to change. **Scrum** is a framework: "
            "**Sprints** (1–4 weeks, usually 2), fixed increment delivery. **Ceremonies**: Sprint Planning (what to build), "
            "Daily Standup (15 min sync), Sprint Review (demo to stakeholders), Retrospective (improve process). "
            "**Artifacts**: Product Backlog (prioritized by PO), Sprint Backlog (committed work), Increment (done software). "
            "**Roles**: Product Owner (what), Scrum Master (process), Development Team (how). **Definition of Done** ensures quality."
        ),
        "code": """/*
  Sprint timeline (2 weeks):

  Day 1:  Sprint Planning — select stories, define sprint goal
  Daily:  Standup 15 min — yesterday / today / blockers
  Day 10: Sprint Review — demo working increment to stakeholders
  Day 10: Retrospective — Start/Stop/Continue, action items

  User Story format:
  "As a customer, I want to cancel my order within 30 minutes,
   so that I can change my mind before shipping."

  Story points (Fibonacci: 1,2,3,5,8,13):
  - Relative complexity, NOT hours
  - Team velocity = avg points completed per sprint

  Definition of Done:
  □ Code complete + peer reviewed
  □ Unit tests passing
  □ Deployed to staging
  □ Acceptance criteria met
  □ Documentation updated

  Kanban alternative: continuous flow, WIP limits, no fixed sprints
*/""",
        "language": "text",
        "key_points": [
            "Sprint Planning, Standup, Review, Retro — four ceremonies",
            "User stories: As a [role], I want [goal], so that [benefit]",
            "Story points measure complexity not hours",
            "Definition of Done ensures consistent quality",
            "Scrum Master removes impediments, protects team focus",
        ],
    },
    "pair-programming": {
        "explanation": (
            "**Pair programming** — two developers at one workstation: **Driver** writes code, **Navigator** reviews, thinks ahead, "
            "checks logic. Benefits: **knowledge sharing**, **fewer defects**, **faster onboarding**, **collective ownership**. "
            "Styles: **Driver-Navigator** (classic), **Ping-Pong TDD** (one writes test, other implements), "
            "**Mob programming** (whole team, rotating driver). Remote: VS Code Live Share, timed role swaps every 25 min. "
            "Best for: complex features, critical production bugs, onboarding juniors, architectural decisions."
        ),
        "code": """/*
  Pair programming session — Cancel Order feature

  Driver: implements CancelOrderHandler
  Navigator: asks "What if order already shipped?" "Is this idempotent?"

  Ping-Pong TDD flow:
  1. Navigator writes failing test: CancelOrder_AlreadyShipped_Throws
  2. Driver implements minimum code to pass
  3. Driver writes test: CancelOrder_WithinWindow_PublishesRefundEvent
  4. Navigator implements
  5. Refactor together

  Remote setup:
  - VS Code Live Share or Tuple
  - Timer: swap roles every 25 minutes (Pomodoro)
  - Shared branch: pair/1042-cancel-order

  When NOT to pair:
  - Simple CRUD with clear spec (solo faster)
  - Exploratory spike (solo research, pair to implement)

  Interview: "Pairing on payment integration caught a race condition
  in idempotency check that solo review missed."
*/""",
        "language": "text",
        "key_points": [
            "Driver + Navigator roles — rotate frequently",
            "Not 2x cost — often faster with higher quality",
            "Ping-Pong TDD effective for test-driven work",
            "Mob programming for complex architectural decisions",
            "Remote: Live Share + timed role swaps",
        ],
    },
    "sre-practices": {
        "explanation": (
            "**Site Reliability Engineering (SRE)** applies software engineering to operations. Core concepts: "
            "**SLI** (metric — e.g., p99 latency), **SLO** (target — 99.9% requests < 500ms), **SLA** (contract with penalties), "
            "**Error budget** (100% - SLO = allowed unreliability). When budget exhausted, **freeze features** and focus on reliability. "
            "Reduce **toil** (manual repetitive ops) via automation. **Blameless postmortems** after incidents: timeline, root cause, action items. "
            "On-call rotations with runbooks and escalation paths."
        ),
        "code": """/*
  SLO definition for Order API:

  SLI: HTTP request latency (excluding 4xx)
  SLO: 99.9% of requests complete in < 500ms over 30-day window
  Error budget: 0.1% = 43.2 minutes of bad requests/month

  Burn rate alert:
  - 14.4x burn rate over 1h → page on-call (budget exhausted in 2 days)
  - 6x burn rate over 6h → ticket (budget exhausted in 5 days)

  Blameless postmortem template:
  1. Incident summary (what users experienced)
  2. Timeline (UTC)
  3. Root cause (5 whys)
  4. What went well / what didn't
  5. Action items with owners and due dates
  6. Lessons learned (no blame assignment)

  Toil reduction:
  - Automate deployment (was manual FTP → Azure DevOps pipeline)
  - Automate certificate renewal (was calendar reminder → managed cert)
  - Self-service dashboards instead of manual SQL queries
*/

// SLI measurement with OpenTelemetry
// histogram: http.server.request.duration
// SLO dashboard in Azure Monitor workbook or Grafana""",
        "language": "text",
        "key_points": [
            "SLI → SLO → error budget → engineering decisions",
            "Error budget exhausted = reliability over features",
            "Blameless postmortems — focus on systems not people",
            "Reduce toil through automation",
            "On-call runbooks and escalation paths required",
        ],
    },
    "retry-policies-polly": {
        "explanation": (
            "**Retry policies** automatically re-attempt failed operations for **transient errors** — HTTP 503, timeout, "
            "connection reset. Use **exponential backoff with jitter** to avoid thundering herd. "
            "**Only retry idempotent operations** — or use idempotency keys. Don't retry 400/401/404. "
            "**Polly v8** (`Microsoft.Extensions.Resilience`) provides `ResiliencePipeline` combining retry, circuit breaker, "
            "timeout, and hedging. Register on `HttpClient` via `AddResilienceHandler`. Max retry attempts typically 3."
        ),
        "code": """// Polly v8 — retry with exponential backoff + jitter
builder.Services.AddHttpClient<IInventoryClient, InventoryClient>()
    .AddResilienceHandler("inventory", pipeline =>
    {
        pipeline.AddRetry(new RetryStrategyOptions<HttpResponseMessage>
        {
            MaxRetryAttempts = 3,
            Delay = TimeSpan.FromSeconds(2),
            MaxDelay = TimeSpan.FromSeconds(30),
            BackoffType = DelayBackoffType.Exponential,
            UseJitter = true,
            ShouldHandle = new PredicateBuilder<HttpResponseMessage>()
                .HandleResult(r => r.StatusCode is HttpStatusCode.TooManyRequests
                    or HttpStatusCode.RequestTimeout
                    or >= HttpStatusCode.InternalServerError)
                .Handle<HttpRequestException>()
                .Handle<TaskCanceledException>(),
            OnRetry = args =>
            {
                Log.Warning("Retry {Attempt} after {Delay}ms due to {Outcome}",
                    args.AttemptNumber, args.RetryDelay.TotalMilliseconds, args.Outcome);
                return ValueTask.CompletedTask;
            }
        });
        pipeline.AddTimeout(TimeSpan.FromSeconds(15));
    });

// Don't retry non-idempotent POST without idempotency key
// Do retry: GET, PUT (with same body), idempotent POST (with key)""",
        "language": "csharp",
        "key_points": [
            "Retry transient failures only — 5xx, timeout, 429",
            "Exponential backoff + jitter prevents thundering herd",
            "Never blindly retry non-idempotent POST",
            "Combine retry + circuit breaker + timeout",
            "Polly v8 AddResilienceHandler on HttpClient",
        ],
    },
}
