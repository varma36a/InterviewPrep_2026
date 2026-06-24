"""Enhanced interview-prep content — Azure, Docker/DevOps, HTML/CSS (Part 3)."""

DETAILED_PART3: dict[str, dict] = {
    "app-service": {
        "explanation": (
            "**Azure App Service** is a fully managed **Platform-as-a-Service (PaaS)** for hosting web apps, REST APIs, "
            "and background workers without provisioning or patching VMs. It supports **.NET, Node.js, Python, Java, and PHP**, "
            "and integrates natively with **Azure DevOps, GitHub Actions, and deployment slots** for blue-green releases. "
            "**Deployment slots** (e.g., staging → production) let you warm up a new build and swap traffic with zero downtime. "
            "You can **scale out** (more instances) for traffic spikes or **scale up** (larger SKU) for CPU/memory needs. "
            "Built-in features include **custom domains, free managed TLS certificates, auto-heal, and VNet integration** "
            "for private access to databases. Pair App Service with **Application Insights** for request tracing and "
            "**Key Vault references** so connection strings never live in source control."
        ),
        "code": """# Deploy a .NET 8 API to App Service (Azure CLI)
az group create --name rg-order-app --location eastus

az appservice plan create \\
  --name plan-order-api \\
  --resource-group rg-order-app \\
  --sku B1 \\
  --is-linux

az webapp create \\
  --name order-api-prod \\
  --resource-group rg-order-app \\
  --plan plan-order-api \\
  --runtime \"DOTNET:8\"

# Publish and deploy from local machine
dotnet publish -c Release -o ./publish
cd publish && zip -r ../app.zip .
az webapp deployment source config-zip \\
  --resource-group rg-order-app \\
  --name order-api-prod \\
  --src ../app.zip

# Blue-green via deployment slots
az webapp deployment slot create \\
  --name order-api-prod \\
  --resource-group rg-order-app \\
  --slot staging

# Deploy to staging, run smoke tests, then swap
az webapp deployment slot swap \\
  --name order-api-prod \\
  --resource-group rg-order-app \\
  --slot staging""",
        "language": "bash",
        "key_points": [
            "PaaS — no VM management; focus on code and configuration",
            "Deployment slots enable zero-downtime blue-green deployments",
            "Scale out (horizontal) vs scale up (vertical) — know when to use each",
            "Use Managed Identity + Key Vault references instead of app settings secrets",
            "App Service for Containers when you need a custom Docker image",
        ],
    },
    "key-vault": {
        "explanation": (
            "**Azure Key Vault** is a centralized secrets management service for **passwords, API keys, connection strings, "
            "certificates, and encryption keys**. Storing secrets in `appsettings.json` or environment variables is an "
            "**anti-pattern** — Key Vault eliminates secrets from code, config files, and CI/CD logs. Applications authenticate "
            "via **Managed Identity** (no stored credentials) and retrieve secrets at runtime using the **Azure SDK or "
            "Key Vault configuration provider**. **RBAC** (role-based access control) and **access policies** restrict who "
            "and what can read or write secrets. Secrets can be **rotated** in the vault without redeploying application code — "
            "the app picks up new values on restart or via configuration refresh. In interviews, emphasize the **security boundary**: "
            "developers never see production secrets; pipelines use service principals with least-privilege access."
        ),
        "code": """// Program.cs — load secrets from Key Vault at startup
using Azure.Identity;

var builder = WebApplication.CreateBuilder(args);

// Managed Identity works in Azure; DefaultAzureCredential falls back to
// Azure CLI / Visual Studio credentials during local development
var keyVaultUrl = builder.Configuration["KeyVault:Url"];
if (!string.IsNullOrEmpty(keyVaultUrl))
{
    builder.Configuration.AddAzureKeyVault(
        new Uri(keyVaultUrl),
        new DefaultAzureCredential());
}

// Secrets appear as normal configuration keys
var sqlConnection = builder.Configuration["SqlConnectionString"];
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(sqlConnection));

// Key Vault reference in App Service (no secret in portal UI)
// App Setting value: @Microsoft.KeyVault(SecretUri=https://myvault.vault.azure.net/secrets/SqlConnection/)

var app = builder.Build();
app.Run();""",
        "language": "csharp",
        "key_points": [
            "Never commit secrets — use Key Vault + Managed Identity",
            "DefaultAzureCredential simplifies local dev and Azure prod auth",
            "RBAC: Key Vault Secrets User role for read-only app access",
            "Rotate secrets in vault without code changes",
            "Key Vault references in App Service app settings avoid plain-text secrets",
        ],
    },
    "app-insights": {
        "explanation": (
            "**Azure Application Insights** is an **Application Performance Management (APM)** service that collects "
            "telemetry from your apps: **request rates, response times, failure rates, dependency calls** (SQL, HTTP, Redis), "
            "and custom events/metrics. It enables **distributed tracing** — following a single user request across "
            "microservices using a **correlation ID** (operation_Id). The **Live Metrics** stream shows real-time CPU, "
            "request throughput, and exceptions during deployments. **Smart detection** and **alert rules** notify teams "
            "when failure rates spike or response times degrade. In ASP.NET Core, instrumentation is often automatic via "
            "the **Application Insights SDK or OpenTelemetry**. Custom telemetry (`TrackEvent`, `TrackMetric`) adds "
            "business context like order IDs or payment outcomes. Interview tip: tie App Insights to **SLIs/SLOs** "
            "and on-call runbooks."
        ),
        "code": """// Program.cs — enable Application Insights
builder.Services.AddApplicationInsightsTelemetry();

// Custom telemetry in a service
public class OrderService(TelemetryClient telemetry, IOrderRepository repo)
{
    public async Task<OrderResult> PlaceOrderAsync(Order order)
    {
        // Start a tracked operation — nested dependencies auto-correlate
        using var operation = telemetry.StartOperation<RequestTelemetry>("PlaceOrder");
        operation.Telemetry.Properties["CustomerId"] = order.CustomerId.ToString();

        try
        {
            await repo.SaveAsync(order);

            // Business event for dashboards and funnels
            telemetry.TrackEvent("OrderPlaced", new Dictionary<string, string>
            {
                ["OrderId"] = order.Id.ToString(),
                ["Total"] = order.Total.ToString("F2")
            });

            telemetry.TrackMetric("OrderValue", (double)order.Total);
            return OrderResult.Success(order.Id);
        }
        catch (Exception ex)
        {
            telemetry.TrackException(ex, new Dictionary<string, string>
            {
                ["OrderId"] = order.Id.ToString()
            });
            throw;
        }
    }
}""",
        "language": "csharp",
        "key_points": [
            "Automatic tracking of HTTP requests, dependencies, and exceptions",
            "Distributed tracing correlates calls across microservices",
            "Custom events/metrics add business-level observability",
            "Alert on failure rate, duration, or availability SLO breaches",
            "OpenTelemetry is the modern standard; App Insights is a backend",
        ],
    },
    "azure-devops-cicd": {
        "explanation": (
            "A **CI/CD pipeline** for .NET + Angular on Azure automates **build, test, and deploy** on every commit or PR. "
            "**Continuous Integration** runs on PRs: restore packages, compile, run unit/integration tests, and publish artifacts. "
            "**Continuous Deployment** triggers on merge to `main`: deploy the API to an App Service **staging slot**, "
            "deploy the Angular build to **Static Web Apps or Blob Storage + CDN**, run **smoke tests**, then **swap slots** "
            "for zero-downtime release. Pipeline secrets (connection strings, service principals) live in **variable groups "
            "linked to Key Vault** — never hard-coded in YAML. Use **environments** with approval gates for production. "
            "In interviews, walk through the full flow: PR → build → test → artifact → deploy staging → validate → promote."
        ),
        "code": """# azure-pipelines.yml — .NET API + Angular SPA
trigger:
  branches:
    include: [main]

pr:
  branches:
    include: [main]

variables:
  buildConfiguration: Release
  dotnetVersion: '8.x'
  nodeVersion: '20.x'

stages:
  # ── CI: Build & Test ──────────────────────────────────────
  - stage: Build
    displayName: Build and Test
    jobs:
      - job: BuildApi
        pool: { vmImage: ubuntu-latest }
        steps:
          - task: UseDotNet@2
            inputs: { version: $(dotnetVersion) }
          - task: DotNetCoreCLI@2
            displayName: Restore & Test
            inputs:
              command: test
              projects: '**/*Tests.csproj'
              arguments: '--configuration $(buildConfiguration)'
          - task: DotNetCoreCLI@2
            displayName: Publish API
            inputs:
              command: publish
              publishWebProjects: true
              arguments: '--configuration $(buildConfiguration) -o $(Build.ArtifactStagingDirectory)/api'
          - publish: $(Build.ArtifactStagingDirectory)/api
            artifact: api-drop

      - job: BuildWeb
        pool: { vmImage: ubuntu-latest }
        steps:
          - task: NodeTool@0
            inputs: { versionSpec: $(nodeVersion) }
          - script: |
              npm ci --prefix ClientApp
              npm run build --prefix ClientApp -- --configuration production
            displayName: Build Angular
          - publish: ClientApp/dist
            artifact: web-drop

  # ── CD: Deploy to staging, smoke test, swap ────────────────
  - stage: Deploy
    displayName: Deploy to Production
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployApi
        environment: production
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: 'azure-prod-connection'
                    appType: webAppLinux
                    appName: 'order-api-prod'
                    deployToSlotOrASE: true
                    slotName: staging
                    package: '$(Pipeline.Workspace)/api-drop'
                - script: curl -f https://order-api-prod-staging.azurewebsites.net/health
                  displayName: Smoke test staging
                - task: AzureAppServiceManage@0
                  inputs:
                    action: 'Swap Slots'
                    webAppName: 'order-api-prod'
                    sourceSlot: staging""",
        "language": "yaml",
        "key_points": [
            "PR triggers run CI (build + test); main branch triggers CD",
            "Publish artifacts once; deploy the same bits to staging then prod",
            "Deployment slots + swap = zero-downtime releases",
            "Secrets in variable groups linked to Key Vault, not in YAML",
            "Smoke tests on staging before slot swap or production promotion",
        ],
    },
    "service-bus": {
        "explanation": (
            "**Azure Service Bus** is an enterprise **message broker** for reliable asynchronous communication between "
            "distributed services. It supports **queues** (point-to-point: one consumer per message) and **topics/subscriptions** "
            "(pub/sub: multiple subscribers each get a copy). Unlike simple **Azure Storage Queues**, Service Bus offers "
            "**transactions, sessions, duplicate detection, scheduled delivery, and dead-letter queues (DLQ)**. Messages "
            "are delivered **at-least-once**, so consumers must be **idempotent** — processing the same message twice "
            "should not corrupt state. Failed messages after max retries land in the **DLQ** for investigation and replay. "
            "Common .NET integration: **Azure.Messaging.ServiceBus SDK**, **MassTransit**, or **Azure Functions triggers**. "
            "Use Service Bus when you need guaranteed delivery, ordering (sessions), or pub/sub; use Storage Queues for "
            "simple, high-volume, cost-sensitive workloads."
        ),
        "code": """// Producer — send order event to a Service Bus queue
await using var client = new ServiceBusClient(connectionString);
var sender = client.CreateSender("order-placed");

var orderEvent = new OrderPlacedEvent(order.Id, order.CustomerId, order.Total);
var message = new ServiceBusMessage(JsonSerializer.Serialize(orderEvent))
{
    MessageId = order.Id.ToString(),       // enables duplicate detection
    ContentType = "application/json",
    Subject = "OrderPlaced"
};

await sender.SendMessageAsync(message);

// Consumer — Azure Function with automatic retry + DLQ
[Function(nameof(ProcessOrderPlaced))]
public async Task ProcessOrderPlaced(
    [ServiceBusTrigger("order-placed", Connection = "ServiceBus")]
    ServiceBusReceivedMessage message,
    ServiceBusMessageActions messageActions)
{
    var orderEvent = JsonSerializer.Deserialize<OrderPlacedEvent>(message.Body.ToString());

    // Idempotent: check if already processed before side effects
    if (await _processedStore.ExistsAsync(message.MessageId))
    {
        await messageActions.CompleteMessageAsync(message);
        return;
    }

    await _inventoryService.ReserveStockAsync(orderEvent!.ProductId);
    await _processedStore.MarkProcessedAsync(message.MessageId);
    // Function runtime completes message on success; failures → retry → DLQ
}""",
        "language": "csharp",
        "key_points": [
            "Queues = one consumer; Topics/Subscriptions = pub/sub",
            "At-least-once delivery — design idempotent consumers",
            "Dead-letter queue captures poison messages after max retries",
            "Sessions guarantee ordered processing for related messages",
            "Storage Queues are simpler/cheaper; Service Bus is enterprise-grade",
        ],
    },
    "full-architecture": {
        "explanation": (
            "A **full-stack .NET + Angular system on Azure** typically follows a layered, cloud-native architecture. "
            "The **Angular SPA** is hosted on **Azure Static Web Apps** or **Blob Storage + CDN** for global low-latency delivery. "
            "An **API gateway** (**Azure API Management** or **Front Door**) handles **rate limiting, TLS termination, "
            "and JWT validation** before traffic reaches the backend. The **.NET 8 API** runs on **App Service or AKS**, "
            "using **Managed Identity** to access **Azure SQL** (transactional data), **Redis Cache** (hot reads/sessions), "
            "and **Key Vault** (secrets). **Long-running or async work** (email, inventory sync) goes through **Service Bus** "
            "to **Azure Functions** workers. **Entra ID (Azure AD)** issues JWTs for authentication; the API enforces "
            "authorization policies. **Application Insights** provides end-to-end observability. In interviews, draw this "
            "diagram and explain **why each service exists** and **how data flows synchronously vs asynchronously**."
        ),
        "code": """/*
  Full-Stack Azure Architecture (typical e-commerce / LOB app)
  ═══════════════════════════════════════════════════════════════

  ┌─────────────┐
  │   Browser   │  Angular SPA (TypeScript, RxJS, HttpClient)
  └──────┬──────┘
         │ HTTPS
         ▼
  ┌─────────────────┐
  │ Azure Front Door │  Global load balancing, WAF, CDN
  │   or APIM        │  Rate limiting, JWT validation, routing
  └──────┬──────────┘
         │
    ┌────┴────────────────────────────┐
    │                                 │
    ▼                                 ▼
┌──────────────┐              ┌──────────────┐
│ Static Web   │              │ App Service  │  .NET 8 Minimal API / Web API
│ Apps (Angular)│              │  or AKS      │  Clean Architecture, EF Core
└──────────────┘              └──────┬───────┘
                                     │ Managed Identity (no secrets in code)
                    ┌────────────────┼────────────────┐
                    │                │                │
                    ▼                ▼                ▼
             ┌───────────┐   ┌────────────┐   ┌─────────────┐
             │ Azure SQL  │   │ Redis Cache│   │  Key Vault  │
             │ (orders,   │   │ (sessions, │   │ (conn strs, │
             │  users)    │   │  hot data) │   │  API keys)  │
             └───────────┘   └────────────┘   └─────────────┘
                    │
                    │ publish events
                    ▼
             ┌─────────────┐       ┌──────────────────┐
             │ Service Bus  │──────▶│ Azure Functions  │
             │ (async work) │       │ (email, reports) │
             └─────────────┘       └──────────────────┘

  ┌──────────────┐     ┌───────────────────────┐
  │  Entra ID    │     │ Application Insights  │
  │  (JWT auth)  │     │ (telemetry, alerts)   │
  └──────────────┘     └───────────────────────┘
*/""",
        "language": "text",
        "key_points": [
            "Separate sync (HTTP API) from async (Service Bus + Functions) paths",
            "Managed Identity eliminates stored credentials between Azure services",
            "API Management / Front Door for gateway concerns (auth, rate limit, WAF)",
            "Redis reduces database load; Service Bus decouples heavy processing",
            "Application Insights + Entra ID are cross-cutting on every layer",
        ],
    },
    "azure-functions": {
        "explanation": (
            "**Azure Functions** is a **serverless compute** platform that runs event-driven code without managing servers. "
            "You pay for **executions and execution time** (Consumption plan) rather than idle VM hours. **Triggers** define "
            "what starts a function: **HTTP, Timer, Queue, Blob, Service Bus, Event Grid, Cosmos DB change feed**, and more. "
            "**Bindings** simplify input/output connections to Azure services without boilerplate SDK code. The **Consumption "
            "plan** has **cold start latency** (first request after idle); the **Premium plan** keeps instances warm for "
            "latency-sensitive workloads. **Durable Functions** orchestrate multi-step workflows with state persistence "
            "and automatic retry. Use Functions for **async background tasks** (send email, process uploads, sync data) — "
            "not as a replacement for a full API unless traffic is sporadic."
        ),
        "code": """// Azure Functions isolated worker (.NET 8)
// host.json configures logging, timeout, Service Bus retry policy

// HTTP-triggered function
[Function("GetOrderStatus")]
public async Task<HttpResponseData> GetOrderStatus(
    [HttpTrigger(AuthorizationLevel.Function, "get", Route = "orders/{id}")]
    HttpRequestData req,
    int id)
{
    var order = await _db.Orders.FindAsync(id);
    var response = req.CreateResponse(
        order is null ? HttpStatusCode.NotFound : HttpStatusCode.OK);
    if (order is not null)
        await response.WriteAsJsonAsync(new { order.Id, order.Status });
    return response;
}

// Service Bus trigger — process async order events
[Function(nameof(ProcessOrderEvent))]
public async Task ProcessOrderEvent(
    [ServiceBusTrigger("order-events", Connection = "ServiceBus")]
    string messageBody)
{
    var orderEvent = JsonSerializer.Deserialize<OrderEvent>(messageBody);
    await _emailService.SendConfirmationAsync(orderEvent!.CustomerEmail);
}

// Timer trigger — nightly cleanup job (cron: daily at 2 AM UTC)
[Function("CleanupExpiredSessions")]
public async Task CleanupExpiredSessions(
    [TimerTrigger("0 0 2 * * *")] TimerInfo timer)
{
    await _sessionStore.DeleteExpiredAsync();
}""",
        "language": "csharp",
        "key_points": [
            "Serverless — pay per execution; no server management",
            "Triggers start functions; bindings connect to Azure services",
            "Consumption plan cold starts; Premium plan for low-latency needs",
            "Durable Functions for multi-step workflows with built-in retry",
            "Ideal for event-driven background processing, not primary CRUD APIs",
        ],
    },
    "blob-storage": {
        "explanation": (
            "**Azure Blob Storage** is **object storage** optimized for unstructured data: **files, images, videos, backups, "
            "and static website assets**. Data is organized into **containers** (like folders) containing **blobs** classified "
            "as **Block blobs** (files), **Page blobs** (VHDs), or **Append blobs** (logs). **Access tiers** control cost vs "
            "retrieval speed: **Hot** (frequent access), **Cool** (infrequent, lower storage cost), **Cold** (rare access), "
            "and **Archive** (long-term retention, hours to rehydrate). For client uploads, issue **Shared Access Signatures "
            "(SAS)** with time-limited, scoped permissions instead of exposing account keys. Front **Blob Storage with Azure "
            "CDN** for global static asset delivery. In .NET, use **Azure.Storage.Blobs** SDK with **Managed Identity** "
            "in production."
        ),
        "code": """// Upload, download, and generate SAS for client-side upload
using Azure.Storage.Blobs;
using Azure.Storage.Blobs.Models;
using Azure.Storage.Sas;

var blobServiceClient = new BlobServiceClient(
    new Uri("https://mystorageaccount.blob.core.windows.net"),
    new DefaultAzureCredential());

// Ensure container exists (private by default)
var container = blobServiceClient.GetBlobContainerClient("invoices");
await container.CreateIfNotExistsAsync(PublicAccessType.None);

// Server-side upload
var blobClient = container.GetBlobClient("2026/invoice-1042.pdf");
await blobClient.UploadAsync(fileStream, overwrite: true);

// Set metadata and content type for browser rendering
await blobClient.SetHttpHeadersAsync(new BlobHttpHeaders
{
    ContentType = "application/pdf"
});

// Generate time-limited SAS for direct browser upload (avoid proxying large files)
var sasBuilder = new BlobSasBuilder
{
    BlobContainerName = container.Name,
    BlobName = "2026/invoice-1043.pdf",
    Resource = "b",                              // blob-level SAS
    ExpiresOn = DateTimeOffset.UtcNow.AddHours(1)
};
sasBuilder.SetPermissions(BlobSasPermissions.Create | BlobSasPermissions.Write);
var sasUri = blobClient.GenerateSasUri(sasBuilder);
// Return sasUri to Angular client for direct PUT upload""",
        "language": "csharp",
        "key_points": [
            "Block blobs for files; access tiers (Hot/Cool/Cold/Archive) control cost",
            "SAS tokens enable secure, time-limited client uploads/downloads",
            "Never expose storage account keys — use Managed Identity or SAS",
            "CDN in front of blob containers for global static asset delivery",
            "Lifecycle management policies auto-tier or delete old blobs",
        ],
    },
    "cosmos-db": {
        "explanation": (
            "**Azure Cosmos DB** is a globally distributed, multi-model **NoSQL database** with **single-digit millisecond "
            "latency** and **99.999% SLA** availability. It supports multiple APIs: **SQL (document)**, MongoDB, Cassandra, "
            "Gremlin, and Table. The **partition key** is the most critical design decision — it determines how data is "
            "distributed across physical partitions and affects **query performance and RU cost**. Choose a key with "
            "**high cardinality** (e.g., `customerId`, `tenantId`) to avoid hot partitions; never partition by low-cardinality "
            "fields like `status` or `country`. Throughput is billed in **Request Units (RUs)** — provisioned (fixed) or "
            "serverless (pay-per-request). **Consistency levels** range from **Strong** to **Eventual**, letting you trade "
            "freshness for performance. Use Cosmos DB for **globally distributed apps, IoT telemetry, user profiles, "
            "and catalog data** — not as a drop-in replacement for relational transactional workloads."
        ),
        "code": """// Cosmos DB SQL API — container setup and CRUD
using Microsoft.Azure.Cosmos;

var client = new CosmosClient(endpoint, new DefaultAzureCredential());
var database = await client.CreateDatabaseIfNotExistsAsync("OrderDb");
var container = await database.Database.CreateContainerIfNotExistsAsync(
    id: "Orders",
    partitionKeyPath: "/customerId",   // HIGH cardinality — good choice
    throughput: 400);                   // 400 RU/s provisioned

// Create document
var order = new OrderDocument
{
    Id = Guid.NewGuid().ToString(),
    CustomerId = "cust-789",           // partition key value
    Items = new[] { new OrderItem("Widget", 2, 29.99m) },
    Total = 59.98m,
    CreatedAt = DateTime.UtcNow
};
await container.CreateItemAsync(order, new PartitionKey(order.CustomerId));

// Point read — most efficient (1 RU for small doc)
var response = await container.ReadItemAsync<OrderDocument>(
    id: order.Id,
    partitionKey: new PartitionKey("cust-789"));

// Query WITHIN a single partition — efficient
var query = new QueryDefinition(
    "SELECT * FROM c WHERE c.customerId = @cid AND c.total > @min")
    .WithParameter("@cid", "cust-789")
    .WithParameter("@min", 50);
// BAD: cross-partition query without partition key filter — expensive at scale""",
        "language": "csharp",
        "key_points": [
            "Partition key choice is the #1 design decision — high cardinality",
            "RU (Request Units) billing — provisioned vs serverless",
            "Point reads with partition key are cheapest; cross-partition queries cost more",
            "Consistency levels: Strong → Bounded Staleness → Session → Eventual",
            "SQL API uses JSON documents; not a relational replacement for complex joins",
        ],
    },
    "aks-basics": {
        "explanation": (
            "**Azure Kubernetes Service (AKS)** is a **managed Kubernetes** platform for running containerized applications "
            "at scale. Azure manages the **control plane** (API server, scheduler, etcd); you manage **node pools** "
            "(VMs running your containers). Core concepts: **Pods** (one or more containers), **Deployments** (declarative "
            "replica management + rolling updates), **Services** (stable network endpoint for pods), and **Ingress** "
            "(HTTP routing + TLS). **Azure Container Registry (ACR)** stores Docker images; AKS pulls from ACR via "
            "**Managed Identity**. **Horizontal Pod Autoscaler (HPA)** scales replicas based on CPU/memory/custom metrics. "
            "Choose **AKS over App Service** when you need **multi-container orchestration, custom networking, service mesh, "
            "or portable Kubernetes workloads**. Choose App Service when you want **simpler PaaS** without cluster management."
        ),
        "code": """# Kubernetes Deployment + Service + Ingress for .NET API
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-api
  labels:
    app: order-api
spec:
  replicas: 3                          # run 3 instances for HA
  selector:
    matchLabels:
      app: order-api
  template:
    metadata:
      labels:
        app: order-api
    spec:
      containers:
      - name: api
        image: myregistry.azurecr.io/order-api:1.2.0
        ports:
        - containerPort: 8080
        env:
        - name: ASPNETCORE_ENVIRONMENT
          value: Production
        resources:
          requests: { memory: \"256Mi\", cpu: \"250m\" }
          limits:   { memory: \"512Mi\", cpu: \"500m\" }
        livenessProbe:
          httpGet: { path: /health, port: 8080 }
          initialDelaySeconds: 15
        readinessProbe:
          httpGet: { path: /health/ready, port: 8080 }

---
apiVersion: v1
kind: Service
metadata:
  name: order-api-service
spec:
  selector:
    app: order-api
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: order-api-ingress
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  rules:
  - host: api.mycompany.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: order-api-service
            port:
              number: 80
  tls:
  - hosts: [api.mycompany.com]
    secretName: api-tls-secret""",
        "language": "yaml",
        "key_points": [
            "Pods → Deployments → Services → Ingress is the standard stack",
            "ACR stores images; AKS pulls via Managed Identity",
            "HPA auto-scales replicas based on CPU, memory, or custom metrics",
            "Liveness/readiness probes ensure healthy traffic routing",
            "AKS for complex orchestration; App Service for simpler PaaS hosting",
        ],
    },
    "redis-cache": {
        "explanation": (
            "**Azure Cache for Redis** is a managed **in-memory data store** used for **distributed caching, session state, "
            "pub/sub messaging, and rate limiting**. It dramatically **reduces database load** by storing frequently accessed "
            "data (product catalogs, user profiles, API responses) in memory with configurable **TTL (time-to-live)**. "
            "The **cache-aside pattern** is most common: check cache first → on miss, read DB → populate cache → return. "
            "In ASP.NET Core, register via **`AddStackExchangeRedisCache`** and inject **`IDistributedCache`**. "
            "Redis supports **data structures** beyond strings: hashes, lists, sets, and sorted sets. **Pub/Sub** enables "
            "real-time notifications across app instances. **Important**: Redis is **not a persistent database** — always "
            "have a backing store and set TTLs on every key to prevent unbounded memory growth."
        ),
        "code": """// Program.cs — register Redis as distributed cache
builder.Services.AddStackExchangeRedisCache(options =>
{
    options.Configuration = builder.Configuration["Redis:Connection"];
    options.InstanceName = "OrderApp:";   // key prefix to avoid collisions
});

// Cache-aside pattern in a service
public class ProductService(IDistributedCache cache, AppDbContext db)
{
    public async Task<ProductDto?> GetProductAsync(int id)
    {
        var cacheKey = $"product:{id}";

        // 1. Check cache first
        var cached = await cache.GetStringAsync(cacheKey);
        if (cached is not null)
            return JsonSerializer.Deserialize<ProductDto>(cached);

        // 2. Cache miss — read from database
        var product = await db.Products
            .Where(p => p.Id == id)
            .Select(p => new ProductDto(p.Id, p.Name, p.Price))
            .FirstOrDefaultAsync();

        if (product is null) return null;

        // 3. Populate cache with TTL
        await cache.SetStringAsync(cacheKey, JsonSerializer.Serialize(product),
            new DistributedCacheEntryOptions
            {
                AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(10)
            });

        return product;
    }

    public async Task InvalidateProductAsync(int id)
    {
        // Invalidate on update/delete to prevent stale reads
        await cache.RemoveAsync($"product:{id}");
    }
}""",
        "language": "csharp",
        "key_points": [
            "Cache-aside: check cache → DB on miss → populate cache",
            "Always set TTL on cached entries to prevent stale/unbounded data",
            "Invalidate cache on writes to maintain consistency",
            "IDistributedCache abstraction works with Redis or in-memory",
            "Redis is not persistent storage — always have a backing database",
        ],
    },
    "docker-basics": {
        "explanation": (
            "**Docker** packages applications and their dependencies into **portable, isolated containers** that run "
            "consistently across dev, CI, and production. An **image** is an immutable, layered template built from "
            "a **Dockerfile**; a **container** is a running instance of that image. **Multi-stage builds** keep production "
            "images small by compiling in a SDK stage and copying only the publish output into a slim runtime stage. "
            "Each Dockerfile instruction (FROM, COPY, RUN) creates a **cached layer** — order instructions from least "
            "to most frequently changed for faster rebuilds. Use a **`.dockerignore`** to exclude `bin/`, `obj/`, and "
            "`.git` from the build context. In interviews, explain why containers beat VMs for microservices: **fast startup, "
            "minimal overhead, and identical environments everywhere**."
        ),
        "code": """# Multi-stage Dockerfile for .NET 8 Web API
# ── Stage 1: Build ──────────────────────────────────────────
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copy csproj first — Docker caches restore layer separately
COPY OrderApi/OrderApi.csproj OrderApi/
RUN dotnet restore OrderApi/OrderApi.csproj

# Copy remaining source and publish
COPY OrderApi/ OrderApi/
RUN dotnet publish OrderApi/OrderApi.csproj \\
    -c Release \\
    -o /app/publish \\
    --no-restore

# ── Stage 2: Runtime (much smaller — no SDK) ────────────────
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app

# Run as non-root user for security
RUN adduser --disabled-password --gecos '' appuser
USER appuser

COPY --from=build /app/publish .

# ASP.NET Core listens on 8080 in containers by default
ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080

ENTRYPOINT [\"dotnet\", \"OrderApi.dll\"]

# Build and run locally:
#   docker build -t order-api:local .
#   docker run -p 5000:8080 --env ConnectionStrings__Sql=\"...\" order-api:local""",
        "language": "dockerfile",
        "key_points": [
            "Image = immutable template; Container = running instance",
            "Multi-stage builds produce small production images (runtime only)",
            "Copy csproj before source code to leverage Docker layer caching",
            "Run containers as non-root in production",
            ".dockerignore excludes bin/obj/node_modules from build context",
        ],
    },
    "docker-compose": {
        "explanation": (
            "**Docker Compose** defines and runs **multi-container applications** using a single **`docker-compose.yml`** "
            "file. It is ideal for **local development** where you need the API, database, Redis, and message broker "
            "running together with one command: **`docker compose up -d`**. The **`depends_on`** directive controls startup "
            "order, and **named volumes** persist database data across container restarts. **Environment variables** and "
            "**.env` files** inject connection strings without hard-coding secrets. **Networks** isolate services — "
            "containers reference each other by **service name** as hostname (e.g., `Server=db` for SQL Server). "
            "Compose files mirror production topology, reducing **\"works on my machine\"** issues. For production, "
            "teams typically move to **AKS, App Service, or ECS** — Compose is primarily a dev/test tool."
        ),
        "code": """# docker-compose.yml — local full-stack dev environment
services:
  api:
    build:
      context: .
      dockerfile: OrderApi/Dockerfile
    ports:
      - \"5000:8080\"                    # host:container
    environment:
      ASPNETCORE_ENVIRONMENT: Development
      ConnectionStrings__Sql: \"Server=db;Database=Orders;User=sa;Password=Dev_Passw0rd!;TrustServerCertificate=True\"
      Redis__Connection: \"redis:6379\"
    depends_on:
      db:
        condition: service_healthy        # wait for SQL to be ready
      redis:
        condition: service_started
    networks:
      - app-network

  db:
    image: mcr.microsoft.com/mssql/server:2022-latest
    environment:
      ACCEPT_EULA: \"Y\"
      SA_PASSWORD: \"Dev_Passw0rd!\"
    ports:
      - \"1433:1433\"
    volumes:
      - sqldata:/var/opt/mssql          # persist DB across restarts
    healthcheck:
      test: /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P \"Dev_Passw0rd!\" -C -Q \"SELECT 1\"
      interval: 10s
      retries: 5
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    ports:
      - \"6379:6379\"
    networks:
      - app-network

volumes:
  sqldata:                              # named volume for SQL data

networks:
  app-network:
    driver: bridge

# Commands:
#   docker compose up -d        # start all services in background
#   docker compose logs -f api  # tail API logs
#   docker compose down -v      # stop and remove volumes""",
        "language": "yaml",
        "key_points": [
            "Single YAML file defines all services, networks, and volumes",
            "docker compose up -d starts the entire local stack",
            "Services communicate by service name (e.g., db, redis)",
            "Named volumes persist database data across restarts",
            "Primarily for local dev — production uses AKS or App Service",
        ],
    },
    "terraform": {
        "explanation": (
            "**Terraform** is an **Infrastructure as Code (IaC)** tool by HashiCorp that provisions cloud resources "
            "declaratively using **HCL (HashiCorp Configuration Language)**. Unlike Azure-native **ARM templates or Bicep**, "
            "Terraform is **multi-cloud** — the same workflow applies to Azure, AWS, and GCP. The **state file** "
            "(`terraform.tfstate`) tracks what resources exist; store it remotely in **Azure Storage** with locking "
            "for team collaboration. The workflow is **`terraform init → plan → apply`**: plan shows a diff before "
            "any changes are made. **Modules** encapsulate reusable infrastructure patterns (e.g., a standard web app "
            "module). In interviews, compare Terraform vs Bicep: Terraform wins on **multi-cloud portability**; "
            "Bicep wins on **Azure-native integration and zero state file management**."
        ),
        "code": """# main.tf — provision Azure App Service with Terraform
terraform {
  required_providers {
    azurerm = {
      source  = \"hashicorp/azurerm\"
      version = \"~> 3.0\"
    }
  }
  # Remote state — required for team collaboration
  backend \"azurerm\" {
    resource_group_name  = \"rg-terraform-state\"
    storage_account_name = \"tfstatestore\"
    container_name       = \"tfstate\"
    key                  = \"order-app.prod.tfstate\"
  }
}

provider \"azurerm\" {
  features {}
}

resource \"azurerm_resource_group\" \"rg\" {
  name     = \"rg-order-app\"
  location = \"East US\"
}

resource \"azurerm_service_plan\" \"plan\" {
  name                = \"plan-order-api\"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = \"Linux\"
  sku_name            = \"B1\"
}

resource \"azurerm_linux_web_app\" \"api\" {
  name                = \"order-api-prod\"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.plan.id

  site_config {
    application_stack {
      dotnet_version = \"8.0\"
    }
    always_on = true
  }

  app_settings = {
    \"ASPNETCORE_ENVIRONMENT\" = \"Production\"
  }

  identity {
    type = \"SystemAssigned\"    # enable Managed Identity
  }
}

# Workflow:
#   terraform init     # download providers, configure backend
#   terraform plan     # preview changes (dry run)
#   terraform apply    # create/update resources""",
        "language": "hcl",
        "key_points": [
            "Declarative IaC — describe desired state, Terraform reconciles",
            "terraform plan before apply — always review the diff",
            "Remote state in Azure Storage with locking for team use",
            "Modules encapsulate reusable infrastructure patterns",
            "Multi-cloud portable; Bicep is Azure-native alternative without state files",
        ],
    },
    "message-brokers": {
        "explanation": (
            "**Message brokers** decouple services by routing messages between **producers** and **consumers** asynchronously. "
            "**RabbitMQ** is a traditional **AMQP broker** using **exchanges and queues** — great for task distribution "
            "and request/reply patterns; popular in .NET via **MassTransit**. **Apache Kafka** is an **event streaming "
            "platform** — messages are persisted in **topics/partitions** and can be **replayed**, making it ideal for "
            "**event sourcing, audit logs, and stream analytics** at massive scale. **Azure Service Bus** is Microsoft's "
            "managed enterprise broker with **topics, subscriptions, sessions, transactions, and dead-letter queues**. "
            "All brokers typically deliver **at-least-once**, so consumers must be **idempotent**. In interviews, explain "
            "**when to pick each**: RabbitMQ for classic messaging, Kafka for event streams/replay, Service Bus for "
            "Azure-native enterprise integration."
        ),
        "code": """// MassTransit abstracts broker choice — swap RabbitMQ ↔ Azure Service Bus
// Program.cs
builder.Services.AddMassTransit(x =>
{
    x.AddConsumer<OrderPlacedConsumer>();

    // Option A: RabbitMQ (self-hosted or CloudAMQP)
    x.UsingRabbitMq((context, cfg) =>
    {
        cfg.Host(\"rabbitmq://localhost\");
        cfg.ConfigureEndpoints(context);
    });

    // Option B: Azure Service Bus (managed)
    // x.UsingAzureServiceBus((context, cfg) =>
    // {
    //     cfg.Host(builder.Configuration[\"ServiceBus:Connection\"]);
    //     cfg.ConfigureEndpoints(context);
    // });
});

// Consumer — same code regardless of broker
public class OrderPlacedConsumer : IConsumer<OrderPlacedEvent>
{
    public async Task Consume(ConsumeContext<OrderPlacedEvent> context)
    {
        var order = context.Message;

        // Idempotent: skip if already processed
        if (await _store.ExistsAsync(order.OrderId)) return;

        await _inventoryService.ReserveStockAsync(order.ProductId);
        await _emailService.SendConfirmationAsync(order.CustomerEmail);
        await _store.MarkProcessedAsync(order.OrderId);
    }
}

// Kafka concept (Confluent .NET client) — event streaming with replay
// await producer.ProduceAsync(\"order-events\",
//     new Message<Null, string> { Value = JsonSerializer.Serialize(orderEvent) });""",
        "language": "csharp",
        "key_points": [
            "RabbitMQ: AMQP exchanges/queues — classic task distribution",
            "Kafka: persisted event streams with replay — high throughput analytics",
            "Azure Service Bus: managed enterprise messaging on Azure",
            "At-least-once delivery everywhere — design idempotent consumers",
            "MassTransit in .NET abstracts broker implementation details",
        ],
    },
    "wcf-legacy": {
        "explanation": (
            "**Windows Communication Foundation (WCF)** is a .NET Framework technology for building **SOAP-based web services** "
            "with features like **transactions, reliable messaging, and WS-Security**. It was the standard for **enterprise "
            "integrations** in the 2005–2015 era — banking, insurance, and government systems still run WCF endpoints today. "
            "WCF relies on **XML envelopes, WSDL contracts, and SOAP bindings** (HTTP, TCP, MSMQ). **.NET Core/.NET 5+** "
            "supports WCF **client** libraries only — you **cannot host** new WCF services on modern .NET. The migration "
            "path is to **expose REST or gRPC APIs** alongside existing SOAP endpoints, then gradually migrate consumers. "
            "In interviews, show you understand **SOAP vs REST** trade-offs: SOAP has built-in WS-* standards for "
            "enterprise security and transactions; REST is simpler, JSON-based, and web-friendly."
        ),
        "code": """// ── LEGACY: WCF SOAP Service (.NET Framework) ──────────────
[ServiceContract(Namespace = \"http://orders.mycompany.com/v1\")]
public interface IOrderService
{
    [OperationContract]
    Order GetOrder(int id);

    [OperationContract]
    void SubmitOrder(Order order);
}

public class OrderService : IOrderService
{
    public Order GetOrder(int id) => /* read from database */;
    public void SubmitOrder(Order order) => /* save to database */;
}

// ── MODERN REPLACEMENT: ASP.NET Core Minimal API (.NET 8) ──
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// REST — JSON, HTTP verbs, OpenAPI/Swagger
app.MapGet(\"/api/orders/{id:int}\", async (int id, AppDbContext db) =>
    await db.Orders.FindAsync(id) is { } order
        ? Results.Ok(order)
        : Results.NotFound());

app.MapPost(\"/api/orders\", async (CreateOrderDto dto, AppDbContext db) =>
{
    var order = new Order { CustomerName = dto.CustomerName, Total = dto.Total };
    db.Orders.Add(order);
    await db.SaveChangesAsync();
    return Results.Created($\"/api/orders/{order.Id}\", order);
});

// gRPC — binary, strongly typed, high performance (internal services)
// builder.Services.AddGrpc();
// app.MapGrpcService<OrderGrpcService>();

app.Run();""",
        "language": "csharp",
        "key_points": [
            "WCF = SOAP services on .NET Framework — still common in legacy enterprise",
            ".NET Core+ supports WCF client only — cannot host new WCF services",
            "Migration: expose REST/gRPC alongside SOAP, migrate consumers gradually",
            "SOAP: XML, WSDL, WS-Security, transactions — enterprise-heavy",
            "REST/gRPC: JSON/binary, simpler, modern standard for new development",
        ],
    },
    "cicd-docker": {
        "explanation": (
            "A **CI/CD pipeline for Docker** builds container images on every commit, **pushes them to a registry** "
            "(Azure Container Registry — ACR), and **deploys to AKS or App Service for Containers**. The pipeline tags "
            "images with the **build ID or git commit SHA** for traceability — never rely on `:latest` in production. "
            "**Multi-stage Dockerfiles** keep images small and secure. Enable **ACR Tasks** or pipeline steps for "
            "**vulnerability scanning** (Microsoft Defender for Cloud, Trivy). AKS pulls images from ACR using "
            "**Managed Identity** (AcrPull role) — no registry passwords stored in cluster config. **Deployment strategies** "
            "include rolling updates (default in Kubernetes), blue-green, and canary. In interviews, describe the full "
            "flow: code push → build image → scan → push to ACR → deploy to AKS → health check."
        ),
        "code": """# Azure DevOps pipeline — build, push to ACR, deploy to AKS
trigger:
  branches:
    include: [main]

variables:
  acrName: myregistry
  imageName: order-api
  aksCluster: aks-prod
  resourceGroup: rg-order-app

stages:
  - stage: BuildAndPush
    jobs:
      - job: Docker
        pool: { vmImage: ubuntu-latest }
        steps:
          - task: Docker@2
            displayName: Build and push to ACR
            inputs:
              containerRegistry: acr-connection     # service connection to ACR
              repository: $(imageName)
              command: buildAndPush
              Dockerfile: OrderApi/Dockerfile
              tags: |
                $(Build.BuildId)
                $(Build.SourceVersion)             # git SHA for traceability

          - script: |
              # Optional: scan image for vulnerabilities
              trivy image $(acrName).azurecr.io/$(imageName):$(Build.BuildId) \\
                --severity HIGH,CRITICAL --exit-code 1
            displayName: Vulnerability scan

  - stage: Deploy
    dependsOn: BuildAndPush
    jobs:
      - deployment: DeployToAKS
        environment: production
        strategy:
          runOnce:
            deploy:
              steps:
                - task: KubernetesManifest@1
                  inputs:
                    action: deploy
                    kubernetesServiceConnection: aks-prod-connection
                    namespace: default
                    manifests: k8s/deployment.yaml
                    containers: |
                      $(acrName).azurecr.io/$(imageName):$(Build.BuildId)""",
        "language": "yaml",
        "key_points": [
            "Tag images with build ID or git SHA — never :latest in production",
            "ACR stores images; AKS pulls via Managed Identity (AcrPull role)",
            "Scan images for vulnerabilities before deployment",
            "Multi-stage Dockerfiles for small, secure production images",
            "Deployment strategies: rolling update, blue-green, or canary",
        ],
    },
    "semantic-html": {
        "explanation": (
            "**Semantic HTML** uses elements that describe the **meaning and structure** of content, not just its visual "
            "appearance. Instead of `<div>` soup, use **`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, "
            "and `<footer>`** to create a meaningful document outline. This improves **accessibility** — screen readers "
            "use landmarks to navigate (\"skip to main content\"), and assistive tech understands heading hierarchy. "
            "It also boosts **SEO** because search engines parse semantic structure to understand page content. "
            "Use **ARIA attributes** (`aria-label`, `aria-labelledby`, `role`) only when native HTML elements are "
            "insufficient. Follow the **heading hierarchy** (`<h1>` once per page, then `<h2>`, `<h3>`) — never skip "
            "levels for styling convenience."
        ),
        "code": """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Order #1042 — My App</title>
</head>
<body>
  <!-- Landmark: site header with navigation -->
  <header>
    <a href=\"/\" aria-label=\"My App home\">
      <img src=\"/logo.svg\" alt=\"My App logo\">
    </a>
    <nav aria-label=\"Main navigation\">
      <ul>
        <li><a href=\"/\" aria-current=\"page\">Dashboard</a></li>
        <li><a href=\"/orders\">Orders</a></li>
        <li><a href=\"/settings\">Settings</a></li>
      </ul>
    </nav>
  </header>

  <!-- Primary content area — one per page -->
  <main>
    <article aria-labelledby=\"order-title\">
      <h1 id=\"order-title\">Order #1042</h1>
      <p>Placed on <time datetime=\"2026-06-15\">June 15, 2026</time></p>

      <!-- Thematic grouping of related content -->
      <section aria-labelledby=\"items-heading\">
        <h2 id=\"items-heading\">Line Items</h2>
        <table>
          <caption class=\"sr-only\">Products in this order</caption>
          <thead>
            <tr><th scope=\"col\">Product</th><th scope=\"col\">Qty</th><th scope=\"col\">Price</th></tr>
          </thead>
          <tbody>
            <tr><td>Widget Pro</td><td>2</td><td>$29.99</td></tr>
          </tbody>
        </table>
      </section>

      <section aria-labelledby=\"summary-heading\">
        <h2 id=\"summary-heading\">Order Summary</h2>
        <p>Total: <strong>$59.98</strong></p>
      </section>
    </article>

    <!-- Supplementary content -->
    <aside aria-label=\"Related orders\">
      <h2>Recent Orders</h2>
      <!-- related content -->
    </aside>
  </main>

  <footer>
    <p>&copy; 2026 My App. All rights reserved.</p>
  </footer>
</body>
</html>""",
        "language": "html",
        "key_points": [
            "Use semantic tags (header, nav, main, article, section, footer) over divs",
            "One h1 per page; maintain proper heading hierarchy (h1 → h2 → h3)",
            "ARIA attributes supplement — not replace — semantic HTML",
            "Improves screen reader navigation and SEO ranking",
            "table caption, th scope, and time datetime enhance accessibility",
        ],
    },
    "flexbox-grid": {
        "explanation": (
            "**CSS Flexbox** and **CSS Grid** are the two modern layout systems — they solve different problems. "
            "**Flexbox** is **one-dimensional**: it arranges items in a single row OR column. Use it for **component-level "
            "layouts**: navbars, card rows, centering content, and distributing space along one axis. **`display: flex`** "
            "with **`justify-content`** (main axis) and **`align-items`** (cross axis) handles most component alignment. "
            "**CSS Grid** is **two-dimensional**: it defines both rows AND columns simultaneously. Use it for **page-level "
            "layouts**: dashboards, holy-grail layouts, photo galleries, and form grids. **`grid-template-columns: "
            "repeat(auto-fit, minmax(280px, 1fr))`** creates responsive columns without media queries. "
            "**Rule of thumb**: Flexbox for components, Grid for pages. They compose well — a Grid cell can contain "
            "a Flexbox container."
        ),
        "code": """/* ── Flexbox: horizontal navbar component ─────────────── */
.navbar {
  display: flex;
  justify-content: space-between;  /* logo left, links right */
  align-items: center;             /* vertical centering */
  padding: 0 1.5rem;
  gap: 1rem;
}

.nav-links {
  display: flex;
  gap: 1.5rem;                     /* even spacing between links */
  list-style: none;
}

/* Flexbox: center a login card vertically and horizontally */
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

/* ── CSS Grid: responsive dashboard page layout ───────── */
.dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  padding: 1.5rem;
}

/* Grid: holy-grail layout (header, sidebar, main, footer) */
.app-layout {
  display: grid;
  grid-template-areas:
    \"header header\"
    \"sidebar main\"
    \"footer footer\";
  grid-template-columns: 240px 1fr;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}

.app-header  { grid-area: header; }
.app-sidebar { grid-area: sidebar; }
.app-main    { grid-area: main; }
.app-footer  { grid-area: footer; }

/* Responsive: collapse sidebar on mobile */
@media (max-width: 768px) {
  .app-layout {
    grid-template-areas:
      \"header\"
      \"main\"
      \"footer\";
    grid-template-columns: 1fr;
  }
  .app-sidebar { display: none; }
}""",
        "language": "css",
        "key_points": [
            "Flexbox = one-dimensional (row OR column) — use for components",
            "Grid = two-dimensional (rows AND columns) — use for page layouts",
            "auto-fit/minmax creates responsive grids without media queries",
            "Flexbox and Grid compose together naturally",
            "Bootstrap and Tailwind CSS build on these primitives",
        ],
    },
    "responsive-design": {
        "explanation": (
            "**Responsive design** ensures web applications work well on **all screen sizes** — mobile phones, tablets, "
            "desktops, and ultrawide monitors. The foundation is the **viewport meta tag** (`<meta name=\"viewport\" "
            "content=\"width=device-width, initial-scale=1.0\">`) which tells mobile browsers to use the device width "
            "instead of zooming out to a desktop layout. Use a **mobile-first** approach: write base styles for small "
            "screens, then add **`@media (min-width: ...)`** queries to enhance for larger viewports. Prefer **flexible "
            "units** (`rem`, `%`, `fr`, `vw`) over fixed pixels for typography and layout. **Responsive images** use "
            "`srcset` and `sizes` attributes or CSS `object-fit` to serve appropriate resolutions. In Angular, "
            "**BreakpointObserver** from `@angular/cdk/layout` detects viewport changes in TypeScript for conditional "
            "component rendering."
        ),
        "code": """<!-- Viewport meta tag — required in index.html -->
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">

<!-- Responsive images with srcset -->
<img
  src=\"/assets/hero-800.jpg\"
  srcset=\"/assets/hero-400.jpg 400w,
          /assets/hero-800.jpg 800w,
          /assets/hero-1200.jpg 1200w\"
  sizes=\"(max-width: 600px) 100vw, 800px\"
  alt=\"Dashboard preview\">

/* Mobile-first CSS — base styles for small screens */
.container {
  padding: 1rem;
  font-size: 1rem;           /* 16px base — scales with user preferences */
}

.sidebar { display: none; }  /* hidden on mobile */
.content { width: 100%; }

.card-grid {
  display: grid;
  grid-template-columns: 1fr;  /* single column on mobile */
  gap: 1rem;
}

/* Tablet and up */
@media (min-width: 768px) {
  .layout {
    display: grid;
    grid-template-columns: 240px 1fr;
  }
  .sidebar { display: block; }
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .container { max-width: 1200px; margin: 0 auto; }
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

/* Angular BreakpointObserver — conditional logic in TypeScript */
/*
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';

readonly isMobile$ = this.breakpointObserver
  .observe([Breakpoints.Handset])
  .pipe(map(result => result.matches));
*/""",
        "language": "css",
        "key_points": [
            "Viewport meta tag is required for proper mobile rendering",
            "Mobile-first: base styles for small screens, min-width media queries up",
            "Use rem, %, fr — not fixed px — for flexible layouts",
            "Responsive images: srcset/sizes or CSS object-fit",
            "Angular BreakpointObserver for viewport-aware component logic",
        ],
    },
    "angular-material": {
        "explanation": (
            "**Angular Material** is Google's **Material Design component library** for Angular, providing pre-built "
            "UI components: **buttons, dialogs, tables, form fields, navigation, and date pickers**. It ensures "
            "**consistent design, accessibility (a11y), and theming** across your application. Install via "
            "`ng add @angular/material` which configures theming, animations, and typography. **Theming** uses "
            "CSS custom properties and Sass palettes (`$primary`, `$accent`, `$warn`) to match brand colors. "
            "Angular's default **ViewEncapsulation.Emulated** scopes component styles by adding unique attributes — "
            "use **`:host`** to style the component root and **`::ng-deep`** is deprecated (prefer global styles "
            "or `ViewEncapsulation.None` sparingly). **Angular CDK** (Component Dev Kit) provides lower-level "
            "primitives like **Overlay, Portal, DragDrop, and BreakpointObserver** that Material builds upon."
        ),
        "code": """// app.config.ts — provide Material animations
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

export const appConfig: ApplicationConfig = {
  providers: [
    provideAnimationsAsync(),   // required for Material animations
  ],
};

// order-table.component.ts — Material table with sorting and pagination
@Component({
  selector: 'app-order-table',
  standalone: true,
  imports: [
    MatTableModule,
    MatSortModule,
    MatPaginatorModule,
    MatButtonModule,
    MatIconModule,
  ],
  template: `
    <table mat-table [dataSource]=\"dataSource\" matSort>
      <ng-container matColumnDef=\"id\">
        <th mat-header-cell *matHeaderCellDef mat-sort-header>Order ID</th>
        <td mat-cell *matCellDef=\"let row\">{{ row.id }}</td>
      </ng-container>

      <ng-container matColumnDef=\"customer\">
        <th mat-header-cell *matHeaderCellDef mat-sort-header>Customer</th>
        <td mat-cell *matCellDef=\"let row\">{{ row.customerName }}</td>
      </ng-container>

      <ng-container matColumnDef=\"total\">
        <th mat-header-cell *matHeaderCellDef mat-sort-header>Total</th>
        <td mat-cell *matCellDef=\"let row\">{{ row.total | currency }}</td>
      </ng-container>

      <tr mat-header-row *matHeaderRowDef=\"displayedColumns\"></tr>
      <tr mat-row *matRowDef=\"let row; columns: displayedColumns;\"></tr>
    </table>

    <mat-paginator [pageSizeOptions]=\"[10, 25, 50]\" showFirstLastButtons>
    </mat-paginator>
  `,
  styleUrl: './order-table.component.css',
  encapsulation: ViewEncapsulation.Emulated,  // default — scoped styles
})
export class OrderTableComponent implements AfterViewInit {
  displayedColumns = ['id', 'customer', 'total'];
  dataSource = new MatTableDataSource<Order>();

  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatPaginator) paginator!: MatPaginator;

  ngAfterViewInit() {
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
  }
}

/* order-table.component.css — scoped via emulated encapsulation */
:host {
  display: block;
  padding: 1rem;
}
:host(.compact) { font-size: 0.875rem; }""",
        "language": "typescript",
        "key_points": [
            "ng add @angular/material sets up theming, animations, and typography",
            "Pre-built accessible components: tables, dialogs, form fields, nav",
            "Theming via Sass palettes or CSS custom properties",
            "ViewEncapsulation.Emulated scopes styles; :host targets component root",
            "Angular CDK provides lower-level primitives Material builds on",
        ],
    },
}
