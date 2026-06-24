"""CS Fundamentals detailed content — items 1–20."""

CS_DETAILED_PART1: dict[str, dict] = {
    "cs-process-vs-thread": {
        "explanation": (
            "A **process** is an independent program execution with its own memory space (code, data, heap, stack), "
            "file descriptors, and PID. Processes are isolated — one crash doesn't corrupt another.\n\n"
            "A **thread** is a lightweight unit of execution *within* a process. Threads share the process memory "
            "(heap, global vars) but have private stack and registers. Cheaper to create; need synchronization for shared data.\n\n"
            "**Use threads** for concurrent I/O within one app; **processes** for isolation (browser tabs, microservices)."
        ),
        "code": """Process vs Thread
─────────────────
Process A          Process B
┌─────────────┐   ┌─────────────┐
│ Memory      │   │ Memory      │  ← separate address spaces
│ Thread 1    │   │ Thread 1    │
│ Thread 2    │   └─────────────┘
└─────────────┘

IPC (Inter-Process): pipes, sockets, shared memory
Thread sync: mutex, lock, Monitor

.NET:
  Process.Start("notepad.exe")  // new process
  Task.Run(() => ...)           // thread pool thread
  Parallel.For(...)             // multiple threads""",
        "language": "csharp",
        "key_points": ["Process = isolated memory", "Threads share heap", "Sync shared mutable state", "IPC vs in-process locks"],
    },
    "cs-deadlock": {
        "explanation": (
            "**Deadlock:** Two+ threads blocked forever, each waiting for a resource held by another.\n\n"
            "**Four necessary conditions (Coffman):** Mutual exclusion, hold and wait, no preemption, circular wait.\n\n"
            "**Prevention:** Lock ordering (always acquire A before B), try-lock with timeout, banker's algorithm. "
            "**Detection:** Wait-for graph cycle. **Recovery:** Kill/restart thread."
        ),
        "code": """Deadlock example:
  Thread 1: lock(A) → lock(B)
  Thread 2: lock(B) → lock(A)  // circular wait!

Prevention — consistent ordering:
  Thread 1: lock(A) → lock(B)
  Thread 2: lock(A) → lock(B)  // same order

C# try-lock:
  if (Monitor.TryEnter(obj, TimeSpan.FromSeconds(1)))
  {
    try { /* work */ }
    finally { Monitor.Exit(obj); }
  }

DB deadlock: SQL Server detects → victim rollback""",
        "language": "csharp",
        "key_points": ["Four Coffman conditions", "Lock ordering prevents", "Try-lock timeout", "DB detects deadlocks"],
    },
    "cs-virtual-memory": {
        "explanation": (
            "**Virtual memory** gives each process a large logical address space independent of physical RAM.\n\n"
            "**Paging:** Memory split into fixed-size pages (4KB); page table maps virtual → physical frame. "
            "**Page fault:** Page not in RAM → OS loads from disk (swap).\n\n"
            "**TLB:** Hardware cache of page table entries for speed. Enables overcommit and process isolation."
        ),
        "code": """Virtual address → Page table → Physical frame

Page fault flow:
  1. CPU accesses virtual addr
  2. Not in TLB → page table walk
  3. Present bit = 0 → PAGE FAULT
  4. OS loads page from disk to free frame
  5. Update page table, retry instruction

Benefits:
  - Process isolation (can't access other's memory)
  - More virtual memory than physical RAM
  - Shared pages (DLL code shared across processes)""",
        "key_points": ["Page table maps virtual→physical", "Page fault loads from disk", "TLB speeds lookup", "Enables isolation"],
    },
    "cs-context-switch": {
        "explanation": (
            "**Context switch:** OS saves state of running thread (registers, PC, stack pointer) and restores another thread's state.\n\n"
            "**Cost:** CPU cache pollution, TLB flush, kernel scheduler overhead — microseconds but adds up with many threads.\n\n"
            "**Implication:** More threads ≠ faster; optimal often ≈ CPU cores for CPU-bound; more threads for I/O-bound."
        ),
        "code": """Context switch steps:
  1. Save register state of Thread A to PCB
  2. Pick next runnable thread (scheduler)
  3. Restore register state of Thread B
  4. Resume execution of Thread B

Costs:
  - Direct: save/restore registers
  - Indirect: CPU cache miss, TLB miss

Rule of thumb:
  CPU-bound: threads ≈ core count
  I/O-bound:  threads >> core count (waiting on disk/network)""",
        "key_points": ["Save/restore CPU state", "Cache/TLB flush cost", "Match threads to workload type"],
    },
    "cs-cpu-scheduling": {
        "explanation": (
            "**FCFS (First Come First Served):** Simple queue; convoy effect if long job first.\n\n"
            "**SJF (Shortest Job First):** Minimizes average wait; can starve long jobs.\n\n"
            "**Round Robin:** Time quantum (e.g. 10ms); fair; good for time-sharing.\n\n"
            "**MLFQ:** Multiple queues with different priorities; aging prevents starvation."
        ),
        "code": """Round Robin example (quantum = 4ms):
  Queue: [P1(24ms), P2(3ms), P3(3ms)]
  P1 runs 4ms → back of queue
  P2 runs 3ms → done
  P3 runs 3ms → done
  P1 runs 4ms → ... until complete

Metrics:
  Turnaround time = completion - arrival
  Waiting time = turnaround - burst
  Response time = first run - arrival

Modern OS: CFS in Linux (fair proportional scheduling)""",
        "key_points": ["RR fair with time quantum", "SJF optimal avg wait", "Starvation via aging", "MLFQ multi-level"],
    },
    "cs-osi-tcpip": {
        "explanation": (
            "**OSI 7 layers:** Physical → Data Link → Network → Transport → Session → Presentation → Application.\n\n"
            "**TCP/IP 4 layers:** Network Access (link) → Internet (IP) → Transport (TCP/UDP) → Application (HTTP, DNS).\n\n"
            "**Interview mapping:** HTTP at application; TCP/UDP at transport; IP routing at network; Ethernet/WiFi at link."
        ),
        "code": """OSI vs TCP/IP:

OSI (7)              TCP/IP (4)        Examples
─────────────────────────────────────────────────
Application  ┐
Presentation ├──────► Application       HTTP, DNS, TLS
Session      ┘
Transport    ───────► Transport        TCP, UDP
Network      ───────► Internet         IP, ICMP
Data Link    ┐
Physical     ├──────► Network Access   Ethernet, WiFi
             ┘

Encapsulation:
  HTTP data → TCP segment → IP packet → Ethernet frame""",
        "key_points": ["HTTP = application layer", "TCP/UDP = transport", "IP = network routing", "Encapsulation at each layer"],
    },
    "cs-tcp-vs-udp": {
        "explanation": (
            "**TCP:** Connection-oriented, reliable, ordered delivery, congestion control, retransmission. "
            "Higher overhead. Used: HTTP, email, file transfer.\n\n"
            "**UDP:** Connectionless, no guarantee of delivery/order, low latency, no congestion control. "
            "Used: DNS, video streaming, gaming, VoIP, QUIC foundation."
        ),
        "code": """TCP:
  - 3-way handshake (SYN, SYN-ACK, ACK)
  - Sequence numbers, ACKs, retransmit on loss
  - Flow control (window size)
  - Congestion control (slow start, AIMD)

UDP:
  - Send datagram, no connection
  - No ordering, no retransmit (app handles)
  - 8-byte header vs TCP 20+ bytes

Choose UDP when:
  - Loss tolerable (live video — skip frame)
  - Low latency critical (online game position)
  - DNS query (single request/response)""",
        "key_points": ["TCP reliable ordered", "UDP fast connectionless", "QUIC = UDP + reliability in user space"],
    },
    "cs-http-versions": {
        "explanation": (
            "**HTTP/1.1:** Persistent connections but head-of-line blocking — one request at a time per connection (pipelining rarely used).\n\n"
            "**HTTP/2:** Multiplexed streams on one TCP connection, header compression (HPACK), binary framing, server push.\n\n"
            "**HTTP/3:** QUIC over UDP — eliminates TCP head-of-line blocking, faster connection setup (0-RTT)."
        ),
        "code": """HTTP/1.1 problem:
  Request 1 (large) blocks Request 2 on same connection

HTTP/2:
  One TCP connection
  Stream 1: GET /api/users
  Stream 3: GET /api/orders   ← parallel
  Stream 5: GET /style.css

HTTP/3 (QUIC):
  UDP-based, each stream independent
  Connection migration (WiFi → 4G keeps session)
  Built-in TLS 1.3

All use same semantics (methods, status codes, headers)""",
        "key_points": ["H2 multiplexing fixes H1 blocking", "H3 QUIC over UDP", "Same REST semantics across versions"],
    },
    "cs-tls-handshake": {
        "explanation": (
            "**TLS** encrypts HTTP into HTTPS. **TLS 1.3** handshake: ~1 RTT (or 0-RTT resumption).\n\n"
            "**Steps:** ClientHello (cipher suites) → ServerHello + certificate → key exchange → "
            "both derive session keys → encrypted Application Data.\n\n"
            "**Certificate:** Server proves identity via CA-signed cert; client validates chain."
        ),
        "code": """TLS 1.3 handshake (simplified):

Client                          Server
  │── ClientHello (key share) ──►│
  │◄─ ServerHello + cert + share ─│
  │── Finished (encrypted) ─────►│
  │◄─ Finished (encrypted) ───────│
  │══ Encrypted HTTP traffic ═════│

Client validates:
  - Cert not expired
  - Hostname matches (SAN)
  - Signed by trusted CA
  - Not revoked (OCSP)

Forward secrecy: ephemeral keys — past sessions safe if cert stolen""",
        "key_points": ["TLS 1.3 ~1 RTT", "Certificate chain validation", "Forward secrecy with ephemeral keys"],
    },
    "cs-dns": {
        "explanation": (
            "**DNS** resolves domain names to IP addresses.\n\n"
            "**Resolution order:** Browser cache → OS cache → resolver (ISP/8.8.8.8) → "
            "root server → TLD (.com) → authoritative nameserver.\n\n"
            "**Record types:** A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), TXT (verification)."
        ),
        "code": """Resolve www.example.com:

  1. Browser cache hit? → return IP
  2. OS cache (/etc/hosts, systemd-resolved)
  3. Recursive resolver (8.8.8.8)
     a. Root → .com TLD server
     b. TLD → example.com authoritative NS
     c. NS → A record 93.184.216.34
  4. Cache result (TTL e.g. 300s)

Load balancing:
  Multiple A records → client picks one (round robin)

CDN:
  CNAME www → d123.cloudfront.net (geo-routed)""",
        "key_points": ["Recursive resolver does the work", "TTL controls cache duration", "A vs CNAME vs MX"],
    },
    "cs-tcp-handshake": {
        "explanation": (
            "**Three-way handshake** establishes TCP connection:\n"
            "1. Client → SYN (seq=x)\n"
            "2. Server → SYN-ACK (seq=y, ack=x+1)\n"
            "3. Client → ACK (ack=y+1)\n\n"
            "**Why 3-way?** Both sides agree on initial sequence numbers; prevents stale duplicate SYN.\n\n"
            "**Teardown:** FIN-WAIT → CLOSE-WAIT → TIME-WAIT (2×MSL) ensures late packets don't confuse new connection."
        ),
        "code": """Three-way handshake:

Client                    Server
  │──── SYN seq=100 ────────►│
  │◄── SYN-ACK seq=300 ──────│  ack=101
  │──── ACK ack=301 ────────►│
  │════ DATA transfer ═══════│

TIME-WAIT (2×MSL ≈ 2-4 min):
  Client waits after close so late ACKs don't
  reset a new connection on same port

SYN flood attack:
  Mitigation: SYN cookies (server doesn't allocate
  state until final ACK)""",
        "key_points": ["SYN → SYN-ACK → ACK", "TIME-WAIT prevents confusion", "SYN cookies against flood"],
    },
    "cs-acid": {
        "explanation": (
            "**Atomicity:** All or nothing — transaction commits fully or rolls back entirely.\n\n"
            "**Consistency:** DB moves from one valid state to another (constraints satisfied).\n\n"
            "**Isolation:** Concurrent transactions don't interfere (isolation levels define how much).\n\n"
            "**Durability:** Committed data survives crash (WAL written to disk before ack)."
        ),
        "code": """Transfer $100 A → B:

BEGIN TRANSACTION
  UPDATE accounts SET balance = balance - 100 WHERE id = 'A';
  UPDATE accounts SET balance = balance + 100 WHERE id = 'B';
COMMIT;  -- both succeed or both rollback

Durability mechanism:
  Write-Ahead Log (WAL): log record to disk BEFORE
  applying change to data pages

If crash after COMMIT:
  Replay WAL on recovery → data intact

NoSQL trade-off:
  Some sacrifice ACID for availability/scale (BASE)""",
        "key_points": ["All-or-nothing atomicity", "WAL for durability", "Isolation levels vary", "BASE in some NoSQL"],
    },
    "cs-normalization": {
        "explanation": (
            "**1NF:** Atomic columns (no repeating groups); each cell single value.\n\n"
            "**2NF:** 1NF + no partial dependency on composite PK (non-key cols depend on full PK).\n\n"
            "**3NF:** 2NF + no transitive dependency (non-key col depends only on PK, not other non-key cols).\n\n"
            "**Denormalization:** Intentionally break normal form for read performance (reporting tables, caches)."
        ),
        "code": """Unnormalized:
  Orders(order_id, customer_name, customer_email, product, qty)
  ← customer data repeated per line item

3NF design:
  Customers(customer_id, name, email)
  Orders(order_id, customer_id, order_date)
  OrderItems(order_id, product_id, qty)
  Products(product_id, name, price)

Benefits: no update anomalies (change email once)
Cost: joins on read → denormalize for hot reads

BCNF: stricter — every determinant is a candidate key""",
        "key_points": ["1NF atomic", "2NF no partial deps", "3NF no transitive deps", "Denormalize for read perf"],
    },
    "cs-db-indexing": {
        "explanation": (
            "**Index** speeds lookups at cost of write overhead and storage.\n\n"
            "**B-tree (default):** Balanced tree; O(log n) seek; supports range queries (`WHERE age BETWEEN 20 AND 30`).\n\n"
            "**Hash index:** O(1) equality; no range scans.\n\n"
            "**Clustered index:** Data rows stored in index order (SQL Server PK). **Non-clustered:** separate structure with row pointer."
        ),
        "code": """B-tree index on last_name:

         [M]
        /   \\
     [D,H] [R,Z]
    / | \\  / | \\
  rows sorted under leaves → range scan efficient

CREATE INDEX IX_Orders_CustomerId ON Orders(CustomerId);

Covering index (avoid table lookup):
  CREATE INDEX IX ON Orders(CustomerId) INCLUDE (OrderDate, Total);
  → query satisfied entirely from index

When NOT to index:
  - Small tables (full scan faster)
  - High write / low read columns
  - Low cardinality (gender: M/F) — sometimes useless""",
        "language": "sql",
        "key_points": ["B-tree for range + equality", "Hash for equality only", "Covering index avoids lookup", "Write amplification"],
    },
    "cs-isolation-levels": {
        "explanation": (
            "**Read Uncommitted:** Dirty reads allowed (reads uncommitted data).\n\n"
            "**Read Committed:** Only committed data; non-repeatable reads possible (default SQL Server/PostgreSQL).\n\n"
            "**Repeatable Read:** Same row reads consistent within transaction; phantom rows possible.\n\n"
            "**Serializable:** Full isolation; slowest; prevents phantoms via range locks."
        ),
        "code": """Anomalies:
  Dirty read:     read uncommitted data (rolled back later)
  Non-repeatable: same query, different result (row updated)
  Phantom read:   same query, different rows (rows inserted)

SQL Server:
  SET TRANSACTION ISOLATION LEVEL READ COMMITTED;  -- default

PostgreSQL:
  READ COMMITTED (default)
  REPEATABLE READ uses snapshot isolation (no phantoms)

Choose:
  Reporting: READ COMMITTED OK
  Financial reconcile: SERIALIZABLE or explicit locks""",
        "language": "sql",
        "key_points": ["Higher isolation = fewer anomalies", "Serializable slowest", "PostgreSQL RR = snapshot"],
    },
    "cs-stack-vs-heap": {
        "explanation": (
            "**Stack:** LIFO; stores local variables, return addresses; fast allocation (pointer bump); "
            "automatic cleanup when function returns; limited size (stack overflow).\n\n"
            "**Heap:** Dynamic allocation (`new`, objects); managed by GC in .NET; slower; survives beyond function scope; fragmentation risk.\n\n"
            "**.NET:** Value types on stack (if local) or inline in object; reference types always on heap."
        ),
        "code": """void Example()
{
    int x = 10;              // stack (value type local)
    var list = new List<int>(); // ref on stack → object on heap
}

Stack frame:
  | return addr |
  | x = 10      |
  └─────────────┘

Heap:
  [List object][array backing store]

Stack overflow:
  Infinite recursion → StackOverflowException

Heap:
  OutOfMemoryException if GC can't satisfy alloc""",
        "language": "csharp",
        "key_points": ["Stack auto-managed LIFO", "Heap for dynamic lifetime", "Ref on stack, object on heap in .NET"],
    },
    "cs-garbage-collection": {
        "explanation": (
            "**.NET GC** is generational: Gen0 (short-lived), Gen1 (buffer), Gen2 (long-lived). "
            "Most objects die young — Gen0 collections frequent and fast.\n\n"
            "**Mark-and-sweep:** Mark reachable objects from roots; sweep unmarked; compact heap optionally.\n\n"
            "**`IDisposable`:** For unmanaged resources (files, DB connections) — deterministic cleanup via `using`."
        ),
        "code": """Generational GC:
  new object → Gen0
  Survives collection → promoted Gen1 → Gen2
  Gen2 collection = full GC (expensive pause)

using var conn = new SqlConnection(...);
// Dispose called at end of scope — deterministic

GC.Collect(); // rarely call — let GC decide

LOH (Large Object Heap):
  Objects ≥ 85KB → LOH (not compacted by default)

Monitor:
  dotnet-counters, App Insights GC metrics""",
        "language": "csharp",
        "key_points": ["Gen0/1/2 generational", "using for IDisposable", "LOH for large objects", "Avoid unnecessary GC.Collect"],
    },
    "cs-compiler-interpreter": {
        "explanation": (
            "**Compiler:** Translates entire source to machine code/binary ahead of time (C, Rust, Go). "
            "Fast runtime; slow build; platform-specific binary.\n\n"
            "**Interpreter:** Executes source line-by-line (early Python, bash). Slow runtime; no build step.\n\n"
            "**.NET hybrid:** C# → IL (compile) → CLR JIT compiles IL to native at runtime (.NET Native AOT precompiles)."
        ),
        "code": """Compilation pipeline (.NET):

  Program.cs ──Roslyn──► IL (DLL)
                           │
                      CLR JIT at runtime
                           │
                      Native machine code

JIT benefits:
  - Optimization based on actual runtime profile
  - Platform-specific code generation

AOT (.NET 8 Native AOT):
  IL → native at publish time
  Faster startup, no JIT, larger binary

Python: bytecode interpreter (CPython)
Java: bytecode + JVM JIT (similar to .NET)""",
        "key_points": [".NET = compile to IL + JIT", "Native AOT precompiles", "Interpreter slower per execution"],
    },
    "cs-cpu-cache": {
        "explanation": (
            "**CPU cache** (L1 ~1ns, L2, L3 ~10-40ns) is much faster than RAM (~100ns). "
            "Data fetched in **cache lines** (typically 64 bytes).\n\n"
            "**Spatial locality:** Sequential array access fast. **Temporal locality:** Reuse recently accessed data.\n\n"
            "**False sharing:** Two threads modify different vars on same cache line → cache line bounces between cores."
        ),
        "code": """Memory hierarchy:
  L1 cache  ~1 cycle
  L2 cache  ~10 cycles
  L3 cache  ~40 cycles
  RAM       ~100+ cycles
  SSD       ~100,000 cycles

Optimize:
  // Cache-friendly — sequential scan
  for (int i = 0; i < n; i++) sum += arr[i];

  // Cache-unfriendly — random access
  for (int i = 0; i < n; i++) sum += arr[random[i]];

False sharing fix:
  Pad struct fields to separate cache lines
  (high-perf concurrent counters)""",
        "key_points": ["64-byte cache lines", "Sequential access fast", "False sharing hurts multi-thread", "L1/L2/L3 hierarchy"],
    },
}
