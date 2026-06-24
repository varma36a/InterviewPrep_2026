"""Detailed content for market topics missing from primary market files."""

MARKET_DETAILED_GAPS: dict[str, dict] = {
    "bulk-insert-update": {
        "explanation": (
            "Standard `SaveChangesAsync()` sends **one SQL statement per entity**, which is too slow for thousands of records in batch imports or archival jobs. EF Core 7+ provides **`ExecuteUpdateAsync`** and **`ExecuteDeleteAsync`** for set-based updates and deletes **without loading entities** into memory. For large inserts, use **EFCore.BulkExtensions**, **SqlBulkCopy** (SQL Server), or **PostgreSQL COPY**. Bulk operations **bypass change tracking**, interceptors, and domain events — add compensating logic when side effects matter. **When** to use: mass status changes, log purges, ETL imports; **pitfall**: long transactions lock tables — batch in chunks and test on staging with production-scale volumes."
        ),
        "code": """// EF Core 7+ — bulk update without loading entities
var cancelled = await _db.Orders
    .Where(o => o.Status == OrderStatus.Pending && o.CreatedAt < cutoff)
    .ExecuteUpdateAsync(s => s
        .SetProperty(o => o.Status, OrderStatus.Cancelled)
        .SetProperty(o => o.UpdatedAt, DateTime.UtcNow));

// EF Core 7+ — bulk delete
var deleted = await _db.AuditLogs
    .Where(l => l.CreatedAt < retentionDate)
    .ExecuteDeleteAsync();

// Large insert — third-party BulkExtensions
await _db.BulkInsertAsync(orders, o => {
    o.BatchSize = 5000;
    o.SetOutputIdentity = true; // populate generated IDs
});""",
        "language": "csharp",
        "key_points": [
            "ExecuteUpdate/ExecuteDelete avoid entity loading (EF 7+)",
            "BulkExtensions or SqlBulkCopy for large inserts",
            "Bypasses change tracking, interceptors, and events",
            "Batch in chunks to reduce lock duration",
            "Always test with production-scale data volumes",
        ],
    },
    "change-tracking": {
        "explanation": (
            "EF Core **change tracking** monitors entity modifications through the **`ChangeTracker`**, which snapshots queried entities and compares current vs original values on **`SaveChangesAsync()`**. Tracked entities move through states: **Added**, **Modified**, **Deleted**, **Unchanged**, and **Detached**. **Why it matters**: only changed entities generate SQL, but tracking consumes memory on read-heavy paths. Use **`AsNoTracking()`** for read-only queries. **When** updating disconnected DTOs from APIs, **`Update()`** marks all properties Modified — watch for overwriting unchanged columns. **Pitfall**: long-lived DbContext instances accumulate tracked entities; scope per request."
        ),
        "code": """// Tracked query — EF watches for changes
var order = await _db.Orders.Include(o => o.Lines).FirstAsync(o => o.Id == 1);
order.Status = OrderStatus.Shipped; // automatically marked Modified
order.Lines.Add(new OrderLine { ProductId = 5, Qty = 2 }); // marked Added
await _db.SaveChangesAsync();

// Read-only — no tracking overhead
var summaries = await _db.Orders.AsNoTracking()
    .Select(o => new OrderSummary(o.Id, o.Total)).ToListAsync();

// Disconnected update from API payload
public async Task UpdateOrderAsync(OrderDto dto)
{
    var order = new Order { Id = dto.Id, Status = dto.Status };
    _db.Orders.Update(order); // marks all properties Modified
    await _db.SaveChangesAsync();
}""",
        "language": "csharp",
        "key_points": [
            "ChangeTracker monitors Added/Modified/Deleted/Unchanged",
            "AsNoTracking() for read-only queries — faster, less memory",
            "SaveChanges generates SQL only for changed entities",
            "Update() marks all properties Modified in disconnected scenarios",
            "Scope DbContext per request — avoid long-lived tracked graphs",
        ],
    },
    "compiled-queries": {
        "explanation": (
            "**Compiled queries** cache the LINQ expression tree translation so EF does not recompile the same query on every call. Define once with **`EF.CompileAsyncQuery`** or **`EF.CompileQuery`**, then invoke with the DbContext and parameters. **Why**: modest gain for simple queries but meaningful for **high-frequency hot paths** (auth checks, config lookups on every request). **How**: expression must be fixed — cannot compile queries with dynamic predicates. **When**: after profiling shows repeated query compilation cost. **Pitfall**: premature compiled queries add complexity without measurable gain."
        ),
        "code": """// Compile once — reuse across all requests
private static readonly Func<AppDbContext, int, Task<Order?>> GetOrderById =
    EF.CompileAsyncQuery((AppDbContext db, int id) =>
        db.Orders.AsNoTracking().FirstOrDefault(o => o.Id == id));

public async Task<Order?> GetOrderAsync(int id)
    => await GetOrderById(_db, id);

// Sync variant
private static readonly Func<AppDbContext, string, IEnumerable<Product>> GetByCategory =
    EF.CompileQuery((AppDbContext db, string category) =>
        db.Products.AsNoTracking().Where(p => p.Category == category));""",
        "language": "csharp",
        "key_points": [
            "EF.CompileAsyncQuery / CompileQuery — define once, reuse",
            "Best for high-frequency identical queries",
            "Expression must be fixed — no dynamic WHERE clauses",
            "Profile before optimizing — gain is modest for simple queries",
            "Works with AsNoTracking for read-only hot paths",
        ],
    },
    "connection-pooling": {
        "explanation": (
            "**Connection pooling** reuses open database connections instead of creating a new TCP connection per query. ADO.NET pools connections automatically when connection strings are identical. **Why**: connection setup (TLS, auth, session init) is expensive — pooling cuts latency dramatically under load. **How**: use **`Min Pool Size`** and **`Max Pool Size`** in the connection string; default max is 100 on SQL Server. **When**: always in production web APIs. **Pitfalls**: connection leaks (missing `Dispose`/`await using`) exhaust the pool causing timeouts; changing connection string attributes creates separate pools."
        ),
        "code": """// Connection string with explicit pool settings
"Server=sql.example.com;Database=Orders;User Id=app;Password=***;
 Min Pool Size=5;Max Pool Size=200;Connection Timeout=30;Pooling=true"

// Always dispose connections — EF Core handles this via DbContext
await using var conn = new SqlConnection(connectionString);
await conn.OpenAsync();
await using var cmd = new SqlCommand("SELECT COUNT(*) FROM Orders", conn);
var count = (int)(await cmd.ExecuteScalarAsync()!);

// Pool exhaustion symptom: "Timeout expired. The timeout period elapsed
// while attempting to consume the pre-login handshake acknowledgement"
// Fix: find leaked connections, increase Max Pool Size, or reduce concurrency""",
        "language": "csharp",
        "key_points": [
            "ADO.NET pools connections automatically with identical strings",
            "Min/Max Pool Size tune warm connections and ceiling",
            "Connection leaks exhaust the pool — always dispose",
            "Each unique connection string creates a separate pool",
            "Symptom of exhaustion: timeout during pre-login handshake",
        ],
    },
    "dbcontext-pooling": {
        "explanation": (
            "**DbContext pooling** (`AddDbContextPool`) reuses `DbContext` instances across requests, resetting internal state between uses. **Why**: avoids model compilation and service injection cost on every request. Default pool size is 1024. **Critical rule**: never store **per-request state** on the DbContext (fields, cached lists) — the instance is reused. **How**: register with `AddDbContextPool<AppDbContext>`. **When** you need scoped services in the context, use **`IDbContextFactory`** instead. **Pitfall**: injecting scoped services into DbContext constructor breaks pooling."
        ),
        "code": """// Register pooled context — faster than AddDbContext
builder.Services.AddDbContextPool<AppDbContext>(options =>
    options.UseSqlServer(connectionString),
    poolSize: 128);

public class AppDbContext : DbContext
{
    // BAD — state persists across requests with pooling!
    // private List<Order> _cachedOrders = [];

    // GOOD — stateless context, query per request
    public DbSet<Order> Orders => Set<Order>();
}

// When you need scoped services in context, use factory instead
builder.Services.AddDbContextFactory<AppDbContext>(options =>
    options.UseSqlServer(connectionString));""",
        "language": "csharp",
        "key_points": [
            "AddDbContextPool reuses instances — faster startup",
            "Never store per-request state on DbContext fields",
            "Default pool size 1024 — tune for your load",
            "Use IDbContextFactory when injecting scoped services",
            "Scoped DbContext per request still applies to usage pattern",
        ],
    },
    "global-query-filters": {
        "explanation": (
            "**Global query filters** automatically append predicates to every LINQ query for an entity type — commonly for **soft delete** (`IsDeleted == false`), **multi-tenancy** (`TenantId == currentTenant`), or **row-level security**. Configure in **`OnModelCreating`** with **`HasQueryFilter`**. **Why**: centralizes cross-cutting data rules so developers cannot forget the filter. **How**: access tenant ID via injected service in DbContext. **When**: tenant isolation and soft-delete are universal. **Pitfalls**: filters are silently applied — use **`IgnoreQueryFilters()`** for admin/reporting; raw SQL bypasses filters."
        ),
        "code": """public class AppDbContext : DbContext
{
    private readonly ITenantProvider _tenant;

    public AppDbContext(DbContextOptions<AppDbContext> options, ITenantProvider tenant)
        : base(options) => _tenant = tenant;

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Order>().HasQueryFilter(o =>
            !o.IsDeleted && o.TenantId == _tenant.CurrentTenantId);
    }
}

// Normal query — filter applied automatically
var orders = await _db.Orders.ToListAsync();

// Admin view — bypass filter explicitly
var allOrders = await _db.Orders.IgnoreQueryFilters().ToListAsync();""",
        "language": "csharp",
        "key_points": [
            "HasQueryFilter in OnModelCreating — automatic predicate",
            "Common uses: soft delete, multi-tenancy, active records",
            "IgnoreQueryFilters() for admin and reporting queries",
            "Raw SQL and FromSqlRaw bypass global filters",
            "Inject tenant context via DbContext constructor",
        ],
    },
    "index-strategies": {
        "explanation": (
            "**Index strategies** determine how quickly the database finds rows. **Clustered index** defines physical row order (one per table — usually primary key). **Non-clustered indexes** are separate B-tree structures for lookup columns. **Covering indexes** include all queried columns to avoid **key lookups**. **Why**: missing indexes cause table scans; too many indexes slow writes. **How**: index foreign keys, WHERE/JOIN columns, and ORDER BY columns used together. **Pitfall**: over-indexing every column hurts INSERT/UPDATE throughput — profile with execution plans before adding indexes."
        ),
        "code": """-- Non-clustered index on frequently filtered column
CREATE NONCLUSTERED INDEX IX_Orders_Status_CreatedAt
ON Orders (Status, CreatedAt DESC)
INCLUDE (CustomerId, Total);  -- covering index avoids key lookup

-- Filtered index — smaller, faster for partial queries
CREATE NONCLUSTERED INDEX IX_Orders_Active
ON Orders (CustomerId, OrderDate)
WHERE IsDeleted = 0;

-- EF Core Fluent API
modelBuilder.Entity<Order>()
    .HasIndex(o => new { o.Status, o.CreatedAt })
    .HasDatabaseName("IX_Orders_Status_CreatedAt");""",
        "language": "sql",
        "key_points": [
            "Clustered index = physical order; one per table",
            "Index FK columns and frequent WHERE/JOIN predicates",
            "INCLUDE columns for covering indexes — avoid key lookups",
            "Filtered indexes for partial queries (e.g., IsDeleted = 0)",
            "Too many indexes slow writes — profile before adding",
        ],
    },
    "isolation-levels": {
        "explanation": (
            "**Transaction isolation levels** control how concurrent transactions see each other's uncommitted changes. **Read Uncommitted** allows dirty reads; **Read Committed** (SQL Server default) prevents dirty reads; **Repeatable Read** prevents non-repeatable reads; **Serializable** prevents phantoms but locks heavily. **Snapshot** uses row versioning for consistent reads without shared locks. **Why**: higher isolation prevents anomalies but reduces concurrency. **How**: set via `IsolationLevel` in EF Core transactions. **When**: use Snapshot for long-running reports; Serializable for financial reconciliation. **Pitfall**: default Read Committed may still cause lost updates — use optimistic concurrency (`RowVersion`)."
        ),
        "code": """// Explicit isolation level in EF Core
await using var tx = await _db.Database.BeginTransactionAsync(
    System.Data.IsolationLevel.Snapshot);

try
{
    var balance = await _db.Accounts.FirstAsync(a => a.Id == accountId);
    balance.Amount -= transferAmount;
    await _db.SaveChangesAsync();
    await tx.CommitAsync();
}
catch
{
    await tx.RollbackAsync();
    throw;
}

// Optimistic concurrency — RowVersion column
public class Order
{
    public int Id { get; set; }
    [Timestamp]
    public byte[] RowVersion { get; set; } = null!;
}""",
        "language": "csharp",
        "key_points": [
            "Read Committed is SQL Server default — no dirty reads",
            "Snapshot isolation uses row versioning — good for reports",
            "Serializable prevents phantoms but hurts concurrency",
            "Use RowVersion for optimistic concurrency on hot rows",
            "Higher isolation = fewer anomalies, more locking",
        ],
    },
    "migration-strategy": {
        "explanation": (
            "An EF Core **migration strategy** defines how schema changes ship safely across environments. **How**: generate migrations with `dotnet ef migrations add`, apply via **`dotnet ef database update`** in CI/CD — never auto-migrate production on app startup. **Why**: idempotent scripts in pipelines give auditability and rollback options. **Zero-downtime pattern**: expand-contract — add nullable column, deploy dual-write code, backfill, then drop old column. **When**: every schema change in team environments. **Pitfalls**: editing applied migrations breaks history; destructive changes without backups cause outages."
        ),
        "code": """# CI/CD pipeline step — apply migrations
dotnet ef database update --project OrderApi --connection "$(SqlConnection)"

// Dev only — auto-migrate on startup (NEVER in production)
if (app.Environment.IsDevelopment())
    await scope.ServiceProvider.GetRequiredService<AppDbContext>()
        .Database.MigrateAsync();

# Zero-downtime expand-contract:
# 1. ADD Column NewStatus NVARCHAR(20) NULL
# 2. Deploy app writing to both old and new columns
# 3. Backfill: UPDATE Orders SET NewStatus = Status WHERE NewStatus IS NULL
# 4. ALTER COLUMN NewStatus NOT NULL; drop old column""",
        "language": "csharp",
        "key_points": [
            "Apply migrations in CI/CD — not on production startup",
            "Expand-contract pattern for zero-downtime schema changes",
            "Never edit already-applied migration files",
            "Idempotent scripts safe to re-run in pipelines",
            "Always backup before destructive migrations",
        ],
    },
    "owned-entity-types": {
        "explanation": (
            "**Owned entity types** model value objects that belong exclusively to one parent entity — no independent identity or table lifecycle. EF maps them to **separate columns** in the parent table or a **dedicated owned table** with a shadow FK. **Why**: encapsulates concepts like Address, Money, or Dimensions without polluting the parent with flat columns. **How**: configure with **`OwnsOne`** or **`OwnsMany`** in Fluent API. **When**: DDD value objects, embedded aggregates. **Pitfalls**: owned entities cannot be queried directly as root entities; changing ownership requires careful migration."
        ),
        "code": """public class Order
{
    public int Id { get; set; }
    public Address ShippingAddress { get; set; } = null!;
}

public class Address  // value object — no own Id
{
    public string Street { get; set; } = "";
    public string City { get; set; } = "";
    public string PostalCode { get; set; } = "";
}

// Fluent API
modelBuilder.Entity<Order>().OwnsOne(o => o.ShippingAddress, a =>
{
    a.Property(p => p.Street).HasColumnName("ShipStreet");
    a.Property(p => p.City).HasColumnName("ShipCity");
});""",
        "language": "csharp",
        "key_points": [
            "OwnsOne/OwnsMany for value objects without independent identity",
            "Mapped to parent table columns or dedicated owned table",
            "Cannot query owned type as root DbSet",
            "Good for Address, Money, Dimensions patterns",
            "Use Fluent API for column naming in shared tables",
        ],
    },
    "pagination-strategies": {
        "explanation": (
            "**Pagination strategies** limit result sets for APIs and UI lists. **Offset pagination** (`Skip/Take` or `LIMIT/OFFSET`) is simple but **degrades on large offsets** — page 10,000 scans 100,000 rows. **Keyset (cursor) pagination** uses the last seen sort key (`WHERE Id > @cursor ORDER BY Id LIMIT 20`) and scales consistently. **Why**: prevents memory exhaustion and slow queries on large tables. **How**: return `nextCursor` in API responses. **When**: cursor for infinite scroll and large datasets; offset for admin pages with jump-to-page. **Pitfall**: cursor pagination requires stable sort keys."
        ),
        "code": """// Offset — simple but slow at high page numbers
var page = 3; var pageSize = 20;
var offsetPage = await _db.Orders.AsNoTracking()
    .OrderByDescending(o => o.CreatedAt)
    .Skip((page - 1) * pageSize).Take(pageSize)
    .ToListAsync();

// Keyset cursor — scalable
public async Task<PagedResult<OrderDto>> GetOrdersAsync(int? cursorId, int pageSize = 20)
{
    var query = _db.Orders.AsNoTracking().OrderByDescending(o => o.Id);
    if (cursorId.HasValue)
        query = (IOrderedQueryable<Order>)query.Where(o => o.Id < cursorId.Value);

    var items = await query.Take(pageSize + 1).ToListAsync();
    var hasMore = items.Count > pageSize;
    if (hasMore) items.RemoveAt(items.Count - 1);
    return new PagedResult(items, hasMore ? items.Last().Id : null);
}""",
        "language": "csharp",
        "key_points": [
            "Offset Skip/Take simple but slow at high page numbers",
            "Keyset cursor pagination scales — WHERE Id > cursor",
            "Return nextCursor token in API responses",
            "Require stable sort key for cursor pagination",
            "Avoid SELECT COUNT(*) on huge tables for total pages",
        ],
    },
    "query-execution-plans": {
        "explanation": (
            "A **query execution plan** shows how the database engine executes a query — operators, join types, index usage, and estimated vs actual row counts. **Why**: essential for performance troubleshooting. Look for **Index Seek** (good) vs **Index Scan** or **Table Scan** (bad on large tables). **Key Lookup** means the index does not cover all columns. **How**: enable EF Core SQL logging in Development; use SSMS **Actual Execution Plan** (Ctrl+M). **When**: any slow query investigation. **Pitfall**: large estimated vs actual row mismatch indicates **stale statistics** — run `UPDATE STATISTICS`."
        ),
        "code": """// Enable EF Core SQL logging in Development
builder.Services.AddDbContext<AppDbContext>(options =>
{
    options.UseSqlServer(connectionString)
        .LogTo(Console.WriteLine, LogLevel.Information)
        .EnableSensitiveDataLogging(); // dev only!
});

-- SQL Server — actual execution plan
SET STATISTICS IO ON;
SELECT o.Id, o.Total, c.Name
FROM Orders o
INNER JOIN Customers c ON c.Id = o.CustomerId
WHERE o.Status = 'Pending' AND o.Total > 100;
-- Look for: Index Seek (good) vs Scan (bad)
UPDATE STATISTICS Orders;""",
        "language": "sql",
        "key_points": [
            "Index Seek good; Table/Index Scan on large tables bad",
            "Estimated vs actual row mismatch = stale statistics",
            "EF Core LogTo in Development captures generated SQL",
            "Covering indexes eliminate Key Lookup operations",
            "Compare estimated vs actual rows in execution plan",
        ],
    },
    "raw-sql-ef": {
        "explanation": (
            "EF Core supports **raw SQL** for queries EF cannot translate or for DBA-optimized SQL. **`FromSqlRaw`** executes SELECT against a `DbSet` — returned entities are tracked by default. **`ExecuteSqlRawAsync`** runs INSERT/UPDATE/DELETE without returning entities. **Why**: use when LINQ generates suboptimal SQL or for database-specific features. **How**: always use **parameter placeholders** (`{0}`, `{1}`) — never string interpolation. **When**: complex reports, hints, bulk ops. **Pitfall**: raw SQL bypasses global query filters unless you include filter conditions manually."
        ),
        "code": """// Raw query returning entities (must match entity shape)
var orders = await _db.Orders
    .FromSqlRaw("SELECT * FROM Orders WHERE CustomerId = {0} AND Total > {1}",
        customerId, minTotal)
    .AsNoTracking()
    .ToListAsync();

// Raw command — no return value
var rowsAffected = await _db.Database.ExecuteSqlRawAsync(
    "UPDATE Orders SET Status = {0} WHERE CreatedAt < {1}",
    "Cancelled", cutoffDate);

// EF 8+ — arbitrary result type
var stats = await _db.Database
    .SqlQuery<DepartmentStats>(
        "SELECT Department, COUNT(*) AS HeadCount FROM Employees GROUP BY Department")
    .ToListAsync();""",
        "language": "csharp",
        "key_points": [
            "FromSqlRaw for SELECT returning entities",
            "ExecuteSqlRawAsync for INSERT/UPDATE/DELETE",
            "Always use {0} placeholders — never string interpolation",
            "SqlQuery<T> (EF 8+) for arbitrary result shapes",
            "Raw SQL bypasses global query filters by default",
        ],
    },
    "soft-delete-pattern": {
        "explanation": (
            "The **soft delete pattern** marks records as deleted with a flag (`IsDeleted`, `DeletedAt`) instead of physically removing rows. **Why**: preserves audit history, supports undo, and maintains FK integrity. **How**: combine a **`HasQueryFilter(o => !o.IsDeleted)`** global filter with an interceptor or override `SaveChanges` to set the flag on delete. **When**: business data with compliance or recovery requirements. **Pitfall**: unique constraints must account for soft-deleted rows (filtered unique index); use **`IgnoreQueryFilters()`** for admin restore views."
        ),
        "code": """public class Order
{
    public int Id { get; set; }
    public bool IsDeleted { get; set; }
    public DateTime? DeletedAt { get; set; }
}

// Global filter — deleted rows invisible by default
modelBuilder.Entity<Order>().HasQueryFilter(o => !o.IsDeleted);

// Soft delete instead of physical remove
public async Task DeleteOrderAsync(int id)
{
    var order = await _db.Orders.FindAsync(id);
    order!.IsDeleted = true;
    order.DeletedAt = DateTime.UtcNow;
    await _db.SaveChangesAsync();
}

// Filtered unique index — allow reuse of email after soft delete
// CREATE UNIQUE INDEX IX_Users_Email ON Users(Email) WHERE IsDeleted = 0""",
        "language": "csharp",
        "key_points": [
            "IsDeleted/DeletedAt flag instead of DELETE statement",
            "Global query filter hides soft-deleted rows automatically",
            "Filtered unique indexes allow reuse after soft delete",
            "IgnoreQueryFilters() for admin restore and audit views",
            "Override SaveChanges or use interceptor for consistent deletes",
        ],
    },
    "stored-procedures": {
        "explanation": (
            "**Stored procedures** are precompiled SQL routines in the database — useful for complex reporting, legacy integration, and performance-critical batch operations. EF Core maps them via **`FromSqlRaw`** on a `DbSet` or **`ExecuteSqlRawAsync`** for non-query procs. **Why**: DBA-tuned plans, centralized business logic in DB-centric architectures. **How**: use parameters to prevent injection. **When**: complex multi-step DB logic, legacy systems. **Pitfall**: business logic in procs is harder to test, version, and deploy — prefer application layer unless performance demands it."
        ),
        "code": """// Map stored procedure returning entities
var orders = await _db.Orders
    .FromSqlRaw("EXEC usp_GetOrdersByCustomer @CustomerId = {0}, @MinTotal = {1}",
        customerId, minTotal)
    .AsNoTracking()
    .ToListAsync();

// Execute non-query stored procedure
await _db.Database.ExecuteSqlRawAsync(
    "EXEC usp_ArchiveOrders @CutoffDate = {0}", cutoffDate);

-- SQL Server stored procedure example
CREATE PROCEDURE usp_GetOrdersByCustomer
    @CustomerId INT, @MinTotal DECIMAL(18,2)
AS
    SELECT * FROM Orders
    WHERE CustomerId = @CustomerId AND Total >= @MinTotal AND IsDeleted = 0;""",
        "language": "csharp",
        "key_points": [
            "FromSqlRaw with EXEC for result-set procedures",
            "ExecuteSqlRawAsync for non-query procedures",
            "Always parameterize — never concatenate user input",
            "Harder to unit test than application-layer logic",
            "Good for DBA-optimized reporting and legacy integration",
        ],
    },
    "value-converters": {
        "explanation": (
            "**Value converters** in EF Core map between a CLR type and the database column type. Built-in converters handle enums-to-string, bool-to-int, etc. **Custom converters** implement **`ValueConverter<TModel,TProvider>`** for encryption, JSON serialization, or domain-specific types. **Why**: keep rich domain types in C# while storing efficient DB representations. **How**: configure with **`HasConversion`** in Fluent API or attributes. **When**: enum as string, encrypted columns, Value Objects. **Pitfall**: null handling must be explicit; querying converted columns may not translate to SQL efficiently."
        ),
        "code": """// Enum stored as string — readable in DB
modelBuilder.Entity<Order>()
    .Property(o => o.Status)
    .HasConversion<string>();

// Custom converter — encrypt sensitive data
public class EncryptedStringConverter(IEncryptionService crypto)
    : ValueConverter<string, string>(
        v => crypto.Encrypt(v),
        v => crypto.Decrypt(v));

modelBuilder.Entity<Customer>()
    .Property(c => c.Ssn)
    .HasConversion(new EncryptedStringConverter(crypto));

// JSON column via System.Text.Json
modelBuilder.Entity<Order>()
    .Property(o => o.Metadata)
    .HasConversion(
        v => JsonSerializer.Serialize(v, (JsonSerializerOptions?)null),
        v => JsonSerializer.Deserialize<OrderMetadata>(v, (JsonSerializerOptions?)null)!);""",
        "language": "csharp",
        "key_points": [
            "HasConversion maps CLR type to DB column type",
            "Built-in enum-to-string is most common pattern",
            "Custom converters for encryption, JSON, value objects",
            "Handle null explicitly for nullable properties",
            "Some conversions prevent efficient SQL translation",
        ],
    },
    "window-functions": {
        "explanation": (
            "**Window functions** perform calculations across a set of rows related to the current row without collapsing groups like `GROUP BY`. **`ROW_NUMBER()`** assigns unique sequential numbers; **`RANK()`** allows ties with gaps; **`DENSE_RANK()`** allows ties without gaps. **`PARTITION BY`** defines window groups; **`ORDER BY`** defines ordering within the window. **Why**: top-N per group, running totals, deduplication. **When**: analytics queries EF cannot express cleanly. **Pitfall**: EF Core 8+ translates some window functions; complex ones need raw SQL."
        ),
        "code": """-- Top 3 orders per customer by total
WITH RankedOrders AS (
    SELECT Id, CustomerId, Total,
        ROW_NUMBER() OVER (
            PARTITION BY CustomerId ORDER BY Total DESC
        ) AS RowNum
    FROM Orders WHERE IsDeleted = 0
)
SELECT Id, CustomerId, Total FROM RankedOrders WHERE RowNum <= 3;

-- Running total per customer
SELECT Id, CustomerId, Total,
    SUM(Total) OVER (PARTITION BY CustomerId ORDER BY OrderDate) AS RunningTotal
FROM Orders;""",
        "language": "sql",
        "key_points": [
            "ROW_NUMBER — unique; RANK/DENSE_RANK allow ties",
            "PARTITION BY defines window groups",
            "Top-N per group is the classic interview pattern",
            "Running totals use SUM() OVER (ORDER BY ...)",
            "Complex window functions often need raw SQL in EF Core",
        ],
    },
    "agile-scrum": {
        "explanation": (
            "**Agile** values working software, customer collaboration, and responding to change over rigid plans. **Scrum** is a framework with **Sprints** (1–4 weeks, usually 2) delivering fixed increments. **Ceremonies**: Sprint Planning, Daily Standup (15 min), Sprint Review, Retrospective. **Artifacts**: Product Backlog, Sprint Backlog, Increment. **Roles**: Product Owner (what), Scrum Master (process), Development Team (how). **Why**: predictable delivery with feedback loops. **Pitfall**: skipping retrospectives or overloading sprints without a clear Definition of Done erodes quality."
        ),
        "code": """/*
  Sprint timeline (2 weeks):
  Day 1:  Sprint Planning — select stories, define sprint goal
  Daily:  Standup 15 min — yesterday / today / blockers
  Day 10: Sprint Review — demo increment to stakeholders
  Day 10: Retrospective — Start/Stop/Continue

  User Story: "As a customer, I want to cancel my order within 30 minutes,
               so that I can change my mind before shipping."

  Definition of Done:
  □ Code complete + peer reviewed
  □ Unit tests passing
  □ Deployed to staging
  □ Acceptance criteria met
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
    "api-security-best-practices": {
        "explanation": (
            "**API security** layers defense across transport, authentication, authorization, and input handling. Use **HTTPS/TLS 1.2+**, validate **JWT issuer/audience/expiry**, enforce **RBAC policies**, **rate limiting**, and **CORS allowlists** (never wildcard with credentials). **Why**: APIs are primary attack surface. **How**: security headers (HSTS, X-Content-Type-Options), secrets in Key Vault, structured audit logging without tokens. **When**: every production endpoint. **Pitfall**: returning stack traces in errors and logging PII or bearer tokens."
        ),
        "code": """builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(o =>
    {
        o.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true, ValidateAudience = true,
            ValidateLifetime = true, ValidateIssuerSigningKey = true,
            ClockSkew = TimeSpan.FromMinutes(1)
        };
    });

builder.Services.AddRateLimiter(o => o.AddFixedWindowLimiter("api", f =>
{
    f.Window = TimeSpan.FromMinutes(1);
    f.PermitLimit = 100;
}));

app.UseHsts(); app.UseHttpsRedirection();
app.UseAuthentication(); app.UseAuthorization(); app.UseRateLimiter();
app.UseCors(p => p.WithOrigins("https://app.example.com").AllowAnyHeader());""",
        "language": "csharp",
        "key_points": [
            "HTTPS everywhere; HSTS in production",
            "Validate JWT fully — issuer, audience, expiry",
            "Rate limiting prevents abuse and DoS",
            "CORS allowlist — not wildcard in prod",
            "Never log tokens, passwords, or unnecessary PII",
        ],
    },
    "blue-green-deployment": {
        "explanation": (
            "**Blue-green deployment** maintains two identical production environments. **Blue** serves live traffic; deploy the new version to **Green**, run smoke tests, then **switch traffic** instantly. **Why**: zero-downtime deploys with rollback in seconds (switch back). **How**: Azure **App Service deployment slots**, AKS with two deployments, or Front Door origin switch. **When**: production APIs requiring instant rollback. **Pitfall**: both versions may run briefly — database migrations must be **backward compatible** (expand-contract pattern)."
        ),
        "code": """# Azure App Service blue-green with slots
az webapp deployment source config-zip \
  --name order-api --slot staging --src ./publish.zip

curl -f https://order-api-staging.azurewebsites.net/health

# Swap — instant traffic switch
az webapp deployment slot swap \
  --name order-api --slot staging --target-slot production

# Rollback — swap again (seconds)
az webapp deployment slot swap --name order-api --slot staging""",
        "language": "bash",
        "key_points": [
            "Two identical environments — instant traffic switch",
            "App Service slots are built-in blue-green",
            "Smoke test green before swap",
            "Rollback is another swap — seconds not hours",
            "DB migrations must be backward compatible",
        ],
    },
    "caching-strategies": {
        "explanation": (
            "Common **caching strategies** trade freshness for speed. **Cache-aside (lazy loading)** — app checks cache, on miss reads DB and populates; most common. **Read-through** — cache layer loads from DB transparently. **Write-through** — write cache and DB synchronously. **Write-behind** — write cache first, async flush (risky). **Why**: reduce DB load and latency. **How**: TTL on all keys, invalidate on writes. **Pitfall**: **cache stampede** when many requests miss simultaneously — use locking or staggered expiration."
        ),
        "code": """public async Task<OrderDto?> GetOrderAsync(int id, CancellationToken ct)
{
    var key = $"order:{id}";
    var cached = await _cache.GetStringAsync(key, ct);
    if (cached is not null)
        return JsonSerializer.Deserialize<OrderDto>(cached);

    var order = await _db.Orders.AsNoTracking()
        .Where(o => o.Id == id)
        .Select(o => new OrderDto(o.Id, o.CustomerName, o.Total))
        .FirstOrDefaultAsync(ct);

    if (order is not null)
        await _cache.SetStringAsync(key, JsonSerializer.Serialize(order),
            new DistributedCacheEntryOptions {
                AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5) }, ct);
    return order;
}""",
        "language": "csharp",
        "key_points": [
            "Cache-aside most common — app manages cache lifecycle",
            "Always set TTL to prevent unbounded growth",
            "Invalidate or update cache on writes",
            "Redis for multi-instance; IMemoryCache for single node",
            "Cache stampede: lock or stagger expiration",
        ],
    },
    "canary-releases": {
        "explanation": (
            "**Canary releases** route a **small percentage of traffic** to the new version while the majority stays on stable. **Why**: limits blast radius — detect problems before full rollout. **How**: monitor error rate, latency, and business metrics; gradually increase (5% → 25% → 100%) or auto-rollback on SLO breach. Implement via **Front Door weighted routing**, Istio in AKS, or **feature flags** at app level. **When**: high-risk changes to payment or checkout flows. **Pitfall**: canary metrics must compare against stable baseline, not absolute thresholds alone."
        ),
        "code": """[HttpPost("checkout")]
public async Task<IActionResult> Checkout([FromBody] CheckoutDto dto)
{
    var useV2 = await _featureManager.IsEnabledAsync("CheckoutV2");
    var sw = Stopwatch.StartNew();
    try
    {
        var result = useV2
            ? await _checkoutV2.ProcessAsync(dto)
            : await _checkoutV1.ProcessAsync(dto);
        _metrics.Record("checkout.success", 1,
            new TagList { { "version", useV2 ? "v2" : "v1" } });
        return Ok(result);
    }
    finally
    {
        _metrics.Record("checkout.duration_ms", sw.ElapsedMilliseconds,
            new TagList { { "version", useV2 ? "v2" : "v1" } });
    }
}
// Infrastructure: Front Door origin weights 95/5""",
        "language": "csharp",
        "key_points": [
            "Small traffic percentage limits blast radius",
            "Monitor golden signals on canary vs stable",
            "Automated rollback on SLO breach",
            "Feature flags OR traffic routing — both valid",
            "Combine with blue-green for infra-level canary",
        ],
    },
    "cap-theorem": {
        "explanation": (
            "The **CAP theorem** states a distributed system during a **network partition** must choose between **Consistency** (all nodes see same data) and **Availability** (every request gets a response). **Partition tolerance** is non-negotiable in cloud systems — networks fail. **CP systems** (Azure SQL) may reject writes during partition; **AP systems** (Cosmos DB eventual consistency) stay available but reads may be stale. **PACELC** extends: else choose Latency vs Consistency. **Interview tip**: justify consistency choice — payments need CP; product catalog tolerates AP."
        ),
        "code": """/*
  Payment service (CP):
  - Strong consistency — never double-charge
  - Azure SQL + RowVersion optimistic concurrency

  Product catalog (AP):
  - Eventual consistency OK — stale price 30s acceptable
  - Cosmos DB + Redis cache

  Partition scenario:
  East/West lose network link
  CP: one side stops writes (split-brain prevention)
  AP: both accept writes → conflict resolution needed
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
    "circuit-breaker-pattern": {
        "explanation": (
            "The **Circuit Breaker** prevents cascading failures when a downstream dependency is unhealthy. States: **Closed** (normal), **Open** (fail fast — don't call failing service), **Half-Open** (probe with limited requests to test recovery). **Why**: protects your service from wasting threads on doomed calls. **How**: after N failures, open circuit for cooldown. **When**: external HTTP APIs, payment gateways. **Pitfall**: combine with timeout and retry — retry only when circuit is closed."
        ),
        "code": """builder.Services.AddHttpClient<IPaymentGateway, StripeGateway>()
    .AddResilienceHandler("stripe", builder =>
    {
        builder.AddCircuitBreaker(new CircuitBreakerStrategyOptions<HttpResponseMessage>
        {
            FailureRatio = 0.5,
            MinimumThroughput = 10,
            BreakDuration = TimeSpan.FromSeconds(30),
            ShouldHandle = new PredicateBuilder<HttpResponseMessage>()
                .HandleResult(r => (int)r.StatusCode >= 500)
        });
        builder.AddTimeout(TimeSpan.FromSeconds(10));
    });
// When open — return fallback or cached response""",
        "language": "csharp",
        "key_points": [
            "Closed → Open → Half-Open state machine",
            "Fail fast when dependency is down",
            "Combine circuit breaker + retry + timeout",
            "Polly v8 ResiliencePipeline in .NET 8",
            "Return graceful degradation when circuit open",
        ],
    },
    "code-review-best-practices": {
        "explanation": (
            "Effective **code reviews** improve quality, spread knowledge, and catch bugs early. **Authors**: keep PRs small (< 400 lines), self-review first, link work items. **Reviewers**: check correctness, security, tests, naming — not bike-shedding style. **Why**: cheapest defect detection before production. **How**: automated checks (linters, SAST, tests) so humans focus on design. **When**: every merge to main. **Pitfall**: rubber-stamping or blocking on formatting that linters should handle."
        ),
        "code": """/*
  PR Description:
  ## What — Add order cancellation endpoint
  ## Why — Closes #1042
  ## How to test — POST /api/v1/orders/42/cancel

  Reviewer checklist:
  □ Authorization — can user cancel this order?
  □ Tests cover happy path + edge cases?
  □ Database migration backward compatible?
  □ No secrets in code?

  Feedback: suggest, don't demand (unless blocking)
  ✅ "Extract validation to OrderValidator — reused in PlaceOrder"
  ❌ "Wrong indentation" (let linter handle)
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
    "feature-flags": {
        "explanation": (
            "**Feature flags (feature toggles)** decouple **deployment from release** — ship code dark, enable when ready. **Why**: gradual rollout, A/B testing, kill switches, tenant-specific features. **How**: **Microsoft.FeatureManagement** with ASP.NET Core and **Azure App Configuration** for dynamic flags without redeploy. **When**: risky features, canary at app level. **Pitfall**: stale flags accumulate technical debt — remove after 100% rollout."
        ),
        "code": """builder.Services.AddFeatureManagement(builder.Configuration);

[FeatureGate("BetaCheckout")]
[HttpPost("checkout/v2")]
public async Task<IActionResult> CheckoutV2([FromBody] CheckoutDto dto)
    => Ok(await _checkoutV2.ProcessAsync(dto));

// appsettings.json
// "FeatureManagement": { "BetaCheckout": true }

// Azure App Configuration — refresh without restart
builder.Configuration.AddAzureAppConfiguration(o =>
    o.Connect(connStr).UseFeatureFlags());""",
        "language": "csharp",
        "key_points": [
            "Decouple deploy from release",
            "Percentage rollout for canary at app level",
            "Azure App Configuration for centralized management",
            "Kill switch disables bad features instantly",
            "Remove flags after 100% rollout — avoid debt",
        ],
    },
    "git-workflow": {
        "explanation": (
            "**Trunk-based development** merges small changes to `main` frequently via short-lived branches (< 2 days). **GitFlow** uses long-lived `develop`, `release/*`, `hotfix/*` — suits scheduled releases but slower feedback. **GitHub Flow** is simpler: main + feature branches + PR. **Why**: workflow choice affects CI/CD speed. **How**: branch policies — require PR reviews, passing builds, no direct push to main. **Pitfall**: long-lived feature branches cause painful merge conflicts."
        ),
        "code": """# Trunk-based (recommended for CI/CD)
git checkout main && git pull
git checkout -b feat/order-cancel
git commit -m "feat(orders): add cancel endpoint"
git push -u origin feat/order-cancel
gh pr create --title "Add order cancel endpoint"

# Conventional commits: feat|fix|refactor(scope): message

# GitFlow: feature → develop → release/1.4 → main + develop""",
        "language": "bash",
        "key_points": [
            "Trunk-based enables continuous delivery",
            "Short-lived branches (< 2 days) reduce merge pain",
            "Protect main with branch policies and required reviews",
            "GitFlow for scheduled release trains",
            "Conventional commits for automated changelogs",
        ],
    },
    "idempotency": {
        "explanation": (
            "**Idempotency** means performing the same operation multiple times produces the same result as once. **Why**: critical for HTTP retries, message queue consumers (at-least-once delivery), and webhooks. GET, PUT, DELETE are naturally idempotent; **POST is not** — use **Idempotency-Key** header. **How**: store processed keys with response in Redis/SQL; return cached response on duplicate. **Pitfall**: retries without idempotency cause duplicate orders or double charges."
        ),
        "code": """[HttpPost]
public async Task<IActionResult> CreateOrder(
    [FromBody] CreateOrderDto dto,
    [FromHeader(Name = "Idempotency-Key")] string idempotencyKey)
{
    var cacheKey = $"idempotency:{idempotencyKey}";
    var cached = await _cache.GetStringAsync(cacheKey);
    if (cached is not null)
        return StatusCode(201, JsonSerializer.Deserialize<object>(cached));

    var order = await _service.CreateAsync(dto);
    await _cache.SetStringAsync(cacheKey, JsonSerializer.Serialize(order),
        new DistributedCacheEntryOptions {
            AbsoluteExpirationRelativeToNow = TimeSpan.FromHours(24) });
    return CreatedAtAction(nameof(Get), new { id = order.Id }, order);
}""",
        "language": "csharp",
        "key_points": [
            "POST needs Idempotency-Key for safe retries",
            "At-least-once messaging requires idempotent consumers",
            "Store key + response; return same result on replay",
            "Unique DB constraints as last line of defense",
            "Payment APIs mandate idempotency keys",
        ],
    },
    "mediator-pattern-mediatr": {
        "explanation": (
            "The **Mediator pattern** decouples request senders from handlers. **MediatR** implements mediator + CQRS in .NET — each command/query is a record with one handler. **Pipeline behaviors** wrap handlers for validation, logging, transactions. **Why**: single responsibility, easy testing, organized use cases. **How**: controllers call `_mediator.Send(command)`. **When**: growing service classes need decomposition. **Pitfall**: over-mediating simple CRUD adds ceremony without benefit."
        ),
        "code": """public record CancelOrderCommand(int OrderId, string Reason) : IRequest;

public class CancelOrderHandler(IOrderRepository repo) : IRequestHandler<CancelOrderCommand>
{
    public async Task Handle(CancelOrderCommand cmd, CancellationToken ct)
    {
        var order = await repo.GetByIdAsync(cmd.OrderId, ct)
            ?? throw new NotFoundException(cmd.OrderId);
        order.Cancel(cmd.Reason);
        await repo.SaveChangesAsync(ct);
    }
}

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
            "Controllers call _mediator.Send() — thin controllers",
            "Pairs naturally with CQRS",
            "Test handlers directly without HTTP layer",
        ],
    },
    "observability-three-pillars": {
        "explanation": (
            "**Observability** is understanding system internal state from external outputs. Three pillars: **Logs** (discrete timestamped events — structured JSON preferred), **Metrics** (numeric aggregates — request rate, error rate, latency), **Traces** (request journey across services with spans and correlation IDs). **Why**: debugging distributed systems requires all three correlated. **How**: OpenTelemetry exports to Azure Monitor, Grafana, Jaeger. **Pitfall**: logging alone is insufficient — you need RED metrics (Rate, Errors, Duration) per service."
        ),
        "code": """builder.Services.AddOpenTelemetry()
    .WithTracing(t => t
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddEntityFrameworkCoreInstrumentation())
    .WithMetrics(m => m.AddAspNetCoreInstrumentation())
    .UseAzureMonitor();

// Structured log — auto-correlated with trace
logger.LogInformation("Placing order {OrderId} for {CustomerId}",
    order.Id, order.CustomerId);
// TraceId and SpanId injected into log scope automatically""",
        "language": "csharp",
        "key_points": [
            "Logs + Metrics + Traces — not just logging",
            "Structured logging with message templates",
            "Correlation ID links logs across microservices",
            "RED: Rate, Errors, Duration for every service",
            "OpenTelemetry → Azure Monitor / Grafana / Jaeger",
        ],
    },
    "owasp-top-10": {
        "explanation": (
            "The **OWASP Top 10** lists the most critical web application security risks. For .NET APIs focus on: **A01 Broken Access Control** — verify user owns resource; **A02 Cryptographic Failures** — TLS, hash passwords with bcrypt/Argon2; **A03 Injection** — parameterized queries; **A05 Security Misconfiguration** — disable debug in prod; **A06 Vulnerable Components** — Dependabot audit. **Why**: interviewers expect concrete mitigations in code, not just names. **Pitfall**: returning 404 instead of 403 enables resource enumeration."
        ),
        "code": """[Authorize]
[HttpGet("{id}")]
public async Task<IActionResult> GetOrder(int id)
{
    var order = await _repo.GetAsync(id);
    if (order is null) return NotFound();
    if (order.CustomerId != User.GetCustomerId()) return Forbid();
    return Ok(order);
}

// A03 — EF Core parameterized (never string concat)
var orders = await _db.Orders
    .Where(o => o.CustomerName == customerName).ToListAsync();

// A06 — dotnet list package --vulnerable""",
        "language": "csharp",
        "key_points": [
            "A01 Access Control — check every endpoint",
            "A03 Injection — parameterized queries always",
            "A06 Vulnerable components — automate dependency scanning",
            "A05 Misconfiguration — secure defaults, no debug in prod",
            "A09 Logging — audit auth failures and admin actions",
        ],
    },
    "pair-programming": {
        "explanation": (
            "**Pair programming** — two developers at one workstation: **Driver** writes code, **Navigator** reviews and thinks ahead. **Why**: knowledge sharing, fewer defects, faster onboarding, collective ownership. **Styles**: Driver-Navigator, **Ping-Pong TDD** (one writes test, other implements), **Mob programming** (whole team). **When**: complex features, critical bugs, onboarding juniors. **Pitfall**: pairing on simple CRUD with clear spec is slower than solo — choose context wisely."
        ),
        "code": """/*
  Ping-Pong TDD flow:
  1. Navigator writes failing test: CancelOrder_AlreadyShipped_Throws
  2. Driver implements minimum code to pass
  3. Driver writes test: CancelOrder_WithinWindow_PublishesRefundEvent
  4. Navigator implements
  5. Refactor together

  Remote: VS Code Live Share, swap roles every 25 min (Pomodoro)

  When NOT to pair: simple CRUD, exploratory spikes (solo research)
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
    "rest-api-design": {
        "explanation": (
            "**REST API design** best practices: use **resource nouns** (not verbs), correct **HTTP methods** and **status codes**, consistent **versioning** (/v1/), **pagination** (cursor preferred), **RFC 7807 Problem Details** for errors. **Why**: predictable contracts for consumers. **How**: DTOs not entity models, PATCH for partial updates, OpenAPI documentation. **When**: every public API. **Pitfall**: using POST for everything or returning 200 with error body instead of proper status codes."
        ),
        "code": """[ApiController]
[Route("api/v1/orders")]
public class OrdersController(IOrderService service) : ControllerBase
{
    [HttpGet]
    public async Task<ActionResult<PagedResult<OrderSummaryDto>>> List(
        [FromQuery] int page = 1, [FromQuery] int pageSize = 20)
        => Ok(await service.ListAsync(page, pageSize));

    [HttpPost]
    [ProducesResponseType(typeof(OrderDetailDto), StatusCodes.Status201Created)]
    public async Task<ActionResult<OrderDetailDto>> Create([FromBody] CreateOrderDto dto)
    {
        var order = await service.CreateAsync(dto);
        return CreatedAtAction(nameof(Get), new { id = order.Id }, order);
    }
}""",
        "language": "csharp",
        "key_points": [
            "Nouns in URLs; HTTP verbs for actions",
            "201 Created + Location header on POST",
            "Cursor pagination for large datasets",
            "Problem Details (RFC 7807) for consistent errors",
            "Version via URL path or header — be consistent",
        ],
    },
    "retry-policies-polly": {
        "explanation": (
            "**Retry policies** automatically re-attempt failed operations for **transient errors** — HTTP 503, timeout, connection reset. **Why**: cloud networks are unreliable; retries improve resilience. **How**: **exponential backoff with jitter** avoids thundering herd. **Only retry idempotent operations** or use idempotency keys. **Polly v8** `ResiliencePipeline` combines retry, circuit breaker, timeout. **Pitfall**: retrying non-idempotent POST without idempotency key causes duplicates."
        ),
        "code": """builder.Services.AddHttpClient<IInventoryClient, InventoryClient>()
    .AddResilienceHandler("inventory", pipeline =>
    {
        pipeline.AddRetry(new RetryStrategyOptions<HttpResponseMessage>
        {
            MaxRetryAttempts = 3,
            Delay = TimeSpan.FromSeconds(2),
            BackoffType = DelayBackoffType.Exponential,
            UseJitter = true,
            ShouldHandle = new PredicateBuilder<HttpResponseMessage>()
                .HandleResult(r => (int)r.StatusCode >= 500)
                .Handle<HttpRequestException>()
        });
        pipeline.AddTimeout(TimeSpan.FromSeconds(15));
    });""",
        "language": "csharp",
        "key_points": [
            "Retry transient failures only — 5xx, timeout, 429",
            "Exponential backoff + jitter prevents thundering herd",
            "Never blindly retry non-idempotent POST",
            "Combine retry + circuit breaker + timeout",
            "Polly v8 AddResilienceHandler on HttpClient",
        ],
    },
    "sre-practices": {
        "explanation": (
            "**Site Reliability Engineering (SRE)** applies software engineering to operations. **SLI** (metric), **SLO** (target — 99.9% requests < 500ms), **SLA** (contract with penalties), **Error budget** (100% - SLO = allowed unreliability). **Why**: data-driven reliability decisions. **How**: when budget exhausted, freeze features and focus on reliability; **blameless postmortems** after incidents. **Pitfall**: SLOs without alerting burn rate detection — you discover budget exhaustion too late."
        ),
        "code": """/*
  SLO: 99.9% of requests complete in < 500ms over 30-day window
  Error budget: 0.1% = 43.2 minutes of bad requests/month

  Burn rate alert:
  - 14.4x burn over 1h → page on-call
  - 6x burn over 6h → ticket

  Blameless postmortem:
  1. Incident summary  2. Timeline  3. Root cause (5 whys)
  4. What went well / didn't  5. Action items with owners
*/""",
        "language": "text",
        "key_points": [
            "SLI → SLO → error budget → engineering decisions",
            "Error budget exhausted = reliability over features",
            "Blameless postmortems — focus on systems not people",
            "Reduce toil through automation",
            "On-call runbooks and escalation paths required",
        ],
    },
    "technical-debt-management": {
        "explanation": (
            "**Technical debt** is the implied cost of future rework from choosing an easy solution now. Not all debt is bad — **conscious tradeoffs** for speed can be correct if tracked and repaid. **Why**: unmanaged debt slows delivery and increases bugs. **How**: debt register in backlog, allocate 10–20% sprint capacity, **boy scout rule** (leave code cleaner), **strangler fig** for legacy. **When**: every sprint includes some repayment. **Pitfall**: hiding debt or refactoring without business alignment wastes effort."
        ),
        "code": """/*
  Technical Debt Register:
  | ID   | Description              | Impact | Effort |
  | TD-1 | OrderService god class   | High   | 3 pts  |
  | TD-2 | No integration tests     | High   | 5 pts  |

  Strategies:
  1. 20% sprint capacity for debt
  2. Boy Scout Rule — improve one thing per PR touch
  3. Strangler fig — migrate endpoint by endpoint
  4. SonarQube in CI — fail on new critical issues
*/""",
        "language": "text",
        "key_points": [
            "Track debt explicitly — don't hide it",
            "Allocate 10–20% sprint capacity for repayment",
            "Boy Scout Rule on every touch",
            "Strangler fig for legacy migration",
            "Measure: bugs, lead time, code churn",
        ],
    },
    "twelve-factor-app": {
        "explanation": (
            "The **Twelve-Factor App** defines best practices for **cloud-native SaaS**. Key factors for .NET on Azure: **III. Config** — environment variables / Key Vault, not hardcoded secrets; **VI. Processes** — stateless, share nothing (session in Redis); **IX. Disposability** — fast startup, graceful SIGTERM shutdown; **XI. Logs** — stdout streams to Azure Monitor; **XII. Admin** — EF migrations as release task. **Why**: portability and operability in cloud. **Pitfall**: storing secrets in appsettings.json committed to git."
        ),
        "code": """/*
  III. Config — Key Vault references
  "ConnectionStrings__Sql": "@Microsoft.KeyVault(SecretUri=...)"

  VI. Processes — stateless; session in Redis
  builder.Services.AddStackExchangeRedisCache(...);

  IX. Disposability — graceful shutdown
  builder.Services.Configure<HostOptions>(o =>
      o.ShutdownTimeout = TimeSpan.FromSeconds(30));

  XII. Admin — migration as pipeline step
  dotnet ef database update --connection "$(SqlConnection)"
*/""",
        "language": "text",
        "key_points": [
            "Config in environment / Key Vault — not source code",
            "Stateless processes — externalize session state",
            "Logs as event streams to stdout / Azure Monitor",
            "Disposability — fast startup, graceful SIGTERM handling",
            "Dev/prod parity — same containers, same services",
        ],
    },
    "aria-attributes": {
        "explanation": (
            "**WAI-ARIA** attributes enhance accessibility when native HTML semantics are insufficient. The first rule of ARIA: **don't use ARIA if native HTML works** — use `<button>` not `<div role=\"button\">`. Key attributes: `aria-label`, `aria-labelledby`/`aria-describedby`, `aria-expanded`/`aria-controls`, `aria-live` for dynamic announcements, `aria-hidden=\"true\"` for decorative elements. **Why**: screen readers need programmatic names and state. **How**: test with NVDA, VoiceOver, axe DevTools. **Pitfall**: incorrect ARIA is worse than no ARIA — it actively misleads assistive technology."
        ),
        "code": """<!-- Disclosure widget -->
<button type="button" aria-expanded="false" aria-controls="filter-menu" id="filter-btn">
  Filters
</button>
<ul id="filter-menu" role="menu" aria-labelledby="filter-btn" hidden>
  <li role="menuitem">Status</li>
</ul>

<!-- Dynamic status updates -->
<div aria-live="polite" aria-atomic="true" class="sr-only">
  {{ saveStatusMessage }}
</div>

<!-- Decorative icon -->
<span aria-hidden="true">📦</span> Order shipped""",
        "language": "html",
        "key_points": [
            "First rule: use native HTML before ARIA",
            "aria-live for dynamic content announcements",
            "aria-describedby links inputs to hint/error text",
            "aria-hidden hides decorative content from screen readers",
            "Test with screen readers and axe DevTools",
        ],
    },
    "bem-methodology": {
        "explanation": (
            "**BEM (Block Element Modifier)** is a CSS naming convention: **Block** (standalone component, e.g. `card`), **Element** (part of block, `card__title`), **Modifier** (variant, `card--featured`). **Why**: avoids specificity wars and makes component boundaries explicit. **How**: flat selectors — no nesting beyond block. **When**: large codebases without CSS-in-JS. **Pitfall**: overly deep element names (`card__header__title__icon`) — keep elements one level deep under block."
        ),
        "code": """/* Block */
.card { padding: 1rem; border: 1px solid #ddd; }

/* Element — part of card */
.card__title { font-size: 1.25rem; font-weight: 600; }
.card__body  { margin-top: 0.5rem; color: #555; }

/* Modifier — variant */
.card--featured { border-color: #2563eb; background: #eff6ff; }
.card__title--large { font-size: 1.5rem; }

<!-- HTML -->
<article class="card card--featured">
  <h2 class="card__title">Order #1042</h2>
  <p class="card__body">Shipped today</p>
</article>""",
        "language": "css",
        "key_points": [
            "Block__Element--Modifier naming convention",
            "Flat selectors — avoid deep nesting",
            "Modifiers express variants without new blocks",
            "Elements belong to one block only",
            "Pairs well with component-based frameworks",
        ],
    },
    "bootstrap-vs-tailwind": {
        "explanation": (
            "**Bootstrap** provides pre-built components (navbar, modal, grid) with opinionated styling — fast prototyping but sites look similar without customization. **Tailwind CSS** is **utility-first** — compose designs with atomic classes (`flex`, `p-4`, `text-blue-600`) in HTML. **Why choose Bootstrap**: rapid MVP, team knows Bootstrap, jQuery-free v5+. **Why Tailwind**: full design control, smaller production CSS via PurgeCSS, no fighting framework defaults. **Pitfall**: Tailwind HTML can get verbose — extract components with `@apply` or framework components."
        ),
        "code": """<!-- Bootstrap — component classes -->
<button class="btn btn-primary">Place Order</button>
<div class="card"><div class="card-body">Order #1042</div></div>

<!-- Tailwind — utility composition -->
<button class="rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700">
  Place Order
</button>
<div class="rounded-lg border border-gray-200 p-4 shadow-sm">
  Order #1042
</div>

/* Tailwind @apply — extract repeated patterns */
.btn-primary {
  @apply rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700;
}""",
        "language": "html",
        "key_points": [
            "Bootstrap: pre-built components, faster prototyping",
            "Tailwind: utility-first, full design control",
            "Tailwind PurgeCSS removes unused utilities in prod",
            "Bootstrap sites look similar without customization",
            "Extract repeated Tailwind patterns with @apply",
        ],
    },
    "critical-css-performance": {
        "explanation": (
            "**Critical CSS** is the minimum CSS required to render above-the-fold content. **Why**: render-blocking CSS delays First Contentful Paint — inlining critical CSS eliminates an extra round trip for initial paint. **How**: extract critical styles, inline in `<head>`, load full stylesheet asynchronously with `media=\"print\" onload`. **When**: performance-critical landing pages. **Pitfall**: inlining too much CSS bloats HTML and prevents caching — typically keep critical CSS under 14KB."
        ),
        "code": """<head>
  <!-- Inline critical CSS for above-the-fold -->
  <style>
    .hero { display: flex; min-height: 100vh; align-items: center; }
    .nav  { position: fixed; top: 0; width: 100%; background: #fff; }
  </style>

  <!-- Load full stylesheet asynchronously -->
  <link rel="preload" href="/styles/main.css" as="style"
        onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="/styles/main.css"></noscript>
</head>

/* Tools: critical (npm), Penthouse, Angular build optimizer */""",
        "language": "html",
        "key_points": [
            "Inline critical CSS in <head> for fast first paint",
            "Load full stylesheet asynchronously after",
            "Keep critical CSS small — under ~14KB",
            "Tools: critical, Penthouse, build optimizer plugins",
            "Too much inline CSS hurts cacheability",
        ],
    },
    "css-animations-transitions": {
        "explanation": (
            "**CSS transitions** animate property changes between two states (`transition: opacity 0.3s ease`). **CSS animations** use `@keyframes` for multi-step sequences independent of state changes. **Why**: GPU-accelerated properties (`transform`, `opacity`) animate smoothly without layout thrashing. **How**: prefer transitions for hover/focus; keyframes for loaders and complex sequences. **When**: micro-interactions, page transitions. **Pitfall**: animating `width`, `height`, or `top` triggers layout — use `transform: scale()` instead."
        ),
        "code": """/* Transition — hover state change */
.btn {
  background: #2563eb;
  transition: background 0.2s ease, transform 0.15s ease;
}
.btn:hover  { background: #1d4ed8; transform: translateY(-1px); }
.btn:active { transform: translateY(0); }

/* Keyframe animation — loading spinner */
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
.spinner {
  animation: spin 0.8s linear infinite;
}

/* Respect user preference */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}""",
        "language": "css",
        "key_points": [
            "Animate transform and opacity — GPU accelerated",
            "Transitions for state changes; keyframes for sequences",
            "Avoid animating width/height/top — causes layout",
            "prefers-reduced-motion for accessibility",
            "will-change sparingly — only during animation",
        ],
    },
    "css-box-model": {
        "explanation": (
            "The **CSS box model** defines how element size is calculated: **content** + **padding** + **border** + **margin**. **`box-sizing: border-box`** includes padding and border in the declared width/height — the modern default most resets apply. **`box-sizing: content-box`** (default in CSS spec) adds padding and border outside the width. **Why**: misunderstanding box model causes layout overflow bugs. **How**: set `box-sizing: border-box` globally. **Pitfall**: margin collapse between adjacent block elements surprises developers — only vertical margins collapse."
        ),
        "code": """*, *::before, *::after { box-sizing: border-box; }

.box {
  width: 300px;
  padding: 20px;
  border: 2px solid #333;
  margin: 16px;
  /* With border-box: total rendered width = 300px */
  /* With content-box: total = 300 + 40 + 4 = 344px */
}

/* Margin collapse — adjacent vertical margins merge */
.block-a { margin-bottom: 24px; }
.block-b { margin-top: 16px; }
/* Gap between them = 24px (larger wins), not 40px */""",
        "language": "css",
        "key_points": [
            "Content + padding + border + margin = box model",
            "border-box includes padding/border in width",
            "Set border-box globally — modern best practice",
            "Vertical margins collapse between block elements",
            "content-box adds padding/border outside declared width",
        ],
    },
    "css-containment": {
        "explanation": (
            "**CSS containment** tells the browser an element's subtree is independent — enabling **layout**, **style**, **paint**, or **size** containment optimizations. **Why**: limits recalculation scope during DOM changes — critical for long lists and complex dashboards. **How**: `contain: layout paint` on list items or card components. **`content-visibility: auto`** skips rendering off-screen content. **When**: virtualized lists, heavy SPAs. **Pitfall**: `contain: size` requires explicit dimensions or content may collapse to zero height."
        ),
        "code": """/* Limit layout/paint recalculation scope */
.order-card {
  contain: layout paint;
  content-visibility: auto;
  contain-intrinsic-size: 0 120px; /* placeholder height while skipped */
}

/* Strict containment for isolated widget */
.dashboard-widget {
  contain: strict; /* layout + style + paint + size */
  width: 100%;
  height: 400px;
}

/* Performance: browser skips layout for off-screen cards */
.product-list-item {
  content-visibility: auto;
  contain-intrinsic-size: 0 80px;
}""",
        "language": "css",
        "key_points": [
            "contain: layout paint limits recalculation scope",
            "content-visibility: auto skips off-screen rendering",
            "contain-intrinsic-size prevents layout shift",
            "strict containment requires explicit dimensions",
            "Best for long lists and complex dashboards",
        ],
    },
    "css-custom-properties": {
        "explanation": (
            "**CSS custom properties (variables)** are defined with `--name: value` and used with `var(--name)`. Unlike SASS variables, they are **live** — change at runtime via JavaScript or media queries. **Why**: theming (dark mode), design tokens, component variants without preprocessor. **How**: define tokens on `:root`, override in `.dark` or `[data-theme]`. **When**: design systems, theme switching. **Pitfall**: `var()` fallback is required for older browsers; invalid values silently fall back."
        ),
        "code": """:root {
  --color-primary: #2563eb;
  --color-surface: #ffffff;
  --color-text: #1f2937;
  --spacing-md: 1rem;
  --radius: 0.5rem;
}

[data-theme="dark"] {
  --color-primary: #3b82f6;
  --color-surface: #111827;
  --color-text: #f9fafb;
}

.btn-primary {
  background: var(--color-primary);
  color: var(--color-surface);
  padding: var(--spacing-md);
  border-radius: var(--radius);
}

// JS runtime theme switch
document.documentElement.setAttribute('data-theme', 'dark');""",
        "language": "css",
        "key_points": [
            "Define with --name on :root; use var(--name)",
            "Live at runtime — unlike SASS compile-time variables",
            "Override in [data-theme] or .dark for theming",
            "var(--name, fallback) for graceful degradation",
            "Design tokens: colors, spacing, radius as variables",
        ],
    },
    "css-grid-advanced": {
        "explanation": (
            "**CSS Grid advanced** techniques go beyond basic two-column layouts. **`grid-template-areas`** names regions for readable layout definitions. **`minmax()`**, **`auto-fill`**, **`auto-fit`**, and **`fr`** units create responsive grids without media queries. **`subgrid`** (now widely supported) lets nested grids align to parent tracks. **Why**: Grid handles two-dimensional layouts that Flexbox cannot. **Pitfall**: using Grid for one-dimensional row/column — Flexbox is simpler there."
        ),
        "code": """.dashboard {
  display: grid;
  grid-template-columns: 240px 1fr;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "sidebar header"
    "sidebar main"
    "sidebar footer";
  min-height: 100vh;
}
.sidebar { grid-area: sidebar; }
.header  { grid-area: header; }
.main    { grid-area: main; overflow: auto; }

/* Responsive card grid — no media queries */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}""",
        "language": "css",
        "key_points": [
            "grid-template-areas for named layout regions",
            "repeat(auto-fill, minmax(280px, 1fr)) — responsive grid",
            "fr unit distributes remaining space proportionally",
            "subgrid aligns nested grid to parent tracks",
            "Grid for 2D layouts; Flexbox for 1D",
        ],
    },
    "css-layer": {
        "explanation": (
            "**CSS `@layer`** controls cascade order explicitly — solving specificity wars between frameworks, components, and utilities. **Why**: without layers, load order and `!important` are the only cascade controls. **How**: declare layer order first (`@layer reset, base, components, utilities`), then assign rules to layers. **When**: combining Tailwind, component CSS, and third-party styles. **Pitfall**: unlayered styles always beat layered styles — put everything in layers."
        ),
        "code": """/* Declare layer order — first = lowest priority */
@layer reset, base, components, utilities;

@layer reset {
  *, *::before, *::after { box-sizing: border-box; margin: 0; }
}

@layer base {
  body { font-family: system-ui, sans-serif; line-height: 1.5; }
}

@layer components {
  .btn { padding: 0.5rem 1rem; border-radius: 0.375rem; }
}

@layer utilities {
  .text-center { text-align: center; }
  .mt-4 { margin-top: 1rem; }
}

/* Unlayered styles override ALL layers — avoid mixing */""",
        "language": "css",
        "key_points": [
            "@layer declares explicit cascade priority order",
            "First declared layer = lowest priority",
            "Unlayered styles beat all layered styles",
            "Solves framework vs component specificity conflicts",
            "Pair with Tailwind @layer base/components/utilities",
        ],
    },
    "css-preprocessors-sass": {
        "explanation": (
            "**SASS/SCSS preprocessors** extend CSS with variables, nesting, mixins, functions, and imports — compiled to standard CSS at build time. **Why**: DRY stylesheets before native CSS variables and nesting. **How**: `$variable`, `@mixin`/`@include`, `&` parent selector, `@use` (replaces deprecated `@import`). **When**: legacy codebases; modern projects often use PostCSS or native CSS. **Pitfall**: deep nesting creates high specificity selectors — limit to 3 levels; `@import` is deprecated in favor of `@use`."
        ),
        "code": """// _variables.scss
$primary: #2563eb;
$spacing-md: 1rem;

// _mixins.scss
@mixin flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

// card.scss
@use 'variables' as v;
@use 'mixins' as m;

.card {
  padding: v.$spacing-md;
  border: 1px solid v.$primary;

  &__title {
    font-weight: 600;
    @include m.flex-center;
  }

  &--featured { background: lighten(v.$primary, 45%); }
}""",
        "language": "css",
        "key_points": [
            "Variables, mixins, nesting — compiled to CSS",
            "@use replaces deprecated @import",
            "Limit nesting depth — avoid specificity bloat",
            "Native CSS variables often replace SASS variables",
            "Modern stacks use PostCSS or CSS-native features",
        ],
    },
    "css-reset-vs-normalize": {
        "explanation": (
            "A **CSS reset** (e.g., Meyer Reset) strips all default browser styles to zero — aggressive blank slate. **Normalize.css** preserves useful defaults while fixing cross-browser inconsistencies. **Why**: browsers render `<h1>`, `<button>`, and margins differently without normalization. **How**: most projects use a minimal reset + `box-sizing: border-box` or Tailwind Preflight (based on Normalize). **When**: start of every project. **Pitfall**: full reset removes semantic styling — you must rebuild all base styles."
        ),
        "code": """/* Minimal modern reset (similar to Tailwind Preflight) */
*, *::before, *::after { box-sizing: border-box; }
* { margin: 0; padding: 0; }

html { line-height: 1.5; -webkit-text-size-adjust: 100%; }
body { min-height: 100vh; }

img, video { max-width: 100%; display: block; }
button, input, select, textarea { font: inherit; color: inherit; }

/* Normalize approach — preserve useful defaults */
/* h1 { font-size: 2em; margin: 0.67em 0; } — kept, not zeroed */""",
        "language": "css",
        "key_points": [
            "Reset: zero everything — blank slate",
            "Normalize: fix inconsistencies, keep useful defaults",
            "Tailwind Preflight is a modern Normalize-based reset",
            "Always set box-sizing: border-box globally",
            "Full reset requires rebuilding all base typography",
        ],
    },
    "css-specificity": {
        "explanation": (
            "**CSS specificity** determines which rule wins when selectors conflict. Order: **inline styles** (1000) > **IDs** (100) > **classes/attributes/pseudo-classes** (10) > **elements/pseudo-elements** (1). **Why**: understanding prevents `!important` abuse. **How**: prefer low-specificity selectors — single class over chained selectors. **When**: debugging why styles don't apply. **Pitfall**: `#nav .menu li a` is hard to override — use BEM single-class selectors instead."
        ),
        "code": """/* Specificity: (0,1,0) — one class */
.btn-primary { background: blue; }

/* Specificity: (0,2,1) — harder to override */
nav.header .btn-primary { background: red; } /* wins over above */

/* Specificity: (1,0,0) — ID beats classes */
#main .btn-primary { background: green; } /* wins */

/* Avoid !important — last resort */
.btn-primary { background: blue !important; } /* code smell */

/* Better: use same or higher specificity intentionally */
.btn-primary.btn-primary { background: blue; } /* (0,2,0) */""",
        "language": "css",
        "key_points": [
            "Inline > ID > Class > Element specificity order",
            "Prefer single-class selectors (BEM)",
            "Avoid deep chained selectors — hard to override",
            "!important is a last resort — signals design problem",
            "Later rule wins only when specificity is equal",
        ],
    },
    "css-units-rem-em": {
        "explanation": (
            "**rem** is relative to the root (`html`) font size — typically 16px, so `1rem = 16px`, `1.5rem = 24px`. **em** is relative to the **parent** element's font size — compounds in nested elements. **Why**: rem gives consistent, accessible sizing; users who increase browser font size get proportional layouts. **How**: set `html { font-size: 100%; }`, use rem for spacing/sizing, em for component-relative padding. **Pitfall**: em nesting compounds (`1.2em` inside `1.2em` = 1.44em) — prefer rem for most values."
        ),
        "code": """html { font-size: 100%; } /* respects user browser setting — 16px default */

body  { font-size: 1rem; }     /* 16px */
h1    { font-size: 2rem; }     /* 32px */
.small { font-size: 0.875rem; } /* 14px */

.card {
  padding: 1.5rem;       /* 24px — consistent everywhere */
  margin-bottom: 1rem;
}

/* em — relative to parent font size */
.btn {
  font-size: 1rem;
  padding: 0.5em 1em;  /* scales with button font-size */
}

/* Avoid px for typography — breaks user font-size preferences */""",
        "language": "css",
        "key_points": [
            "rem = relative to root html font size",
            "em = relative to parent — compounds when nested",
            "Use rem for spacing, sizing, typography",
            "Use em for component-relative padding/icons",
            "Avoid px for typography — respect user preferences",
        ],
    },
    "dark-mode-implementation": {
        "explanation": (
            "**Dark mode** reduces eye strain and saves OLED battery. **Why**: user expectation in modern apps. **How**: CSS **`prefers-color-scheme: dark`** media query for system preference; **`[data-theme=\"dark\"]`** for manual toggle; CSS custom properties for token swap. **When**: always offer system preference support; optional manual override. **Pitfall**: pure black `#000` backgrounds cause halation — use dark gray (`#111827`) and reduce contrast on large white text blocks."
        ),
        "code": """:root {
  --bg: #ffffff; --text: #1f2937; --surface: #f3f4f6;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #111827; --text: #f9fafb; --surface: #1f2937;
  }
}
[data-theme="dark"]  { --bg: #111827; --text: #f9fafb; --surface: #1f2937; }
[data-theme="light"] { --bg: #ffffff; --text: #1f2937; --surface: #f3f4f6; }

body { background: var(--bg); color: var(--text); }

// Angular — persist preference
toggleDark() {
  const dark = document.documentElement.getAttribute('data-theme') !== 'dark';
  document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
  localStorage.setItem('theme', dark ? 'dark' : 'light');
}""",
        "language": "css",
        "key_points": [
            "prefers-color-scheme: dark for system preference",
            "CSS custom properties enable token swap",
            "Avoid pure #000 — use dark gray (#111827)",
            "Persist manual toggle in localStorage",
            "color-scheme: dark hints browser UI elements",
        ],
    },
    "flexbox-advanced": {
        "explanation": (
            "**Flexbox advanced** patterns handle complex one-dimensional layouts. Key properties: **`flex-grow/shrink/basis`** control sizing; **`align-self`** overrides cross-axis alignment for one item; **`order`** reorders visually (not DOM); **`flex-wrap`** enables multi-row flex. **Why**: centering, equal-height columns, sticky footers without floats. **How**: `display: flex` on container. **When**: nav bars, card rows, form layouts. **Pitfall**: `order` changes visual order but not tab/screen reader order — avoid for accessibility."
        ),
        "code": """/* Holy grail — sticky footer */
.page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.page-main  { flex: 1; } /* grows to fill space */
.page-footer { flex-shrink: 0; }

/* Equal-width columns with flex */
.toolbar {
  display: flex;
  gap: 1rem;
  align-items: center;
}
.toolbar-spacer { flex: 1; } /* pushes items apart */
.btn { flex-shrink: 0; }

/* Wrap responsive card row */
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
.card { flex: 1 1 280px; } /* grow, shrink, min 280px */""",
        "language": "css",
        "key_points": [
            "flex: 1 shorthand for flex-grow/shrink/basis",
            "flex-wrap for responsive multi-row layouts",
            "align-self overrides cross-axis for one item",
            "order changes visual not DOM order — a11y risk",
            "Flexbox for 1D; Grid for 2D layouts",
        ],
    },
    "html-forms-validation": {
        "explanation": (
            "HTML forms collect user input with built-in **constraint validation**. Attributes like `required`, `min`/`max`, `pattern`, `type=\"email\"` trigger native browser validation. **Why**: free client-side validation before server round trip. **How**: pair inputs with `<label for=\"id\">`; display errors with `role=\"alert\"`; use `aria-invalid` and `aria-describedby`. **`novalidate`** disables native validation for framework validation (Angular Reactive Forms). **Pitfall**: never rely on client validation alone — always validate on server."
        ),
        "code": """<form [formGroup]="orderForm" (ngSubmit)="submit()" novalidate>
  <label for="qty">Quantity</label>
  <input id="qty" type="number" formControlName="quantity"
         min="1" max="99" required
         [attr.aria-invalid]="orderForm.get('quantity')?.invalid"
         aria-describedby="qty-error">
  <span id="qty-error" role="alert"
        *ngIf="orderForm.get('quantity')?.touched && orderForm.get('quantity')?.invalid">
    Enter a quantity between 1 and 99.
  </span>

  <label for="email">Email</label>
  <input id="email" type="email" formControlName="email" required>

  <button type="submit" [disabled]="orderForm.invalid">Place Order</button>
</form>""",
        "language": "html",
        "key_points": [
            "Always use <label for=\"id\"> with inputs",
            "role=\"alert\" for error messages",
            "aria-invalid and aria-describedby for accessibility",
            "HTML5 types: email, url, number, date, tel",
            "Always validate on server — client validation is UX only",
        ],
    },
    "html5-semantic-deep-dive": {
        "explanation": (
            "**HTML5 semantic elements** convey meaning to browsers, screen readers, and search engines. `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>` replace meaningless `<div>` soup. **Why**: accessibility landmarks, SEO, readable markup. **How**: one `<main>` per page; `<article>` for self-contained content; `<section>` needs a heading. **When**: every page layout. **Pitfall**: using `<section>` without a heading violates HTML spec; don't use `<b>` when `<strong>`  conveys meaning."
        ),
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Order Dashboard</title>
</head>
<body>
  <header>
    <nav aria-label="Main navigation">
      <a href="/orders">Orders</a>
    </nav>
  </header>

  <main id="main-content">
    <h1>Your Orders</h1>
    <article aria-labelledby="order-1042">
      <h2 id="order-1042">Order #1042</h2>
      <p>Status: <strong>Shipped</strong></p>
      <time datetime="2026-06-23">June 23, 2026</time>
    </article>
  </main>

  <footer><p>&copy; 2026 Acme Corp</p></footer>
</body>
</html>""",
        "language": "html",
        "key_points": [
            "One <main> per page — primary content landmark",
            "<article> for self-contained content blocks",
            "<section> requires an associated heading",
            "Landmark roles improve screen reader navigation",
            "Use <time datetime> for machine-readable dates",
        ],
    },
    "media-queries": {
        "explanation": (
            "**Media queries** apply CSS conditionally based on viewport, device, or user preferences. **Why**: responsive design — adapt layout to screen size. **How**: `@media (min-width: 768px) { ... }` for breakpoints; `(prefers-reduced-motion)`, `(prefers-color-scheme: dark)` for accessibility. **Mobile-first**: start with base mobile styles, add `min-width` queries for larger screens. **Pitfall**: device-specific breakpoints (iPhone width) break on new devices — use content-based breakpoints."
        ),
        "code": """/* Mobile-first base styles */
.grid { display: grid; grid-template-columns: 1fr; gap: 1rem; }
.sidebar { display: none; }

/* Tablet */
@media (min-width: 768px) {
  .grid { grid-template-columns: 1fr 1fr; }
}

/* Desktop */
@media (min-width: 1024px) {
  .grid { grid-template-columns: 240px 1fr; }
  .sidebar { display: block; }
}

/* Accessibility preferences */
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}""",
        "language": "css",
        "key_points": [
            "Mobile-first: base styles + min-width queries",
            "Content-based breakpoints, not device-specific widths",
            "prefers-reduced-motion and prefers-color-scheme queries",
            "min-width (mobile-first) vs max-width (desktop-first)",
            "Container queries (@container) for component-level responsiveness",
        ],
    },
    "mobile-first-design": {
        "explanation": (
            "**Mobile-first design** starts with the smallest screen layout and progressively enhances for larger viewports. **Why**: mobile traffic dominates; designing mobile-first forces prioritization of essential content. **How**: base CSS targets mobile; `@media (min-width: ...)` adds complexity for tablet/desktop. **When**: all responsive web apps. **Pitfall**: designing desktop-first then cramming mobile as afterthought produces bloated mobile pages — hide content with CSS, don't remove from DOM unnecessarily."
        ),
        "code": """/* Mobile-first: single column, touch-friendly targets */
.nav { flex-direction: column; }
.nav-link { padding: 1rem; min-height: 44px; } /* touch target */
.hero h1 { font-size: 1.75rem; }

/* Tablet enhancement */
@media (min-width: 768px) {
  .nav { flex-direction: row; }
  .hero h1 { font-size: 2.5rem; }
}

/* Desktop enhancement */
@media (min-width: 1024px) {
  .hero { display: grid; grid-template-columns: 1fr 1fr; }
  .hero h1 { font-size: 3rem; }
}

<meta name="viewport" content="width=device-width, initial-scale=1">""",
        "language": "css",
        "key_points": [
            "Base styles for mobile; min-width queries for larger screens",
            "Touch targets minimum 44×44px",
            "Prioritize essential content on small screens",
            "Requires viewport meta tag for proper scaling",
            "Progressive enhancement, not graceful degradation",
        ],
    },
    "print-stylesheets": {
        "explanation": (
            "**Print stylesheets** optimize page appearance when printed or saved as PDF. **Why**: invoices, reports, and order confirmations need clean print output. **How**: `@media print { ... }` hides navigation, sets black text on white, expands accordion content. **When**: any page users might print. **Pitfall**: background colors and images are stripped by default — use `-webkit-print-color-adjust: exact` sparingly; avoid relying on color alone for meaning."
        ),
        "code": """@media print {
  /* Hide non-essential UI */
  nav, .sidebar, .btn, footer { display: none !important; }

  /* Clean typography for print */
  body { font-size: 12pt; color: #000; background: #fff; }

  /* Expand full content */
  .accordion-panel { display: block !important; height: auto !important; }

  /* Show link URLs after anchor text */
  a[href^="http"]::after { content: " (" attr(href) ")"; font-size: 0.8em; }

  /* Avoid page breaks inside elements */
  .order-line-item { page-break-inside: avoid; }

  @page { margin: 2cm; }
}""",
        "language": "css",
        "key_points": [
            "@media print for print-specific styles",
            "Hide navigation, buttons, and sidebars",
            "page-break-inside: avoid for table rows and cards",
            "Use pt units for print typography",
            "Show URLs for external links in print output",
        ],
    },
    "pseudo-classes-elements": {
        "explanation": (
            "**Pseudo-classes** select elements in a specific state (`:hover`, `:focus-visible`, `:nth-child`, `:not()`, `:checked`). **Pseudo-elements** style specific parts (`::before`, `::after`, `::placeholder`, `::selection`). **Why**: interactive feedback and decorative content without extra DOM nodes. **How**: `:focus-visible` for keyboard focus rings (not mouse clicks); `::before`/`::after` for icons. **Pitfall**: `:focus` on all elements shows rings on mouse click — use `:focus-visible` instead."
        ),
        "code": """/* Interactive states */
.btn:hover  { background: #1d4ed8; }
.btn:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
}
.btn:active { transform: scale(0.98); }

/* Structural pseudo-classes */
li:nth-child(even) { background: #f9fafb; }
input:not([type="hidden"]) { display: block; margin-bottom: 0.5rem; }

/* Pseudo-elements */
.required-field::after { content: " *"; color: #ef4444; }
input::placeholder { color: #9ca3af; }
::selection { background: #bfdbfe; color: #1e3a8a; }""",
        "language": "css",
        "key_points": [
            "Pseudo-classes (:hover) vs pseudo-elements (::before)",
            ":focus-visible for keyboard-only focus rings",
            ":nth-child, :not(), :checked for structural selection",
            "::before/::after for decorative content without DOM",
            ":focus-visible preferred over :focus for a11y",
        ],
    },
    "responsive-images": {
        "explanation": (
            "**Responsive images** serve appropriately sized images for each viewport — saving bandwidth and improving LCP. **Why**: a 4000px hero image on mobile wastes megabytes. **How**: `srcset` with width descriptors (`800w`) and `sizes` attribute tells browser which to download; `<picture>` for art direction (different crop per breakpoint). **When**: all content images, especially heroes and product photos. **Pitfall**: missing `width`/`height` attributes cause Cumulative Layout Shift (CLS)."
        ),
        "code": """<!-- Responsive srcset — browser picks best size -->
<img
  src="product-800.jpg"
  srcset="product-400.jpg 400w,
          product-800.jpg 800w,
          product-1200.jpg 1200w"
  sizes="(max-width: 600px) 100vw, 50vw"
  width="800" height="600"
  alt="Blue running shoes"
  loading="lazy">

<!-- Art direction with picture element -->
<picture>
  <source media="(min-width: 768px)" srcset="hero-wide.jpg">
  <source media="(max-width: 767px)" srcset="hero-tall.jpg">
  <img src="hero-wide.jpg" alt="Summer sale" width="1200" height="400">
</picture>""",
        "language": "html",
        "key_points": [
            "srcset + sizes for resolution switching",
            "picture element for art direction per breakpoint",
            "Always set width/height to prevent CLS",
            "loading=\"lazy\" for below-fold images",
            "WebP/AVIF with fallback for modern formats",
        ],
    },
    "viewport-meta-tag": {
        "explanation": (
            "The **viewport meta tag** tells mobile browsers how to scale and size the page. `<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">` sets viewport width to device width and 1:1 zoom. **Why**: without it, mobile browsers render at ~980px desktop width then shrink — making responsive CSS ineffective. **How**: include in every HTML `<head>`. **When**: always, first thing in head after charset. **Pitfall**: `user-scalable=no` or `maximum-scale=1` blocks pinch-zoom — an accessibility violation (WCAG 1.4.4)."
        ),
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <!-- Required for responsive design on mobile -->
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Order Dashboard</title>
</head>

<!-- BAD — blocks zoom (accessibility violation) -->
<!-- <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"> -->

<!-- Angular index.html — same tag required -->
<!-- src/index.html -->""",
        "language": "html",
        "key_points": [
            "width=device-width matches viewport to device width",
            "initial-scale=1 sets 1:1 zoom on load",
            "Required for responsive CSS to work on mobile",
            "Never disable zoom — WCAG accessibility violation",
            "Include in index.html for SPAs (Angular, React)",
        ],
    },
    "wcag-accessibility": {
        "explanation": (
            "**WCAG (Web Content Accessibility Guidelines)** defines how to make web content accessible. Levels: **A**, **AA** (legal standard in most jurisdictions), **AAA**. Four principles (**POUR**): **Perceivable** (alt text, contrast), **Operable** (keyboard nav, no seizure triggers), **Understandable** (clear language, error identification), **Robust** (valid HTML, ARIA). **Why**: legal compliance (ADA, EAA), broader audience. **How**: test with axe, Lighthouse, screen readers. **Pitfall**: color contrast ratio 4.5:1 for normal text is AA minimum — don't rely on color alone."
        ),
        "code": """<!-- Perceivable: alt text, sufficient contrast -->
<img src="chart.png" alt="Sales increased 23% in Q2 2026">

<!-- Operable: keyboard accessible, visible focus -->
<button class="btn" type="button">Submit</button>
<!-- focus-visible styles in CSS -->

<!-- Understandable: label errors clearly -->
<label for="email">Email</label>
<input id="email" type="email" aria-describedby="email-error" aria-invalid="true">
<span id="email-error" role="alert">Enter a valid email address.</span>

<!-- Robust: semantic HTML, lang attribute -->
<html lang="en">

/* AA contrast: 4.5:1 normal text, 3:1 large text (18pt+) */""",
        "language": "html",
        "key_points": [
            "POUR: Perceivable, Operable, Understandable, Robust",
            "AA level is the legal standard in most regions",
            "4.5:1 contrast ratio for normal text (AA)",
            "Keyboard navigation and visible focus required",
            "Test with axe DevTools, Lighthouse, screen readers",
        ],
    },
    "z-index-stacking-context": {
        "explanation": (
            "**z-index** controls stacking order within a **stacking context** — not globally across the page. A new stacking context is created by: `position` + `z-index`, `opacity < 1`, `transform`, `filter`, `isolation: isolate`. **Why**: modals behind overlays, dropdowns clipped by parent `overflow: hidden`. **How**: modals at root level (Angular CDK Overlay); use consistent z-index scale (100, 200, 300). **Pitfall**: raising z-index on a child cannot escape parent's stacking context — move element to document root."
        ),
        "code": """/* Z-index scale — avoid arbitrary large numbers */
:root {
  --z-dropdown: 100;
  --z-sticky:   200;
  --z-modal:    300;
  --z-tooltip:  400;
}

.dropdown  { position: absolute; z-index: var(--z-dropdown); }
.modal     { position: fixed; z-index: var(--z-modal); }

/* Stacking context trap — z-index: 9999 won't help */
.card {
  transform: translateZ(0); /* creates new stacking context */
  overflow: hidden;         /* clips dropdown inside card */
}

/* Fix: render dropdown via CDK Overlay at document root */
/* Angular: <div cdkOverlayOrigin> + Overlay service */""",
        "language": "css",
        "key_points": [
            "z-index only compares within same stacking context",
            "position+ z-index, transform, opacity create new contexts",
            "Use consistent z-index scale — not z-index: 9999",
            "Modals/dropdowns should render at document root",
            "overflow: hidden on parent clips z-indexed children",
        ],
    },
}
