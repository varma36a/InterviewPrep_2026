"""CS Fundamentals detailed content — items 21–40."""

CS_DETAILED_PART2: dict[str, dict] = {
    "cs-big-o": {
        "explanation": (
            "**Big O** describes upper bound growth rate as input size n increases; ignores constants.\n\n"
            "**Common:** O(1) hash lookup, O(log n) binary search, O(n) linear scan, O(n log n) efficient sort, "
            "O(n²) nested loops, O(2^n) subsets, O(n!) permutations.\n\n"
            "Interview: state time AND space complexity; mention best/average/worst when relevant."
        ),
        "code": """Complexity cheat sheet:

O(1)       hash table get, array index
O(log n)   binary search, balanced BST ops
O(n)       single loop, hash map build
O(n log n) merge sort, heap sort, LINQ OrderBy
O(n²)      nested loops, bubble sort
O(2^n)     recursive subsets
O(n!)      permutations

Space:
  O(1)  two pointers, in-place
  O(n)  hash map, recursion stack depth n

Amortized:
  List.Add amortized O(1) despite occasional resize O(n)""",
        "key_points": ["Drop constants and lower terms", "State space complexity too", "Amortized for dynamic arrays"],
    },
    "cs-hash-table-internals": {
        "explanation": (
            "**Hash table** maps keys to values via hash function → bucket index.\n\n"
            "**Collision resolution:** **Chaining** (linked list per bucket) or **open addressing** (probe next slot).\n\n"
            "**Load factor:** entries/capacity; rehash when exceeds threshold (~0.75). .NET `Dictionary` uses chaining + prime bucket sizes."
        ),
        "code": """hash(key) → bucket index

Chaining:
  bucket[3] → (k1,v1) → (k9,v9) → null

Open addressing (linear probing):
  if bucket occupied, try bucket+1, +2...

.NET Dictionary<K,V>:
  - GetHashCode() + Equals() on keys
  - Resize when load factor exceeded
  - O(1) average, O(n) worst (all collisions)

Distributed:
  Consistent hashing for cache sharding across nodes""",
        "language": "csharp",
        "key_points": ["Hash → bucket", "Chaining or probing", "Rehash on load factor", "GetHashCode + Equals required"],
    },
    "cs-sorting-comparison": {
        "explanation": (
            "**QuickSort:** O(n log n) average, O(n²) worst (bad pivot); in-place; not stable.\n\n"
            "**MergeSort:** O(n log n) always; O(n) extra space; stable.\n\n"
            "**HeapSort:** O(n log n); in-place; not stable.\n\n"
            "**.NET `Array.Sort`:** Introsort (QuickSort + HeapSort fallback). **`OrderBy`:** stable merge sort."
        ),
        "code": """Algorithm    | Best      | Avg       | Worst     | Space | Stable
-------------|-----------|-----------|-----------|-------|-------
QuickSort    | O(n log n)| O(n log n)| O(n²)     | O(log n)| No
MergeSort    | O(n log n)| O(n log n)| O(n log n)| O(n)  | Yes
HeapSort     | O(n log n)| O(n log n)| O(n log n)| O(1)  | No
Counting Sort| O(n+k)    | O(n+k)    | O(n+k)    | O(k)  | Yes*
(* integers in small range)

When n < 10: insertion sort (fast for tiny)
TimSort (Python/Java): merge + insertion hybrid""",
        "key_points": ["QuickSort in-place average fast", "MergeSort stable O(n log n)", "Introsort in .NET", "Counting sort for integers"],
    },
    "cs-mutex-semaphore": {
        "explanation": (
            "**Mutex (mutual exclusion):** Only one thread holds lock at a time. `lock()` in C#.\n\n"
            "**Semaphore:** Counting lock — allows N concurrent threads. `SemaphoreSlim(3)` = max 3 at once.\n\n"
            "**Monitor:** C# built-in — `lock`, `Wait`, `Pulse` for condition signaling."
        ),
        "code": """// Mutex — one at a time
private readonly object _gate = new();
lock (_gate)
{
    // critical section — only one thread
}

// Semaphore — limit concurrency (e.g. DB pool)
var sem = new SemaphoreSlim(10); // max 10 concurrent
await sem.WaitAsync();
try { await QueryDatabase(); }
finally { sem.Release(); }

// ReaderWriterLockSlim — many readers OR one writer
_rw.EnterReadLock();  // multiple OK
_rw.EnterWriteLock(); // exclusive""",
        "language": "csharp",
        "key_points": ["lock = mutex", "SemaphoreSlim limits N concurrent", "ReaderWriterLockSlim for read-heavy"],
    },
    "cs-race-condition": {
        "explanation": (
            "**Race condition:** Outcome depends on non-deterministic thread interleaving.\n\n"
            "Classic: `count++` is read-modify-write — not atomic across threads.\n\n"
            "**Prevention:** Locks, `Interlocked` atomic ops, immutable data, thread-safe collections (`ConcurrentDictionary`), "
            "avoid shared mutable state (prefer message passing)."
        ),
        "code": """// Race: two threads both read count=5, write 6
int count = 0;
Interlocked.Increment(ref count); // atomic — safe

// Thread-safe collection
var dict = new ConcurrentDictionary<string, int>();
dict.AddOrUpdate("key", 1, (_, v) => v + 1);

// Immutable — no races
public record Order(int Id, decimal Total);

// async pitfall — not thread-safe:
static int _counter;
async Task Bad() { _counter++; await Task.Delay(1); }""",
        "language": "csharp",
        "key_points": ["read-modify-write not atomic", "Interlocked for counters", "Concurrent collections", "Prefer immutability"],
    },
    "cs-thread-pool": {
        "explanation": (
            "**Thread pool** maintains reusable worker threads to avoid create/destroy overhead.\n\n"
            "**.NET ThreadPool:** `Task.Run`, ASP.NET request handling, `async` continuations use pool threads.\n\n"
            "**Starvation:** All threads blocked → queue grows → delays. **Don't block pool threads** (`Task.Result`, sync-over-async)."
        ),
        "code": """// Queues work to thread pool
await Task.Run(() => CpuHeavyWork());

// ASP.NET Core: each request on pool thread
// async I/O releases thread during await

ThreadPool.SetMinThreads(100, 100); // rarely needed

Anti-pattern (blocks pool thread):
  public IActionResult Get()
  {
      var data = _service.GetDataAsync().Result; // BAD
      return Ok(data);
  }

Correct:
  public async Task<IActionResult> Get()
  {
      var data = await _service.GetDataAsync();
      return Ok(data);
  }""",
        "language": "csharp",
        "key_points": ["Task.Run uses pool", "Don't block with .Result", "async frees thread during I/O", "ConfigureAwait in libraries"],
    },
    "cs-encryption-types": {
        "explanation": (
            "**Symmetric (AES):** Same key encrypt/decrypt; fast; key distribution problem. Used for bulk data encryption.\n\n"
            "**Asymmetric (RSA, ECDH):** Public/private key pair; public encrypts, private decrypts; slow; used for key exchange and signatures.\n\n"
            "**HTTPS:** Asymmetric handshake to agree symmetric session key, then AES for data."
        ),
        "code": """HTTPS combines both:

1. Asymmetric (TLS cert RSA/EC):
   Client encrypts pre-master secret with server's public key
   Server decrypts with private key

2. Symmetric (AES-256-GCM):
   Bulk HTTP data encrypted with shared session key

Digital signature:
  Hash document → encrypt hash with private key
  Verify with public key (proves authenticity)

Key management:
  Azure Key Vault, rotate keys periodically
  Never hardcode keys in source""",
        "key_points": ["AES for bulk symmetric", "RSA/EC for key exchange", "HTTPS uses both", "Key Vault for secrets"],
    },
    "cs-oauth-flow": {
        "explanation": (
            "**Authorization Code Flow** (most secure for web apps):\n"
            "1. Redirect user to IdP login\n"
            "2. User authenticates → redirect back with **authorization code**\n"
            "3. Backend exchanges code + client_secret for **access token** + **refresh token**\n"
            "4. API calls use `Authorization: Bearer {access_token}`\n\n"
            "**PKCE** required for SPAs/mobile (no client secret). **Never** store tokens in localStorage if XSS risk — use HttpOnly cookies."
        ),
        "code": """Authorization Code Flow:

Browser → GET /authorize?
  client_id=app&redirect_uri=...&scope=openid profile
  &response_type=code&state=xyz&code_challenge=...

User logs in at IdP (Azure AD, Auth0)

Redirect → https://app/callback?code=AUTH_CODE&state=xyz

Backend POST /token:
  grant_type=authorization_code
  code=AUTH_CODE
  client_id + client_secret
  redirect_uri

Response:
  { access_token, refresh_token, expires_in, id_token }

API: Authorization: Bearer eyJhbG...""",
        "key_points": ["Code exchanged server-side", "PKCE for public clients", "Refresh token for renewal", "HttpOnly cookies vs XSS"],
    },
    "cs-jwt-structure": {
        "explanation": (
            "**JWT** = Header.Payload.Signature (Base64url encoded).\n\n"
            "**Header:** alg (HS256, RS256), typ JWT.\n"
            "**Payload:** claims (sub, iss, aud, exp, roles).\n"
            "**Signature:** HMAC or RSA sign — tampering invalidates token.\n\n"
            "**Stateless auth:** API validates signature + exp without DB lookup (unless revocation list needed)."
        ),
        "code": """eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0In0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
 └─ header ─────────┘ └─ payload ────┘ └─ signature ─────────────────────┘

Validate in ASP.NET Core:
  builder.Services.AddAuthentication(JwtBearerDefaults...)
    .AddJwtBearer(o => {
      o.TokenValidationParameters = new() {
        ValidateIssuer = true,
        ValidateAudience = true,
        ValidateLifetime = true,
        ValidateIssuerSigningKey = true,
      };
    });

Never put passwords in payload — it's Base64, not encrypted!""",
        "language": "csharp",
        "key_points": ["Three parts header.payload.sig", "Validate iss/aud/exp", "JWT ≠ encrypted", "Short expiry + refresh"],
    },
    "cs-owasp-top": {
        "explanation": (
            "**SQL Injection:** Attacker injects SQL via input. **Prevent:** parameterized queries / EF Core (never string concat).\n\n"
            "**XSS (Cross-Site Scripting):** Inject script into page. **Prevent:** encode output, CSP header, sanitize HTML.\n\n"
            "**CSRF:** Forged request from victim's browser. **Prevent:** anti-forgery tokens, SameSite cookies, check Origin header."
        ),
        "code": """// SQL Injection — NEVER:
var sql = $"SELECT * FROM Users WHERE Email = '{email}'";

// Safe — parameterized:
await cmd.ExecuteAsync("SELECT * FROM Users WHERE Email = @email",
  new { email });

// XSS — encode in Razor/Angular:
@Html.Encode(userInput)  // or {{ userInput }} auto-escape

// CSRF — ASP.NET Core:
[ValidateAntiForgeryToken]
public IActionResult Transfer(TransferDto dto) { ... }

// Cookie flags:
Set-Cookie: session=...; HttpOnly; Secure; SameSite=Strict""",
        "language": "csharp",
        "key_points": ["Parameterized SQL always", "Encode output for XSS", "Anti-forgery for CSRF", "HttpOnly + SameSite cookies"],
    },
    "cs-rest-vs-grpc": {
        "explanation": (
            "**REST:** HTTP verbs + JSON; human-readable; cacheable; wide tooling; verbose payloads.\n\n"
            "**gRPC:** HTTP/2 + Protocol Buffers binary; strongly typed `.proto` contracts; streaming (client, server, bidirectional); "
            "faster; harder to debug in browser (needs gRPC-Web).\n\n"
            "**Choose REST** for public APIs, browsers. **gRPC** for internal microservice communication."
        ),
        "code": """REST:
  GET /api/users/123
  Content-Type: application/json
  { "id": 123, "name": "Alice" }

gRPC (.proto):
  service UserService {
    rpc GetUser (UserRequest) returns (UserResponse);
    rpc ListUsers (stream UserRequest) returns (stream UserResponse);
  }

Performance: Protobuf ~3-10× smaller than JSON
Streaming: gRPC native for live feeds

Public API → REST + OpenAPI
Internal svc-to-svc → gRPC""",
        "key_points": ["REST JSON human-friendly", "gRPC binary + streaming", "gRPC internal, REST external", "Proto contracts"],
    },
    "cs-pub-sub": {
        "explanation": (
            "**Publish-Subscribe:** Publishers send messages to a **topic** without knowing subscribers. "
            "Subscribers receive copies of messages they subscribed to.\n\n"
            "Decouples services; enables fan-out; async processing.\n\n"
            "**Examples:** Kafka topics, Azure Service Bus topics, RabbitMQ exchanges, Redis Pub/Sub."
        ),
        "code": """Order Service ──publish──► topic: order.placed
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
              Email Svc      Inventory Svc   Analytics Svc
              (subscribe)    (subscribe)     (subscribe)

vs Point-to-point queue:
  One message → one consumer

Kafka specifics:
  - Log retained (replay possible)
  - Partitions for ordering per key
  - Consumer groups for scale""",
        "key_points": ["Topic fan-out to subscribers", "Decouples producer/consumer", "Kafka retains log", "At-least-once common"],
    },
    "cs-cap-theorem": {
        "explanation": (
            "In a **distributed system**, during a **network partition** you cannot have both full **Consistency** "
            "and full **Availability** — must choose.\n\n"
            "**CP:** Reject requests or block until partition heals (ZooKeeper, bank ledger).\n\n"
            "**AP:** Serve requests with possibly stale data (DNS, Cassandra tunable, social likes).\n\n"
            "Partition tolerance is mandatory in distributed systems — real choice is C vs A during partition."
        ),
        "code": """Partition scenario:

  [Node A]  X  [Node B]   ← network split

CP choice (Consistency):
  Reject writes on both sides until healed
  → unavailable during partition

AP choice (Availability):
  Both accept writes independently
  → inconsistent until merge (conflict resolution)

Examples:
  CP: etcd, ZooKeeper, SQL primary with sync replica
  AP: DynamoDB (default), Cassandra, CouchDB

BASE (AP systems):
  Basically Available, Soft state, Eventual consistency""",
        "key_points": ["Partition forces trade-off", "CP vs AP examples", "BASE complements ACID", "Pick per subsystem"],
    },
    "cs-consistent-hashing": {
        "explanation": (
            "Maps keys and servers onto a hash ring. Key assigned to first server clockwise.\n\n"
            "When server added/removed, only **K/n** keys remap (vs nearly all with `hash % N`).\n\n"
            "**Virtual nodes** spread load evenly when few physical servers."
        ),
        "code": """hash % 3 (bad):
  Add 4th server → ~75% keys remap

Consistent hash ring:
       S1
      /  \\
    K     S2
      \\  /
       S3

Add S4 between S2-S3:
  Only keys between S2 and S4 move

Use cases:
  - Memcached client routing
  - Cassandra token assignment
  - CDN origin selection
  - Load balancer sticky routing""",
        "key_points": ["Ring minimizes remapping", "Virtual nodes balance load", "Used in distributed caches"],
    },
    "cs-load-balancing-algos": {
        "explanation": (
            "**Round Robin:** Rotate through servers sequentially — simple; ignores load.\n\n"
            "**Weighted Round Robin:** More traffic to powerful servers.\n\n"
            "**Least Connections:** Route to server with fewest active connections — good for long-lived connections.\n\n"
            "**IP Hash:** Same client IP → same server (session affinity)."
        ),
        "code": """Algorithm          | Best for
-------------------|----------------------------------
Round Robin        | Equal servers, short requests
Weighted RR        | Heterogeneous server capacity
Least Connections  | WebSocket, long polling, DB pools
Random             | Simple, surprisingly effective
IP Hash            | Session stickiness without shared session store
Consistent Hash    | Cache servers (minimize miss on change)

Health checks:
  Passive: observe 5xx rates
  Active:  GET /health every N seconds
  Remove unhealthy from rotation""",
        "key_points": ["Least conn for long requests", "Weighted for mixed hardware", "Health checks required", "Sticky vs stateless"],
    },
    "cs-client-server-p2p": {
        "explanation": (
            "**Client-Server:** Central server provides service; clients request. Easy to manage, single point of failure, "
            "doesn't scale horizontally without infrastructure.\n\n"
            "**Peer-to-Peer:** Each node is client and server (BitTorrent, blockchain). Scales with participants; "
            "harder to coordinate, security/consistency challenges.\n\n"
            "**Hybrid:** CDN edge nodes (peers cache content); Skype historically hybrid."
        ),
        "code": """Client-Server:
  [Client] ──HTTP──► [Server] ──► [Database]
  Pros: centralized control, easier security
  Cons: server bottleneck, SPOF

P2P:
  [Peer A] ◄────────► [Peer B]
     ▲                   ▲
     └───────► [Peer C] ◄┘
  Pros: no central bottleneck, resilient
  Cons: NAT traversal, trust, consistency

Modern web = mostly client-server
  + CDN (edge cache peers)
  + Microservices (many servers)""",
        "key_points": ["Client-server centralized", "P2P scales with nodes", "CDN is hybrid edge cache", "Most enterprise = client-server"],
    },
    "cs-cqrs": {
        "explanation": (
            "**CQRS** separates **Command** (write) model from **Query** (read) model.\n\n"
            "Write side: normalized, business rules, events. Read side: denormalized views optimized for queries.\n\n"
            "Often paired with **Event Sourcing** (store events, rebuild state). Use when read/write patterns diverge heavily — not for CRUD apps."
        ),
        "code": """Traditional:
  Same model + DB for reads and writes

CQRS:
  Command API → Write DB (normalized)
       │
       └── events ──► Projector ──► Read DB (denormalized views)
  Query API  → Read DB only

Example:
  PlaceOrder command → Orders table + OrderPlaced event
  Projector updates: OrderSummaryView, CustomerOrderHistoryView

Benefits:
  - Scale reads independently (replicas, Elasticsearch)
  - Optimized query models

Cost:
  - Eventual consistency on read side
  - More infrastructure complexity""",
        "key_points": ["Separate read/write models", "Event sourcing optional", "Scale reads independently", "Not for simple CRUD"],
    },
    "cs-iaas-paas-saas": {
        "explanation": (
            "**IaaS:** Rent VMs, networks, storage — you manage OS, runtime, app. (Azure VMs, AWS EC2)\n\n"
            "**PaaS:** Platform manages OS/runtime — you deploy code. (Azure App Service, Heroku)\n\n"
            "**SaaS:** Complete application — you configure. (Office 365, Salesforce, Gmail)\n\n"
            "**Shared responsibility:** You manage less as you move up the stack."
        ),
        "code": """Responsibility matrix:

              You manage │ Provider manages
──────────────┼──────────┼──────────────────
IaaS (VM)     │ App, Data│ OS, HW, Network
PaaS (App Svc)│ App, Data│ Runtime, OS, HW
SaaS (M365)   │ Data,Users│ Everything else

Azure examples:
  IaaS: Virtual Machines, Azure Disk
  PaaS: App Service, Azure SQL, Functions
  SaaS: Microsoft 365, Dynamics 365

Choose PaaS for faster deploy + less ops
Choose IaaS for full control / legacy apps""",
        "key_points": ["IaaS most control", "PaaS deploy code only", "SaaS complete product", "Shared responsibility model"],
    },
    "cs-scalability-elasticity": {
        "explanation": (
            "**Scalability:** Ability to handle growing load (more users, data). Horizontal or vertical.\n\n"
            "**Elasticity:** Automatically scale resources up/down based on demand — pay for what you use.\n\n"
            "Cloud enables elasticity: K8s HPA, Azure App Service autoscale, serverless (Functions) scale to zero."
        ),
        "code": """Scalable but not elastic:
  Fixed 10 servers handle growth to 10K users
  (manual provisioning)

Elastic:
  Min 2 → Max 50 instances based on CPU/request count
  Scale out at 70% CPU, scale in at 30%

Kubernetes HPA:
  apiVersion: autoscaling/v2
  kind: HorizontalPodAutoscaler
  spec:
    minReplicas: 2
    maxReplicas: 20
    metrics:
    - type: Resource
      resource:
        name: cpu
        targetAverageUtilization: 70

Serverless: scale 0 → 1000 concurrent invocations automatically""",
        "language": "yaml",
        "key_points": ["Scalability = capacity for growth", "Elasticity = auto scale", "HPA in Kubernetes", "Serverless extreme elasticity"],
    },
    "cs-cicd-pipeline": {
        "explanation": (
            "**CI (Continuous Integration):** Merge code frequently; automated build + test on each commit.\n\n"
            "**CD (Continuous Delivery/Deployment):** Automated deploy to staging/production. "
            "Delivery = manual gate; Deployment = fully automatic.\n\n"
            "**Stages:** Source → Build → Unit Test → Integration Test → Security Scan → Deploy Staging → Deploy Prod."
        ),
        "code": """Typical pipeline (GitHub Actions / Azure DevOps):

  git push
     │
     ▼
  Build (dotnet build)
     │
     ▼
  Unit tests (dotnet test)
     │
     ▼
  Integration tests (Testcontainers)
     │
     ▼
  Docker build + push to ACR
     │
     ▼
  Deploy staging (Helm → AKS)
     │
     ▼
  Smoke tests
     │
     ▼
  Deploy production (canary 10% → 100%)

Strategies:
  Blue-green: switch traffic instantly
  Canary: gradual rollout + metric watch
  Feature flags: decouple deploy from release""",
        "key_points": ["CI = build + test every commit", "CD automates deploy", "Canary/blue-green safe rollout", "Feature flags"],
    },
    "cs-testing-pyramid": {
        "explanation": (
            "**Testing pyramid:** Many **unit tests** (fast, isolated), fewer **integration tests** (DB, API), "
            "fewest **E2E tests** (full browser flow — slow, flaky).\n\n"
            "Also: **contract tests** (Pact between services), **load tests** (k6, JMeter), **security scans** (SAST/DAST)."
        ),
        "code": """        / E2E \\          few — Playwright, Cypress
       /─────────\\
      / Integration\\     some — Testcontainers, WebApplicationFactory
     /───────────────\\
    /   Unit tests    \\  many — xUnit, NUnit, Jest

Unit test (.NET):
  [Fact]
  public void CalculateTotal_AppliesDiscount()
  {
    var svc = new OrderService();
    Assert.Equal(90, svc.CalculateTotal(100, 0.1m));
  }

Integration:
  await using var factory = new WebApplicationFactory<Program>();
  var client = factory.CreateClient();
  var resp = await client.GetAsync("/api/health");

Shift-left: test early in pipeline, not only QA at end""",
        "language": "csharp",
        "key_points": ["Many unit, few E2E", "Integration with Testcontainers", "Contract tests for microservices", "Shift-left testing"],
    },
}
