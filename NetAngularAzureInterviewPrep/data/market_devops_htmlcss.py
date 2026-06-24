"""Market-relevant Docker/DevOps and HTML/CSS interview topics (2025/2026)."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("optional", "foundation"): [
        InterviewItem(
            "k8s-pods-services-deployments",
            "Explain Kubernetes Pods, Services, and Deployments.",
            "**Pod** = smallest deployable unit (one or more containers). **Service** = stable network endpoint. **Deployment** = declarative rolling updates for Pods.",
            """apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-api
spec:
  replicas: 3
  selector:
    matchLabels: { app: order-api }
  template:
    metadata:
      labels: { app: order-api }
    spec:
      containers:
      - name: api
        image: myacr.azurecr.io/order-api:1.2.0
        ports: [{ containerPort: 8080 }]
---
apiVersion: v1
kind: Service
metadata:
  name: order-api-svc
spec:
  selector: { app: order-api }
  ports: [{ port: 80, targetPort: 8080 }]
  type: ClusterIP""",
            "yaml",
            key_points=["Pod = ephemeral; use Deployments for stateless apps", "Service provides stable DNS inside cluster", "Deployment handles rollouts and rollbacks"],
        ),
        InterviewItem(
            "docker-multistage-builds",
            "What are multi-stage Docker builds and why use them?",
            "Separate build and runtime stages so production images contain only compiled output — smaller attack surface and faster pulls.",
            """FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY *.csproj ./
RUN dotnet restore
COPY . .
RUN dotnet publish -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app
COPY --from=build /app/publish .
USER appuser
EXPOSE 8080
ENTRYPOINT [\"dotnet\", \"OrderApi.dll\"]""",
            "dockerfile",
            key_points=["Final stage excludes SDK and source", "Copy csproj first for layer cache", "Run as non-root in runtime stage"],
        ),
        InterviewItem(
            "docker-networking",
            "How does Docker networking work?",
            "Containers join **bridge**, **host**, or **overlay** networks. Compose creates a default network; services reach each other by name.",
            """# docker-compose.yml
services:
  api:
    build: .
    networks: [app-net]
  db:
    image: postgres:16
    networks: [app-net]
networks:
  app-net:
    driver: bridge

# Inspect: docker network inspect app-net
# Custom bridge: docker network create my-net""",
            "yaml",
            key_points=["Default bridge isolates containers", "Service name = DNS hostname in Compose", "Overlay networks for Swarm/K8s CNI"],
        ),
        InterviewItem(
            "docker-volumes",
            "Explain Docker volumes vs bind mounts.",
            "**Volumes** are managed by Docker and persist data outside container lifecycle. **Bind mounts** map host paths — good for dev hot-reload.",
            """services:
  db:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data   # named volume
  api:
    build: .
    volumes:
      - ./src:/app/src:ro                 # bind mount (dev only)

volumes:
  pgdata:""",
            "yaml",
            key_points=["Named volumes survive container removal", "Bind mounts tie to host filesystem", "Never store DB data in container layer"],
        ),
        InterviewItem(
            "k8s-secrets-configmaps",
            "What are Kubernetes Secrets and ConfigMaps?",
            "**ConfigMaps** store non-sensitive config; **Secrets** store sensitive data (base64-encoded, not encrypted at rest by default).",
            """apiVersion: v1
kind: ConfigMap
metadata:
  name: order-api-config
data:
  ASPNETCORE_ENVIRONMENT: Production
  LogLevel__Default: Information
---
apiVersion: v1
kind: Secret
metadata:
  name: order-api-secrets
type: Opaque
stringData:
  ConnectionStrings__Sql: \"Server=sql;Database=Orders;...\"
---
# Mount in Deployment:
# envFrom: [{ configMapRef: { name: order-api-config } }]
# env: [{ name: ConnectionStrings__Sql, valueFrom: { secretKeyRef: { name: order-api-secrets, key: ConnectionStrings__Sql } } }]""",
            "yaml",
            key_points=["ConfigMap for settings, Secret for credentials", "Prefer Azure Key Vault + CSI driver in prod", "Never commit Secrets to Git"],
        ),
        InterviewItem(
            "azure-container-registry",
            "What is Azure Container Registry (ACR)?",
            "Managed private Docker registry in Azure. Integrates with AKS, App Service, and pipelines via service connections.",
            """# Push image to ACR
az acr login --name myregistry
docker tag order-api:1.0 myregistry.azurecr.io/order-api:1.0
docker push myregistry.azurecr.io/order-api:1.0

# AKS pull with managed identity (no admin creds)
az aks update -g rg -n myaks --attach-acr myregistry""",
            "bash",
            key_points=["Use SKU tiers: Basic/Standard/Premium", "Enable vulnerability scanning (Defender)", "Attach ACR to AKS for pull without secrets"],
        ),
        InterviewItem(
            "semantic-versioning",
            "Explain semantic versioning (SemVer).",
            "**MAJOR.MINOR.PATCH** — breaking change, new feature, bug fix. Tags Docker images and NuGet packages consistently.",
            """# Git tag examples
git tag v1.0.0    # initial release
git tag v1.1.0    # new feature, backward compatible
git tag v1.1.1    # patch fix

# NuGet / Docker tag alignment
docker tag order-api myacr.azurecr.io/order-api:1.1.0
dotnet pack -p:PackageVersion=1.1.0""",
            "bash",
            key_points=["MAJOR = breaking API changes", "Pre-release suffix: 1.0.0-beta.1", "Align Git tags, NuGet, and container tags"],
        ),
        InterviewItem(
            "nuget-package-management",
            "How do you manage NuGet packages in .NET projects?",
            "Use **Central Package Management**, lock files, and private feeds (Azure Artifacts). Pin versions for reproducible builds.",
            """<!-- Directory.Packages.props -->
<Project>
  <PropertyGroup>
    <ManagePackageVersionsCentrally>true</ManagePackageVersionsCentrally>
  </PropertyGroup>
  <ItemGroup>
    <PackageVersion Include=\"Microsoft.EntityFrameworkCore\" Version=\"8.0.11\" />
    <PackageVersion Include=\"Serilog.AspNetCore\" Version=\"8.0.3\" />
  </ItemGroup>
</Project>

<!-- OrderApi.csproj -->
<ItemGroup>
  <PackageReference Include=\"Microsoft.EntityFrameworkCore\" />
</ItemGroup>""",
            "xml",
            key_points=["Central Package Management avoids version drift", "Use nuget.config for feed sources", "Audit packages with dotnet list package --vulnerable"],
        ),
    ],
    ("optional", "intermediate"): [
        InterviewItem(
            "k8s-helm-charts",
            "What are Helm charts in Kubernetes?",
            "Helm packages K8s manifests as **charts** with templated values — install, upgrade, and rollback releases.",
            """# Chart structure: charts/order-api/
#   Chart.yaml, values.yaml, templates/deployment.yaml

# values.yaml
replicaCount: 3
image:
  repository: myacr.azurecr.io/order-api
  tag: \"1.2.0\"

# Install / upgrade
helm upgrade --install order-api ./charts/order-api -f values-prod.yaml
helm rollback order-api 2""",
            "yaml",
            key_points=["Helm = package manager for K8s", "values.yaml per environment (dev/staging/prod)", "helm rollback for fast recovery"],
        ),
        InterviewItem(
            "k8s-ingress-controllers",
            "What is a Kubernetes Ingress controller?",
            "Ingress routes external HTTP/S traffic to Services. Controllers (NGINX, Traefik, Azure App Gateway) implement the Ingress spec.",
            """apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: order-api-ingress
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  ingressClassName: nginx
  tls:
  - hosts: [api.example.com]
    secretName: api-tls
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: order-api-svc
            port: { number: 80 }""",
            "yaml",
            key_points=["Ingress = L7 routing + TLS termination", "Needs an Ingress Controller installed", "AKS: Application Gateway or NGINX add-on"],
        ),
        InterviewItem(
            "k8s-liveness-readiness-probes",
            "Explain liveness and readiness probes in Kubernetes.",
            "**Liveness** restarts unhealthy containers. **Readiness** removes Pod from Service endpoints until ready — prevents traffic to starting apps.",
            """containers:
- name: api
  livenessProbe:
    httpGet:
      path: /health/live
      port: 8080
    initialDelaySeconds: 15
    periodSeconds: 10
  readinessProbe:
    httpGet:
      path: /health/ready
      port: 8080
    initialDelaySeconds: 5
    periodSeconds: 5""",
            "yaml",
            key_points=["Liveness = is process alive?", "Readiness = can accept traffic?", "Use separate /health/live and /health/ready endpoints"],
        ),
        InterviewItem(
            "github-actions-cicd",
            "How do you set up CI/CD with GitHub Actions?",
            "Workflow YAML triggers on push/PR; jobs run build, test, and deploy steps on hosted or self-hosted runners.",
            """name: CI/CD
on:
  push:
    branches: [main]
jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with: { dotnet-version: '8.0.x' }
      - run: dotnet restore && dotnet test --no-restore
      - run: docker build -t order-api:${{ github.sha }} .
      - uses: azure/docker-login@v2
        with:
          login-server: myacr.azurecr.io
          username: ${{ secrets.ACR_USERNAME }}
          password: ${{ secrets.ACR_PASSWORD }}
      - run: docker push myacr.azurecr.io/order-api:${{ github.sha }}""",
            "yaml",
            key_points=["Secrets stored in repo/org settings", "Matrix builds for multi-target testing", "Reusable workflows reduce duplication"],
        ),
        InterviewItem(
            "azure-pipelines-yaml",
            "How do Azure Pipelines YAML pipelines work?",
            "Declarative multi-stage pipelines with triggers, variables, and template reuse. Integrates with Azure DevOps repos and ACR/AKS.",
            """trigger:
  branches: { include: [main] }

stages:
- stage: Build
  jobs:
  - job: BuildAndTest
    pool: { vmImage: 'ubuntu-latest' }
    steps:
    - task: UseDotNet@2
      inputs: { version: '8.x' }
    - script: dotnet test --configuration Release
    - task: Docker@2
      inputs:
        containerRegistry: 'acr-connection'
        repository: 'order-api'
        command: 'buildAndPush'
        tags: '$(Build.BuildId)'

- stage: Deploy
  dependsOn: Build
  jobs:
  - deployment: DeployAKS
    environment: production
    strategy:
      runOnce:
        deploy:
          steps:
          - task: KubernetesManifest@1
            inputs:
              action: 'deploy'
              manifests: 'k8s/deployment.yaml'""",
            "yaml",
            key_points=["Stages separate build from deploy", "Environments add approval gates", "Variable groups for secrets"],
        ),
        InterviewItem(
            "container-security-scanning",
            "How do you scan container images for vulnerabilities?",
            "Scan in CI with Trivy, Snyk, or ACR Defender. Fail builds on critical CVEs; pin base image digests.",
            """# GitHub Actions — Trivy scan
- name: Scan image
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: myacr.azurecr.io/order-api:${{ github.sha }}
    severity: 'CRITICAL,HIGH'
    exit-code: '1'

# ACR: enable Microsoft Defender for Cloud
# az acr update -n myregistry --admin-enabled false""",
            "yaml",
            key_points=["Scan on every build before push", "Use minimal distroless or alpine bases", "Patch base images regularly"],
        ),
        InterviewItem(
            "gitflow-vs-trunk",
            "Compare GitFlow vs trunk-based development.",
            "**GitFlow** uses long-lived develop/release branches — good for scheduled releases. **Trunk-based** commits to main with short feature branches — ideal for CI/CD.",
            """# Trunk-based (recommended for CI/CD)
git checkout -b feat/order-search
# small commits, PR to main, merge within 1-2 days
git push origin feat/order-search

# GitFlow
# main (prod) ← release/1.2 ← develop ← feature/order-search
# hotfix/1.1.1 branches from main for urgent fixes""",
            "bash",
            key_points=["Trunk-based + feature flags = continuous delivery", "GitFlow suits release trains and legacy teams", "Keep branches short-lived regardless of model"],
        ),
        InterviewItem(
            "sonarqube-code-quality",
            "What is SonarQube and how is it used in CI?",
            "Static analysis for bugs, code smells, coverage, and security hotspots. Quality gates block merges on failing metrics.",
            """# Azure Pipeline step
- task: SonarQubePrepare@6
  inputs:
    SonarQube: 'SonarQubeConnection'
    scannerMode: 'dotnet'
    projectKey: 'OrderApi'
- script: dotnet build --no-incremental
- task: SonarQubeAnalyze@6
- task: SonarQubePublish@6
  inputs:
    pollingTimeoutSec: '300'

# Quality gate: coverage > 80%, 0 blocker issues""",
            "yaml",
            key_points=["Integrates with PR decoration", "Tracks technical debt over time", "Distinguish from SAST — SonarQube is broader quality"],
        ),
    ],
    ("optional", "advanced"): [
        InterviewItem(
            "prometheus-grafana-monitoring",
            "How do Prometheus and Grafana work together?",
            "Prometheus **scrapes metrics** from /metrics endpoints; Grafana **visualizes** dashboards and alerts.",
            """# ASP.NET Core — prometheus-net
app.MapMetrics();  // exposes /metrics

# prometheus.yml
scrape_configs:
  - job_name: 'order-api'
    static_configs:
      - targets: ['order-api:8080']

# Grafana dashboard: request rate, p95 latency, error rate
# Alert: rate(http_requests_total{status=~\"5..\"}[5m]) > 0.1""",
            "yaml",
            key_points=["Pull-based metrics model", "Use histograms for latency percentiles", "Alert on SLIs: availability, latency, errors"],
        ),
        InterviewItem(
            "iac-comparison",
            "Compare Terraform, Bicep, ARM, and Pulumi for IaC.",
            "All declare desired infrastructure state. Terraform is multi-cloud HCL; Bicep/ARM are Azure-native; Pulumi uses real programming languages.",
            """# Terraform
resource \"azurerm_kubernetes_cluster\" \"aks\" {
  name                = \"myaks\"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  default_node_pool { name = \"default\"; node_count = 2; vm_size = \"Standard_D2s_v3\" }
}

# Bicep equivalent
resource aks 'Microsoft.ContainerService/managedClusters@2023-07-01' = {
  name: 'myaks'
  location: location
  properties: { agentPoolProfiles: [{ name: 'default', count: 2, vmSize: 'Standard_D2s_v3' }] }
}""",
            "hcl",
            key_points=["Terraform state file needs remote backend", "Bicep compiles to ARM — no state file", "Choose based on cloud scope and team skills"],
        ),
        InterviewItem(
            "container-orchestration-concepts",
            "What are core container orchestration concepts?",
            "Orchestrators schedule containers, handle scaling, self-healing, service discovery, and rolling updates across a cluster.",
            """# Desired state: 3 replicas always running
kubectl scale deployment order-api --replicas=3

# Self-healing: delete a pod, Deployment recreates it
kubectl delete pod order-api-abc123

# Horizontal scaling
kubectl autoscale deployment order-api --min=2 --max=10 --cpu-percent=70""",
            "bash",
            key_points=["Declarative desired state vs imperative commands", "Scheduler places Pods on nodes by resources", "K8s, Docker Swarm, Nomad are orchestrators"],
        ),
        InterviewItem(
            "devsecops",
            "What is DevSecOps?",
            "Integrates security into every CI/CD stage — shift-left scanning, least privilege, secrets management, and compliance as code.",
            """# DevSecOps pipeline stages:
# 1. Pre-commit: secret scanning (gitleaks)
# 2. Build: SAST (SonarQube), dependency audit (dotnet list package --vulnerable)
# 3. Container: image scan (Trivy)
# 4. Deploy: policy checks (OPA/Kyverno), RBAC least privilege
# 5. Runtime: WAF, network policies, Defender for Cloud""",
            "text",
            key_points=["Security gates in pipeline, not after deploy", "Automate compliance checks", "Culture: devs own security basics"],
        ),
        InterviewItem(
            "sast-dast",
            "Explain SAST vs DAST security testing.",
            "**SAST** analyzes source code statically (SonarQube, Semgrep). **DAST** tests running apps externally (OWASP ZAP, Burp).",
            """# SAST — run in CI on source
dotnet tool install --global security-scan
security-scan ./OrderApi.sln

# DAST — scan staging environment
docker run -t owasp/zap2docker-stable zap-baseline.py \\
  -t https://staging-api.example.com/swagger""",
            "bash",
            key_points=["SAST finds issues early, may have false positives", "DAST finds runtime/config issues", "Use both in a defense-in-depth strategy"],
        ),
        InterviewItem(
            "elk-stack",
            "What is the ELK stack?",
            "**Elasticsearch** stores/logs search, **Logstash/Fluentd** ingests, **Kibana** visualizes. Azure alternative: **Azure Monitor + Log Analytics**.",
            """# Serilog → Elasticsearch sink
Log.Logger = new LoggerConfiguration()
    .WriteTo.Console()
    .WriteTo.Elasticsearch(new ElasticsearchSinkOptions(new Uri(\"http://elastic:9200\"))
    {
        AutoRegisterTemplate = true,
        IndexFormat = \"order-api-{0:yyyy.MM.dd}\"
    })
    .CreateLogger();

# Kibana: search logs, build dashboards, set alerts""",
            "csharp",
            key_points=["Structured logging (JSON) enables powerful queries", "Index per day for retention management", "Correlate logs with trace IDs"],
        ),
        InterviewItem(
            "ansible-basics",
            "What is Ansible and when do you use it?",
            "Agentless configuration management using YAML playbooks over SSH. Complements containers — configures VMs, installs agents, bootstraps nodes.",
            """# playbook.yml — install Docker on Ubuntu VMs
- hosts: webservers
  become: yes
  tasks:
    - name: Install Docker
      apt:
        name: docker.io
        state: present
        update_cache: yes
    - name: Start Docker
      service:
        name: docker
        state: started
        enabled: yes""",
            "yaml",
            key_points=["Idempotent tasks — safe to re-run", "Inventory defines target hosts", "Use for VM config; K8s for container orchestration"],
        ),
        InterviewItem(
            "zero-downtime-deployments",
            "How do you achieve zero-downtime deployments?",
            "Rolling updates, blue-green, or canary releases with health checks ensure traffic never hits unhealthy instances.",
            """# K8s rolling update (default strategy)
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0

# App Service deployment slots
az webapp deployment slot swap -g rg -n order-api --slot staging --target-slot production

# Readiness probe ensures new pods accept traffic only when ready""",
            "yaml",
            key_points=["maxUnavailable: 0 keeps full capacity during rollout", "Blue-green: instant swap after validation", "Database migrations need backward-compatible changes"],
        ),
    ],
    ("htmlcss", "foundation"): [
        InterviewItem(
            "css-box-model",
            "Explain the CSS box model.",
            "Every element is a box: **content → padding → border → margin**. `box-sizing: border-box` includes padding/border in width.",
            """.card {
  box-sizing: border-box;
  width: 300px;
  padding: 16px;
  border: 2px solid #ccc;
  margin: 8px;
}""",
            "css",
            key_points=["content-box (default) vs border-box", "Margin collapse between adjacent blocks", "Use border-box globally for predictable layouts"],
        ),
        InterviewItem(
            "css-specificity",
            "How does CSS specificity work?",
            "Specificity score: inline (1000) > ID (100) > class/attribute/pseudo-class (10) > element (1). `!important` overrides normal rules.",
            """.card .title { color: blue; }       /* 0-1-1 */
.card-title { color: red; }             /* 0-2-0 — wins */""",
            "css",
            key_points=["Avoid !important except utilities", "ID selectors are hard to override", "Keep selectors shallow for maintainability"],
        ),
        InterviewItem(
            "css-custom-properties",
            "What are CSS custom properties (variables)?",
            "Runtime themable values declared with `--name` and used with `var()`. Cascade and inherit unlike SASS variables.",
            """:root {
  --color-primary: #512BD4;
  --spacing-md: 1rem;
}
.btn-primary { background: var(--color-primary); padding: var(--spacing-md); }
[data-theme=\"dark\"] { --color-primary: #7B68EE; }""",
            "css",
            key_points=["Scoped by selector — inherit down DOM", "Change at runtime without rebuild", "Fallback: var(--color, #000)"],
        ),
        InterviewItem(
            "css-units-rem-em",
            "Explain CSS units: rem, em, vh, vw.",
            "**rem** = root font-size (accessible scaling). **em** = parent font-size. **vh/vw** = viewport percentage.",
            """html { font-size: 16px; }
.hero { min-height: 100vh; }
.card { padding: 1.5rem; }
.card h3 { font-size: 1.25em; }""",
            "css",
            key_points=["Prefer rem for spacing and typography", "vh problematic on mobile (address bar)", "Use clamp() for fluid typography"],
        ),
        InterviewItem(
            "css-reset-vs-normalize",
            "Compare CSS reset vs normalize.",
            "**Reset** zeroes all defaults (Eric Meyer). **Normalize** preserves useful defaults while fixing cross-browser bugs.",
            """*, *::before, *::after { box-sizing: border-box; }
* { margin: 0; }
body { line-height: 1.5; -webkit-font-smoothing: antialiased; }""",
            "css",
            key_points=["Reset = blank slate; Normalize = consistent baseline", "Most projects use a small custom reset", "Tailwind Preflight is a modern reset"],
        ),
        InterviewItem(
            "viewport-meta-tag",
            "Why is the viewport meta tag important?",
            "Tells mobile browsers to use device width and initial scale — without it, pages render at desktop width zoomed out.",
            """<meta charset=\"UTF-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">""",
            "html",
            key_points=["Required for responsive mobile layouts", "Avoid user-scalable=no (accessibility)", "initial-scale=1 prevents zoom-on-load issues"],
        ),
        InterviewItem(
            "html5-semantic-deep-dive",
            "Deep dive: HTML5 semantic elements.",
            "Semantic tags convey meaning: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`, `<figure>`.",
            """<main id=\"content\">
  <article>
    <header><h1>Order #1042</h1></header>
    <section aria-labelledby=\"items-heading\">
      <h2 id=\"items-heading\">Line Items</h2>
    </section>
  </article>
  <aside aria-label=\"Related orders\">...</aside>
</main>""",
            "html",
            key_points=["One <main> per page", "Section needs heading for outline", "Better SEO and screen reader navigation"],
        ),
        InterviewItem(
            "aria-attributes",
            "What are ARIA attributes and when should you use them?",
            "ARIA adds accessibility when native HTML is insufficient. First rule: **use native semantics before ARIA**.",
            """<button aria-expanded=\"false\" aria-controls=\"menu\">Menu</button>
<div aria-live=\"polite\">{{ statusMessage }}</div>
<input aria-describedby=\"email-hint\" required>
<span id=\"email-hint\">We'll never share your email.</span>""",
            "html",
            key_points=["Don't change semantics with wrong roles", "aria-hidden hides decorative elements", "Test with screen readers (NVDA, VoiceOver)"],
        ),
        InterviewItem(
            "html-forms-validation",
            "How do HTML forms and validation work?",
            "Native validation via attributes; `novalidate` defers to JS. Accessible labels and error messages are required.",
            """<label for=\"qty\">Quantity</label>
<input id=\"qty\" type=\"number\" min=\"1\" max=\"99\" required
       aria-invalid=\"true\" aria-describedby=\"qty-error\">
<span id=\"qty-error\" role=\"alert\">Enter 1–99</span>""",
            "html",
            key_points=["Always pair inputs with <label>", "Use role=\"alert\" for error messages", "HTML5 types: email, url, number, date"],
        ),
    ],
    ("htmlcss", "intermediate"): [
        InterviewItem(
            "flexbox-advanced",
            "Advanced Flexbox: align, grow, shrink, and wrap.",
            "Control alignment with `justify-content`/`align-items`, sizing with `flex-grow/shrink/basis`, and wrapping with `flex-wrap`.",
            """.toolbar {
  display: flex; justify-content: space-between; align-items: center;
  gap: 1rem; flex-wrap: wrap;
}
.toolbar__search { flex: 1 1 200px; }
.toolbar__actions { flex: 0 0 auto; }""",
            "css",
            key_points=["flex: 1 = flex: 1 1 0%", "align-self overrides per item", "gap replaces margin hacks"],
        ),
        InterviewItem(
            "css-grid-advanced",
            "Advanced CSS Grid: template areas and auto-fit.",
            "Named grid areas for layouts; `repeat(auto-fit, minmax())` for responsive columns without media queries.",
            """.dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}
.page-layout {
  grid-template-areas: \"header header\" \"sidebar main\" \"footer footer\";
}""",
            "css",
            key_points=["grid-template-areas for readable layouts", "auto-fit collapses empty tracks", "subgrid (modern) aligns nested grids"],
        ),
        InterviewItem(
            "media-queries",
            "How do CSS media queries work?",
            "Apply styles based on viewport width, height, orientation, or prefers-* user preferences.",
            """@media (min-width: 768px) { .layout { grid-template-columns: 240px 1fr; } }
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; }
}""",
            "css",
            key_points=["Mobile-first: min-width queries", "Test prefers-reduced-motion and color-scheme", "Container queries (@container) for component-level responsiveness"],
        ),
        InterviewItem(
            "mobile-first-design",
            "What is mobile-first design?",
            "Start with base styles for small screens, then enhance with min-width media queries for larger viewports.",
            """.nav { flex-direction: column; }
@media (min-width: 768px) { .nav { flex-direction: row; } }
@media (min-width: 1024px) { .grid { grid-template-columns: repeat(3, 1fr); } }""",
            "css",
            key_points=["Forces focus on essential content", "Progressive enhancement over graceful degradation", "Touch targets ≥ 44×44px"],
        ),
        InterviewItem(
            "pseudo-classes-elements",
            "Explain CSS pseudo-classes and pseudo-elements.",
            "Pseudo-classes (`:hover`, `:focus-visible`, `:nth-child`) select state. Pseudo-elements (`::before`, `::after`) style generated content.",
            """a:focus-visible { outline: 2px solid var(--color-primary); }
tr:nth-child(even) { background: #f8f9fa; }
.tooltip::after { content: attr(data-tip); opacity: 0; }
.tooltip:hover::after { opacity: 1; }""",
            "css",
            key_points=[":focus-visible for keyboard-only focus rings", "::before/::after need content property", ":not() excludes elements from rules"],
        ),
        InterviewItem(
            "css-animations-transitions",
            "CSS transitions vs animations — when to use each?",
            "**Transitions** animate between two states on property change. **Animations** define multi-step keyframe sequences.",
            """.btn { transition: background-color 0.2s ease; }
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
.modal { animation: fadeInUp 0.3s ease-out; }""",
            "css",
            key_points=["Transition needs trigger (hover, class toggle)", "Animation runs automatically via keyframes", "Respect prefers-reduced-motion"],
        ),
        InterviewItem(
            "bem-methodology",
            "What is BEM CSS methodology?",
            "**Block__Element--Modifier** — predictable, flat selectors that avoid specificity wars.",
            """.card { padding: 1rem; }
.card__title { font-size: 1.25rem; }
.card--highlighted { border: 2px solid var(--color-primary); }""",
            "css",
            key_points=["No nesting like .card .title", "Modifier classes combine with block", "Works well with component frameworks"],
        ),
        InterviewItem(
            "bootstrap-vs-tailwind",
            "Compare Bootstrap vs Tailwind CSS.",
            "Bootstrap provides pre-built components and grid. Tailwind is utility-first — compose designs with atomic classes.",
            """<!-- Bootstrap -->
<button class=\"btn btn-primary\">Submit</button>
<!-- Tailwind -->
<button class=\"bg-indigo-600 text-white px-4 py-2 rounded-lg\">Submit</button>""",
            "html",
            key_points=["Bootstrap = faster prototyping with defaults", "Tailwind = more design control, smaller custom CSS", "Both support dark mode and responsive utilities"],
        ),
        InterviewItem(
            "responsive-images",
            "How do you implement responsive images in HTML?",
            "Use `srcset`/`sizes` for resolution switching and `<picture>` for art direction.",
            """<img src=\"hero-800.jpg\"
  srcset=\"hero-400.jpg 400w, hero-800.jpg 800w, hero-1200.jpg 1200w\"
  sizes=\"(max-width: 600px) 100vw, 50vw\"
  alt=\"Dashboard\" loading=\"lazy\" width=\"800\" height=\"450\">""",
            "html",
            key_points=["Always set width/height to prevent layout shift", "loading=\"lazy\" for below-fold images", "WebP/AVIF in srcset for smaller files"],
        ),
    ],
    ("htmlcss", "advanced"): [
        InterviewItem(
            "wcag-accessibility",
            "What is WCAG 2.1 and how do you meet it?",
            "Web Content Accessibility Guidelines — levels A, AA, AAA. AA is the industry standard for contrast, keyboard access, and labels.",
            """<img src=\"chart.png\" alt=\"Q2 revenue up 12% to $4.2M\">
<a href=\"#main\" class=\"skip-link\">Skip to content</a>
:focus-visible { outline: 2px solid #005fcc; outline-offset: 2px; }""",
            "html",
            key_points=["AA contrast: 4.5:1 normal text, 3:1 large text", "All functionality available via keyboard", "Use axe DevTools or Lighthouse for audits"],
        ),
        InterviewItem(
            "dark-mode-implementation",
            "How do you implement dark mode in CSS?",
            "Use `prefers-color-scheme`, CSS variables, and optional manual toggle with `data-theme` attribute.",
            """:root { --bg: #fff; --text: #1a1a1a; }
@media (prefers-color-scheme: dark) {
  :root { --bg: #121212; --text: #e0e0e0; }
}
body { background: var(--bg); color: var(--text); }""",
            "css",
            key_points=["CSS variables make theming trivial", "Respect system preference by default", "Persist user choice in localStorage"],
        ),
        InterviewItem(
            "css-preprocessors-sass",
            "What are CSS preprocessors like SASS?",
            "SASS adds variables, nesting, mixins, and functions — compiled to CSS. Modern CSS variables reduce the need.",
            """$primary: #512BD4;
@mixin flex-center { display: flex; justify-content: center; align-items: center; }
.card { border-color: $primary; @include flex-center; }""",
            "scss",
            key_points=["SASS compiles to CSS at build time", "Mixins reuse declaration blocks", "Native CSS now has variables, nesting, and @layer"],
        ),
        InterviewItem(
            "critical-css-performance",
            "What is critical CSS and how does it improve performance?",
            "Inline above-the-fold CSS in `<head>`; defer full stylesheet. Reduces render-blocking and improves LCP.",
            """<style>/* Critical shell styles */</style>
<link rel=\"preload\" href=\"styles.css\" as=\"style\"
      onload=\"this.onload=null;this.rel='stylesheet'\">""",
            "html",
            key_points=["Extract critical CSS per route/template", "Preload fonts and hero images", "Target LCP element for fastest paint"],
        ),
        InterviewItem(
            "z-index-stacking-context",
            "Explain z-index and stacking contexts.",
            "z-index only compares elements in the same stacking context. New contexts created by `position`+z-index, opacity<1, transform, filter.",
            """.modal-backdrop { z-index: 100; }
.modal { z-index: 101; }
.header { position: relative; z-index: 1; } /* traps child z-index */""",
            "css",
            key_points=["Don't use z-index: 9999 everywhere", "Portal/modal to document body escapes context", "isolation: isolate creates intentional context"],
        ),
        InterviewItem(
            "css-containment",
            "What is CSS containment?",
            "Tells browser an element's layout/paint/style is isolated — improves rendering performance for large lists and widgets.",
            """.order-row { contain: layout style paint; }
.virtual-list-item {
  content-visibility: auto;
  contain-intrinsic-size: 0 48px;
}""",
            "css",
            key_points=["contain: strict = layout + style + paint", "content-visibility: auto for long lists", "Useful in data tables and infinite scroll"],
        ),
        InterviewItem(
            "print-stylesheets",
            "How do you create print stylesheets?",
            "Use `@media print` to hide navigation, expand links, and optimize page breaks for invoices and reports.",
            """@media print {
  .sidebar, .nav { display: none !important; }
  .order-table { page-break-inside: avoid; }
  @page { margin: 2cm; size: A4; }
}""",
            "css",
            key_points=["Hide interactive UI in print", "page-break-inside: avoid for tables", "Test with browser Print Preview"],
        ),
        InterviewItem(
            "css-layer",
            "What are CSS @layer and cascade layers?",
            "Layers control cascade order independent of specificity — declare layer order once, assign rules to layers.",
            """@layer reset, base, components, utilities;
@layer reset { * { box-sizing: border-box; margin: 0; } }
@layer utilities { .text-center { text-align: center; } }""",
            "css",
            key_points=["Solves specificity wars in large codebases", "Framework CSS can live in lower layers", "Tailwind v4 uses layers internally"],
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "k8s-pods-services-deployments": {
        "explanation": (
            "**Kubernetes** organizes containerized workloads into three core abstractions. A **Pod** is the smallest "
            "schedulable unit — one or more containers that share network namespace and storage volumes. Pods are "
            "ephemeral; never create them directly in production. A **Deployment** declares desired replica count and "
            "Pod template, handling rolling updates, rollbacks, and self-healing when nodes fail. A **Service** provides "
            "a stable virtual IP and DNS name (`order-api-svc.default.svc.cluster.local`) that load-balances traffic "
            "across healthy Pod replicas. In interviews, walk through the flow: Deployment creates ReplicaSet → "
            "ReplicaSet creates Pods → Service routes traffic to Pods matching its selector label."
        ),
        "code": """apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-api
  labels: { app: order-api }
spec:
  replicas: 3
  selector:
    matchLabels: { app: order-api }
  template:
    metadata:
      labels: { app: order-api }
    spec:
      containers:
      - name: api
        image: myacr.azurecr.io/order-api:1.2.0
        ports: [{ containerPort: 8080 }]
        resources:
          requests: { cpu: \"100m\", memory: \"128Mi\" }
          limits:   { cpu: \"500m\", memory: \"512Mi\" }
---
apiVersion: v1
kind: Service
metadata:
  name: order-api-svc
spec:
  selector: { app: order-api }
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP

# kubectl rollout status deployment/order-api
# kubectl rollout undo deployment/order-api""",
        "language": "yaml",
        "key_points": [
            "Pod = ephemeral; Deployments manage Pod lifecycle",
            "Service provides stable DNS and load balancing",
            "Labels/selectors connect Deployments, Services, and Ingress",
            "Use resource requests/limits to prevent noisy-neighbor issues",
            "kubectl rollout undo for instant rollback",
        ],
    },
    "docker-multistage-builds": {
        "explanation": (
            "**Multi-stage Docker builds** use multiple `FROM` instructions in one Dockerfile. Each stage starts fresh "
            "from a base image, and you selectively copy artifacts between stages with `COPY --from=stage`. The final "
            "runtime stage contains only the compiled application — no SDK, source code, or build tools. This dramatically "
            "reduces image size (often 80%+ smaller), shrinks the attack surface, and speeds up image pulls in CI/CD. "
            "Order Dockerfile instructions from least to most frequently changed: copy `.csproj` and restore before "
            "copying full source to maximize **layer cache** hits. Always run the runtime stage as a **non-root user**."
        ),
        "code": """FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY OrderApi/OrderApi.csproj OrderApi/
RUN dotnet restore OrderApi/OrderApi.csproj
COPY OrderApi/ OrderApi/
RUN dotnet publish OrderApi/OrderApi.csproj -c Release -o /app/publish --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app
RUN adduser --disabled-password --gecos '' appuser
USER appuser
COPY --from=build /app/publish .
ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080
ENTRYPOINT [\"dotnet\", \"OrderApi.dll\"]""",
        "language": "dockerfile",
        "key_points": [
            "Final image contains only runtime + published output",
            "Copy csproj first for Docker layer caching",
            "Run as non-root user in production",
            "Use .dockerignore to exclude bin/obj/.git",
            "Tag with semantic version and git SHA",
        ],
    },
    "docker-networking": {
        "explanation": (
            "Docker provides several **network drivers**. The default **bridge** network isolates containers on a host "
            "while allowing them to communicate. **Docker Compose** automatically creates a project-scoped bridge network "
            "where each service is reachable by its **service name** as hostname — e.g., `Server=db` in a connection "
            "string resolves to the `db` container. **Host** networking removes isolation (container uses host's network "
            "stack). **Overlay** networks span multiple Docker hosts for Swarm or are replaced by CNI plugins in "
            "Kubernetes. Understanding networking is critical for debugging connectivity issues between API, database, "
            "and cache containers in local dev environments."
        ),
        "code": """# docker-compose.yml
services:
  api:
    build: .
    ports: [\"5000:8080\"]
    networks: [app-net]
    environment:
      ConnectionStrings__Sql: \"Server=db;Database=Orders;...\"
  db:
    image: postgres:16
    networks: [app-net]
  redis:
    image: redis:7-alpine
    networks: [app-net]

networks:
  app-net:
    driver: bridge

# Debug: docker network inspect netangularazureinterviewprep_app-net
# Custom network: docker network create --driver bridge my-net""",
        "language": "yaml",
        "key_points": [
            "Compose service name = DNS hostname on shared network",
            "Published ports (5000:8080) expose to host",
            "Bridge is default for single-host container communication",
            "Use docker network inspect for troubleshooting",
            "K8s uses CNI (Azure CNI, Calico) instead of Docker networks",
        ],
    },
    "docker-volumes": {
        "explanation": (
            "Container filesystems are **ephemeral** — data is lost when the container is removed. **Docker volumes** "
            "persist data in a location managed by Docker, independent of container lifecycle. **Named volumes** "
            "(declared under top-level `volumes:` in Compose) are ideal for database data. **Bind mounts** map a "
            "host directory into the container — useful for dev hot-reload but tie data to a specific machine. "
            "**tmpfs mounts** store data in memory for temporary files. In production on AKS, use **PersistentVolumeClaims** "
            "instead of Docker volumes. Never store stateful data in the container's writable layer."
        ),
        "code": """services:
  db:
    image: mcr.microsoft.com/mssql/server:2022-latest
    environment:
      ACCEPT_EULA: \"Y\"
      SA_PASSWORD: \"${DB_PASSWORD}\"
    volumes:
      - sqldata:/var/opt/mssql        # named volume — persists across restarts
  api:
    build: .
    volumes:
      - ./appsettings.Development.json:/app/appsettings.Development.json:ro

volumes:
  sqldata:
    driver: local

# docker volume ls
# docker volume inspect sqldata
# Backup: docker run --rm -v sqldata:/data -v $(pwd):/backup alpine tar czf /backup/db-backup.tar.gz /data""",
        "language": "yaml",
        "key_points": [
            "Named volumes survive container removal",
            "Bind mounts for dev config hot-reload only",
            "Never store DB data in container writable layer",
            "AKS uses PersistentVolumeClaims for stateful workloads",
            "Back up volumes before major upgrades",
        ],
    },
    "k8s-secrets-configmaps": {
        "explanation": (
            "Kubernetes separates **configuration** from **secrets**. A **ConfigMap** stores non-sensitive key-value "
            "data like log levels, feature flags, and environment names. A **Secret** stores sensitive data such as "
            "connection strings and API keys — encoded in base64 but **not encrypted at rest** by default. Mount them "
            "as environment variables or files in Pod specs. In production Azure environments, prefer **Azure Key Vault "
            "Provider for Secrets Store CSI Driver** to inject secrets without storing them in etcd. Never commit Secret "
            "manifests to Git — use sealed-secrets, external-secrets operator, or pipeline-injected values."
        ),
        "code": """apiVersion: v1
kind: ConfigMap
metadata:
  name: order-api-config
data:
  ASPNETCORE_ENVIRONMENT: Production
  LogLevel__Default: Warning
---
apiVersion: v1
kind: Secret
metadata:
  name: order-api-secrets
type: Opaque
stringData:
  ConnectionStrings__Sql: \"Server=tcp:sql.database.windows.net;...\"
---
# Deployment snippet
spec:
  containers:
  - name: api
    envFrom:
    - configMapRef: { name: order-api-config }
    env:
    - name: ConnectionStrings__Sql
      valueFrom:
        secretKeyRef: { name: order-api-secrets, key: ConnectionStrings__Sql }""",
        "language": "yaml",
        "key_points": [
            "ConfigMap for non-sensitive; Secret for credentials",
            "Base64 in Secrets is NOT encryption — use Key Vault CSI",
            "Never commit Secrets to version control",
            "Mount as env vars or files depending on app needs",
            "Rotate secrets without redeploying via CSI auto-rotation",
        ],
    },
    "azure-container-registry": {
        "explanation": (
            "**Azure Container Registry (ACR)** is a managed, private Docker/OCI registry hosted in Azure. It stores "
            "container images close to your compute (AKS, App Service) for fast pulls. ACR integrates with Azure DevOps "
            "and GitHub Actions via service connections. **SKU tiers** range from Basic (dev) to Premium (geo-replication, "
            "content trust). Enable **Microsoft Defender for Cloud** to scan images for CVEs on push. Attach ACR to AKS "
            "with managed identity so nodes pull images without storing admin credentials. Use **ACR Tasks** for "
            "cloud-native image builds triggered by Git commits."
        ),
        "code": """# Create and push
az acr create -g rg-order -n myregistry --sku Standard
az acr login --name myregistry
docker build -t myregistry.azurecr.io/order-api:1.2.0 .
docker push myregistry.azurecr.io/order-api:1.2.0

# Attach to AKS (managed identity pull)
az aks update -g rg-order -n myaks --attach-acr myregistry

# ACR Task — build in cloud on git push
az acr task create -n build-order-api -r myregistry \\
  --context https://github.com/org/order-api.git \\
  --file Dockerfile --git-access-token $GIT_TOKEN""",
        "language": "bash",
        "key_points": [
            "Private registry — no Docker Hub rate limits",
            "Attach ACR to AKS for passwordless image pull",
            "Enable vulnerability scanning with Defender",
            "Tag images with semver and git SHA",
            "Premium SKU for geo-replication in multi-region",
        ],
    },
    "semantic-versioning": {
        "explanation": (
            "**Semantic Versioning (SemVer)** uses **MAJOR.MINOR.PATCH** to communicate the nature of changes. Increment "
            "**MAJOR** for breaking API changes, **MINOR** for backward-compatible features, and **PATCH** for "
            "bug fixes. Pre-release versions use suffixes like `1.0.0-beta.1`. Consistent versioning across Git tags, "
            "NuGet packages, Docker images, and Helm chart appVersion enables traceability from production back to "
            "source code. In CI/CD, auto-generate versions from Git tags or use tools like **GitVersion** or "
            "**MinVer** for .NET projects. Interviewers expect you to explain how versioning drives deployment strategy."
        ),
        "code": """# Git tagging workflow
git tag -a v1.2.0 -m \"Release 1.2.0 — order search feature\"
git push origin v1.2.0

# Align Docker and NuGet
docker tag order-api myacr.azurecr.io/order-api:1.2.0
docker push myacr.azurecr.io/order-api:1.2.0
dotnet pack -c Release -p:PackageVersion=1.2.0

# MinVer in .NET — auto version from git height
# <PackageReference Include=\"MinVer\" PrivateAssets=\"all\" />""",
        "language": "bash",
        "key_points": [
            "MAJOR = breaking changes",
            "MINOR = new features, backward compatible",
            "PATCH = bug fixes only",
            "Align Git tags, NuGet, Docker, and Helm versions",
            "Pre-release: 1.0.0-rc.1 for release candidates",
        ],
    },
    "nuget-package-management": {
        "explanation": (
            "**.NET dependency management** centers on NuGet packages declared in `.csproj` files. **Central Package "
            "Management** (CPM) defines all package versions in a single `Directory.Packages.props` file, preventing "
            "version drift across projects in a solution. Use **`nuget.config`** to configure feed sources including "
            "nuget.org and private feeds like **Azure Artifacts**. Run `dotnet list package --vulnerable` and "
            "`dotnet list package --outdated` in CI to catch security and staleness issues. Lock files (`packages.lock.json`) "
            "ensure reproducible restores. For interviews, mention transitive dependency resolution and how "
            "Dependabot/Renovate automate updates."
        ),
        "code": """<!-- Directory.Packages.props -->
<Project>
  <PropertyGroup>
    <ManagePackageVersionsCentrally>true</ManagePackageVersionsCentrally>
  </PropertyGroup>
  <ItemGroup>
    <PackageVersion Include=\"Microsoft.EntityFrameworkCore\" Version=\"8.0.11\" />
    <PackageVersion Include=\"Serilog.AspNetCore\" Version=\"8.0.3\" />
  </ItemGroup>
</Project>

<!-- OrderApi.csproj -->
<ItemGroup>
  <PackageReference Include=\"Microsoft.EntityFrameworkCore\" />
</ItemGroup>

# Audit in CI
dotnet list OrderApi.sln package --vulnerable --include-transitive""",
        "language": "xml",
        "key_points": [
            "Central Package Management prevents version drift",
            "nuget.config for private Azure Artifacts feeds",
            "Audit transitive dependencies in CI",
            "Lock files for reproducible builds",
            "Pin major versions; automate patch updates",
        ],
    },
    "k8s-helm-charts": {
        "explanation": (
            "**Helm** is the package manager for Kubernetes. A **chart** is a collection of templated YAML manifests "
            "packaged with a `Chart.yaml` (metadata), `values.yaml` (defaults), and `templates/` directory. Helm "
            "renders templates with values and installs them as a **release**. This enables environment-specific "
            "deployments (dev/staging/prod) from the same chart by swapping values files. Helm supports **rollback** "
            "to previous revisions, **hooks** for pre/post install jobs, and chart repositories for sharing. In "
            "enterprise .NET shops, Helm charts often wrap Deployments, Services, Ingress, ConfigMaps, and HPA together."
        ),
        "code": """# charts/order-api/values.yaml
replicaCount: 3
image:
  repository: myacr.azurecr.io/order-api
  tag: \"1.2.0\"
ingress:
  enabled: true
  host: api.example.com

# charts/order-api/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
      - name: api
        image: \"{{ .Values.image.repository }}:{{ .Values.image.tag }}\"

# Commands
helm upgrade --install order-api ./charts/order-api -f values-prod.yaml
helm history order-api
helm rollback order-api 2""",
        "language": "yaml",
        "key_points": [
            "Chart = templated K8s manifests + values",
            "One chart, multiple values files per environment",
            "helm rollback for fast recovery",
            "Use helm lint and helm template for validation",
            "OCI registries can store Helm charts",
        ],
    },
    "k8s-ingress-controllers": {
        "explanation": (
            "A Kubernetes **Ingress** resource defines HTTP/S routing rules from outside the cluster to internal "
            "Services. Ingress alone does nothing — an **Ingress Controller** (NGINX, Traefik, Azure Application Gateway) "
            "watches Ingress resources and configures the actual load balancer. Ingress handles **path-based routing**, "
            "**host-based routing**, and **TLS termination** via referenced Secrets or cert-manager. On AKS, common "
            "choices are the **NGINX Ingress Controller** add-on or **Application Gateway Ingress Controller (AGIC)** "
            "for WAF integration. Compare Ingress (L7 HTTP) with LoadBalancer Service type (L4 TCP) for interview depth."
        ),
        "code": """apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: order-api-ingress
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/rate-limit: \"100\"
spec:
  ingressClassName: nginx
  tls:
  - hosts: [api.example.com]
    secretName: api-tls-cert
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: order-api-svc
            port: { number: 80 }
      - path: /health
        pathType: Exact
        backend:
          service:
            name: order-api-svc
            port: { number: 80 }""",
        "language": "yaml",
        "key_points": [
            "Ingress = routing rules; Controller implements them",
            "TLS termination at ingress reduces in-cluster overhead",
            "AKS: NGINX add-on or Application Gateway (WAF)",
            "cert-manager automates Let's Encrypt certificates",
            "pathType: Prefix vs Exact vs ImplementationSpecific",
        ],
    },
    "k8s-liveness-readiness-probes": {
        "explanation": (
            "Kubernetes **health probes** determine container lifecycle and traffic routing. A **liveness probe** "
            "checks if the container is alive — failure causes a restart. A **readiness probe** checks if the container "
            "can accept traffic — failure removes the Pod from Service endpoints without restarting it. This prevents "
            "users from hitting apps still starting up or temporarily unable to serve (e.g., during DB migration). "
            "Implement separate `/health/live` and `/health/ready` endpoints in ASP.NET Core. Configure "
            "`initialDelaySeconds`, `periodSeconds`, and `failureThreshold` appropriately to avoid restart loops."
        ),
        "code": """// Program.cs — ASP.NET Core health checks
builder.Services.AddHealthChecks()
    .AddSqlServer(builder.Configuration.GetConnectionString(\"Sql\"), name: \"sql\")
    .AddRedis(builder.Configuration[\"Redis:Connection\"], name: \"redis\");

app.MapHealthChecks(\"/health/live\", new HealthCheckOptions
{
    Predicate = _ => false  // always healthy if process runs
});
app.MapHealthChecks(\"/health/ready\", new HealthCheckOptions
{
    Predicate = check => check.Tags.Contains(\"ready\")
});

# Deployment probes
livenessProbe:
  httpGet: { path: /health/live, port: 8080 }
  initialDelaySeconds: 15
  periodSeconds: 10
readinessProbe:
  httpGet: { path: /health/ready, port: 8080 }
  initialDelaySeconds: 5
  periodSeconds: 5""",
        "language": "csharp",
        "key_points": [
            "Liveness = restart on failure",
            "Readiness = remove from load balancer on failure",
            "Separate endpoints for live vs ready",
            "Tune initialDelaySeconds to avoid restart loops",
            "Startup probe for slow-starting .NET apps",
        ],
    },
    "github-actions-cicd": {
        "explanation": (
            "**GitHub Actions** provides CI/CD via YAML workflow files in `.github/workflows/`. Workflows trigger on "
            "events (push, pull_request, schedule) and run **jobs** on **runners** (GitHub-hosted or self-hosted). "
            "Each job contains **steps** using built-in actions or shell commands. Store secrets in repository or "
            "organization settings — never in YAML. Reusable workflows and composite actions reduce duplication. "
            "For .NET projects, the typical pipeline restores, builds, tests, publishes artifacts, builds Docker images, "
            "pushes to ACR, and deploys to AKS or App Service. Matrix strategies test across OS and .NET versions."
        ),
        "code": """name: CI/CD Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with: { dotnet-version: '8.0.x' }
      - run: dotnet restore && dotnet build --no-restore
      - run: dotnet test --no-build --verbosity normal
      - run: docker build -t myacr.azurecr.io/order-api:${{ github.sha }} .
      - uses: azure/docker-login@v2
        with:
          login-server: myacr.azurecr.io
          username: ${{ secrets.ACR_USERNAME }}
          password: ${{ secrets.ACR_PASSWORD }}
      - run: docker push myacr.azurecr.io/order-api:${{ github.sha }}
      - uses: azure/k8s-set-context@v4
        with:
          kubeconfig: ${{ secrets.KUBE_CONFIG }}
      - run: kubectl set image deployment/order-api api=myacr.azurecr.io/order-api:${{ github.sha }}""",
        "language": "yaml",
        "key_points": [
            "Workflows live in .github/workflows/",
            "Secrets via ${{ secrets.NAME }} — never hardcode",
            "Matrix builds for multi-version testing",
            "Reusable workflows for shared pipeline logic",
            "Environment protection rules for prod deploys",
        ],
    },
    "azure-pipelines-yaml": {
        "explanation": (
            "**Azure Pipelines** is Azure DevOps' CI/CD service using YAML pipelines checked into the repo. Pipelines "
            "have **triggers** (CI), **stages** (logical groupings), **jobs** (run on agents), and **steps** (tasks or "
            "scripts). **Variable groups** and **Key Vault** integration inject secrets. **Environments** add approval "
            "gates and deployment history for production. **Templates** promote reuse across microservices. The "
            "Docker@2 task builds and pushes to ACR; KubernetesManifest@1 deploys to AKS. Compare with GitHub Actions "
            "— Azure Pipelines integrates deeply with Azure DevOps boards, repos, and Artifacts."
        ),
        "code": """trigger:
  branches: { include: [main] }

variables:
  - group: order-api-secrets
  - name: imageTag
    value: $(Build.BuildId)

stages:
- stage: Build
  jobs:
  - job: BuildTest
    pool: { vmImage: 'ubuntu-latest' }
    steps:
    - task: UseDotNet@2
      inputs: { version: '8.x' }
    - script: dotnet test --configuration Release
    - task: Docker@2
      displayName: Build and push
      inputs:
        containerRegistry: 'acr-service-connection'
        repository: 'order-api'
        command: 'buildAndPush'
        Dockerfile: 'OrderApi/Dockerfile'
        tags: $(imageTag)

- stage: Deploy
  dependsOn: Build
  condition: succeeded()
  jobs:
  - deployment: DeployProd
    environment: production
    strategy:
      runOnce:
        deploy:
          steps:
          - task: KubernetesManifest@1
            inputs:
              action: 'deploy'
              namespace: 'production'
              manifests: 'k8s/deployment.yaml'
              containers: 'order-api=myacr.azurecr.io/order-api:$(imageTag)'""",
        "language": "yaml",
        "key_points": [
            "Stages separate build from deploy with dependencies",
            "Environments add manual approval gates",
            "Variable groups centralize secrets",
            "Templates reuse pipeline logic across repos",
            "Deployment jobs track history per environment",
        ],
    },
    "container-security-scanning": {
        "explanation": (
            "**Container security scanning** identifies CVEs in base images and installed packages before deployment. "
            "Scan in CI on every build — tools include **Trivy**, **Snyk**, **Grype**, and **Microsoft Defender for "
            "Cloud** (ACR integration). Fail the pipeline on CRITICAL/HIGH severity findings. Best practices: use "
            "**minimal base images** (distroless, alpine, aspnet runtime only), pin base images by **digest** not "
            "tag, run as **non-root**, and keep images updated. Scan both the Dockerfile build context and the final "
            "pushed image. In regulated industries, maintain an SBOM (Software Bill of Materials) for audit trails."
        ),
        "code": """# GitHub Actions — Trivy scan before push
- name: Build image
  run: docker build -t order-api:${{ github.sha }} .

- name: Scan with Trivy
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: order-api:${{ github.sha }}
    format: 'sarif'
    severity: 'CRITICAL,HIGH'
    exit-code: '1'

# Pin base image by digest for reproducibility
FROM mcr.microsoft.com/dotnet/aspnet:8.0@sha256:abc123...

# ACR — enable Defender for Cloud image scanning
az security pricing create -n ContainerRegistry --tier Standard""",
        "language": "yaml",
        "key_points": [
            "Scan every image in CI before deploy",
            "Fail on CRITICAL/HIGH CVEs",
            "Use minimal non-root runtime images",
            "Pin base images by digest",
            "Generate SBOM for compliance audits",
        ],
    },
    "gitflow-vs-trunk": {
        "explanation": (
            "**GitFlow** uses long-lived branches: `main` (production), `develop` (integration), `feature/*`, "
            "`release/*`, and `hotfix/*`. It suits scheduled release trains and teams needing strict production "
            "stabilization. **Trunk-based development** commits to a single `main` branch with short-lived feature "
            "branches (hours to days). It pairs with **feature flags** and continuous delivery. Most modern DevOps "
            "teams prefer trunk-based for faster feedback and simpler CI/CD. GitFlow adds overhead with merge "
            "conflicts across long-lived branches. Interview answer: choose based on release cadence — daily deploys "
            "favor trunk; quarterly releases may tolerate GitFlow."
        ),
        "code": """# Trunk-based (recommended for CI/CD)
git checkout -b feat/order-search
# commit, push, open PR, merge within 1-2 days
git push origin feat/order-search
# main is always deployable

# GitFlow
git checkout develop
git checkout -b feature/order-search develop
# ... work, merge back to develop
git checkout -b release/1.2 develop
# stabilize, merge to main AND develop
git checkout -b hotfix/1.1.1 main
# fix, merge to main AND develop""",
        "language": "bash",
        "key_points": [
            "Trunk-based = short branches + feature flags",
            "GitFlow = long-lived develop + release branches",
            "Trunk-based enables continuous delivery",
            "Keep branches alive < 2 days regardless of model",
            "main/master should always be deployable",
        ],
    },
    "sonarqube-code-quality": {
        "explanation": (
            "**SonarQube** is a platform for continuous **code quality and security** inspection. It analyzes source "
            "code for bugs, code smells, duplications, test coverage, and security hotspots. **Quality gates** define "
            "pass/fail criteria (e.g., coverage > 80%, zero blocker issues) and can block PR merges. SonarQube integrates "
            "with Azure DevOps, GitHub Actions, and GitLab CI. It complements but differs from **SAST** tools — "
            "SonarQube focuses on maintainability and broad quality metrics while dedicated SAST tools dig deeper "
            "into security vulnerabilities. Use SonarQube for technical debt tracking over time and PR decoration "
            "with inline comments."
        ),
        "code": """# Azure Pipeline — SonarQube for .NET
- task: SonarQubePrepare@6
  inputs:
    SonarQube: 'SonarQubeConnection'
    scannerMode: 'dotnet'
    projectKey: 'OrderApi'
    extraProperties: |
      sonar.cs.opencover.reportsPaths=$(Agent.TempDirectory)/coverage.opencover.xml
- script: dotnet build --no-incremental
- script: dotnet test --collect:\"XPlat Code Coverage\"
- task: SonarQubeAnalyze@6
- task: SonarQubePublish@6
  inputs:
    pollingTimeoutSec: '300'

# Quality gate conditions (configured in SonarQube UI):
# - Coverage on new code > 80%
# - 0 blocker/critical issues on new code
# - Duplicated lines < 3%""",
        "language": "yaml",
        "key_points": [
            "Quality gates block merges on failing metrics",
            "Tracks technical debt and code smells over time",
            "PR decoration shows inline issue comments",
            "Integrate coverage reports for .NET",
            "Complements SAST — broader quality focus",
        ],
    },
    "prometheus-grafana-monitoring": {
        "explanation": (
            "**Prometheus** is an open-source monitoring system that **scrapes metrics** from HTTP `/metrics` endpoints "
            "at configured intervals. It stores time-series data and supports PromQL queries for alerting. **Grafana** "
            "visualizes Prometheus data in dashboards with panels for request rates, error rates, and latency percentiles. "
            "In ASP.NET Core, use **prometheus-net** or **OpenTelemetry** exporters to expose metrics. Define **SLIs** "
            "(Service Level Indicators) like availability, latency p95, and error rate. Set **alerts** in Grafana or "
            "Alertmanager for on-call response. Azure Monitor and Application Insights provide managed alternatives "
            "with similar concepts."
        ),
        "code": """// Program.cs — expose Prometheus metrics
builder.Services.AddOpenTelemetry()
    .WithMetrics(m => m
        .AddAspNetCoreInstrumentation()
        .AddRuntimeInstrumentation()
        .AddPrometheusExporter());

app.MapPrometheusScrapingEndpoint();  // /metrics

# prometheus.yml
scrape_configs:
  - job_name: 'order-api'
    scrape_interval: 15s
    static_configs:
      - targets: ['order-api-svc:8080']

# PromQL alert example
# rate(http_server_request_duration_seconds_count{status=~\"5..\"}[5m]) > 0.05""",
        "language": "csharp",
        "key_points": [
            "Pull-based metrics scraping model",
            "Use histograms for latency percentiles (p95, p99)",
            "SLIs: availability, latency, error rate",
            "Grafana dashboards + Alertmanager for on-call",
            "OpenTelemetry is the modern unified standard",
        ],
    },
    "iac-comparison": {
        "explanation": (
            "**Infrastructure as Code (IaC)** declares desired cloud state in version-controlled files. **Terraform** "
            "uses HCL, supports multi-cloud, and tracks state in a state file (use remote backend in Azure Storage). "
            "**Bicep/ARM** are Azure-native — Bicep compiles to ARM JSON with no separate state file (Azure holds state). "
            "**Pulumi** uses real languages (C#, TypeScript, Python) for infrastructure. **Ansible** is procedural "
            "configuration management, not strictly IaC for cloud resources. Choose based on: cloud scope (Azure-only vs "
            "multi-cloud), team language preference, and existing toolchain. In interviews, explain idempotency, "
            "plan/apply workflow, and state management."
        ),
        "code": """# Terraform — multi-cloud capable
terraform {
  backend \"azurerm\" {
    resource_group_name  = \"rg-tfstate\"
    storage_account_name = \"tfstatestore\"
    container_name       = \"tfstate\"
    key                  = \"prod.terraform.tfstate\"
  }
}
resource \"azurerm_kubernetes_cluster\" \"aks\" {
  name                = \"myaks\"
  location            = \"eastus\"
  resource_group_name = azurerm_resource_group.rg.name
  default_node_pool { name = \"default\"; node_count = 2; vm_size = \"Standard_D2s_v3\" }
}

# Bicep — Azure-native, no state file
param location string = resourceGroup().location
resource aks 'Microsoft.ContainerService/managedClusters@2023-07-01' = {
  name: 'myaks'
  location: location
  properties: { agentPoolProfiles: [{ name: 'default', count: 2, vmSize: 'Standard_D2s_v3' }] }
}""",
        "language": "hcl",
        "key_points": [
            "Terraform = multi-cloud HCL + state file",
            "Bicep = Azure-native, no separate state",
            "Always terraform plan / what-if before apply",
            "Remote state with locking prevents conflicts",
            "Modules/templates for reusable infrastructure",
        ],
    },
    "container-orchestration-concepts": {
        "explanation": (
            "**Container orchestration** automates deployment, scaling, networking, and lifecycle management of "
            "containers across a cluster of machines. Core concepts: **scheduling** (placing containers on nodes based "
            "on resources), **desired state reconciliation** (always maintain N replicas), **service discovery** "
            "(DNS-based routing to containers), **self-healing** (restart failed containers), and **rolling updates** "
            "(zero-downtime deployments). **Kubernetes** dominates the market; alternatives include Docker Swarm and "
            "HashiCorp Nomad. Orchestration sits above container runtimes (containerd, CRI-O) and below application "
            "platforms. AKS is Azure's managed Kubernetes service."
        ),
        "code": """# Declarative desired state
kubectl apply -f deployment.yaml   # ensures 3 replicas exist

# Self-healing — delete a pod, Deployment recreates it
kubectl delete pod order-api-abc123

# Scaling
kubectl scale deployment order-api --replicas=5
kubectl autoscale deployment order-api --min=2 --max=10 --cpu-percent=70

# Rolling update
kubectl set image deployment/order-api api=myacr.azurecr.io/order-api:1.3.0
kubectl rollout status deployment/order-api
kubectl rollout undo deployment/order-api""",
        "language": "bash",
        "key_points": [
            "Desired state reconciliation loop",
            "Scheduler assigns Pods to Nodes by resources",
            "Self-healing replaces failed containers",
            "Service discovery via cluster DNS",
            "AKS = managed Kubernetes on Azure",
        ],
    },
    "devsecops": {
        "explanation": (
            "**DevSecOps** integrates security practices into every phase of the DevOps lifecycle — shifting security "
            "left rather than bolting it on before release. Key practices: **secret scanning** in pre-commit hooks "
            "(gitleaks), **dependency auditing** in build (dotnet list package --vulnerable), **SAST** static analysis "
            "(SonarQube), **container image scanning** (Trivy/Defender), **IaC policy checks** (Checkov, OPA), "
            "**RBAC least privilege** in K8s, and **runtime protection** (WAF, network policies). Culture matters: "
            "developers share responsibility for security basics, while security teams provide guardrails and tooling. "
            "Automate compliance checks rather than manual gate reviews."
        ),
        "code": """# DevSecOps pipeline stages
# 1. Pre-commit: gitleaks detect secrets
# 2. Build: dotnet list package --vulnerable
# 3. SAST: SonarQube quality gate
# 4. Container: Trivy scan — fail on CRITICAL
# 5. IaC: checkov -f main.tf
# 6. Deploy: Kyverno policy — no :latest tags
# 7. Runtime: Azure Defender, WAF, network policies

# K8s network policy — restrict ingress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: order-api-policy
spec:
  podSelector: { matchLabels: { app: order-api } }
  policyTypes: [Ingress]
  ingress:
  - from:
    - podSelector: { matchLabels: { app: ingress-nginx } }
    ports: [{ port: 8080 }]""",
        "language": "yaml",
        "key_points": [
            "Shift-left: security in every pipeline stage",
            "Automate scans — don't rely on manual review",
            "Least privilege RBAC in K8s and Azure",
            "Network policies restrict pod-to-pod traffic",
            "Culture: shared security responsibility",
        ],
    },
    "sast-dast": {
        "explanation": (
            "**SAST (Static Application Security Testing)** analyzes source code or bytecode without executing the "
            "application. It finds issues like SQL injection patterns, hardcoded secrets, and insecure crypto early in "
            "development. Tools: SonarQube, Semgrep, Checkmarx. **DAST (Dynamic Application Security Testing)** tests "
            "the running application from outside, simulating attacker behavior. Tools: OWASP ZAP, Burp Suite. SAST "
            "runs in CI on every commit; DAST runs against staging environments. Use both for defense in depth — "
            "SAST catches code-level issues; DAST finds runtime misconfigurations, auth flaws, and missing headers."
        ),
        "code": """# SAST — run in CI on source code
dotnet tool install --global security-scan
security-scan ./OrderApi.sln --fail-on-severity high

# Semgrep custom rules
# semgrep --config=p/csharp ./src/

# DAST — scan staging environment
docker run -t owasp/zap2docker-stable zap-baseline.py \\
  -t https://staging-api.example.com/swagger/index.html \\
  -r zap-report.html

# ASP.NET Core security headers (caught by DAST if missing)
app.Use(async (ctx, next) =>
{
    ctx.Response.Headers[\"X-Content-Type-Options\"] = \"nosniff\";
    ctx.Response.Headers[\"X-Frame-Options\"] = \"DENY\";
    await next();
});""",
        "language": "bash",
        "key_points": [
            "SAST = static code analysis in CI",
            "DAST = dynamic testing against running app",
            "SAST finds issues early; DAST finds runtime flaws",
            "Use both for comprehensive coverage",
            "DAST targets staging, never production",
        ],
    },
    "elk-stack": {
        "explanation": (
            "The **ELK stack** (Elasticsearch, Logstash, Kibana) is a popular open-source logging and analytics "
            "platform. **Elasticsearch** indexes and searches log data. **Logstash** (or **Fluentd**/**Filebeat**) "
            "collects and transforms logs. **Kibana** provides search UI, dashboards, and alerting. In .NET, use "
            "**Serilog** with an Elasticsearch sink to ship structured JSON logs. Log correlation via **trace IDs** "
            "(OpenTelemetry) links logs across microservices. Azure alternatives: **Azure Monitor Logs** (Log Analytics) "
            "with KQL queries. Best practice: structured logging with consistent fields enables powerful filtering."
        ),
        "code": """// Program.cs — Serilog to Elasticsearch
Log.Logger = new LoggerConfiguration()
    .Enrich.FromLogContext()
    .Enrich.WithProperty(\"Application\", \"OrderApi\")
    .WriteTo.Console(new JsonFormatter())
    .WriteTo.Elasticsearch(new ElasticsearchSinkOptions(new Uri(\"http://elastic:9200\"))
    {
        AutoRegisterTemplate = true,
        IndexFormat = \"order-api-{0:yyyy.MM.dd}\"
    })
    .CreateLogger();

// Structured logging with correlation
using (LogContext.PushProperty(\"OrderId\", orderId))
using (LogContext.PushProperty(\"TraceId\", Activity.Current?.TraceId))
{
    Log.Information(\"Processing order {OrderId}\", orderId);
}

# Kibana KQL query
# level: \"Error\" and Application: \"OrderApi\" and @timestamp > now-1h""",
        "language": "csharp",
        "key_points": [
            "Structured JSON logging enables powerful queries",
            "Correlate logs with trace/span IDs",
            "Index per day for retention management",
            "Azure Monitor Logs is the managed alternative",
            "Never log PII or secrets",
        ],
    },
    "ansible-basics": {
        "explanation": (
            "**Ansible** is an agentless IT automation tool that configures servers, deploys apps, and orchestrates "
            "tasks using YAML **playbooks**. It connects over SSH (Linux) or WinRM (Windows) — no agent installed on "
            "targets. Each playbook contains **plays** (target hosts) and **tasks** (modules like apt, copy, service). "
            "Ansible is **idempotent** — running the same playbook twice produces the same result. Use Ansible for "
            "VM configuration (install Docker, agents, hardening) while Kubernetes handles container orchestration. "
            "**Inventory** files define target hosts; **roles** organize reusable task collections."
        ),
        "code": """# inventory.ini
[webservers]
web1 ansible_host=10.0.1.10
web2 ansible_host=10.0.1.11

[webservers:vars]
ansible_user=azureuser

# playbook.yml — install Docker on Ubuntu VMs
- hosts: webservers
  become: yes
  tasks:
    - name: Install required packages
      apt:
        name: [\"docker.io\", \"docker-compose\"]
        state: present
        update_cache: yes
    - name: Add user to docker group
      user:
        name: \"{{ ansible_user }}\"
        groups: docker
        append: yes
    - name: Ensure Docker is running
      service:
        name: docker
        state: started
        enabled: yes

# Run: ansible-playbook -i inventory.ini playbook.yml""",
        "language": "yaml",
        "key_points": [
            "Agentless — connects via SSH/WinRM",
            "Idempotent — safe to re-run playbooks",
            "Inventory defines target hosts",
            "Roles organize reusable automation",
            "Complements K8s — configures VMs, not containers",
        ],
    },
    "zero-downtime-deployments": {
        "explanation": (
            "**Zero-downtime deployments** ensure users never experience service interruption during releases. "
            "Strategies include **rolling updates** (gradually replace old instances), **blue-green** (two identical "
            "environments, instant traffic switch), and **canary** (route small percentage to new version first). "
            "Kubernetes rolling updates with `maxUnavailable: 0` maintain full capacity. **Readiness probes** ensure "
            "new instances only receive traffic when healthy. **App Service deployment slots** enable blue-green on "
            "Azure. Database migrations must be **backward compatible** (expand-contract pattern) so old and new code "
            "versions coexist during rollout."
        ),
        "code": """# K8s — rolling update with zero downtime
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # allow 1 extra pod during update
      maxUnavailable: 0  # never drop below 3 ready pods

# App Service — blue-green with slots
az webapp deployment slot create -g rg -n order-api --slot staging
az webapp deployment slot swap -g rg -n order-api --slot staging --target-slot production

# Database — expand-contract migration pattern
# Phase 1: add nullable column (old code ignores it)
# Phase 2: deploy new code writing to new column
# Phase 3: backfill data, make column required
# Phase 4: remove old column""",
        "language": "yaml",
        "key_points": [
            "maxUnavailable: 0 maintains full capacity",
            "Readiness probes gate traffic to healthy pods",
            "Blue-green: instant swap after validation",
            "Canary: gradual traffic shift to new version",
            "DB migrations must be backward compatible",
        ],
    },
    "css-box-model": {
        "explanation": (
            "The **CSS box model** defines how elements occupy space on the page. Every element is a rectangular box "
            "composed of four layers from inside out: **content**, **padding**, **border**, and **margin**. By default, "
            "`box-sizing: content-box` means the `width` property applies only to content — padding and border add "
            "extra size. Setting `box-sizing: border-box` includes padding and border in the declared width, making "
            "layouts predictable. **Margin collapse** occurs when adjacent vertical margins combine into the larger "
            "value. Apply `*, *::before, *::after { box-sizing: border-box; }` globally as a modern best practice."
        ),
        "code": """/* Global border-box reset */
*, *::before, *::after { box-sizing: border-box; }

.card {
  width: 300px;
  padding: 16px;
  border: 2px solid #ccc;
  margin: 8px;
  /* With border-box: total rendered width = 300px */
  /* With content-box: total = 300 + 32 + 4 = 336px */
}

.box-model-demo {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 5px solid #512BD4;
  margin: 10px;
}""",
        "language": "css",
        "key_points": [
            "content → padding → border → margin",
            "border-box includes padding/border in width",
            "Margin collapse on adjacent block elements",
            "Apply border-box globally for predictable sizing",
            "Use devtools box model overlay to debug",
        ],
    },
    "css-specificity": {
        "explanation": (
            "**CSS specificity** determines which rule wins when multiple rules target the same element. Specificity "
            "is calculated as (inline styles, ID selectors, class/attribute/pseudo-class selectors, element/pseudo-element "
            "selectors) — often written as four numbers like 0-2-1. Inline styles beat everything except `!important`. "
            "`!important` overrides normal cascade but creates maintenance nightmares — avoid except in utility classes. "
            "Keep selectors **shallow and class-based** (BEM) to avoid specificity wars. The cascade order is: "
            "origin → importance → specificity → source order."
        ),
        "code": """/* Specificity: 0-0-1 */
p { color: black; }

/* Specificity: 0-1-0 */
.highlight { color: yellow; }

/* Specificity: 0-1-1 */
.card p { color: blue; }

/* Specificity: 0-2-0 — wins over .card p */
.card-title { color: red; }

/* Specificity: 1-0-0 — inline style wins all */
/* <p style=\"color: green\"> */

/* Avoid */
#header .nav .item a { color: purple; } /* 0-1-3 — hard to override */""",
        "language": "css",
        "key_points": [
            "Inline > ID > class > element",
            "Avoid !important except utility overrides",
            "Shallow class selectors (BEM) prevent wars",
            "Same specificity: last rule in source wins",
            ":where() reduces specificity to zero",
        ],
    },
    "css-custom-properties": {
        "explanation": (
            "**CSS custom properties** (variables) are declared with `--name: value` and consumed with `var(--name)`. "
            "Unlike SASS variables (compile-time), CSS variables are **runtime** — they cascade through the DOM and "
            "can be changed via JavaScript or media queries. Define design tokens in `:root` and override per theme "
            "or component. Use fallback values: `var(--color-primary, #512BD4)`. Custom properties enable **dark mode**, "
            "theming, and dynamic spacing without rebuilding CSS. Angular Material and modern design systems rely "
            "heavily on CSS variables for theme switching."
        ),
        "code": """:root {
  --color-primary: #512BD4;
  --color-surface: #ffffff;
  --color-text: #1a1a1a;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --radius: 8px;
  --font-body: 'Segoe UI', system-ui, sans-serif;
}

.btn-primary {
  background: var(--color-primary);
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius);
  font-family: var(--font-body);
}

[data-theme=\"dark\"] {
  --color-primary: #7B68EE;
  --color-surface: #1e1e1e;
  --color-text: #e0e0e0;
}

/* JS toggle: document.documentElement.setAttribute('data-theme', 'dark') */""",
        "language": "css",
        "key_points": [
            "Runtime theming — unlike SASS compile-time vars",
            "Cascade and inherit through DOM tree",
            "Fallback: var(--name, defaultValue)",
            "Define design tokens in :root",
            "Override per component or theme attribute",
        ],
    },
    "css-units-rem-em": {
        "explanation": (
            "CSS provides absolute units (**px**) and relative units. **rem** (root em) is relative to the root "
            "element's font-size (typically 16px) — ideal for spacing and typography because it respects user browser "
            "font settings (accessibility). **em** is relative to the **parent** element's font-size — useful for "
            "component-scoped scaling but can compound unexpectedly. **vh/vw** are percentages of viewport height/width "
            "— `100vh` for full-screen heroes, but mobile browsers have issues with address bar resizing. Use "
            "**clamp()** for fluid typography: `font-size: clamp(1rem, 2.5vw, 2rem)`."
        ),
        "code": """html { font-size: 16px; }  /* 1rem = 16px */

body { font-size: 1rem; line-height: 1.5; }

h1 { font-size: 2.5rem; }    /* 40px */
h2 { font-size: 1.75rem; }   /* 28px */

.card {
  padding: 1.5rem;            /* 24px — scales with root */
  margin-bottom: 1rem;
}

.card__badge {
  font-size: 0.875em;         /* relative to .card font-size */
}

.hero {
  min-height: 100vh;          /* full viewport — test on mobile */
  padding: clamp(1rem, 5vw, 4rem);
}

.fluid-heading {
  font-size: clamp(1.5rem, 4vw, 3rem);
}""",
        "language": "css",
        "key_points": [
            "rem = root font-size — best for spacing/type",
            "em = parent font-size — can compound",
            "vh/vw for viewport-relative sizing",
            "clamp() for fluid responsive typography",
            "Avoid px for typography — breaks user zoom",
        ],
    },
    "css-reset-vs-normalize": {
        "explanation": (
            "Browsers apply default styles (user agent stylesheet) that differ across Chrome, Firefox, and Safari. "
            "A **CSS reset** (Eric Meyer's) sets all elements to zero/none — a blank canvas but requires re-adding "
            "all base styles. **Normalize.css** preserves useful defaults (like `h1` being bold) while fixing "
            "cross-browser inconsistencies. Modern projects often use a **minimal custom reset** or framework "
            "resets like **Tailwind Preflight**. The key goal is consistent starting point across browsers so your "
            "component styles behave predictably."
        ),
        "code": """/* Modern minimal reset (common in Angular/React apps) */
*, *::before, *::after {
  box-sizing: border-box;
}
* { margin: 0; }
body {
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}
img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
}
input, button, textarea, select {
  font: inherit;
}

/* Alternative: npm install normalize.css */
/* @import 'normalize.css'; */

/* Tailwind Preflight does similar automatically */""",
        "language": "css",
        "key_points": [
            "Reset = zero everything; Normalize = fix inconsistencies",
            "Most projects use minimal custom reset today",
            "Tailwind Preflight is a modern opinionated reset",
            "Always set box-sizing: border-box globally",
            "Test cross-browser after applying reset",
        ],
    },
    "viewport-meta-tag": {
        "explanation": (
            "The **viewport meta tag** tells mobile browsers how to scale and size the page. Without it, mobile "
            "browsers assume a ~980px desktop viewport and zoom out, making responsive CSS ineffective. "
            "`width=device-width` sets the viewport to the device's screen width. `initial-scale=1.0` prevents "
            "automatic zoom on load. Never use `user-scalable=no` or `maximum-scale=1` — this blocks pinch-to-zoom "
            "and fails **WCAG accessibility** requirements. Place the viewport meta tag in `<head>` before any "
            "CSS. It is the foundation of all responsive web design."
        ),
        "code": """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <!-- Do NOT use: user-scalable=no (accessibility violation) -->
  <title>Order Dashboard</title>
  <link rel=\"stylesheet\" href=\"styles.css\">
</head>
<body>
  <!-- Now media queries and responsive units work correctly -->
</body>
</html>""",
        "language": "html",
        "key_points": [
            "Required for responsive design on mobile",
            "width=device-width matches screen width",
            "Never disable user scaling (WCAG fail)",
            "Place in <head> before CSS",
            "Test on real devices, not just devtools",
        ],
    },
    "html5-semantic-deep-dive": {
        "explanation": (
            "**Semantic HTML5 elements** convey meaning to browsers, search engines, and assistive technologies — not "
            "just visual structure. Key elements: `<header>` (introductory content), `<nav>` (navigation links), "
            "`<main>` (primary content — one per page), `<article>` (self-contained content), `<section>` (thematic "
            "grouping with heading), `<aside>` (tangentially related), `<footer>` (footer info), `<figure>`/`<figcaption>` "
            "(media with caption). Semantic markup improves **SEO** (Google understands page structure), **accessibility** "
            "(screen readers navigate by landmarks), and **maintainability** (code reads like an outline)."
        ),
        "code": """<!DOCTYPE html>
<html lang=\"en\">
<body>
  <header>
    <nav aria-label=\"Main navigation\">
      <a href=\"/\">Home</a>
      <a href=\"/orders\">Orders</a>
    </nav>
  </header>

  <main id=\"content\">
    <article>
      <header>
        <h1>Order #1042</h1>
        <time datetime=\"2026-06-23\">June 23, 2026</time>
      </header>
      <section aria-labelledby=\"items-heading\">
        <h2 id=\"items-heading\">Line Items</h2>
        <table>...</table>
      </section>
      <footer><p>Total: $249.99</p></footer>
    </article>
    <aside aria-label=\"Related orders\">
      <h2>Recent Orders</h2>
    </aside>
  </main>

  <footer>&copy; 2026 OrderApp</footer>
</body>
</html>""",
        "language": "html",
        "key_points": [
            "One <main> per page for accessibility",
            "Every <section> needs a heading",
            "Landmark roles improve screen reader navigation",
            "Better SEO than div soup",
            "Use <time datetime> for machine-readable dates",
        ],
    },
    "aria-attributes": {
        "explanation": (
            "**WAI-ARIA** (Accessible Rich Internet Applications) attributes enhance accessibility when native HTML "
            "semantics are insufficient. The first rule of ARIA: **don't use ARIA if native HTML works** — use `<button>` "
            "not `<div role=\"button\">`. Key attributes: `aria-label` (accessible name), `aria-labelledby`/`aria-describedby` "
            "(reference other elements), `aria-expanded`/`aria-controls` (disclosure widgets), `aria-live` (dynamic content "
            "announcements), `aria-hidden=\"true\"` (hide decorative elements from screen readers). Test with NVDA, "
            "VoiceOver, or axe DevTools."
        ),
        "code": """<!-- Disclosure widget -->
<button type=\"button\"
        aria-expanded=\"false\"
        aria-controls=\"filter-menu\"
        id=\"filter-btn\">
  Filters
</button>
<ul id=\"filter-menu\" role=\"menu\" aria-labelledby=\"filter-btn\" hidden>
  <li role=\"menuitem\">Status</li>
  <li role=\"menuitem\">Date Range</li>
</ul>

<!-- Dynamic status updates -->
<div aria-live=\"polite\" aria-atomic=\"true\" class=\"sr-only\">
  {{ saveStatusMessage }}
</div>

<!-- Form field association -->
<label for=\"email\">Email</label>
<input id=\"email\" type=\"email\"
       aria-describedby=\"email-hint\"
       aria-invalid=\"{{ emailInvalid\"
       required>
<span id=\"email-hint\">We'll never share your email.</span>
<span id=\"email-error\" role=\"alert\" *ngIf=\"emailInvalid\">Invalid email.</span>

<!-- Decorative icon -->
<span aria-hidden=\"true\">📦</span> Order shipped""",
        "language": "html",
        "key_points": [
            "First rule: use native HTML before ARIA",
            "aria-live for dynamic content announcements",
            "aria-describedby links inputs to hint/error text",
            "aria-hidden hides decorative content",
            "Test with screen readers and axe DevTools",
        ],
    },
    "html-forms-validation": {
        "explanation": (
            "HTML forms collect user input with built-in **constraint validation**. Attributes like `required`, "
            "`min`/`max`, `pattern`, `type=\"email\"`, and `type=\"url\"` trigger native browser validation. The "
            "`novalidate` attribute disables native validation, deferring to JavaScript/framework validation (Angular "
            "Reactive Forms). Always pair inputs with `<label for=\"id\">` for accessibility. Display errors with "
            "`role=\"alert\"` so screen readers announce them. Use `aria-invalid=\"true\"` and `aria-describedby` "
            "pointing to error messages. Combine HTML5 validation for simple cases with framework validation for "
            "complex business rules."
        ),
        "code": """<form [formGroup]=\"orderForm\" (ngSubmit)=\"submit()\" novalidate>
  <div class=\"field\">
    <label for=\"qty\">Quantity</label>
    <input id=\"qty\" type=\"number\" formControlName=\"quantity\"
           min=\"1\" max=\"99\" required
           [attr.aria-invalid]=\"orderForm.get('quantity')?.invalid\"
           aria-describedby=\"qty-error\">
    <span id=\"qty-error\" role=\"alert\"
          *ngIf=\"orderForm.get('quantity')?.touched && orderForm.get('quantity')?.invalid\">
      Enter a quantity between 1 and 99.
    </span>
  </div>

  <div class=\"field\">
    <label for=\"email\">Email</label>
    <input id=\"email\" type=\"email\" formControlName=\"email\"
           pattern=\"[a-z0-9._%+\\-]+@[a-z0-9.\\-]+\\.[a-z]{2,}$\"
           required aria-describedby=\"email-hint\">
    <span id=\"email-hint\">Order confirmation will be sent here.</span>
  </div>

  <button type=\"submit\" [disabled]=\"orderForm.invalid\">Place Order</button>
</form>""",
        "language": "html",
        "key_points": [
            "Always use <label for=\"id\"> with inputs",
            "role=\"alert\" for error messages",
            "aria-invalid and aria-describedby for accessibility",
            "HTML5 types: email, url, number, date, tel",
            "novalidate + framework validation for complex rules",
        ],
    },
    "flexbox-advanced": {
        "explanation": (
            "Advanced **Flexbox** techniques go beyond basic centering. **`flex-grow`**, **`flex-shrink`**, and "
            "**`flex-basis`** control how items grow, shrink, and set initial size — shorthand `flex: 1 1 200px`. "
            "**`flex-wrap: wrap`** allows items to flow to new lines. **`align-self`** overrides alignment for "
            "individual items. **`order`** changes visual order without changing DOM (use cautiously for a11y). "
            "**`gap`** replaces margin hacks for spacing between items. Common patterns: sticky footer, equal-height "
            "columns, responsive toolbars, and navigation bars."
        ),
        "code": """/* Responsive toolbar */
.toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}
.toolbar__brand { flex: 0 0 auto; }
.toolbar__search { flex: 1 1 200px; min-width: 0; }
.toolbar__actions {
  flex: 0 0 auto;
  display: flex;
  gap: 0.5rem;
}

/* Sticky footer layout */
.page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.page__content { flex: 1; }

/* Equal-height cards in a row */
.card-row {
  display: flex;
  align-items: stretch;
  gap: 1rem;
}
.card-row > * { flex: 1; }""",
        "language": "css",
        "key_points": [
            "flex: 1 = flex: 1 1 0%",
            "min-width: 0 prevents flex item overflow",
            "gap replaces margin spacing hacks",
            "align-self for per-item override",
            "flex-wrap for responsive toolbars",
        ],
    },
    "css-grid-advanced": {
        "explanation": (
            "Advanced **CSS Grid** features enable complex layouts without media queries. **`grid-template-areas`** "
            "assign named regions for readable layout code. **`repeat(auto-fit, minmax(280px, 1fr))`** creates "
            "responsive columns that auto-wrap. **`subgrid`** (modern browsers) lets nested grids inherit parent "
            "track sizing. **`grid-auto-flow: dense`** fills gaps in masonry-like layouts. Grid excels at "
            "two-dimensional page layouts while Flexbox handles one-dimensional component internals. Combine both: "
            "Grid for page shell, Flexbox inside grid cells."
        ),
        "code": """/* Named grid areas — dashboard layout */
.page-layout {
  display: grid;
  min-height: 100vh;
  grid-template-areas:
    \"header header\"
    \"sidebar main\"
    \"footer footer\";
  grid-template-columns: 240px 1fr;
  grid-template-rows: auto 1fr auto;
}
.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }
.footer  { grid-area: footer; }

@media (max-width: 768px) {
  .page-layout {
    grid-template-areas:
      \"header\"
      \"main\"
      \"footer\";
    grid-template-columns: 1fr;
  }
  .sidebar { display: none; }
}

/* Auto-responsive card grid — no media query needed */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}""",
        "language": "css",
        "key_points": [
            "grid-template-areas for readable layouts",
            "auto-fit + minmax for responsive columns",
            "Grid for 2D page layouts, Flexbox for 1D components",
            "subgrid aligns nested items to parent tracks",
            "Combine Grid shell + Flexbox components",
        ],
    },
    "media-queries": {
        "explanation": (
            "**Media queries** apply CSS conditionally based on device characteristics. Width queries "
            "(`min-width`, `max-width`) are most common for responsive breakpoints. Modern queries also target "
            "**user preferences**: `prefers-color-scheme` (dark/light), `prefers-reduced-motion` (accessibility), "
            "and `prefers-contrast`. Use **mobile-first** approach: base styles for small screens, `min-width` "
            "queries to enhance for larger viewports. **Container queries** (`@container`) respond to parent "
            "container size, enabling truly component-level responsiveness independent of viewport."
        ),
        "code": """/* Mobile-first breakpoints */
.container { padding: 1rem; }

@media (min-width: 768px) {   /* tablet */
  .container { padding: 2rem; max-width: 720px; }
}
@media (min-width: 1024px) {  /* desktop */
  .container { max-width: 960px; }
}
@media (min-width: 1280px) {  /* wide */
  .container { max-width: 1200px; }
}

/* User preference queries */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
@media (prefers-color-scheme: dark) {
  :root { --bg: #121212; --text: #e0e0e0; }
}

/* Container query — component-level responsive */
.card-container { container-type: inline-size; }
@container (min-width: 400px) {
  .card { display: grid; grid-template-columns: 120px 1fr; }
}""",
        "language": "css",
        "key_points": [
            "Mobile-first: base styles + min-width queries",
            "prefers-reduced-motion for accessibility",
            "prefers-color-scheme for dark mode",
            "Container queries for component responsiveness",
            "Avoid too many breakpoints — content-driven",
        ],
    },
    "mobile-first-design": {
        "explanation": (
            "**Mobile-first design** starts with base CSS for the smallest screens, then progressively enhances "
            "for tablets and desktops using `min-width` media queries. This forces prioritization of essential "
            "content and performance. Contrast with **desktop-first** (max-width queries) which tends to hide "
            "rather than enhance. Key practices: touch targets ≥ 44×44px, readable font sizes (16px minimum), "
            "avoid hover-only interactions, optimize images for mobile bandwidth, and test on real devices. "
            "Angular's CDK BreakpointObserver programmatically responds to viewport changes."
        ),
        "code": """/* Mobile-first base styles */
.nav {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}
.sidebar { display: none; }

/* Tablet enhancement */
@media (min-width: 768px) {
  .nav { flex-direction: row; justify-content: space-between; }
  .grid { grid-template-columns: repeat(2, 1fr); }
}

/* Desktop enhancement */
@media (min-width: 1024px) {
  .layout {
    display: grid;
    grid-template-columns: 240px 1fr;
  }
  .sidebar { display: block; }
  .grid { grid-template-columns: repeat(3, 1fr); }
}""",
        "language": "css",
        "key_points": [
            "Base styles target smallest screen",
            "min-width queries add enhancements",
            "Touch targets ≥ 44×44px",
            "Progressive enhancement over graceful degradation",
            "Test on real mobile devices",
        ],
    },
    "pseudo-classes-elements": {
        "explanation": (
            "**Pseudo-classes** select elements in a specific state: **:hover**, **:focus-visible**, **:active**, "
            "**:nth-child(n)**, **:not()**, **:checked**, **:disabled**. **Pseudo-elements** create virtual elements: "
            "**::before**, **::after**, **::first-line**, **::placeholder**. Use **:focus-visible** instead of **:focus** "
            "to show focus rings only for keyboard navigation (not mouse clicks). **::before**/**::after** require "
            "the **content** property. **:nth-child(even)** enables zebra striping. Combine pseudo-classes with "
            "pseudo-elements for tooltips, decorative markers, and form validation styling."
        ),
        "code": """/* Keyboard-only focus ring */
a:focus-visible,
button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
a:focus:not(:focus-visible) { outline: none; }

/* Zebra striping */
tbody tr:nth-child(even) { background: #f8f9fa; }

/* Form validation styling */
input:invalid:not(:placeholder-shown) {
  border-color: #dc3545;
}
input:valid:not(:placeholder-shown) {
  border-color: #28a745;
}

/* Tooltip with pseudo-element */
.tooltip { position: relative; }
.tooltip::after {
  content: attr(data-tip);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: #333;
  color: #fff;
  padding: 4px 8px;
  border-radius: 4px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
}
.tooltip:hover::after,
.tooltip:focus-visible::after { opacity: 1; }""",
        "language": "css",
        "key_points": [
            ":focus-visible for keyboard-only focus rings",
            "::before/::after require content property",
            ":nth-child for zebra striping and patterns",
            ":not() excludes elements from rules",
            ":invalid/:valid for form feedback styling",
        ],
    },
    "css-animations-transitions": {
        "explanation": (
            "**CSS transitions** smoothly animate property changes between two states when triggered (hover, class "
            "toggle, JS). Specify `transition: property duration timing-function`. **CSS animations** use `@keyframes` "
            "to define multi-step sequences that run automatically. Use transitions for micro-interactions (button "
            "hover, modal fade) and animations for complex sequences (loading spinners, slide-in panels). Always "
            "respect `@media (prefers-reduced-motion: reduce)` for accessibility — disable or simplify animations "
            "for users who prefer reduced motion."
        ),
        "code": """/* Transitions — micro-interactions */
.btn {
  background: var(--color-primary);
  transform: translateY(0);
  transition: background-color 0.2s ease,
              transform 0.15s ease,
              box-shadow 0.2s ease;
}
.btn:hover {
  background: #3a1fa0;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(81, 43, 212, 0.3);
}

/* Keyframe animation — modal entrance */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}
.modal {
  animation: fadeInUp 0.3s ease-out;
}

/* Accessibility — respect user preference */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}""",
        "language": "css",
        "key_points": [
            "Transitions for two-state property changes",
            "Animations for multi-step @keyframes sequences",
            "Use transform/opacity for GPU-accelerated animation",
            "Always respect prefers-reduced-motion",
            "Keep animations under 300ms for UI feedback",
        ],
    },
    "bem-methodology": {
        "explanation": (
            "**BEM (Block Element Modifier)** is a CSS naming convention that creates predictable, flat selectors. "
            "A **Block** is a standalone component (`.card`). An **Element** is a part of a block (`.card__title`). "
            "A **Modifier** changes appearance or behavior (`.card--highlighted`, `.card__title--large`). BEM avoids "
            "deep nesting (`.card .title`) that causes specificity wars. Elements and modifiers combine with the "
            "block class. While utility-first frameworks like Tailwind reduce the need for custom BEM CSS, understanding "
            "BEM remains valuable for component-based architectures and Angular component styles."
        ),
        "code": """/* Block */
.card {
  padding: 1rem;
  border-radius: 8px;
  background: var(--color-surface);
}

/* Elements */
.card__header { margin-bottom: 0.75rem; }
.card__title { font-size: 1.25rem; font-weight: 600; }
.card__body { color: var(--color-text-muted); }
.card__footer { margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid #eee; }

/* Modifiers */
.card--highlighted { border: 2px solid var(--color-primary); }
.card--compact { padding: 0.5rem; }
.card__title--large { font-size: 1.5rem; }

<!-- HTML -->
<article class=\"card card--highlighted\">
  <div class=\"card__header\">
    <h2 class=\"card__title card__title--large\">Order Summary</h2>
  </div>
  <div class=\"card__body\">3 items — $249.99</div>
  <div class=\"card__footer\">
    <button class=\"btn btn-primary\">Checkout</button>
  </div>
</article>""",
        "language": "css",
        "key_points": [
            "Block__Element--Modifier naming",
            "Flat selectors — no .block .element nesting",
            "Modifiers combine with block/element classes",
            "Reduces specificity conflicts",
            "Works well with component-based frameworks",
        ],
    },
    "bootstrap-vs-tailwind": {
        "explanation": (
            "**Bootstrap** is a component-based CSS framework with pre-built UI components (buttons, modals, navbars), "
            "a 12-column grid, and JavaScript plugins. It provides opinionated defaults for rapid prototyping. "
            "**Tailwind CSS** is utility-first — compose designs by applying atomic classes (`flex`, `p-4`, `bg-blue-500`) "
            "directly in HTML. Tailwind offers more design control and typically produces smaller custom CSS via "
            "purging unused utilities. Bootstrap 5 dropped jQuery; Tailwind requires a build step. Both support "
            "dark mode, responsive utilities, and integrate with Angular. Choose Bootstrap for speed; Tailwind for "
            "custom design systems."
        ),
        "code": """<!-- Bootstrap 5 -->
<nav class=\"navbar navbar-expand-lg navbar-dark bg-primary\">
  <a class=\"navbar-brand\" href=\"#\">OrderApp</a>
  <div class=\"collapse navbar-collapse\">
    <ul class=\"navbar-nav ms-auto\">
      <li class=\"nav-item\"><a class=\"nav-link\" href=\"/orders\">Orders</a></li>
    </ul>
  </div>
</nav>
<div class=\"row g-3\">
  <div class=\"col-md-4\"><div class=\"card\">...</div></div>
</div>

<!-- Tailwind CSS -->
<nav class=\"flex items-center justify-between bg-indigo-600 text-white px-6 py-3\">
  <a href=\"#\" class=\"text-xl font-bold\">OrderApp</a>
  <a href=\"/orders\" class=\"hover:text-indigo-200\">Orders</a>
</nav>
<div class=\"grid grid-cols-1 md:grid-cols-3 gap-4 p-4\">
  <div class=\"rounded-lg shadow-md p-4 bg-white\">...</div>
</div>""",
        "language": "html",
        "key_points": [
            "Bootstrap = pre-built components, faster prototyping",
            "Tailwind = utility-first, more design control",
            "Both support responsive and dark mode",
            "Tailwind purges unused CSS for smaller bundles",
            "Angular works with both via ng add or manual setup",
        ],
    },
    "responsive-images": {
        "explanation": (
            "**Responsive images** serve appropriately sized images based on device viewport and resolution, saving "
            "bandwidth and improving LCP (Largest Contentful Paint). Use **`srcset`** with width descriptors (`400w`) "
            "and **`sizes`** to tell the browser how wide the image renders at different breakpoints. **`<picture>`** "
            "enables **art direction** — different crops for mobile vs desktop. Always include **`width` and `height`** "
            "attributes to prevent Cumulative Layout Shift (CLS). Use **`loading=\"lazy\"`** for below-fold images. "
            "Serve modern formats (WebP, AVIF) via `<picture>` `<source>` elements."
        ),
        "code": """<!-- Resolution switching with srcset -->
<img
  src=\"product-800.jpg\"
  srcset=\"product-400.jpg 400w,
          product-800.jpg 800w,
          product-1200.jpg 1200w\"
  sizes=\"(max-width: 600px) 100vw,
         (max-width: 1024px) 50vw,
         400px\"
  alt=\"Wireless headphones\"
  loading=\"lazy\"
  width=\"800\"
  height=\"600\">

<!-- Art direction with picture -->
<picture>
  <source media=\"(min-width: 768px)\" srcset=\"banner-wide.webp\" type=\"image/webp\">
  <source media=\"(max-width: 767px)\" srcset=\"banner-mobile.webp\" type=\"image/webp\">
  <img src=\"banner-fallback.jpg\" alt=\"Summer sale banner\"
       width=\"1200\" height=\"400\">
</picture>""",
        "language": "html",
        "key_points": [
            "srcset + sizes for resolution switching",
            "picture element for art direction",
            "width/height prevent layout shift (CLS)",
            "loading=\"lazy\" for below-fold images",
            "WebP/AVIF via picture source elements",
        ],
    },
    "wcag-accessibility": {
        "explanation": (
            "**WCAG 2.1** (Web Content Accessibility Guidelines) defines how to make web content accessible to people "
            "with disabilities. Conformance levels: **A** (minimum), **AA** (industry standard), **AAA** (enhanced). "
            "Four principles — **Perceivable** (alt text, contrast), **Operable** (keyboard access, no seizures), "
            "**Understandable** (clear labels, predictable), **Robust** (valid HTML, ARIA). Key AA requirements: "
            "4.5:1 contrast ratio for normal text, all functionality via keyboard, visible focus indicators, form "
            "labels, and skip navigation links. Audit with axe DevTools, Lighthouse, or WAVE."
        ),
        "code": """<!-- Skip link for keyboard users -->
<a href=\"#main-content\" class=\"skip-link\">Skip to main content</a>

<main id=\"main-content\">
  <!-- Perceivable: meaningful alt text -->
  <img src=\"chart-q2.png\"
       alt=\"Q2 2026 revenue chart showing 12% growth to $4.2M\">

  <!-- Operable: keyboard-accessible custom button -->
  <button type=\"button\" aria-label=\"Close dialog\"
          (click)=\"close()\" (keydown.escape)=\"close()\">
    &times;
  </button>

  <!-- Understandable: associated labels -->
  <label for=\"search\">Search orders</label>
  <input id=\"search\" type=\"search\" autocomplete=\"off\">
</main>

/* Focus visible — WCAG 2.4.7 */
:focus-visible {
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}
.skip-link {
  position: absolute;
  top: -100%;
  left: 0;
  z-index: 1000;
}
.skip-link:focus { top: 0; }""",
        "language": "html",
        "key_points": [
            "AA is the industry standard conformance level",
            "4.5:1 contrast for normal text, 3:1 for large",
            "All functionality must work via keyboard",
            "Meaningful alt text for informative images",
            "Audit with axe DevTools and Lighthouse",
        ],
    },
    "dark-mode-implementation": {
        "explanation": (
            "**Dark mode** reduces eye strain and saves battery on OLED screens. Implement with CSS custom properties "
            "and toggle via `prefers-color-scheme` media query (respects OS setting) plus an optional manual toggle "
            "stored in `localStorage`. Define light theme tokens in `:root` and override in `[data-theme=\"dark\"]` "
            "or `@media (prefers-color-scheme: dark)`. Use `color-scheme: dark` CSS property to style native form "
            "controls. Angular Material provides built-in dark theme support. Ensure sufficient contrast ratios "
            "in both themes for WCAG AA compliance."
        ),
        "code": """:root {
  color-scheme: light;
  --bg-primary: #ffffff;
  --bg-surface: #f5f5f5;
  --text-primary: #1a1a1a;
  --text-muted: #666666;
  --border: #e0e0e0;
}

@media (prefers-color-scheme: dark) {
  :root {
    color-scheme: dark;
    --bg-primary: #121212;
    --bg-surface: #1e1e1e;
    --text-primary: #e0e0e0;
    --text-muted: #aaaaaa;
    --border: #333333;
  }
}

[data-theme=\"dark\"] {
  color-scheme: dark;
  --bg-primary: #121212;
  --bg-surface: #1e1e1e;
  --text-primary: #e0e0e0;
  --text-muted: #aaaaaa;
  --border: #333333;
}

body {
  background: var(--bg-primary);
  color: var(--text-primary);
}

// Toggle with persistence
// const theme = localStorage.getItem('theme') || 'auto';
// document.documentElement.setAttribute('data-theme', theme);""",
        "language": "css",
        "key_points": [
            "CSS variables enable runtime theme switching",
            "prefers-color-scheme respects OS preference",
            "Manual toggle + localStorage for user choice",
            "color-scheme styles native form controls",
            "Verify contrast ratios in both themes",
        ],
    },
    "css-preprocessors-sass": {
        "explanation": (
            "**CSS preprocessors** like SASS/SCSS extend CSS with variables, nesting, mixins, functions, and imports — "
            "compiled to standard CSS at build time. SASS variables are **compile-time** (unlike CSS custom properties). "
            "**Mixins** reuse declaration blocks with parameters. **Nesting** mirrors HTML structure but can produce "
            "over-specific selectors if overused. Modern native CSS now supports nesting, `@layer`, and custom properties, "
            "reducing the need for preprocessors. Angular CLI supports SASS out of the box (`scss` in angular.json). "
            "Many teams migrate from SASS variables to CSS custom properties for theming."
        ),
        "code": """// _variables.scss
$primary: #512BD4;
$spacing-md: 1rem;
$breakpoint-md: 768px;

// _mixins.scss
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

@mixin respond-to($breakpoint) {
  @media (min-width: $breakpoint) { @content; }
}

// card.component.scss
@import 'variables';
@import 'mixins';

.card {
  padding: $spacing-md;
  border: 1px solid lighten($primary, 40%);

  &__title {
    color: $primary;
    font-size: 1.25rem;
  }

  &--highlighted {
    border-color: $primary;
    @include flex-center;
  }

  @include respond-to($breakpoint-md) {
    padding: 2rem;
  }
}""",
        "language": "scss",
        "key_points": [
            "SASS compiles to CSS at build time",
            "Mixins reuse parameterized declaration blocks",
            "Avoid deep nesting — causes specificity issues",
            "Native CSS now has nesting, @layer, variables",
            "Angular CLI supports SCSS by default",
        ],
    },
    "critical-css-performance": {
        "explanation": (
            "**Critical CSS** is the minimum CSS needed to render above-the-fold content. Inlining it in `<head>` "
            "eliminates render-blocking requests for the first paint, improving **LCP** and **FCP** metrics. Load "
            "the full stylesheet asynchronously with `rel=\"preload\"` + `onload` swap. Tools like **Critical**, "
            "**Penthouse**, and build plugins (Angular critical CSS inlining) automate extraction. Also preload "
            "hero images and fonts. Target the LCP element specifically. Balance inline size (keep under ~14KB) "
            "against caching benefits of external stylesheets."
        ),
        "code": """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Order Dashboard</title>

  <!-- Inline critical CSS (~2-4 KB) -->
  <style>
    body { margin: 0; font-family: system-ui, sans-serif; color: #1a1a1a; }
    .header { display: flex; align-items: center; padding: 1rem; background: #512BD4; color: #fff; }
    .hero { min-height: 60vh; display: flex; align-items: center; padding: 2rem; }
    .hero h1 { font-size: clamp(1.5rem, 4vw, 3rem); }
  </style>

  <!-- Async load full stylesheet -->
  <link rel=\"preload\" href=\"styles.css\" as=\"style\"
        onload=\"this.onload=null;this.rel='stylesheet'\">
  <noscript><link rel=\"stylesheet\" href=\"styles.css\"></noscript>

  <!-- Preload LCP image -->
  <link rel=\"preload\" href=\"hero.webp\" as=\"image\" type=\"image/webp\">
</head>""",
        "language": "html",
        "key_points": [
            "Inline above-the-fold CSS in <head>",
            "Async load full stylesheet with preload",
            "Keep inline critical CSS under ~14KB",
            "Preload LCP image and critical fonts",
            "Automate extraction with build tools",
        ],
    },
    "z-index-stacking-context": {
        "explanation": (
            "**z-index** controls stacking order, but only among elements in the same **stacking context**. A new "
            "stacking context is created by: `position` + z-index, `opacity` < 1, `transform`, `filter`, `isolation: "
            "isolate`, and others. A child with `z-index: 9999` inside a parent with `z-index: 1` cannot appear "
            "above a sibling with `z-index: 2`. Fix by moving modals/tooltips to the document body (Angular CDK Overlay "
            "does this). Use `isolation: isolate` to intentionally create a context. Avoid z-index values like 99999."
        ),
        "code": """/* Problem: z-index trapped in parent context */
.header {
  position: relative;
  z-index: 1;  /* creates stacking context */
}
.header .dropdown {
  position: absolute;
  z-index: 9999;  /* still below .sidebar z-index: 2 */
}
.sidebar {
  position: relative;
  z-index: 2;
}

/* Solution 1: portal modal to body (Angular CDK Overlay) */
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 1000;
  background: rgba(0,0,0,0.5);
}
.modal {
  position: fixed;
  z-index: 1001;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
}

/* Solution 2: intentional isolation */
.widget { isolation: isolate; }""",
        "language": "css",
        "key_points": [
            "z-index only compares within same stacking context",
            "position + z-index creates new context",
            "Portal modals to document body to escape",
            "isolation: isolate for intentional contexts",
            "Avoid z-index: 9999 — use structured layers",
        ],
    },
    "css-containment": {
        "explanation": (
            "**CSS containment** tells the browser that an element's subtree is independent, enabling rendering "
            "optimizations. `contain: layout` isolates layout calculations. `contain: paint` clips painting to "
            "bounds. `contain: style` isolates counter/quote scope. `contain: strict` combines all three. "
            "**`content-visibility: auto`** skips rendering off-screen content until needed — powerful for long "
            "lists and data tables. **`contain-intrinsic-size`** provides placeholder dimensions to prevent layout "
            "shift when content becomes visible. Essential for performance in data-heavy Angular applications."
        ),
        "code": """/* Contain layout recalculations to this subtree */
.order-card {
  contain: layout style paint;
}

/* Virtual scroll / long list optimization */
.virtual-list-item {
  content-visibility: auto;
  contain-intrinsic-size: 0 48px;  /* placeholder height */
}

/* Data table row — skip off-screen rendering */
.table-row {
  content-visibility: auto;
  contain-intrinsic-size: 0 52px;
}

/* Strict containment for isolated widgets */
.dashboard-widget {
  contain: strict;
  overflow: hidden;
}

/* Angular CDK Virtual Scroll uses similar concepts internally */""",
        "language": "css",
        "key_points": [
            "contain: strict = layout + style + paint",
            "content-visibility: auto skips off-screen rendering",
            "contain-intrinsic-size prevents layout shift",
            "Powerful for long lists and data tables",
            "Angular CDK Virtual Scroll for large datasets",
        ],
    },
    "print-stylesheets": {
        "explanation": (
            "**Print stylesheets** optimize page layout when users print or save as PDF. Use `@media print` to hide "
            "navigation, buttons, and ads; adjust colors for ink savings; and control page breaks. Show link URLs "
            "after anchor text with `::after { content: \" (\" attr(href) \")\" }`. Use `page-break-inside: avoid` "
            "on tables and figures to prevent awkward splits. Set `@page` margins and paper size. Essential for "
            "invoice, report, and order summary pages in enterprise applications."
        ),
        "code": """@media print {
  /* Hide non-essential UI */
  .sidebar, .navbar, .btn, .footer-nav,
  .toast, .modal-backdrop { display: none !important; }

  /* Optimize for print */
  body {
    font-size: 12pt;
    color: #000;
    background: #fff;
  }

  /* Show link URLs */
  a[href^=\"http\"]::after {
    content: \" (\" attr(href) \")\";
    font-size: 0.8em;
    color: #666;
  }

  /* Prevent awkward page breaks */
  .order-table, .invoice-header, figure {
    page-break-inside: avoid;
  }
  h2, h3 { page-break-after: avoid; }

  /* Page setup */
  @page {
    margin: 2cm;
    size: A4 portrait;
  }
}""",
        "language": "css",
        "key_points": [
            "Hide navigation and interactive elements",
            "page-break-inside: avoid for tables",
            "Show URLs for external links",
            "Use @page for margins and paper size",
            "Test with browser Print Preview",
        ],
    },
    "css-layer": {
        "explanation": (
            "**CSS cascade layers** (`@layer`) control the order in which styles cascade, independent of specificity "
            "and source order. Declare layer order upfront: `@layer reset, base, components, utilities`. Rules in "
            "later-declared layers win over earlier layers regardless of selector specificity. This solves "
            "specificity wars in large codebases where utility classes need to override component styles. Unlayered "
            "CSS beats all layers. **Tailwind v4** uses layers internally. Layers work alongside `@import` and "
            "can be nested."
        ),
        "code": """/* Declare layer order — later layers win */
@layer reset, base, components, utilities;

@layer reset {
  *, *::before, *::after { box-sizing: border-box; margin: 0; }
}

@layer base {
  body { font-family: system-ui, sans-serif; line-height: 1.5; }
  h1 { font-size: 2rem; font-weight: 700; }
}

@layer components {
  .btn {
    padding: 0.5rem 1rem;
    border-radius: 4px;
    background: var(--color-primary);
    color: #fff;
  }
  .card { padding: 1rem; border: 1px solid #eee; border-radius: 8px; }
}

@layer utilities {
  .text-center { text-align: center; }
  .mt-4 { margin-top: 1rem; }
  .hidden { display: none; }
}

/* Unlayered CSS beats ALL layers */
/* .btn { background: red; } — this wins over @layer components .btn */""",
        "language": "css",
        "key_points": [
            "Layers control cascade order independent of specificity",
            "Later-declared layers win over earlier layers",
            "Unlayered CSS beats all layered CSS",
            "Solves specificity wars in large codebases",
            "Tailwind v4 uses @layer internally",
        ],
    },
}
