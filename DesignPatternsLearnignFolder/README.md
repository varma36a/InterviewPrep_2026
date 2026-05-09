# C# Design Patterns Learning (Real-time Examples)

This folder contains runnable C# examples for all classic GoF design patterns:

- **Creational**: Singleton, Factory Method, Abstract Factory, Builder, Prototype
- **Structural**: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy
- **Behavioral**: Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor

Run:

```bash
dotnet run --project DesignPatternsLearnign.csproj
```

## Pattern Guide (Purpose + Problem + Benefit)

### Creational

1. **Singleton**
   - Purpose: Ensure only one shared instance exists.
   - Problem solved: Multiple conflicting configuration/state objects.
   - Benefit: Centralized and controlled global access.

2. **Factory Method**
   - Purpose: Create objects without exposing exact construction logic.
   - Problem solved: Conditional object creation spread across code.
   - Benefit: Cleaner creation logic and easier extension.

3. **Abstract Factory**
   - Purpose: Create related families of objects.
   - Problem solved: Mixing incompatible product variants (e.g., region-specific rules).
   - Benefit: Consistent object families and easier swapping.

4. **Builder**
   - Purpose: Build complex objects step-by-step.
   - Problem solved: Constructors with many optional parameters.
   - Benefit: Readable, flexible, and controlled construction.

5. **Prototype**
   - Purpose: Create objects by cloning existing instances.
   - Problem solved: Expensive/repetitive object creation.
   - Benefit: Faster setup and easy template duplication.

### Structural

6. **Adapter**
   - Purpose: Convert one interface to another expected by clients.
   - Problem solved: Incompatible third-party or legacy APIs.
   - Benefit: Reuse existing components without rewriting.

7. **Bridge**
   - Purpose: Decouple abstraction from implementation.
   - Problem solved: Class explosion from combining dimensions.
   - Benefit: Independent evolution of both sides.

8. **Composite**
   - Purpose: Treat individual objects and compositions uniformly.
   - Problem solved: Tree hierarchies handled with special-case logic.
   - Benefit: Simpler recursive operations on hierarchical data.

9. **Decorator**
   - Purpose: Add behavior dynamically to objects.
   - Problem solved: Subclass explosion for feature combinations.
   - Benefit: Flexible runtime feature composition.

10. **Facade**
    - Purpose: Provide a simplified interface to a subsystem.
    - Problem solved: Complex workflows with many dependencies.
    - Benefit: Easier usage and reduced coupling.

11. **Flyweight**
    - Purpose: Share common intrinsic state among many objects.
    - Problem solved: Memory overhead from repeated similar objects.
    - Benefit: Lower memory usage and better performance.

12. **Proxy**
    - Purpose: Control access to a real object.
    - Problem solved: Need for authorization, caching, lazy loading, or monitoring.
    - Benefit: Cross-cutting control without changing core object.

### Behavioral

13. **Chain of Responsibility**
    - Purpose: Pass request through handlers until one processes it.
    - Problem solved: Hardcoded if/else routing logic.
    - Benefit: Flexible request pipelines and separation of concerns.

14. **Command**
    - Purpose: Encapsulate a request as an object.
    - Problem solved: Tight coupling between invoker and receiver.
    - Benefit: Queueing, logging, undo, and macro operations.

15. **Interpreter**
    - Purpose: Evaluate grammar/rules as object expressions.
    - Problem solved: Hardcoded business rule evaluation logic.
    - Benefit: Extensible and composable rule evaluation.

16. **Iterator**
    - Purpose: Traverse collections without exposing internals.
    - Problem solved: Clients dependent on concrete data structure.
    - Benefit: Uniform and safe traversal logic.

17. **Mediator**
    - Purpose: Centralize communication between objects.
    - Problem solved: Many-to-many object dependencies.
    - Benefit: Reduced coupling and easier coordination changes.

18. **Memento**
    - Purpose: Capture and restore object state.
    - Problem solved: No safe rollback/undo mechanism.
    - Benefit: Undo support while preserving encapsulation.

19. **Observer**
    - Purpose: Notify subscribers when state changes.
    - Problem solved: Polling and tight coupling for updates.
    - Benefit: Event-driven, scalable notification flow.

20. **State**
    - Purpose: Change behavior when internal state changes.
    - Problem solved: Large state-based switch/if blocks.
    - Benefit: Cleaner state transitions and behavior isolation.

21. **Strategy**
    - Purpose: Swap algorithms at runtime.
    - Problem solved: Hardcoded algorithm selection.
    - Benefit: Open/closed design and easier testing.

22. **Template Method**
    - Purpose: Define algorithm skeleton with overridable steps.
    - Problem solved: Duplicated process flow across variants.
    - Benefit: Reuse common flow and customize specific steps.

23. **Visitor**
    - Purpose: Add external operations to object structures.
    - Problem solved: Frequent new operations requiring model changes.
    - Benefit: New behavior without modifying existing element classes.

## Where to look

- All executable implementations and demos are in `Program.cs`.
- Each pattern example prints labeled output (`Singleton -> ...`, `Adapter -> ...`) to make behavior easy to trace while running.
