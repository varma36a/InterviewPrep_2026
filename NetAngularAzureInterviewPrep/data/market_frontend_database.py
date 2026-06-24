"""Market-relevant Angular/TypeScript and Database interview topics (2025/2026)."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("frontend", "foundation"): [
        InterviewItem(
            "standalone-components",
            "What are standalone components in Angular and why use them?",
            "Standalone components declare their own imports instead of NgModule. "
            "They are the default in Angular 19+ and simplify bootstrapping, lazy loading, and tree-shaking.",
            """@Component({
  selector: 'app-order-card',
  standalone: true,
  imports: [CommonModule, MatButtonModule],
  template: `<button mat-button>{{ order.id }}</button>`
})
export class OrderCardComponent {
  @Input({ required: true }) order!: Order;
}""",
            "typescript",
            key_points=["No NgModule required", "imports array replaces module imports", "Default in new Angular projects"],
        ),
        InterviewItem(
            "control-flow",
            "Explain Angular's built-in control flow (@if, @for, @switch).",
            "Angular 17+ replaces *ngIf, *ngFor with @if/@for/@switch — better type checking and performance.",
            """@Component({
  template: `
    @if (orders$ | async; as orders) {
      @for (o of orders; track o.id) {
        <app-order-row [order]="o" />
      } @empty { <p>No orders</p> }
    } @else { <app-spinner /> }
  `
})
export class OrderListComponent {}""",
            "typescript",
            key_points=["track expression required in @for", "@empty block for empty collections", "Better compile-time checks than structural directives"],
        ),
        InterviewItem(
            "lifecycle-hooks",
            "Explain Angular component lifecycle hooks and when to use each.",
            "Hooks run at specific points: init, changes, content checks, view checks, destroy. "
            "Use ngOnInit for setup, ngOnDestroy for cleanup.",
            """export class OrdersComponent implements OnInit, OnDestroy {
  private destroy$ = new Subject<void>();

  ngOnInit() {
    this.orders$ = this.service.getOrders()
      .pipe(takeUntil(this.destroy$));
  }

  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }
}""",
            "typescript",
            key_points=["ngOnChanges for @Input reference changes", "ngAfterViewInit when ViewChild is ready", "Always unsubscribe in ngOnDestroy"],
        ),
        InterviewItem(
            "input-output",
            "How do @Input and @Output work in Angular?",
            "@Input passes data parent → child. @Output emits events child → parent via EventEmitter.",
            """@Component({ selector: 'app-order-row', template: `...` })
export class OrderRowComponent {
  @Input({ required: true }) order!: Order;
  @Output() delete = new EventEmitter<number>();

  onDelete() { this.delete.emit(this.order.id); }
}

// Parent: <app-order-row [order]="o" (delete)="remove($event)" />""",
            "typescript",
            key_points=["required: true for mandatory inputs", "Prefer signals input()/output() in Angular 17.1+", "Never mutate @Input objects in place with OnPush"],
        ),
        InterviewItem(
            "pipes",
            "What are Angular pipes? Built-in vs custom pipes?",
            "Pipes transform template values. Pure pipes recalculate only on reference change; impure on every CD cycle.",
            """@Pipe({ name: 'currencyLocale', standalone: true })
export class CurrencyLocalePipe implements PipeTransform {
  transform(value: number, locale = 'en-US'): string {
    return new Intl.NumberFormat(locale, { style: 'currency', currency: 'USD' }).format(value);
  }
}
// Template: {{ order.total | currencyLocale:'en-GB' }}""",
            "typescript",
            key_points=["async pipe subscribes to Observables", "Pure pipes are performant by default", "DatePipe, CurrencyPipe, JsonPipe built-in"],
        ),
        InterviewItem(
            "ts-generics",
            "Explain TypeScript generics with Angular examples.",
            "Generics create reusable, type-safe abstractions. Angular uses them in HttpClient, services, and components.",
            """interface ApiResponse<T> { data: T; meta: { total: number }; }

@Injectable({ providedIn: 'root' })
export class ApiService {
  constructor(private http: HttpClient) {}
  getList<T>(url: string): Observable<T[]> {
    return this.http.get<ApiResponse<T[]>>(url).pipe(map(r => r.data));
  }
}""",
            "typescript",
            key_points=["Constraints: extends, keyof", "Generic components: ListComponent<T>", "Avoid any — generics preserve type flow"],
        ),
    ],
    ("frontend", "intermediate"): [
        InterviewItem(
            "angular-signals",
            "What are Angular Signals and how do they differ from Observables?",
            "Signals are synchronous reactive primitives with fine-grained updates. "
            "computed() derives values; effect() runs side effects.",
            """@Component({ selector: 'app-cart', template: `Total: {{ total() }}` })
export class CartComponent {
  items = signal<CartItem[]>([]);
  total = computed(() => this.items().reduce((s, i) => s + i.price * i.qty, 0));

  addItem(item: CartItem) {
    this.items.update(list => [...list, item]);
  }
}""",
            "typescript",
            key_points=["signal(), computed(), effect()", "toSignal() bridges Observable → signal", "OnPush works naturally with signals"],
        ),
        InterviewItem(
            "defer-blocks",
            "What are @defer blocks in Angular?",
            "@defer lazy-loads template sections on triggers (viewport, idle, interaction) — improves initial bundle and LCP.",
            """@Component({
  template: `
    @defer (on viewport) {
      <app-heavy-chart [data]="chartData" />
    } @placeholder { <div class="skeleton" /> }
    @loading (minimum 300ms) { <app-spinner /> }
    @error { <p>Chart failed to load</p> }
  `
})
export class DashboardComponent {}""",
            "typescript",
            key_points=["Triggers: on idle, on viewport, on interaction", "Splits code into separate chunks", "placeholder/loading/error blocks customize UX"],
        ),
        InterviewItem(
            "inject-function",
            "How does the inject() function work in Angular?",
            "inject() enables functional DI outside constructors — guards, interceptors, resolvers, and field initializers.",
            """export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);
  return auth.isLoggedIn() ? true : router.createUrlTree(['/login']);
};

@Component({ /* ... */ })
export class ProfileComponent {
  private auth = inject(AuthService);
  user = toSignal(this.auth.currentUser$);
}""",
            "typescript",
            key_points=["Works in injection context only", "Preferred for functional guards/interceptors", "Replaces constructor DI in many cases"],
        ),
        InterviewItem(
            "http-interceptors",
            "How do HTTP interceptors work in Angular?",
            "Interceptors sit in the HttpClient pipeline — add auth headers, handle errors, log requests globally.",
            """export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(AuthService).getToken();
  if (token) {
    req = req.clone({ setHeaders: { Authorization: `Bearer ${token}` } });
  }
  return next(req).pipe(
    catchError(err => err.status === 401 ? inject(Router).navigate(['/login']) : throwError(() => err))
  );
};
// provideHttpClient(withInterceptors([authInterceptor]))""",
            "typescript",
            key_points=["Functional interceptors (HttpInterceptorFn) in Angular 15+", "Order matters in interceptor chain", "Clone requests — they are immutable"],
        ),
        InterviewItem(
            "route-guards-resolvers",
            "Explain route guards and resolvers in Angular routing.",
            "Guards control navigation (canActivate, canDeactivate). Resolvers prefetch data before route activation.",
            """export const orderResolver: ResolveFn<Order> = (route) =>
  inject(OrderService).getById(+route.paramMap.get('id')!);

const routes: Routes = [{
  path: 'orders/:id',
  component: OrderDetailComponent,
  canActivate: [authGuard],
  resolve: { order: orderResolver }
}];""",
            "typescript",
            key_points=["CanActivateFn returns boolean | UrlTree", "Resolver data available in route.snapshot.data", "canMatch for route matching logic"],
        ),
        InterviewItem(
            "directives",
            "What is the difference between structural and attribute directives?",
            "Structural directives change DOM layout (*ngIf → @if). Attribute directives change appearance/behavior of elements.",
            """@Directive({ selector: '[appHighlight]', standalone: true })
export class HighlightDirective {
  constructor(private el: ElementRef, private renderer: Renderer2) {}
  @Input() set appHighlight(color: string) {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', color);
  }
}
// <tr appHighlight="yellow" *ngFor="let o of orders">""",
            "typescript",
            key_points=["Structural: @if, @for, ng-template", "Attribute: ngClass, ngStyle, custom", "HostListener for DOM events"],
        ),
        InterviewItem(
            "angular-unit-testing",
            "How do you unit test Angular components and services?",
            "Use TestBed to configure module/standalone imports. Mock HttpClient with HttpClientTestingModule. Jasmine or Jest.",
            """describe('OrderService', () => {
  let service: OrderService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [OrderService, provideHttpClient(), provideHttpClientTesting()]
    });
    service = TestBed.inject(OrderService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it('fetches orders', () => {
    service.getOrders().subscribe(orders => expect(orders.length).toBe(1));
    httpMock.expectOne('/api/orders').flush([{ id: 1 }]);
  });
});""",
            "typescript",
            key_points=["TestBed.configureTestingModule for standalone", "ComponentFixture + detectChanges()", "Mock services with jasmine.createSpyObj"],
        ),
        InterviewItem(
            "ts-type-narrowing",
            "What is type narrowing in TypeScript?",
            "TypeScript refines types within control flow using typeof, instanceof, in, and discriminated unions.",
            """type Result<T> = { ok: true; value: T } | { ok: false; error: string };

function handle<T>(result: Result<T>): T {
  if (!result.ok) throw new Error(result.error); // narrowed to error branch
  return result.value; // narrowed to success branch
}

function process(input: string | number) {
  if (typeof input === 'string') return input.toUpperCase();
  return input.toFixed(2);
}""",
            "typescript",
            key_points=["Discriminated unions with literal types", "in operator for object shape checks", "Assertions (as) only when you are certain"],
        ),
        InterviewItem(
            "observables-vs-promises",
            "Observables vs Promises — when to use each in Angular?",
            "Promises resolve once; Observables emit multiple values, are cancellable, and compose with operators.",
            """// Promise — single value, not cancellable
const orders = await firstValueFrom(this.http.get<Order[]>('/api/orders'));

// Observable — streams, cancellable, composable
this.searchControl.valueChanges.pipe(
  debounceTime(300),
  distinctUntilChanged(),
  switchMap(term => this.api.search(term)),
  takeUntil(this.destroy$)
).subscribe(results => this.results = results);""",
            "typescript",
            key_points=["HttpClient returns Observable by default", "firstValueFrom/lastValueFrom convert to Promise", "Use Observables for events, streams, cancellation"],
        ),
        InterviewItem(
            "angular-material-ui",
            "How do you use Angular Material in enterprise apps?",
            "Angular Material provides Material Design components — tables, dialogs, form controls, theming.",
            """@Component({
  standalone: true,
  imports: [MatTableModule, MatPaginatorModule, MatSortModule],
  template: `
    <table mat-table [dataSource]="dataSource" matSort>
      <ng-container matColumnDef="id"><th mat-header-cell *matHeaderCellDef>ID</th>
        <td mat-cell *matCellDef="let row">{{ row.id }}</td></ng-container>
      <tr mat-header-row *matHeaderRowDef="columns"></tr>
      <tr mat-row *matRowDef="let row; columns: columns"></tr>
    </table>
    <mat-paginator [pageSize]="10" />`
})
export class OrdersTableComponent {}""",
            "typescript",
            key_points=["Import only needed modules (tree-shaking)", "Theming via @angular/material prebuilt or custom", "MatDialog for modal workflows"],
        ),
        InterviewItem(
            "form-validation",
            "How do you implement form validation in Angular reactive forms?",
            "Validators on FormControls — built-in and custom. Cross-field validation on FormGroup. Show errors in template.",
            """this.form = this.fb.group({
  email: ['', [Validators.required, Validators.email]],
  password: ['', [Validators.required, Validators.minLength(8)]],
  confirm: ['']
}, { validators: this.passwordMatch });

passwordMatch(group: AbstractControl): ValidationErrors | null {
  const p = group.get('password')?.value;
  const c = group.get('confirm')?.value;
  return p === c ? null : { mismatch: true };
}""",
            "typescript",
            key_points=["Validators.required, min, max, pattern", "form.invalid blocks submit", "Typed forms (FormGroup<{...}>) in Angular 14+"],
        ),
        InterviewItem(
            "lazy-loading-routes",
            "How does lazy loading work with standalone routes in modern Angular?",
            "loadComponent/loadChildren defer feature code until navigation — smaller initial bundle.",
            """export const routes: Routes = [
  { path: '', component: HomeComponent },
  {
    path: 'orders',
    loadChildren: () => import('./orders/orders.routes').then(m => m.ORDER_ROUTES),
    canActivate: [authGuard]
  },
  { path: 'admin', loadComponent: () => import('./admin/admin.component').then(m => m.AdminComponent) }
];""",
            "typescript",
            key_points=["loadChildren for route arrays", "loadComponent for single standalone component", "PreloadingStrategy for background prefetch"],
        ),
    ],
    ("frontend", "advanced"): [
        InterviewItem(
            "ngrx-state",
            "When would you use NgRx for state management in Angular?",
            "NgRx provides predictable global state with actions, reducers, effects, and selectors — ideal for complex shared state.",
            """// actions
export const loadOrders = createAction('[Orders] Load');
export const loadOrdersSuccess = createAction('[Orders] Load Success', props<{ orders: Order[] }>());

// reducer
export const ordersReducer = createReducer(initialState,
  on(loadOrdersSuccess, (state, { orders }) => ({ ...state, orders }))
);

// component
orders$ = this.store.select(selectAllOrders);
ngOnInit() { this.store.dispatch(loadOrders()); }""",
            "typescript",
            key_points=["Single source of truth for app state", "Effects for side effects (HTTP)", "ComponentStore for local/feature state alternative"],
        ),
        InterviewItem(
            "angular-ssr-hydration",
            "Explain Angular SSR and hydration.",
            "SSR renders HTML on the server for SEO and fast FCP. Hydration attaches client behavior to server-rendered DOM.",
            """// angular.json — add @angular/ssr
// server.ts serves rendered HTML
export const serverConfig: ApplicationConfig = {
  providers: [provideServerRendering()]
};

// Client bootstraps and hydrates without re-rendering entire tree
bootstrapApplication(AppComponent, appConfig);""",
            "typescript",
            key_points=["ng add @angular/ssr scaffolds setup", "Hydration avoids flicker on load", "Use TransferState to avoid duplicate HTTP on client"],
        ),
        InterviewItem(
            "onpush-strategy",
            "Explain ChangeDetectionStrategy.OnPush and optimization techniques.",
            "OnPush checks component only when @Input reference changes, events fire, or async pipe emits — major perf win.",
            """@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `@for (o of orders(); track o.id) { <span>{{ o.total }}</span> }`
})
export class OrderListComponent {
  orders = input.required<Order[]>();
  // Immutable update: this.orders.set([...this.orders(), newOrder]);
}""",
            "typescript",
            key_points=["Immutable data updates trigger OnPush", "MarkForCheck() when mutating external state", "Signals + OnPush is the modern default pattern"],
        ),
    ],
    ("database", "foundation"): [
        InterviewItem(
            "acid-properties",
            "What are ACID properties in database transactions?",
            "ACID guarantees reliable transactions: Atomicity, Consistency, Isolation, Durability.",
            """BEGIN TRANSACTION;
  UPDATE Accounts SET Balance = Balance - 100 WHERE Id = 1;
  UPDATE Accounts SET Balance = Balance + 100 WHERE Id = 2;
COMMIT; -- both succeed or both roll back (Atomicity)""",
            "sql",
            key_points=["Atomicity — all or nothing", "Isolation — concurrent transactions don't interfere", "Durability — committed data survives crashes"],
        ),
        InterviewItem(
            "normalization",
            "Explain database normalization (1NF, 2NF, 3NF).",
            "Normalization reduces redundancy by organizing columns and dependencies into separate tables.",
            """-- Before (violates 1NF — repeating groups)
Orders(Id, Customer, Product1, Product2)

-- After 3NF — separate entities, no transitive dependencies
Customers(Id, Name)
Orders(Id, CustomerId, OrderDate)
OrderLines(OrderId, ProductId, Qty)
Products(Id, Name, Price)""",
            "sql",
            key_points=["1NF — atomic values, no repeating groups", "2NF — no partial key dependencies", "3NF — no transitive dependencies"],
        ),
        InterviewItem(
            "sql-views",
            "What are SQL views and when do you use them?",
            "Views are virtual tables from a stored query — simplify reporting, enforce security, abstract complexity.",
            """CREATE VIEW vw_ActiveOrders AS
SELECT o.Id, c.Name AS Customer, o.Total, o.OrderDate
FROM Orders o
INNER JOIN Customers c ON c.Id = o.CustomerId
WHERE o.Status = 'Active';

SELECT * FROM vw_ActiveOrders WHERE Total > 500;""",
            "sql",
            key_points=["Indexed views (SQL Server) can improve performance", "Hide sensitive columns from users", "EF Core can map entities to views"],
        ),
        InterviewItem(
            "sql-injection-prevention",
            "How do you prevent SQL injection in .NET applications?",
            "Never concatenate user input into SQL. Use parameterized queries, EF Core LINQ, or Dapper with parameters.",
            """// Vulnerable — NEVER do this
var sql = $"SELECT * FROM Users WHERE Name = '{userInput}'";

// Safe — parameterized
var user = await _db.Users
    .FirstOrDefaultAsync(u => u.Name == userInput);

// Raw SQL with parameters
await _db.Database.ExecuteSqlRawAsync(
    "UPDATE Orders SET Status = {0} WHERE Id = {1}", status, id);""",
            "csharp",
            key_points=["EF Core LINQ parameterizes automatically", "Stored procedures still need parameters", "Validate and sanitize input at API layer too"],
        ),
        InterviewItem(
            "sqlserver-vs-postgresql",
            "Compare SQL Server and PostgreSQL for .NET applications.",
            "SQL Server integrates tightly with Azure and Windows ecosystem. PostgreSQL is open-source, cross-platform, strong JSON support.",
            """// EF Core — same code, different provider
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(connectionString));   // Azure SQL / SQL Server
// or
    options.UseNpgsql(connectionString));    // PostgreSQL

// PostgreSQL JSON query example
var results = await _db.Orders
    .Where(o => EF.Functions.JsonContains(o.Metadata, @"{""priority"": ""high""}"))
    .ToListAsync();""",
            "csharp",
            key_points=["Both fully supported by EF Core", "PostgreSQL: lower cost, JSON/arrays native", "SQL Server: Azure integration, SSIS, Reporting Services"],
        ),
    ],
    ("database", "intermediate"): [
        InterviewItem(
            "isolation-levels",
            "Explain SQL transaction isolation levels.",
            "Isolation levels trade consistency for concurrency — control dirty reads, non-repeatable reads, phantom reads.",
            """await using var tx = await _db.Database.BeginTransactionAsync(
    System.Data.IsolationLevel.ReadCommitted);
try {
    // ReadCommitted — default, prevents dirty reads
    await _db.SaveChangesAsync();
    await tx.CommitAsync();
} catch { await tx.RollbackAsync(); throw; }""",
            "csharp",
            key_points=["Read Uncommitted → Serializable (strictest)", "Read Committed is SQL Server default", "Serializable prevents phantoms but hurts concurrency"],
        ),
        InterviewItem(
            "stored-procedures",
            "When do you use stored procedures vs EF Core LINQ?",
            "Stored procedures encapsulate complex SQL, enforce security, and can optimize execution plans — common in legacy/DBA-heavy teams.",
            """// Call from EF Core
var orders = await _db.Orders
    .FromSqlRaw("EXEC usp_GetOrdersByCustomer @CustomerId = {0}", customerId)
    .AsNoTracking()
    .ToListAsync();

-- SQL Server stored procedure
CREATE PROCEDURE usp_GetOrdersByCustomer @CustomerId INT AS
SELECT * FROM Orders WHERE CustomerId = @CustomerId;""",
            "sql",
            key_points=["DBA can tune without redeploying app", "Parameterize to prevent injection", "EF migrations don't manage sproc bodies automatically"],
        ),
        InterviewItem(
            "index-strategies",
            "Deep dive: how do you design effective database indexes?",
            "Index columns in WHERE, JOIN, ORDER BY. Use covering indexes, filtered indexes, and avoid over-indexing write-heavy tables.",
            """CREATE NONCLUSTERED INDEX IX_Orders_CustomerId_Status
ON Orders (CustomerId, Status)
INCLUDE (OrderDate, Total)
WHERE Status != 'Cancelled';

-- Check for scans vs seeks in execution plan
SET STATISTICS IO ON;""",
            "sql",
            key_points=["Clustered index = table sort order (one per table)", "INCLUDE columns for covering index", "Monitor fragmentation and rebuild/reorganize"],
        ),
        InterviewItem(
            "connection-pooling",
            "What is connection pooling and how does it affect .NET apps?",
            "Pooling reuses open DB connections — avoids expensive connect/disconnect per request. Enabled by default in ADO.NET.",
            """// Connection string — pooling on by default
"Server=...;Database=OrderDb;Max Pool Size=100;Min Pool Size=5;Connection Timeout=30"

// Anti-pattern — opening new connection per row
foreach (var id in ids) {
  await using var conn = new SqlConnection(cs); // pool helps but still wasteful
}

// Better — single connection or EF DbContext per request (scoped)""",
            "csharp",
            key_points=["DbContext is scoped per HTTP request", "Don't hold connections open unnecessarily", "Pool exhaustion causes timeouts — watch Max Pool Size"],
        ),
        InterviewItem(
            "pagination-strategies",
            "Compare offset vs keyset pagination for large datasets.",
            "OFFSET/FETCH is simple but slow on deep pages. Keyset (seek) pagination uses last-seen key — constant time.",
            """// Offset — page 1000 of 20 = scans 20000 rows
var page = await _db.Orders.OrderBy(o => o.Id)
    .Skip(19980).Take(20).ToListAsync();

// Keyset — efficient for infinite scroll
var page = await _db.Orders
    .Where(o => o.Id > lastSeenId)
    .OrderBy(o => o.Id).Take(20).ToListAsync();""",
            "csharp",
            key_points=["Offset pagination degrades on large offsets", "Keyset requires stable sort key", "Return next cursor token to client"],
        ),
        InterviewItem(
            "soft-delete-pattern",
            "How do you implement soft delete in EF Core?",
            "Mark records as deleted with IsDeleted flag instead of physical DELETE — preserves audit trail and referential integrity.",
            """public class Order {
    public int Id { get; set; }
    public bool IsDeleted { get; set; }
    public DateTime? DeletedAt { get; set; }
}

// Override SaveChanges
public override int SaveChanges() {
    foreach (var entry in ChangeTracker.Entries<ISoftDeletable>()
        .Where(e => e.State == EntityState.Deleted)) {
        entry.State = EntityState.Modified;
        entry.Entity.IsDeleted = true;
        entry.Entity.DeletedAt = DateTime.UtcNow;
    }
    return base.SaveChanges();
}""",
            "csharp",
            key_points=["Combine with global query filter", "Unique indexes may need filtered unique constraint", "Hard delete for GDPR erasure requests"],
        ),
        InterviewItem(
            "global-query-filters",
            "What are EF Core global query filters?",
            "Filters automatically apply WHERE clauses to all queries — ideal for multi-tenancy and soft delete.",
            """protected override void OnModelCreating(ModelBuilder model) {
    model.Entity<Order>().HasQueryFilter(o => !o.IsDeleted);
    model.Entity<Order>().HasQueryFilter(o => o.TenantId == _tenantProvider.TenantId);
}

// Bypass filter when needed
var all = await _db.Orders.IgnoreQueryFilters().ToListAsync();""",
            "csharp",
            key_points=["Applied to all queries including Include", "IgnoreQueryFilters() for admin/reporting", "Multiple filters are AND-combined"],
        ),
        InterviewItem(
            "owned-entity-types",
            "What are owned entity types in EF Core?",
            "Owned types map value objects embedded in parent table — Address, Money, without separate identity.",
            """public class Order {
    public int Id { get; set; }
    public Address ShippingAddress { get; set; } = null!;
}

public class Address { // no Id — owned by Order
    public string Street { get; set; } = "";
    public string City { get; set; } = "";
}

model.Entity<Order>().OwnsOne(o => o.ShippingAddress);""",
            "csharp",
            key_points=["Stored in same table (usually) with column prefix", "No separate DbSet for owned type", "Good for DDD value objects"],
        ),
        InterviewItem(
            "value-converters",
            "How do EF Core value converters work?",
            "Converters map between CLR types and database column types — enums as strings, ValueObjects, encrypted fields.",
            """model.Entity<Order>()
    .Property(o => o.Status)
    .HasConversion<string>(); // stores enum as 'Pending', 'Shipped'

model.Entity<User>()
    .Property(u => u.Email)
    .HasConversion(
        v => Encrypt(v),
        v => Decrypt(v));""",
            "csharp",
            key_points=["Built-in enum ↔ string/ int conversions", "Custom converters for complex types", "Nullable handling must be explicit"],
        ),
        InterviewItem(
            "change-tracking",
            "Explain EF Core change tracking.",
            "DbContext tracks entity state (Added, Modified, Deleted, Unchanged). SaveChanges generates INSERT/UPDATE/DELETE SQL.",
            """var order = await _db.Orders.FindAsync(1); // tracked
order.Status = OrderStatus.Shipped; // marked Modified

var entry = _db.Entry(order);
Console.WriteLine(entry.State); // Modified
Console.WriteLine(entry.Property(o => o.Status).IsModified); // true

await _db.SaveChangesAsync(); // UPDATE Orders SET Status = ...""",
            "csharp",
            key_points=["AsNoTracking() skips tracking for read-only", "Attach/Update for disconnected scenarios", "DetectChanges runs before SaveChanges"],
        ),
        InterviewItem(
            "dbcontext-pooling",
            "What is DbContext pooling in ASP.NET Core?",
            "Pooling reuses DbContext instances — resets state between requests. Faster than creating new context each time.",
            """builder.Services.AddDbContextPool<AppDbContext>(options =>
    options.UseSqlServer(connectionString),
    poolSize: 128);

// Do NOT store state on DbContext fields — instance is reused!
// Bad: private List<Order> _cache = [];
// Good: use IMemoryCache or scoped service for per-request state""",
            "csharp",
            key_points=["AddDbContextPool vs AddDbContext", "OnConfiguring still runs per lease", "Don't inject scoped services into pooled context constructor"],
        ),
        InterviewItem(
            "raw-sql-ef",
            "How do you execute raw SQL safely in EF Core?",
            "FromSqlRaw for queries, ExecuteSqlRaw for commands. Always use parameters — never string interpolation.",
            """var minTotal = 100;
var orders = await _db.Orders
    .FromSqlRaw("SELECT * FROM Orders WHERE Total > {0}", minTotal)
    .AsNoTracking()
    .ToListAsync();

var rows = await _db.Database.ExecuteSqlRawAsync(
    "UPDATE Orders SET Status = {0} WHERE Id = {1}", "Shipped", orderId);""",
            "csharp",
            key_points=["FromSqlRaw must return entity shape for DbSet", "SqlQuery<T> for arbitrary result types (EF 8+)", "Parameters prevent SQL injection"],
        ),
        InterviewItem(
            "window-functions",
            "Explain SQL window functions (ROW_NUMBER, RANK, DENSE_RANK).",
            "Window functions compute across related rows without collapsing groups — ranking, running totals, moving averages.",
            """SELECT Id, CustomerId, Total,
  ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate DESC) AS RowNum,
  RANK() OVER (ORDER BY Total DESC) AS RevenueRank,
  SUM(Total) OVER (PARTITION BY CustomerId) AS CustomerTotal
FROM Orders;

-- Top 3 orders per customer
WITH Ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY Total DESC) rn
  FROM Orders
) SELECT * FROM Ranked WHERE rn <= 3;""",
            "sql",
            key_points=["PARTITION BY defines window groups", "RANK allows ties; ROW_NUMBER is unique", "Supported in SQL Server and PostgreSQL"],
        ),
    ],
    ("database", "advanced"): [
        InterviewItem(
            "bulk-insert-update",
            "How do you perform bulk insert/update in EF Core?",
            "SaveChanges sends one statement per entity — slow for large batches. Use ExecuteUpdate, ExecuteDelete, or bulk libraries.",
            """// EF Core 7+ — bulk update without loading entities
await _db.Orders
    .Where(o => o.Status == OrderStatus.Pending && o.CreatedAt < cutoff)
    .ExecuteUpdateAsync(s => s.SetProperty(o => o.Status, OrderStatus.Cancelled));

// Bulk insert — EFCore.BulkExtensions or COPY (PostgreSQL)
await _db.BulkInsertAsync(orders); // third-party""",
            "csharp",
            key_points=["ExecuteUpdate/ExecuteDelete bypass change tracker", "BulkExtensions for large inserts", "Consider SqlBulkCopy for millions of rows"],
        ),
        InterviewItem(
            "compiled-queries",
            "What are compiled queries in EF Core?",
            "Compiled queries cache the query expression translation — faster for hot paths executed repeatedly.",
            """private static readonly Func<AppDbContext, int, Task<Order?>> GetOrderById =
    EF.CompileAsyncQuery((AppDbContext db, int id) =>
        db.Orders.AsNoTracking().FirstOrDefault(o => o.Id == id));

public async Task<Order?> GetOrderAsync(int id) =>
    await GetOrderById(_db, id);""",
            "csharp",
            key_points=["Compile once, reuse across requests", "Marginal gain for simple queries", "Best for high-frequency identical queries"],
        ),
        InterviewItem(
            "migration-strategy",
            "Describe a production database migration strategy with EF Core.",
            "Generate idempotent scripts in CI, review in PR, apply via pipeline — never auto-migrate production on app startup.",
            """# CI pipeline
dotnet ef migrations script --idempotent -o deploy/migration.sql
# DBA review → apply in maintenance window

# Program.cs — dev only
if (app.Environment.IsDevelopment())
    await db.Database.MigrateAsync(); // NEVER in production""",
            "csharp",
            key_points=["Idempotent scripts safe to re-run", "Backward-compatible migrations for zero-downtime", "Separate data migrations from schema migrations"],
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "standalone-components": {
        "explanation": (
            "**Standalone components** (Angular 14+, default in Angular 19+) declare dependencies directly in "
            "the `@Component({ imports: [...] })` array instead of belonging to an NgModule. This eliminates "
            "boilerplate `NgModule` files, simplifies bootstrapping with `bootstrapApplication()`, and "
            "makes lazy loading cleaner via `loadComponent`/`loadChildren`. Standalone components are "
            "**tree-shakeable** — unused imports can be dropped at build time. They work seamlessly with "
            "the modern control flow syntax, functional guards, and the `inject()` API. For enterprise "
            "migrations, you can incrementally convert NgModule-based features to standalone without "
            "a big-bang rewrite."
        ),
        "code": """// Standalone component — no NgModule wrapper needed
@Component({
  selector: 'app-order-card',
  standalone: true,
  imports: [CommonModule, MatButtonModule, CurrencyPipe],
  template: `
    <h3>{{ order().id }}</h3>
    <p>{{ order().total | currency }}</p>
    <button mat-button (click)="onEdit()">Edit</button>
  `
})
export class OrderCardComponent {
  order = input.required<Order>();          // signal-based input (modern)
  edit = output<number>();                // signal-based output

  onEdit() { this.edit.emit(this.order().id); }
}

// Bootstrapping without AppModule
bootstrapApplication(AppComponent, {
  providers: [provideRouter(routes), provideHttpClient()]
});""",
        "language": "typescript",
        "key_points": [
            "imports array replaces NgModule imports/exports",
            "Default scaffolding in Angular 19+",
            "Works with lazy loadComponent and loadChildren",
            "Easier unit testing — fewer TestBed imports",
        ],
    },
    "control-flow": {
        "explanation": (
            "Angular 17 introduced **built-in control flow** — `@if`, `@for`, `@switch` — replacing structural "
            "directives like `*ngIf`, `*ngFor`, and `*ngSwitch`. The new syntax offers **better type narrowing** "
            "(TypeScript knows the type inside `@if` blocks), improved **runtime performance**, and clearer "
            "templates. `@for` requires an explicit **`track` expression** for efficient DOM reconciliation — "
            "typically the entity's unique id. The `@empty` block handles empty collections without a separate "
            "`*ngIf` check. Migration schematics can auto-convert legacy templates. This is the standard pattern "
            "in 2025/2026 Angular codebases."
        ),
        "code": """@Component({
  selector: 'app-order-list',
  standalone: true,
  template: `
    @if (loading()) {
      <app-spinner />
    } @else if (error(); as err) {
      <p class="error">{{ err }}</p>
    } @else {
      @for (order of orders(); track order.id) {
        <app-order-row [order]="order" />
      } @empty {
        <p>No orders found.</p>
      }
    }

    @switch (status()) {
      @case ('pending') { <span class="badge">Pending</span> }
      @case ('shipped') { <span class="badge shipped">Shipped</span> }
      @default { <span class="badge unknown">Unknown</span> }
    }
  `
})
export class OrderListComponent {
  orders = signal<Order[]>([]);
  loading = signal(true);
  error = signal<string | null>(null);
  status = signal('pending');
}""",
        "language": "typescript",
        "key_points": [
            "@for requires track — use unique id, not index",
            "@empty replaces *ngIf + length check",
            "Better type narrowing than *ngIf",
            "Migration: ng generate @angular/core:control-flow",
        ],
    },
    "lifecycle-hooks": {
        "explanation": (
            "Angular components follow a **lifecycle** managed by the framework. Key hooks: **`ngOnChanges`** "
            "(when @Input values change), **`ngOnInit`** (one-time initialization after first input binding), "
            "**`ngDoCheck`/`ngAfterContentChecked`/`ngAfterViewChecked`** (custom change detection — use sparingly), "
            "**`ngAfterViewInit`** (ViewChild/ViewChildren available), and **`ngOnDestroy`** (cleanup). "
            "In modern apps, prefer **`takeUntilDestroyed()`** or the **`async` pipe** over manual subscription "
            "management. With signals, many patterns shift from `ngOnChanges` to `computed()` and `effect()`. "
            "Interviewers want to hear that you **never subscribe without unsubscribing** in long-lived components."
        ),
        "code": """@Component({ /* ... */ })
export class OrdersComponent implements OnInit, OnDestroy {
  private destroy$ = new Subject<void>();
  orders: Order[] = [];

  constructor(private orderService: OrderService) {}

  ngOnInit(): void {
    // One-time setup — fetch data, subscribe to streams
    this.orderService.getOrders()
      .pipe(takeUntil(this.destroy$))
      .subscribe(orders => this.orders = orders);
  }

  ngOnDestroy(): void {
    // Cleanup — prevent memory leaks
    this.destroy$.next();
    this.destroy$.complete();
  }
}

// Modern alternative (Angular 16+)
private orderService = inject(OrderService);
orders = toSignal(this.orderService.getOrders(), { initialValue: [] });""",
        "language": "typescript",
        "key_points": [
            "ngOnInit for initialization, not constructor",
            "ngAfterViewInit when you need ViewChild DOM access",
            "Always clean up subscriptions and timers in ngOnDestroy",
            "takeUntilDestroyed() simplifies cleanup in Angular 16+",
        ],
    },
    "input-output": {
        "explanation": (
            "**`@Input()`** decorates properties that receive data from a parent component — data flows **down** "
            "the component tree. **`@Output()`** decorates `EventEmitter` fields that emit events **up** to the "
            "parent. Angular 17.1+ introduced **`input()`** and **`output()`** signal-based alternatives with "
            "better type inference and required-input enforcement. With **`ChangeDetectionStrategy.OnPush`**, "
            "mutating an `@Input` object's properties in place won't trigger re-render — you must emit new "
            "references. This parent-child contract is fundamental to Angular's component architecture and "
            "separates presentation components (dumb) from container components (smart)."
        ),
        "code": """// Child component — receives data, emits events
@Component({
  selector: 'app-order-row',
  standalone: true,
  template: `
    <td>{{ order().customerName }}</td>
    <td>{{ order().total | currency }}</td>
    <td><button (click)="onDelete()">Delete</button></td>
  `
})
export class OrderRowComponent {
  order = input.required<Order>();           // required parent data
  delete = output<number>();                 // emit order id to parent

  onDelete() { this.delete.emit(this.order().id); }
}

// Parent template
// <app-order-row
//   [order]="selectedOrder"
//   (delete)="removeOrder($event)" />""",
        "language": "typescript",
        "key_points": [
            "Data down (@Input), events up (@Output)",
            "input.required<T>() enforces mandatory inputs at compile time",
            "Don't mutate @Input objects with OnPush strategy",
            "EventEmitter is the standard output mechanism",
        ],
    },
    "pipes": {
        "explanation": (
            "**Pipes** transform displayed values in templates without changing the source data. Angular provides "
            "built-in pipes: **`DatePipe`**, **`CurrencyPipe`**, **`DecimalPipe`**, **`JsonPipe`**, **`AsyncPipe`**, "
            "and more. **Pure pipes** (default) recalculate only when the input **reference** changes — they are "
            "cached for performance. **Impure pipes** run on every change detection cycle (use sparingly). "
            "Custom pipes implement `PipeTransform`. The **`async` pipe** subscribes to Observables/Promises and "
            "automatically unsubscribes — it is essential for avoiding memory leaks. Standalone pipes declare "
            "`standalone: true` and are imported directly into components."
        ),
        "code": """// Custom standalone pipe
@Pipe({ name: 'truncate', standalone: true })
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 50, suffix = '...'): string {
    if (!value || value.length <= limit) return value;
    return value.substring(0, limit) + suffix;
  }
}

// Usage in template
// {{ longDescription | truncate:80 }}
// {{ order.date | date:'mediumDate' }}
// {{ order.total | currency:'USD':'symbol':'1.2-2' }}
// {{ orders$ | async }}  ← subscribes and auto-unsubscribes

@Pipe({ name: 'filterOrders', standalone: true, pure: false }) // impure — runs every CD
export class FilterOrdersPipe implements PipeTransform {
  transform(orders: Order[], status: string): Order[] {
    return orders.filter(o => o.status === status);
  }
}""",
        "language": "typescript",
        "key_points": [
            "Pure pipes cached until input reference changes",
            "AsyncPipe eliminates manual subscribe/unsubscribe",
            "Chaining: {{ value | pipe1 | pipe2 }}",
            "Impure pipes impact performance — use computed() instead when possible",
        ],
    },
    "ts-generics": {
        "explanation": (
            "**Generics** let you write functions, classes, and interfaces that work with multiple types while "
            "preserving type safety — no casting or `any`. In Angular, generics appear everywhere: **`HttpClient.get<T>()`**, "
            "**`Observable<T>`**, **`FormGroup<T>`**, **`signal<T>()`**, and reusable **`ApiResponse<T>`** wrappers. "
            "**Constraints** (`T extends HasId`) limit what types can be passed. **Generic components** like "
            "`DataTableComponent<T>` enable reusable UI for any entity type. Interviewers expect you to explain "
            "how generics flow type information from service → component → template without runtime overhead "
            "(TypeScript erases generics at compile time)."
        ),
        "code": """// Generic API wrapper
interface ApiResponse<T> {
  data: T;
  meta: { total: number; page: number };
}

// Generic service method
@Injectable({ providedIn: 'root' })
export class ApiService {
  constructor(private http: HttpClient) {}

  getList<T>(url: string): Observable<T[]> {
    return this.http.get<ApiResponse<T[]>>(url).pipe(
      map(response => response.data)  // T is preserved end-to-end
    );
  }
}

// Generic constraint
interface HasId { id: number; }

function findById<T extends HasId>(items: T[], id: number): T | undefined {
  return items.find(item => item.id === id);
}

// Usage — type inferred
this.api.getList<Order>('/api/orders').subscribe(orders => {
  // orders is Order[] — not any[]
});""",
        "language": "typescript",
        "key_points": [
            "Generics preserve type safety without runtime cost",
            "HttpClient.get<T>() is the most common Angular generic",
            "Constraints: T extends BaseEntity limits type parameter",
            "Avoid any — use unknown or generics instead",
        ],
    },
    "angular-signals": {
        "explanation": (
            "**Signals** (Angular 16+) are synchronous reactive primitives that hold a value and notify consumers "
            "when it changes. **`signal()`** creates writable state, **`computed()`** derives read-only values "
            "from other signals, and **`effect()`** runs side effects when dependencies change. Unlike Observables, "
            "signals are **always synchronous** and integrate with Angular's change detection for **fine-grained** "
            "updates — only components reading changed signals re-render. **`toSignal()`** converts Observables to "
            "signals; **`toObservable()`** goes the other way. Signals are the recommended state primitive for "
            "new Angular code in 2025/2026, often replacing BehaviorSubject for component-local state."
        ),
        "code": """@Component({
  selector: 'app-shopping-cart',
  template: `
    <p>Items: {{ itemCount() }}</p>
    <p>Total: {{ total() | currency }}</p>
    <button (click)="addItem()">Add Item</button>
  `
})
export class ShoppingCartComponent {
  items = signal<CartItem[]>([]);

  // Derived state — recalculates when items() changes
  itemCount = computed(() => this.items().length);
  total = computed(() =>
    this.items().reduce((sum, i) => sum + i.price * i.qty, 0)
  );

  constructor() {
    // Side effect when total exceeds budget
    effect(() => {
      if (this.total() > 500) console.warn('Budget exceeded!');
    });
  }

  addItem() {
    this.items.update(list => [...list, { id: Date.now(), price: 29.99, qty: 1 }]);
  }
}""",
        "language": "typescript",
        "key_points": [
            "signal(), computed(), effect() — core trio",
            "Synchronous reads: this.items() not this.items",
            "Immutable updates via .set() or .update()",
            "toSignal() bridges HttpClient Observables to template-friendly signals",
        ],
    },
    "defer-blocks": {
        "explanation": (
            "**`@defer` blocks** (Angular 17+) enable **lazy loading at the template level** — deferring the "
            "download and rendering of heavy components until a trigger condition is met. Triggers include "
            "**`on idle`** (browser idle), **`on viewport`** (element enters viewport), **`on interaction`** "
            "(click/hover), **`on timer`**, and **`when`** (custom boolean). This improves **Largest Contentful "
            "Paint (LCP)** and initial bundle size. Blocks like **`@placeholder`**, **`@loading`**, and **`@error`** "
            "customize the UX during loading. `@defer` is ideal for charts, rich editors, and below-the-fold content "
            "in enterprise dashboards."
        ),
        "code": """@Component({
  selector: 'app-dashboard',
  template: `
    <h1>Dashboard</h1>

    @defer (on viewport) {
      <!-- Heavy chart loaded only when scrolled into view -->
      <app-revenue-chart [data]="chartData()" />
    } @placeholder {
      <div class="chart-skeleton" style="height:300px"></div>
    } @loading (minimum 200ms) {
      <app-spinner message="Loading chart..." />
    } @error {
      <p>Failed to load chart. <button (click)="retry()">Retry</button></p>
    }

    @defer (on interaction) {
      <app-admin-panel />
    } @placeholder {
      <button>Show Admin Panel</button>
    }
  `
})
export class DashboardComponent {
  chartData = signal<ChartPoint[]>([]);
  retry() { /* reload chart data */ }
}""",
        "language": "typescript",
        "key_points": [
            "on viewport — best for below-fold content",
            "on idle — load after critical content renders",
            "Creates separate JS chunks automatically",
            "minimum on @loading prevents flicker on fast networks",
        ],
    },
    "inject-function": {
        "explanation": (
            "The **`inject()`** function (Angular 14+) retrieves dependencies from the current **injection context** "
            "without constructor injection. It works in **`CanActivateFn` guards**, **`HttpInterceptorFn`**, "
            "**`ResolveFn` resolvers**, **`APP_INITIALIZER` factories**, and class **field initializers**. "
            "This enables **functional** (non-class) Angular APIs that are tree-shakeable and easier to test. "
            "`inject()` must be called synchronously during construction — not inside async callbacks or setTimeout. "
            "It is the preferred pattern for new guards and interceptors in 2025/2026 Angular applications."
        ),
        "code": """// Functional route guard — no class needed
export const authGuard: CanActivateFn = (route, state) => {
  const auth = inject(AuthService);
  const router = inject(Router);

  if (auth.isLoggedIn()) return true;
  return router.createUrlTree(['/login'], {
    queryParams: { returnUrl: state.url }
  });
};

// Functional HTTP interceptor
export const loggingInterceptor: HttpInterceptorFn = (req, next) => {
  const logger = inject(LoggerService);
  logger.log(`HTTP ${req.method} ${req.url}`);
  return next(req);
};

// Class field injection (alternative to constructor)
@Component({ /* ... */ })
export class ProfileComponent {
  private auth = inject(AuthService);
  private http = inject(HttpClient);
  user = toSignal(this.auth.currentUser$);
}""",
        "language": "typescript",
        "key_points": [
            "Must run in injection context (constructor, factory, field init)",
            "Preferred for CanActivateFn and HttpInterceptorFn",
            "Cannot call inside setTimeout or async callbacks",
            "Replaces constructor DI for cleaner class bodies",
        ],
    },
    "http-interceptors": {
        "explanation": (
            "**HTTP interceptors** form a middleware chain around every `HttpClient` request. They can **attach "
            "auth tokens**, **add correlation IDs**, **log requests**, **retry failures**, and **handle 401/403 "
            "globally**. Angular 15+ uses **functional interceptors** (`HttpInterceptorFn`) registered via "
            "`provideHttpClient(withInterceptors([...]))`. Interceptors receive the request and a **`next` handler** "
            "— they must call `next(modifiedReq)` to continue the chain. Requests are **immutable** — use "
            "`req.clone({ setHeaders: {...} })` to modify. Order of registration determines execution order "
            "for outgoing requests (first registered runs first)."
        ),
        "code": """// Auth interceptor — attach JWT to every API call
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const auth = inject(AuthService);
  const token = auth.getToken();

  if (token && req.url.startsWith('/api')) {
    req = req.clone({
      setHeaders: { Authorization: `Bearer ${token}` }
    });
  }
  return next(req);
};

// Error interceptor — global 401 handling
export const errorInterceptor: HttpInterceptorFn = (req, next) => {
  const router = inject(Router);
  return next(req).pipe(
    catchError(err => {
      if (err.status === 401) router.navigate(['/login']);
      return throwError(() => err);
    })
  );
};

// Register in app.config.ts
providers: [
  provideHttpClient(withInterceptors([authInterceptor, errorInterceptor]))
]""",
        "language": "typescript",
        "key_points": [
            "Functional interceptors with HttpInterceptorFn (Angular 15+)",
            "Clone requests — HttpRequest is immutable",
            "Chain order: first registered runs first on outgoing",
            "Use for auth headers, logging, retry, error handling",
        ],
    },
    "route-guards-resolvers": {
        "explanation": (
            "**Route guards** control whether navigation to/from a route is allowed. **`canActivate`** checks "
            "before entering, **`canDeactivate`** before leaving (unsaved changes), **`canMatch`** for route "
            "matching logic. **`CanActivateFn`** is the modern functional form returning `boolean | UrlTree`. "
            "**Resolvers** prefetch data before the route activates — data is available in `route.snapshot.data` "
            "or via `ActivatedRoute.data` Observable. This prevents components from rendering empty while "
            "waiting for HTTP. Guards and resolvers both use `inject()` for service access. Common enterprise "
            "patterns: auth guard, role guard, feature-flag guard, and order-detail resolver."
        ),
        "code": """// Role-based guard
export const adminGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  return auth.hasRole('Admin') ? true : inject(Router).createUrlTree(['/forbidden']);
};

// Resolver — prefetch order before component loads
export const orderResolver: ResolveFn<Order> = (route) => {
  const id = Number(route.paramMap.get('id'));
  return inject(OrderService).getById(id);
};

const routes: Routes = [
  {
    path: 'orders/:id',
    component: OrderDetailComponent,
    canActivate: [authGuard, adminGuard],
    resolve: { order: orderResolver }
  }
];

// Component reads resolved data
@Component({ /* ... */ })
export class OrderDetailComponent {
  private route = inject(ActivatedRoute);
  order = this.route.snapshot.data['order'] as Order;
}""",
        "language": "typescript",
        "key_points": [
            "CanActivateFn returns boolean or UrlTree (redirect)",
            "Resolver prevents empty-state flicker on detail pages",
            "canDeactivate for unsaved form warnings",
            "Functional guards preferred over class-based CanActivate",
        ],
    },
    "directives": {
        "explanation": (
            "Angular **directives** modify DOM elements or their behavior. **Structural directives** change layout "
            "(now largely replaced by `@if`/`@for`). **Attribute directives** change appearance or behavior of an "
            "existing element — e.g., `ngClass`, `ngStyle`, or custom directives like `appHighlight`. Custom "
            "directives use **`@Directive`**, **`ElementRef`**, **`Renderer2`** (preferred over direct DOM "
            "manipulation for SSR compatibility), and **`@HostListener`** for event binding. **`@HostBinding`** "
            "binds properties to the host element. Directives are powerful for cross-cutting UI behavior like "
            "permission-based visibility, tooltips, and drag-and-drop."
        ),
        "code": """// Custom attribute directive — highlight row on hover
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective {
  private el = inject(ElementRef);
  private renderer = inject(Renderer2);

  @Input() appHighlightColor = 'yellow';

  @HostListener('mouseenter')
  onEnter() {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.appHighlightColor);
  }

  @HostListener('mouseleave')
  onLeave() {
    this.renderer.removeStyle(this.el.nativeElement, 'backgroundColor');
  }
}

// Usage: <tr appHighlight appHighlightColor="lightblue" *ngFor="let o of orders">""",
        "language": "typescript",
        "key_points": [
            "Attribute directives change element behavior/appearance",
            "Use Renderer2 instead of nativeElement for SSR safety",
            "HostListener binds to host element events",
            "Structural directives largely replaced by @if/@for",
        ],
    },
    "angular-unit-testing": {
        "explanation": (
            "Angular unit tests use **`TestBed`** to configure the testing module with providers, imports, and "
            "declarations. **`ComponentFixture`** wraps the component; **`detectChanges()`** triggers change "
            "detection. For HTTP, use **`provideHttpClientTesting()`** and **`HttpTestingController`** to mock "
            "and flush responses. **Jasmine** is the default runner; **Jest** is popular in enterprise for speed. "
            "Test **behavior not implementation** — verify rendered output and service interactions, not private "
            "fields. **`fakeAsync`/`tick`** control async timing. Standalone components simplify TestBed setup "
            "by importing only what the component needs."
        ),
        "code": """describe('OrderListComponent', () => {
  let fixture: ComponentFixture<OrderListComponent>;
  let httpMock: HttpTestingController;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OrderListComponent],  // standalone component
      providers: [provideHttpClient(), provideHttpClientTesting()]
    }).compileComponents();

    fixture = TestBed.createComponent(OrderListComponent);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it('renders orders from API', () => {
    fixture.detectChanges(); // triggers ngOnInit

    httpMock.expectOne('/api/orders').flush([
      { id: 1, customerName: 'Alice', total: 99.99 }
    ]);
    fixture.detectChanges();

    const rows = fixture.nativeElement.querySelectorAll('tr');
    expect(rows.length).toBe(1);
    expect(rows[0].textContent).toContain('Alice');
  });

  afterEach(() => httpMock.verify()); // no outstanding requests
});""",
        "language": "typescript",
        "key_points": [
            "TestBed.configureTestingModule with standalone imports",
            "HttpTestingController.expectOne().flush() for HTTP mocks",
            "ComponentFixture.detectChanges() triggers rendering",
            "Test behavior and DOM output, not private methods",
        ],
    },
    "ts-type-narrowing": {
        "explanation": (
            "**Type narrowing** is TypeScript's ability to refine a variable's type within a conditional block. "
            "Mechanisms include **`typeof`** checks, **`instanceof`**, **`in` operator**, **discriminated unions** "
            "(literal type tags like `{ type: 'success' }`), and **truthiness** checks. After narrowing, TypeScript "
            "knows the exact type — no casting needed. This is critical in Angular for handling **API result types**, "
            "**union route params**, and **template type guards**. The **`never` type** appears in exhaustive "
            "`switch` checks — if a new union member is added, the compiler flags unhandled cases."
        ),
        "code": """// Discriminated union — most common interview pattern
type ApiResult<T> =
  | { status: 'success'; data: T }
  | { status: 'error'; message: string; code: number };

function handleResult<T>(result: ApiResult<T>): T {
  if (result.status === 'error') {
    throw new Error(`[${result.code}] ${result.message}`);
  }
  return result.data; // TS knows this is success branch
}

// typeof and instanceof narrowing
function format(value: string | number | Date): string {
  if (value instanceof Date) return value.toISOString();
  if (typeof value === 'number') return value.toFixed(2);
  return value.toUpperCase();
}

// Exhaustive switch with never
function assertNever(x: never): never {
  throw new Error('Unexpected value: ' + x);
}""",
        "language": "typescript",
        "key_points": [
            "Discriminated unions with literal type tags",
            "typeof, instanceof, in — control-flow narrowing",
            "never type for exhaustive switch checks",
            "Avoid 'as' assertions when narrowing suffices",
        ],
    },
    "observables-vs-promises": {
        "explanation": (
            "**Promises** represent a **single future value** — they resolve once and cannot be cancelled natively. "
            "**Observables** (RxJS) emit **multiple values over time**, support **cancellation** via `unsubscribe`, "
            "and compose with **operators** (`map`, `filter`, `switchMap`, `debounceTime`). Angular's `HttpClient` "
            "returns Observables because HTTP can be retried, cancelled, and composed. Use **`firstValueFrom()`** "
            "or **`lastValueFrom()`** when you need a Promise from an Observable (e.g., in async/await code). "
            "For event streams (search-as-you-type, WebSocket), Observables are essential. For one-shot async "
            "in services, either works — but Observables integrate better with Angular's ecosystem."
        ),
        "code": """// Observable — cancellable, composable, multi-value
this.searchControl.valueChanges.pipe(
  debounceTime(300),              // wait 300ms after typing stops
  distinctUntilChanged(),         // skip duplicate values
  filter(term => term.length >= 2),
  switchMap(term => this.api.search(term)),  // cancel previous search
  takeUntil(this.destroy$)        // cancel on component destroy
).subscribe(results => this.results = results);

// Convert Observable → Promise when needed
async loadOrders(): Promise<Order[]> {
  return firstValueFrom(this.http.get<Order[]>('/api/orders'));
}

// Promise — single value, simpler mental model
const orders = await fetch('/api/orders').then(r => r.json());""",
        "language": "typescript",
        "key_points": [
            "Observables: multi-value, cancellable, composable with operators",
            "Promises: single value, simpler, native async/await",
            "HttpClient returns Observable — use firstValueFrom for await",
            "switchMap cancels previous inner Observable (search pattern)",
        ],
    },
    "angular-material-ui": {
        "explanation": (
            "**Angular Material** is Google's Material Design component library for Angular — providing "
            "production-ready UI components: **tables**, **dialogs**, **form controls**, **snackbars**, "
            "**sidenav**, **steppers**, and more. Import only the modules you need for **tree-shaking**. "
            "**Theming** uses SCSS mixins or prebuilt themes (`azure-blue`, `rose-red`). **`MatTable`** with "
            "**`MatPaginator`** and **`MatSort`** is the standard enterprise data grid pattern. **`MatDialog`** "
            "opens modal dialogs with injected data. Material integrates with Angular CDK for accessibility, "
            "overlay management, and drag-drop. It is the most common UI library in .NET + Angular enterprise stacks."
        ),
        "code": """@Component({
  selector: 'app-orders-table',
  standalone: true,
  imports: [MatTableModule, MatPaginatorModule, MatSortModule, MatButtonModule],
  template: `
    <table mat-table [dataSource]="dataSource" matSort>
      <ng-container matColumnDef="id">
        <th mat-header-cell *matHeaderCellDef mat-sort-header>ID</th>
        <td mat-cell *matCellDef="let row">{{ row.id }}</td>
      </ng-container>
      <ng-container matColumnDef="total">
        <th mat-header-cell *matHeaderCellDef mat-sort-header>Total</th>
        <td mat-cell *matCellDef="let row">{{ row.total | currency }}</td>
      </ng-container>
      <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
      <tr mat-row *matRowDef="let row; columns: displayedColumns"></tr>
    </table>
    <mat-paginator [pageSizeOptions]="[10, 25, 50]" />`
})
export class OrdersTableComponent implements AfterViewInit {
  displayedColumns = ['id', 'total'];
  dataSource = new MatTableDataSource<Order>([]);

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }
}""",
        "language": "typescript",
        "key_points": [
            "Import individual Mat modules for tree-shaking",
            "MatTableDataSource + MatPaginator + MatSort pattern",
            "MatDialog for modal workflows with MAT_DIALOG_DATA",
            "Theming via @angular/material prebuilt themes",
        ],
    },
    "form-validation": {
        "explanation": (
            "Angular **reactive forms** provide synchronous access to form state and validation. Attach "
            "**`Validators`** to `FormControl`s: `required`, `email`, `minLength`, `pattern`, and custom "
            "synchronous/async validators. **Cross-field validation** goes on the `FormGroup` via a group-level "
            "validator function. Display errors by checking `control.invalid && control.touched`. **Typed forms** "
            "(Angular 14+) give compile-time type safety on `form.value`. For async validation (e.g., check "
            "username availability), use **`AsyncValidatorFn`**. Always validate on the **server** too — client "
            "validation is UX, not security."
        ),
        "code": """this.form = this.fb.group({
  email: ['', [Validators.required, Validators.email]],
  password: ['', [Validators.required, Validators.minLength(8)]],
  confirmPassword: ['']
}, { validators: this.passwordMatchValidator });

passwordMatchValidator(group: AbstractControl): ValidationErrors | null {
  const pass = group.get('password')?.value;
  const confirm = group.get('confirmPassword')?.value;
  return pass === confirm ? null : { passwordMismatch: true };
}

onSubmit() {
  if (this.form.invalid) {
    this.form.markAllAsTouched(); // show all errors
    return;
  }
  this.authService.register(this.form.value as RegisterDto).subscribe();
}

// Template error display
// @if (form.get('email')?.invalid && form.get('email')?.touched) {
//   <span>Valid email required</span>
// }""",
        "language": "typescript",
        "key_points": [
            "Validators.required, email, minLength, pattern built-in",
            "Cross-field validation on FormGroup level",
            "markAllAsTouched() to show errors on submit",
            "Server-side validation is mandatory for security",
        ],
    },
    "lazy-loading-routes": {
        "explanation": (
            "**Lazy loading** defers loading feature code until the user navigates to that route — reducing "
            "initial bundle size and improving **Time to Interactive**. Modern Angular supports **`loadChildren`** "
            "for route files and **`loadComponent`** for single standalone components. Each lazy route creates a "
            "separate JavaScript chunk loaded on demand. **`PreloadAllModules`** or custom **`PreloadingStrategy`** "
            "can prefetch routes in the background after initial load. Combine with **`canActivate` guards** "
            "to protect lazy features. This is standard in enterprise Angular apps with multiple feature areas "
            "(orders, admin, reports)."
        ),
        "code": """// app.routes.ts — lazy-loaded feature routes
export const routes: Routes = [
  { path: '', component: HomeComponent },
  {
    path: 'orders',
    loadChildren: () =>
      import('./features/orders/orders.routes').then(m => m.ORDER_ROUTES),
    canActivate: [authGuard]
  },
  {
    path: 'admin',
    loadComponent: () =>
      import('./features/admin/admin.component').then(m => m.AdminComponent),
    canActivate: [adminGuard]
  },
  { path: '**', redirectTo: '' }
];

// orders.routes.ts — feature route file
export const ORDER_ROUTES: Routes = [
  { path: '', component: OrderListComponent },
  { path: ':id', component: OrderDetailComponent, resolve: { order: orderResolver } }
];

// Optional preloading after initial load
provideRouter(routes, withPreloading(PreloadAllModules))""",
        "language": "typescript",
        "key_points": [
            "loadChildren for route arrays, loadComponent for single component",
            "Each lazy route = separate JS chunk",
            "PreloadAllModules for background prefetch",
            "Always protect lazy routes with guards",
        ],
    },
    "ngrx-state": {
        "explanation": (
            "**NgRx** implements the **Redux pattern** for Angular — a predictable state container with "
            "**actions** (events), **reducers** (pure state transitions), **effects** (side effects like HTTP), "
            "and **selectors** (memoized queries). Use NgRx when multiple features share complex state, you need "
            "**time-travel debugging**, or audit requirements demand traceable state changes. For simpler apps, "
            "**ComponentStore** (NgRx local store) or **signals** may suffice. NgRx **Entity Adapter** simplifies "
            "collection CRUD. The `@ngrx/store-devtools` browser extension visualizes action history. "
            "Enterprise teams often use NgRx for auth, cart, and notification state across lazy-loaded modules."
        ),
        "code": """// Actions
export const loadOrders = createAction('[Orders Page] Load');
export const loadOrdersSuccess = createAction(
  '[Orders API] Load Success', props<{ orders: Order[] }>()
);
export const loadOrdersFailure = createAction(
  '[Orders API] Load Failure', props<{ error: string }>()
);

// Reducer
export const ordersFeature = createFeature({
  name: 'orders',
  reducer: createReducer(initialState,
    on(loadOrders, state => ({ ...state, loading: true })),
    on(loadOrdersSuccess, (state, { orders }) => ({
      ...state, orders, loading: false
    }))
  )
});

// Effect — side effect (HTTP call)
loadOrders$ = createEffect(() => this.actions$.pipe(
  ofType(loadOrders),
  switchMap(() => this.api.getOrders().pipe(
    map(orders => loadOrdersSuccess({ orders })),
    catchError(err => of(loadOrdersFailure({ error: err.message })))
  ))
));""",
        "language": "typescript",
        "key_points": [
            "Actions → Reducers → Selectors → Effects pipeline",
            "ComponentStore for feature-local state (lighter than global store)",
            "Entity Adapter for normalized collections",
            "DevTools for time-travel debugging",
        ],
    },
    "angular-ssr-hydration": {
        "explanation": (
            "**Server-Side Rendering (SSR)** generates HTML on the server for each request — improving **SEO**, "
            "**First Contentful Paint**, and social media link previews. **`@angular/ssr`** (formerly Angular Universal) "
            "provides `provideServerRendering()` and a Node.js Express server. **Hydration** (Angular 16+) attaches "
            "client-side behavior to server-rendered DOM **without destroying and re-creating** it — eliminating "
            "flicker. **`TransferState`** serializes server-fetched data to the client, avoiding duplicate HTTP "
            "calls. Use SSR for public-facing pages; admin dashboards behind auth often remain CSR-only."
        ),
        "code": """// Add SSR: ng add @angular/ssr

// app.config.server.ts
export const serverConfig: ApplicationConfig = {
  providers: [provideServerRendering()]
};

// TransferState — avoid double HTTP fetch
@Injectable({ providedIn: 'root' })
export class OrderService {
  private http = inject(HttpClient);
  private transferState = inject(TransferState);

  getOrders(): Observable<Order[]> {
    const key = makeStateKey<Order[]>('orders');

    if (this.transferState.hasKey(key)) {
      const data = this.transferState.get(key, []);
      this.transferState.remove(key);
      return of(data); // use server-fetched data on client
    }

    return this.http.get<Order[]>('/api/orders').pipe(
      tap(orders => {
        if (isPlatformServer(inject(PLATFORM_ID))) {
          this.transferState.set(key, orders);
        }
      })
    );
  }
}""",
        "language": "typescript",
        "key_points": [
            "ng add @angular/ssr scaffolds server.ts and config",
            "Hydration attaches client logic without DOM rebuild",
            "TransferState prevents duplicate HTTP on client boot",
            "SSR for public pages; CSR fine for authenticated apps",
        ],
    },
    "onpush-strategy": {
        "explanation": (
            "**`ChangeDetectionStrategy.OnPush`** tells Angular to check a component only when: (1) an **`@Input` "
            "reference** changes, (2) an event originates from the component, (3) an **`async` pipe** receives a "
            "new value, or (4) **`markForCheck()`** is called. Default change detection checks the entire tree "
            "on every event — expensive in large apps. OnPush with **immutable data patterns** (spread operator, "
            "new array references) dramatically reduces checks. Combined with **signals**, OnPush becomes the "
            "natural default. Avoid mutating `@Input` object properties in place — Angular won't detect the change."
        ),
        "code": """@Component({
  selector: 'app-order-list',
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    @for (order of orders(); track order.id) {
      <app-order-row [order]="order" (delete)="removeOrder($event)" />
    }
  `
})
export class OrderListComponent {
  orders = input.required<Order[]>();
  private orderService = inject(OrderService);

  removeOrder(id: number) {
    // Immutable update — new reference triggers OnPush
    const updated = this.orders().filter(o => o.id !== id);
    // With signal input, parent must update; or use local signal:
    this.localOrders.update(list => list.filter(o => o.id !== id));
  }

  localOrders = signal<Order[]>([]);

  refresh() {
    this.orderService.getOrders().subscribe(orders => {
      this.localOrders.set(orders); // new reference → OnPush detects
    });
  }
}""",
        "language": "typescript",
        "key_points": [
            "OnPush checks only on input ref change, events, async pipe",
            "Immutable updates: [...arr, newItem] not arr.push(newItem)",
            "markForCheck() when updating from external async source",
            "Signals + OnPush is the 2025/2026 performance default",
        ],
    },
    "acid-properties": {
        "explanation": (
            "**ACID** defines the four guarantees of reliable database transactions. **Atomicity** means all "
            "operations in a transaction succeed or all roll back — no partial updates. **Consistency** ensures "
            "the database moves from one valid state to another, honoring constraints and rules. **Isolation** "
            "controls how concurrent transactions interact — preventing dirty reads and other anomalies. "
            "**Durability** guarantees committed data survives crashes (written to disk/WAL). In .NET, EF Core's "
            "`SaveChangesAsync()` wraps changes in a transaction by default. For multi-step operations across "
            "entities or raw SQL, use explicit `BeginTransactionAsync()`."
        ),
        "code": """// EF Core — SaveChanges is atomic by default
await using var tx = await _db.Database.BeginTransactionAsync();
try
{
    var order = new Order { CustomerName = "Alice", Total = 150m };
    _db.Orders.Add(order);
    await _db.SaveChangesAsync(); // INSERT Order

    _db.Inventory.Update(inventory); // UPDATE stock
    await _db.SaveChangesAsync();

    await tx.CommitAsync(); // both succeed together
}
catch
{
    await tx.RollbackAsync(); // both rolled back on any failure
    throw;
}""",
        "language": "csharp",
        "key_points": [
            "Atomicity — all or nothing, no partial commits",
            "Isolation level controls concurrency behavior",
            "Durability — committed data survives server crash",
            "SaveChangesAsync wraps changes in implicit transaction",
        ],
    },
    "normalization": {
        "explanation": (
            "**Normalization** organizes relational data to reduce redundancy and anomalies. **1NF** requires "
            "atomic column values and no repeating groups (no `Product1, Product2` columns). **2NF** removes "
            "partial dependencies — non-key columns must depend on the **whole** primary key (relevant for "
            "composite keys). **3NF** removes **transitive dependencies** — non-key columns depend only on the "
            "primary key, not on other non-key columns. Higher normal forms (BCNF, 4NF) exist but 3NF suffices "
            "for most apps. Denormalization is sometimes intentional for read performance — but understand "
            "normalization first before breaking it."
        ),
        "code": """-- ❌ Denormalized (repeating groups, update anomalies)
CREATE TABLE Orders (
    Id INT PRIMARY KEY,
    CustomerName NVARCHAR(100),
    Product1 NVARCHAR(100),
    Product2 NVARCHAR(100)
);

-- ✅ 3NF — separate entities, FK relationships
CREATE TABLE Customers (Id INT PRIMARY KEY, Name NVARCHAR(100));
CREATE TABLE Orders (Id INT PRIMARY KEY, CustomerId INT REFERENCES Customers(Id), OrderDate DATE);
CREATE TABLE OrderLines (
    OrderId INT REFERENCES Orders(Id),
    ProductId INT REFERENCES Products(Id),
    Quantity INT,
    PRIMARY KEY (OrderId, ProductId)
);
CREATE TABLE Products (Id INT PRIMARY KEY, Name NVARCHAR(100), Price DECIMAL(18,2));""",
        "language": "sql",
        "key_points": [
            "1NF — atomic values, no repeating groups",
            "2NF — no partial key dependencies",
            "3NF — no transitive dependencies on non-key columns",
            "Denormalize intentionally for read performance when needed",
        ],
    },
    "sql-views": {
        "explanation": (
            "A **SQL view** is a stored query that acts as a virtual table — no data duplication (usually). "
            "Views **simplify complex joins** for reporting, **restrict column access** for security, and "
            "**abstract schema changes** from application code. SQL Server supports **indexed views** (materialized) "
            "for performance. EF Core can map entities to views using `ToView()`. Views can be updatable under "
            "certain conditions (single table, no aggregation). In enterprise apps, views are common for "
            "read-only reporting dashboards and DBA-managed data access layers."
        ),
        "code": """-- Create a view joining orders and customers
CREATE VIEW vw_OrderSummary AS
SELECT o.Id, c.Name AS CustomerName, o.OrderDate, o.Total, o.Status
FROM Orders o
INNER JOIN Customers c ON c.Id = o.CustomerId
WHERE o.IsDeleted = 0;

-- Query the view like a table
SELECT * FROM vw_OrderSummary WHERE Total > 1000 ORDER BY OrderDate DESC;

// EF Core — map entity to view (read-only)
model.Entity<OrderSummary>().ToView("vw_OrderSummary").HasNoKey();""",
        "language": "sql",
        "key_points": [
            "Virtual table — stored query, not data copy",
            "Indexed views in SQL Server for performance",
            "EF Core ToView() for read-only entity mapping",
            "Use for reporting, security, and schema abstraction",
        ],
    },
    "sql-injection-prevention": {
        "explanation": (
            "**SQL injection** occurs when user input is concatenated into SQL strings, allowing attackers to "
            "execute arbitrary commands. Prevention: **always use parameterized queries**. EF Core LINQ automatically "
            "parameterizes. Dapper uses `@Param` syntax. Raw SQL in EF uses `{0}` placeholders — never string "
            "interpolation. Also validate input at the API layer (length, format, allowlists). Stored procedures "
            "with parameters are safe; dynamic SQL inside sprocs is not. ORMs don't eliminate injection if you "
            "build raw SQL strings manually. This is a top security interview question for full-stack .NET roles."
        ),
        "code": """// ❌ VULNERABLE — never concatenate user input
var sql = $"SELECT * FROM Users WHERE Email = '{userInput}'";
// Attacker input: ' OR '1'='1' -- returns all users

// ✅ Safe — EF Core LINQ (auto-parameterized)
var user = await _db.Users
    .FirstOrDefaultAsync(u => u.Email == userInput);

// ✅ Safe — parameterized raw SQL
var orders = await _db.Orders
    .FromSqlRaw("SELECT * FROM Orders WHERE Status = {0} AND Total > {1}", status, minTotal)
    .ToListAsync();

// ✅ Safe — Dapper
var result = await conn.QueryAsync<Order>(
    "SELECT * FROM Orders WHERE CustomerId = @Id", new { Id = customerId });""",
        "language": "csharp",
        "key_points": [
            "Never concatenate user input into SQL strings",
            "EF Core LINQ and parameterized raw SQL are safe",
            "Validate and sanitize at API layer too",
            "Use least-privilege DB accounts in production",
        ],
    },
    "sqlserver-vs-postgresql": {
        "explanation": (
            "**SQL Server** is Microsoft's enterprise RDBMS with deep **Azure integration** (Azure SQL), SSIS, "
            "Reporting Services, and T-SQL features (indexed views, columnstore). **PostgreSQL** is open-source, "
            "cross-platform, with strong **JSON/JSONB**, arrays, full-text search, and lower licensing cost. "
            "Both are fully supported by **EF Core** via `UseSqlServer()` and `UseNpgsql()`. Choose SQL Server "
            "for Microsoft-centric Azure stacks; PostgreSQL for cost-sensitive or polyglot cloud deployments. "
            "Application code stays largely the same — differences appear in SQL dialect, types, and tooling."
        ),
        "code": """// Same EF Core code — swap provider
builder.Services.AddDbContext<AppDbContext>(options =>
{
    // SQL Server / Azure SQL
    options.UseSqlServer(connectionString);

    // PostgreSQL
    // options.UseNpgsql(connectionString);
});

// PostgreSQL JSON query (Npgsql)
var highPriority = await _db.Orders
    .Where(o => EF.Functions.JsonContains(o.Metadata, @"{""priority"":""high""}"))
    .ToListAsync();

// SQL Server specific — temporal tables, columnstore
// PostgreSQL specific — JSONB operators, array types, CTEs""",
        "language": "csharp",
        "key_points": [
            "Both fully supported by EF Core",
            "SQL Server: Azure integration, enterprise tooling",
            "PostgreSQL: open-source, JSONB, lower cost",
            "Application code mostly portable — watch SQL dialect differences",
        ],
    },
    "isolation-levels": {
        "explanation": (
            "**Transaction isolation levels** control what one transaction can see while another is in progress. "
            "From least to most strict: **Read Uncommitted** (dirty reads allowed), **Read Committed** (default — "
            "no dirty reads), **Repeatable Read** (same row reads return same value), **Serializable** (full "
            "isolation, prevents phantom reads). Higher isolation = more locking = less concurrency. SQL Server "
            "default is Read Committed; PostgreSQL default is Read Committed with MVCC. In EF Core, set via "
            "`BeginTransactionAsync(IsolationLevel.ReadCommitted)`. Most web apps use default; adjust only when "
            "you have proven concurrency bugs."
        ),
        "code": """// Explicit isolation level in EF Core
await using var tx = await _db.Database.BeginTransactionAsync(
    System.Data.IsolationLevel.RepeatableRead);
try
{
    var order = await _db.Orders.FindAsync(orderId);
    order!.Status = OrderStatus.Processing;
    await _db.SaveChangesAsync();
    await tx.CommitAsync();
}
catch { await tx.RollbackAsync(); throw; }

// Isolation level trade-offs:
// Read Uncommitted  — dirty reads possible (avoid)
// Read Committed    — default, prevents dirty reads
// Repeatable Read   — prevents non-repeatable reads
// Serializable      — strictest, prevents phantom reads, slowest""",
        "language": "csharp",
        "key_points": [
            "Read Committed is default for most databases",
            "Higher isolation = more locks = less concurrency",
            "Serializable prevents phantoms but hurts throughput",
            "Optimistic concurrency (RowVersion) often better than Serializable",
        ],
    },
    "stored-procedures": {
        "explanation": (
            "**Stored procedures** are precompiled SQL stored in the database. Benefits: **performance** (cached "
            "execution plan), **security** (grant EXEC without table access), **centralized business logic** "
            "(DBA can tune without app redeploy), and **reduced network traffic**. Drawbacks: harder to version "
            "control, test, and debug compared to application code. In .NET, call via EF Core `FromSqlRaw` or "
            "Dapper. EF Core migrations don't manage sproc bodies — maintain them separately. Common in legacy "
            "enterprise and reporting-heavy systems where DBAs own query optimization."
        ),
        "code": """-- SQL Server stored procedure
CREATE PROCEDURE usp_GetOrdersByCustomer
    @CustomerId INT,
    @MinTotal DECIMAL(18,2) = 0
AS
BEGIN
    SET NOCOUNT ON;
    SELECT Id, CustomerName, Total, OrderDate
    FROM Orders
    WHERE CustomerId = @CustomerId AND Total >= @MinTotal AND IsDeleted = 0
    ORDER BY OrderDate DESC;
END;

// Call from EF Core
var orders = await _db.Set<OrderDto>()
    .FromSqlRaw("EXEC usp_GetOrdersByCustomer @CustomerId = {0}, @MinTotal = {1}",
        customerId, 100m)
    .AsNoTracking()
    .ToListAsync();""",
        "language": "sql",
        "key_points": [
            "Precompiled plans — faster for repeated calls",
            "Grant EXEC without direct table SELECT permission",
            "EF migrations don't manage sproc bodies",
            "Prefer app code for new greenfield projects",
        ],
    },
    "index-strategies": {
        "explanation": (
            "Effective **index design** is critical for query performance. Index columns used in **WHERE**, "
            "**JOIN**, and **ORDER BY** clauses. A **clustered index** defines physical row order (one per table). "
            "**Nonclustered indexes** are separate structures with pointers to data. **Covering indexes** include "
            "all columns needed by a query (via INCLUDE) — avoiding key lookups. **Filtered indexes** index a "
            "subset of rows (e.g., `WHERE Status = 'Active'`). Monitor for **index scans vs seeks** in execution "
            "plans. Over-indexing slows INSERT/UPDATE/DELETE — balance read vs write performance."
        ),
        "code": """-- Nonclustered index on foreign key + filter column
CREATE NONCLUSTERED INDEX IX_Orders_CustomerId_Status
ON Orders (CustomerId, Status)
INCLUDE (OrderDate, Total)  -- covering index: query needs no table lookup
WHERE IsDeleted = 0;        -- filtered index: only active orders

-- Find missing indexes (SQL Server DMVs)
SELECT d.statement, d.equality_columns, d.inequality_columns,
       s.avg_user_impact, s.user_seeks
FROM sys.dm_db_missing_index_details d
JOIN sys.dm_db_missing_index_groups g ON d.index_handle = g.index_handle
JOIN sys.dm_db_missing_index_group_stats s ON g.index_group_handle = s.group_handle;""",
        "language": "sql",
        "key_points": [
            "Index FK columns and WHERE/JOIN columns",
            "INCLUDE creates covering indexes — avoids key lookup",
            "Filtered indexes for subset queries (active, non-deleted)",
            "Monitor fragmentation — rebuild/reorganize periodically",
        ],
    },
    "connection-pooling": {
        "explanation": (
            "**Connection pooling** reuses open database connections instead of creating new TCP connections "
            "for each request — dramatically reducing latency. ADO.NET pools connections **by default** using "
            "the connection string as the pool key. Settings: **`Max Pool Size`** (default 100), **`Min Pool Size`**, "
            "**`Connection Timeout`**. In ASP.NET Core, **`DbContext` is scoped per request** — one context per "
            "HTTP request, returned to pool after request completes. Pool exhaustion causes timeout errors — "
            "symptoms: slow responses, `Timeout expired` exceptions. Fix: close connections promptly, increase "
            "pool size, or reduce connection hold time."
        ),
        "code": """// Connection string with pool settings
"Server=myserver.database.windows.net;Database=OrderDb;
 Max Pool Size=200;Min Pool Size=10;Connection Timeout=30;
 Encrypt=True;TrustServerCertificate=False"

// ASP.NET Core — DbContext scoped per request (automatic pooling)
builder.Services.AddDbContextPool<AppDbContext>(options =>
    options.UseSqlServer(connectionString), poolSize: 128);

// Anti-pattern — long-running connection outside request scope
// Bad: holding connection open during external API call
// Good: query DB, release connection, then call external API""",
        "language": "csharp",
        "key_points": [
            "Pooling enabled by default in ADO.NET",
            "DbContext scoped per HTTP request",
            "Pool exhaustion causes Timeout expired errors",
            "AddDbContextPool reuses context instances for performance",
        ],
    },
    "pagination-strategies": {
        "explanation": (
            "Two main pagination strategies: **offset** (`SKIP`/`OFFSET`) and **keyset** (seek/cursor). "
            "Offset is simple (`Skip(20).Take(20)`) but **degrades on deep pages** — SQL Server must scan "
            "and discard all preceding rows. **Keyset pagination** uses the last-seen key (`WHERE Id > @lastId "
            "ORDER BY Id LIMIT 20`) — **constant time** regardless of page depth. Return a **cursor token** "
            "to the client for the next page. Offset works for small datasets and admin UIs with page numbers. "
            "Keyset is essential for infinite scroll and high-volume APIs."
        ),
        "code": """// Offset pagination — simple but slow on page 5000
public async Task<PagedResult<Order>> GetPageAsync(int page, int size)
{
    var items = await _db.Orders.AsNoTracking()
        .OrderBy(o => o.Id)
        .Skip((page - 1) * size).Take(size)
        .ToListAsync();
    var total = await _db.Orders.CountAsync();
    return new PagedResult<Order>(items, total, page, size);
}

// Keyset pagination — fast at any depth
public async Task<CursorResult<Order>> GetAfterAsync(int lastId, int size)
{
    var items = await _db.Orders.AsNoTracking()
        .Where(o => o.Id > lastId)
        .OrderBy(o => o.Id).Take(size)
        .ToListAsync();
    var nextCursor = items.LastOrDefault()?.Id;
    return new CursorResult<Order>(items, nextCursor);
}""",
        "language": "csharp",
        "key_points": [
            "Offset degrades on deep pages — O(offset + limit)",
            "Keyset uses WHERE Id > lastSeen — constant time",
            "Return cursor token for next page to client",
            "Offset fine for admin UIs with page numbers",
        ],
    },
    "soft-delete-pattern": {
        "explanation": (
            "**Soft delete** marks records as deleted (`IsDeleted = true`, `DeletedAt = timestamp`) instead of "
            "physical `DELETE`. Benefits: **audit trail**, **referential integrity** preserved, **undo capability**, "
            "and **reporting** on historical data. Implement by overriding `SaveChanges` to intercept `Deleted` "
            "state and convert to `Modified`. Combine with **global query filters** to auto-exclude soft-deleted "
            "rows. Challenges: unique constraints must account for deleted rows (filtered unique index), storage "
            "grows over time, and **GDPR** may require hard delete for personal data."
        ),
        "code": """public interface ISoftDeletable
{
    bool IsDeleted { get; set; }
    DateTime? DeletedAt { get; set; }
}

public override int SaveChanges()
{
    foreach (var entry in ChangeTracker.Entries<ISoftDeletable>())
    {
        if (entry.State == EntityState.Deleted)
        {
            entry.State = EntityState.Modified;
            entry.Entity.IsDeleted = true;
            entry.Entity.DeletedAt = DateTime.UtcNow;
        }
    }
    return base.SaveChanges();
}

// Global filter — auto-exclude deleted rows
model.Entity<Order>().HasQueryFilter(o => !o.IsDeleted);

// Hard delete for GDPR
await _db.Orders.IgnoreQueryFilters()
    .Where(o => o.Id == id).ExecuteDeleteAsync();""",
        "language": "csharp",
        "key_points": [
            "Override SaveChanges to intercept Deleted state",
            "Combine with HasQueryFilter for automatic exclusion",
            "Filtered unique indexes for soft-deleted uniqueness",
            "Hard delete for GDPR/personal data erasure",
        ],
    },
    "global-query-filters": {
        "explanation": (
            "EF Core **global query filters** automatically append a WHERE clause to every query for an entity "
            "type. Common uses: **soft delete** (`!IsDeleted`), **multi-tenancy** (`TenantId == currentTenant`), "
            "and **active records only**. Defined in `OnModelCreating` with `HasQueryFilter()`. Multiple filters "
            "on the same entity are **AND-combined**. Use **`IgnoreQueryFilters()`** for admin/reporting queries "
            "that need all records. Filters apply to direct queries and `Include()` navigation. They do NOT apply "
            "to raw SQL. Essential pattern for SaaS multi-tenant applications."
        ),
        "code": """public class AppDbContext : DbContext
{
    private readonly ITenantProvider _tenant;

    protected override void OnModelCreating(ModelBuilder model)
    {
        // Soft delete filter
        model.Entity<Order>().HasQueryFilter(o => !o.IsDeleted);

        // Multi-tenancy filter
        model.Entity<Order>().HasQueryFilter(o => o.TenantId == _tenant.TenantId);
        // Both filters AND-combined: !IsDeleted AND TenantId == current
    }
}

// Normal query — filters applied automatically
var orders = await _db.Orders.ToListAsync();
// SQL: SELECT * FROM Orders WHERE IsDeleted = 0 AND TenantId = @tenant

// Admin query — bypass filters
var allOrders = await _db.Orders.IgnoreQueryFilters().ToListAsync();""",
        "language": "csharp",
        "key_points": [
            "HasQueryFilter in OnModelCreating",
            "Multiple filters AND-combined",
            "IgnoreQueryFilters() for admin/reporting",
            "Standard for multi-tenancy and soft delete",
        ],
    },
    "owned-entity-types": {
        "explanation": (
            "**Owned entity types** in EF Core model **value objects** that belong to a parent entity — no "
            "separate identity or table (usually). Examples: `Address`, `Money`, `Dimensions`. Configured with "
            "`OwnsOne()` or `OwnsMany()`. Columns are stored in the **parent table** with a prefix (e.g., "
            "`ShippingAddress_Street`). Owned types cannot be queried directly via `DbSet`. They support nested "
            "ownership and table splitting. This aligns with **DDD value objects** — immutable, no identity, "
            "defined by their attributes. Alternative: complex types or JSON columns for flexible schemas."
        ),
        "code": """public class Order
{
    public int Id { get; set; }
    public Address ShippingAddress { get; set; } = null!;
    public Address BillingAddress { get; set; } = null!;
}

public class Address  // no Id — value object owned by Order
{
    public string Street { get; set; } = "";
    public string City { get; set; } = "";
    public string PostalCode { get; set; } = "";
}

// Configuration
model.Entity<Order>().OwnsOne(o => o.ShippingAddress, sa =>
{
    sa.Property(a => a.Street).HasColumnName("ShipStreet");
    sa.Property(a => a.City).HasColumnName("ShipCity");
});
model.Entity<Order>().OwnsOne(o => o.BillingAddress);

// Table columns: ShipStreet, ShipCity, BillingAddress_Street, etc.""",
        "language": "csharp",
        "key_points": [
            "OwnsOne/OwnsMany — no separate identity",
            "Columns stored in parent table with prefix",
            "Cannot query owned types via DbSet directly",
            "Aligns with DDD value objects pattern",
        ],
    },
    "value-converters": {
        "explanation": (
            "EF Core **value converters** translate between CLR types and database column types during "
            "read/write. Built-in: **enum ↔ string/int**, **bool ↔ int**, **DateTime ↔ long**. Custom converters "
            "for encryption, compression, or complex value objects. Defined with `HasConversion()` on a property. "
            "The converter must handle **null** explicitly if the property is nullable. Value comparers "
            "(`HasConversion(converter, comparer)`) control change tracking for complex types. Useful when "
            "the database stores data differently than your domain model prefers."
        ),
        "code": """// Enum stored as string in database
model.Entity<Order>()
    .Property(o => o.Status)
    .HasConversion<string>(); // DB column: 'Pending', 'Shipped', etc.

// Custom converter — encrypt email at rest
model.Entity<User>()
    .Property(u => u.Email)
    .HasConversion(
        v => Encrypt(v),    // CLR → DB
        v => Decrypt(v));   // DB → CLR

// Value object as JSON string
model.Entity<Product>()
    .Property(p => p.Metadata)
    .HasConversion(
        v => JsonSerializer.Serialize(v, (JsonSerializerOptions?)null),
        v => JsonSerializer.Deserialize<ProductMetadata>(v, (JsonSerializerOptions?)null)!);""",
        "language": "csharp",
        "key_points": [
            "HasConversion maps CLR type ↔ DB column type",
            "Built-in enum-to-string is most common",
            "Custom converters for encryption, JSON, etc.",
            "Handle null explicitly for nullable properties",
        ],
    },
    "change-tracking": {
        "explanation": (
            "EF Core **change tracking** monitors entity modifications via the **`ChangeTracker`**. When you "
            "query entities (without `AsNoTracking`), EF snapshots their state. On `SaveChangesAsync()`, it "
            "compares current vs original values and generates **INSERT/UPDATE/DELETE** SQL only for changed "
            "entities. States: **Added**, **Modified**, **Deleted**, **Unchanged**, **Detached**. "
            "**`AsNoTracking()`** skips tracking for read-only queries — faster, less memory. For disconnected "
            "scenarios (API payloads), use **`Attach()` + mark Modified** or **`Update()`**. Understanding "
            "tracking prevents surprise UPDATE statements and memory leaks in long-lived contexts."
        ),
        "code": """// Tracked query — EF watches for changes
var order = await _db.Orders.Include(o => o.Lines).FirstAsync(o => o.Id == 1);
order.Status = OrderStatus.Shipped; // automatically marked Modified
order.Lines.Add(new OrderLine { ProductId = 5, Qty = 2 }); // marked Added
await _db.SaveChangesAsync(); // generates UPDATE + INSERT SQL

// Read-only — no tracking overhead
var summaries = await _db.Orders.AsNoTracking()
    .Select(o => new OrderSummary(o.Id, o.Total)).ToListAsync();

// Disconnected update (from API payload)
public async Task UpdateOrderAsync(OrderDto dto)
{
    var order = new Order { Id = dto.Id, Status = dto.Status };
    _db.Orders.Update(order); // marks all properties Modified
    await _db.SaveChangesAsync();
}""",
        "language": "csharp",
        "key_points": [
            "ChangeTracker monitors Added/Modified/Deleted/Unchanged",
            "AsNoTracking() for read-only queries — faster",
            "SaveChanges generates SQL only for changed entities",
            "Update() marks all properties Modified (disconnected scenario)",
        ],
    },
    "dbcontext-pooling": {
        "explanation": (
            "**DbContext pooling** (`AddDbContextPool`) reuses `DbContext` instances across requests — resetting "
            "internal state between uses. This avoids the cost of creating new context instances (model compilation, "
            "service injection). Default pool size is 1024. **Critical rule**: never store **per-request state** "
            "on the DbContext itself (fields, cached lists) — the instance is reused. Use scoped services or "
            "`IMemoryCache` for per-request data. Do not inject **scoped services** into the DbContext constructor "
            "when pooling — use `IDbContextFactory` or `IServiceProvider` instead."
        ),
        "code": """// Register pooled context — faster than AddDbContext
builder.Services.AddDbContextPool<AppDbContext>(options =>
    options.UseSqlServer(connectionString),
    poolSize: 128);

public class AppDbContext : DbContext
{
    // ❌ BAD — state persists across requests with pooling!
    // private List<Order> _cachedOrders = [];

    // ✅ GOOD — stateless context, query per request
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
        ],
    },
    "raw-sql-ef": {
        "explanation": (
            "EF Core supports **raw SQL** for queries EF can't translate or for DBA-optimized SQL. "
            "**`FromSqlRaw`** executes SELECT against a `DbSet` — returned entities are tracked by default. "
            "**`ExecuteSqlRawAsync`** runs INSERT/UPDATE/DELETE without returning entities. Always use "
            "**parameter placeholders** (`{0}`, `{1}`) — EF parameterizes them automatically. Never use "
            "string interpolation. EF 8+ adds **`SqlQuery<T>`** for arbitrary result types. Raw SQL bypasses "
            "global query filters unless you include the filter conditions manually. Use when LINQ generates "
            "suboptimal SQL or for database-specific features."
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
        "SELECT Department, COUNT(*) AS HeadCount, AVG(Salary) AS AvgSalary " +
        "FROM Employees GROUP BY Department")
    .ToListAsync();""",
        "language": "csharp",
        "key_points": [
            "FromSqlRaw for SELECT returning entities",
            "ExecuteSqlRawAsync for INSERT/UPDATE/DELETE",
            "Always use {0} placeholders — never string interpolation",
            "SqlQuery<T> (EF 8+) for arbitrary result shapes",
        ],
    },
    "window-functions": {
        "explanation": (
            "**Window functions** perform calculations across a set of rows related to the current row — "
            "without collapsing groups like `GROUP BY`. **`ROW_NUMBER()`** assigns unique sequential numbers. "
            "**`RANK()`** allows ties with gaps; **`DENSE_RANK()`** allows ties without gaps. **`PARTITION BY`** "
            "defines window groups; **`ORDER BY`** defines ordering within the window. Common uses: top-N per "
            "group, running totals, moving averages, deduplication. Supported in SQL Server and PostgreSQL. "
            "EF Core 8+ translates some window functions; complex ones may need raw SQL."
        ),
        "code": """-- Top 3 orders per customer by total
WITH RankedOrders AS (
    SELECT Id, CustomerId, Total, OrderDate,
        ROW_NUMBER() OVER (
            PARTITION BY CustomerId
            ORDER BY Total DESC
        ) AS RowNum
    FROM Orders
    WHERE IsDeleted = 0
)
SELECT Id, CustomerId, Total, OrderDate
FROM RankedOrders
WHERE RowNum <= 3;

-- Running total per customer
SELECT Id, CustomerId, Total,
    SUM(Total) OVER (PARTITION BY CustomerId ORDER BY OrderDate) AS RunningTotal,
    RANK() OVER (ORDER BY Total DESC) AS RevenueRank
FROM Orders;""",
        "language": "sql",
        "key_points": [
            "ROW_NUMBER — unique; RANK/DENSE_RANK allow ties",
            "PARTITION BY defines window groups",
            "Top-N per group is the classic interview pattern",
            "EF Core 8+ translates some; complex ones need raw SQL",
        ],
    },
    "bulk-insert-update": {
        "explanation": (
            "Standard `SaveChangesAsync()` sends **one SQL statement per entity** — too slow for thousands of "
            "records. EF Core 7+ provides **`ExecuteUpdateAsync`** and **`ExecuteDeleteAsync`** for bulk "
            "operations without loading entities into memory. For large inserts, use **EFCore.BulkExtensions**, "
            "**SqlBulkCopy** (SQL Server), or **PostgreSQL COPY**. Bulk operations bypass change tracking — "
            "they don't trigger interceptors or domain events. Use for batch imports, archival, and mass status "
            "updates. Always test on staging with production-scale data volumes."
        ),
        "code": """// EF Core 7+ — bulk update without loading entities
var cancelled = await _db.Orders
    .Where(o => o.Status == OrderStatus.Pending && o.CreatedAt < cutoff)
    .ExecuteUpdateAsync(setters => setters
        .SetProperty(o => o.Status, OrderStatus.Cancelled)
        .SetProperty(o => o.UpdatedAt, DateTime.UtcNow));

// EF Core 7+ — bulk delete
var deleted = await _db.AuditLogs
    .Where(l => l.CreatedAt < retentionDate)
    .ExecuteDeleteAsync();

// Large insert — third-party BulkExtensions
await _db.BulkInsertAsync(orders, options => {
    options.BatchSize = 5000;
    options.SetOutputIdentity = true; // populate generated IDs
});""",
        "language": "csharp",
        "key_points": [
            "ExecuteUpdate/ExecuteDelete — no entity loading (EF 7+)",
            "BulkExtensions or SqlBulkCopy for large inserts",
            "Bypasses change tracking and interceptors",
            "Test with production-scale data volumes",
        ],
    },
    "compiled-queries": {
        "explanation": (
            "**Compiled queries** cache the LINQ expression tree translation so EF doesn't recompile the same "
            "query on every call. Define once with **`EF.CompileAsyncQuery`** or **`EF.CompileQuery`**, then "
            "invoke with the DbContext and parameters. Benefit is modest for simple queries but meaningful for "
            "**high-frequency hot paths** (e.g., auth checks, config lookups called on every request). Cannot "
            "compile queries with dynamic predicates — the expression must be fixed. Profile before optimizing; "
            "premature compiled queries add complexity without measurable gain."
        ),
        "code": """// Compile once — reuse across all requests
private static readonly Func<AppDbContext, int, Task<Order?>> GetOrderById =
    EF.CompileAsyncQuery((AppDbContext db, int id) =>
        db.Orders.AsNoTracking().FirstOrDefault(o => o.Id == id));

private static readonly Func<AppDbContext, int, IAsyncEnumerable<OrderLine>> GetOrderLines =
    EF.CompileAsyncQuery((AppDbContext db, int orderId) =>
        db.OrderLines.AsNoTracking().Where(l => l.OrderId == orderId));

// Usage in service
public async Task<Order?> GetOrderAsync(int id) =>
    await GetOrderById(_db, id);""",
        "language": "csharp",
        "key_points": [
            "EF.CompileAsyncQuery — define once, reuse everywhere",
            "Meaningful for high-frequency identical queries",
            "Cannot compile dynamic/runtime-built predicates",
            "Profile first — marginal gain for simple queries",
        ],
    },
    "migration-strategy": {
        "explanation": (
            "A production **EF Core migration strategy** ensures schema changes are safe, reviewable, and "
            "reversible. Generate **idempotent SQL scripts** in CI (`dotnet ef migrations script --idempotent`) "
            "so scripts can be re-run safely. Have DBAs review scripts in PRs. Apply via **pipeline**, not "
            "`Database.Migrate()` on app startup in production. For **zero-downtime deploys**, make migrations "
            "**backward-compatible** — add columns as nullable first, deploy app, then backfill and add constraints. "
            "Never edit already-applied migrations. Keep data migrations (seed/fix) separate from schema migrations."
        ),
        "code": """# CI/CD pipeline — generate idempotent script
dotnet ef migrations script --idempotent -o deploy/migration.sql
# DBA reviews migration.sql in PR
# Pipeline applies script in maintenance window

# Development only — auto-migrate on startup
if (app.Environment.IsDevelopment())
{
    using var scope = app.Services.CreateScope();
    await scope.ServiceProvider.GetRequiredService<AppDbContext>()
        .Database.MigrateAsync();
}
// NEVER call MigrateAsync() in production on startup

# Zero-downtime pattern:
# 1. Migration: ADD Column NewStatus NVARCHAR(20) NULL
# 2. Deploy app that writes to both old and new columns
# 3. Backfill: UPDATE Orders SET NewStatus = Status WHERE NewStatus IS NULL
# 4. Migration: ALTER COLUMN NewStatus NOT NULL; drop old column""",
        "language": "csharp",
        "key_points": [
            "Idempotent scripts safe to re-run in CI/CD",
            "Never auto-migrate production on app startup",
            "Backward-compatible migrations for zero-downtime",
            "Never edit already-applied migration files",
        ],
    },
}
