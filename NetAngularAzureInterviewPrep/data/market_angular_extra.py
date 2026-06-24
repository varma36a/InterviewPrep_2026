"""Additional top Angular interview questions — expands frontend section to 50+."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("frontend", "foundation"): [
        InterviewItem(
            "ngmodule-vs-standalone",
            "NgModule vs standalone components — what changed in modern Angular?",
            "Standalone components replace NgModule boilerplate for most new apps.",
            "",
        ),
        InterviewItem(
            "view-encapsulation",
            "What is ViewEncapsulation in Angular? Explain Emulated, None, and ShadowDom.",
            "Controls how component CSS is scoped to the DOM.",
            "",
        ),
        InterviewItem(
            "content-projection",
            "What is content projection (ng-content) in Angular?",
            "Pass template content from parent into child component slots.",
            "",
        ),
        InterviewItem(
            "viewchild-contentchild",
            "What is the difference between @ViewChild and @ContentChild?",
            "ViewChild queries the component template; ContentChild queries projected content.",
            "",
        ),
        InterviewItem(
            "async-pipe",
            "Why use the async pipe in Angular templates?",
            "Subscribes to Observables/Promises and triggers change detection automatically.",
            "",
        ),
        InterviewItem(
            "trackby-for-loops",
            "What is trackBy and why use it in @for / *ngFor loops?",
            "trackBy helps Angular identify list items by id to avoid re-rendering entire DOM.",
            "",
        ),
        InterviewItem(
            "two-way-binding",
            "How does two-way binding work in Angular?",
            "Combines property binding and event binding — [(ngModel)] or model() signals.",
            "",
        ),
        InterviewItem(
            "template-driven-forms",
            "When would you use template-driven forms vs reactive forms?",
            "Template-driven for simple forms; reactive for complex validation and testing.",
            "",
        ),
    ],
    ("frontend", "intermediate"): [
        InterviewItem(
            "host-listener-binding",
            "What are @HostListener and @HostBinding in Angular?",
            "Listen to host DOM events and bind properties on the host element.",
            "",
        ),
        InterviewItem(
            "angular-security-xss",
            "How does Angular protect against XSS? What is DomSanitizer?",
            "Angular sanitizes bindings by default; DomSanitizer for trusted HTML.",
            "",
        ),
        InterviewItem(
            "activated-route-params",
            "How do you read route params, query params, and fragments in Angular?",
            "ActivatedRoute provides snapshot and observable access to URL data.",
            "",
        ),
        InterviewItem(
            "functional-route-guards",
            "What are functional route guards in Angular (CanActivateFn)?",
            "Modern guard functions using inject() instead of class-based guards.",
            "",
        ),
        InterviewItem(
            "component-communication",
            "What are the patterns for component communication in Angular?",
            "Parent-child via @Input/@Output, siblings via shared service, NgRx for global state.",
            "",
        ),
        InterviewItem(
            "form-array-reactive",
            "How do you use FormArray for dynamic reactive forms?",
            "FormArray holds a list of FormGroup/FormControl for repeating fields.",
            "",
        ),
        InterviewItem(
            "custom-injection-token",
            "What is InjectionToken and when do you use it?",
            "Type-safe token for injecting configuration values or non-class dependencies.",
            "",
        ),
        InterviewItem(
            "share-replay-rxjs",
            "What does shareReplay do in RxJS and when use it in Angular?",
            "Multicasts and replays the last N emissions to late subscribers — cache HTTP calls.",
            "",
        ),
        InterviewItem(
            "combineLatest-forkJoin",
            "Explain combineLatest vs forkJoin in RxJS.",
            "combineLatest emits when any source emits; forkJoin waits for all to complete.",
            "",
        ),
        InterviewItem(
            "subject-vs-behaviorsubject",
            "What is the difference between Subject, BehaviorSubject, and ReplaySubject?",
            "BehaviorSubject has current value; ReplaySubject replays N past values.",
            "",
        ),
        InterviewItem(
            "angular-cdk",
            "What is the Angular Component Dev Kit (CDK)?",
            "Headless UI primitives: overlay, drag-drop, a11y, virtual scroll, breakpoints.",
            "",
        ),
        InterviewItem(
            "angular-cli-commands",
            "What essential Angular CLI commands should you know for interviews?",
            "ng new, generate, build, test, serve, lint, update, and ng add.",
            "",
        ),
    ],
    ("frontend", "advanced"): [
        InterviewItem(
            "signal-computed-effect",
            "Explain Angular signals: signal(), computed(), and effect().",
            "Fine-grained reactivity without Zone.js — computed derives, effect runs side effects.",
            "",
        ),
        InterviewItem(
            "zoneless-angular",
            "What is zoneless Angular and why is Angular moving away from Zone.js?",
            "Signals + manual change detection remove Zone.js patch overhead.",
            "",
        ),
        InterviewItem(
            "aot-vs-jit-compilation",
            "What is the difference between AOT and JIT compilation in Angular?",
            "AOT compiles at build time for production; JIT compiled in browser (dev only today).",
            "",
        ),
        InterviewItem(
            "dynamic-components",
            "How do you load components dynamically in Angular?",
            "ViewContainerRef.createComponent() or NgComponentOutlet for runtime component loading.",
            "",
        ),
        InterviewItem(
            "angular-error-handler",
            "How do you implement global error handling in Angular?",
            "Custom ErrorHandler service catches unhandled errors app-wide.",
            "",
        ),
        InterviewItem(
            "angular-pwa-service-worker",
            "How does Angular PWA and service workers work?",
            "ng add @angular/pwa registers a service worker for offline caching and updates.",
            "",
        ),
        InterviewItem(
            "typescript-decorators",
            "What are TypeScript decorators and how does Angular use them?",
            "@Component, @Injectable, @Input are decorators — metadata for Angular compiler.",
            "",
        ),
        InterviewItem(
            "angular-performance",
            "What are the top Angular performance optimization techniques?",
            "OnPush, trackBy, lazy loading, pure pipes, defer blocks, signals, virtual scroll.",
            "",
        ),
        InterviewItem(
            "angular-i18n",
            "How does internationalization (i18n) work in Angular?",
            "Mark strings in templates, extract messages, build per-locale bundles.",
            "",
        ),
        InterviewItem(
            "angular-vs-react",
            "Compare Angular vs React for enterprise interviews.",
            "Angular = full framework (DI, routing, forms); React = library + ecosystem choices.",
            "",
        ),
    ],
}

# Remove placeholder hack — explanations come from MARKET_DETAILED
for _items in MARKET_ITEMS.values():
    for item in _items:
        if not item.code.strip():
            item.code = "// See detailed code example below"

MARKET_DETAILED: dict[str, dict] = {
    "ngmodule-vs-standalone": {
        "explanation": (
            "Before Angular 14+, every component belonged to an **NgModule** that declared imports, "
            "declarations, and providers. **Standalone components** (`standalone: true`) bundle their "
            "own dependencies directly — no NgModule wrapper required. Modern Angular apps bootstrap "
            "with `bootstrapApplication(AppComponent, { providers: [...] })` instead of `NgModule`. "
            "**When to use NgModule today:** legacy apps, shared libraries not yet migrated, or "
            "FeatureModule patterns in large codebases. **Interview tip:** greenfield Angular 17+ "
            "projects should default to standalone; mention gradual migration with `imports: [OldModule]`."
        ),
        "code": """// Modern standalone component — no NgModule
@Component({
  selector: 'app-orders',
  standalone: true,
  imports: [CommonModule, RouterLink, OrderRowComponent],
  template: `
    @for (order of orders(); track order.id) {
      <app-order-row [order]="order" />
    }
  `
})
export class OrdersComponent {
  orders = signal<Order[]>([]);
}

// Bootstrap without NgModule (main.ts)
bootstrapApplication(AppComponent, {
  providers: [provideRouter(routes), provideHttpClient()]
});

// Legacy NgModule — still valid, common in enterprise codebases
@NgModule({
  declarations: [LegacyDashboardComponent],
  imports: [CommonModule, RouterModule],
  exports: [LegacyDashboardComponent]
})
export class DashboardModule {}""",
        "language": "typescript",
        "key_points": [
            "Standalone = self-contained imports, no NgModule required",
            "bootstrapApplication replaces platformBrowserDynamic().bootstrapModule",
            "Migrate incrementally — standalone components can import NgModules",
            "Angular CLI defaults to standalone for ng generate component",
            "NgModule still appears in legacy and library code — know both",
        ],
    },
    "view-encapsulation": {
        "explanation": (
            "**ViewEncapsulation** controls how Angular scopes component CSS to prevent style leakage. "
            "**Emulated (default):** Angular adds unique attributes (`_ngcontent-xxx`) to elements and "
            "rewrites selectors — simulates Shadow DOM without native support. **None:** styles become "
            "global — use for theme overrides or third-party integration. **ShadowDom:** uses native "
            "Shadow DOM for true style isolation. **When to change:** use `Encapsulation.None` for "
            "global utility components; `ShadowDom` when embedding in non-Angular pages. "
            "**Pitfall:** `::ng-deep` pierces encapsulation but is deprecated — prefer CSS variables or `:host`."
        ),
        "code": """@Component({
  selector: 'app-card',
  encapsulation: ViewEncapsulation.Emulated, // default
  styles: [`
    :host { display: block; padding: 1rem; }
    :host(.highlight) { border: 2px solid #512BD4; }
    .title { font-weight: 600; } /* scoped to this component */
  `],
  template: `<h2 class="title">{{ title }}</h2><ng-content />`
})
export class CardComponent {
  @Input() title = '';
}

// ShadowDom — true isolation, styles don't leak in or out
@Component({
  selector: 'app-widget',
  encapsulation: ViewEncapsulation.ShadowDom,
  styles: [`button { background: #512BD4; color: white; }`],
  template: `<button><ng-content /></button>`
})
export class WidgetComponent {}""",
        "language": "typescript",
        "key_points": [
            "Emulated = default, attribute-based scoping",
            "ShadowDom = native browser isolation",
            "None = global styles — use sparingly",
            ":host targets the component root element",
            "Avoid ::ng-deep — use CSS custom properties instead",
        ],
    },
    "content-projection": {
        "explanation": (
            "**Content projection** passes HTML/template content from a parent component into a child "
            "via `<ng-content>`. It enables reusable wrapper components (cards, modals, layouts) "
            "without knowing the inner content at design time. **Single-slot** projection uses one "
            "`<ng-content />`. **Multi-slot** uses `select` attribute: "
            "`<ng-content select=\"[card-header]\" />`. **Conditional projection:** content is always "
            "in the parent's template — the child decides where to render it. This differs from "
            "`@Input` which passes data, not templates."
        ),
        "code": """// Child — layout shell with named slots
@Component({
  selector: 'app-panel',
  standalone: true,
  template: `
    <header><ng-content select="[panel-header]" /></header>
    <main><ng-content /></main>           <!-- default slot -->
    <footer><ng-content select="[panel-footer]" /></footer>
  `
})
export class PanelComponent {}

// Parent — projects content into slots
@Component({
  template: `
    <app-panel>
      <h2 panel-header>Order Summary</h2>
      <p>3 items — $149.99</p>
      <button panel-footer>Checkout</button>
    </app-panel>
  `
})
export class CheckoutComponent {}""",
        "language": "typescript",
        "key_points": [
            "ng-content = template injection from parent to child",
            "select attribute enables multi-slot projection",
            "Different from @Input — passes markup, not just data",
            "Common in design systems: Card, Modal, Layout components",
            "Projected content stays in parent scope (can access parent methods)",
        ],
    },
    "viewchild-contentchild": {
        "explanation": (
            "**@ViewChild** queries elements in the component's **own template** — child components, "
            "DOM elements, or directives. **@ContentChild** queries elements **projected** into the "
            "component via `<ng-content>`. Both support `{ static: true }` (available in ngOnInit) "
            "vs `{ static: false }` (available after ngAfterViewInit/ngAfterContentInit). "
            "Modern Angular prefers **`viewChild()` and `contentChild()` signal-based queries** "
            "(Angular 17+). Use ViewChild to call methods on child components or focus an input element."
        ),
        "code": """@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [ChildComponent],
  template: `
    <app-child #childRef />
    <ng-content />
  `
})
export class ParentComponent implements AfterViewInit {
  // Signal-based (Angular 17+) — preferred
  child = viewChild.required(ChildComponent);
  searchInput = viewChild<ElementRef>('searchInput');

  // Classic decorator — still common in interviews
  @ViewChild('childRef') childClassic!: ChildComponent;
  @ContentChild(TabDirective) activeTab?: TabDirective;

  ngAfterViewInit() {
    this.child()?.focus(); // signal query
    this.childClassic.highlight();
  }
}""",
        "language": "typescript",
        "key_points": [
            "ViewChild = own template; ContentChild = projected content",
            "static: true available in ngOnInit; false in ngAfterViewInit",
            "viewChild() signal queries are the modern API (Angular 17+)",
            "Use to imperatively call child methods or access DOM",
            "Avoid overusing — prefer @Input/@Output for data flow",
        ],
    },
    "async-pipe": {
        "explanation": (
            "The **`async` pipe** subscribes to an Observable or Promise in the template and "
            "automatically unsubscribes when the component is destroyed — preventing memory leaks. "
            "When the Observable emits, it triggers **change detection** so the view updates. "
            "It is essential with **OnPush** change detection because it marks the component "
            "for check on each emission. **Best practice:** expose Observables from services "
            "and use `| async` in templates instead of manual `.subscribe()` in components."
        ),
        "code": """@Component({
  selector: 'app-orders',
  standalone: true,
  imports: [AsyncPipe],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    @if (orders$ | async; as orders) {
      <ul>
        @for (order of orders; track order.id) {
          <li>{{ order.id }} — {{ order.total | currency }}</li>
        }
      </ul>
    } @else {
      <p>Loading...</p>
    }
  `
})
export class OrdersComponent {
  orders$ = inject(OrderService).getOrders(); // Observable — no manual subscribe
}""",
        "language": "typescript",
        "key_points": [
            "Auto-subscribes and auto-unsubscribes — no memory leaks",
            "Triggers change detection on each emission",
            "Critical with OnPush strategy",
            "Use `as` alias: `(orders$ | async) as orders`",
            "Prefer async pipe over manual subscribe in components",
        ],
    },
    "trackby-for-loops": {
        "explanation": (
            "When Angular re-renders a list, it compares items by **object identity** by default. "
            "If the array is replaced (e.g., from HTTP), Angular destroys and recreates all DOM "
            "nodes — losing focus, animation state, and performance. **`trackBy`** (or `@for track`) "
            "tells Angular to identify items by a **stable unique key** (usually `id`). "
            "Only changed/added/removed items get DOM updates. This is a **top performance question** "
            "in Angular interviews, especially for large tables and infinite scroll lists."
        ),
        "code": """// Modern @for with track (Angular 17+)
@Component({
  template: `
    @for (user of users; track user.id) {
      <app-user-row [user]="user" />
    }
  `
})
export class UserListComponent {
  users: User[] = [];
}

// Legacy *ngFor with trackBy function
@Component({
  template: `
    <li *ngFor="let item of items; trackBy: trackById">{{ item.name }}</li>
  `
})
export class LegacyListComponent {
  items: Item[] = [];
  trackById(index: number, item: Item) { return item.id; } // stable identity
}""",
        "language": "typescript",
        "key_points": [
            "track / trackBy prevents unnecessary DOM re-creation",
            "Use a stable unique id — never track by index for mutable lists",
            "@for track is the modern syntax (Angular 17+)",
            "Critical for large lists, tables, and OnPush components",
            "Without trackBy, replacing array reference re-renders everything",
        ],
    },
    "two-way-binding": {
        "explanation": (
            "**Two-way binding** synchronizes a property and an event in both directions — when the "
            "model changes, the view updates; when the user changes the view, the model updates. "
            "Syntax: **`[(ngModel)]=\"property\"`** (banana-in-a-box). Under the hood it combines "
            "`[ngModel]` (property binding) and `(ngModelChange)` (event binding). "
            "In modern Angular, **`model()` signal inputs** (Angular 17.2+) provide two-way binding "
            "for components: `<app-search [(query)]=\"searchTerm\" />`. Requires `FormsModule` for ngModel."
        ),
        "code": """// Template-driven two-way binding
@Component({
  imports: [FormsModule],
  template: `
    <input [(ngModel)]="searchTerm" placeholder="Search orders..." />
    <p>You typed: {{ searchTerm }}</p>
  `
})
export class SearchComponent {
  searchTerm = '';
}

// Modern model() signal — two-way binding for custom components
@Component({ selector: 'app-counter', standalone: true, template: `...` })
export class CounterComponent {
  count = model(0); // parent can bind [(count)]="myCount"
}

// Parent usage
@Component({ template: `<app-counter [(count)]="total" />` })
export class ParentComponent { total = 0; }""",
        "language": "typescript",
        "key_points": [
            "[(ngModel)] = property binding + event binding combined",
            "Requires FormsModule import for ngModel",
            "model() signal is the modern two-way binding API",
            "Use for simple form inputs; prefer reactive forms for complex validation",
            "Banana-in-a-box syntax: [()] wraps property and event",
        ],
    },
    "template-driven-forms": {
        "explanation": (
            "**Template-driven forms** define form structure and validation in the HTML template using "
            "directives like `ngModel`, `ngForm`, and `#formRef=\"ngForm\"`. Angular creates the "
            "FormControl internally — less boilerplate but harder to unit test. **Reactive forms** "
            "define the model in TypeScript with `FormBuilder` — better for complex validation, "
            "dynamic fields, and testing. **Interview answer:** use template-driven for simple login "
            "or search forms; use reactive for multi-step wizards, dynamic FormArrays, and enterprise apps."
        ),
        "code": """// Template-driven — logic in template
@Component({
  imports: [FormsModule],
  template: `
    <form #loginForm="ngForm" (ngSubmit)="onSubmit(loginForm)">
      <input name="email" [(ngModel)]="email" required email #emailCtrl="ngModel" />
      @if (emailCtrl.invalid && emailCtrl.touched) {
        <span class="error">Valid email required</span>
      }
      <button [disabled]="loginForm.invalid">Login</button>
    </form>
  `
})
export class LoginComponent {
  email = '';
  onSubmit(form: NgForm) {
    if (form.valid) this.authService.login(this.email);
  }
}""",
        "language": "typescript",
        "key_points": [
            "Template-driven: Angular creates FormControl from ngModel",
            "Reactive: explicit FormGroup/FormControl in TypeScript",
            "Template-driven simpler; reactive more testable and powerful",
            "Enterprise apps overwhelmingly prefer reactive forms",
            "Both support validation — reactive makes cross-field rules easier",
        ],
    },
    "host-listener-binding": {
        "explanation": (
            "**@HostListener** listens to events on the **host element** of a component or directive "
            "— e.g., keyboard shortcuts, click-outside detection, hover effects. "
            "**@HostBinding** binds a property or class/style on the host element — e.g., "
            "`@HostBinding('class.active') isActive = true`. These are common in **directives** "
            "and reusable behavior components. Modern alternative: use **`host` property** in "
            "the `@Component`/`@Directive` decorator metadata (Angular 15+ preferred)."
        ),
        "code": """// Directive — click outside to close dropdown
@Directive({ selector: '[clickOutside]', standalone: true })
export class ClickOutsideDirective {
  @Output() clickOutside = new EventEmitter<void>();

  @HostListener('document:click', ['$event.target'])
  onClick(target: HTMLElement) {
    if (!this.elementRef.nativeElement.contains(target)) {
      this.clickOutside.emit();
    }
  }
  constructor(private elementRef: ElementRef) {}
}

// Modern host metadata (preferred in new code)
@Component({
  selector: 'app-toggle',
  host: {
    '[class.active]': 'isOn()',
    '(click)': 'toggle()',
    'role': 'switch',
    '[attr.aria-checked]': 'isOn()'
  },
  template: `<span>{{ isOn() ? 'ON' : 'OFF' }}</span>`
})
export class ToggleComponent {
  isOn = signal(false);
  toggle() { this.isOn.update(v => !v); }
}""",
        "language": "typescript",
        "key_points": [
            "HostListener = listen to events on the host element",
            "HostBinding = bind class/style/property on host",
            "Modern host: {} in decorator metadata is preferred",
            "Common for directives: click-outside, keyboard shortcuts",
            "Use role and aria attributes for accessibility",
        ],
    },
    "angular-security-xss": {
        "explanation": (
            "Angular **sanitizes all data binding by default** to prevent **Cross-Site Scripting (XSS)** — "
            "it strips dangerous HTML, URLs, and styles from interpolated values. "
            "**DomSanitizer** lets you explicitly mark content as trusted when you must render HTML "
            "from a CMS or rich text editor: `bypassSecurityTrustHtml()`. **Never bypass sanitization "
            "for user input** — only for admin-controlled content. Angular also provides "
            "**HttpClient XSRF protection** and **Content Security Policy** headers as defense layers. "
            "This is a mandatory security question for full-stack Angular + .NET interviews."
        ),
        "code": """@Component({
  template: `
    <!-- Safe — Angular sanitizes automatically -->
    <p>{{ userComment }}</p>

    <!-- Dangerous if unsanitized — use DomSanitizer for trusted CMS content -->
    <div [innerHTML]="trustedHtml"></div>
  `
})
export class CommentComponent implements OnInit {
  userComment = '<script>alert("xss")</script>Hello'; // rendered as text, script stripped
  trustedHtml!: SafeHtml;

  constructor(private sanitizer: DomSanitizer) {}

  ngOnInit() {
    const cmsContent = this.cmsService.getArticleBody(); // admin-controlled only!
    this.trustedHtml = this.sanitizer.bypassSecurityTrustHtml(cmsContent);
  }
}

// API: always validate and encode on server too (defense in depth)""",
        "language": "typescript",
        "key_points": [
            "Angular sanitizes {{ }}, [property], and [innerHTML] by default",
            "DomSanitizer.bypassSecurityTrustHtml only for trusted admin content",
            "Never bypass sanitization for user-generated input",
            "Combine with server-side validation and CSP headers",
            "HttpClient includes built-in XSRF token support",
        ],
    },
    "activated-route-params": {
        "explanation": (
            "**ActivatedRoute** gives access to the current route's **params**, **queryParams**, "
            "**fragment**, and **data**. Use **`route.snapshot.paramMap.get('id')`** for one-time "
            "reads (e.g., on init). Subscribe to **`route.paramMap`** when params can change "
            "without component destruction (same route, different id). **Query params** carry "
            "filters and pagination: `?page=2&sort=date`. **Route data** is static config set "
            "in route definition — useful for breadcrumbs and page titles."
        ),
        "code": """@Component({ selector: 'app-order-detail', standalone: true, template: `...` })
export class OrderDetailComponent implements OnInit {
  private route = inject(ActivatedRoute);
  private orderService = inject(OrderService);
  order = signal<Order | null>(null);

  ngOnInit() {
    // Snapshot — one-time read (component recreated on param change)
    const id = this.route.snapshot.paramMap.get('id')!;

    // Observable — reacts when params change without destroy/recreate
    this.route.paramMap.pipe(
      switchMap(params => this.orderService.getById(+params.get('id')!)),
      takeUntilDestroyed()
    ).subscribe(order => this.order.set(order));

    // Query params: /orders?page=2&status=shipped
    this.route.queryParamMap.subscribe(q => {
      const page = +(q.get('page') ?? 1);
      const status = q.get('status');
    });
  }
}""",
        "language": "typescript",
        "key_points": [
            "snapshot for one-time read; observable for reactive param changes",
            "paramMap for route params (/orders/:id); queryParamMap for ?key=value",
            "switchMap cancels previous HTTP call when id changes",
            "Route data property for static config (title, permissions)",
            "takeUntilDestroyed() auto-unsubscribes (Angular 16+)",
        ],
    },
    "functional-route-guards": {
        "explanation": (
            "Angular 15+ introduced **functional guards** — plain functions instead of injectable classes. "
            "They use the **`inject()`** function to access services inside the guard. "
            "Types: **`CanActivateFn`**, **`CanDeactivateFn`**, **`CanMatchFn`**, **`ResolveFn`**. "
            "Functional guards are **tree-shakable**, simpler to test, and the recommended approach "
            "for new code. Class-based guards (`implements CanActivate`) still work in legacy apps."
        ),
        "code": """// Functional guard — modern approach
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);
  if (auth.isLoggedIn()) return true;
  return router.createUrlTree(['/login']);
};

// Role-based guard with route data
export const roleGuard: CanActivateFn = (route) => {
  const auth = inject(AuthService);
  const requiredRole = route.data['role'] as string;
  return auth.hasRole(requiredRole) || inject(Router).createUrlTree(['/unauthorized']);
};

// Route config
const routes: Routes = [
  { path: 'admin', canActivate: [authGuard, roleGuard], data: { role: 'Admin' },
    loadComponent: () => import('./admin/admin.component') },
  { path: 'orders', canActivate: [authGuard],
    loadChildren: () => import('./orders/orders.routes') },
];""",
        "language": "typescript",
        "key_points": [
            "CanActivateFn replaces class CanActivate guards",
            "Use inject() inside functional guards for DI",
            "Return UrlTree to redirect; return false to cancel navigation",
            "CanMatchFn for lazy-load protection (replaces CanLoad)",
            "Stack multiple guards: canActivate: [authGuard, roleGuard]",
        ],
    },
    "component-communication": {
        "explanation": (
            "Angular components communicate through several patterns depending on relationship. "
            "**Parent → Child:** `@Input()` properties. **Child → Parent:** `@Output()` EventEmitter. "
            "**Sibling components:** shared **injectable service** (Subject/BehaviorSubject). "
            "**Distant/unrelated:** **NgRx store** or signal-based shared state service. "
            "**Avoid:** `@ViewChild` for data flow (imperative, tight coupling). "
            "Interviewers want you to describe the right pattern for each scenario and explain "
            "why services scale better than `@Input` chaining through many levels (prop drilling)."
        ),
        "code": """// 1. Parent → Child via @Input
@Component({ template: `<app-row [order]="order" [highlight]="true" />` })
export class OrderListComponent { order: Order = { id: 1, total: 99 }; }

// 2. Child → Parent via @Output
@Component({ selector: 'app-row', template: `<button (click)="selected.emit(order)">Select</button>` })
export class OrderRowComponent {
  @Input() order!: Order;
  @Output() selected = new EventEmitter<Order>();
}

// 3. Siblings via shared service
@Injectable({ providedIn: 'root' })
export class CartService {
  private items = signal<CartItem[]>([]);
  readonly cart = this.items.asReadonly();
  addItem(item: CartItem) { this.items.update(list => [...list, item]); }
}

// HeaderComponent and CartBadgeComponent both inject CartService""",
        "language": "typescript",
        "key_points": [
            "@Input down, @Output up — direct parent-child only",
            "Shared service for siblings and unrelated components",
            "NgRx/signal store for complex global state",
            "Avoid prop drilling — don't chain @Input through 5 levels",
            "ViewChild is for imperative DOM access, not primary data flow",
        ],
    },
    "form-array-reactive": {
        "explanation": (
            "**FormArray** is a Reactive Forms construct for **dynamic lists of controls** — "
            "order line items, phone numbers, skills, or any repeating field group. "
            "Each entry is a `FormGroup` or `FormControl` inside the array. "
            "You can **add/remove** entries at runtime with `push()` and `removeAt()`. "
            "In templates, iterate with `@for` over `formArray.controls`. "
            "Common enterprise pattern for invoice lines, address lists, and multi-select forms."
        ),
        "code": """@Component({
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="orderForm" (ngSubmit)="submit()">
      <div formArrayName="lines">
        @for (line of lines.controls; track $index; let i = $index) {
          <div [formGroupName]="i">
            <input formControlName="product" placeholder="Product" />
            <input formControlName="qty" type="number" />
            <button type="button" (click)="removeLine(i)">Remove</button>
          </div>
        }
      </div>
      <button type="button" (click)="addLine()">Add Line</button>
      <button type="submit" [disabled]="orderForm.invalid">Submit</button>
    </form>
  `
})
export class OrderFormComponent {
  private fb = inject(FormBuilder);
  orderForm = this.fb.group({
    customer: ['', Validators.required],
    lines: this.fb.array<FormGroup>([])
  });
  get lines() { return this.orderForm.get('lines') as FormArray; }
  addLine() {
    this.lines.push(this.fb.group({ product: ['', Validators.required], qty: [1, Validators.min(1)] }));
  }
  removeLine(i: number) { this.lines.removeAt(i); }
  submit() { console.log(this.orderForm.value); }
}""",
        "language": "typescript",
        "key_points": [
            "FormArray holds dynamic list of FormGroup/FormControl",
            "add/remove entries at runtime with push() and removeAt()",
            "Use formArrayName and formGroupName in template",
            "Common for order lines, tags, phone numbers",
            "Validate entire array and individual entries",
        ],
    },
    "custom-injection-token": {
        "explanation": (
            "**InjectionToken** creates a type-safe token for values that aren't classes — "
            "API URLs, feature flags, configuration objects, or third-party instances. "
            "Unlike string tokens, InjectionToken provides **compile-time type checking** "
            "and avoids naming collisions. Use with **`@Inject(TOKEN)`** in constructors "
            "or **`inject(TOKEN)`** in functional code. Common in libraries and "
            "enterprise apps for environment-specific configuration."
        ),
        "code": """// Define typed tokens
export const API_BASE_URL = new InjectionToken<string>('api.baseUrl');
export const APP_CONFIG = new InjectionToken<AppConfig>('app.config');

// Provide values
bootstrapApplication(AppComponent, {
  providers: [
    { provide: API_BASE_URL, useValue: 'https://api.example.com' },
    { provide: APP_CONFIG, useValue: { featureX: true, maxRetries: 3 } },
  ]
});

// Consume in service
@Injectable({ providedIn: 'root' })
export class OrderService {
  private baseUrl = inject(API_BASE_URL);
  private config = inject(APP_CONFIG);
  private http = inject(HttpClient);

  getOrders() {
    return this.http.get<Order[]>(`${this.baseUrl}/orders`);
  }
}""",
        "language": "typescript",
        "key_points": [
            "InjectionToken for non-class dependencies (config, URLs, flags)",
            "Type-safe unlike string-based DI tokens",
            "Provide with useValue, useFactory, or useClass",
            "inject(TOKEN) or @Inject(TOKEN) to consume",
            "Common for API URLs and feature configuration",
        ],
    },
    "share-replay-rxjs": {
        "explanation": (
            "**shareReplay** multicasts an Observable and **replays the last N emissions** to "
            "new subscribers — preventing duplicate HTTP calls when multiple components subscribe "
            "to the same data stream. Without it, each `.subscribe()` triggers a new HTTP request. "
            "Use **`shareReplay({ bufferSize: 1, refCount: true })`** to cache the latest value "
            "and auto-unsubscribe when all subscribers leave. Essential for **shared lookup data** "
            "(countries, categories) and **auth user profile** accessed from many components."
        ),
        "code": """@Injectable({ providedIn: 'root' })
export class LookupService {
  private http = inject(HttpClient);

  // Without shareReplay — every subscribe = new HTTP call
  // getCountries() { return this.http.get<Country[]>('/api/countries'); }

  // With shareReplay — one HTTP call, cached result shared
  private countries$ = this.http.get<Country[]>('/api/countries').pipe(
    shareReplay({ bufferSize: 1, refCount: true })
  );

  getCountries() { return this.countries$; }
}

// Component A and Component B both subscribe — only ONE HTTP request
@Component({ template: `@for (c of countries$ | async; track c.code) { ... }` })
export class ComponentA { countries$ = inject(LookupService).getCountries(); }""",
        "language": "typescript",
        "key_points": [
            "shareReplay caches and replays last N values to late subscribers",
            "Prevents duplicate HTTP calls from multiple subscribers",
            "bufferSize: 1 for latest value; refCount: true for auto cleanup",
            "Use for shared lookup/reference data",
            "Alternative: store in signal after first fetch",
        ],
    },
    "combineLatest-forkJoin": {
        "explanation": (
            "**combineLatest** emits whenever **any** source Observable emits, combining the "
            "latest value from each — ideal for **reactive forms** where multiple filters combine. "
            "**forkJoin** waits until **all** sources complete, then emits an array/tuple of final "
            "values — ideal for **parallel HTTP calls** on page load (user + orders + settings). "
            "If any forkJoin source errors, the entire result errors. "
            "Use **`forkJoin({ user: user$, orders: orders$ })`** for named results."
        ),
        "code": """// forkJoin — parallel HTTP on page load, wait for ALL
@Component({ /* ... */ })
export class DashboardComponent implements OnInit {
  private http = inject(HttpClient);
  dashboard$ = forkJoin({
    user: this.http.get<User>('/api/me'),
    orders: this.http.get<Order[]>('/api/orders'),
    stats: this.http.get<Stats>('/api/stats'),
  }); // emits once when all three complete

  template = `@if (dashboard$ | async; as d) {
    <h1>Welcome {{ d.user.name }}</h1>
    <p>{{ d.orders.length }} orders</p>
  }`;
}

// combineLatest — react to any filter change
filters$ = combineLatest([this.statusFilter$, this.dateRange$]).pipe(
  switchMap(([status, range]) => this.api.search(status, range))
);""",
        "language": "typescript",
        "key_points": [
            "forkJoin = wait for all to complete (parallel HTTP on init)",
            "combineLatest = emit when any source changes (reactive filters)",
            "forkJoin fails if any source errors",
            "Use forkJoin object syntax for named results",
            "switchMap after combineLatest to cancel stale API calls",
        ],
    },
    "subject-vs-behaviorsubject": {
        "explanation": (
            "All three are **RxJS Subjects** (both Observable and Observer). "
            "**Subject:** no initial value; subscribers only get **future** emissions. "
            "**BehaviorSubject:** stores and emits the **current value** to new subscribers immediately. "
            "**ReplaySubject:** replays the **last N values** to new subscribers. "
            "In Angular, **BehaviorSubject** is the standard for shared service state "
            "(cart count, auth user). **Subject** for event buses (notification fired). "
            "Modern apps increasingly replace these with **Angular signals**."
        ),
        "code": """// Subject — event bus, no initial value
@Injectable({ providedIn: 'root' })
export class NotificationService {
  private notifications = new Subject<string>();
  notifications$ = this.notifications.asObservable();
  notify(message: string) { this.notifications.next(message); }
}

// BehaviorSubject — state with current value
@Injectable({ providedIn: 'root' })
export class AuthService {
  private userSubject = new BehaviorSubject<User | null>(null);
  user$ = this.userSubject.asObservable();
  get currentUser() { return this.userSubject.value; } // synchronous access
  login(user: User) { this.userSubject.next(user); }
  logout() { this.userSubject.next(null); }
}

// Modern replacement with signals
@Injectable({ providedIn: 'root' })
export class ModernAuthService {
  private userSignal = signal<User | null>(null);
  user = this.userSignal.asReadonly();
  login(user: User) { this.userSignal.set(user); }
}""",
        "language": "typescript",
        "key_points": [
            "Subject = no memory, events only",
            "BehaviorSubject = current value + future updates",
            "ReplaySubject = last N values replayed",
            "BehaviorSubject.value for synchronous read",
            "Signals are the modern Angular alternative",
        ],
    },
    "angular-cdk": {
        "explanation": (
            "The **Angular Component Dev Kit (CDK)** provides **headless, behavior-focused** UI "
            "primitives without Material Design styling. Key modules: **Overlay** (popups, tooltips), "
            "**Portal** (dynamic content injection), **Drag & Drop**, **Virtual Scroll** (large lists), "
            "**A11y** (focus management, live announcer), **Layout** (BreakpointObserver), "
            "**Table** (data source abstraction). Use CDK when you need behavior without Material "
            "look, or when building a custom design system on top of CDK primitives."
        ),
        "code": """import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { CdkVirtualScrollViewport } from '@angular/cdk/scrolling';
import { LiveAnnouncer } from '@angular/cdk/a11y';

@Component({
  standalone: true,
  imports: [CdkVirtualScrollViewport],
  template: `
    <!-- Virtual scroll — renders only visible rows (10k+ items) -->
    <cdk-virtual-scroll-viewport itemSize="48" style="height: 400px">
      @for (item of items; track item.id) {
        <div class="row">{{ item.name }}</div>
      }
    </cdk-virtual-scroll-viewport>
  `
})
export class LargeListComponent {
  items = Array.from({ length: 10000 }, (_, i) => ({ id: i, name: `Item ${i}` }));
  private bp = inject(BreakpointObserver);
  isMobile$ = this.bp.observe([Breakpoints.Handset]); // responsive layout
}""",
        "language": "typescript",
        "key_points": [
            "CDK = headless UI behaviors without Material styling",
            "Virtual Scroll for performant large lists",
            "BreakpointObserver for responsive component logic",
            "Overlay/Portal for modals, tooltips, dropdowns",
            "Build custom design systems on CDK primitives",
        ],
    },
    "angular-cli-commands": {
        "explanation": (
            "The **Angular CLI** (`ng`) scaffolds, builds, tests, and deploys Angular apps. "
            "Interviewers expect familiarity with daily commands and the **`angular.json`** "
            "workspace configuration. Key commands: **`ng new`**, **`ng generate`** (component, "
            "service, guard, pipe), **`ng serve`**, **`ng build`**, **`ng test`**, **`ng lint`**, "
            "**`ng update`** (migrate versions), **`ng add`** (install libraries like Angular Material). "
            "Production builds use **`ng build --configuration production`** with AOT compilation and tree-shaking."
        ),
        "code": """# Project setup
ng new my-app --standalone --style=scss --routing
cd my-app

# Generate artifacts
ng generate component orders/order-list --standalone
ng generate service core/auth
ng generate guard core/auth --functional
ng generate pipe shared/currency-format

# Development
ng serve                          # dev server at localhost:4200
ng serve --open --port 4300       # custom port, auto-open browser

# Production build
ng build --configuration production  # output in dist/, AOT + tree-shaking

# Testing & quality
ng test                           # Karma/Jasmine unit tests
ng lint                           # ESLint rules

# Add libraries
ng add @angular/material          # installs + configures Material
ng add @angular/pwa               # adds service worker

# Update Angular version
ng update @angular/core @angular/cli""",
        "language": "bash",
        "key_points": [
            "ng generate (ng g) scaffolds components, services, guards, pipes",
            "ng serve for dev; ng build --configuration production for deploy",
            "ng add installs and configures libraries (Material, PWA)",
            "ng update migrates between Angular versions",
            "angular.json controls build targets and configurations",
        ],
    },
    "signal-computed-effect": {
        "explanation": (
            "**Signals** are Angular's fine-grained reactivity primitives (Angular 16+). "
            "**`signal(initialValue)`** creates writable reactive state. "
            "**`computed(() => ...)`** derives read-only values from other signals — like a "
            "spreadsheet formula, recalculates only when dependencies change. "
            "**`effect(() => ...)`** runs side effects (logging, localStorage, HTTP) when "
            "signals change — runs during change detection. Signals enable **zoneless Angular** "
            "and are the future of Angular state management, replacing many RxJS + BehaviorSubject patterns."
        ),
        "code": """@Component({
  selector: 'app-cart',
  standalone: true,
  template: `
    <p>Items: {{ itemCount() }}</p>
    <p>Subtotal: {{ subtotal() | currency }}</p>
    <p>Tax: {{ tax() | currency }}</p>
    <p>Total: {{ total() | currency }}</p>
  `
})
export class CartComponent {
  items = signal<CartItem[]>([]);

  // Derived state — auto-recalculates when items changes
  itemCount = computed(() => this.items().length);
  subtotal = computed(() => this.items().reduce((sum, i) => sum + i.price * i.qty, 0));
  tax = computed(() => this.subtotal() * 0.08);
  total = computed(() => this.subtotal() + this.tax());

  addItem(item: CartItem) {
    this.items.update(list => [...list, item]); // immutable update
  }

  constructor() {
    // Side effect — runs when total changes
    effect(() => {
      console.log('Cart total updated:', this.total());
    });
  }
}""",
        "language": "typescript",
        "key_points": [
            "signal() = writable reactive state",
            "computed() = derived read-only, recalculates on dependency change",
            "effect() = side effects when signals change",
            "update() and set() modify signals; mutate() for in-place changes",
            "Foundation for zoneless Angular and modern state management",
        ],
    },
    "zoneless-angular": {
        "explanation": (
            "Traditional Angular relies on **Zone.js** to monkey-patch async APIs (setTimeout, "
            "Promise, XHR) and trigger change detection after every async operation — convenient "
            "but adds overhead. **Zoneless Angular** (experimental in Angular 18+, stabilizing) "
            "removes Zone.js entirely. Change detection runs only when **signals update**, "
            "events fire, or **`ChangeDetectorRef.markForCheck()`** is called. "
            "Benefits: **smaller bundle**, **faster runtime**, **better debugging**. "
            "Requires signals, async pipe, or manual CD triggers throughout the app."
        ),
        "code": """// Enable zoneless (Angular 18+)
bootstrapApplication(AppComponent, {
  providers: [
    provideExperimentalZonelessChangeDetection(),
    provideRouter(routes),
    provideHttpClient(),
  ]
});

// Components must use signals or async pipe for updates
@Component({
  selector: 'app-dashboard',
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <h1>{{ title() }}</h1>
    @if (data$ | async; as data) {
      <app-chart [data]="data" />
    }
  `
})
export class DashboardComponent {
  title = signal('Dashboard');
  data$ = inject(DataService).getChartData(); // async pipe triggers CD
}

// Remove zone.js from polyfills in angular.json when going zoneless""",
        "language": "typescript",
        "key_points": [
            "Zone.js patches async APIs to trigger change detection automatically",
            "Zoneless removes Zone.js — signals and async pipe drive updates",
            "Smaller bundle and better performance without Zone overhead",
            "Requires OnPush + signals/async pipe throughout the app",
            "Angular's long-term direction — know the tradeoffs for interviews",
        ],
    },
    "aot-vs-jit-compilation": {
        "explanation": (
            "**JIT (Just-In-Time)** compilation happens in the **browser at runtime** — the Angular "
            "compiler ships with the app, increasing bundle size. **AOT (Ahead-Of-Time)** compilation "
            "happens at **build time** — templates are compiled to JavaScript before deployment. "
            "Production builds always use **AOT** today (faster startup, smaller bundle, template "
            "errors caught at build time). JIT is only used in **`ng serve`** development mode. "
            "AOT enables **tree-shaking** of unused components and **metadata stripping**."
        ),
        "code": """# Development — JIT (faster rebuilds, template errors in browser console)
ng serve

# Production — AOT (compiled at build time)
ng build --configuration production
# Output: dist/my-app/ — pre-compiled, tree-shaken, minified

# angular.json configuration
{
  "projects": {
    "my-app": {
      "architect": {
        "build": {
          "configurations": {
            "production": {
              "aot": true,           // always true in modern Angular
              "optimization": true,
              "buildOptimizer": true,
              "sourceMap": false
            },
            "development": {
              "aot": false,          // JIT for faster dev rebuilds
              "optimization": false
            }
          }
        }
      }
    }
  }
}""",
        "language": "bash",
        "key_points": [
            "AOT = compile templates at build time (production default)",
            "JIT = compile in browser at runtime (dev only today)",
            "AOT catches template errors before deployment",
            "AOT enables tree-shaking and smaller bundles",
            "Modern Angular CLI uses AOT for production automatically",
        ],
    },
    "dynamic-components": {
        "explanation": (
            "**Dynamic components** are created at **runtime** rather than declared in a template. "
            "Use cases: plugin systems, conditional widgets, modal content, dashboard builders. "
            "Approaches: **`ViewContainerRef.createComponent()`** (imperative API) or "
            "**`NgComponentOutlet`** (declarative directive). With standalone components, "
            "pass the component class directly — no NgModule factory needed. "
            "Always **`destroy()`** dynamic components to prevent memory leaks."
        ),
        "code": """// Imperative — ViewContainerRef.createComponent
@Component({
  selector: 'app-dashboard',
  template: `<ng-container #widgetHost />`
})
export class DashboardComponent implements OnInit {
  @ViewChild('widgetHost', { read: ViewContainerRef }) host!: ViewContainerRef;

  ngOnInit() {
    const widgetType = this.configService.getWidgetType(); // 'chart' | 'table'
    const component = widgetType === 'chart' ? ChartWidget : TableWidget;
    this.host.clear();
    const ref = this.host.createComponent(component);
    ref.setInput('data', this.dashboardData); // pass inputs
  }
}

// Declarative — NgComponentOutlet
@Component({
  imports: [NgComponentOutlet],
  template: `<ng-container *ngComponentOutlet="activeWidget; inputs: widgetInputs" />`
})
export class DynamicHostComponent {
  activeWidget = ChartWidget;
  widgetInputs = { data: this.chartData };
}""",
        "language": "typescript",
        "key_points": [
            "ViewContainerRef.createComponent() for imperative loading",
            "NgComponentOutlet for declarative dynamic rendering",
            "Standalone components simplify dynamic loading (no module factory)",
            "setInput() passes data; destroy ref on cleanup",
            "Use cases: dashboards, plugins, modals, tab content",
        ],
    },
    "angular-error-handler": {
        "explanation": (
            "Angular's global **`ErrorHandler`** catches unhandled errors across the app — "
            "template errors, HTTP failures not caught locally, and runtime exceptions. "
            "Replace the default handler to **log to Application Insights**, show user-friendly "
            "toast messages, or redirect to an error page. Combine with **HTTP interceptors** "
            "for API errors and component-level `try/catch` for expected failures. "
            "Enterprise apps always implement a custom ErrorHandler integrated with monitoring."
        ),
        "code": """@Injectable()
export class GlobalErrorHandler implements ErrorHandler {
  private logger = inject(LoggingService);
  private toast = inject(ToastService);

  handleError(error: Error): void {
    // Log to Application Insights / Sentry
    this.logger.error('Unhandled error', {
      message: error.message,
      stack: error.stack,
      timestamp: new Date().toISOString(),
    });

    // User-friendly notification
    this.toast.error('Something went wrong. Please try again.');

    // Re-throw in dev for console visibility
    if (!environment.production) throw error;
  }
}

// Register in bootstrap
bootstrapApplication(AppComponent, {
  providers: [
    { provide: ErrorHandler, useClass: GlobalErrorHandler },
  ]
});""",
        "language": "typescript",
        "key_points": [
            "ErrorHandler catches all unhandled errors app-wide",
            "Integrate with Application Insights, Sentry, or similar",
            "Show user-friendly messages — never expose stack traces in prod",
            "Combine with HTTP interceptors for API error handling",
            "Re-throw in development for debugging",
        ],
    },
    "angular-pwa-service-worker": {
        "explanation": (
            "**Progressive Web Apps (PWA)** make Angular apps installable and work offline. "
            "**`ng add @angular/pwa`** configures a **service worker** that caches static assets "
            "and API responses. The **`ngsw-config.json`** file defines caching strategies: "
            "**prefetch** (install time), **lazy** (first request), **freshness** (network first). "
            "Service workers enable **push notifications**, **background sync**, and **app install prompts**. "
            "Common in enterprise mobile-first apps and field service applications."
        ),
        "code": """# Add PWA support
ng add @angular/pwa

# ngsw-config.json — caching strategy
{
  "index": "/index.html",
  "assetGroups": [{
    "name": "app",
    "installMode": "prefetch",
    "resources": { "files": ["/favicon.ico", "/index.html", "/*.css", "/*.js"] }
  }, {
    "name": "assets",
    "installMode": "lazy",
    "updateMode": "prefetch",
    "resources": { "files": ["/assets/**"] }
  }],
  "dataGroups": [{
    "name": "api-cache",
    "urls": ["/api/lookups/**"],
    "cacheConfig": { "maxSize": 100, "maxAge": "1h", "strategy": "freshness" }
  }]
}

// app.config.ts — register service worker
provideServiceWorker('ngsw-worker.js', {
  enabled: !isDevMode(),
  registrationStrategy: 'registerWhenStable:30000'
})""",
        "language": "yaml",
        "key_points": [
            "ng add @angular/pwa scaffolds service worker + manifest",
            "ngsw-config.json controls asset and API caching strategies",
            "prefetch = cache at install; lazy = cache on first request",
            "Service worker only active in production builds",
            "Enables offline access, install prompts, push notifications",
        ],
    },
    "typescript-decorators": {
        "explanation": (
            "**Decorators** are special declarations that attach **metadata** to classes, methods, "
            "properties, or parameters. Angular relies heavily on decorators: **`@Component`** "
            "(template, selector, styles), **`@Injectable`** (DI scope), **`@Input`/`@Output`** "
            "(component API), **`@HostListener`/`@HostBinding`**. The Angular compiler reads "
            "this metadata at compile time to generate factory functions and injection tokens. "
            "TypeScript 5+ supports **ECMAScript standard decorators** — Angular is migrating to them."
        ),
        "code": """// @Component — defines component metadata
@Component({
  selector: 'app-order-card',       // HTML tag: <app-order-card>
  standalone: true,
  templateUrl: './order-card.html',
  styleUrl: './order-card.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class OrderCardComponent {
  @Input({ required: true }) order!: Order;  // parent passes data in
  @Output() selected = new EventEmitter<Order>(); // child sends events out
}

// @Injectable — marks class for DI
@Injectable({ providedIn: 'root' })  // singleton at root injector
export class OrderService {
  constructor(private http: HttpClient) {} // parameter decorator for injection
}

// Custom property decorator (advanced)
function Log() {
  return (target: any, key: string) => {
    console.log(`Property ${key} defined on ${target.constructor.name}`);
  };
}""",
        "language": "typescript",
        "key_points": [
            "Decorators attach metadata read by Angular compiler",
            "@Component, @Injectable, @Input, @Output are core Angular decorators",
            "providedIn: 'root' makes service app-wide singleton",
            "Experimental decorators today; ES standard decorators coming",
            "Compiler uses metadata to generate factories and injection",
        ],
    },
    "angular-performance": {
        "explanation": (
            "Angular performance optimization is a **frequent senior-level interview topic**. "
            "Key techniques: **`ChangeDetectionStrategy.OnPush`** (check only on input change/events), "
            "**`trackBy`** in lists, **lazy loaded routes** (smaller initial bundle), "
            "**`@defer` blocks** (defer component rendering), **pure pipes** (memoized), "
            "**Virtual Scroll** (CDK for large lists), **signals** (fine-grained updates), "
            "**tree-shaking** (remove unused code), and **avoiding unnecessary subscriptions**. "
            "Measure with **Angular DevTools** and Chrome Performance profiler before optimizing."
        ),
        "code": """// 1. OnPush — skip unnecessary checks
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `@for (item of items(); track item.id) { <app-row [data]="item" /> }`
})
export class OptimizedListComponent {
  items = signal<Item[]>([]); // signal triggers CD on change
}

// 2. @defer — load heavy component only when visible
@Component({
  template: `
    @defer (on viewport) {
      <app-heavy-chart [data]="chartData" />
    } @placeholder {
      <div class="skeleton">Loading chart...</div>
    }
  `
})
export class DashboardComponent {}

// 3. Lazy route — separate bundle
{ path: 'reports', loadComponent: () => import('./reports.component') }""",
        "language": "typescript",
        "key_points": [
            "OnPush + signals = biggest change detection win",
            "trackBy / @for track prevents list re-render",
            "Lazy routes and @defer reduce initial bundle size",
            "Virtual Scroll for 1000+ item lists",
            "Profile before optimizing — Angular DevTools + Chrome",
        ],
    },
    "angular-i18n": {
        "explanation": (
            "Angular **i18n** (internationalization) marks translatable strings in templates with "
            "the **`i18n` attribute**, extracts them to XLIFF/JSON files, and builds **separate "
            "locale bundles** per language. Runtime locale switching requires rebuilding or "
            "loading locale-specific bundles. For **runtime i18n** without rebuild, libraries like "
            "**ngx-translate** load JSON translation files dynamically. Enterprise global apps "
            "typically support 5–20 locales with date/number/currency formatting via **`LOCALE_ID`**."
        ),
        "code": """// Mark strings for translation in template
@Component({
  template: `
    <h1 i18n="@@pageTitle">Order Management</h1>
    <p i18n="@@welcomeMsg">Welcome, {{ userName }}!</p>
    <button i18n="@@saveBtn">Save Order</button>
    <p>{{ orderDate | date:'mediumDate' }}</p> <!-- locale-aware formatting -->
  `
})
export class OrdersComponent {}

# Extract messages to XLIFF file
ng extract-i18n --output-path src/locale --format xlf

# Build for specific locale
ng build --configuration production --localize
# Produces: dist/my-app/en/, dist/my-app/fr/, dist/my-app/de/

# angular.json — define locales
"i18n": {
  "sourceLocale": "en-US",
  "locales": { "fr": "src/locale/messages.fr.xlf", "de": "src/locale/messages.de.xlf" }
}""",
        "language": "typescript",
        "key_points": [
            "i18n attribute marks translatable strings in templates",
            "ng extract-i18n generates XLIFF translation files",
            "Build per locale with --localize flag",
            "Date/number/currency pipes are locale-aware automatically",
            "ngx-translate for runtime switching without rebuild",
        ],
    },
    "angular-vs-react": {
        "explanation": (
            "This comparison question appears in almost every full-stack interview. "
            "**Angular** is a **complete framework** — includes DI, routing, forms, HTTP, "
            "testing utilities, and CLI out of the box. Opinionated structure suits **large "
            "enterprise teams**. **React** is a **UI library** — you choose routing (React Router), "
            "state (Redux/Zustand), forms (React Hook Form), and HTTP (fetch/axios) separately. "
            "React has a larger ecosystem and job market; Angular excels in **enterprise .NET shops**, "
            "banking, and government where structure and TypeScript-first matter."
        ),
        "code": """// Angular — batteries included, opinionated structure
@Component({
  selector: 'app-orders',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `@for (o of orders(); track o.id) { <a [routerLink]="['/orders', o.id]">{{ o.name }}</a> }`
})
export class OrdersComponent {
  orders = signal<Order[]>([]);
  constructor(private http: HttpClient) {} // DI built-in
}

// React equivalent — more choices, less structure
function Orders() {
  const [orders, setOrders] = useState<Order[]>([]);
  useEffect(() => { fetch('/api/orders').then(r => r.json()).then(setOrders); }, []);
  return orders.map(o => <Link key={o.id} to={`/orders/${o.id}`}>{o.name}</Link>);
}

// Key differences:
// Angular: TypeScript default, DI, RxJS, full CLI, .NET enterprise pairing
// React: JSX, hooks, larger ecosystem, more freelance/startup jobs""",
        "language": "typescript",
        "key_points": [
            "Angular = full framework; React = UI library + ecosystem choices",
            "Angular suits large enterprise teams (.NET shops, banking)",
            "React has larger job market and ecosystem",
            "Angular includes DI, routing, forms, HTTP out of the box",
            "Both use component-based architecture and virtual DOM concepts",
        ],
    },
}
