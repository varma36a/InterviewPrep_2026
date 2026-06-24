namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class MementoPattern
{
    internal static void Run()
    {
        var builder = new PizzaCustomizer();
        builder.Toppings = "Cheese, Olives";
        var history = new CustomizationHistory();
        history.Save(builder.Save());
        builder.Toppings = "Cheese, Olives, Extra Pepperoni, Jalapeños";
        builder.Restore(history.Undo());
        Console.WriteLine($"Memento -> Restored toppings: {builder.Toppings}");
    }
}

internal sealed class PizzaMemento(string toppings) { internal string Toppings { get; } = toppings; }
internal sealed class PizzaCustomizer
{
    internal string Toppings { get; set; } = string.Empty;
    internal PizzaMemento Save() => new(Toppings);
    internal void Restore(PizzaMemento snapshot) => Toppings = snapshot.Toppings;
}
internal sealed class CustomizationHistory
{
    private readonly Stack<PizzaMemento> _history = new();
    internal void Save(PizzaMemento snapshot) => _history.Push(snapshot);
    internal PizzaMemento Undo() => _history.Pop();
}
