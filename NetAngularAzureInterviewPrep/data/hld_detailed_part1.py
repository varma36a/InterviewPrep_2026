"""HLD detailed content — items 1–20."""

HLD_DETAILED_PART1: dict[str, dict] = {
    "hld-approach-framework": {
        "explanation": (
            "**Standard 45-minute system design flow:**\n\n"
            "1. **Clarify (5 min)** — functional scope (MVP features), non-functional (scale, latency, availability), "
            "constraints (budget, team size), read/write ratio.\n"
            "2. **Estimate (5 min)** — users, QPS, storage, bandwidth (back-of-envelope).\n"
            "3. **High-level design (15 min)** — draw clients, LB, app servers, cache, DB, queue, CDN. "
            "Define APIs and data model at a high level.\n"
            "4. **Deep dive (15 min)** — interviewer picks bottleneck: sharding, fan-out, consistency, failure modes.\n"
            "5. **Wrap-up (5 min)** — trade-offs, monitoring, future improvements.\n\n"
            "**Interview tip:** Think aloud, ask questions, prioritize — don't jump to Kafka for every problem."
        ),
        "code": """System Design Interview Template
─────────────────────────────────
[1] Requirements
    Functional:    What features? (MVP vs nice-to-have)
    Non-functional: QPS, latency p99, availability 99.9%,
                    consistency needs, data retention

[2] Estimation
    DAU → actions/day → avg QPS → peak QPS (2-3×)
    Storage = records × size × years
    Bandwidth = QPS × payload size

[3] High-Level Architecture
    Client → CDN → LB → API Gateway → Services
                      ↓         ↓
                   Cache     Message Queue
                      ↓         ↓
                   Database(s)  Workers

[4] Deep Dive Topics (pick 1-2)
    - Data model & indexing
    - Scaling reads/writes
    - Hot spots & caching
    - Failure & recovery""",
        "key_points": ["Clarify before designing", "Estimate to justify choices", "Draw diagrams", "State trade-offs explicitly"],
    },
    "hld-functional-nonfunctional": {
        "explanation": (
            "**Functional requirements** describe *what* the system does: "
            "e.g. shorten URL, redirect, optional custom alias, analytics.\n\n"
            "**Non-functional requirements (NFRs)** describe *how well*: "
            "latency (<100ms redirect), availability (99.99%), durability, scalability (100M URLs), "
            "security (HTTPS), compliance (GDPR).\n\n"
            "NFRs drive architecture more than features. A URL shortener at 1K QPS looks very different at 1M QPS."
        ),
        "code": """Functional (URL Shortener):
  - Create short URL from long URL
  - Redirect short → long (301/302)
  - Optional custom alias, expiration
  - Click analytics

Non-Functional:
  - 100:1 read:write ratio → optimize reads
  - p99 redirect latency < 50ms
  - 99.9% availability
  - URLs never lost (durability)
  - Handle 10K writes/s, 1M reads/s at peak

SLA / SLO / SLI:
  SLI = measured metric (e.g. success rate)
  SLO = target (99.9% requests succeed)
  SLA = contract with penalties""",
        "key_points": ["NFRs drive scale decisions", "SLA/SLO/SLI vocabulary", "MVP functional scope first"],
    },
    "hld-back-of-envelope": {
        "explanation": (
            "**Typical calculations interviewers expect:**\n\n"
            "- **QPS:** 10M DAU × 10 actions/day = 100M/day ÷ 86,400 ≈ **1,200 avg QPS**; peak ≈ **3,600 QPS**\n"
            "- **Storage:** 100M new records/year × 500 bytes ≈ **50 GB/year** (raw); add indexes ×2–3\n"
            "- **Bandwidth:** 1M read QPS × 1 KB response ≈ **1 GB/s** outbound\n"
            "- **Memory cache:** cache 20% hot data: 0.2 × total dataset\n\n"
            "Round numbers; state assumptions clearly."
        ),
        "code": """Example: Twitter-like (rough)
  300M DAU, 2 tweets/user/day
  Writes: 600M/day ÷ 86400 ≈ 7K tweet/s (peak ~20K)
  Reads:  timeline 10× writes ≈ 70K–200K read/s

  Tweet: ~300 bytes + media separate
  600M × 300B/day × 365 × 5yr ≈ hundreds of TB (needs sharding)

  Cache hot timelines:
  20M active users × 500 tweets × 300B ≈ 3 TB RAM ( impractical → partial cache )""",
        "key_points": ["Peak ≈ 2–3× average", "State assumptions", "Separate read/write math", "Storage includes indexes"],
    },
    "hld-read-write-heavy": {
        "explanation": (
            "**Read-heavy (100:1+):** Social feeds, URL redirects, product catalogs. "
            "Use CDN, aggressive caching (Redis), read replicas, denormalized read models, CQRS.\n\n"
            "**Write-heavy:** Logging, IoT sensors, analytics ingestion. "
            "Use write-optimized stores (Cassandra, Kafka), batching, async processing, sharding by time/key, "
            "avoid synchronous indexes on hot path.\n\n"
            "**Balanced:** OLTP e-commerce — tune both; cache reads, queue writes for non-critical paths."
        ),
        "code": """Read-heavy pattern:
  Client → CDN → LB → App → Redis cache → DB replica(s)
  Write path: App → DB primary → invalidate cache

Write-heavy pattern:
  Client → LB → Ingest API → Kafka → Stream processors → Column store
  Reads: materialized views / pre-aggregated tables

CQRS (extreme skew):
  Command API → Write DB (normalized)
  Query API  → Read DB (denormalized, rebuilt from events)""",
        "key_points": ["Know read:write ratio early", "CQRS for extreme skew", "Cache invalidation on writes"],
    },
    "hld-vertical-horizontal": {
        "explanation": (
            "**Vertical scaling (scale up):** Bigger CPU/RAM/disk on one machine. Simple but hits hardware ceiling; single point of failure.\n\n"
            "**Horizontal scaling (scale out):** Add more machines behind load balancer. "
            "Requires stateless app tier; database is the hard part (replication, sharding).\n\n"
            "Modern cloud systems scale horizontally. Vertical still used for DB primary briefly or specialized workloads."
        ),
        "code": """Vertical:  4 CPU → 32 CPU, 16GB → 256GB RAM
  Pros: no code change, no distributed complexity
  Cons: ceiling, downtime to resize, expensive

Horizontal: 1 app server → 50 app servers + LB
  Pros: theoretically unlimited, fault isolation
  Cons: stateless design, data consistency, ops complexity

Stateless app checklist:
  - Session in Redis (not in-memory)
  - Sticky sessions avoided or via consistent hash
  - File uploads → object storage (S3)""",
        "key_points": ["Horizontal for web tier", "DB hardest to scale out", "Stateless apps required"],
    },
    "hld-load-balancer": {
        "explanation": (
            "**L4 (Transport):** Routes by IP/port (TCP/UDP). Fast, no HTTP awareness. Used for raw TCP, WebSockets.\n\n"
            "**L7 (Application):** Routes by URL path, headers, cookies. SSL termination, WAF, rate limits.\n\n"
            "**Algorithms:** Round robin (simple), weighted (heterogeneous servers), least connections (long-lived), "
            "IP hash (session affinity), consistent hash (cache nodes)."
        ),
        "code": """                    ┌─────────────┐
Clients ──────────►│ Load Balancer│
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
      App Server 1    App Server 2    App Server 3

L7 example routing:
  /api/users/*  → user-service pool
  /api/orders/* → order-service pool
  /static/*     → CDN origin

Health checks:
  HTTP GET /health every 10s → remove unhealthy nodes""",
        "key_points": ["L4 vs L7 trade-off", "Health checks essential", "Consistent hash for sticky cache"],
    },
    "hld-caching-strategies": {
        "explanation": (
            "**Cache-aside (lazy):** App reads cache; on miss, read DB and populate cache. "
            "App writes DB then deletes cache entry.\n\n"
            "**Write-through:** Write to cache and DB synchronously — consistent but slower writes.\n\n"
            "**Write-back:** Write to cache only; async flush to DB — fast but risk data loss.\n\n"
            "**CDN:** Edge cache for static assets and cacheable API responses (Cache-Control headers)."
        ),
        "code": """Cache-aside (most common):
  read:
    val = cache.get(key)
    if val is null:
      val = db.get(key)
      cache.set(key, val, TTL=3600)
    return val
  write:
    db.update(key, val)
    cache.delete(key)

Eviction: LRU, LFU, TTL
Problems:
  - Cache stampede → lock / probabilistic early expiry
  - Hot key → replicate key across nodes
  - Penetration → bloom filter for non-existent keys""",
        "key_points": ["Cache-aside most common", "TTL + eviction policy", "Invalidate on write", "CDN for static"],
    },
    "hld-db-replication": {
        "explanation": (
            "**Leader-follower (primary-replica):** One leader accepts writes; replicas copy WAL/binlog asynchronously or synchronously.\n\n"
            "**Sync replication:** Strong durability; higher write latency (wait for replica ack).\n\n"
            "**Async replication:** Faster writes; replication lag — stale reads on replicas.\n\n"
            "**Failover:** Promote replica to leader on failure (manual or automated with consensus like Raft)."
        ),
        "code": """         Writes                    Reads
           │                        │
           ▼                        ▼
    ┌─────────────┐          ┌─────────────┐
    │   Leader    │──repl──►│  Replica 1  │
    │  (Primary)  │──repl──►│  Replica 2  │
    └─────────────┘          └─────────────┘

Read-your-writes fix:
  - Route user's reads to leader briefly after write
  - Or track replication lag per session

Multi-leader / leaderless (Dynamo, Cassandra):
  - Higher write availability
  - Conflict resolution (LWW, CRDT)""",
        "key_points": ["Async vs sync trade-off", "Replication lag", "Failover planning"],
    },
    "hld-db-sharding": {
        "explanation": (
            "**Sharding (horizontal partitioning):** Split data across multiple DB instances by shard key (user_id, tenant_id, geo).\n\n"
            "**Strategies:** Hash-based (even distribution), range-based (time series — hot latest shard), "
            "geo-based (EU users → EU shard).\n\n"
            "**Challenges:** Cross-shard joins expensive, rebalancing when adding shards, global unique IDs (Snowflake)."
        ),
        "code": """Hash sharding:
  shard_id = hash(user_id) % num_shards
  user 12345 → shard 7

Range sharding (time):
  2024 data → shard A
  2025 data → shard B  (hot shard problem on current year)

Consistent hashing:
  Add/remove shard → only K/n keys move

Cross-shard query:
  - Avoid — design access patterns per shard key
  - Scatter-gather if unavoidable (slow)

Global ID: Snowflake (timestamp + machine + sequence)""",
        "key_points": ["Pick shard key by access pattern", "Consistent hashing for rebalancing", "Avoid cross-shard joins"],
    },
    "hld-sql-vs-nosql": {
        "explanation": (
            "**SQL (PostgreSQL, MySQL, SQL Server):** ACID transactions, joins, complex queries, strong schema. "
            "Vertical scale + read replicas; sharding harder.\n\n"
            "**NoSQL types:** Document (MongoDB), Key-Value (Redis/DynamoDB), Column (Cassandra), Graph (Neo4j). "
            "Scale-out friendly, flexible schema, eventual consistency common.\n\n"
            "**Polyglot persistence:** SQL for orders/users, Redis for cache, Elasticsearch for search, S3 for blobs."
        ),
        "code": """Choose SQL when:
  - ACID transactions (payments, inventory)
  - Complex joins and reporting
  - Strong consistency required

Choose NoSQL when:
  - Massive scale-out writes (IoT, logs)
  - Flexible/evolving schema (user profiles)
  - Simple key access patterns (session store)
  - Geo-distributed low-latency (DynamoDB global tables)

Common stack:
  PostgreSQL (source of truth)
  + Redis (cache/sessions)
  + Elasticsearch (full-text search)
  + S3 (media/files)""",
        "key_points": ["Polyglot persistence common", "SQL for transactions", "NoSQL for scale-out simple access"],
    },
    "hld-cap-theorem": {
        "explanation": (
            "**CAP:** In a network partition, choose **Consistency** (all nodes see same data) or **Availability** (every request gets a response).\n\n"
            "**CP systems:** ZooKeeper, etcd, HBase — sacrifice availability during partition.\n\n"
            "**AP systems:** Cassandra, DynamoDB (configurable), DNS — serve stale data, reconcile later.\n\n"
            "**PACELC extension:** If no Partition, choose Latency vs Consistency (e.g. DynamoDB tunable)."
        ),
        "code": """During network partition:

CP (Consistency + Partition tolerance):
  Bank transfer — reject writes until quorum restored
  Example: etcd, ZooKeeper

AP (Availability + Partition tolerance):
  Social media likes count — show slightly stale count
  Example: Cassandra, CouchDB

CA (not realistic in distributed):
  Single-node DB — no partition across cluster

Interview answer:
  "We need AP for feed reads with eventual consistency,
   but CP for payment ledger using strong consistency DB." """,
        "key_points": ["Partition forces C vs A choice", "PACELC adds latency dimension", "Different subsystems different choices"],
    },
    "hld-consistent-hashing": {
        "explanation": (
            "**Problem:** Simple `hash(key) % N` remaps almost all keys when N changes.\n\n"
            "**Solution:** Hash keys and nodes onto a ring (0–2^32). Key goes to first node clockwise. "
            "Adding node only affects neighbors. **Virtual nodes** improve balance (each physical node = 100–200 vnodes).\n\n"
            "**Used in:** Memcached clients, Cassandra token ring, CDNs, load balancers."
        ),
        "code": """Simple mod hash (bad):
  N=3 → 4: nearly all keys remap

Consistent hash ring:
        Node A
       /      \\
   Key K       Node B
       \\      /
        Node C

Key K → walk clockwise → lands on Node B
Add Node D → only keys between C and D move

Virtual nodes:
  Node A → A0, A1, A2... on ring (even distribution)""",
        "key_points": ["Minimal remapping on node change", "Virtual nodes for balance", "Used in caches and sharding"],
    },
    "hld-message-queues": {
        "explanation": (
            "**Purpose:** Decouple producers and consumers; absorb traffic spikes; async processing; event-driven microservices.\n\n"
            "**Kafka:** Durable log, high throughput, partition ordering, replay. "
            "**RabbitMQ:** Flexible routing, classic queues. **SQS/Azure Service Bus:** Managed cloud queues.\n\n"
            "**Delivery semantics:** At-most-once, at-least-once (+ idempotent consumer), exactly-once (hard — Kafka transactions)."
        ),
        "code": """Order placed event:

Order Service ──publish──► Kafka topic: orders
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
              Email Worker  Inventory   Analytics
              (consumer)    (consumer)  (consumer)

Benefits:
  - Order API returns fast (async side effects)
  - Spike in orders → queue buffers
  - Retry failed consumers independently

Patterns:
  - Event notification (small payload + fetch)
  - Event-carried state transfer
  - Saga choreography for distributed tx""",
        "key_points": ["Decouple and buffer spikes", "At-least-once + idempotent consumers", "Kafka for high throughput log"],
    },
    "hld-microservices-monolith": {
        "explanation": (
            "**Monolith:** Single deployable unit. Simple debugging, ACID transactions easy, no network between modules. "
            "Hard to scale individual parts; deployment coupling.\n\n"
            "**Microservices:** Independent deploy, scale, tech stack per service. "
            "Network failures, distributed transactions, observability complexity, organizational overhead.\n\n"
            "**Guidance:** Start modular monolith; extract services when team scale or independent scaling justifies cost."
        ),
        "code": """Monolith:
  ┌─────────────────────────────┐
  │  User | Order | Payment     │
  │  (single process + DB)      │
  └─────────────────────────────┘

Microservices:
  User Svc ◄──► Order Svc ◄──► Payment Svc
     │              │               │
   User DB       Order DB        Payment DB

When to split:
  - Different scale needs (search vs checkout)
  - Different teams (Conway's law)
  - Different SLAs / release cadence

Costs:
  - Distributed tracing (OpenTelemetry)
  - API contracts / versioning
  - Saga instead of 2PC""",
        "key_points": ["Start monolith modular", "Split on clear boundaries", "Distributed ops cost real"],
    },
    "hld-consistency-models": {
        "explanation": (
            "**Strong consistency:** Read returns latest write (linearizability). Required for bank balances, inventory counts.\n\n"
            "**Eventual consistency:** Replicas converge; reads may be stale briefly. OK for social likes, view counts.\n\n"
            "**Read-your-writes:** User sees own updates immediately (session stickiness or leader read).\n\n"
            "**Causal consistency:** Causally related ops seen in order."
        ),
        "code": """Strong (single leader DB):
  write → leader → sync/async replicate
  read from leader OR quorum read

Eventual (Dynamo-style):
  write → local replica → gossip to others
  read → any replica (may be stale)

Tunable (DynamoDB):
  ConsistentRead=true  → higher latency, fresh
  ConsistentRead=false → eventual, faster/cheaper

Interview:
  "Feed timeline: eventual OK (stale 1-2s)
   Wallet balance: strong consistency required" """,
        "key_points": ["Match consistency to business need", "Read-your-writes for UX", "Quorum reads for balance"],
    },
    "hld-idempotency": {
        "explanation": (
            "**Idempotent operation:** Performing it multiple times has the same effect as once. "
            "Critical for retries in distributed systems (network timeouts, message redelivery).\n\n"
            "**Implementation:** Client sends `Idempotency-Key` header (UUID); server stores key + result; "
            "duplicate request returns cached response without re-charging.\n\n"
            "**HTTP:** GET, PUT, DELETE naturally idempotent; POST is not — needs explicit key."
        ),
        "code": """POST /payments/charge
Headers: Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000

Server logic:
  if idempotency_store.exists(key):
    return cached_response(key)
  result = charge_card(...)
  idempotency_store.save(key, result, TTL=24h)
  return result

Also use:
  - Unique DB constraint (order_id + action)
  - UPSERT instead of blind INSERT
  - Kafka consumer offset + idempotent handler""",
        "key_points": ["Idempotency-Key for POST", "Store result with TTL", "Natural idempotency for PUT/DELETE"],
    },
    "hld-api-gateway": {
        "explanation": (
            "**API Gateway** is the single entry point for clients: routing, authentication, rate limiting, "
            "SSL termination, request/response transformation, aggregation (BFF pattern).\n\n"
            "**Examples:** Kong, AWS API Gateway, Azure API Management, NGINX Ingress.\n\n"
            "**BFF (Backend for Frontend):** Separate gateway per client type (mobile vs web) to tailor APIs."
        ),
        "code": """Mobile App ──┐
Web App ───────┼──► API Gateway ──► User Service
Admin Portal ──┘         │         Order Service
                         │         Search Service
                    - JWT validate
                    - Rate limit 1000/min
                    - Route /v1/users → user-svc
                    - Circuit break on 5xx
                    - Request logging + trace ID

vs Direct service mesh:
  Gateway = north-south (external)
  Service mesh (Istio) = east-west (internal)""",
        "key_points": ["Single external entry", "Auth + rate limit central", "BFF for client-specific APIs"],
    },
    "hld-observability": {
        "explanation": (
            "**Three pillars:**\n"
            "- **Logs:** Structured JSON events (Serilog → Elasticsearch/Loki)\n"
            "- **Metrics:** Time-series counters/gauges (Prometheus → Grafana)\n"
            "- **Traces:** Distributed request flow (OpenTelemetry → Jaeger/App Insights)\n\n"
            "**SRE practice:** Define SLIs, set SLOs (99.9% availability), alert on error budget burn rate — not every blip."
        ),
        "code": """Request flow with observability:

Client ──► Gateway ──► OrderSvc ──► PaymentSvc
              │            │              │
           trace-id     span          span
           log entry    metric++       log error

Correlation:
  X-Correlation-Id: abc-123 (pass through all services)

Key metrics:
  - Request rate, error rate, duration (RED method)
  - CPU, memory, queue depth (USE method)
  - p50/p95/p99 latency

Alert example:
  SLO: 99.9% success / 30 days
  Burn rate > 2× → page on-call""",
        "key_points": ["Logs + metrics + traces", "Correlation ID everywhere", "Alert on SLO burn not noise"],
    },
    "hld-circuit-breaker": {
        "explanation": (
            "**Circuit breaker** prevents cascade failures when a dependency is down.\n\n"
            "**States:** Closed (normal) → Open (fail fast, no calls) → Half-open (probe one request).\n\n"
            "Combine with **timeouts**, **retries with exponential backoff + jitter**, and **bulkhead** (isolate thread pools per dependency)."
        ),
        "code": """Polly (.NET) example pattern:

Policy
  .Handle<HttpRequestException>()
  .CircuitBreakerAsync(
    exceptionsAllowedBeforeBreaking: 5,
    durationOfBreak: TimeSpan.FromSeconds(30))

Retry with jitter:
  retry: 3 attempts, delay 2^attempt + random(0,1000)ms

Bulkhead:
  max 10 concurrent calls to PaymentSvc
  (other services unaffected if payment hangs)

Fallback:
  if circuit open → return cached quote / degraded response""",
        "language": "csharp",
        "key_points": ["Fail fast when dependency unhealthy", "Backoff + jitter on retry", "Bulkhead isolation"],
    },
    "hld-service-discovery": {
        "explanation": (
            "**Service discovery** lets services find each other without hardcoded IPs.\n\n"
            "**Client-side:** Client queries registry (Consul), caches instances, load balances. (Eureka + Ribbon)\n\n"
            "**Server-side:** Requests go through LB; LB knows healthy backends. (Kubernetes Services + kube-proxy)\n\n"
            "**Health checks:** Liveness (restart if dead), Readiness (remove from LB until ready)."
        ),
        "code": """Kubernetes model:

Pod (order-svc-abc) ──register──► K8s Service "order-svc"
                                         │
Payment Pod ──DNS query order-svc ───────┘
              → virtual IP → kube-proxy → healthy pod

Consul model:
  Service registers: { name: "order", addr: "10.0.1.5:8080" }
  Consumer watches catalog → updates local LB list

Health:
  GET /health/live  → 200 or restart container
  GET /health/ready → 200 or remove from rotation""",
        "key_points": ["K8s DNS for server-side discovery", "Liveness vs readiness", "Avoid hardcoded endpoints"],
    },
}
