"""HLD detailed content — items 21–40."""

HLD_DETAILED_PART2: dict[str, dict] = {
    "hld-rate-limiting": {
        "explanation": (
            "**Purpose:** Protect APIs from abuse, ensure fair usage, prevent overload.\n\n"
            "**Token bucket:** Tokens refill at fixed rate; request consumes token; allows bursts up to bucket size.\n\n"
            "**Sliding window log:** Track timestamps per window — precise but memory-heavy.\n\n"
            "**Fixed window counter:** Simple per-minute count in Redis — boundary spike problem.\n\n"
            "**Distributed:** Redis INCR + EXPIRE or Lua script for atomic sliding window across nodes."
        ),
        "code": """Token bucket (Redis):
  tokens = min(capacity, tokens + (now - last) * rate)
  if tokens >= 1:
    tokens -= 1; allow
  else: return 429 Too Many Requests

Response headers:
  X-RateLimit-Limit: 1000
  X-RateLimit-Remaining: 742
  X-RateLimit-Reset: 1699999999

Layers:
  CDN/Edge → API Gateway → App (defense in depth)

Per: IP, user_id, API key, endpoint""",
        "key_points": ["Token bucket allows burst", "Redis for distributed limit", "Return 429 + headers"],
    },
    "hld-multi-region": {
        "explanation": (
            "**Active-passive:** Primary region serves traffic; secondary on standby for DR (RPO/RTO defined). "
            "Failover via DNS/global LB.\n\n"
            "**Active-active:** Multiple regions serve simultaneously; users routed to nearest (geo-DNS). "
            "Harder: data replication lag, conflict resolution, split-brain.\n\n"
            "**Consider:** GDPR data residency, cross-region replication cost, global load balancer (Azure Front Door, Route 53)."
        ),
        "code": """Active-active (simplified):

Global LB (geo-routing)
    ├── US-East region: App + DB replica (leader US)
    └── EU-West region: App + DB replica (reads local)

User in Paris → EU-West (low latency)
Writes → route to leader OR multi-leader with conflict resolution

DR metrics:
  RPO = max data loss (replication lag)
  RTO = max downtime to recover

Challenges:
  - Cross-region writes (latency)
  - Clock skew / conflict merge
  - Session stickiness to region""",
        "key_points": ["Active-active for latency", "RPO/RTO for DR", "Data residency compliance"],
    },
    "hld-design-url-shortener": {
        "explanation": (
            "**Core flow:** POST long URL → generate short code → store mapping → GET /{code} → 301 redirect.\n\n"
            "**ID generation:** Base62 encode auto-increment ID (Snowflake) or MD5 hash (collision retry). "
            "Custom alias: unique constraint.\n\n"
            "**Scale:** 100:1 read:write — cache hot URLs in Redis; DB sharded by hash(code). "
            "**Analytics:** Async queue logs clicks."
        ),
        "code": """API:
  POST /api/v1/urls  { "long_url": "...", "alias": "optional" }
  GET  /{short_code} → 301 Location: long_url

Data model:
  short_code (PK, 7 chars base62)
  long_url, user_id, created_at, expires_at

Architecture:
  Client → LB → Shortener API → Redis (cache) → PostgreSQL (sharded)
                             └──► Kafka → Analytics DB

7-char base62 ≈ 3.5 trillion URLs
Estimate: 100M URLs × 500B ≈ 50GB + indexes""",
        "key_points": ["Base62 or hash for codes", "Redis cache reads", "301 for SEO/cache", "Shard by code"],
    },
    "hld-design-pastebin": {
        "explanation": (
            "**Upload:** Client POST text → store blob in S3/object storage → metadata (id, expiry, syntax) in DB → return URL.\n\n"
            "**Read:** Lookup metadata → fetch blob from object storage → render with syntax highlighting (client-side Prism.js).\n\n"
            "**Expiry:** TTL in DB + S3 lifecycle policy delete after N days."
        ),
        "code": """POST /paste { content, language, ttl_days }
→ paste_id: abc123
→ URL: pastebin.com/abc123

Storage:
  Metadata DB: id, created, expires, size, language
  Object store: s3://pastes/ab/c1/abc123.txt

Scale:
  Large pastes → direct S3 presigned upload (bypass app server)
  Rate limit: 10 pastes/hour/IP
  Max size: 1MB free tier""",
        "key_points": ["Blob in object storage", "Metadata in SQL", "Presigned upload for large files"],
    },
    "hld-design-twitter": {
        "explanation": (
            "**Write path:** Tweet → Tweet DB (sharded by user_id) → fan-out to followers' timeline caches (Redis lists).\n\n"
            "**Celebrity problem:** User with 50M followers — fan-out on write too slow → hybrid: "
            "normal users fan-out on write; celebrities fan-out on read (merge at read time).\n\n"
            "**Timeline read:** Pull precomputed Redis list; backfill missing celebrity tweets."
        ),
        "code": """Tweet write:
  1. Insert tweet (snowflake ID: time + machine + seq)
  2. If followers < 10K: push tweet_id to each follower's timeline cache
  3. If celebrity: skip fan-out (merge on read)

Timeline read:
  timeline = redis.lrange(user:123:timeline, 0, 800)
  + fetch celebrity tweets from follow graph
  merge + sort by timestamp

Components:
  Tweet service, Timeline service, User graph, Search (Elasticsearch),
  Media service (S3 + CDN), Notification (Kafka)""",
        "key_points": ["Fan-out on write vs read", "Celebrity hybrid", "Snowflake tweet IDs"],
    },
    "hld-design-instagram": {
        "explanation": (
            "**Upload photo:** Client → presigned S3 URL → upload direct → post metadata + processing job.\n\n"
            "**Processing:** Worker generates thumbnails (multiple sizes), stores variants on CDN.\n\n"
            "**Feed:** Similar to Twitter fan-out; media URLs point to CDN. Stories: TTL cache (24h)."
        ),
        "code": """Upload flow:
  1. POST /media/upload-url → presigned S3 PUT
  2. Client uploads image to S3
  3. POST /posts { media_id, caption }
  4. Worker: resize 150px, 640px, 1080px → CDN

Feed:
  Same fan-out as Twitter + CDN URLs for images

Storage estimate:
  500M photos/day × 2MB avg = 1 PB/day raw (needs tiering + compression)

Search:
  Elasticsearch on captions, hashtags, locations""",
        "key_points": ["Presigned S3 upload", "Async image processing", "CDN for delivery", "Feed like Twitter"],
    },
    "hld-design-whatsapp": {
        "explanation": (
            "**Real-time:** WebSocket gateway maintains persistent connections; message routed to recipient's gateway.\n\n"
            "**Offline:** Store in message queue/DB; push notification (FCM/APNs) on delivery.\n\n"
            "**Groups:** Fan-out to members; sequence numbers per chat for ordering. E2E encryption: Signal protocol."
        ),
        "code": """Send message:
  Client A ──WS──► Gateway A ──► Message Service ──► Gateway B ──WS──► Client B
                                    │
                              Message DB (persist)
                                    │
                              Push if B offline

Group chat (100 members):
  msg → store once → 100 delivery records OR fan-out to member inboxes

Presence:
  Heartbeat every 30s → Redis: user:online

Scale:
  Millions concurrent WebSocket connections → gateway cluster + sticky sessions""",
        "key_points": ["WebSocket gateway cluster", "Store-then-forward", "Push for offline", "Sequence per chat"],
    },
    "hld-design-youtube": {
        "explanation": (
            "**Upload:** Chunked resumable upload to blob storage → transcode pipeline (multiple resolutions/codecs) "
            "→ HLS/DASH segments on CDN.\n\n"
            "**Streaming:** Adaptive bitrate — client switches quality based on bandwidth.\n\n"
            "**Popular vs long-tail:** Hot videos on CDN edge; cold storage on cheaper tier (S3 Glacier)."
        ),
        "code": """Upload:
  Client → Resumable upload API → Raw storage (S3)
  → Transcode workers (1080p, 720p, 480p, 360p)
  → Segment + manifest (.m3u8) → CDN

Playback:
  Client requests manifest → CDN serves segments
  ABR algorithm picks quality per segment

View count:
  Async aggregate (eventual) — not synchronous on play

Recommendation:
  Offline ML pipeline (separate from serving path)""",
        "key_points": ["Transcode pipeline async", "HLS/DASH + CDN", "Adaptive bitrate", "Separate recommendation ML"],
    },
    "hld-design-uber": {
        "explanation": (
            "**Driver location:** Stream GPS updates (Kafka) → geospatial index (Geohash/QuadTree in Redis).\n\n"
            "**Matching:** Rider request → find nearby available drivers → dispatch offer → first accept wins.\n\n"
            "**ETA:** Routing API (OSRM/Google Maps) cached for common routes. Surge pricing: demand/supply ratio per geohash."
        ),
        "code": """Rider requests ride:
  1. Geohash rider location
  2. Query drivers in adjacent geohash cells (radius 5km)
  3. Filter: available, rating > 4.5
  4. Send offer to top 3 drivers (timeout 15s)
  5. First accept → create trip, notify both

Location updates:
  Driver app → every 4s → location service → Redis GEOADD

Storage:
  Trips DB (SQL), Locations (Redis/stream), Payments (separate svc)

Peak: New Year's Eve → queue matching requests""",
        "key_points": ["Geohash/QuadTree for proximity", "Offer/accept pattern", "Location streaming", "Surge by geohash"],
    },
    "hld-design-notifications": {
        "explanation": (
            "**Channels:** Push (FCM/APNs), Email (SendGrid), SMS (Twilio), In-app.\n\n"
            "**Architecture:** Event → Notification service → priority queues → channel workers → provider APIs.\n\n"
            "**Features:** User preferences (opt-out), templates, idempotent delivery, retry + DLQ, rate limit per channel."
        ),
        "code": """Event: order.shipped → Notification Service

  1. Load user preferences (push=yes, email=yes, sms=no)
  2. Render template: "Order {{id}} shipped"
  3. Enqueue:
     HIGH priority → push queue
     NORMAL       → email queue
  4. Workers call FCM / SendGrid with retry (3×)
  5. Log delivery status; DLQ on permanent failure

Dedup:
  notification_id unique — skip if already sent

Scale:
  Batch email (1000/recipient list)
  Push: 1M/min peak → horizontal workers""",
        "key_points": ["Priority queues per channel", "User preferences", "Idempotent delivery", "Retry + DLQ"],
    },
    "hld-design-autocomplete": {
        "explanation": (
            "**Goal:** Return top 5 suggestions as user types prefix.\n\n"
            "**Approach:** Precompute popular prefix → top queries (offline job). "
            "Store in trie or sorted DB index. At runtime: lookup prefix, return top-k by frequency.\n\n"
            "**Scale:** Cache hot prefixes in Redis; debounce client (300ms); personalize optional (user history)."
        ),
        "code": """Offline pipeline:
  Search logs → count (prefix, query) pairs
  Keep top 10 queries per prefix (min length 2)

Runtime:
  GET /suggest?q=inst
  → Redis: prefix:inst → ["instagram", "institute", ...]
  → if miss: DB trie lookup

Data structure:
  Trie node: { char, children[], top_queries[] }

Latency target: < 50ms p99
  - Entire popular trie in memory (~ few GB)""",
        "key_points": ["Precompute offline", "Trie or prefix index", "Client debounce", "Top-k by frequency"],
    },
    "hld-design-web-crawler": {
        "explanation": (
            "**Components:** URL frontier (priority queue), fetcher workers, parser, dedup (Bloom filter), "
            "content store, link extractor re-enqueueing new URLs.\n\n"
            "**Politeness:** Per-domain rate limit (1 req/sec), respect robots.txt.\n\n"
            "**Scale:** Distributed workers; URL frontier in Redis/Kafka; Bloom filter for seen URLs (memory efficient)."
        ),
        "code": """Loop:
  1. Pop URL from frontier (priority: PageRank, freshness)
  2. Check robots.txt cache
  3. HTTP fetch (timeout 10s, follow redirects max 3)
  4. Parse HTML → extract links + text
  5. Bloom filter: if URL seen, skip else add
  6. Store page in object storage + index text in Elasticsearch
  7. Enqueue new links (same domain throttle)

Frontier:
  Kafka topic partitioned by hash(domain)

1B pages × 20KB avg = 20TB storage""",
        "key_points": ["Bloom filter dedup", "Per-domain politeness", "Distributed frontier", "Separate fetch and parse"],
    },
    "hld-design-distributed-cache": {
        "explanation": (
            "**Redis Cluster:** Hash slots (16384) across nodes; consistent hashing; replication per master.\n\n"
            "**Patterns:** Cache-aside, TTL per key, eviction LRU.\n\n"
            "**Problems:** Hot key (replicate key), cache penetration (Bloom filter), cache avalanche (random TTL jitter)."
        ),
        "code": """Redis Cluster (3 masters, 3 replicas):

  key → CRC16(key) mod 16384 → slot → node

Client library handles MOVED/ASK redirects

Hot key mitigation:
  - Local in-process cache (L1) in front of Redis
  - Replicate hot key to multiple Redis keys (read fan-out)

Cache aside:
  miss → DB → set with TTL=3600 + jitter(0-300s)

Memory estimate:
  100M keys × 1KB = 100GB → cluster sharded""",
        "key_points": ["Redis cluster hash slots", "Hot key replication", "TTL jitter prevents avalanche"],
    },
    "hld-design-rate-limiter-sys": {
        "explanation": (
            "**Distributed rate limiter as a service:** All API nodes call central Redis counter.\n\n"
            "**Sliding window log in Redis:** Sorted set of timestamps; remove old; count in window.\n\n"
            "**Alternative:** Token bucket with Lua script for atomicity.\n\n"
            "**API:** `Allow(user_id, limit, window)` → bool + remaining."
        ),
        "code": """Sliding window (Redis ZSET):

  key = rate:{user_id}:{endpoint}
  now = unix_ms()
  ZREMRANGEBYSCORE key 0 (now - window_ms)
  count = ZCARD key
  if count < limit:
    ZADD key now uuid()
    EXPIRE key window_sec
    return ALLOW
  else:
    return DENY (429)

Multi-tier:
  Free: 100 req/min
  Pro:  10000 req/min

Deploy as sidecar or API gateway plugin""",
        "key_points": ["Redis ZSET sliding window", "Lua for atomicity", "Per user + endpoint limits"],
    },
    "hld-design-ecommerce": {
        "explanation": (
            "**Checkout flow:** Cart → validate inventory → reserve stock → payment → create order → confirm email.\n\n"
            "**Inventory:** Pessimistic lock or atomic decrement (`UPDATE stock SET qty=qty-1 WHERE qty>0`). "
            "Reservation TTL releases on payment timeout.\n\n"
            "**Saga:** If payment fails → compensate (release inventory). Outbox pattern for reliable events."
        ),
        "code": """Checkout saga:
  1. CartSvc: validate items
  2. InventorySvc: reserve(stock, TTL=15min) → reservation_id
  3. PaymentSvc: charge(idempotency_key)
     SUCCESS → 4. OrderSvc: create order
               5. InventorySvc: confirm reservation
               6. EmailSvc: confirmation (async)
     FAIL    → release reservation

Overselling prevention:
  UPDATE products SET stock = stock - 1
  WHERE id = ? AND stock > 0
  (rows affected = 0 → sold out)

Flash sale:
  Queue checkout requests → process sequentially per SKU""",
        "key_points": ["Reserve inventory with TTL", "Saga with compensation", "Idempotent payment", "Atomic stock decrement"],
    },
    "hld-design-payment": {
        "explanation": (
            "**PCI compliance:** Never store raw card numbers; use tokenization (Stripe Elements).\n\n"
            "**Ledger:** Double-entry bookkeeping; immutable transaction log.\n\n"
            "**Reconciliation:** Match internal ledger with processor settlements daily. Webhooks for async status."
        ),
        "code": """Charge flow:
  Client → token (Stripe.js) → Payment API
  → Processor (Stripe/Adyen)
  → Webhook: payment.succeeded
  → Update ledger + order status

Ledger entries:
  DEBIT  customer_wallet  $100
  CREDIT merchant_account  $97
  CREDIT platform_fee       $3

Idempotency-Key on every charge API call
Exactly-once ledger via unique transaction_id constraint

Reconciliation job (nightly):
  Compare processor CSV vs internal ledger""",
        "key_points": ["Tokenization for PCI", "Immutable ledger", "Webhooks + idempotency", "Daily reconciliation"],
    },
    "hld-design-newsfeed": {
        "explanation": (
            "**Facebook-style feed:** Aggregate posts from friends + pages + ads; rank by ML model (engagement prediction).\n\n"
            "**Hybrid fan-out:** Precompute for normal users; pull+merge for high-follower sources.\n\n"
            "**Ranking pipeline:** Candidate generation → feature fetch → ML ranker → diversity filter → cache per user."
        ),
        "code": """Feed generation (on read):
  1. Pull precomputed feed slice from cache (last 800 post IDs)
  2. Fetch fresh posts from high-follower sources
  3. Merge + deduplicate
  4. Ranker service: score each post (ML model)
  5. Inject ads at positions 3, 8, 15
  6. Return paginated (cursor-based)

Cache:
  feed:user:123 → sorted set of post_ids by score
  TTL refresh on pull (stale OK 30s)

Write:
  Post → fan-out to friends' feed caches (async workers)""",
        "key_points": ["ML ranking pipeline", "Hybrid fan-out", "Cursor pagination", "Ads injection slots"],
    },
    "hld-design-google-docs": {
        "explanation": (
            "**Collaborative editing:** Operational Transformation (OT) or CRDTs for conflict-free concurrent edits.\n\n"
            "**Sync:** WebSocket broadcasts operations; server orders/transforms ops; clients apply transformed ops.\n\n"
            "**Persistence:** Operation log (append-only) + periodic snapshots for fast load."
        ),
        "code": """Edit operation:
  { doc_id, user_id, revision, op: { type: "insert", pos: 42, text: "hello" } }

Server:
  1. Receive op at revision N
  2. Transform against concurrent ops (OT)
  3. Assign revision N+1
  4. Broadcast to all connected clients
  5. Append to operation log (Kafka)

Snapshot every 1000 ops → S3
Load: latest snapshot + replay ops since

Presence:
  WebSocket room per doc; cursor positions broadcast""",
        "key_points": ["OT or CRDT for conflicts", "Operation log + snapshots", "WebSocket sync", "Revision numbers"],
    },
    "hld-design-dropbox": {
        "explanation": (
            "**Sync model:** Files chunked (4MB blocks); content-hash (SHA-256) per block; dedup identical blocks.\n\n"
            "**Upload:** Client computes hashes → sync API returns missing blocks → upload only deltas.\n\n"
            "**Metadata:** File tree in SQL; block mapping table; conflict → save both as conflicted copies."
        ),
        "code": """Block upload:
  1. Split file into 4MB chunks
  2. hash(chunk) for each
  3. POST /sync/check { hashes[] } → missing_hashes
  4. Upload only missing blocks (dedup saves storage)
  5. POST /files/commit { path, block_hashes[], version }

Metadata:
  files(id, user_id, path, version, device_id)
  blocks(hash PK, s3_key, size)

Conflict (2 devices edit same file):
  Create "file (conflicted copy).txt"

Storage savings:
  Same block hash stored once globally""",
        "key_points": ["Content-hash block dedup", "Upload only missing blocks", "Version per file", "Conflict copies"],
    },
    "hld-design-ticketmaster": {
        "explanation": (
            "**Core problem:** Prevent double booking under extreme concurrency (flash sales).\n\n"
            "**Approaches:** Pessimistic DB row lock on seat, distributed lock (Redis), or queue-based sequential booking.\n\n"
            "**Waiting room:** Queue users before sale; admit N/sec to purchase flow."
        ),
        "code": """Seat booking (pessimistic):
  BEGIN TRANSACTION
  SELECT * FROM seats WHERE event_id=? AND seat_id=? FOR UPDATE
  IF status = 'available':
    UPDATE seats SET status='held', user_id=?, hold_expires=now()+10min
    COMMIT → proceed to payment
  ELSE ROLLBACK → seat taken

Payment timeout job:
  Release holds where hold_expires < now()

Flash sale:
  Virtual waiting room (queue 1M users)
  Admit 5000/min to booking UI

Alternative: Kafka queue per event — single consumer assigns seats""",
        "key_points": ["SELECT FOR UPDATE or distributed lock", "Hold with TTL", "Waiting room for flash sales", "No double booking"],
    },
}
