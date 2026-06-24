"""Additional database & EF Core interview topics — expands database section to 50+."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("database", "foundation"): [
        InterviewItem(
            "sql-cte",
            "What are Common Table Expressions (CTEs) in SQL?",
            "Named temporary result sets defined with WITH — improve readability for multi-step queries.",
            "",
        ),
        InterviewItem(
            "sql-subqueries",
            "Explain correlated vs non-correlated subqueries in SQL.",
            "Subqueries nest inside WHERE, FROM, or SELECT — correlated subqueries reference outer rows.",
            "",
        ),
        InterviewItem(
            "sql-union",
            "What is the difference between UNION and UNION ALL?",
            "UNION removes duplicates; UNION ALL concatenates all rows — faster when duplicates are acceptable.",
            "",
        ),
        InterviewItem(
            "sql-self-join",
            "What is a self-join and when do you use it?",
            "Join a table to itself — org hierarchies, comparing rows within the same table.",
            "",
        ),
        InterviewItem(
            "clustered-nonclustered-index",
            "Compare clustered vs nonclustered indexes in SQL Server.",
            "Clustered index defines physical row order (one per table); nonclustered indexes are separate B-tree structures.",
            "",
        ),
    ],
    ("database", "intermediate"): [
        InterviewItem(
            "covering-indexes",
            "What is a covering index and how does INCLUDE help?",
            "Index contains all columns needed by a query — avoids key lookups to the base table.",
            "",
        ),
        InterviewItem(
            "sql-deadlocks",
            "What causes SQL deadlocks and how do you prevent them?",
            "Circular lock waits between transactions — consistent lock order, shorter transactions, retry logic.",
            "",
        ),
        InterviewItem(
            "optimistic-concurrency-rowversion",
            "How does optimistic concurrency with RowVersion work in EF Core?",
            "RowVersion/timestamp column detects concurrent updates — SaveChanges throws DbUpdateConcurrencyException.",
            "",
        ),
        InterviewItem(
            "database-replication",
            "Explain SQL Server replication and Always On availability groups.",
            "Replication copies data to subscribers; AGs provide HA failover with shared or distributed storage.",
            "",
        ),
        InterviewItem(
            "backup-restore",
            "Describe SQL Server backup types and restore strategies.",
            "Full, differential, and log backups — point-in-time restore and recovery models (Simple vs Full).",
            "",
        ),
        InterviewItem(
            "ef-relationships",
            "Configure one-to-many and many-to-many relationships in EF Core.",
            "Fluent API or conventions map FK columns and join entities for M:N in EF Core 5+.",
            "",
        ),
        InterviewItem(
            "split-queries",
            "What are split queries in EF Core and when use AsSplitQuery?",
            "EF splits Include chains into multiple SQL queries — avoids cartesian explosion on collection includes.",
            "",
        ),
        InterviewItem(
            "query-hints-nolock",
            "What does the NOLOCK hint do and what are the risks?",
            "READ UNCOMMITTED via table hint — dirty reads, phantom rows; use only for approximate reporting.",
            "",
        ),
    ],
    ("database", "advanced"): [
        InterviewItem(
            "ef-interceptors",
            "What are EF Core interceptors and common use cases?",
            "Hooks into command/connection/save pipeline — auditing, slow-query logging, tenant filtering.",
            "",
        ),
        InterviewItem(
            "ientity-type-configuration",
            "How does IEntityTypeConfiguration<T> organize EF Core mappings?",
            "Separate configuration classes per entity — keeps OnModelCreating clean and testable.",
            "",
        ),
        InterviewItem(
            "seed-data",
            "How do you seed initial data in EF Core migrations?",
            "HasData in OnModelCreating or migrationBuilder.InsertData — idempotent seed scripts for prod.",
            "",
        ),
        InterviewItem(
            "ef-retry-strategy",
            "Configure EF Core execution strategy and retry for transient failures.",
            "SqlServerRetryingExecutionStrategy wraps SaveChanges for deadlocks and connection blips.",
            "",
        ),
        InterviewItem(
            "specification-pattern",
            "What is the Specification pattern with EF Core repositories?",
            "Encapsulates query criteria as reusable, composable objects — keeps repositories thin.",
            "",
        ),
        InterviewItem(
            "temporal-tables",
            "What are SQL Server system-versioned temporal tables?",
            "Automatic history tracking — current and history tables with ValidFrom/ValidTo columns.",
            "",
        ),
        InterviewItem(
            "json-columns-sqlserver",
            "How do you map and query JSON columns in SQL Server with EF Core?",
            "JSON column type with OPENJSON, JSON_VALUE, and EF Core 8+ JSON column mapping.",
            "",
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "sql-cte": {
        "explanation": (
            "A **Common Table Expression (CTE)** is a named temporary result set defined with `WITH` that exists "
            "only for the duration of a single statement. CTEs improve **readability** for multi-step queries, "
            "enable **recursive hierarchies** (org charts, bill-of-materials), and can be referenced multiple "
            "times in the same query. Unlike temp tables, CTEs are not materialized (usually inlined by the optimizer). "
            "**When to use:** replace nested subqueries, build intermediate aggregates, or walk trees with "
            "`WITH RECURSIVE` (PostgreSQL) / recursive CTE (SQL Server). **Pitfall:** deep recursion without "
            "MAXRECURSION guard can run forever."
        ),
        "code": """-- Non-recursive CTE — top customers by revenue
WITH CustomerRevenue AS (
    SELECT CustomerId, SUM(Total) AS Revenue
    FROM Orders
    WHERE OrderDate >= '2025-01-01'
    GROUP BY CustomerId
)
SELECT c.Name, cr.Revenue
FROM CustomerRevenue cr
INNER JOIN Customers c ON c.Id = cr.CustomerId
WHERE cr.Revenue > 10000
ORDER BY cr.Revenue DESC;

-- Recursive CTE — employee hierarchy
WITH OrgChart AS (
    SELECT Id, Name, ManagerId, 0 AS Level
    FROM Employees WHERE ManagerId IS NULL
    UNION ALL
    SELECT e.Id, e.Name, e.ManagerId, oc.Level + 1
    FROM Employees e
    INNER JOIN OrgChart oc ON e.ManagerId = oc.Id
)
SELECT * FROM OrgChart ORDER BY Level, Name;""",
        "language": "sql",
        "key_points": [
            "WITH clause defines one or more CTEs before the main SELECT",
            "Recursive CTE: anchor member UNION ALL recursive member",
            "Improves readability vs deeply nested subqueries",
            "SQL Server OPTION (MAXRECURSION 100) limits recursion depth",
        ],
    },
    "sql-subqueries": {
        "explanation": (
            "A **subquery** is a query nested inside another query — in `WHERE`, `FROM`, `SELECT`, or `HAVING`. "
            "**Non-correlated** subqueries run independently and execute once. **Correlated** subqueries reference "
            "columns from the outer query and execute per outer row — often slower but expressive. "
            "**EXISTS** is preferred over `IN` for large sets when checking existence (short-circuits). "
            "Modern SQL often replaces subqueries with **JOINs** or **CTEs** for clarity and optimizer flexibility. "
            "In EF Core, subqueries translate to SQL subselects when using `.Where(x => context.Other.Any(...))`."
        ),
        "code": """-- Non-correlated — orders above average total
SELECT Id, CustomerId, Total
FROM Orders
WHERE Total > (SELECT AVG(Total) FROM Orders);

-- Correlated — customers with at least one high-value order
SELECT c.Id, c.Name
FROM Customers c
WHERE EXISTS (
    SELECT 1 FROM Orders o
    WHERE o.CustomerId = c.Id AND o.Total > 500
);

-- EF Core translates to subquery
var customers = await _db.Customers
    .Where(c => c.Orders.Any(o => o.Total > 500))
    .ToListAsync();""",
        "language": "sql",
        "key_points": [
            "Non-correlated runs once; correlated references outer row",
            "EXISTS often outperforms IN for large datasets",
            "CTEs and JOINs often replace complex subqueries",
            "EF Core LINQ generates subqueries for Any/All patterns",
        ],
    },
    "sql-union": {
        "explanation": (
            "**UNION** combines result sets from two or more SELECT statements with **identical column count and "
            "compatible types**. **UNION** (default) removes duplicate rows — requires a sort/distinct pass. "
            "**UNION ALL** keeps all rows including duplicates — **faster** when you know sets are disjoint or "
            "duplicates are acceptable. **Use cases:** merge active and archived tables, combine regional datasets, "
            "build report totals. **ORDER BY** applies to the final combined result (only one ORDER BY at the end). "
            "**Interview tip:** prefer UNION ALL unless you explicitly need deduplication."
        ),
        "code": """-- UNION ALL — faster, keeps duplicates
SELECT Id, Name, 'Active' AS Source FROM ActiveCustomers
UNION ALL
SELECT Id, Name, 'Archived' AS Source FROM ArchivedCustomers;

-- UNION — deduplicates (slower)
SELECT ProductId FROM OrderLines2024
UNION
SELECT ProductId FROM OrderLines2025;

-- Combined with CTE for reporting
WITH AllOrders AS (
    SELECT CustomerId, Total FROM Orders2024
    UNION ALL
    SELECT CustomerId, Total FROM Orders2025
)
SELECT CustomerId, SUM(Total) AS LifetimeSpend
FROM AllOrders
GROUP BY CustomerId;""",
        "language": "sql",
        "key_points": [
            "Column count and types must match across SELECTs",
            "UNION removes duplicates; UNION ALL is faster",
            "Single ORDER BY applies to final combined result",
            "Common for merging partitioned or archived data",
        ],
    },
    "sql-self-join": {
        "explanation": (
            "A **self-join** joins a table to itself using table **aliases** — essential when rows relate to "
            "other rows in the same table. Classic examples: **employee/manager hierarchy**, finding duplicate "
            "records, sequential events (compare each order to the previous), and **adjacency list** patterns. "
            "Recursive CTEs often replace deep self-join chains for hierarchies. In EF Core, self-referencing "
            "relationships use `HasOne/WithMany` pointing to the same entity type with a nullable FK (ManagerId)."
        ),
        "code": """-- Employee and their manager names
SELECT e.Name AS Employee, m.Name AS Manager
FROM Employees e
LEFT JOIN Employees m ON e.ManagerId = m.Id;

-- Find duplicate emails
SELECT a.Email, a.Id AS Id1, b.Id AS Id2
FROM Users a
INNER JOIN Users b ON a.Email = b.Email AND a.Id < b.Id;

-- EF Core self-referencing relationship
public class Employee {
    public int Id { get; set; }
    public string Name { get; set; } = "";
    public int? ManagerId { get; set; }
    public Employee? Manager { get; set; }
    public List<Employee> DirectReports { get; set; } = [];
}
// modelBuilder.Entity<Employee>()
//     .HasOne(e => e.Manager).WithMany(e => e.DirectReports)
//     .HasForeignKey(e => e.ManagerId);""",
        "language": "sql",
        "key_points": [
            "Use table aliases — join table to itself",
            "Common for hierarchies, duplicates, sequential comparisons",
            "Recursive CTEs scale better than chained self-joins",
            "EF Core maps self-referencing FK relationships",
        ],
    },
    "clustered-nonclustered-index": {
        "explanation": (
            "SQL Server indexes are **B-tree** structures speeding data retrieval. A **clustered index** defines "
            "the **physical sort order** of table rows — only **one per table** (usually the primary key). "
            "Leaf pages contain the actual data rows. A **nonclustered index** is a separate structure with "
            "index key + pointer (row locator) to clustered index or heap. **Heap** = table with no clustered index. "
            "**Choose clustered on:** primary key or most common range-scan column. **Nonclustered on:** FK columns, "
            "WHERE/JOIN/ORDER BY columns. Too many indexes slow INSERT/UPDATE/DELETE."
        ),
        "code": """-- Clustered index on PK (default when PK defined)
CREATE TABLE Orders (
    Id INT PRIMARY KEY CLUSTERED,  -- clustered by Id
    CustomerId INT NOT NULL,
    OrderDate DATE NOT NULL,
    Total DECIMAL(18,2)
);

-- Nonclustered index on FK + filter column
CREATE NONCLUSTERED INDEX IX_Orders_CustomerId_OrderDate
ON Orders (CustomerId, OrderDate);

-- Query uses clustered seek on Id, nonclustered seek on CustomerId
SELECT * FROM Orders WHERE Id = 42;
SELECT * FROM Orders WHERE CustomerId = 7 ORDER BY OrderDate DESC;""",
        "language": "sql",
        "key_points": [
            "One clustered index per table — defines physical row order",
            "Nonclustered indexes are separate B-trees with row pointers",
            "Primary key creates clustered index by default in SQL Server",
            "Index FK columns and frequent WHERE/JOIN columns",
        ],
    },
    "covering-indexes": {
        "explanation": (
            "A **covering index** includes **all columns** referenced by a query (SELECT, WHERE, JOIN, ORDER BY) "
            "so SQL Server can satisfy the query entirely from the index without a **key lookup** to the base table. "
            "Use the **INCLUDE** clause for non-key columns to avoid bloating the index key width. "
            "**Filtered indexes** (`WHERE Status = 'Active'`) further reduce size. Check execution plans for "
            "**Key Lookup** operators — sign you need a covering index. Trade-off: wider indexes cost more on writes "
            "and storage."
        ),
        "code": """-- Query: list active orders for a customer
-- SELECT OrderDate, Total FROM Orders
-- WHERE CustomerId = @id AND Status = 'Active'
-- ORDER BY OrderDate DESC;

CREATE NONCLUSTERED INDEX IX_Orders_Covering_Active
ON Orders (CustomerId, Status, OrderDate DESC)
INCLUDE (Total)
WHERE Status = 'Active';

-- Execution plan should show Index Seek + no Key Lookup
SET STATISTICS IO ON;
SELECT OrderDate, Total
FROM Orders
WHERE CustomerId = 7 AND Status = 'Active'
ORDER BY OrderDate DESC;""",
        "language": "sql",
        "key_points": [
            "INCLUDE adds non-key columns to index leaf pages",
            "Eliminates Key Lookup — index-only scan",
            "Filtered indexes reduce size for partial datasets",
            "Balance read performance vs write overhead",
        ],
    },
    "sql-deadlocks": {
        "explanation": (
            "A **deadlock** occurs when two or more transactions hold locks the others need — SQL Server detects "
            "the cycle and **kills one victim** (error 1205). Common causes: **inconsistent lock order** (Tx1 locks "
            "A then B, Tx2 locks B then A), long transactions, missing indexes causing lock escalation. "
            "**Prevention:** access tables in consistent order, keep transactions short, use appropriate isolation "
            "levels, index hot columns. **In .NET:** catch `SqlException` number 1205 and retry with backoff; "
            "EF Core `SqlServerRetryingExecutionStrategy` handles this automatically."
        ),
        "code": """// EF Core — enable automatic deadlock retry
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(connectionString, sql =>
        sql.EnableRetryOnFailure(
            maxRetryCount: 3,
            maxRetryDelay: TimeSpan.FromSeconds(5),
            errorNumbersToAdd: null)));

// Manual retry pattern
for (var attempt = 0; attempt < 3; attempt++)
{
    try
    {
        await using var tx = await _db.Database.BeginTransactionAsync();
        await _db.SaveChangesAsync();
        await tx.CommitAsync();
        break;
    }
    catch (SqlException ex) when (ex.Number == 1205)
    {
        if (attempt == 2) throw;
        await Task.Delay(100 * (attempt + 1));
    }
}""",
        "language": "csharp",
        "key_points": [
            "SQL Server picks a deadlock victim — error 1205",
            "Consistent lock ordering prevents circular waits",
            "EnableRetryOnFailure in EF Core for transient deadlocks",
            "Keep transactions short; index to avoid lock escalation",
        ],
    },
    "optimistic-concurrency-rowversion": {
        "explanation": (
            "**Optimistic concurrency** assumes conflicts are rare — no locks during read; conflict detected at "
            "save time. SQL Server **`rowversion`** (formerly timestamp) is an auto-incrementing binary column "
            "that changes on every UPDATE. EF Core maps it with `[Timestamp]` or `.IsRowVersion()`. "
            "On `SaveChanges`, EF adds `WHERE RowVersion = @original` — if zero rows affected, throws "
            "`DbUpdateConcurrencyException`. **Handle by:** reloading entity, merging changes, or notifying user. "
            "Alternative: concurrency token on a specific column (e.g., `ModifiedAt`)."
        ),
        "code": """public class Order
{
    public int Id { get; set; }
    public string Status { get; set; } = "";
    [Timestamp]
    public byte[] RowVersion { get; set; } = null!;
}

// Fluent API
modelBuilder.Entity<Order>()
    .Property(o => o.RowVersion)
    .IsRowVersion();

// Handle conflict
try
{
    order.Status = "Shipped";
    await _db.SaveChangesAsync();
}
catch (DbUpdateConcurrencyException)
{
    var dbValues = await entry.GetDatabaseValuesAsync();
    // Reload, merge, or throw to UI
    throw new ConflictException("Order was modified by another user.");
}""",
        "language": "csharp",
        "key_points": [
            "rowversion auto-updates on every row change",
            "IsRowVersion() maps SQL Server timestamp/rowversion",
            "DbUpdateConcurrencyException on stale RowVersion",
            "Prefer over pessimistic locking for web apps",
        ],
    },
    "database-replication": {
        "explanation": (
            "**SQL Server replication** copies data to subscriber databases — types include **transactional** "
            "(near real-time, OLTP), **merge** (bi-directional, occasionally connected), and **snapshot** "
            "(full copy). **Always On Availability Groups** provide **high availability** with synchronous or "
            "asynchronous replicas and automatic failover — preferred for modern HA over legacy replication. "
            "**Azure SQL** offers active geo-replication and auto-failover groups. **Read scale-out:** route "
            "reporting queries to readable secondary replicas. Know **RPO/RTO** implications of sync vs async."
        ),
        "code": """/*
  Always On Availability Group (conceptual)
  ┌─────────────┐     sync/async     ┌─────────────┐
  │  Primary    │ ─────────────────► │  Secondary  │  (readable)
  │  (read/write)│                    │  (read-only) │
  └─────────────┘                    └─────────────┘
         │ failover (automatic/manual)
         ▼
  Listener: ag-listener.contoso.com

  Azure SQL — connection string with ApplicationIntent=ReadOnly
  for reporting replica
*/
Server=tcp:myserver.database.windows.net;Database=Orders;
ApplicationIntent=ReadOnly;""",
        "language": "text",
        "key_points": [
            "Transactional replication for near-real-time OLTP copies",
            "Always On AGs — HA with automatic failover",
            "Azure SQL geo-replication for DR and read scale-out",
            "Sync replicas: zero data loss; async: lower latency impact",
        ],
    },
    "backup-restore": {
        "explanation": (
            "SQL Server **backup strategy** protects against data loss and enables point-in-time recovery. "
            "**Full backup** captures entire database. **Differential** captures changes since last full. "
            "**Transaction log backup** (Full recovery model) enables **point-in-time restore** between fulls. "
            "**Recovery models:** Simple (no log backups, minimal storage), Full (complete PITR), Bulk-logged "
            "(bulk operations minimal logging). **Azure SQL** automates backups with configurable retention. "
            "**Test restores regularly** — an untested backup is not a backup."
        ),
        "code": """-- Full + log backup chain (on-premises)
BACKUP DATABASE OrderDb
TO DISK = 'D:\\Backups\\OrderDb_Full.bak'
WITH COMPRESSION, CHECKSUM;

BACKUP LOG OrderDb
TO DISK = 'D:\\Backups\\OrderDb_Log.trn';

-- Point-in-time restore
RESTORE DATABASE OrderDb FROM DISK = 'OrderDb_Full.bak' WITH NORECOVERY;
RESTORE LOG OrderDb FROM DISK = 'OrderDb_Log1.trn' WITH NORECOVERY;
RESTORE LOG OrderDb FROM DISK = 'OrderDb_Log2.trn'
WITH RECOVERY, STOPAT = '2025-06-15 14:30:00';""",
        "language": "sql",
        "key_points": [
            "Full + differential + log backups for PITR",
            "Simple recovery model — no log backups",
            "Azure SQL: automated backups, LTR for compliance",
            "Test restore procedures — validate RPO/RTO",
        ],
    },
    "ef-relationships": {
        "explanation": (
            "EF Core maps relational relationships via **conventions** or **Fluent API**. **One-to-many:** FK on "
            "dependent entity (`Order.CustomerId`). **One-to-one:** FK on dependent side, unique constraint. "
            "**Many-to-many (EF Core 5+):** skip entity — EF creates join table automatically; or explicit "
            "**join entity** for payload columns (Quantity, AssignedDate). Configure with `HasOne/WithMany`, "
            "`HasMany/WithMany`, `UsingEntity`. **Cascade delete** behavior must be chosen explicitly — "
            "`DeleteBehavior.Restrict` is safer for production than Cascade on deep graphs."
        ),
        "code": """// One-to-many
modelBuilder.Entity<Order>()
    .HasOne(o => o.Customer)
    .WithMany(c => c.Orders)
    .HasForeignKey(o => o.CustomerId)
    .OnDelete(DeleteBehavior.Restrict);

// Many-to-many with explicit join entity (payload)
modelBuilder.Entity<StudentCourse>()
    .HasKey(sc => new { sc.StudentId, sc.CourseId });

modelBuilder.Entity<StudentCourse>()
    .HasOne(sc => sc.Student).WithMany(s => s.Enrollments)
    .HasForeignKey(sc => sc.StudentId);

// Many-to-many without join entity (EF 5+)
modelBuilder.Entity<Post>()
    .HasMany(p => p.Tags)
    .WithMany(t => t.Posts);""",
        "language": "csharp",
        "key_points": [
            "FK column lives on the many side of 1:N",
            "Explicit join entity when M:N has extra columns",
            "DeleteBehavior.Restrict prevents accidental cascades",
            "Include() loads related entities — watch N+1",
        ],
    },
    "split-queries": {
        "explanation": (
            "When EF Core loads multiple **`Include()`** collection navigations, a single SQL JOIN can produce a "
            "**cartesian explosion** — duplicate parent rows multiplied by child counts, wasting bandwidth and memory. "
            "**Split queries** (`AsSplitQuery()`) issue **separate SQL queries** per collection include — one for "
            "parents, one per collection. Default is single query since EF Core 5. Enable globally with "
            "`UseQuerySplittingBehavior(QuerySplittingBehavior.SplitQuery)`. **Trade-off:** split queries mean "
            "multiple round trips — fine for large graphs, worse for small/simple includes over high-latency links."
        ),
        "code": """// Single query — cartesian product risk with two collections
var orders = await _db.Orders
    .Include(o => o.Lines)
    .Include(o => o.Payments)  // Lines × Payments row explosion
    .ToListAsync();

// Split query — 3 SQL statements, no duplication
var orders = await _db.Orders
    .AsSplitQuery()
    .Include(o => o.Lines)
    .Include(o => o.Payments)
    .AsNoTracking()
    .ToListAsync();

// Global default in Program.cs
options.UseSqlServer(cs, o => o.UseQuerySplittingBehavior(
    QuerySplittingBehavior.SplitQuery));""",
        "language": "csharp",
        "key_points": [
            "Cartesian explosion from multiple collection Includes",
            "AsSplitQuery() — separate SQL per collection",
            "Multiple round trips vs single bloated result",
            "Use AsNoTracking for read-only split queries",
        ],
    },
    "query-hints-nolock": {
        "explanation": (
            "The **`WITH (NOLOCK)`** table hint (equivalent to **READ UNCOMMITTED** isolation) allows reading "
            "rows without acquiring shared locks — readers don't block writers and vice versa. **Use case:** "
            "approximate reporting dashboards where **dirty reads** are acceptable. **Risks:** read uncommitted "
            "data, **phantom rows**, reading rows that get rolled back, duplicate/missing rows during page splits. "
            "**Never use NOLOCK** for financial transactions or authoritative counts. Prefer **READ COMMITTED SNAPSHOT "
            "(RCSI)** for read/write concurrency without dirty reads."
        ),
        "code": """-- NOLOCK hint — dirty reads possible
SELECT COUNT(*) AS ActiveOrders
FROM Orders WITH (NOLOCK)
WHERE Status = 'Active';

-- Better alternative — enable RCSI at database level
ALTER DATABASE OrderDb SET READ_COMMITTED_SNAPSHOT ON;
-- Readers use row versions, no shared locks, no dirty reads

-- EF Core — raw SQL only (no LINQ equivalent)
var count = await _db.Orders
    .FromSqlRaw("SELECT * FROM Orders WITH (NOLOCK) WHERE Status = {0}", "Active")
    .CountAsync(); // avoid — prefer RCSI instead""",
        "language": "sql",
        "key_points": [
            "NOLOCK = READ UNCOMMITTED — allows dirty reads",
            "Acceptable only for approximate/non-critical reporting",
            "RCSI is the safer concurrency alternative",
            "Never use for financial or authoritative data",
        ],
    },
    "ef-interceptors": {
        "explanation": (
            "EF Core **interceptors** hook into the pipeline at four levels: **DbCommand** (SQL logging, retry, "
            "tenant injection), **DbConnection** (connection open/close auditing), **DbTransaction**, and "
            "**SaveChanges**. Register with `AddInterceptors()` or `options.AddInterceptors()`. "
            "**Use cases:** slow-query logging, automatic **CreatedAt/UpdatedAt** stamps, soft-delete enforcement, "
            "multi-tenant connection switching, SQL command sanitization. Interceptors replace older "
            "IDbCommandInterceptor patterns and work with both sync and async paths via Async methods."
        ),
        "code": """public class AuditInterceptor : SaveChangesInterceptor
{
    public override InterceptionResult<int> SavingChanges(
        DbContextEventData eventData,
        InterceptionResult<int> result)
    {
        var entries = eventData.Context!.ChangeTracker.Entries<IAuditable>();
        foreach (var entry in entries)
        {
            if (entry.State == EntityState.Added)
                entry.Entity.CreatedAt = DateTime.UtcNow;
            if (entry.State == EntityState.Modified)
                entry.Entity.UpdatedAt = DateTime.UtcNow;
        }
        return base.SavingChanges(eventData, result);
    }
}

// Registration
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(cs)
           .AddInterceptors(new AuditInterceptor()));""",
        "language": "csharp",
        "key_points": [
            "SaveChangesInterceptor for audit fields and validation",
            "DbCommandInterceptor for SQL logging and hints",
            "Register via AddInterceptors in DbContext options",
            "Supports both sync and async interception methods",
        ],
    },
    "ientity-type-configuration": {
        "explanation": (
            "`IEntityTypeConfiguration<TEntity>` separates **Fluent API mapping** into dedicated classes — "
            "keeps `OnModelCreating` readable in large domains. Implement `Configure(EntityTypeBuilder<T> builder)` "
            "with property constraints, relationships, indexes, and seed data. Apply with "
            "`modelBuilder.ApplyConfigurationsFromAssembly(typeof(AppDbContext).Assembly)`. "
            "**Benefits:** single responsibility per entity, easier unit testing of mappings, discoverable via "
            "convention-based assembly scanning. One configuration class per aggregate root is a common pattern."
        ),
        "code": """public class OrderConfiguration : IEntityTypeConfiguration<Order>
{
    public void Configure(EntityTypeBuilder<Order> builder)
    {
        builder.ToTable("Orders");
        builder.HasKey(o => o.Id);
        builder.Property(o => o.Total).HasPrecision(18, 2);
        builder.Property(o => o.Status).HasMaxLength(20).IsRequired();
        builder.HasIndex(o => new { o.CustomerId, o.OrderDate });
        builder.HasOne(o => o.Customer)
            .WithMany(c => c.Orders)
            .HasForeignKey(o => o.CustomerId);
    }
}

// AppDbContext
protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    modelBuilder.ApplyConfigurationsFromAssembly(typeof(AppDbContext).Assembly);
}""",
        "language": "csharp",
        "key_points": [
            "One configuration class per entity — clean OnModelCreating",
            "ApplyConfigurationsFromAssembly auto-discovers configs",
            "Configure indexes, precision, relationships, table names",
            "Supports testing mapping rules in isolation",
        ],
    },
    "seed-data": {
        "explanation": (
            "EF Core **seed data** populates lookup tables and default records via migrations. Use `HasData()` "
            "in `IEntityTypeConfiguration` or `OnModelCreating` — EF generates `InsertData`/`DeleteData` in "
            "migration files. **Requirements:** must specify primary key values; entities need parameterless "
            "constructors or use anonymous objects. **Production:** prefer **idempotent SQL scripts** or "
            "dedicated seed commands over `MigrateAsync()` on startup. **`migrationBuilder.InsertData`** for "
            "manual migration seeding. Re-running migrations applies seed changes idempotently."
        ),
        "code": """public class RoleConfiguration : IEntityTypeConfiguration<Role>
{
    public void Configure(EntityTypeBuilder<Role> builder)
    {
        builder.HasData(
            new Role { Id = 1, Name = "Admin" },
            new Role { Id = 2, Name = "User" },
            new Role { Id = 3, Name = "ReadOnly" }
        );
    }
}

// dotnet ef migrations add SeedRoles
// Generated migration contains:
// migrationBuilder.InsertData(table: "Roles", columns: ..., values: ...);

// Dev-only auto-migrate (never in production)
if (app.Environment.IsDevelopment())
    await db.Database.MigrateAsync();""",
        "language": "csharp",
        "key_points": [
            "HasData() embeds seed data in migrations",
            "Must provide explicit primary key values",
            "Idempotent via migration history — not raw INSERT",
            "Never auto-migrate production on app startup",
        ],
    },
    "ef-retry-strategy": {
        "explanation": (
            "Cloud databases encounter **transient faults** — throttling, failover, deadlocks, connection drops. "
            "EF Core **execution strategies** wrap operations in retry logic. `SqlServerRetryingExecutionStrategy` "
            "retries on error numbers 4060, 40197, 40501, 40613, 49918, 49919, 49920, 1205, etc. Configure with "
            "`EnableRetryOnFailure(maxRetryCount, maxRetryDelay, errorNumbersToAdd)`. "
            "**Important:** user-initiated transactions must run inside `strategy.ExecuteAsync()` — "
            "retries cannot resume a failed transaction automatically."
        ),
        "code": """builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(connectionString, sqlOptions =>
        sqlOptions.EnableRetryOnFailure(
            maxRetryCount: 5,
            maxRetryDelay: TimeSpan.FromSeconds(30),
            errorNumbersToAdd: null)));

// Manual transaction with execution strategy
var strategy = _db.Database.CreateExecutionStrategy();
await strategy.ExecuteAsync(async () =>
{
    await using var tx = await _db.Database.BeginTransactionAsync();
    _db.Orders.Add(order);
    await _db.SaveChangesAsync();
    await tx.CommitAsync();
});""",
        "language": "csharp",
        "key_points": [
            "EnableRetryOnFailure for Azure SQL and transient errors",
            "Wrap manual transactions in CreateExecutionStrategy()",
            "Retries deadlocks (1205) and connection failures",
            "Not a substitute for idempotent business logic",
        ],
    },
    "specification-pattern": {
        "explanation": (
            "The **Specification pattern** encapsulates query criteria as reusable, composable objects — "
            "decoupling repositories from LINQ details. Define `ISpecification<T>` with `Criteria` (Expression), "
            "`Includes`, `OrderBy`, and `Paging`. Compose specs with **AND/OR** (`AndSpecification`). "
            "**Benefits:** DRY query logic, testable criteria, clean repository interface (`GetBySpecAsync`). "
            "Libraries like **Ardalis.Specification** provide base classes integrated with EF Core. "
            "Alternative: inline `IQueryable` extension methods for simpler apps."
        ),
        "code": """public interface ISpecification<T>
{
    Expression<Func<T, bool>> Criteria { get; }
    List<Expression<Func<T, object>>> Includes { get; }
}

public class ActiveOrdersSpec : Specification<Order>
{
    public ActiveOrdersSpec(int customerId) =>
        Query.Where(o => o.CustomerId == customerId && o.Status == "Active")
             .Include(o => o.Lines)
             .OrderByDescending(o => o.OrderDate);
}

// Repository
public async Task<List<Order>> GetBySpecAsync(ISpecification<Order> spec) =>
    await ApplySpecification(spec).ToListAsync();

private IQueryable<Order> ApplySpecification(ISpecification<Order> spec) =>
    spec.Includes.Aggregate(_db.Orders.AsQueryable(),
        (query, include) => query.Include(include))
    .Where(spec.Criteria);""",
        "language": "csharp",
        "key_points": [
            "Encapsulates query criteria away from repositories",
            "Composable with AND/OR for complex filters",
            "Ardalis.Specification is popular in .NET ecosystem",
            "Keeps controllers/services free of LINQ details",
        ],
    },
    "temporal-tables": {
        "explanation": (
            "SQL Server **system-versioned temporal tables** automatically track **row history** — every UPDATE "
            "and DELETE moves the old row to a **history table** with `ValidFrom`/`ValidTo` period columns. "
            "Query past states with `FOR SYSTEM_TIME AS OF '2025-01-15'`. **Use cases:** audit trails, "
            "regulatory compliance, point-in-time reporting without custom triggers. EF Core 6+ supports "
            "temporal tables via `.ToTable(tb => tb.IsTemporal())`. **Storage cost:** history table grows "
            "unbounded — define retention policies."
        ),
        "code": """-- Create temporal table
CREATE TABLE Orders (
    Id INT PRIMARY KEY,
    Status NVARCHAR(20),
    Total DECIMAL(18,2),
    ValidFrom DATETIME2 GENERATED ALWAYS AS ROW START,
    ValidTo   DATETIME2 GENERATED ALWAYS AS ROW END,
    PERIOD FOR SYSTEM_TIME (ValidFrom, ValidTo)
) WITH (SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.OrdersHistory));

-- Query as of a past date
SELECT * FROM Orders
FOR SYSTEM_TIME AS OF '2025-06-01T00:00:00'
WHERE Id = 42;

// EF Core 6+
modelBuilder.Entity<Order>().ToTable("Orders", tb => tb.IsTemporal());""",
        "language": "sql",
        "key_points": [
            "Automatic history on UPDATE/DELETE — no triggers needed",
            "FOR SYSTEM_TIME AS OF queries past row versions",
            "EF Core IsTemporal() maps system-versioned tables",
            "Plan history table retention and storage growth",
        ],
    },
    "json-columns-sqlserver": {
        "explanation": (
            "SQL Server **`NVARCHAR` JSON columns** (with `ISJSON` check constraint) store semi-structured data "
            "without schema migrations for every new attribute. Query with **`JSON_VALUE`**, **`JSON_QUERY`**, "
            "**`OPENJSON`**, and **`JSON_MODIFY`**. EF Core 7+ maps JSON columns to owned types or "
            "`Dictionary<string, object>`. **Use when:** flexible metadata, feature flags, user preferences. "
            "**Avoid when:** data needs FK constraints, frequent relational joins, or strict schema validation — "
            "use normalized columns instead."
        ),
        "code": """CREATE TABLE Orders (
    Id INT PRIMARY KEY,
    Metadata NVARCHAR(MAX) CONSTRAINT CK_Orders_Metadata CHECK (ISJSON(Metadata) = 1)
);

INSERT INTO Orders (Id, Metadata)
VALUES (1, '{\"priority\": \"high\", \"source\": \"mobile\"}');

-- Query JSON properties
SELECT Id, JSON_VALUE(Metadata, '$.priority') AS Priority
FROM Orders
WHERE JSON_VALUE(Metadata, '$.priority') = 'high';

// EF Core 8 — map owned type to JSON column
modelBuilder.Entity<Order>()
    .OwnsOne(o => o.Metadata, nav => nav.ToJson());""",
        "language": "sql",
        "key_points": [
            "JSON_VALUE for scalars; JSON_QUERY for objects/arrays",
            "ISJSON check constraint validates column content",
            "EF Core ToJson() maps owned types to JSON columns",
            "Not a replacement for normalized relational design",
        ],
    },
}
