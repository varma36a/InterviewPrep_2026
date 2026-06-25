"""Angular interview questions — exact phrasing for common L1–L5 screen questions."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("frontend", "foundation"): [
        InterviewItem(
            "angular-iq-lifecycle-hooks",
            "Life cycle hooks usages (ngOnInit, ngOnChanges, ngAfterViewInit)?",
            "Angular lifecycle hooks run at specific phases of a component's life.",
            "",
        ),
        InterviewItem(
            "angular-iq-component",
            "What do you understand by Angular component?",
            "A component is the basic UI building block — class + template + metadata.",
            "",
        ),
        InterviewItem(
            "angular-iq-component-decorator",
            "What is @Component decorator and what do we config there?",
            "@Component metadata defines selector, template, styles, and change detection.",
            "",
        ),
        InterviewItem(
            "angular-iq-parent-child-data",
            "How to handle data transfer between parent and child components?",
            "Parent → child via @Input; child → parent via @Output EventEmitter or signals.",
            "",
        ),
        InterviewItem(
            "angular-iq-async-pipe",
            "Usage of async pipe?",
            "Subscribes to Observables/Promises in the template and triggers change detection.",
            "",
        ),
        InterviewItem(
            "angular-iq-trackby-ngfor",
            "trackBy for ngFor?",
            "Stable identity function so Angular reuses DOM nodes when list data changes.",
            "",
        ),
        InterviewItem(
            "angular-iq-structural-directives",
            "What are all structural directives?",
            "Directives that change DOM layout — *ngIf, *ngFor, *ngSwitch (modern: @if, @for, @switch).",
            "",
        ),
    ],
    ("frontend", "intermediate"): [
        InterviewItem(
            "angular-iq-angular-service",
            "What is Angular service and its usage?",
            "Singleton injectable class for shared logic, HTTP, and state.",
            "",
        ),
        InterviewItem(
            "angular-iq-onpush",
            "What is OnPush change detection strategy?",
            "Checks component only when @Input ref changes, events fire, or async pipe emits.",
            "",
        ),
        InterviewItem(
            "angular-iq-route-data",
            "How to pass static and dynamic data to routed component?",
            "route data/config, params, queryParams, and router state.",
            "",
        ),
        InterviewItem(
            "angular-iq-resolve-guard",
            "What is resolve guard?",
            "Pre-fetch route data before navigation completes (ResolveFn / resolver).",
            "",
        ),
        InterviewItem(
            "angular-iq-content-projection",
            "What is content projection?",
            "Pass markup from parent into child slots via ng-content.",
            "",
        ),
        InterviewItem(
            "angular-iq-viewchild",
            "What is ViewChild?",
            "Query a child component or DOM element from the component's own template.",
            "",
        ),
        InterviewItem(
            "angular-iq-pure-impure-pipes",
            "Difference between impure and pure pipes?",
            "Pure pipes run only when input reference changes; impure run every change detection.",
            "",
        ),
        InterviewItem(
            "angular-iq-switchmap",
            "What is switchMap?",
            "RxJS operator that switches to a new inner Observable and cancels the previous one.",
            "",
        ),
        InterviewItem(
            "angular-iq-forkjoin-combinelatest",
            "forkJoin vs combineLatest?",
            "forkJoin waits for all to complete; combineLatest emits when any source emits.",
            "",
        ),
        InterviewItem(
            "angular-iq-take-tap",
            "What is take() and tap() operator?",
            "take(n) completes after n emissions; tap() performs side effects without changing stream.",
            "",
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "angular-iq-lifecycle-hooks": {
        "explanation": (
            "Angular runs **lifecycle hooks** at well-defined points so you can initialize data, react to "
            "input changes, access the DOM, and clean up resources.\n\n"
            "**`ngOnChanges`** — called when **@Input** properties change (first call before `ngOnInit`). "
            "Receives `SimpleChanges` with previous/current values. Use when child must react to parent input updates.\n\n"
            "**`ngOnInit`** — runs **once** after the first input binding. Use for **initialization**: load data, "
            "subscribe to streams, read route params. Prefer over constructor (no DOM, DI is ready).\n\n"
            "**`ngAfterViewInit`** — runs once after the component **view** (and child views) are created. "
            "**ViewChild** references are available here. Use to focus inputs, init chart libraries, or measure DOM.\n\n"
            "Also know: **`ngOnDestroy`** (unsubscribe, clear timers), **`ngAfterContentInit`** (projected content ready)."
        ),
        "code": """@Component({
  selector: 'app-order-detail',
  template: `<h2>{{ order?.id }}</h2><canvas #chart></canvas>`,
})
export class OrderDetailComponent implements OnChanges, OnInit, AfterViewInit, OnDestroy {
  @Input() orderId!: number;
  @ViewChild('chart') chartRef!: ElementRef<HTMLCanvasElement>;

  private destroy$ = new Subject<void>();

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['orderId'] && !changes['orderId'].firstChange) {
      this.loadOrder(this.orderId); // parent changed input
    }
  }

  ngOnInit(): void {
    this.loadOrder(this.orderId); // one-time setup
    this.orderService.updates$.pipe(takeUntil(this.destroy$)).subscribe(/* ... */);
  }

  ngAfterViewInit(): void {
    this.initChart(this.chartRef.nativeElement); // DOM / ViewChild ready
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}""",
        "language": "typescript",
        "key_points": [
            "ngOnInit for setup — not constructor",
            "ngOnChanges when @Input values change",
            "ngAfterViewInit when ViewChild/DOM is ready",
            "Always clean up subscriptions in ngOnDestroy",
        ],
    },
    "angular-iq-component": {
        "explanation": (
            "An **Angular component** is the fundamental building block of the UI. It combines:\n\n"
            "1. **TypeScript class** — state, logic, event handlers\n"
            "2. **HTML template** — what to render\n"
            "3. **CSS/SCSS styles** — scoped (usually) to the component\n"
            "4. **Metadata** via `@Component` — selector, change detection, providers\n\n"
            "Components are **declared in a module** (legacy) or **standalone** (modern). The Angular compiler "
            "turns templates into efficient rendering instructions. Components form a **tree** — parent/child "
            "relationships with data flowing down via `@Input` and up via `@Output`.\n\n"
            "**Interview tip:** contrast with **directives** (no template of their own) and **services** (no view)."
        ),
        "code": """@Component({
  selector: 'app-order-card',
  standalone: true,
  imports: [CommonModule, CurrencyPipe],
  template: `
    <article class="card" (click)="selected.emit(order)">
      <h3>{{ order.title }}</h3>
      <p>{{ order.total | currency }}</p>
    </article>
  `,
  styleUrl: './order-card.component.scss',
})
export class OrderCardComponent {
  @Input({ required: true }) order!: Order;
  @Output() selected = new EventEmitter<Order>();
}""",
        "language": "typescript",
        "key_points": [
            "Class + template + styles + @Component metadata",
            "Selector used as custom HTML tag in templates",
            "Standalone components are the modern default",
            "Component tree mirrors UI hierarchy",
        ],
    },
    "angular-iq-component-decorator": {
        "explanation": (
            "The **`@Component` decorator** attaches metadata Angular needs to create, compile, and render a component.\n\n"
            "Common configuration:\n"
            "- **`selector`** — CSS selector (`app-orders`, `[appHighlight]`, `.widget`)\n"
            "- **`template` / `templateUrl`** — inline HTML or external file\n"
            "- **`styles` / `styleUrl(s)`** — component-scoped CSS\n"
            "- **`standalone: true`** — no NgModule required (modern apps)\n"
            "- **`imports`** — other standalone components, pipes, directives\n"
            "- **`providers`** — component-level DI scope\n"
            "- **`changeDetection`** — `Default` vs `OnPush`\n"
            "- **`encapsulation`** — `Emulated` (default), `ShadowDom`, `None`\n"
            "- **`host`** — bind attributes/classes on the host element"
        ),
        "code": """@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [RouterOutlet, OrderListComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
  encapsulation: ViewEncapsulation.Emulated,
  providers: [DashboardFacade], // instance per component subtree
  host: {
    class: 'dashboard-host',
    '(window:resize)': 'onResize()',
  },
})
export class DashboardComponent {}""",
        "language": "typescript",
        "key_points": [
            "selector defines how component is used in HTML",
            "templateUrl + styleUrl for larger components",
            "imports replaces NgModule for standalone",
            "changeDetection and providers are common interview configs",
        ],
    },
    "angular-iq-parent-child-data": {
        "explanation": (
            "**Parent → Child:** pass data with **`@Input()`** (or `input()` signal in Angular 17.1+). "
            "Parent binds: `<app-child [user]=\"currentUser\" />`.\n\n"
            "**Child → Parent:** emit events with **`@Output() EventEmitter`** (or `output()` signal). "
            "Child calls `this.saved.emit(data)`; parent listens `(saved)=\"onSaved($event)\"`.\n\n"
            "**Sibling components:** share a **service** (Subject/BehaviorSubject/signal store) — no direct binding.\n\n"
            "**Two-way binding:** `[(ngModel)]` or **`model()`** signal with two-way binding syntax.\n\n"
            "Avoid `@ViewChild` for primary data flow — it's imperative and couples components."
        ),
        "code": """// child.component.ts
@Component({ selector: 'app-order-form', /* ... */ })
export class OrderFormComponent {
  @Input({ required: true }) order!: Order;
  @Output() save = new EventEmitter<Order>();

  submit(): void {
    this.save.emit({ ...this.order, updatedAt: new Date() });
  }
}

// parent.component.html
<app-order-form [order]="selected" (save)="onSave($event)" />

// Modern signals API
export class OrderFormComponent {
  order = input.required<Order>();
  save = output<Order>();
}""",
        "language": "typescript",
        "key_points": [
            "@Input down, @Output up — unidirectional data flow",
            "EventEmitter for child → parent communication",
            "Shared service for sibling/global state",
            "Prefer signals input()/output() in new code",
        ],
    },
    "angular-iq-async-pipe": {
        "explanation": (
            "The **`async` pipe** subscribes to an **Observable** or **Promise** in the template and "
            "returns the latest value. It **automatically unsubscribes** when the component is destroyed — "
            "preventing memory leaks.\n\n"
            "Benefits:\n"
            "- No manual `subscribe()` in the component class\n"
            "- Triggers **change detection** when new values arrive (critical with **OnPush**)\n"
            "- Keeps templates declarative: `orders$ | async`\n\n"
            "Use with `*ngIf` / `@if` and nullish coalescing: `@if (user$ | async; as user) { ... }`"
        ),
        "code": """@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    @if (orders$ | async; as orders) {
      <ul>
        @for (o of orders; track o.id) {
          <li>{{ o.id }} — {{ o.total | currency }}</li>
        }
      </ul>
    } @else {
      <p>Loading...</p>
    }
  `,
})
export class OrdersComponent {
  orders$ = inject(OrderService).getOrders(); // Observable<Order[]>
}""",
        "language": "typescript",
        "key_points": [
            "Auto-subscribe and auto-unsubscribe in template",
            "Essential with OnPush change detection",
            "Use with @if ... as alias for null-safe access",
            "Avoid manual subscribe when async pipe suffices",
        ],
    },
    "angular-iq-trackby-ngfor": {
        "explanation": (
            "When Angular renders a list, it needs to know **which items changed**. Without **trackBy**, "
            "replacing the array causes Angular to **destroy and recreate all DOM nodes** — slow and loses "
            "focus/animation state.\n\n"
            "**trackBy** (legacy `*ngFor`) or **`track` expression** (modern `@for`) provides a **stable identity** "
            "(usually `item.id`) so Angular **reuses** existing DOM nodes.\n\n"
            "Always use for dynamic lists: tables, search results, infinite scroll."
        ),
        "code": """// Modern @for (Angular 17+)
@for (order of orders; track order.id) {
  <app-order-row [order]="order" />
} @empty {
  <p>No orders found.</p>
}

// Legacy *ngFor + trackBy
<ul>
  <li *ngFor="let item of items; trackBy: trackById">{{ item.name }}</li>
</ul>

trackById(_index: number, item: Item): number {
  return item.id; // stable key — only re-render changed rows
}""",
        "language": "typescript",
        "key_points": [
            "track / trackBy gives each row a stable identity",
            "Prevents full list DOM teardown on array replace",
            "Use business id — not array index (unless static list)",
            "Critical for performance in large tables",
        ],
    },
    "angular-iq-structural-directives": {
        "explanation": (
            "**Structural directives** change the **DOM layout** by adding/removing elements (they use `<ng-template>` "
            "under the hood).\n\n"
            "**Classic structural directives:**\n"
            "- **`*ngIf`** — conditionally include/exclude a template\n"
            "- **`*ngFor`** — repeat a template for each item\n"
            "- **`*ngSwitch` / `*ngSwitchCase` / `*ngSwitchDefault`** — switch/case rendering\n\n"
            "**Modern built-in control flow (Angular 17+):** `@if`, `@for`, `@switch` — preferred in new code; "
            "better type checking and `@empty` block for lists.\n\n"
            "Contrast with **attribute directives** (`ngClass`, `ngStyle`, custom) — they change appearance/behavior "
            "without adding/removing the element."
        ),
        "code": """<!-- Modern control flow -->
@if (isLoggedIn) {
  <app-dashboard />
} @else {
  <app-login />
}

@for (user of users; track user.id) {
  <app-user-card [user]="user" />
} @empty {
  <p>No users.</p>
}

@switch (role) {
  @case ('admin') { <app-admin-panel /> }
  @case ('user') { <app-user-home /> }
  @default { <app-guest /> }
}""",
        "language": "html",
        "key_points": [
            "Structural = add/remove DOM (*ngIf, *ngFor, *ngSwitch)",
            "Modern @if/@for/@switch replace legacy directives",
            "Attribute directives change behavior, not layout",
            "@empty handles zero-item lists in @for",
        ],
    },
    "angular-iq-angular-service": {
        "explanation": (
            "An **Angular service** is an injectable class (`@Injectable`) that holds **shared logic** outside "
            "any single component — HTTP calls, caching, auth, logging, state management.\n\n"
            "**Usage:**\n"
            "- Register with **`providedIn: 'root'`** for app-wide singleton\n"
            "- Inject via **constructor** or **`inject()`** function\n"
            "- Component-level **`providers`** for scoped instances\n\n"
            "Services keep components thin and testable — mock services in unit tests."
        ),
        "code": """@Injectable({ providedIn: 'root' })
export class OrderService {
  private http = inject(HttpClient);
  private cache = new Map<number, Order>();

  getOrders(): Observable<Order[]> {
    return this.http.get<Order[]>('/api/orders');
  }

  getById(id: number): Observable<Order> {
    if (this.cache.has(id)) {
      return of(this.cache.get(id)!);
    }
    return this.http.get<Order>(`/api/orders/${id}`).pipe(
      tap(order => this.cache.set(id, order)),
    );
  }
}

@Component({ /* ... */ })
export class OrdersComponent {
  private orders = inject(OrderService);
  orders$ = this.orders.getOrders();
}""",
        "language": "typescript",
        "key_points": [
            "@Injectable + providedIn: 'root' = singleton",
            "inject() or constructor DI to use in components",
            "Services for HTTP, auth, shared state, utilities",
            "Mock services in unit tests with TestBed",
        ],
    },
    "angular-iq-onpush": {
        "explanation": (
            "**`ChangeDetectionStrategy.OnPush`** tells Angular to check a component **only when**:\n"
            "1. An **@Input reference** changes (not deep mutation)\n"
            "2. An **event** originates from the component or its children\n"
            "3. An **async pipe** bound Observable emits\n"
            "4. Explicit **`markForCheck()`** or signal updates (Angular 16+)\n\n"
            "Default strategy checks the **entire subtree** on every browser event — expensive in large apps. "
            "OnPush + **immutable updates** (`this.items = [...items, newItem]`) is the main performance pattern."
        ),
        "code": """@Component({
  selector: 'app-order-row',
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `<span>{{ order.id }} — {{ order.total | currency }}</span>`,
})
export class OrderRowComponent {
  @Input({ required: true }) order!: Order;
}

// Parent — immutable update triggers OnPush child
addOrder(order: Order): void {
  this.orders = [...this.orders, order]; // new array reference ✓
  // BAD: this.orders.push(order) — same ref, OnPush child won't update
}""",
        "language": "typescript",
        "key_points": [
            "OnPush skips checks until input ref change or events",
            "Never mutate @Input objects in place",
            "async pipe and signals trigger OnPush updates",
            "Major performance win in large component trees",
        ],
    },
    "angular-iq-route-data": {
        "explanation": (
            "Pass data to routed components via the **Router** configuration and **ActivatedRoute**.\n\n"
            "**Static data** — `data` property on route config (roles, page title, feature flags):\n"
            "`{ path: 'admin', data: { role: 'admin' }, component: AdminComponent }`\n\n"
            "**Dynamic route params** — `/orders/:id` → `ActivatedRoute.snapshot.paramMap` or `paramMap` Observable\n\n"
            "**Query params** — `/orders?status=open` → `queryParamMap`\n\n"
            "**Router state** — `router.navigate(['/edit'], { state: { order } })` (not in URL, lost on refresh)\n\n"
            "For pre-fetching before render, use a **resolver** (resolve guard)."
        ),
        "code": """// app.routes.ts
{
  path: 'orders/:id',
  component: OrderDetailComponent,
  data: { breadcrumb: 'Order Detail' },
  resolve: { order: orderResolver },
}

// component
export class OrderDetailComponent {
  private route = inject(ActivatedRoute);
  id = toSignal(this.route.paramMap.pipe(map(p => +p.get('id')!)));
  breadcrumb = this.route.snapshot.data['breadcrumb'];

  // From resolver
  order = inject(ActivatedRoute).snapshot.data['order'] as Order;
}""",
        "language": "typescript",
        "key_points": [
            "data = static config on route definition",
            "paramMap / queryParamMap for dynamic URL segments",
            "router state for one-time navigation payload",
            "resolvers pre-load data before component renders",
        ],
    },
    "angular-iq-resolve-guard": {
        "explanation": (
            "A **resolve guard** ( **`ResolveFn`** in modern Angular) **pre-fetches data** before the route "
            "activates and the component renders. The navigation **waits** until the Observable/Promise completes.\n\n"
            "Use when the component **requires data immediately** (no loading spinner flash) — e.g. edit form "
            "needs entity by id.\n\n"
            "Contrast with **`CanActivate`** (allow/deny navigation) and lazy loading. "
            "If resolve fails, navigation is cancelled or redirected to an error route."
        ),
        "code": """export const orderResolver: ResolveFn<Order> = (route) => {
  const id = +route.paramMap.get('id')!;
  const service = inject(OrderService);
  return service.getById(id).pipe(
    catchError(() => {
      inject(Router).navigate(['/not-found']);
      return EMPTY;
    }),
  );
};

// routes
{ path: 'orders/:id/edit', component: OrderEditComponent, resolve: { order: orderResolver } }

// component — data ready on init
order = inject(ActivatedRoute).snapshot.data['order'] as Order;""",
        "language": "typescript",
        "key_points": [
            "ResolveFn pre-loads data before route activation",
            "Navigation waits for Observable/Promise to complete",
            "Avoids empty-then-load flicker in the component",
            "Handle errors — redirect if entity not found",
        ],
    },
    "angular-iq-content-projection": {
        "explanation": (
            "**Content projection** passes **HTML/content from the parent** into a child component using "
            "**`<ng-content>`** — like slots in Web Components.\n\n"
            "**Single slot:** `<ng-content></ng-content>` receives everything between child tags.\n\n"
            "**Multi-slot:** `<ng-content select=\"[card-header]\">` — targeted projection.\n\n"
            "Use for reusable wrappers: cards, modals, layout shells, tables with custom cell templates."
        ),
        "code": """// card.component.html
<div class="card">
  <header><ng-content select="[card-header]"></ng-content></header>
  <section><ng-content></ng-content></section>
  <footer><ng-content select="[card-footer]"></ng-content></footer>
</div>

// parent usage
<app-card>
  <h2 card-header>Orders</h2>
  <p>42 open orders today.</p>
  <button card-footer (click)="refresh()">Refresh</button>
</app-card>""",
        "language": "html",
        "key_points": [
            "ng-content = slot for parent-provided markup",
            "select attribute for named/multi-slot projection",
            "Use for reusable layout/wrapper components",
            "ContentChild queries projected content from parent",
        ],
    },
    "angular-iq-viewchild": {
        "explanation": (
            "**`@ViewChild`** queries a **child component, directive, or DOM element** from the component's "
            "**own template** (not projected content — use **`@ContentChild`** for that).\n\n"
            "Available after view init:\n"
            "- **`static: true`** — available in `ngOnInit` (single, fixed element)\n"
            "- **`static: false`** (default) — available in **`ngAfterViewInit`**\n\n"
            "Modern Angular: **`viewChild()` / `viewChild.required()`** signal-based queries (Angular 17+).\n\n"
            "Use for: focus input, call child method, integrate third-party DOM libs — **not** primary data flow."
        ),
        "code": """@Component({
  template: `
    <input #searchBox type="search" />
    <app-order-table #table />
  `,
})
export class OrdersPageComponent implements AfterViewInit {
  searchInput = viewChild<ElementRef<HTMLInputElement>>('searchBox');
  table = viewChild.required(OrderTableComponent);

  ngAfterViewInit(): void {
    this.searchInput()?.nativeElement.focus();
    this.table().refresh();
  }

  // Classic API
  @ViewChild('searchBox') searchBoxClassic!: ElementRef;
  @ViewChild(OrderTableComponent) tableClassic!: OrderTableComponent;
}""",
        "language": "typescript",
        "key_points": [
            "ViewChild = query own template; ContentChild = projected content",
            "Available in ngAfterViewInit (static: false)",
            "viewChild() signal API is modern Angular 17+",
            "Use for DOM/imperative access — not data binding",
        ],
    },
    "angular-iq-pure-impure-pipes": {
        "explanation": (
            "Angular **pipes** transform values in templates (`{{ date | date:'short' }}`).\n\n"
            "**Pure pipe** (default): runs **only** when the **input reference** changes or the component "
            "is marked dirty from its zone. Angular caches the result for performance.\n\n"
            "**Impure pipe** (`pure: false`): runs on **every change detection cycle** — needed when transform "
            "depends on global/mutated state (e.g. filtering a shared array in place).\n\n"
            "**Prefer pure pipes** — impure pipes can hurt performance. Use **`computed()` signals** or "
            "component getters for complex derived state instead of impure pipes."
        ),
        "code": """// Pure — default, cached until input ref changes
@Pipe({ name: 'orderTotal', pure: true })
export class OrderTotalPipe implements PipeTransform {
  transform(items: OrderItem[]): number {
    return items.reduce((sum, i) => sum + i.price, 0);
  }
}

// Impure — runs every CD cycle (use sparingly)
@Pipe({ name: 'filterActive', pure: false })
export class FilterActivePipe implements PipeTransform {
  transform(users: User[]): User[] {
    return users.filter(u => u.active); // if users mutated in place
  }
}""",
        "language": "typescript",
        "key_points": [
            "Pure = cached, runs on input reference change only",
            "Impure = every change detection (pure: false)",
            "Default pipes (date, currency, async) are pure",
            "Avoid impure pipes in large templates — perf cost",
        ],
    },
    "angular-iq-switchmap": {
        "explanation": (
            "**`switchMap`** is an RxJS **higher-order operator**. For each value from the source Observable, "
            "it **subscribes to an inner Observable** and emits its values. When a **new source value arrives**, "
            "it **unsubscribes from the previous inner** Observable.\n\n"
            "**Classic Angular use case:** **typeahead search** — cancel the in-flight HTTP request when the user "
            "types the next character.\n\n"
            "Compare: **`mergeMap`** keeps all inner subscriptions; **`concatMap`** queues them; "
            "**`switchMap`** cancels stale work."
        ),
        "code": """// Search box — cancel previous HTTP on new keystroke
this.searchControl.valueChanges.pipe(
  debounceTime(300),
  distinctUntilChanged(),
  switchMap(term =>
    this.http.get<Item[]>(`/api/search?q=${encodeURIComponent(term)}`)
  ),
).subscribe(results => this.results.set(results));

// Route param → load entity (cancel if user navigates quickly)
this.route.paramMap.pipe(
  switchMap(params => this.service.getById(+params.get('id')!)),
).subscribe(order => this.order.set(order));""",
        "language": "typescript",
        "key_points": [
            "Cancels previous inner Observable on new source value",
            "Ideal for search, route params, repeated user input",
            "Use mergeMap when all requests must complete",
            "Always handle errors with catchError in HTTP chains",
        ],
    },
    "angular-iq-forkjoin-combinelatest": {
        "explanation": (
            "**`forkJoin`** — waits until **all** source Observables **complete**, then emits **once** with "
            "an array (or object) of their **final values**. If **any** source errors, forkJoin errors. "
            "Perfect for **parallel HTTP on page init** (load user + orders + settings together).\n\n"
            "**`combineLatest`** — emits whenever **any** source emits, after each has emitted at least once. "
            "Gets the **latest value from each**. Perfect for **form filters** that react to multiple changing inputs.\n\n"
            "Rule of thumb: **forkJoin = parallel init load**; **combineLatest = reactive combinations**."
        ),
        "code": """// forkJoin — dashboard init (all must complete)
forkJoin({
  user: this.userService.getProfile(),
  orders: this.orderService.getRecent(),
  settings: this.settingsService.get(),
}).subscribe(({ user, orders, settings }) => {
  this.dashboard.set({ user, orders, settings });
});

// combineLatest — reactive filter
combineLatest([
  this.statusFilter.valueChanges.pipe(startWith('open')),
  this.dateRange.valueChanges.pipe(startWith('7d')),
]).pipe(
  switchMap(([status, range]) => this.api.search(status, range)),
).subscribe(rows => this.rows.set(rows));""",
        "language": "typescript",
        "key_points": [
            "forkJoin = wait for all to complete, emit once",
            "combineLatest = emit when any source emits latest tuple",
            "forkJoin fails if any inner stream errors",
            "combineLatest + switchMap = cancellable filtered search",
        ],
    },
    "angular-iq-take-tap": {
        "explanation": (
            "**`take(n)`** — completes after receiving **n emissions**, then unsubscribes. "
            "`take(1)` is common for one-shot HTTP-like streams or first value only.\n\n"
            "**`tap()`** (formerly `do`) — performs **side effects** (logging, caching, loading flags) "
            "**without modifying** the stream values. Use for `console.log`, set `loading = true/false`, "
            "write to cache.\n\n"
            "Both are pure utility operators — **`tap`** belongs in the middle of a pipe; **`take`** "
            "often at the end to limit subscription lifetime."
        ),
        "code": """this.orderService.getOrders().pipe(
  tap(() => this.loading.set(true)),           // side effect before
  tap(orders => console.debug('loaded', orders.length)),
  catchError(err => {
    this.error.set(err.message);
    return of([]);
  }),
  tap(() => this.loading.set(false)),          // side effect after
).subscribe(orders => this.orders.set(orders));

// take(1) — auto-complete after first emission
this.authService.getToken().pipe(take(1)).subscribe(token => this.token = token);

// takeUntil — preferred unsubscribe pattern in components
this.updates$.pipe(takeUntil(this.destroy$)).subscribe(/* ... */);""",
        "language": "typescript",
        "key_points": [
            "take(n) completes after n values — take(1) for one-shot",
            "tap() for side effects without changing stream data",
            "tap for loading spinners and debug logging",
            "takeUntil(destroy$) for component cleanup",
        ],
    },
}
