"""Additional Microsoft Azure interview topics — expands azure section to 50+."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("azure", "foundation"): [
        InterviewItem(
            "azure-vms",
            "When do you choose Azure VMs vs PaaS (App Service)?",
            "IaaS VMs give full OS control — lift-and-shift, custom software, legacy apps.",
            "",
        ),
        InterviewItem(
            "app-service-plan-skus",
            "Explain Azure App Service Plan SKUs and scaling options.",
            "Free/Shared for dev; Basic/Standard/Premium for production — scale up (SKU) vs scale out (instances).",
            "",
        ),
        InterviewItem(
            "azure-static-web-apps",
            "What are Azure Static Web Apps?",
            "Host Angular/React SPAs with CDN, free SSL, API integration, and GitHub Actions CI/CD.",
            "",
        ),
        InterviewItem(
            "azure-rbac",
            "How does Azure RBAC work?",
            "Role assignments grant permissions at scope (subscription, RG, resource) — least privilege via built-in/custom roles.",
            "",
        ),
        InterviewItem(
            "azure-dns",
            "What is Azure DNS and how do you configure custom domains?",
            "Host DNS zones in Azure — A/CNAME records point custom domains to App Service, Front Door, or SWA.",
            "",
        ),
    ],
    ("azure", "intermediate"): [
        InterviewItem(
            "azure-durable-functions",
            "What are Durable Functions and common orchestration patterns?",
            "Stateful serverless workflows — fan-out/fan-in, chaining, human interaction, long-running processes.",
            "",
        ),
        InterviewItem(
            "azure-logic-apps",
            "When do you use Logic Apps vs Azure Functions?",
            "Low-code workflow automation with 400+ connectors — B2B integration, approvals, scheduled ETL triggers.",
            "",
        ),
        InterviewItem(
            "azure-application-gateway",
            "What is Azure Application Gateway?",
            "Layer-7 load balancer with URL routing, SSL termination, session affinity, and optional WAF.",
            "",
        ),
        InterviewItem(
            "azure-waf",
            "What does Azure Web Application Firewall (WAF) protect against?",
            "OWASP Top 10 rules — SQL injection, XSS, bot protection on App Gateway, Front Door, or CDN.",
            "",
        ),
        InterviewItem(
            "azure-private-link",
            "Explain Azure Private Link and Private Endpoints.",
            "Private IP access to PaaS services over VNet — no public internet exposure for SQL, Storage, Key Vault.",
            "",
        ),
        InterviewItem(
            "azure-vpn-gateway",
            "What is Azure VPN Gateway?",
            "Site-to-site or point-to-site encrypted tunnels connecting on-premises networks to Azure VNets.",
            "",
        ),
        InterviewItem(
            "azure-traffic-manager",
            "How does Azure Traffic Manager route traffic?",
            "DNS-based global load balancer — priority, weighted, performance, or geographic routing profiles.",
            "",
        ),
        InterviewItem(
            "azure-signalr",
            "What is Azure SignalR Service?",
            "Managed real-time messaging — scales WebSocket connections for live dashboards, chat, notifications.",
            "",
        ),
        InterviewItem(
            "web-app-containers",
            "How do you run containerized apps on Azure App Service?",
            "Web App for Containers pulls from ACR/Docker Hub — custom images with CI/CD and managed scaling.",
            "",
        ),
    ],
    ("azure", "advanced"): [
        InterviewItem(
            "azure-expressroute",
            "Compare ExpressRoute vs VPN Gateway for hybrid connectivity.",
            "ExpressRoute is private dedicated fiber — higher bandwidth, lower latency, SLA; VPN uses public internet.",
            "",
        ),
        InterviewItem(
            "azure-policy",
            "What is Azure Policy and how does it enforce governance?",
            "Declarative rules audit or deny non-compliant resources — enforce tags, SKUs, regions at scale.",
            "",
        ),
        InterviewItem(
            "azure-sentinel",
            "What is Microsoft Sentinel?",
            "Cloud-native SIEM/SOAR — collect logs, detect threats with analytics rules, automate incident response.",
            "",
        ),
        InterviewItem(
            "azure-data-factory",
            "What is Azure Data Factory?",
            "Cloud ETL/ELT orchestration — copy/transform data between SQL, Blob, Cosmos DB, on-premises sources.",
            "",
        ),
        InterviewItem(
            "azure-devtest-labs",
            "What is Azure DevTest Labs?",
            "Self-service sandbox environments — policies, cost caps, auto-shutdown for dev/test VMs and artifacts.",
            "",
        ),
        InterviewItem(
            "azure-blueprints",
            "What are Azure Blueprints (now Template Specs)?",
            "Repeatable environment definitions — ARM/Bicep templates, RBAC, policies deployed as a single package.",
            "",
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "azure-vms": {
        "explanation": (
            "**Azure Virtual Machines (IaaS)** provide full control over the OS, runtime, and installed software — "
            "ideal for **lift-and-shift** legacy apps, custom middleware, Windows/SQL Server workloads requiring "
            "specific patches, or software not available on PaaS. You manage OS patching, scaling, and availability. "
            "**Choose PaaS (App Service, Azure Functions)** when you want managed runtime, built-in deployment slots, "
            "and auto-scale without VM maintenance. **Choose VMs when:** GPO/domain join, third-party agents, "
            "non-standard ports, or licensed software with per-VM licensing. Pair VMs with **Availability Sets/Zones**, "
            "**Azure Backup**, and **Update Management**."
        ),
        "code": """# Azure CLI — create .NET-ready Linux VM
az vm create \\
  --resource-group rg-prod \\
  --name vm-api-01 \\
  --image Ubuntu2204 \\
  --size Standard_D2s_v5 \\
  --admin-username azureuser \\
  --generate-ssh-keys \\
  --vnet-name vnet-prod \\
  --subnet snet-app

# Install .NET 8 and run API as systemd service
# Use VMSS (scale set) for horizontal scaling behind Load Balancer""",
        "language": "bash",
        "key_points": [
            "IaaS — you manage OS, patching, runtime, scaling",
            "Use for lift-and-shift, legacy, or custom software",
            "Availability Zones for 99.99% SLA across datacenters",
            "Prefer App Service/AKS when PaaS fits the workload",
        ],
    },
    "app-service-plan-skus": {
        "explanation": (
            "An **App Service Plan** defines the **compute resources** (VM size, count, features) shared by Web Apps, "
            "APIs, and Function Apps (Dedicated plan). **SKUs:** **Free/Shared** (dev only, no SLA), **Basic** (manual "
            "scale, custom domains), **Standard** (auto-scale, staging slots, daily backup), **Premium v3** (more "
            "CPU/memory, zone redundancy, faster instances). **Scale up** = bigger SKU; **scale out** = more instances. "
            "**Always On** (Standard+) prevents cold idle. **Interview tip:** right-size plan — one plan can host "
            "multiple apps; isolate prod and dev on separate plans."
        ),
        "code": """# Bicep — Standard S1 plan with auto-scale
resource plan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: 'plan-orders-prod'
  location: location
  sku: { name: 'S1', tier: 'Standard', capacity: 2 }
  properties: { reserved: false }
}

resource autoscale 'Microsoft.Insights/autoscaleSettings@2022-10-01' = {
  name: 'plan-autoscale'
  properties: {
    profiles: [{
      capacity: { minimum: '2', maximum: '10', default: '2' }
      rules: [{
        metricTrigger: { metricName: 'CpuPercentage', threshold: 70 }
        scaleAction: { direction: 'Increase', type: 'ChangeCount', value: '1' }
      }]
    }]
  }
}""",
        "language": "bicep",
        "key_points": [
            "Plan SKU defines CPU, RAM, features, and SLA",
            "Standard+ required for deployment slots and auto-scale",
            "Scale up (bigger SKU) vs scale out (more instances)",
            "Multiple apps can share one plan — isolate prod/dev",
        ],
    },
    "azure-static-web-apps": {
        "explanation": (
            "**Azure Static Web Apps (SWA)** hosts **static frontends** (Angular, React, Vue, Blazor WASM) on a "
            "global CDN with **free SSL**, **custom domains**, and **integrated CI/CD** from GitHub/Azure DevOps. "
            "The **`api/`** folder or linked Azure Functions provides serverless API backend. **Staging environments** "
            "auto-created per PR. **Authentication** built-in with Entra ID, GitHub, Google. **When to use:** SPA + "
            "light API, marketing sites, documentation. **When not:** heavy backend logic — use App Service or AKS instead. "
            "Pair with **Azure Front Door** for enterprise WAF and multi-region."
        ),
        "code": """# .github/workflows/azure-static-web-apps.yml
name: Deploy SWA
on:
  push:
    branches: [main]
jobs:
  build_and_deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Angular
        run: npm ci && npm run build -- --configuration production
      - uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_SWA_TOKEN }}
          app_location: "ClientApp"
          output_location: "dist/client-app/browser"
          api_location: "Api"  # optional Azure Functions""",
        "language": "yaml",
        "key_points": [
            "CDN-hosted SPA with GitHub Actions CI/CD",
            "PR preview environments auto-generated",
            "Built-in auth and optional Azure Functions API",
            "Free tier available; Standard for custom domains/WAF",
        ],
    },
    "azure-rbac": {
        "explanation": (
            "**Azure Role-Based Access Control (RBAC)** assigns **permissions** to Entra ID users, groups, or "
            "service principals at a **scope** (management group, subscription, resource group, resource). "
            "Effective permission = role assignment at scope + inherited parent scopes. **Built-in roles:** "
            "Owner, Contributor, Reader, plus service-specific roles (e.g., **Key Vault Secrets User**, "
            "**Storage Blob Data Contributor**). **Custom roles** define granular actions. "
            "**Least privilege:** grant minimum role at narrowest scope. **PIM** adds just-in-time elevated access."
        ),
        "code": """# Assign Key Vault Secrets User to App Service managed identity
az role assignment create \\
  --assignee-object-id <managed-identity-object-id> \\
  --assignee-principal-type ServicePrincipal \\
  --role "Key Vault Secrets User" \\
  --scope /subscriptions/<sub>/resourceGroups/rg-prod/providers/Microsoft.KeyVault/vaults/kv-orders

# Bicep role assignment
resource kvRole 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(keyVault.id, appService.id, 'SecretsUser')
  scope: keyVault
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', '4633458b-17de-408a-b874-0445c86b69e6')
    principalId: appService.identity.principalId
    principalType: 'ServicePrincipal'
  }
}""",
        "language": "bash",
        "key_points": [
            "Role + scope + assignee = permission grant",
            "Least privilege — narrow scope, minimum role",
            "Managed identities need explicit RBAC on target resources",
            "PIM for just-in-time privileged access",
        ],
    },
    "azure-dns": {
        "explanation": (
            "**Azure DNS** hosts DNS zones and records using Azure's name servers — manage **A**, **AAAA**, **CNAME**, "
            "**MX**, **TXT** records for custom domains. Point your registrar's NS records to Azure DNS or delegate "
            "subdomains. **App Service custom domain:** create CNAME (www) or A record (apex via ALIAS) + verify "
            "ownership TXT record. **Front Door / Traffic Manager:** CNAME to endpoint. **Private DNS zones** resolve "
            "names within VNets (e.g., `sql.internal.contoso.com` → private endpoint IP). "
            "Integrates with **Azure Certificate** (App Service Managed Certificate) for free TLS."
        ),
        "code": """# Create DNS zone and A record for API
az network dns zone create -g rg-prod -n contoso.com

az network dns record-set a add-record \\
  -g rg-prod -z contoso.com -n api \\
  -a <app-service-ip-or-frontdoor-ip>

# App Service — verify domain ownership
az webapp config hostname add \\
  --webapp-name order-api \\
  --resource-group rg-prod \\
  --hostname api.contoso.com

# Private DNS zone for internal PaaS resolution
az network private-dns zone create -g rg-prod -n privatelink.database.windows.net""",
        "language": "bash",
        "key_points": [
            "Azure DNS hosts public and private zones",
            "CNAME for subdomains; ALIAS/A for apex records",
            "TXT record verifies domain ownership for App Service",
            "Private DNS zones resolve private endpoint hostnames in VNet",
        ],
    },
    "azure-durable-functions": {
        "explanation": (
            "**Durable Functions** extend Azure Functions with **stateful orchestrations** — long-running, "
            "reliable workflows that survive restarts. Patterns: **function chaining**, **fan-out/fan-in** "
            "(parallel processing), **async HTTP APIs**, **monitoring**, **human interaction** (approval timeouts). "
            "Uses **event sourcing** — orchestration state stored in Azure Storage or Netherite/MSSQL. "
            "**Orchestrator** must be deterministic (no random, no direct I/O — call activity functions). "
            "Choose **Consumption**, **Premium**, or **Dedicated** plan depending on latency and VNet needs."
        ),
        "code": """[Function(nameof(OrderOrchestrator))]
public static async Task<OrderResult> OrderOrchestrator(
    [OrchestrationTrigger] TaskOrchestrationContext context)
{
    var order = context.GetInput<OrderRequest>()!;

    // Fan-out — process each line in parallel
    var tasks = order.Lines.Select(line =>
        context.CallActivityAsync<bool>("ValidateInventory", line));
    var results = await Task.WhenAll(tasks);

    if (results.Any(r => !r))
        return new OrderResult { Success = false };

    await context.CallActivityAsync("ChargePayment", order);
    await context.CallActivityAsync("SendConfirmation", order);
    return new OrderResult { Success = true };
}""",
        "language": "csharp",
        "key_points": [
            "Orchestrator functions must be deterministic",
            "Activity functions perform I/O and side effects",
            "Fan-out/fan-in for parallel batch processing",
            "State persisted — survives function restarts",
        ],
    },
    "azure-logic-apps": {
        "explanation": (
            "**Azure Logic Apps** is a **low-code integration** service with 400+ connectors (Office 365, SAP, SQL, "
            "Service Bus, Salesforce). Define workflows visually or in JSON — triggers (HTTP, schedule, queue) and "
            "actions (send email, transform JSON, call API). **When vs Functions:** Logic Apps for integration "
            "workflows, B2B (EDI/X12), approval flows, quick prototypes. Functions for custom code, performance-critical "
            "paths, complex business logic. **Standard (single-tenant)** runs in App Service environment with VNet; "
            "**Consumption** is serverless multi-tenant."
        ),
        "code": """// Logic App workflow definition (simplified JSON)
{
  "definition": {
    "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
    "triggers": {
      "When_order_placed": {
        "type": "ServiceBus",
        "inputs": {
          "queueName": "orders",
          "connection": "@parameters('serviceBusConnection')"
        }
      }
    },
    "actions": {
      "Parse_JSON": { "type": "ParseJson", "inputs": { "content": "@triggerBody()" } },
      "Send_email": {
        "type": "ApiConnection",
        "inputs": { "host": { "connection": { "name": "@parameters('office365')" } } }
      }
    }
  }
}""",
        "language": "json",
        "key_points": [
            "Low-code workflows with 400+ connectors",
            "Ideal for integration, approvals, scheduled ETL triggers",
            "Standard Logic Apps support VNet integration",
            "Use Functions when custom code or performance dominates",
        ],
    },
    "azure-application-gateway": {
        "explanation": (
            "**Azure Application Gateway** is a **Layer-7 (HTTP/HTTPS) load balancer** with **URL-based routing**, "
            "**SSL/TLS termination**, **cookie-based session affinity**, **WebSocket** support, and optional "
            "**WAF** integration. Unlike L4 Load Balancer, App Gateway understands HTTP headers and paths — "
            "route `/api/*` to backend pool A, `/static/*` to pool B. Deployed in a dedicated subnet "
            "(`GatewaySubnet` or dedicated AppGw subnet). **v2 SKU** supports autoscale and zone redundancy. "
            "Use with **App Service** (backend pool), **VMSS**, or **AKS Ingress**."
        ),
        "code": """# Bicep — Application Gateway with path-based routing
resource appGw 'Microsoft.Network/applicationGateways@2023-05-01' = {
  name: 'appgw-prod'
  properties: {
    sku: { name: 'WAF_v2', tier: 'WAF_v2', capacity: 2 }
    gatewayIPConfigurations: [ { name: 'gwip', properties: { subnet: { id: appGwSubnet.id } } } ]
    sslCertificates: [ { name: 'wildcard-contoso', properties: { /* Key Vault reference */ } } ]
    urlPathMaps: [{
      name: 'pathmap'
      properties: {
        pathRules: [{
          name: 'api-rule'
          properties: {
            paths: ['/api/*']
            backendAddressPool: { id: resourceId('Microsoft.Network/applicationGateways/backendAddressPools', 'appgw-prod', 'api-pool') }
          }
        }]
      }
    }]
  }
}""",
        "language": "bicep",
        "key_points": [
            "Layer-7 routing by URL path, host header, or query string",
            "SSL termination offloads TLS from backend servers",
            "WAF_v2 SKU includes Web Application Firewall",
            "Requires dedicated subnet; v2 supports autoscale",
        ],
    },
    "azure-waf": {
        "explanation": (
            "**Azure Web Application Firewall (WAF)** protects web apps from common exploits defined in **OWASP Core "
            "Rule Sets** (SQL injection, XSS, CSRF, file inclusion) and **bot protection**. Available on "
            "**Application Gateway WAF_v2**, **Azure Front Door Premium**, and **CDN Premium**. "
            "**Modes:** Detection (log only) vs Prevention (block). **Custom rules** match IP, geo, headers, rate "
            "limits. **Exclusions** prevent false positives on specific paths. In interviews, explain placing WAF "
            "at the **edge** before traffic reaches App Service or AKS ingress."
        ),
        "code": """# WAF custom rule — block requests from specific country
{
  "name": "BlockHighRiskCountries",
  "priority": 10,
  "ruleType": "MatchRule",
  "action": "Block",
  "matchConditions": [{
    "matchVariables": [{ "variableName": "RemoteAddr" }],
    "operator": "GeoMatch",
    "matchValues": ["KP", "IR"]
  }]
}

# Enable OWASP 3.2 managed rule set
{
  "managedRuleSets": [{
    "ruleSetType": "OWASP",
    "ruleSetVersion": "3.2"
  }]
}""",
        "language": "json",
        "key_points": [
            "OWASP Core Rule Sets block common web attacks",
            "Detection vs Prevention modes",
            "Available on App Gateway, Front Door Premium, CDN",
            "Custom rules for geo-blocking, rate limiting, IP allowlists",
        ],
    },
    "azure-private-link": {
        "explanation": (
            "**Azure Private Link** exposes PaaS services via **private IP addresses** inside your VNet using "
            "**Private Endpoints**. Traffic stays on the **Microsoft backbone** — never traverses the public internet. "
            "Supported services: Azure SQL, Storage, Key Vault, Cosmos DB, Service Bus, App Service (inbound), etc. "
            "Create a **Private DNS zone** (`privatelink.database.windows.net`) to resolve the service FQDN to "
            "private IP. **Contrast with Service Endpoints:** endpoints extend VNet identity to the service; "
            "Private Link brings the service into your VNet. Required for many compliance/regulatory architectures."
        ),
        "code": """# Bicep — private endpoint for Azure SQL
resource privateEndpoint 'Microsoft.Network/privateEndpoints@2023-05-01' = {
  name: 'pe-sql-orders'
  location: location
  properties: {
    subnet: { id: subnetData.id }
    privateLinkServiceConnections: [{
      name: 'sql-connection'
      properties: {
        privateLinkServiceId: sqlServer.id
        groupIds: ['sqlServer']
      }
    }]
  }
}

resource dnsGroup 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2023-05-01' = {
  parent: privateEndpoint
  name: 'default'
  properties: {
    privateDnsZoneConfigs: [{
      name: 'sql-dns'
      properties: {
        privateDnsZoneId: privateDnsZone.id
      }
    }]
  }
}""",
        "language": "bicep",
        "key_points": [
            "Private Endpoint assigns private IP in your VNet",
            "Traffic never leaves Azure backbone network",
            "Private DNS zone resolves service FQDN to private IP",
            "Required for many compliance and zero-trust designs",
        ],
    },
    "azure-vpn-gateway": {
        "explanation": (
            "**Azure VPN Gateway** sends encrypted traffic between Azure VNets and **on-premises** networks over "
            "the public internet. **Site-to-site (S2S):** IPsec/IKE tunnel from on-prem VPN device to Azure. "
            "**Point-to-site (P2S):** individual client VPN (OpenVPN, IKEv2). **VNet-to-VNet:** connect Azure "
            "regions. **Gateway SKUs:** Basic (dev), VpnGw1-5 (production bandwidth/throughput). "
            "**vs ExpressRoute:** VPN uses internet (cheaper, easier); ExpressRoute uses private dedicated circuit "
            "(higher bandwidth, lower latency, SLA). Often combined — VPN as ExpressRoute failover."
        ),
        "code": """# Create VPN Gateway (takes ~30-45 min)
az network vnet subnet create \\
  --resource-group rg-prod \\
  --vnet-name vnet-prod \\
  --name GatewaySubnet \\
  --address-prefixes 10.10.255.0/27

az network vnet-gateway create \\
  --resource-group rg-prod \\
  --name vpngw-prod \\
  --public-ip-address vpngw-pip \\
  --vnet vnet-prod \\
  --gateway-type Vpn \\
  --vpn-type RouteBased \\
  --sku VpnGw2 \\
  --vpn-gateway-generation Generation2

# Local network gateway = on-premises address space + public IP""",
        "language": "bash",
        "key_points": [
            "GatewaySubnet required — minimum /27 address space",
            "Site-to-site for datacenter; point-to-site for remote devs",
            "RouteBased (BGP) preferred over PolicyBased",
            "VPN over internet; ExpressRoute for dedicated private link",
        ],
    },
    "azure-traffic-manager": {
        "explanation": (
            "**Azure Traffic Manager** is a **DNS-based global traffic router** — clients resolve to the best "
            "endpoint based on routing method. **Priority:** active-passive failover (primary/secondary). "
            "**Weighted:** distribute traffic by percentage (canary, A/B). **Performance:** route to lowest-latency "
            "region. **Geographic:** route by user country/region (data sovereignty). "
            "**Contrast with Front Door:** Traffic Manager is DNS-level (TTL delay on failover); "
            "Front Door is HTTP reverse proxy with instant failover and WAF. Use both: TM for non-HTTP, "
            "Front Door for web apps."
        ),
        "code": """# Azure CLI — performance routing profile
az network traffic-manager profile create \\
  --resource-group rg-prod \\
  --name tm-orders-global \\
  --routing-method Performance \\
  --unique-dns-name orders-global \\
  --ttl 30

az network traffic-manager endpoint create \\
  --resource-group rg-prod \\
  --profile-name tm-orders-global \\
  --name eastus-endpoint \\
  --type azureTargets \\
  --target-resource-id <app-service-eastus-id> \\
  --endpoint-status Enabled

# CNAME: orders.contoso.com → orders-global.trafficmanager.net""",
        "language": "bash",
        "key_points": [
            "DNS-based routing — not an HTTP reverse proxy",
            "Performance, Priority, Weighted, Geographic methods",
            "Failover delay depends on DNS TTL (typically 30-60s)",
            "Pair with Front Door for HTTP apps needing instant failover",
        ],
    },
    "azure-signalr": {
        "explanation": (
            "**Azure SignalR Service** is a **fully managed** real-time messaging layer that scales WebSocket and "
            "SSE connections — offloads connection management from your app server. Your ASP.NET Core app uses "
            "the same **SignalR API**; the service handles connection fan-out across instances. "
            "**Use cases:** live dashboards, chat, notifications, collaborative editing. "
            "**Modes:** Default (serverless with Azure Functions), Classic (app server owns hub logic), "
            "**Premium** (regional, multi-unit scale). Solves the **scale-out problem** where sticky sessions "
            "alone cannot broadcast across all App Service instances."
        ),
        "code": """// Program.cs — connect to Azure SignalR Service
builder.Services.AddSignalR()
    .AddAzureSignalR(builder.Configuration["Azure:SignalR:ConnectionString"]);

app.MapHub<OrderHub>("/hubs/orders");

// Hub — same code as self-hosted SignalR
public class OrderHub : Hub
{
    public async Task JoinOrderGroup(int orderId) =>
        await Groups.AddToGroupAsync(Context.ConnectionId, $"order-{orderId}");

    public async Task NotifyStatusChange(int orderId, string status) =>
        await Clients.Group($"order-{orderId}").SendAsync("StatusChanged", status);
}""",
        "language": "csharp",
        "key_points": [
            "Managed service scales WebSocket connections globally",
            "Same ASP.NET Core SignalR API — minimal code change",
            "Solves broadcast across multiple App Service instances",
            "Premium tier for SLA and multi-unit regional scale",
        ],
    },
    "web-app-containers": {
        "explanation": (
            "**Web App for Containers** runs **custom Docker images** on App Service — pull from **Azure Container "
            "Registry (ACR)**, Docker Hub, or private registry. Combines container flexibility with PaaS benefits: "
            "managed scaling, deployment slots, custom domains, TLS. Configure via `linuxFxVersion: DOCKER|<image>`. "
            "**CI/CD:** GitHub Actions or Azure Pipelines build/push to ACR, then deploy to Web App. "
            "**When vs AKS:** Web App for Containers for simple container hosting; AKS for orchestration, "
            "service mesh, complex microservices. Enable **Managed Identity** to pull from ACR without credentials."
        ),
        "code": """# Create Web App for Containers
az acr create -g rg-prod -n myregistry --sku Basic
az acr build -r myregistry -t order-api:v1 .

az appservice plan create -g rg-prod -n plan-containers --is-linux --sku P1v3
az webapp create -g rg-prod -p plan-containers -n order-api \\
  --deployment-container-image-name myregistry.azurecr.io/order-api:v1

# Enable managed identity + AcrPull role
az webapp identity assign -g rg-prod -n order-api
az role assignment create --assignee <principal-id> --role AcrPull --scope <acr-id>""",
        "language": "bash",
        "key_points": [
            "Run custom Docker images on managed App Service",
            "Pull from ACR with managed identity (no passwords)",
            "Deployment slots work with containers",
            "Simpler than AKS for single-container web apps",
        ],
    },
    "azure-expressroute": {
        "explanation": (
            "**Azure ExpressRoute** provides **private dedicated connectivity** between on-premises datacenters and "
            "Azure via a connectivity provider (Equinix, AT&T, etc.) — traffic does **not** traverse the public internet. "
            "**Higher bandwidth** (50 Mbps to 100 Gbps), **lower latency**, **consistent performance**, and **SLA**. "
            "**Models:** Provider edge, provider backbone, Microsoft peering (Office 365, Azure public services), "
            "Private peering (VNet access). **ExpressRoute Gateway** connects VNets to the circuit. "
            "**Coexist with VPN:** use VPN as backup when ExpressRoute fails. Required for strict compliance, "
            "large data migration, or hybrid architectures at enterprise scale."
        ),
        "code": """/*
  ExpressRoute topology
  On-Prem Datacenter
       │
       │  Dedicated private fiber (via provider)
       ▼
  ExpressRoute Circuit ──► ExpressRoute Gateway (in GatewaySubnet)
                               │
                               ├── Private Peering → VNet (10.0.0.0/16)
                               └── Microsoft Peering → Azure PaaS public IPs

  Backup: Site-to-Site VPN tunnel (over internet) — automatic failover
*/

# Link VNet to ExpressRoute circuit
az network vpn-gateway create \\
  --name ergw-prod --resource-group rg-prod \\
  --vnet vnet-prod --gateway-type ExpressRoute \\
  --sku Standard""",
        "language": "text",
        "key_points": [
            "Private dedicated connection — not over public internet",
            "Bandwidth 50 Mbps to 100 Gbps with SLA",
            "Private peering for VNet; Microsoft peering for PaaS",
            "VPN as backup path for circuit failure",
        ],
    },
    "azure-policy": {
        "explanation": (
            "**Azure Policy** enforces **organizational standards** at scale — audit or **deny** non-compliant "
            "resource creation. Examples: require `Environment` tag, restrict VM SKUs to approved list, "
            "enforce HTTPS-only Storage, limit allowed Azure regions. **Initiatives** group related policies. "
            "**Effects:** Audit, Deny, DeployIfNotExists (remediate), Modify (add tags). Assign at subscription, "
            "MG, or RG scope. Complements **RBAC** (who can act) with **what they can create**. "
            "Integrates with **Azure Blueprints/Template Specs** for landing zones."
        ),
        "code": """// Policy definition — require Environment tag on resources
{
  "properties": {
    "displayName": "Require Environment tag",
    "policyRule": {
      "if": {
        "allOf": [
          { "field": "type", "equals": "Microsoft.Web/sites" },
          { "field": "tags['Environment']", "exists": "false" }
        ]
      },
      "then": { "effect": "deny" }
    }
  }
}

# Assign policy at subscription scope
az policy assignment create \\
  --name require-env-tag \\
  --policy RequireEnvironmentTag \\
  --scope /subscriptions/<sub-id>""",
        "language": "json",
        "key_points": [
            "Deny, Audit, DeployIfNotExists, Modify effects",
            "Initiatives bundle related policies together",
            "Complements RBAC — governs resource configuration",
            "Use for tagging, SKU restrictions, region allowlists",
        ],
    },
    "azure-sentinel": {
        "explanation": (
            "**Microsoft Sentinel** is a cloud-native **SIEM (Security Information and Event Management)** and "
            "**SOAR (Security Orchestration, Automation, Response)** platform. Collect logs from Azure services, "
            "on-premises, firewalls, Entra ID, Office 365 via **Data Connectors**. **Analytics rules** detect "
            "threats (KQL queries, ML, fusion). **Incidents** aggregate related alerts. **Playbooks** (Logic Apps) "
            "automate response — disable account, block IP, create ticket. **Workbooks** visualize security posture. "
            "Billing based on **GB ingested** — tune data retention and use Basic logs where appropriate."
        ),
        "code": """// KQL analytics rule — detect brute-force sign-in failures
SigninLogs
| where TimeGenerated > ago(1h)
| where ResultType != 0  // failed sign-in
| summarize FailedAttempts = count() by UserPrincipalName, IPAddress
| where FailedAttempts > 10
| project UserPrincipalName, IPAddress, FailedAttempts

// Automated response playbook (Logic App triggered by Sentinel incident)
// 1. Get incident details
// 2. Disable user in Entra ID (Graph API)
// 3. Block IP in Azure Firewall
// 4. Post to Teams channel""",
        "language": "sql",
        "key_points": [
            "SIEM + SOAR — collect, detect, respond",
            "KQL analytics rules for threat detection",
            "Playbooks automate incident response via Logic Apps",
            "Pay per GB ingested — tune retention and connectors",
        ],
    },
    "azure-data-factory": {
        "explanation": (
            "**Azure Data Factory (ADF)** is a cloud **ETL/ELT orchestration** service — visually or programmatically "
            "define pipelines that **copy**, **transform**, and **move data** between sources. **Activities:** Copy "
            "(bulk data movement), Data Flow (Spark-based transform), Lookup, ForEach, If Condition. "
            "**Linked Services** define connections (Azure SQL, Blob, Cosmos DB, on-prem SQL via **Integration Runtime**). "
            "**Triggers:** schedule, tumbling window, event-based (Storage blob created). "
            "**Use when:** nightly warehouse loads, data lake ingestion, hybrid on-prem → cloud migration."
        ),
        "code": """// ADF Copy activity pipeline (JSON concept)
{
  "name": "CopyOrdersToDataLake",
  "properties": {
    "activities": [{
      "name": "CopyOrders",
      "type": "Copy",
      "inputs": [{ "referenceName": "AzureSqlOrders", "type": "DatasetReference" }],
      "outputs": [{ "referenceName": "ParquetDataLake", "type": "DatasetReference" }],
      "typeProperties": {
        "source": { "type": "AzureSqlSource", "sqlReaderQuery": "SELECT * FROM Orders WHERE ModifiedAt > @{pipeline().parameters.lastRun}" },
        "sink": { "type": "ParquetSink" }
      }
    }],
    "parameters": { "lastRun": { "type": "String" } }
  }
}""",
        "language": "json",
        "key_points": [
            "Copy activity for bulk data movement between sources",
            "Self-hosted Integration Runtime for on-premises access",
            "Mapping Data Flows for Spark-based transformations",
            "Schedule or event triggers for automated pipelines",
        ],
    },
    "azure-devtest-labs": {
        "explanation": (
            "**Azure DevTest Labs** provides **self-service sandbox environments** for developers and testers — "
            "pre-configured **artifacts** (install .NET SDK, SQL Server, Docker), **formulas** (VM templates), "
            "and **policies** (max VMs per user, allowed VM sizes, auto-shutdown schedule). "
            "**Cost control:** auto-shutdown at 7 PM, cap total lab spend, restrict expensive SKUs. "
            "**Reusable artifacts** from GitHub or custom scripts. Integrates with **Azure DevOps** for "
            "environment provisioning in pipelines. Ideal for **training**, **POC**, and **QA** — not production workloads."
        ),
        "code": """# Create DevTest Lab with auto-shutdown policy
az labs create \\
  --resource-group rg-devtest \\
  --name devtest-orders \\
  --location eastus

az labs policy create \\
  --lab-name devtest-orders \\
  --resource-group rg-devtest \\
  --name auto-shutdown \\
  --policy-set vm \\
  --name auto-shutdown \\
  --threshold 0 \\
  --fact-name AutoShutdown \\
  --fact-data '{"timeZoneId":"Eastern Standard Time","dailyRecurrence":{"time":"1900"}}'

# Developer creates VM from formula with pre-installed .NET 8 artifact""",
        "language": "bash",
        "key_points": [
            "Self-service VMs with cost policies and auto-shutdown",
            "Artifacts automate software installation on VM creation",
            "Cap spend and restrict VM SKUs per user or lab",
            "For dev/test/training — not production workloads",
        ],
    },
    "azure-blueprints": {
        "explanation": (
            "**Azure Blueprints** (evolving toward **Template Specs** and **Deployment Stacks**) package "
            "repeatable **landing zone** definitions — ARM/Bicep templates, **RBAC role assignments**, and "
            "**Azure Policy** initiatives deployed as a **single atomic package**. Enforce compliance from "
            "day one: logging, networking, tags, security baselines. **Blueprint definition** → published "
            "version → assigned to subscription. **Artifacts** can include Resource Groups, templates, policies, "
            "role assignments. **Interview context:** enterprise cloud adoption frameworks (CAF) use blueprints "
            "for consistent, auditable environment provisioning vs ad-hoc resource creation."
        ),
        "code": """// Template Spec — modern replacement for Blueprint artifacts
resource templateSpec 'Microsoft.Resources/templateSpecs@2022-02-01' = {
  name: 'landing-zone-prod'
  location: location
  properties: { displayName: 'Production Landing Zone' }
}

resource templateSpecVersion 'Microsoft.Resources/templateSpecs/versions@2022-02-01' = {
  parent: templateSpec
  name: '1.0.0'
  properties: {
    mainTemplate: {
      '$schema': 'https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#'
      contentVersion: '1.0.0.0'
      resources: [
        /* VNet, Log Analytics, Key Vault, Policy assignments */
      ]
    }
  }
}

// Deploy template spec to new subscription
az deployment sub create \\
  --location eastus \\
  --template-spec /subscriptions/<sub>/resourceGroups/rg/providers/Microsoft.Resources/templateSpecs/landing-zone-prod/versions/1.0.0""",
        "language": "bicep",
        "key_points": [
            "Package templates + RBAC + policies as one deployable unit",
            "Template Specs are the modern Blueprint artifact approach",
            "Landing zones enforce compliance from first deployment",
            "Used in Cloud Adoption Framework (CAF) enterprise adoption",
        ],
    },
}
