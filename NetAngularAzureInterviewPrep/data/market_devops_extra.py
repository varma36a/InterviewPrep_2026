"""Additional Docker/DevOps interview topics — expands optional section to 50+."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("optional", "foundation"): [
        InterviewItem(
            "docker-run-exec-logs",
            "Explain docker run, exec, and logs commands.",
            "Core CLI for starting containers, running commands inside, and viewing output.",
            "",
        ),
        InterviewItem(
            "docker-buildx",
            "What is Docker Buildx and multi-platform builds?",
            "Extended builder for cache, multi-arch images, and build secrets.",
            "",
        ),
        InterviewItem(
            "docker-registry",
            "How do Docker registries work? Compare Docker Hub, ACR, ECR.",
            "Store and distribute images — tags, digests, authentication.",
            "",
        ),
        InterviewItem(
            "k8s-namespaces",
            "What are Kubernetes namespaces?",
            "Virtual clusters for isolation, RBAC, quotas, and resource organization.",
            "",
        ),
        InterviewItem(
            "masstransit-basics",
            "What is MassTransit and how does it abstract message brokers?",
            ".NET distributed application framework over RabbitMQ, Azure Service Bus, Kafka.",
            "",
        ),
        InterviewItem(
            "dependabot",
            "What is Dependabot and how does it improve supply chain security?",
            "Automated dependency update PRs for NuGet, npm, Docker, GitHub Actions.",
            "",
        ),
        InterviewItem(
            "packer-basics",
            "What is HashiCorp Packer?",
            "Build identical machine images for multiple platforms from one template.",
            "",
        ),
    ],
    ("optional", "intermediate"): [
        InterviewItem(
            "k8s-statefulset",
            "When do you use a StatefulSet instead of a Deployment?",
            "Stable network identity and persistent storage for stateful workloads.",
            "",
        ),
        InterviewItem(
            "k8s-daemonset",
            "What is a Kubernetes DaemonSet?",
            "Runs one pod per node — logging agents, monitoring, CNI plugins.",
            "",
        ),
        InterviewItem(
            "k8s-jobs-cronjobs",
            "Explain Kubernetes Jobs and CronJobs.",
            "Run-to-completion workloads and scheduled batch tasks.",
            "",
        ),
        InterviewItem(
            "k8s-network-policy",
            "What are Kubernetes NetworkPolicies?",
            "Pod-level firewall rules controlling ingress/egress traffic.",
            "",
        ),
        InterviewItem(
            "github-actions-matrix",
            "How do matrix builds work in GitHub Actions?",
            "Run jobs across multiple OS, runtime, or configuration dimensions.",
            "",
        ),
        InterviewItem(
            "trivy-scanning",
            "How do you scan containers with Trivy?",
            "Open-source scanner for image vulnerabilities, misconfigs, and secrets.",
            "",
        ),
        InterviewItem(
            "helm-values-templates",
            "Explain Helm values, templates, and _helpers.tpl.",
            "Parameterize Kubernetes manifests with Go templating and release values.",
            "",
        ),
    ],
    ("optional", "advanced"): [
        InterviewItem(
            "k8s-rbac",
            "Explain Kubernetes RBAC — Roles, ClusterRoles, Bindings.",
            "Least-privilege access control for users and service accounts.",
            "",
        ),
        InterviewItem(
            "argocd-gitops",
            "What is Argo CD and GitOps deployment?",
            "Declarative continuous delivery — Git as source of truth for cluster state.",
            "",
        ),
        InterviewItem(
            "istio-basics",
            "What is Istio service mesh? Sidecar, traffic management, mTLS.",
            "L7 observability, security, and routing for microservices on Kubernetes.",
            "",
        ),
        InterviewItem(
            "flux-cd",
            "What is Flux CD and how does it differ from Argo CD?",
            "GitOps toolkit — controllers reconcile cluster from Git repositories.",
            "",
        ),
        InterviewItem(
            "k8s-resource-limits",
            "Explain Kubernetes requests, limits, and ResourceQuotas.",
            "CPU/memory scheduling guarantees and namespace capacity caps.",
            "",
        ),
        InterviewItem(
            "github-actions-reusable-workflows",
            "What are reusable workflows and composite actions in GitHub Actions?",
            "DRY CI/CD — share pipeline logic across repositories.",
            "",
        ),
    ],
}

for _items in MARKET_ITEMS.values():
    for item in _items:
        if not item.code.strip():
            item.code = "// See detailed code example below"

MARKET_DETAILED: dict[str, dict] = {
    "docker-run-exec-logs": {
        "explanation": (
            "**docker run** creates and starts a container from an image. Key flags: `-d` (detached), `-p` "
            "(port map), `--name`, `-e` (env vars), `-v` (volume), `--rm` (remove on exit), `--network`. "
            "**docker exec** runs a command in a **running** container — debugging shells (`exec -it bash`), "
            "one-off migrations, health checks. **docker logs** streams stdout/stderr; `-f` follow, `--tail`, "
            "`--since`. Interview tip: `run` vs `start` (existing container), and never store data in "
            "ephemeral container filesystem without volumes."
        ),
        "code": """# Run API container — map port, env, network, auto-remove
docker run -d --name order-api \\
  -p 8080:8080 \\
  -e ASPNETCORE_ENVIRONMENT=Development \\
  -e ConnectionStrings__Sql=\"Server=host.docker.internal;...\" \\
  --network app-net \\
  myregistry.azurecr.io/order-api:1.2.0

# Exec into running container for troubleshooting
docker exec -it order-api /bin/sh
docker exec order-api dotnet --info

# View logs — follow tail, last 100 lines
docker logs -f --tail 100 order-api
docker logs --since 10m order-api""",
        "language": "bash",
        "key_points": [
            "docker run = create + start; docker start = existing container",
            "exec requires running container — debug without rebuilding",
            "logs captures stdout/stderr — use structured logging to stdout",
            "-p host:container port mapping for local access",
            "Always use named volumes for persistent data",
        ],
    },
    "docker-buildx": {
        "explanation": (
            "**Docker Buildx** is the extended build toolkit supporting **multi-platform images** (amd64 + arm64), "
            "**build cache** export/import, **BuildKit** features (secrets, SSH mounts, cache mounts), and "
            "remote builders. Essential for Apple Silicon devs building images that run on Linux amd64 in AKS. "
            "`docker buildx build --platform linux/amd64,linux/arm64 --push`. Use **GitHub Actions buildx** "
            "with QEMU for CI multi-arch. Compare to plain `docker build` which is single-platform by default."
        ),
        "code": """# Enable buildx builder
docker buildx create --name multiarch --use
docker buildx inspect --bootstrap

# Multi-platform build and push to ACR
docker buildx build \\
  --platform linux/amd64,linux/arm64 \\
  -t myregistry.azurecr.io/order-api:1.3.0 \\
  --push .

# Cache from/to registry — faster CI builds
docker buildx build \\
  --cache-from type=registry,ref=myregistry.azurecr.io/order-api:buildcache \\
  --cache-to type=registry,ref=myregistry.azurecr.io/order-api:buildcache,mode=max \\
  -t myregistry.azurecr.io/order-api:1.3.0 --push .""",
        "language": "bash",
        "key_points": [
            "Buildx enables multi-arch images (amd64 + arm64)",
            "BuildKit cache mounts speed up dotnet restore layers",
            "Push manifest list — one tag, multiple architectures",
            "Use in CI with docker/setup-buildx-action",
            "Secrets: --secret id=nuget,src=nuget.config for private feeds",
        ],
    },
    "docker-registry": {
        "explanation": (
            "A **container registry** stores and distributes **Docker/OCI images** by **tag** and immutable "
            "**digest** (sha256). **Docker Hub** is public default; **Azure Container Registry (ACR)**, "
            "**Amazon ECR**, **Google GCR** are private cloud registries. Workflow: `docker tag`, `docker push`, "
            "K8s pulls via `imagePullSecrets` or managed identity (AKS+ACR). Best practices: **immutable tags** "
            "(git SHA), scan on push, **retention policies**, avoid `:latest` in production manifests."
        ),
        "code": """# Tag and push to ACR
az acr login --name myregistry
docker tag order-api:1.2.0 myregistry.azurecr.io/order-api:1.2.0
docker tag order-api:1.2.0 myregistry.azurecr.io/order-api:$(git rev-parse --short HEAD)
docker push myregistry.azurecr.io/order-api:1.2.0
docker push myregistry.azurecr.io/order-api:$(git rev-parse --short HEAD)

# Pull by digest — immutable reference
docker pull myregistry.azurecr.io/order-api@sha256:abc123...

# K8s deployment references specific tag or digest
# image: myregistry.azurecr.io/order-api:1.2.0""",
        "language": "bash",
        "key_points": [
            "Tag = mutable label; digest = immutable content hash",
            "Prefer private registry (ACR) over Docker Hub for prod",
            "AKS attach-acr enables pull without imagePullSecrets",
            "Never rely on :latest in production deployments",
            "Enable vulnerability scanning on push (Defender/Trivy)",
        ],
    },
    "k8s-namespaces": {
        "explanation": (
            "**Namespaces** partition a single Kubernetes cluster into **virtual clusters** for isolation, "
            "RBAC, resource quotas, and naming scope. Default namespaces: `default`, `kube-system`, "
            "`kube-public`. Common pattern: **dev/staging/prod** namespaces or **team-per-namespace**. "
            "DNS: `service.namespace.svc.cluster.local`. Objects like Services are namespaced; Nodes and "
            "PersistentVolumes are cluster-scoped. Use **ResourceQuota** and **LimitRange** per namespace."
        ),
        "code": """apiVersion: v1
kind: Namespace
metadata:
  name: orders-prod
  labels:
    env: production
    team: orders
---
apiVersion: v1
kind: ResourceQuota
metadata:
  name: orders-quota
  namespace: orders-prod
spec:
  hard:
    requests.cpu: \"20\"
    requests.memory: 40Gi
    pods: \"50\"
---
# Deploy to namespace
# kubectl apply -f deployment.yaml -n orders-prod
# kubectl get pods -n orders-prod""",
        "language": "yaml",
        "key_points": [
            "Namespaces isolate resources within one cluster",
            "Service DNS includes namespace: svc.ns.svc.cluster.local",
            "Combine with RBAC for team/environment isolation",
            "ResourceQuota caps total namespace consumption",
            "Not a security boundary alone — use NetworkPolicy too",
        ],
    },
    "masstransit-basics": {
        "explanation": (
            "**MassTransit** is a .NET **distributed application framework** abstracting message brokers "
            "(RabbitMQ, Azure Service Bus, Amazon SQS, Kafka). Provides **consumers**, **sagas**, **routing slips**, "
            "**retry/redelivery**, **outbox**, and **test harness**. Register in DI; configure transport once. "
            "Interview: compare to raw Service Bus SDK — MassTransit handles serialization, correlation, "
            "middleware (consume filters), and poison message handling. Common in microservices event-driven "
            "architectures on Azure."
        ),
        "code": """// Program.cs — Azure Service Bus transport
builder.Services.AddMassTransit(x =>
{
    x.AddConsumer<OrderPlacedConsumer>();
    x.AddSagaStateMachine<PlaceOrderSaga, PlaceOrderSagaState>()
        .EntityFrameworkRepository(r => r.AddDbContext<AppDbContext>());

    x.UsingAzureServiceBus((ctx, cfg) =>
    {
        cfg.Host(builder.Configuration[\"ServiceBus:ConnectionString\"]);
        cfg.ConfigureEndpoints(ctx);
    });
});

public class OrderPlacedConsumer(IEmailSender email) : IConsumer<OrderPlacedEvent>
{
    public async Task Consume(ConsumeContext<OrderPlacedEvent> ctx)
        => await email.SendOrderConfirmationAsync(ctx.Message.OrderId);
}""",
        "language": "csharp",
        "key_points": [
            "MassTransit abstracts broker wiring and message patterns",
            "Built-in retry, saga, outbox, and consumer middleware",
            "ConfigureEndpoints auto-wires queues/topics from consumers",
            "Test with in-memory or test harness — no broker needed",
            "Prefer over raw SDK for consistent microservice messaging",
        ],
    },
    "dependabot": {
        "explanation": (
            "**Dependabot** (GitHub native) opens **automated PRs** when dependencies have security advisories "
            "or version updates. Supports **NuGet**, **npm**, **Docker**, **GitHub Actions**, **pip**, etc. "
            "Configure via `.github/dependabot.yml` — schedule, directories, ignore rules, grouping. "
            "Part of **supply chain security** alongside Trivy and SBOM. Best practice: enable for security "
            "updates immediately; batch minor version bumps weekly; require CI pass before merge."
        ),
        "code": """# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: \"nuget\"
    directory: \"/\"
    schedule:
      interval: \"weekly\"
    groups:
      dotnet-minor:
        patterns: [\"*\"]
        update-types: [\"minor\", \"patch\"]

  - package-ecosystem: \"docker\"
    directory: \"/\"
    schedule:
      interval: \"weekly\"

  - package-ecosystem: \"github-actions\"
    directory: \"/\"
    schedule:
      interval: \"weekly\"

# Dependabot opens PRs like: \"Bump Newtonsoft.Json from 13.0.1 to 13.0.3\"""",
        "language": "yaml",
        "key_points": [
            "Automated dependency update PRs on GitHub",
            "Configure ecosystems: nuget, docker, github-actions",
            "Group minor/patch updates to reduce PR noise",
            "Security alerts should auto-trigger PRs",
            "Combine with CI tests and branch protection",
        ],
    },
    "packer-basics": {
        "explanation": (
            "**HashiCorp Packer** builds **machine images** (AMIs, Azure VM images, Docker images) from a "
            "single template — **immutable infrastructure** for VMs that aren't containerized. Template uses "
            "builders (azure-arm, amazon-ebs) + provisioners (shell, ansible). Output: golden image with agents, "
            "hardening, and baseline config baked in. Use when legacy workloads run on VMs but you want "
            "repeatable builds. Complements Terraform (provisions resources from images)."
        ),
        "code": """# packer.pkr.hcl — Azure managed image
packer {
  required_plugins {
    azure = { source = \"github.com/hashicorp/azure\" version = \">= 2.0.0\" }
  }
}

source \"azure-arm\" \"ubuntu\" {
  os_type         = \"Linux\"
  image_publisher = \"Canonical\"
  image_offer     = \"0001-com-ubuntu-server-jammy\"
  image_sku       = \"22_04-lts\"
  location        = \"East US\"
  vm_size         = \"Standard_D2s_v3\"
}

build {
  sources = [\"source.azure-arm.ubuntu\"]
  provisioner \"shell\" {
    inline = [
      \"sudo apt-get update\",
      \"sudo apt-get install -y docker.io dotnet-runtime-8.0\",
      \"sudo systemctl enable docker\"
    ]
  }
}""",
        "language": "hcl",
        "key_points": [
            "Packer builds immutable VM/machine images from templates",
            "Builders target cloud; provisioners configure software",
            "Golden images reduce config drift vs manual VM setup",
            "Pair with Terraform to launch VMs from Packer images",
            "Different from Docker — full OS images for VM workloads",
        ],
    },
    "k8s-statefulset": {
        "explanation": (
            "**StatefulSet** manages stateful applications needing **stable network identity** and **persistent "
            "storage**. Pods get predictable names (`web-0`, `web-1`), ordered deploy/scale, and **PersistentVolumeClaims** "
            "via `volumeClaimTemplates`. Use for databases, Kafka, Elasticsearch — not stateless APIs (use Deployment). "
            "**Headless Service** (`clusterIP: None`) provides stable DNS per pod. Deleting StatefulSet does not "
            "auto-delete PVCs — data retention by design."
        ),
        "code": """apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis
spec:
  serviceName: redis-headless
  replicas: 3
  selector:
    matchLabels: { app: redis }
  template:
    metadata:
      labels: { app: redis }
    spec:
      containers:
      - name: redis
        image: redis:7
        ports: [{ containerPort: 6379 }]
        volumeMounts:
        - name: data
          mountPath: /data
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [\"ReadWriteOnce\"]
      resources:
        requests:
          storage: 10Gi
---
apiVersion: v1
kind: Service
metadata:
  name: redis-headless
spec:
  clusterIP: None
  selector: { app: redis }
  ports: [{ port: 6379 }]""",
        "language": "yaml",
        "key_points": [
            "Stable pod names and ordered rollout — web-0, web-1",
            "volumeClaimTemplates provision PVC per pod",
            "Headless Service for stable per-pod DNS",
            "Use for databases/message brokers — not stateless APIs",
            "PVCs persist after StatefulSet deletion",
        ],
    },
    "k8s-daemonset": {
        "explanation": (
            "A **DaemonSet** ensures **one pod runs on every (or selected) node** — automatically schedules "
            "new pods when nodes join. Use cases: **log collectors** (Fluentd, Filebeat), **node monitoring** "
            "(Prometheus node-exporter), **CNI/network plugins**, **storage agents**. Unlike Deployment (N replicas "
            "cluster-wide), DaemonSet is **per-node**. Can target node subsets via `nodeSelector` or tolerations "
            "for tainted nodes."
        ),
        "code": """apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluent-bit
  namespace: logging
spec:
  selector:
    matchLabels: { app: fluent-bit }
  template:
    metadata:
      labels: { app: fluent-bit }
    spec:
      tolerations:
      - key: node-role.kubernetes.io/control-plane
        effect: NoSchedule
      containers:
      - name: fluent-bit
        image: fluent/fluent-bit:2.2
        volumeMounts:
        - name: varlog
          mountPath: /var/log
          readOnly: true
        - name: containers
          mountPath: /var/lib/docker/containers
          readOnly: true
      volumes:
      - name: varlog
        hostPath: { path: /var/log }
      - name: containers
        hostPath: { path: /var/lib/docker/containers }""",
        "language": "yaml",
        "key_points": [
            "One pod per node — auto-schedules on new nodes",
            "Log shippers and monitoring agents are classic use cases",
            "Use nodeSelector/tolerations for specific node pools",
            "Different from Deployment — per-node not N replicas total",
            "DaemonSet pods often need hostPath or privileged access",
        ],
    },
    "k8s-jobs-cronjobs": {
        "explanation": (
            "**Jobs** run pods to **completion** (batch, migrations, one-off tasks) — `restartPolicy: Never` "
            "or `OnFailure`. **CronJobs** schedule Jobs on cron syntax. Use for DB migrations, report "
            "generation, cleanup tasks. Contrast with Deployments (long-running). Set **`backoffLimit`**, "
            "**`activeDeadlineSeconds`**, and **`ttlSecondsAfterFinished`** for cleanup. For recurring .NET "
            "tasks, consider Hangfire/Azure Functions; CronJob when K8s-native batch is preferred."
        ),
        "code": """apiVersion: batch/v1
kind: CronJob
metadata:
  name: nightly-report
spec:
  schedule: \"0 2 * * *\"
  jobTemplate:
    spec:
      backoffLimit: 3
      ttlSecondsAfterFinished: 86400
      template:
        spec:
          restartPolicy: OnFailure
          containers:
          - name: report
            image: myregistry.azurecr.io/report-job:1.0
            env:
            - name: ConnectionStrings__Sql
              valueFrom:
                secretKeyRef:
                  name: db-secrets
                  key: sql
            command: [\"dotnet\", \"ReportJob.dll\"]
---
# One-off migration Job
# kubectl create job migrate-v2 --from=cronjob/nightly-report""",
        "language": "yaml",
        "key_points": [
            "Job = run to completion; CronJob = scheduled Job",
            "Use for batch, migrations, reports — not long-running services",
            "Set backoffLimit and activeDeadlineSeconds",
            "ttlSecondsAfterFinished cleans completed Job pods",
            "restartPolicy Never or OnFailure — not Always",
        ],
    },
    "k8s-network-policy": {
        "explanation": (
            "**NetworkPolicy** defines **pod-level firewall rules** for ingress/egress — requires CNI support "
            "(Calico, Cilium, Azure NPM). Default K8s allows all pod-to-pod traffic; NetworkPolicy **denies by "
            "default** when applied (whitelist model depends on CNI). Specify `podSelector`, `namespaceSelector`, "
            "`ipBlock`, ports, protocols. Zero-trust microsegmentation: only order-api can talk to SQL on 1433. "
            "Test policies in staging — misconfiguration causes silent failures."
        ),
        "code": """apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: order-api-ingress
  namespace: orders-prod
spec:
  podSelector:
    matchLabels: { app: order-api }
  policyTypes: [Ingress, Egress]
  ingress:
  - from:
    - namespaceSelector:
        matchLabels: { name: ingress-nginx }
    - podSelector:
        matchLabels: { app: web-bff }
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels: { app: sql-proxy }
    ports:
    - protocol: TCP
      port: 1433
  - to:  # allow DNS
    - namespaceSelector: {}
      podSelector:
        matchLabels: { k8s-app: kube-dns }
    ports:
    - protocol: UDP
      port: 53""",
        "language": "yaml",
        "key_points": [
            "NetworkPolicy = pod firewall — requires CNI support",
            "Default allow-all unless policies restrict traffic",
            "Combine namespace + pod selectors for microsegmentation",
            "Always allow DNS egress or pods break",
            "Azure AKS: enable Azure Network Policy or Calico",
        ],
    },
    "github-actions-matrix": {
        "explanation": (
            "**Matrix strategy** runs the same job across **multiple configurations** — OS, .NET version, "
            "Node version, project paths. Generates parallel jobs from `matrix:` keys. Use `include` for "
            "extra combos, `exclude` to skip. Fail-fast controls whether one failure cancels others. "
            "Essential for libraries supporting multiple runtimes. Combine with **caching** per matrix leg."
        ),
        "code": """name: CI
on: [push, pull_request]
jobs:
  test:
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest]
        dotnet: [\"8.0.x\", \"9.0.x\"]
        include:
          - os: ubuntu-latest
            dotnet: 8.0.x
            coverage: true
        exclude:
          - os: windows-latest
            dotnet: 9.0.x
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: ${{ matrix.dotnet }}
      - run: dotnet test --configuration Release
      - if: matrix.coverage
        run: dotnet test --collect:\"XPlat Code Coverage\"""",
        "language": "yaml",
        "key_points": [
            "Matrix runs job across OS/runtime/config combinations",
            "include adds combos; exclude removes them",
            "fail-fast: false keeps other legs running on failure",
            "Reference matrix vars with ${{ matrix.key }}",
            "Parallel matrix legs speed up multi-platform CI",
        ],
    },
    "trivy-scanning": {
        "explanation": (
            "**Trivy** (Aqua Security) scans **container images**, **filesystems**, **IaC**, and **Git repos** "
            "for **CVEs**, misconfigurations, and **secrets**. Open-source; integrates with CI, ACR, and "
            "admission controllers. Severity: CRITICAL/HIGH should block deploy. Compare to Defender for Cloud, "
            "Snyk. Run in pipeline after `docker build`, before push to prod. **`trivy image --severity "
            "CRITICAL,HIGH --exit-code 1`** fails CI on findings."
        ),
        "code": """# Scan local image before push
trivy image --severity CRITICAL,HIGH myregistry.azurecr.io/order-api:1.2.0

# Fail CI on critical/high CVEs
trivy image --exit-code 1 --ignore-unfixed \\
  --severity CRITICAL,HIGH \\
  myregistry.azurecr.io/order-api:${{ github.sha }}

# Scan Dockerfile/IaC for misconfigs
trivy config .
trivy fs --scanners secret,vuln .

# GitHub Action
- uses: aquasecurity/trivy-action@master
  with:
    image-ref: myregistry.azurecr.io/order-api:${{ github.sha }}
    format: sarif
    output: trivy-results.sarif
    severity: CRITICAL,HIGH""",
        "language": "bash",
        "key_points": [
            "Trivy scans images, filesystems, IaC, and secrets",
            "Use --exit-code 1 in CI to block vulnerable images",
            "Scan before prod deploy — shift-left security",
            "SARIF output integrates with GitHub Security tab",
            "Combine with Dependabot for defense in depth",
        ],
    },
    "helm-values-templates": {
        "explanation": (
            "**Helm** packages K8s manifests as **charts** with **templates** (Go templating) and **values.yaml** "
            "defaults. `_helpers.tpl` defines reusable named templates (`define`/`include`). At install/upgrade, "
            "Helm renders templates with merged values (`-f prod.yaml`, `--set`). **`{{ .Values.replicaCount }}`**, "
            "**`{{ include \"chart.fullname\" . }}`**, **`{{- if .Values.ingress.enabled }}`**. Release history "
            "enables rollback. Deep dive beyond basic chart install: parameterize every env-specific field."
        ),
        "code": """# values.yaml
replicaCount: 3
image:
  repository: myregistry.azurecr.io/order-api
  tag: \"1.2.0\"
ingress:
  enabled: true
  host: api.example.com

# templates/_helpers.tpl
{{- define \"order-api.fullname\" -}}
{{- printf \"%s-%s\" .Release.Name .Chart.Name | trunc 63 | trimSuffix \"-\" }}
{{- end }}

# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include \"order-api.fullname\" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
      - name: api
        image: \"{{ .Values.image.repository }}:{{ .Values.image.tag }}\"

# helm upgrade --install order-api ./chart -f values-prod.yaml""",
        "language": "yaml",
        "key_points": [
            "values.yaml = defaults; -f overrides per environment",
            "_helpers.tpl defines reusable template snippets",
            "Go templating: .Values, .Release, .Chart context",
            "helm upgrade --install is declarative deploy",
            "Keep secrets out of values — use External Secrets/CSI",
        ],
    },
    "k8s-rbac": {
        "explanation": (
            "**RBAC** controls who/what can perform actions on K8s resources. **Role** (namespace-scoped) vs "
            "**ClusterRole** (cluster-wide). **RoleBinding/ClusterRoleBinding** attach subjects (User, Group, "
            "**ServiceAccount**) to roles. Least privilege: CI service account gets deploy Role in one namespace; "
            "app pods get minimal permissions. **`kubectl auth can-i create pods -n prod --as system:serviceaccount:...`**. "
            "Avoid cluster-admin for apps; use dedicated SAs per deployment."
        ),
        "code": """apiVersion: v1
kind: ServiceAccount
metadata:
  name: order-api
  namespace: orders-prod
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: order-api-reader
  namespace: orders-prod
rules:
- apiGroups: [\"\"]
  resources: [\"configmaps\"]
  verbs: [\"get\", \"list\"]
  resourceNames: [\"order-api-config\"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: order-api-binding
  namespace: orders-prod
subjects:
- kind: ServiceAccount
  name: order-api
  namespace: orders-prod
roleRef:
  kind: Role
  name: order-api-reader
  apiGroup: rbac.authorization.k8s.io
---
# Pod spec: serviceAccountName: order-api""",
        "language": "yaml",
        "key_points": [
            "Role/ClusterRole define permissions; Binding assigns to subjects",
            "ServiceAccounts are identity for pods and CI/CD",
            "Least privilege — resourceNames narrows access",
            "auth can-i verifies effective permissions",
            "Separate CI deploy SA from runtime app SA",
        ],
    },
    "argocd-gitops": {
        "explanation": (
            "**Argo CD** implements **GitOps** — **Git repository is source of truth** for desired cluster state. "
            "Argo CD **syncs** K8s manifests (plain YAML, Helm, Kustomize) to cluster, detects **drift**, "
            "supports rollback, and provides UI. Push to Git → Argo detects → applies. Benefits: auditable "
            "changes, reproducible deploys, no kubectl from CI. **App of Apps** pattern for multi-service. "
            "Compare to Flux CD (controller-based, no UI by default)."
        ),
        "code": """# argocd Application manifest — points to Git repo path
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: order-api
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/k8s-manifests.git
    targetRevision: main
    path: apps/order-api/overlays/prod
  destination:
    server: https://kubernetes.default.svc
    namespace: orders-prod
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true

# Git change → webhook/poll → Argo sync → cluster updated
# Rollback: argocd app rollback order-api <revision>""",
        "language": "yaml",
        "key_points": [
            "GitOps — Git is single source of truth for deployments",
            "Argo CD syncs Helm/Kustomize/plain YAML to cluster",
            "selfHeal reverts manual kubectl drift",
            "Automated sync on Git push with prune for deletions",
            "Audit trail via Git history + Argo sync logs",
        ],
    },
    "istio-basics": {
        "explanation": (
            "**Istio** is a **service mesh** — sidecar proxy (Envoy) injected alongside each pod handles **L7 "
            "traffic management**, **mTLS**, **observability** (metrics, traces), and **policy** without app "
            "code changes. Control plane (istiod) configures data plane proxies. Features: **VirtualService** "
            "(routing, retries, timeouts), **DestinationRule** (load balancing, circuit breaking), **PeerAuthentication** "
            "(mTLS). Overhead: sidecar resources and complexity — evaluate need vs YARP/APIM."
        ),
        "code": """# Enable sidecar injection on namespace
apiVersion: v1
kind: Namespace
metadata:
  name: orders-prod
  labels:
    istio-injection: enabled
---
# Canary routing — 90% v1, 10% v2
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: order-api
spec:
  hosts: [order-api]
  http:
  - route:
    - destination:
        host: order-api
        subset: v1
      weight: 90
    - destination:
        host: order-api
        subset: v2
      weight: 10
---
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: order-api
spec:
  host: order-api
  subsets:
  - name: v1
    labels: { version: v1 }
  - name: v2
    labels: { version: v2 }""",
        "language": "yaml",
        "key_points": [
            "Service mesh adds sidecar proxy for L7 traffic control",
            "mTLS between services without app code changes",
            "VirtualService handles routing, retries, canary weights",
            "Observability: automatic metrics and distributed tracing",
            "Tradeoff: complexity and sidecar resource overhead",
        ],
    },
    "flux-cd": {
        "explanation": (
            "**Flux CD** is a **GitOps toolkit** — Kubernetes controllers that **reconcile cluster state** from "
            "Git repositories. Components: **Source Controller** (fetch Git/OCI/Helm repos), **Kustomize "
            "Controller**, **Helm Controller**, **Notification Controller**. **`GitRepository`** + **`Kustomization`** "
            "CRDs define what to sync. CNCF graduated; often chosen for **multi-tenant** and **modular** setups. "
            "Argo CD: monolithic app with UI; Flux: composable controllers, optional UI (Weave GitOps)."
        ),
        "code": """apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: order-api
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/org/k8s-manifests
  ref:
    branch: main
---
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: order-api-prod
  namespace: flux-system
spec:
  interval: 5m
  sourceRef:
    kind: GitRepository
    name: order-api
  path: ./apps/order-api/overlays/prod
  prune: true
  targetNamespace: orders-prod
  healthChecks:
  - apiVersion: apps/v1
    kind: Deployment
    name: order-api
    namespace: orders-prod""",
        "language": "yaml",
        "key_points": [
            "Flux reconciles cluster from Git via controllers",
            "GitRepository + Kustomization/HelmRelease CRDs",
            "Modular toolkit vs Argo CD all-in-one with UI",
            "prune: true removes resources deleted from Git",
            "Part of CNCF — popular for platform engineering teams",
        ],
    },
    "k8s-resource-limits": {
        "explanation": (
            "**requests** = guaranteed resources for scheduling; **limits** = max CPU/memory a container can use. "
            "Omitting requests causes poor scheduling; omitting limits allows noisy neighbor. **LimitRange** "
            "sets defaults per namespace; **ResourceQuota** caps total namespace usage. CPU: throttled at limit; "
            "memory: **OOMKilled** at limit. .NET apps: set requests based on load test; leave headroom for GC. "
            "Vertical Pod Autoscaler recommends values."
        ),
        "code": """apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
  namespace: orders-prod
spec:
  limits:
  - default:
      cpu: \"500m\"
      memory: 512Mi
    defaultRequest:
      cpu: \"100m\"
      memory: 128Mi
    type: Container
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-api
spec:
  template:
    spec:
      containers:
      - name: api
        image: myregistry.azurecr.io/order-api:1.2.0
        resources:
          requests:
            cpu: 250m
            memory: 256Mi
          limits:
            cpu: \"1\"
            memory: 512Mi""",
        "language": "yaml",
        "key_points": [
            "requests = scheduling guarantee; limits = hard cap",
            "Memory over limit → OOMKilled; CPU → throttled",
            "ResourceQuota caps total namespace CPU/memory/pods",
            "LimitRange sets defaults for containers without resources",
            "Load-test to set realistic requests — avoid guessing",
        ],
    },
    "github-actions-reusable-workflows": {
        "explanation": (
            "**Reusable workflows** (`workflow_call`) let repos invoke shared CI/CD pipelines — DRY across "
            "microservice repos. **Composite actions** bundle steps (`action.yml`). Caller passes `secrets: inherit` "
            "or explicit secrets/inputs. Organization `.github` repo hosts `dotnet-ci.yml` called by all APIs. "
            "Contrast with copy-paste YAML and **templates**. Version reusable workflows with tags (`@v2`) for "
            "stability."
        ),
        "code": """# .github/workflows/dotnet-ci-reusable.yml (called workflow)
on:
  workflow_call:
    inputs:
      dotnet-version:
        required: false
        type: string
        default: \"8.0.x\"
    secrets:
      NUGET_TOKEN:
        required: true
jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: ${{ inputs.dotnet-version }}
      - run: dotnet restore
        env:
          NUGET_AUTH_TOKEN: ${{ secrets.NUGET_TOKEN }}
      - run: dotnet test --configuration Release

# Caller repo — .github/workflows/ci.yml
jobs:
  ci:
    uses: org/platform/.github/workflows/dotnet-ci-reusable.yml@v2
    secrets: inherit""",
        "language": "yaml",
        "key_points": [
            "workflow_call enables reusable CI/CD across repos",
            "Composite actions bundle steps; reusable workflows bundle jobs",
            "Pin reusable workflows to tags (@v2) not floating @main",
            "secrets: inherit passes org/repo secrets to called workflow",
            "Platform team maintains one pipeline — services call it",
        ],
    },
}
