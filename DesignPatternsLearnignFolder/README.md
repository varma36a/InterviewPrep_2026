# C# Design Patterns — Pizza Shopping Use Case

All **23 GoF design patterns** are demonstrated through a single domain: **Tony's Pizza Shop**.  
Instead of switching between taxes, VMs, and stock markets, every example uses pizzas, orders, toppings, and delivery — so you can focus on the **pattern mechanics** and **interfaces/abstractions**.

Run all patterns:

```bash
dotnet run --project DesignPatternsLearnign.csproj
```

Run a single pattern:

```bash
dotnet run --project DesignPatternsLearnign.csproj -- singleton
dotnet run --project DesignPatternsLearnign.csproj -- factory
dotnet run --project DesignPatternsLearnign.csproj -- decorator
```

Run a whole category or multiple patterns:

```bash
dotnet run --project DesignPatternsLearnign.csproj -- creational
dotnet run --project DesignPatternsLearnign.csproj -- singleton builder observer
```

List available pattern names:

```bash
dotnet run --project DesignPatternsLearnign.csproj -- help
```

## Unified Domain Map

| Pattern | Pizza Shopping Example |
|---|---|
| **Singleton** | One shared `PizzaShopMenu` with prices |
| **Factory Method** | Create `Margherita` or `Pepperoni` pizzas |
| **Abstract Factory** | NY-style vs Chicago-style crust + sauce families |
| **Builder** | Step-by-step `PizzaOrder` (size, crust, toppings) |
| **Prototype** | Clone a `SignaturePizza` recipe |
| **Adapter** | Legacy POS terminal adapted to pizza checkout |
| **Bridge** | Order fulfillment decoupled from pickup vs delivery |
| **Composite** | Menu tree: categories, items, combo deals |
| **Decorator** | Stack extra cheese & pepperoni on a base pizza |
| **Facade** | One-call `PlaceOrder` (validate → kitchen → delivery) |
| **Flyweight** | Shared `Topping` instances across many orders |
| **Proxy** | Role-gated access to premium menu |
| **Chain of Responsibility** | Escalate order issues: cashier → kitchen → manager |
| **Command** | Queue `PlaceOrder` / `CancelOrder` commands |
| **Interpreter** | Promo rules: order total + loyalty membership |
| **Iterator** | Walk the pizza menu without exposing internals |
| **Mediator** | Kitchen hub coordinates chef & driver |
| **Memento** | Undo pizza customization changes |
| **Observer** | Notify customers when order status changes |
| **State** | Order lifecycle: Placed → Preparing → Out for Delivery → Delivered |
| **Strategy** | Swap standard vs express delivery fee algorithms |
| **Template Method** | Pizza-making skeleton with style-specific steps |
| **Visitor** | Price audit across pizzas and drinks |

## Pattern Guide (Purpose + Problem + Benefit)

### Creational

1. **Singleton** — One shared menu/pricing catalog for the whole shop.
2. **Factory Method** — Create pizza types without exposing construction details.
3. **Abstract Factory** — Produce matching crust + sauce families (NY vs Chicago).
4. **Builder** — Assemble complex orders step-by-step (size, crust, toppings).
5. **Prototype** — Clone signature pizza templates for quick customization.

### Structural

6. **Adapter** — Connect legacy POS payment to modern checkout interface.
7. **Bridge** — Separate order type from fulfillment channel (pickup vs delivery).
8. **Composite** — Treat single menu items and combo categories uniformly.
9. **Decorator** — Add toppings dynamically without subclass explosion.
10. **Facade** — Simplify ordering behind one easy API.
11. **Flyweight** — Share common topping data across thousands of orders.
12. **Proxy** — Control who can view the premium menu.

### Behavioral

13. **Chain of Responsibility** — Route customer complaints to the right handler.
14. **Command** — Encapsulate kitchen actions as queueable commands.
15. **Interpreter** — Evaluate promo eligibility with composable rules.
16. **Iterator** — Traverse the menu without knowing its internal structure.
17. **Mediator** — Centralize kitchen staff communication.
18. **Memento** — Save and restore pizza customization state.
19. **Observer** — Push order status updates to subscribed customers.
20. **State** — Model order lifecycle with isolated state objects.
21. **Strategy** — Swap delivery pricing algorithms at runtime.
22. **Template Method** — Reuse the pizza-making flow, customize each step.
23. **Visitor** — Add price audits without changing menu item classes.

## Where to look

- Entry point: `Program.cs` — runs all three demo groups.
- Creational: `Patterns/Creational/`
- Structural: `Patterns/Structural/`
- Behavioral: `Patterns/Behavioral/`

Each pattern prints labeled output (`Singleton -> ...`, `Adapter -> ...`) so you can trace behavior while running.
