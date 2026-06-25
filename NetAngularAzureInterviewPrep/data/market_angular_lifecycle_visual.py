"""Dedicated Angular lifecycle hooks topic with visual SVG diagrams."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("frontend", "foundation"): [
        InterviewItem(
            "angular-lifecycle-hooks-visual",
            "Angular Component Lifecycle Hooks — Complete Visual Guide",
            "Visual walkthrough of every lifecycle hook from creation to destruction.",
            "",
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "angular-lifecycle-hooks-visual": {
        "explanation": (
            "Every Angular component passes through **three phases**: **Creation**, **Update**, and "
            "**Destruction**. Angular exposes **lifecycle hooks** — methods you implement to run code "
            "at each stage.\n\n"
            "Use the **visual diagrams below** as your interview cheat sheet. In most interviews you "
            "must explain **`ngOnInit`**, **`ngOnChanges`**, **`ngAfterViewInit`**, and **`ngOnDestroy`** "
            "with a real example.\n\n"
            "**Creation phase** — Angular instantiates the class, binds `@Input`s, renders the template, "
            "and initializes child views.\n\n"
            "**Update phase** — runs on every change detection cycle when inputs change, events fire, "
            "Observables emit (async pipe), or signals update.\n\n"
            "**Destruction phase** — when the component is removed from the DOM (`*ngIf` false, route "
            "navigate away). Always clean up here."
        ),
        "images": [
            "assets/angular/lifecycle-timeline.svg",
            "assets/angular/lifecycle-phases.svg",
            "assets/angular/lifecycle-hooks-usage.svg",
        ],
        "code": """@Component({
  selector: 'app-order-detail',
  template: `
    <h2>Order #{{ order?.id }}</h2>
    <canvas #chart></canvas>
  `,
})
export class OrderDetailComponent
  implements OnChanges, OnInit, AfterViewInit, OnDestroy {

  @Input({ required: true }) orderId!: number;
  @ViewChild('chart') chartRef!: ElementRef<HTMLCanvasElement>;

  private destroy$ = new Subject<void>();
  order: Order | null = null;

  // 1️⃣ ngOnChanges — parent changed @Input
  ngOnChanges(changes: SimpleChanges): void {
    if (changes['orderId'] && !changes['orderId'].firstChange) {
      this.fetchOrder(this.orderId);
    }
  }

  // 2️⃣ ngOnInit — one-time initialization
  ngOnInit(): void {
    this.fetchOrder(this.orderId);
    this.orderService.liveUpdates$
      .pipe(takeUntil(this.destroy$))
      .subscribe(o => (this.order = o));
  }

  // 3️⃣ ngAfterViewInit — DOM / ViewChild ready
  ngAfterViewInit(): void {
    this.renderChart(this.chartRef.nativeElement, this.order);
  }

  // 4️⃣ ngOnDestroy — cleanup
  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }

  private fetchOrder(id: number): void {
    this.orderService.getById(id).subscribe(o => (this.order = o));
  }
}""",
        "language": "typescript",
        "key_points": [
            "Creation → Update → Destruction — know the order",
            "ngOnInit: setup once; ngOnChanges: react to @Input",
            "ngAfterViewInit: ViewChild/DOM ready; ngOnDestroy: unsubscribe",
            "Modern apps also use signals/effects — hooks still apply for DOM & cleanup",
        ],
    },
}
