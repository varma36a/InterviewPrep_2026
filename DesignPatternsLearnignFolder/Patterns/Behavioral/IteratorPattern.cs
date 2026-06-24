using System.Collections;

namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class IteratorPattern
{
    internal static void Run()
    {
        var menu = new PizzaMenu(["Margherita", "Pepperoni", "Veggie Supreme", "BBQ Chicken"]);
        foreach (var pizza in menu) Console.WriteLine($"Iterator -> Menu item: {pizza}");
    }
}

internal sealed class PizzaMenu : IEnumerable<string>
{
    private readonly List<string> _pizzas;
    internal PizzaMenu(IEnumerable<string> pizzas) => _pizzas = [.. pizzas];
    public IEnumerator<string> GetEnumerator() => _pizzas.GetEnumerator();
    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
}
