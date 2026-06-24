"""Enhanced interview-prep content for frontend, database, and practices topics (part 2)."""

DETAILED_PART2: dict[str, dict] = {
    # ── Frontend ──────────────────────────────────────────────────────────────
    "js-closures": {
        "explanation": (
            "A **closure** is a function that retains access to variables from its **lexical scope** "
            "even after the outer function has finished executing. In JavaScript, inner functions "
            "carry a reference to the environment in which they were created, not just the values "
            "at call time. This is why `createCounter()` can return methods that still read and "
            "modify the private `count` variable long after `createCounter` returns. Closures power "
            "common patterns: **module patterns**, event handlers, debounce/throttle utilities, and "
            "Angular service factories. Interviewers often probe the **stale closure** trap in loops "
            "with `var` — use `let` or an IIFE to bind each iteration correctly. Closures also keep "
            "variables alive on the heap, so holding large objects in closures can cause **memory leaks** "
            "if references are never released."
        ),
        "code": """// Outer function creates a private scope
function createCounter(initial = 0) {
  let count = initial; // captured by the closure — not accessible from outside

  return {
    increment(step = 1) {
      count += step; // inner function closes over `count`
      return count;
    },
    getCount() {
      return count; // same lexical environment
    },
    reset() {
      count = initial;
    },
  };
}

const counter = createCounter(10);
counter.increment();   // 11
counter.getCount();    // 11 — `count` survived because closures kept it alive

// Stale-closure trap in loops (classic interview question)
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // prints 3, 3, 3 — one shared `i`
}

// Fix: block-scoped `let` creates a new binding per iteration
for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log(j), 100); // prints 0, 1, 2
}""",
        "language": "javascript",
        "key_points": [
            "Closures = function + reference to outer lexical environment",
            "Enable data privacy without classes (module pattern)",
            "Watch stale closures in async callbacks and React/Angular hooks",
            "Avoid capturing large objects unnecessarily — memory stays allocated",
        ],
    },
    "ts-interfaces": {
        "explanation": (
            "In TypeScript, **interfaces** and **type aliases** both describe shapes, but they differ "
            "in capabilities and intent. **Interfaces** are ideal for object contracts: they support "
            "**declaration merging** (two `interface User` blocks merge into one) and clean **`extends`** "
            "inheritance for class-like hierarchies. **Type aliases** are more flexible — they can "
            "express **unions**, **intersections**, mapped types, tuples, and primitive aliases that "
            "interfaces cannot. A common convention: use **interfaces for public API object shapes** "
            "(models, service contracts) and **types for unions, utility compositions, and conditional types**. "
            "Both disappear at compile time — they provide **static type safety** with zero runtime cost. "
            "In Angular, interfaces define DTOs and component `@Input` shapes; generics like `ApiResponse<T>` "
            "make reusable typed wrappers for HTTP calls."
        ),
        "code": """// Interface — extendable, mergeable object contract
interface User {
  id: number;
  name: string;
  email: string;
}

// Declaration merging: both blocks combine into one User interface
interface User {
  createdAt: Date;
}

interface Admin extends User {
  permissions: string[]; // inherits id, name, email, createdAt
}

// Type alias — unions and discriminated unions (great for result types)
type ApiResult<T> =
  | { success: true; data: T }
  | { success: false; error: string; statusCode: number };

function handleResult<T>(result: ApiResult<T>): T {
  if (!result.success) {
    throw new Error(`[${result.statusCode}] ${result.error}`);
  }
  return result.data; // TypeScript narrows to success branch
}

// Utility types — only possible with `type`, not `interface`
type PartialUser = Partial<User>;           // all props optional
type UserPreview = Pick<User, 'id' | 'name'>; // subset of fields
type ReadonlyUser = Readonly<User>;         // immutable view""",
        "language": "typescript",
        "key_points": [
            "Interfaces merge; types do not (but types support unions/intersections)",
            "Use interfaces for extensible object contracts and class implements",
            "Use types for unions, tuples, mapped/conditional types",
            "Strict mode + interfaces catch null/undefined bugs at compile time",
        ],
    },
    "angular-di": {
        "explanation": (
            "**Dependency Injection (DI)** in Angular is a built-in framework feature where the "
            "**injector** creates and wires dependencies instead of components calling `new` directly. "
            "Services decorated with `@Injectable` are registered via **`providedIn: 'root'`** "
            "(app-wide singleton), a **component's `providers` array** (instance per component subtree), "
            "or route-level providers. Angular maintains a **hierarchical injector tree** — child "
            "injectors can override parent registrations, enabling scoped behavior (e.g., a fresh "
            "service per lazy-loaded feature). Modern Angular supports **`inject()`** (functional DI) "
            "alongside constructor injection. DI improves **testability** (mock services easily), "
            "**separation of concerns**, and **tree-shaking** when using `providedIn: 'root'`. "
            "Interview tip: explain why `HttpClient` is injected rather than imported as a singleton."
        ),
        "code": """// Root-level singleton — tree-shakeable, one instance for the app
@Injectable({ providedIn: 'root' })
export class OrderService {
  constructor(private http: HttpClient) {}

  getOrders(): Observable<Order[]> {
    return this.http.get<Order[]>('/api/orders');
  }

  createOrder(order: CreateOrderDto): Observable<Order> {
    return this.http.post<Order>('/api/orders', order);
  }
}

// Component-scoped provider — new instance per component + its children
@Component({
  selector: 'app-order-wizard',
  providers: [OrderWizardStateService], // not shared with other components
  template: `<!-- wizard steps -->`,
})
export class OrderWizardComponent {
  // Modern functional DI (Angular 14+)
  private wizardState = inject(OrderWizardStateService);
  private orders = inject(OrderService); // root singleton still shared
}

// Route-level provider — scoped to a lazy-loaded feature
export const ORDER_ROUTES: Routes = [
  {
    path: '',
    providers: [OrderFacadeService], // lives for the lifetime of this route tree
    loadComponent: () => import('./order-list.component'),
  },
];""",
        "language": "typescript",
        "key_points": [
            "Injector hierarchy: root → route → component (child overrides parent)",
            "providedIn: 'root' = singleton + tree-shaking friendly",
            "inject() vs constructor DI — both resolve from the same injector",
            "Use DI for services, not for every utility function",
        ],
    },
    "rxjs-operators": {
        "explanation": (
            "**RxJS** models asynchronous data as **Observables** — streams that emit values over time. "
            "**Operators** are pure functions that transform one Observable into another without "
            "subscribing (lazy until subscribe). In Angular, `HttpClient` returns Observables, and "
            "operators compose the reactive logic for search boxes, pagination, and error handling. "
            "**`debounceTime` + `distinctUntilChanged`** prevent excessive API calls during typing. "
            "**`switchMap`** cancels the previous inner Observable when a new value arrives — ideal "
            "for search. **`mergeMap`** runs inner Observables concurrently; **`concatMap`** queues them. "
            "**`catchError`** recovers from failures without breaking the stream. Always manage "
            "subscriptions with **`takeUntil(destroy$)`**, the **`async` pipe**, or **`DestroyRef`** "
            "to prevent memory leaks."
        ),
        "code": """@Component({ /* ... */ })
export class OrderSearchComponent implements OnInit, OnDestroy {
  results: Order[] = [];
  private search$ = new Subject<string>();
  private destroy$ = new Subject<void>();

  constructor(private api: OrderApiService) {}

  ngOnInit() {
    this.search$.pipe(
      debounceTime(300),              // wait 300ms after last keystroke
      distinctUntilChanged(),         // skip if search term unchanged
      filter(term => term.length >= 2), // ignore very short queries
      switchMap(term =>               // cancel previous HTTP call on new term
        this.api.search(term).pipe(
          catchError(err => {
            console.error('Search failed', err);
            return of([] as Order[]); // recover with empty result — stream continues
          })
        )
      ),
      takeUntil(this.destroy$)        // auto-unsubscribe on destroy
    ).subscribe(orders => this.results = orders);
  }

  onSearch(term: string) {
    this.search$.next(term);
  }

  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }
}

// BehaviorSubject — Observable + current value (shared state pattern)
private cartCount$ = new BehaviorSubject<number>(0);
readonly count$ = this.cartCount$.asObservable();""",
        "language": "typescript",
        "key_points": [
            "switchMap cancels prior inner stream; mergeMap runs in parallel",
            "Operators are lazy — nothing runs until subscribe (or async pipe)",
            "Always unsubscribe or use async pipe / takeUntil",
            "BehaviorSubject for shared reactive state with a current value",
        ],
    },
    "reactive-forms": {
        "explanation": (
            "Angular offers **template-driven** and **reactive (model-driven)** forms. **Reactive forms** "
            "define the form model explicitly in the component class using **`FormGroup`**, **`FormControl`**, "
            "and **`FormArray`** — making them **synchronous**, **testable**, and ideal for complex "
            "validation logic. **Template-driven forms** rely on directives in the HTML (`ngModel`) and "
            "are simpler for basic inputs but harder to unit test and reason about at scale. Reactive forms "
            "support **built-in validators** (`Validators.required`, `Validators.email`), **custom validators**, "
            "and **cross-field validation** at the group level. **Angular 14+ typed forms** provide "
            "strongly typed `FormControl<T>` values. Prefer reactive forms when you need dynamic form "
            "arrays, conditional fields, or programmatic value changes — common in enterprise CRUD screens."
        ),
        "code": """@Component({
  selector: 'app-order-form',
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      <input formControlName="email" placeholder="Email" />
      <span *ngIf="form.controls.email.hasError('email')">Invalid email</span>

      <input formControlName="quantity" type="number" />
      <span *ngIf="form.controls.quantity.hasError('min')">Min quantity is 1</span>

      <button type="submit" [disabled]="form.invalid">Place Order</button>
    </form>
  `,
})
export class OrderFormComponent {
  private fb = inject(FormBuilder);

  // Define the entire form model in TypeScript — easy to test without DOM
  form = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    quantity: [1, [Validators.required, Validators.min(1), Validators.max(999)]],
    notes: [''], // optional field
  });

  onSubmit() {
    if (this.form.invalid) {
      this.form.markAllAsTouched(); // show validation errors
      return;
    }
    const value = this.form.getRawValue(); // includes disabled controls
    console.log('Submitting:', value);
  }

  // Programmatic updates — reactive forms shine here
  applyBulkDiscount() {
    this.form.patchValue({ quantity: 10 });
  }
}""",
        "language": "typescript",
        "key_points": [
            "Reactive = model in TS; template-driven = model in HTML",
            "FormBuilder, validators, and valueChanges for dynamic UX",
            "Typed forms (Angular 14+) give compile-time control value types",
            "Use FormArray for line items, repeating sections",
        ],
    },
    "change-detection": {
        "explanation": (
            "Angular's **change detection (CD)** checks whether component data changed and updates the DOM. "
            "The **default strategy** runs CD on the entire component tree after every browser event, "
            "HTTP response, timer, and Promise resolution — simple but can be expensive in large apps. "
            "**`ChangeDetectionStrategy.OnPush`** optimizes by checking a component only when its **`@Input` "
            "references change**, an event originates from the component or its children, or an Observable "
            "bound via the **`async` pipe** emits. OnPush requires **immutable data patterns** — replace "
            "arrays/objects instead of mutating them in place. **Angular Signals** (v16+) offer fine-grained "
            "reactivity that reduces unnecessary checks. In interviews, mention **`ChangeDetectorRef.markForCheck()`** "
            "when third-party libraries update state outside Angular's zone."
        ),
        "code": """// OnPush: only re-renders when @Input reference changes or events fire here
@Component({
  selector: 'app-order-row',
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <tr>
      <td>{{ order.id }}</td>
      <td>{{ order.customerName }}</td>
      <td>{{ order.total | currency }}</td>
      <td>{{ statusLabel }}</td>
    </tr>
  `,
})
export class OrderRowComponent {
  @Input({ required: true }) order!: Order;

  // Pure pipe or getter — recalculated only when CD runs for this component
  get statusLabel(): string {
    return this.order.status === 'Shipped' ? '✅ Shipped' : '⏳ Pending';
  }
}

@Component({ /* parent */ })
export class OrderListComponent {
  orders: Order[] = [];

  addOrder(newOrder: Order) {
    // Immutable update — new array reference triggers OnPush child re-check
    this.orders = [...this.orders, newOrder];

    // BAD for OnPush: this.orders.push(newOrder) — same reference, child won't update
  }
}

// Signals (Angular 16+) — granular updates without full tree checks
readonly orders = signal<Order[]>([]);
addViaSignal(order: Order) {
  this.orders.update(list => [...list, order]);
}""",
        "language": "typescript",
        "key_points": [
            "Default CD checks entire tree; OnPush checks only on triggers",
            "OnPush requires immutable @Input updates (new object/array reference)",
            "async pipe triggers CD when Observable emits — preferred pattern",
            "Signals simplify reactivity and reduce manual CD tuning",
        ],
    },
    "var-let-const": {
        "explanation": (
            "**`var`**, **`let`**, and **`const`** all declare variables but differ in scoping, hoisting, "
            "and mutability rules. **`var`** is **function-scoped** and **hoisted** with an initial value "
            "of `undefined` — which causes subtle bugs in loops and conditional blocks. **`let`** and "
            "**`const`** are **block-scoped** (confined to `{}`, loops, and `if` blocks) and sit in the "
            "**temporal dead zone** until their declaration line executes. **`const`** prevents **reassignment** "
            "of the binding but does **not** make object contents immutable — you can still push to a "
            "`const` array. Modern best practice: default to **`const`**, use **`let`** only when "
            "reassignment is needed, and **avoid `var`** entirely in new code. TypeScript/ESLint enforce "
            "this via `prefer-const` and `no-var` rules."
        ),
        "code": """function demonstrateScoping() {
  // var — hoisted to function scope; accessible throughout the function
  if (true) {
    var a = 1;
    let b = 2;     // block-scoped to this if-block
    const c = 3;   // block-scoped, cannot reassign c = 4
  }
  console.log(a); // 1 — var leaks out of the block
  // console.log(b); // ReferenceError — let is block-scoped
}

// Classic var loop bug
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log('var:', i), 50); // 3, 3, 3
}

// let creates a new binding per iteration
for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log('let:', j), 50); // 0, 1, 2
}

// const — binding is fixed, but object contents can change
const config = { theme: 'dark', lang: 'en' };
config.theme = 'light'; // OK — mutating property, not reassigning config
// config = {}           // TypeError — cannot reassign const binding

const ids: number[] = [];
ids.push(42); // OK — array contents are mutable""",
        "language": "javascript",
        "key_points": [
            "var = function-scoped + hoisted; let/const = block-scoped",
            "const prevents reassignment, not mutation of object contents",
            "Default to const; use let when rebinding; never var in modern code",
            "let in loops fixes the classic async closure bug",
        ],
    },
    "promises-async": {
        "explanation": (
            "A **Promise** represents a future value — either resolved or rejected — and enables "
            "chaining with `.then()` / `.catch()`. **`async/await`** is **syntactic sugar** over Promises, "
            "making asynchronous code read like synchronous code while preserving non-blocking behavior. "
            "Use **`try/catch`** around `await` for error handling instead of `.catch()` chains. "
            "**`Promise.all`** runs multiple Promises in parallel and fails fast on the first rejection. "
            "**`Promise.allSettled`** waits for all regardless of outcome. In Angular, **`HttpClient` returns "
            "Observables**, not Promises — but you can convert with **`firstValueFrom()`** or **`lastValueFrom()`** "
            "when interfacing with async/await code. Interviewers may ask about the **event loop**: "
            "`await` yields control, microtasks run before macrotasks."
        ),
        "code": """// async/await — clean sequential flow with try/catch error handling
async function fetchOrders(minTotal = 0): Promise<Order[]> {
  try {
    const response = await fetch(`/api/orders?minTotal=${minTotal}`);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const orders: Order[] = await response.json();
    return orders;
  } catch (error) {
    console.error('Failed to fetch orders:', error);
    return []; // graceful fallback
  }
}

// Parallel requests with Promise.all — faster than sequential await
async function loadDashboard(): Promise<DashboardData> {
  const [orders, customers, stats] = await Promise.all([
    fetchOrders(),
    fetch('/api/customers').then(r => r.json()),
    fetch('/api/stats').then(r => r.json()),
  ]);
  return { orders, customers, stats };
}

// Converting Angular Observable to Promise when needed
import { firstValueFrom } from 'rxjs';

async function getOrderFromApi(id: number): Promise<Order> {
  return firstValueFrom(inject(OrderService).getById(id));
}""",
        "language": "javascript",
        "key_points": [
            "async/await is Promise sugar — still non-blocking",
            "Promise.all for parallel; try/catch for await error handling",
            "Angular HttpClient returns Observable — use firstValueFrom to await",
            "Understand microtask queue: await resumes before setTimeout callbacks",
        ],
    },
    "angular-routing": {
        "explanation": (
            "The **Angular Router** maps URL paths to components, enabling SPA navigation without "
            "full page reloads. Routes are defined in a **`Routes`** array with **`path`**, **`component`** "
            "or **`loadChildren`/`loadComponent`**, and optional **guards**, **resolvers**, and **data**. "
            "**Lazy loading** splits feature modules into separate JavaScript bundles loaded on demand, "
            "dramatically reducing initial bundle size. **Route guards** (`canActivate`, `canDeactivate`, "
            "`canMatch`) protect routes — e.g., requiring authentication before accessing `/admin`. "
            "**`ActivatedRoute`** exposes route parameters, query strings, and resolved data to components. "
            "Use **`routerLink`** for declarative navigation and the **`Router` service** for programmatic "
            "redirects after form submission. Standalone components (Angular 14+) use **`loadComponent`** "
            "instead of NgModule-based lazy loading."
        ),
        "code": """// app.routes.ts — standalone routing with lazy loading and guards
export const APP_ROUTES: Routes = [
  { path: '', component: HomeComponent, title: 'Home' },

  // Lazy-loaded feature — separate bundle, loaded on first visit
  {
    path: 'orders',
    loadChildren: () =>
      import('./features/orders/orders.routes').then(m => m.ORDER_ROUTES),
    canActivate: [authGuard], // functional guard (Angular 15+)
  },

  // Route with parameter and resolver — data fetched before component renders
  {
    path: 'orders/:id',
    loadComponent: () =>
      import('./features/orders/order-detail.component').then(m => m.OrderDetailComponent),
    resolve: { order: orderResolver },
  },

  { path: '**', redirectTo: '' }, // wildcard — catch unknown URLs
];

// Reading route params in a component
@Component({ /* ... */ })
export class OrderDetailComponent {
  private route = inject(ActivatedRoute);
  orderId = this.route.snapshot.paramMap.get('id'); // snapshot for one-time read

  // Or reactive approach for param changes without destroying component
  order$ = this.route.paramMap.pipe(
    switchMap(params => this.orderService.getById(+params.get('id')!))
  );
}""",
        "language": "typescript",
        "key_points": [
            "Lazy loading reduces initial bundle — loadChildren / loadComponent",
            "Guards protect routes; resolvers prefetch data before activation",
            "ActivatedRoute for params; Router for programmatic navigate",
            "Standalone routes replace NgModule-based routing in modern Angular",
        ],
    },
    # ── Database ──────────────────────────────────────────────────────────────
    "sql-joins": {
        "explanation": (
            "SQL **JOINs** combine rows from two or more tables based on a related column, typically a "
            "**foreign key** relationship. An **INNER JOIN** returns only rows where a match exists in "
            "both tables — the intersection. A **LEFT (OUTER) JOIN** returns all rows from the left table "
            "plus matching rows from the right; unmatched right-side columns are **NULL**. **RIGHT JOIN** "
            "is the mirror of LEFT. **FULL OUTER JOIN** returns all rows from both sides, with NULLs where "
            "no match exists (not all databases support it — SQL Server does). **CROSS JOIN** produces a "
            "Cartesian product (every row paired with every row) — rarely used except for generating sequences. "
            "Always **index foreign key columns** on the joining side for performance. In interviews, draw "
            "a Venn diagram and explain which JOIN answers a given business question."
        ),
        "code": """-- INNER JOIN: customers who HAVE placed at least one order
SELECT c.Id, c.Name, o.OrderDate, o.Total
FROM Customers c
INNER JOIN Orders o ON o.CustomerId = c.Id
WHERE o.OrderDate >= '2025-01-01'
ORDER BY o.OrderDate DESC;

-- LEFT JOIN: ALL customers, including those with zero orders
SELECT c.Name, COUNT(o.Id) AS OrderCount, ISNULL(SUM(o.Total), 0) AS TotalSpent
FROM Customers c
LEFT JOIN Orders o ON o.CustomerId = c.Id
GROUP BY c.Id, c.Name
ORDER BY TotalSpent DESC;

-- Self-join: employees and their managers (same table, two aliases)
SELECT e.Name AS Employee, m.Name AS Manager
FROM Employees e
LEFT JOIN Employees m ON e.ManagerId = m.Id;

-- Anti-join pattern: customers with NO orders (LEFT JOIN + WHERE NULL)
SELECT c.Name
FROM Customers c
LEFT JOIN Orders o ON o.CustomerId = c.Id
WHERE o.Id IS NULL;""",
        "language": "sql",
        "key_points": [
            "INNER = matching rows only; LEFT = all left + optional right match",
            "Index foreign key columns used in ON clauses",
            "LEFT JOIN + WHERE NULL = anti-join (rows without matches)",
            "Avoid SELECT * in joins — project only needed columns",
        ],
    },
    "ef-core-basics": {
        "explanation": (
            "**Entity Framework Core (EF Core)** is Microsoft's lightweight **ORM** that maps C# classes "
            "to database tables, letting developers work with objects instead of raw SQL. **Code First** "
            "is the dominant approach: define entity classes and `DbContext`, generate **migrations**, "
            "and apply schema to the database. **Database First** scaffolds models from an existing database "
            "using `dotnet ef dbcontext scaffold`. **`DbContext`** represents a session with the database — "
            "track changes, run queries, and call **`SaveChangesAsync()`**. Configure relationships via "
            "**Data Annotations** (`[ForeignKey]`) or the **Fluent API** in `OnModelCreating` for complex "
            "scenarios. In ASP.NET Core, register `DbContext` as **Scoped** (one instance per HTTP request). "
            "EF Core translates LINQ to SQL, but understanding generated SQL is key for performance interviews."
        ),
        "code": """// Entity classes — Code First maps these to tables
public class Order
{
    public int Id { get; set; }
    public string CustomerName { get; set; } = "";
    public DateTime OrderDate { get; set; } = DateTime.UtcNow;
    public decimal Total { get; set; }

    // Navigation property — one-to-many relationship
    public List<OrderLine> Lines { get; set; } = [];
}

public class OrderLine
{
    public int Id { get; set; }
    public int OrderId { get; set; }       // FK column
    public string ProductName { get; set; } = "";
    public int Quantity { get; set; }
    public Order Order { get; set; } = null!; // navigation back to parent
}

// DbContext — gateway to the database
public class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options)
{
    public DbSet<Order> Orders => Set<Order>();
    public DbSet<OrderLine> OrderLines => Set<OrderLine>();

    protected override void OnModelCreating(ModelBuilder model)
    {
        // Fluent API — preferred for complex mappings
        model.Entity<Order>(entity =>
        {
            entity.HasKey(o => o.Id);
            entity.Property(o => o.CustomerName).HasMaxLength(200).IsRequired();
            entity.HasMany(o => o.Lines)
                  .WithOne(l => l.Order)
                  .HasForeignKey(l => l.OrderId)
                  .OnDelete(DeleteBehavior.Cascade); // delete lines when order deleted
        });
    }
}

// Program.cs registration — Scoped lifetime per HTTP request
// builder.Services.AddDbContext<AppDbContext>(options =>
//     options.UseSqlServer(builder.Configuration.GetConnectionString("Default")));""",
        "language": "csharp",
        "key_points": [
            "Code First: models → migrations → database schema",
            "DbContext is Scoped in web apps — one unit-of-work per request",
            "Fluent API in OnModelCreating for complex relationships",
            "DbSet<T> represents a table; LINQ queries translate to SQL",
        ],
    },
    "linq-queries": {
        "explanation": (
            "**LINQ (Language Integrated Query)** lets you query collections and databases using C# syntax. "
            "In EF Core, the critical distinction is **`IQueryable<T>`** vs **`IEnumerable<T>`**. "
            "**`IQueryable`** builds an **expression tree** executed on the **database server** — filters, "
            "projections, and sorting become SQL `WHERE`, `SELECT`, and `ORDER BY`. Calling **`ToListAsync()`** "
            "or **`AsEnumerable()`** too early **materializes** data into memory, forcing client-side "
            "filtering. Use **`.Select()`** to project only needed columns into DTOs, avoiding over-fetching. "
            "**`AsNoTracking()`** skips change tracking for read-only queries, reducing memory and CPU. "
            "Compose queries by chaining `Where`/`OrderBy` on `IQueryable` — EF Core generates a single "
            "optimized SQL statement. Always review generated SQL in development with **`LogTo()`** or "
            "Application Insights dependency tracking."
        ),
        "code": """public async Task<List<OrderSummaryDto>> GetHighValueOrdersAsync(
    decimal minTotal,
    CancellationToken ct = default)
{
    // GOOD — entire query runs on SQL Server as one statement
    return await _db.Orders
        .AsNoTracking()                              // read-only — no change tracking overhead
        .Where(o => o.Total >= minTotal)             // translated to SQL WHERE
        .OrderByDescending(o => o.OrderDate)         // SQL ORDER BY
        .Select(o => new OrderSummaryDto(            // SQL SELECT only needed columns
            o.Id,
            o.CustomerName,
            o.Total,
            o.Lines.Count))                           // COUNT subquery in SQL
        .Take(50)                                    // SQL TOP 50
        .ToListAsync(ct);                            // materialize here — not before
}

// BAD — loads ALL orders into memory, then filters in C#
var bad = (await _db.Orders.ToListAsync())
    .Where(o => o.Total >= minTotal)   // runs in app memory, not SQL
    .Take(50);

// Composable query — build filters conditionally
public IQueryable<Order> BuildOrderQuery(OrderFilter filter)
{
    var query = _db.Orders.AsNoTracking().AsQueryable();

    if (!string.IsNullOrEmpty(filter.CustomerName))
        query = query.Where(o => o.CustomerName.Contains(filter.CustomerName));

    if (filter.FromDate.HasValue)
        query = query.Where(o => o.OrderDate >= filter.FromDate);

    return query; // still IQueryable — no SQL executed yet
}""",
        "language": "csharp",
        "key_points": [
            "IQueryable = server-side SQL; IEnumerable = in-memory after materialization",
            "Never ToListAsync() before filtering — filter first, materialize last",
            "AsNoTracking for read-only; Select for DTO projection",
            "Enable SQL logging in Development to verify query translation",
        ],
    },
    "n-plus-one": {
        "explanation": (
            "The **N+1 query problem** occurs when code loads a collection of **N parent records** with "
            "one query, then executes **one additional query per parent** to load related child data — "
            "totaling **N + 1** database round trips. It often hides in lazy-loading scenarios: iterating "
            "orders and accessing `order.Lines` triggers a separate SELECT for each order. Symptoms include "
            "slow page loads and hundreds of identical SQL statements in logs. Fixes: **`.Include()` / "
            "`.ThenInclude()`** for eager loading, **explicit projection** with `.Select()` (single query, "
            "no tracking overhead), or **split queries** (`AsSplitQuery()`) when large joins cause cartesian "
            "explosion. Enable **`EnableSensitiveDataLogging`** or EF Core **`LogTo(Console.WriteLine)`** "
            "in development to catch N+1 early. Dapper or raw SQL with JOINs is the escape hatch for "
            "hand-tuned reads."
        ),
        "code": """// PROBLEM — 1 query for orders + N queries for each order's lines
var orders = await _db.Orders.ToListAsync(); // SELECT * FROM Orders
foreach (var order in orders)
{
    // Lazy load fires: SELECT * FROM OrderLines WHERE OrderId = @id  (× N times!)
    Console.WriteLine($"{order.Id}: {order.Lines.Count} lines");
}

// FIX 1 — Eager loading with Include (single JOIN query)
var ordersWithLines = await _db.Orders
    .Include(o => o.Lines)           // JOIN OrderLines in one query
    .AsNoTracking()
    .ToListAsync();

// FIX 2 — Projection (most efficient for read-only DTOs)
var orderDtos = await _db.Orders
    .Select(o => new OrderListDto
    {
        Id = o.Id,
        CustomerName = o.CustomerName,
        LineCount = o.Lines.Count,   // translated to SQL COUNT — no entity hydration
        Total = o.Total,
    })
    .ToListAsync();

// FIX 3 — Split query when Include causes cartesian explosion (many child rows)
var ordersSplit = await _db.Orders
    .Include(o => o.Lines)
    .AsSplitQuery()                  // 2 queries instead of 1 giant JOIN
    .AsNoTracking()
    .ToListAsync();""",
        "language": "csharp",
        "key_points": [
            "N+1 = 1 parent query + N child queries — common with lazy loading",
            "Include/ThenInclude for eager loading; Select for DTO projection",
            "AsSplitQuery prevents cartesian explosion with multiple collections",
            "Log SQL in Development — repetitive identical queries signal N+1",
        ],
    },
    "transactions": {
        "explanation": (
            "A **database transaction** groups multiple operations into a single **atomic unit** — either "
            "all changes **commit** together or all **roll back** on failure (ACID: Atomicity, Consistency, "
            "Isolation, Durability). In EF Core, each **`SaveChangesAsync()`** call is already wrapped in "
            "an implicit transaction. Use **`BeginTransactionAsync()`** when you need **multiple SaveChanges "
            "calls**, raw SQL, or cross-context operations in one atomic unit. Choose an **isolation level** "
            "based on concurrency needs: **Read Committed** (default, good balance), **Repeatable Read** "
            "(prevents non-repeatable reads), **Serializable** (strictest, slowest). For high-concurrency "
            "scenarios, prefer **optimistic concurrency** with a **`RowVersion`** / **`ConcurrencyToken`** "
            "column instead of long-held locks. Distributed transactions across databases are complex — "
            "prefer **Saga patterns** or **outbox pattern** in microservices."
        ),
        "code": """public async Task PlaceOrderAsync(PlaceOrderRequest request, CancellationToken ct)
{
    // Explicit transaction spanning multiple operations
    await using var transaction = await _db.Database.BeginTransactionAsync(ct);

    try
    {
        // Step 1 — insert order via EF Core
        var order = new Order { CustomerName = request.CustomerName, Total = request.Total };
        _db.Orders.Add(order);
        await _db.SaveChangesAsync(ct); // order.Id now generated

        // Step 2 — decrement inventory via raw SQL in the same transaction
        var rowsAffected = await _db.Database.ExecuteSqlAsync(
            $"UPDATE Inventory SET Quantity = Quantity - {request.Quantity} " +
            $"WHERE ProductId = {request.ProductId} AND Quantity >= {request.Quantity}",
            ct);

        if (rowsAffected == 0)
            throw new InvalidOperationException("Insufficient inventory");

        // Step 3 — insert audit log
        _db.AuditLogs.Add(new AuditLog
        {
            Action = "OrderPlaced",
            EntityId = order.Id.ToString(),
            Timestamp = DateTime.UtcNow,
        });
        await _db.SaveChangesAsync(ct);

        await transaction.CommitAsync(ct); // all or nothing
    }
    catch
    {
        await transaction.RollbackAsync(ct); // undo everything
        throw;
    }
}

// Optimistic concurrency — detect concurrent edits without locking
// public byte[] RowVersion { get; set; }  // [Timestamp] attribute on entity""",
        "language": "csharp",
        "key_points": [
            "SaveChangesAsync is already transactional for a single call",
            "BeginTransactionAsync for multi-step atomic operations",
            "RowVersion/ConcurrencyToken for optimistic concurrency control",
            "Avoid Serializable unless necessary — it hurts throughput",
        ],
    },
    "sql-groupby": {
        "explanation": (
            "**GROUP BY** collapses rows sharing the same values in specified columns into summary groups, "
            "typically combined with **aggregate functions** like `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`. "
            "The **`WHERE` clause** filters individual rows **before** grouping; **`HAVING`** filters "
            "**groups after** aggregation — e.g., `HAVING COUNT(*) > 5` keeps only departments with more "
            "than five employees. Every column in the `SELECT` list must either appear in the **`GROUP BY`** "
            "clause or be wrapped in an aggregate function — violating this causes a SQL error (or ambiguous "
            "results in non-standard databases). **GROUP BY** is essential for reporting queries: sales by "
            "region, orders per customer, daily revenue trends. For performance, ensure indexed columns "
            "appear in `WHERE` before grouping, and consider **filtered indexes** on commonly grouped columns."
        ),
        "code": """-- Aggregate orders by customer — count and total revenue
SELECT
    c.Id,
    c.Name,
    COUNT(o.Id)       AS OrderCount,
    SUM(o.Total)      AS TotalRevenue,
    AVG(o.Total)      AS AvgOrderValue,
    MAX(o.OrderDate)  AS LastOrderDate
FROM Customers c
LEFT JOIN Orders o ON o.CustomerId = c.Id
WHERE o.OrderDate >= '2025-01-01'   -- filter ROWS before grouping
GROUP BY c.Id, c.Name               -- every non-aggregated column must be here
HAVING COUNT(o.Id) >= 3             -- filter GROUPS after aggregation
ORDER BY TotalRevenue DESC;

-- Monthly sales report using DATE truncation
SELECT
    YEAR(OrderDate)  AS OrderYear,
    MONTH(OrderDate) AS OrderMonth,
    COUNT(*)         AS OrderCount,
    SUM(Total)       AS MonthlyRevenue
FROM Orders
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
ORDER BY OrderYear, OrderMonth;

-- ROLLUP — subtotals and grand total in one query
SELECT Department, JobTitle, COUNT(*) AS HeadCount
FROM Employees
GROUP BY ROLLUP(Department, JobTitle);""",
        "language": "sql",
        "key_points": [
            "WHERE filters rows before GROUP BY; HAVING filters groups after",
            "Every non-aggregated SELECT column must appear in GROUP BY",
            "Common aggregates: COUNT, SUM, AVG, MIN, MAX",
            "Index columns in WHERE clause; GROUP BY on large unindexed sets is slow",
        ],
    },
    "sql-indexes": {
        "explanation": (
            "A **database index** is a separate data structure (typically **B-tree**) that speeds up "
            "**SELECT**, **WHERE**, **JOIN**, and **ORDER BY** operations by avoiding full **table scans**. "
            "Think of it like a book index — direct lookup instead of reading every page. The trade-off: "
            "indexes **accelerate reads** but **slow down INSERT/UPDATE/DELETE** because the index must "
            "be maintained, and they consume **additional storage**. A **clustered index** determines "
            "physical row order (one per table — usually the primary key). **Nonclustered indexes** are "
            "separate structures pointing to row locations. A **covering index** includes all columns "
            "needed by a query (`INCLUDE` clause), allowing an **index-only scan** without touching the "
            "base table. Always index **foreign keys** and columns frequently used in WHERE/JOIN. Use "
            "**execution plans** to detect missing indexes and avoid over-indexing write-heavy tables."
        ),
        "code": """-- Nonclustered index on FK column — speeds up JOINs and WHERE CustomerId = ?
CREATE NONCLUSTERED INDEX IX_Orders_CustomerId
ON Orders (CustomerId);

-- Covering index — query reads only the index, not the table (index-only scan)
CREATE NONCLUSTERED INDEX IX_Orders_CustomerId_Covering
ON Orders (CustomerId)
INCLUDE (OrderDate, Total, Status);  -- extra columns stored in index leaf

-- Composite index — column order matters (leftmost prefix rule)
CREATE NONCLUSTERED INDEX IX_Orders_Date_Status
ON Orders (OrderDate DESC, Status)
WHERE Status <> 'Cancelled';         -- filtered index — smaller, targeted

-- Query that benefits from the covering index above:
SELECT OrderDate, Total, Status
FROM Orders
WHERE CustomerId = 42
ORDER BY OrderDate DESC;

-- Check for missing indexes (SQL Server DMVs — run in production with care)
-- SELECT * FROM sys.dm_db_missing_index_details;

-- Drop unused indexes after monitoring — they hurt write performance
-- DROP INDEX IX_Orders_OldUnused ON Orders;""",
        "language": "sql",
        "key_points": [
            "B-tree index speeds lookups; trade-off is slower writes + storage",
            "Clustered = physical order (PK); nonclustered = separate pointer structure",
            "Covering index (INCLUDE) enables index-only scans",
            "Always index foreign keys; verify with execution plans, not guesses",
        ],
    },
    "dapper": {
        "explanation": (
            "**Dapper** is a **micro-ORM** for .NET — a thin layer over ADO.NET that maps SQL query results "
            "to strongly typed objects with minimal overhead. Unlike EF Core, Dapper does **not** track entity "
            "state, generate migrations, or translate LINQ — you write **raw SQL** and control exactly what "
            "hits the database. This makes Dapper ideal for **read-heavy**, **performance-critical** queries, "
            "complex reports, bulk operations, and scenarios where EF Core generates suboptimal SQL. "
            "Performance is close to hand-rolled ADO.NET because Dapper simply sets properties via IL emit "
            "or reflection. Use **EF Core for CRUD**, migrations, and change tracking; use **Dapper for "
            "tuned reads and reporting**. Both can coexist in the same application — inject `IDbConnection` "
            "or `SqlConnection` alongside your `DbContext`. Parameterized queries prevent **SQL injection**."
        ),
        "code": """public class OrderReadRepository(IDbConnection connection)
{
    // Simple parameterized query — Dapper maps columns to OrderDto properties
    public async Task<IEnumerable<OrderDto>> GetHighValueOrdersAsync(
        decimal minTotal,
        int top = 50)
    {
        const string sql = @"
            SELECT TOP (@Top)
                o.Id,
                o.CustomerName,
                o.OrderDate,
                o.Total,
                COUNT(l.Id) AS LineCount
            FROM Orders o
            LEFT JOIN OrderLines l ON l.OrderId = o.Id
            WHERE o.Total >= @MinTotal
            GROUP BY o.Id, o.CustomerName, o.OrderDate, o.Total
            ORDER BY o.Total DESC";

        return await connection.QueryAsync<OrderDto>(sql, new
        {
            MinTotal = minTotal,
            Top = top,
        });
    }

    // Multi-mapping — split on Id to map Order + nested OrderLines
    public async Task<OrderWithLines?> GetOrderWithLinesAsync(int orderId)
    {
        const string sql = @"
            SELECT o.*, l.*
            FROM Orders o
            LEFT JOIN OrderLines l ON l.OrderId = o.Id
            WHERE o.Id = @OrderId";

        var lookup = new Dictionary<int, OrderWithLines>();

        await connection.QueryAsync<OrderWithLines, OrderLine, OrderWithLines>(
            sql,
            (order, line) =>
            {
                if (!lookup.TryGetValue(order.Id, out var existing))
                {
                    existing = order;
                    existing.Lines = [];
                    lookup[order.Id] = existing;
                }
                if (line is not null) existing.Lines.Add(line);
                return existing;
            },
            new { OrderId = orderId },
            splitOn: "Id" // second Id column starts OrderLine mapping
        );

        return lookup.Values.FirstOrDefault();
    }
}""",
        "language": "csharp",
        "key_points": [
            "Micro-ORM — raw SQL, manual mapping, near-ADO.NET performance",
            "No change tracking, migrations, or LINQ translation",
            "Best for read-heavy reports, complex joins, bulk operations",
            "Combine with EF Core: EF for writes/migrations, Dapper for tuned reads",
        ],
    },
    "ef-migrations": {
        "explanation": (
            "**EF Core migrations** version-control your database schema alongside application code, "
            "enabling repeatable, auditable schema changes across environments. The workflow: modify entity "
            "classes or Fluent API configuration → run **`dotnet ef migrations add MigrationName`** "
            "to generate a migration file with **`Up()`** and **`Down()`** methods → apply with "
            "**`dotnet ef database update`** (development) or **`dotnet ef migrations script`** "
            "(production — generate idempotent SQL for DBA review). Each migration is a C# class stored "
            "in the `Migrations/` folder and tracked in the **`__EFMigrationsHistory`** table. "
            "**Never edit applied migrations** in production — create a new migration instead. In CI/CD, "
            "run migrations as a deployment step or apply generated SQL scripts. For zero-downtime deploys, "
            "prefer **additive changes** (new nullable columns) before removing old columns in a later release."
        ),
        "code": """# ── CLI workflow ──
# 1. Create migration after model changes
dotnet ef migrations add AddOrderStatusColumn --project Infrastructure --startup-project Api

# 2. Apply to local/dev database
dotnet ef database update

# 3. Generate idempotent SQL script for production (DBA review)
dotnet ef migrations script --idempotent -o deploy.sql

# ── Generated migration class (simplified) ──
public partial class AddOrderStatusColumn : Migration
{
    protected override void Up(MigrationBuilder migrationBuilder)
    {
        // Add column with default so existing rows aren't broken
        migrationBuilder.AddColumn<string>(
            name: "Status",
            table: "Orders",
            type: "nvarchar(50)",
            maxLength: 50,
            nullable: false,
            defaultValue: "Pending");

        // Add index for common filter: WHERE Status = 'Pending'
        migrationBuilder.CreateIndex(
            name: "IX_Orders_Status",
            table: "Orders",
            column: "Status");
    }

    protected override void Down(MigrationBuilder migrationBuilder)
    {
        migrationBuilder.DropIndex(name: "IX_Orders_Status", table: "Orders");
        migrationBuilder.DropColumn(name: "Status", table: "Orders");
    }
}

// Program.cs — optional auto-migrate on startup (dev only, not recommended for prod)
// using (var scope = app.Services.CreateScope())
//     scope.ServiceProvider.GetRequiredService<AppDbContext>().Database.Migrate();""",
        "language": "csharp",
        "key_points": [
            "Model change → migrations add → database update / script",
            "Never modify applied migrations — create a new one instead",
            "Script with --idempotent for safe production deployment",
            "Prefer additive schema changes for zero-downtime releases",
        ],
    },
    # ── Best Practices ────────────────────────────────────────────────────────
    "solid": {
        "explanation": (
            "**SOLID** is five OOP design principles that promote maintainable, flexible code — a staple "
            "of L3+ interviews. **S — Single Responsibility**: a class should have one reason to change "
            "(validation separate from persistence). **O — Open/Closed**: open for extension, closed for "
            "modification — add new discount strategies without editing checkout code. **L — Liskov "
            "Substitution**: subclasses must honor the base class contract without breaking callers. "
            "**I — Interface Segregation**: prefer small, focused interfaces over fat ones that force "
            "empty implementations. **D — Dependency Inversion**: depend on abstractions (`IOrderRepository`), "
            "not concretions (`SqlOrderRepository`). In .NET, DI containers make **D** natural. Don't "
            "just recite definitions — tell a **refactoring story** where applying SOLID fixed a real pain point."
        ),
        "code": """// S — Single Responsibility: each class has one job
public class OrderValidator
{
    public ValidationResult Validate(Order order) =>
        order.Lines.Count == 0
            ? ValidationResult.Fail("Order must have at least one line")
            : ValidationResult.Success();
}

public class OrderRepository(AppDbContext db) : IOrderRepository
{
    public async Task SaveAsync(Order order, CancellationToken ct = default)
    {
        db.Orders.Add(order);
        await db.SaveChangesAsync(ct);
    }
}

// O + D — Open/Closed via Strategy pattern; depend on abstraction
public interface IDiscountStrategy
{
    decimal Apply(Order order);
}

public class TenPercentDiscount : IDiscountStrategy
{
    public decimal Apply(Order order) => order.Subtotal * 0.10m;
}

public class FreeShippingDiscount : IDiscountStrategy
{
    public decimal Apply(Order order) => order.ShippingCost;
}

// Adding a new discount = new class, zero changes to OrderCheckout
public class OrderCheckout(IDiscountStrategy discount)
{
    public decimal CalculateTotal(Order order) =>
        order.Subtotal - discount.Apply(order) + order.Tax;
}

// I — Interface Segregation: small focused interfaces
public interface IOrderReader { Task<Order?> GetAsync(int id); }
public interface IOrderWriter { Task SaveAsync(Order order); }
// Clients depend only on what they need — not a fat IOrderRepository with 20 methods

// L — Liskov: Square must not break Rectangle's setters (classic violation example)""",
        "language": "csharp",
        "key_points": [
            "S: one reason to change per class",
            "O: extend via new classes/strategies, not by editing existing code",
            "L: subclasses must be substitutable without breaking callers",
            "I: small interfaces; D: depend on abstractions via DI",
        ],
    },
    "unit-testing": {
        "explanation": (
            "**Unit testing** verifies individual units of code (classes, methods) in **isolation** from "
            "external dependencies like databases, HTTP APIs, and file systems. In .NET, **xUnit** is the "
            "most popular framework, paired with **Moq** (or NSubstitute) for creating test doubles. "
            "Follow the **Arrange-Act-Assert (AAA)** pattern: set up dependencies and input, execute the "
            "method under test, then verify the outcome and interactions. **Mock** external dependencies "
            "to control behavior and assert that collaborators were called correctly (`Verify`). Test "
            "**behavior and outcomes**, not implementation details like private method calls. Keep tests "
            "**fast**, **deterministic**, and **independent** — no shared mutable state between tests. "
            "For ASP.NET Core, use **`WebApplicationFactory<T>`** for integration tests that exercise "
            "the full HTTP pipeline with an in-memory test server."
        ),
        "code": """public class OrderServiceTests
{
    [Fact]
    public async Task PlaceOrderAsync_ValidOrder_SavesAndSendsConfirmationEmail()
    {
        // Arrange — mock dependencies, create system under test (SUT)
        var repoMock = new Mock<IOrderRepository>();
        var emailMock = new Mock<IEmailSender>();
        var validator = new OrderValidator();

        repoMock
            .Setup(r => r.SaveAsync(It.IsAny<Order>(), It.IsAny<CancellationToken>()))
            .Returns(Task.CompletedTask);

        var sut = new OrderService(repoMock.Object, emailMock.Object, validator);

        var order = new Order
        {
            CustomerEmail = "alice@example.com",
            Lines = [new OrderLine { ProductName = "Widget", Quantity = 2 }],
        };

        // Act — execute the method under test
        await sut.PlaceOrderAsync(order);

        // Assert — verify outcome AND interactions
        repoMock.Verify(
            r => r.SaveAsync(It.Is<Order>(o => o.CustomerEmail == "alice@example.com"),
            It.IsAny<CancellationToken>()),
            Times.Once);

        emailMock.Verify(
            e => e.SendAsync("alice@example.com", It.Is<string>(s => s.Contains("confirmed"))),
            Times.Once);
    }

    [Fact]
    public async Task PlaceOrderAsync_EmptyOrder_ThrowsValidationException()
    {
        var sut = new OrderService(
            Mock.Of<IOrderRepository>(),
            Mock.Of<IEmailSender>(),
            new OrderValidator());

        var emptyOrder = new Order { Lines = [] };

        await Assert.ThrowsAsync<ValidationException>(
            () => sut.PlaceOrderAsync(emptyOrder));
    }
}""",
        "language": "csharp",
        "key_points": [
            "AAA pattern: Arrange, Act, Assert",
            "Mock external deps; test behavior, not implementation details",
            "xUnit + Moq is the standard .NET combo",
            "WebApplicationFactory for integration tests; unit tests stay isolated",
        ],
    },
    "test-pyramid": {
        "explanation": (
            "The **test pyramid** is a model for balancing test types by quantity and cost. At the **base**, "
            "have many **fast, cheap unit tests** (milliseconds each) that verify business logic in isolation. "
            "In the **middle**, fewer **integration tests** (seconds each) verify that components work together "
            "— real database via Testcontainers, HTTP pipeline via WebApplicationFactory. At the **top**, "
            "a small number of **end-to-end (E2E) / UI tests** (minutes each) validate critical user journeys "
            "through the full stack including the browser. The pyramid shape reflects **cost vs confidence**: "
            "unit tests are fast and pinpoint failures; E2E tests are slow, flaky, and hard to maintain. "
            "A common ratio is **70% unit / 20% integration / 10% E2E**, adjusted per project. "
            "Anti-pattern: the **ice cream cone** (many UI tests, few unit tests) leads to slow CI and "
            "hard-to-diagnose failures."
        ),
        "code": """/*
                    Test Pyramid (ideal distribution)
                    ─────────────────────────────
                         ┌─────────┐
                         │  E2E/UI │  ~10% — Playwright, Cypress
                         │  tests  │  Minutes each, full browser stack
                        ─┴─────────┴─
                       ┌─────────────┐
                       │ Integration │  ~20% — WebApplicationFactory,
                       │   tests     │  Testcontainers SQL, API tests
                      ─┴─────────────┴──
                     ┌─────────────────┐
                     │   Unit tests    │  ~70% — xUnit + Moq
                     │  (base — many)  │  Milliseconds, isolated logic
                     └─────────────────┘

    Characteristics:
    ┌──────────────┬───────────┬──────────────┬──────────────────┐
    │  Layer       │  Speed    │  Isolation   │  What it catches │
    ├──────────────┼───────────┼──────────────┼──────────────────┤
    │  Unit        │  ms       │  Full        │  Logic bugs      │
    │  Integration │  seconds  │  Partial     │  Wiring, SQL, DI │
    │  E2E/UI      │  minutes  │  None        │  User flow bugs  │
    └──────────────┴───────────┴──────────────┴──────────────────┘
*/

// Unit test — fast, isolated (base of pyramid)
[Fact]
public void Discount_AppliesTenPercent_WhenSubtotalOver100()
{
    var discount = new TenPercentDiscount();
    var order = new Order { Subtotal = 150m };
    Assert.Equal(15m, discount.Apply(order));
}

// Integration test — middle layer (real DB, real HTTP pipeline)
// public class OrdersApiTests : IClassFixture<WebApplicationFactory<Program>> { ... }

// E2E test — top layer (browser automation, fewest tests)
// await page.GotoAsync("/orders"); await page.ClickAsync("#submit");""",
        "language": "text",
        "key_points": [
            "Many fast unit tests at base; few slow E2E tests at top",
            "Rough ratio: 70% unit / 20% integration / 10% E2E",
            "Ice cream cone anti-pattern: too many UI tests, too few unit tests",
            "CI must run all layers on every PR — fast feedback loop",
        ],
    },
    "microservices": {
        "explanation": (
            "**Microservices** decompose an application into **independently deployable services**, each "
            "owning a bounded business capability (Orders, Payments, Notifications). Benefits: **independent "
            "scaling**, **technology diversity**, **team autonomy**, and **fault isolation**. Costs: "
            "**distributed complexity** — network latency, partial failures, data consistency across services, "
            "and operational overhead (monitoring, deployment, service discovery). **Start with a well-structured "
            "monolith** and split only when team size, scale, or deployment independence demands it — "
            "premature microservices are a common anti-pattern. Use **Domain-Driven Design (DDD) bounded "
            "contexts** to define service boundaries. Communication patterns: **synchronous REST/gRPC** "
            "for queries, **asynchronous messaging** (Azure Service Bus, RabbitMQ) for events. "
            "**Observability is mandatory**: correlation IDs, distributed tracing (Application Insights), "
            "and centralized logging across all services."
        ),
        "code": """/*
  Monolith (modular)                 Microservices
  ┌─────────────────────┐           ┌────────┐ ┌────────┐ ┌──────────┐
  │  Orders │ Payments  │           │ Orders │ │Payments│ │ Notify   │
  │  Users  │ Inventory │           │  Svc   │ │  Svc   │ │  Svc     │
  └──────────┬──────────┘           └───┬────┘ └───┬────┘ └────┬─────┘
             │                          │          │           │
        Single Database            ┌─────┴──────────┴───────────┴─────┐
                                   │       API Gateway / Service Bus   │
                                   └───────────────────────────────────┘
                                   Each service owns its own database
*/

// Event-driven communication — Orders service publishes, Notify service subscribes
public record OrderPlacedEvent(int OrderId, string CustomerEmail, decimal Total);

public class OrderService(IOrderRepository repo, IEventPublisher publisher)
{
    public async Task PlaceOrderAsync(Order order)
    {
        await repo.SaveAsync(order);

        // Fire-and-forget event — Notify service handles email independently
        await publisher.PublishAsync(new OrderPlacedEvent(
            order.Id, order.CustomerEmail, order.Total));
    }
}

// API Gateway routes external requests to internal services
// GET /api/orders/42  →  Orders Service
// POST /api/payments  →  Payments Service
// Correlation ID propagated via HTTP header: X-Correlation-Id""",
        "language": "text",
        "key_points": [
            "Independent deploy, scale, and tech stack per service",
            "Start monolith; split on bounded contexts when justified",
            "Sync REST/gRPC for queries; async messaging for events",
            "Mandatory: correlation IDs, distributed tracing, health checks",
        ],
    },
    "design-patterns": {
        "explanation": (
            "**Design patterns** are proven solutions to recurring software design problems. In .NET "
            "interviews, focus on patterns you can tie to **real code**, not textbook definitions. "
            "**Strategy** — swap algorithms at runtime (shipping calculators, discount rules). "
            "**Repository** — abstract data access behind an interface, enabling testability and "
            "swappable persistence. **Factory / Abstract Factory** — centralize object creation "
            "(`IHttpClientFactory` in ASP.NET Core). **Decorator** — add behavior dynamically "
            "(logging, caching wrappers around a service). **Observer** — react to state changes "
            "(events, RxJS Observables, `IObservable<T>`). **Singleton** — one instance (prefer DI "
            "container registration over manual Singleton). Know **when NOT to use a pattern** — "
            "over-engineering with patterns for simple CRUD is a red flag in interviews."
        ),
        "code": """// Strategy — swap shipping calculation without modifying checkout
public interface IShippingCalculator
{
    decimal Calculate(Order order);
}

public class StandardShipping : IShippingCalculator
{
    public decimal Calculate(Order order) => order.Total > 100 ? 0 : 9.99m;
}

public class ExpressShipping : IShippingCalculator
{
    public decimal Calculate(Order order) => 19.99m;
}

public class CheckoutService(IShippingCalculator shipping)
{
    public decimal GetGrandTotal(Order order) =>
        order.Subtotal + order.Tax + shipping.Calculate(order);
}

// Repository — abstract data access (testable, swappable)
public interface IOrderRepository
{
    Task<Order?> GetByIdAsync(int id, CancellationToken ct = default);
    Task<IReadOnlyList<Order>> GetByCustomerAsync(string email, CancellationToken ct = default);
    Task SaveAsync(Order order, CancellationToken ct = default);
}

// Decorator — add cross-cutting concern without modifying original service
public class LoggingOrderService(IOrderService inner, ILogger<LoggingOrderService> logger)
    : IOrderService
{
    public async Task PlaceOrderAsync(Order order)
    {
        logger.LogInformation("Placing order for {Email}", order.CustomerEmail);
        await inner.PlaceOrderAsync(order);
        logger.LogInformation("Order {Id} placed successfully", order.Id);
    }
}

// Factory — IHttpClientFactory in ASP.NET Core is a built-in Factory pattern
// builder.Services.AddHttpClient<IExternalApiClient, ExternalApiClient>();""",
        "language": "csharp",
        "key_points": [
            "Strategy: interchangeable algorithms (discounts, shipping, payment)",
            "Repository: abstract data access for testability",
            "Decorator: wrap services for logging, caching, retry",
            "Prefer DI over manual Singleton; don't over-apply patterns",
        ],
    },
    "clean-code": {
        "explanation": (
            "**Clean Code** (popularized by Robert C. Martin) emphasizes writing code that humans can "
            "read and maintain easily. Core practices: **meaningful names** that reveal intent "
            "(`CalculateOrderTotal` not `Calc`), **small functions** that do one thing, **minimal "
            "nesting** (guard clauses over deep if/else pyramids), and **comments only where code "
            "cannot express intent** (why, not what). Follow **KISS** (Keep It Simple) and **DRY** "
            "(Don't Repeat Yourself) — but don't abstract prematurely. The **Boy Scout Rule**: leave "
            "code cleaner than you found it. In code reviews, enforce consistent formatting, reject "
            "magic numbers, and flag methods longer than ~20 lines. Clean code reduces onboarding time, "
            "bug density, and the cost of change — interviewers want to hear how you've refactored "
            "a messy module into something readable."
        ),
        "code": """// BAD — cryptic names, deep nesting, magic numbers, no error context
public void P(Order? o)
{
    if (o != null)
    {
        if (o.Lines.Count > 0)
        {
            if (o.Total > 100)
            {
                o.Total = o.Total * 0.9m; // what is 0.9?
            }
        }
    }
}

// GOOD — descriptive names, guard clauses, constants, clear flow
public const decimal BulkDiscountThreshold = 100m;
public const decimal BulkDiscountRate = 0.10m;

public async Task ProcessOrderAsync(Order order, CancellationToken ct = default)
{
    ArgumentNullException.ThrowIfNull(order);

    if (order.Lines.Count == 0)
        throw new ValidationException("An order must contain at least one line item.");

    ApplyBulkDiscountIfEligible(order);

    await _validator.ValidateAsync(order, ct);
    await _repository.SaveAsync(order, ct);
    await _notifier.SendConfirmationAsync(order, ct);
}

private static void ApplyBulkDiscountIfEligible(Order order)
{
    if (order.Subtotal < BulkDiscountThreshold)
        return; // guard clause — flat structure, no nesting

    var discount = order.Subtotal * BulkDiscountRate;
    order.ApplyDiscount(discount);
}""",
        "language": "csharp",
        "key_points": [
            "Meaningful names, small functions, guard clauses over nesting",
            "KISS and DRY — but avoid premature abstraction",
            "Boy Scout Rule: leave code cleaner than you found it",
            "Comments explain WHY; code itself should explain WHAT",
        ],
    },
    "bdd-tdd": {
        "explanation": (
            "**TDD (Test-Driven Development)** follows the **Red-Green-Refactor** cycle: write a **failing "
            "test** first (Red), write the **minimum code** to pass (Green), then **refactor** while keeping "
            "tests green. TDD drives **better design** by forcing you to think about the API before "
            "implementation and produces a safety net for refactoring. **BDD (Behavior-Driven Development)** "
            "extends TDD by expressing tests in **business-readable language** using **Given/When/Then** "
            "scenarios — often with tools like **SpecFlow** (.NET), Cucumber (Java), or Gherkin syntax. "
            "BDD bridges developers, QA, and product owners with a shared vocabulary. Key difference: "
            "TDD focuses on **developer-facing unit tests**; BDD focuses on **behavior specifications** "
            "that non-technical stakeholders can review. Neither requires 100% coverage — aim for "
            "**meaningful coverage** of business-critical paths and edge cases."
        ),
        "code": """// ── TDD: Red → Green → Refactor ──

// RED — write failing test first (no implementation yet)
[Fact]
public void ApplyTenPercentDiscount_SubtotalOver100_ReturnsTenPercentOff()
{
    var order = new Order { Subtotal = 150m };
    var discount = new TenPercentDiscount();

    var result = discount.Apply(order);

    Assert.Equal(15m, result); // FAILS — TenPercentDiscount doesn't exist yet
}

// GREEN — minimal implementation to pass
public class TenPercentDiscount : IDiscountStrategy
{
    private const decimal Threshold = 100m;
    private const decimal Rate = 0.10m;

    public decimal Apply(Order order) =>
        order.Subtotal >= Threshold ? order.Subtotal * Rate : 0m;
}

// REFACTOR — improve design while tests stay green (extract constants, add interface)

// ── BDD: SpecFlow Gherkin feature file ──
/*
Feature: Order Discount
  As a customer
  I want automatic discounts on large orders
  So that I save money on bulk purchases

  Scenario: 10% discount applied when subtotal exceeds $100
    Given an order with subtotal of $150
    When a 10% discount is applied
    Then the discount amount should be $15
    And the order total should be $135 plus tax
*/

// SpecFlow step definitions bind Gherkin to C# code
[Binding]
public class DiscountSteps
{
    private Order _order = null!;
    private decimal _discountAmount;

    [Given(@"an order with subtotal of \\$(.*)")]
    public void GivenSubtotal(decimal subtotal) =>
        _order = new Order { Subtotal = subtotal };

    [When(@"a 10% discount is applied")]
    public void WhenDiscountApplied() =>
        _discountAmount = new TenPercentDiscount().Apply(_order);

    [Then(@"the discount amount should be \\$(.*)")]
    public void ThenDiscountAmount(decimal expected) =>
        Assert.Equal(expected, _discountAmount);
}""",
        "language": "csharp",
        "key_points": [
            "TDD: Red-Green-Refactor — test first, then minimal code",
            "BDD: Given/When/Then scenarios in business language (SpecFlow)",
            "TDD = developer-focused; BDD = stakeholder-readable specifications",
            "Aim for meaningful coverage, not 100% — focus on critical paths",
        ],
    },
}
