"""Design Patterns section — 23 GoF patterns + SOLID with code from DesignPatternsLearnignFolder."""

from data.design_patterns_loader import load_sources, patterns_project_hint
from data.interview_content import InterviewItem, Phase, Section

# Each entry: id, question, phase_id, source files, explanation, key_points, run_name (optional)
_PATTERN_DEFS: list[dict] = [
    # ── Creational (GoF) ──────────────────────────────────────────────────────
    {
        "id": "gof-singleton",
        "phase": "creational",
        "question": "What is the Singleton pattern? When should you use it?",
        "files": ["Patterns/Creational/SingletonPattern.cs"],
        "run": "singleton",
        "explanation": (
            "The **Singleton** pattern guarantees **one shared instance** of a class for the entire application. "
            "In the pizza shop demo, `PizzaShopMenu.Instance` holds the single menu/pricing catalog — every reference "
            "points to the same object (`ReferenceEquals` returns true). Modern C# uses **`Lazy<T>`** for thread-safe "
            "initialization. **Use when:** exactly one coordinator is required (config, cache, logger factory). "
            "**Avoid when:** you need testability — Singleton hides dependencies and complicates unit tests; prefer DI-scoped "
            "services in ASP.NET Core. **Interview tip:** mention double-checked locking vs `Lazy<T>` vs DI singleton lifetime."
        ),
        "key_points": [
            "One instance app-wide — shared state (menu, config)",
            "Private constructor + static Instance accessor",
            "Lazy<T> is thread-safe in modern C#",
            "ASP.NET Core AddSingleton is preferred over hand-rolled Singleton",
            "Run: dotnet run -- singleton",
        ],
    },
    {
        "id": "gof-factory-method",
        "phase": "creational",
        "question": "Explain the Factory Method pattern with an example.",
        "files": ["Patterns/Creational/FactoryMethodPattern.cs"],
        "run": "factory",
        "explanation": (
            "**Factory Method** defines an interface for creating objects but lets subclasses or static factories "
            "decide which concrete type to instantiate. `PizzaFactory.Create(\"margherita\")` returns `IPizza` without "
            "the caller knowing the concrete class. **Problem solved:** avoids `new` scattered everywhere and "
            "centralizes creation logic. **When to use:** product type is chosen at runtime from a fixed set. "
            "Differs from **Abstract Factory** (families of related products) and **Simple Factory** (one static method, not GoF)."
        ),
        "key_points": [
            "Encapsulates object creation behind a factory",
            "Returns interface/abstraction — caller decoupled from concrete type",
            "Switch/strategy on type key is common simple factory",
            "Open for new pizza types by extending factory",
            "Run: dotnet run -- factory",
        ],
    },
    {
        "id": "gof-abstract-factory",
        "phase": "creational",
        "question": "What is the Abstract Factory pattern?",
        "files": ["Patterns/Creational/AbstractFactoryPattern.cs"],
        "run": "abstractfactory",
        "explanation": (
            "**Abstract Factory** creates **families of related objects** without specifying concrete classes. "
            "The pizza demo uses NY-style vs Chicago-style factories — each produces matching **crust + sauce** pairs "
            "that belong together. **When to use:** UI themes, cross-platform widget sets, database provider families. "
            "**Benefit:** client code depends only on abstract interfaces; swapping entire product family is one line change."
        ),
        "key_points": [
            "Creates families of related products (crust + sauce)",
            "Client uses abstract factory interface only",
            "Swap NY vs Chicago factory to change entire style",
            "Heavier than Factory Method — use when products are grouped",
            "Run: dotnet run -- abstractfactory",
        ],
    },
    {
        "id": "gof-builder",
        "phase": "creational",
        "question": "How does the Builder pattern help construct complex objects?",
        "files": ["Patterns/Creational/BuilderPattern.cs"],
        "run": "builder",
        "explanation": (
            "**Builder** separates **step-by-step construction** from the final representation. "
            "Pizza orders are built incrementally: size → crust → toppings → special instructions. "
            "Fluent chaining (`order.WithSize().WithCrust().AddTopping()`) keeps constructors readable. "
            "**When to use:** many optional parameters, immutable objects, or complex validation during build. "
            "In .NET, `StringBuilder`, `HostApplicationBuilder`, and EF model builders follow this pattern."
        ),
        "key_points": [
            "Step-by-step assembly — avoids telescoping constructors",
            "Fluent API with method chaining is common",
            "Director optional — client can orchestrate steps",
            "Same construction process, different representations",
            "Run: dotnet run -- builder",
        ],
    },
    {
        "id": "gof-prototype",
        "phase": "creational",
        "question": "What is the Prototype pattern and when use it?",
        "files": ["Patterns/Creational/PrototypePattern.cs"],
        "run": "prototype",
        "explanation": (
            "**Prototype** creates new objects by **cloning** an existing instance instead of calling `new`. "
            "Signature pizza recipes are cloned and customized — faster than rebuilding from scratch when "
            "initialization is expensive. C# supports **`ICloneable`** or explicit `Clone()` methods; "
            "deep vs shallow copy matters for reference fields. **When to use:** object creation cost is high "
            "or when you need copies with slight variations (templates, game entities)."
        ),
        "key_points": [
            "Clone existing object as template",
            "Shallow vs deep copy — know the difference",
            "Avoid ICloneable in public APIs — prefer explicit Clone()",
            "Useful for preset configurations (signature pizzas)",
            "Run: dotnet run -- prototype",
        ],
    },
    # ── Structural (GoF) ──────────────────────────────────────────────────────
    {
        "id": "gof-adapter",
        "phase": "structural",
        "question": "Explain the Adapter pattern with a legacy integration example.",
        "files": ["Patterns/Structural/AdapterPattern.cs"],
        "run": "adapter",
        "explanation": (
            "**Adapter** converts the interface of a class into another interface clients expect — "
            "the **legacy POS terminal** is adapted to the modern `ICheckout` interface so new code "
            "doesn't depend on old APIs. **Two forms:** class adapter (inheritance) and object adapter "
            "(composition — preferred in C#). **When to use:** third-party libraries, legacy SOAP/WCF, "
            "payment gateways with incompatible interfaces."
        ),
        "key_points": [
            "Wraps incompatible interface to match expected contract",
            "Object adapter (composition) preferred in C#",
            "Common for legacy system integration",
            "Does not change original class — wraps it",
            "Run: dotnet run -- adapter",
        ],
    },
    {
        "id": "gof-bridge",
        "phase": "structural",
        "question": "What problem does the Bridge pattern solve?",
        "files": ["Patterns/Structural/BridgePattern.cs"],
        "run": "bridge",
        "explanation": (
            "**Bridge** decouples an **abstraction** from its **implementation** so both can vary independently. "
            "Pizza orders (abstraction) are separated from fulfillment channel (pickup vs delivery implementation). "
            "Avoids class explosion from combining every order type × every channel in one hierarchy. "
            "**When to use:** two dimensions of variation — UI platform × renderer, shape × drawing API."
        ),
        "key_points": [
            "Abstraction + Implementor — vary independently",
            "Avoids cartesian product of subclasses",
            "Composition over inheritance for implementation",
            "Order type decoupled from delivery channel in demo",
            "Run: dotnet run -- bridge",
        ],
    },
    {
        "id": "gof-composite",
        "phase": "structural",
        "question": "How does the Composite pattern treat individual and group objects uniformly?",
        "files": ["Patterns/Structural/CompositePattern.cs"],
        "run": "composite",
        "explanation": (
            "**Composite** composes objects into **tree structures** and lets clients treat individual objects "
            "and compositions **uniformly**. The menu tree has categories, items, and combo deals — all implement "
            "`IMenuComponent` with `Display()` and price calculation. **When to use:** file systems, org charts, "
            "UI component trees, nested menu structures."
        ),
        "key_points": [
            "Leaf and Composite share common interface",
            "Tree structure — recurse through children",
            "Client code doesn't distinguish single vs group",
            "Menu categories + items + combos in demo",
            "Run: dotnet run -- composite",
        ],
    },
    {
        "id": "gof-decorator",
        "phase": "structural",
        "question": "Explain the Decorator pattern vs subclassing for adding behavior.",
        "files": ["Patterns/Structural/DecoratorPattern.cs"],
        "run": "decorator",
        "explanation": (
            "**Decorator** attaches **additional responsibilities** dynamically without subclass explosion. "
            "Extra cheese and pepperoni wrap a `BasePizza` — each decorator implements `IPizzaOrder` and "
            "delegates to the inner pizza. **vs Subclassing:** 2^n topping combinations would need 2^n classes; "
            "decorators stack arbitrarily. **Real .NET:** `Stream` wrappers (`BufferedStream`, `GZipStream`), "
            "ASP.NET Core middleware pipeline follows decorator chain pattern."
        ),
        "key_points": [
            "Wrap object — same interface, add behavior",
            "Stack multiple decorators (cheese + pepperoni)",
            "Avoids combinatorial subclass explosion",
            "Stream wrappers are classic .NET decorators",
            "Run: dotnet run -- decorator",
        ],
    },
    {
        "id": "gof-facade",
        "phase": "structural",
        "question": "What is the Facade pattern and when use it in APIs?",
        "files": ["Patterns/Structural/FacadePattern.cs"],
        "run": "facade",
        "explanation": (
            "**Facade** provides a **unified simplified interface** to a complex subsystem. "
            "`PlaceOrder` hides validate → kitchen → payment → delivery steps behind one call. "
            "**When to use:** reduce coupling for clients, legacy subsystem wrappers, service orchestration. "
            "**Not the same as** God class — facade delegates, doesn't implement everything itself."
        ),
        "key_points": [
            "Single entry point to complex subsystem",
            "Does not add new functionality — simplifies access",
            "PlaceOrder orchestrates multiple services",
            "Common in application services / orchestrators",
            "Run: dotnet run -- facade",
        ],
    },
    {
        "id": "gof-flyweight",
        "phase": "structural",
        "question": "Explain the Flyweight pattern for memory optimization.",
        "files": ["Patterns/Structural/FlyweightPattern.cs"],
        "run": "flyweight",
        "explanation": (
            "**Flyweight** shares **intrinsic state** across many objects to reduce memory. "
            "Topping definitions (name, base price) are shared instances; each order stores only "
            "extrinsic state (quantity, order id). **When to use:** thousands of similar objects "
            "(characters in editor, map tiles, repeated icons). **Trade-off:** complexity vs memory."
        ),
        "key_points": [
            "Share immutable intrinsic state (topping metadata)",
            "Extrinsic state stored per context (quantity)",
            "Factory/cache for flyweight instances",
            "Memory optimization for large object counts",
            "Run: dotnet run -- flyweight",
        ],
    },
    {
        "id": "gof-proxy",
        "phase": "structural",
        "question": "What is the Proxy pattern? Compare with Decorator.",
        "files": ["Patterns/Structural/ProxyPattern.cs"],
        "run": "proxy",
        "explanation": (
            "**Proxy** provides a **surrogate or placeholder** controlling access to another object. "
            "The demo uses **role-gated access** to the premium menu — proxy checks permissions before delegating. "
            "**Types:** virtual proxy (lazy load), protection proxy (auth), remote proxy (RPC). "
            "**vs Decorator:** proxy controls access; decorator adds behavior. Both wrap an object with same interface."
        ),
        "key_points": [
            "Controls access — lazy load, auth, logging",
            "Same interface as real subject",
            "Protection proxy gates premium menu in demo",
            "Decorator adds behavior; proxy manages access",
            "Run: dotnet run -- proxy",
        ],
    },
    # ── Behavioral (GoF) ─────────────────────────────────────────────────────
    {
        "id": "gof-chain-of-responsibility",
        "phase": "behavioral",
        "question": "How does Chain of Responsibility route requests?",
        "files": ["Patterns/Behavioral/ChainOfResponsibilityPattern.cs"],
        "run": "chain",
        "explanation": (
            "**Chain of Responsibility** passes a request along a **chain of handlers** until one handles it. "
            "Order issues escalate: cashier → kitchen → manager. Each handler either processes or forwards to `_next`. "
            "**When to use:** logging pipelines, middleware, approval workflows, exception handling chains. "
            "ASP.NET Core middleware is a chain of responsibility."
        ),
        "key_points": [
            "Handlers linked in chain — pass or process",
            "Sender decoupled from specific handler",
            "Middleware pipeline is CoR in ASP.NET Core",
            "Escalation: cashier → kitchen → manager",
            "Run: dotnet run -- chain",
        ],
    },
    {
        "id": "gof-command",
        "phase": "behavioral",
        "question": "Explain the Command pattern for undo and queuing.",
        "files": ["Patterns/Behavioral/CommandPattern.cs"],
        "run": "command",
        "explanation": (
            "**Command** encapsulates a request as an **object** — enabling queue, log, undo, and redo. "
            "`PlaceOrderCommand` and `CancelOrderCommand` implement `ICommand.Execute()`. "
            "**When to use:** job queues, transaction logs, UI actions with undo, CQRS command side. "
            "MediatR `IRequest` in .NET is command pattern applied."
        ),
        "key_points": [
            "Encapsulate action as object with Execute()",
            "Enables undo/redo and command queues",
            "Invoker decoupled from receiver",
            "MediatR IRequest is Command pattern",
            "Run: dotnet run -- command",
        ],
    },
    {
        "id": "gof-interpreter",
        "phase": "behavioral",
        "question": "What is the Interpreter pattern?",
        "files": ["Patterns/Behavioral/InterpreterPattern.cs"],
        "run": "interpreter",
        "explanation": (
            "**Interpreter** defines a grammar for language/expressions and interprets sentences. "
            "Promo rules combine conditions: order total AND loyalty membership — each rule is an "
            "expression node with `Interpret()` method. **When to use:** simple DSLs, rule engines, "
            "query filters. **Rare in interviews** but know it for completeness; overkill for complex grammars (use parser generators)."
        ),
        "key_points": [
            "Expression tree with Interpret() method",
            "Composite structure for AND/OR rules",
            "Promo eligibility rules in pizza demo",
            "Simple DSLs only — complex grammars need parsers",
            "Run: dotnet run -- interpreter",
        ],
    },
    {
        "id": "gof-iterator",
        "phase": "behavioral",
        "question": "How does the Iterator pattern traverse collections?",
        "files": ["Patterns/Behavioral/IteratorPattern.cs"],
        "run": "iterator",
        "explanation": (
            "**Iterator** provides sequential access to collection elements **without exposing internal structure**. "
            "Walk the pizza menu with `IEnumerator`/`IEnumerable` — C# **`foreach`** is syntactic sugar for iterator. "
            "**When to use:** custom collections, hide backing store (array vs linked list). "
            "LINQ builds on `IEnumerable` iterator pattern."
        ),
        "key_points": [
            "Sequential access without exposing internals",
            "IEnumerable + IEnumerator in C#",
            "foreach compiles to iterator calls",
            "Multiple iterators possible on same collection",
            "Run: dotnet run -- iterator",
        ],
    },
    {
        "id": "gof-mediator",
        "phase": "behavioral",
        "question": "What is the Mediator pattern? How relates to MediatR?",
        "files": ["Patterns/Behavioral/MediatorPattern.cs"],
        "run": "mediator",
        "explanation": (
            "**Mediator** defines an object that **encapsulates how a set of objects interact** — "
            "colleagues don't reference each other directly. Kitchen hub coordinates chef and driver "
            "without them knowing about each other. **MediatR** in .NET implements mediator for CQRS. "
            "**When to use:** reduce tangled many-to-many dependencies (chat room, air traffic control)."
        ),
        "key_points": [
            "Central hub coordinates colleagues",
            "Reduces many-to-many coupling",
            "Kitchen hub in pizza demo",
            "MediatR library implements this for CQRS",
            "Run: dotnet run -- mediator",
        ],
    },
    {
        "id": "gof-memento",
        "phase": "behavioral",
        "question": "Explain the Memento pattern for undo state.",
        "files": ["Patterns/Behavioral/MementoPattern.cs"],
        "run": "memento",
        "explanation": (
            "**Memento** captures and **externalizes an object's internal state** for later restoration — "
            "undo pizza customization changes. **Originator** creates memento; **Caretaker** stores history. "
            "**When to use:** undo/redo, snapshots, game save states. **Trade-off:** memory cost for history stack."
        ),
        "key_points": [
            "Save/restore object state without exposing internals",
            "Originator, Memento, Caretaker roles",
            "Undo pizza customization in demo",
            "Stack of mementos for undo history",
            "Run: dotnet run -- memento",
        ],
    },
    {
        "id": "gof-observer",
        "phase": "behavioral",
        "question": "What is the Observer pattern? How does .NET use events?",
        "files": ["Patterns/Behavioral/ObserverPattern.cs"],
        "run": "observer",
        "explanation": (
            "**Observer** defines a **one-to-many dependency** — when order status changes, all subscribed "
            "customers are notified. `PizzaOrderTracker.Attach(customer)` and status setter notifies all. "
            "C# **events** and **`IObservable<T>`** implement observer. **When to use:** pub/sub, UI binding, "
            "domain events. **Modern .NET:** prefer domain events + MediatR or message bus for distributed systems."
        ),
        "key_points": [
            "Subject notifies observers on state change",
            "C# events are built-in Observer",
            "Attach/Detach subscribers dynamically",
            "Order status notifications in demo",
            "Run: dotnet run -- observer",
        ],
    },
    {
        "id": "gof-state",
        "phase": "behavioral",
        "question": "How does the State pattern model object behavior changes?",
        "files": ["Patterns/Behavioral/StatePattern.cs"],
        "run": "state",
        "explanation": (
            "**State** lets an object **alter behavior when internal state changes** — order lifecycle: "
            "Placed → Preparing → OutForDelivery → Delivered. Each state is a class implementing `IOrderState`; "
            "context delegates transitions. **vs Strategy:** state objects know transitions; strategy is interchangeable "
            "algorithms chosen by client. **When to use:** workflow engines, order status, TCP connection states."
        ),
        "key_points": [
            "Behavior changes with internal state object",
            "State classes encapsulate transitions",
            "Order lifecycle in pizza demo",
            "vs Strategy — state drives transitions internally",
            "Run: dotnet run -- state",
        ],
    },
    {
        "id": "gof-strategy",
        "phase": "behavioral",
        "question": "Explain the Strategy pattern for swappable algorithms.",
        "files": ["Patterns/Behavioral/StrategyPattern.cs"],
        "run": "strategy",
        "explanation": (
            "**Strategy** defines a family of **interchangeable algorithms** — standard vs express delivery fee. "
            "Context holds `IDeliveryStrategy` and delegates calculation; swap at runtime or via DI. "
            "**When to use:** payment methods, tax calculation, sorting algorithms, compression codecs. "
            "Primary pattern behind **dependency injection** — inject `IShippingCalculator` implementation."
        ),
        "key_points": [
            "Encapsulate algorithms behind common interface",
            "Swap at runtime without changing context",
            "Delivery fee strategies in demo",
            "DI injects strategy implementations",
            "Run: dotnet run -- strategy",
        ],
    },
    {
        "id": "gof-template-method",
        "phase": "behavioral",
        "question": "What is the Template Method pattern?",
        "files": ["Patterns/Behavioral/TemplateMethodPattern.cs"],
        "run": "template",
        "explanation": (
            "**Template Method** defines the **skeleton of an algorithm** in a base class, letting subclasses "
            "override specific steps without changing structure. Pizza-making flow: prepare dough → add sauce → "
            "add toppings → bake — NY and Chicago styles override individual steps. **When to use:** shared workflow "
            "with customizable hooks. **Related:** Hollywood Principle — \"don't call us, we'll call you.\""
        ),
        "key_points": [
            "Base class defines algorithm skeleton",
            "Virtual/abstract hooks for customization",
            "NY vs Chicago override pizza-making steps",
            "Inversion of control — base calls subclass hooks",
            "Run: dotnet run -- template",
        ],
    },
    {
        "id": "gof-visitor",
        "phase": "behavioral",
        "question": "When would you use the Visitor pattern?",
        "files": ["Patterns/Behavioral/VisitorPattern.cs"],
        "run": "visitor",
        "explanation": (
            "**Visitor** lets you **add new operations** to object structures **without changing their classes** — "
            "price audit across pizzas and drinks via `Accept(IVisitor)`. **Double dispatch:** element accepts visitor, "
            "visitor dispatches on element type. **When to use:** compiler AST walks, export/reporting on stable hierarchies. "
            "**Trade-off:** adding new element types requires updating all visitors."
        ),
        "key_points": [
            "Add operations without modifying element classes",
            "Double dispatch — Accept(visitor) + Visit(element)",
            "Price audit across menu items in demo",
            "Hard to add new element types later",
            "Run: dotnet run -- visitor",
        ],
    },
    # ── SOLID (bird domain demos) ─────────────────────────────────────────────
    {
        "id": "solid-single-responsibility",
        "phase": "solid",
        "question": "Explain the Single Responsibility Principle (SRP) with code.",
        "files": [
            "Patterns/SolidPrinciples.Bird/S_SingleResponsibility/SingleResponsibilityDemo.cs",
            "Patterns/SolidPrinciples.Bird/S_SingleResponsibility/BirdDietPlanner.cs",
            "Patterns/SolidPrinciples.Bird/S_SingleResponsibility/BirdHabitatReporter.cs",
        ],
        "run": "srp",
        "explanation": (
            "**SRP:** a class should have **one reason to change** — one job. `BirdDietPlanner` plans meals; "
            "`BirdHabitatReporter` describes habitat — not one god class doing both. **Why:** smaller classes, "
            "easier testing, isolated changes. **Interview tip:** SRP is about **cohesion**, not \"one method only\" — "
            "a repository class has one job: persistence."
        ),
        "key_points": [
            "One reason to change — one responsibility",
            "BirdDietPlanner vs BirdHabitatReporter split",
            "Not one method — one cohesive purpose",
            "Easier unit testing and maintenance",
            "Source: SolidPrinciples.Bird project",
        ],
    },
    {
        "id": "solid-open-closed",
        "phase": "solid",
        "question": "Explain the Open/Closed Principle (OCP) with code.",
        "files": [
            "Patterns/SolidPrinciples.Bird/O_OpenClosed/OpenClosedDemo.cs",
            "Patterns/SolidPrinciples.Bird/O_OpenClosed/IBirdCallClassifier.cs",
            "Patterns/SolidPrinciples.Bird/O_OpenClosed/RobinCallClassifier.cs",
        ],
        "run": "ocp",
        "explanation": (
            "**OCP:** software entities should be **open for extension, closed for modification**. "
            "Add new bird call classifiers (`OwlCallClassifier`) without editing `BirdCallOrchestrator`. "
            "Achieved via **interfaces + DI** — register new implementations. **Interview tip:** strategy pattern "
            "and plugin architectures embody OCP."
        ),
        "key_points": [
            "Extend behavior without modifying existing code",
            "New IBirdCallClassifier implementations plug in",
            "Orchestrator unchanged when adding owl/robin rules",
            "Interfaces + DI enable OCP in .NET",
            "Source: SolidPrinciples.Bird project",
        ],
    },
    {
        "id": "solid-liskov-substitution",
        "phase": "solid",
        "question": "Explain the Liskov Substitution Principle (LSP) with code.",
        "files": [
            "Patterns/SolidPrinciples.Bird/L_LiskovSubstitution/LiskovSubstitutionDemo.cs",
            "Patterns/SolidPrinciples.Bird/L_LiskovSubstitution/LiskovViolationExample.cs",
        ],
        "run": "lsp",
        "explanation": (
            "**LSP:** subtypes must be **substitutable** for base types without breaking behavior. "
            "If `Penguin : IBird` throws on `Fly()`, callers expecting `IBird` break — classic violation. "
            "Demo shows correct locomotion abstractions vs violation. **Interview tip:** favor **small focused "
            "interfaces** over deep inheritance trees that force invalid overrides."
        ),
        "key_points": [
            "Subtypes must honor base type contract",
            "No surprising exceptions or weakened preconditions",
            "Penguin/Fly is classic LSP violation example",
            "Prefer composition and segregated interfaces",
            "Source: SolidPrinciples.Bird project",
        ],
    },
    {
        "id": "solid-interface-segregation",
        "phase": "solid",
        "question": "Explain the Interface Segregation Principle (ISP) with code.",
        "files": [
            "Patterns/SolidPrinciples.Bird/I_InterfaceSegregation/InterfaceSegregationDemo.cs",
            "Patterns/SolidPrinciples.Bird/I_InterfaceSegregation/BirdCapabilities.cs",
        ],
        "run": "isp",
        "explanation": (
            "**ISP:** clients should not depend on methods they don't use — **split fat interfaces**. "
            "Bird capabilities split into `IFlyable`, `ISwimmable`, `ISings` — sparrow implements fly+sing, "
            "duck implements all three. **Avoid:** `IBird` with Fly/Swim/Sing forcing empty NotSupported implementations."
        ),
        "key_points": [
            "Small focused interfaces over god interfaces",
            "IFlyable, ISwimmable, ISings segregated",
            "Classes implement only relevant interfaces",
            "Easier mocking and clearer contracts",
            "Source: SolidPrinciples.Bird project",
        ],
    },
    {
        "id": "solid-dependency-inversion",
        "phase": "solid",
        "question": "Explain the Dependency Inversion Principle (DIP) with code.",
        "files": [
            "Patterns/SolidPrinciples.Bird/D_DependencyInversion/DependencyInversionDemo.cs",
            "Patterns/SolidPrinciples.Bird/D_DependencyInversion/Abstractions.cs",
            "Patterns/SolidPrinciples.Bird/D_DependencyInversion/BirdSanctuaryService.cs",
        ],
        "run": "dip",
        "explanation": (
            "**DIP:** high-level modules depend on **abstractions**, not concretions. "
            "`BirdSanctuaryService` depends on `IBirdCatalogRepository` and `IBirdAlertNotifier` — "
            "swap in-memory vs SQL repository in tests without changing service code. "
            "**Foundation of DI** in ASP.NET Core — register interfaces in `Program.cs`."
        ),
        "key_points": [
            "Depend on abstractions (interfaces), not concrete classes",
            "High-level BirdSanctuaryService decoupled from storage",
            "Enables testing with fake repositories",
            "ASP.NET Core DI container implements DIP",
            "Source: SolidPrinciples.Bird project",
        ],
    },
    {
        "id": "gof-patterns-overview",
        "phase": "creational",
        "question": "How do I run all design pattern demos in this project?",
        "files": ["Program.cs", "Patterns/Shared/PatternRunner.cs"],
        "run": "all",
        "explanation": (
            "All **23 GoF patterns** plus **SOLID bird demos** live in **`DesignPatternsLearnignFolder`** — "
            "a runnable .NET console app using **Tony's Pizza Shop** domain for patterns and **bird sanctuary** for SOLID. "
            f"{patterns_project_hint()} "
            "Use `-- help` to list pattern names, `-- creational` for a category, or `-- singleton builder observer` for multiple."
        ),
        "key_points": [
            "23 GoF patterns — pizza shop unified domain",
            "SOLID demos in SolidPrinciples.Bird subfolder",
            "dotnet run -- <pattern-name> for single pattern",
            "dotnet run with no args runs all patterns",
            "Code in this section loaded from source files",
        ],
    },
]

_PHASE_LABELS = {
    "creational": "Creational",
    "structural": "Structural",
    "behavioral": "Behavioral",
    "solid": "SOLID Principles",
}


def _build_items() -> dict[str, list[InterviewItem]]:
    by_phase: dict[str, list[InterviewItem]] = {k: [] for k in _PHASE_LABELS}
    for p in _PATTERN_DEFS:
        code = load_sources(p["files"])
        run = p.get("run")
        if run:
            code += f"\n\n// Run this demo:\n// dotnet run --project DesignPatternsLearnign.csproj -- {run}"
        by_phase[p["phase"]].append(
            InterviewItem(
                id=p["id"],
                question=p["question"],
                explanation=p["explanation"],
                code=code,
                language="csharp",
                key_points=p["key_points"],
            )
        )
    return by_phase


def _build_detailed() -> dict[str, dict]:
    detailed: dict[str, dict] = {}
    for p in _PATTERN_DEFS:
        code = load_sources(p["files"])
        run = p.get("run")
        if run:
            code += f"\n\n// Run: dotnet run --project DesignPatternsLearnign.csproj -- {run}"
        detailed[p["id"]] = {
            "explanation": p["explanation"],
            "code": code,
            "language": "csharp",
            "key_points": p["key_points"],
        }
    return detailed


_by_phase = _build_items()

DESIGN_PATTERNS_SECTION = Section(
    id="patterns",
    title="Design Patterns",
    emoji="🏗️",
    color="#6366F1",
    subtitle="23 GoF patterns + SOLID — runnable C# from DesignPatternsLearnignFolder",
    phases=[
        Phase("creational", _PHASE_LABELS["creational"], _by_phase["creational"]),
        Phase("structural", _PHASE_LABELS["structural"], _by_phase["structural"]),
        Phase("behavioral", _PHASE_LABELS["behavioral"], _by_phase["behavioral"]),
        Phase("solid", _PHASE_LABELS["solid"], _by_phase["solid"]),
    ],
)

DESIGN_PATTERNS_DETAILED = _build_detailed()


def apply_design_patterns_section(sections: dict, detailed: dict) -> None:
    """Register Design Patterns section and detailed content."""
    sections["patterns"] = DESIGN_PATTERNS_SECTION
    detailed.update(DESIGN_PATTERNS_DETAILED)
