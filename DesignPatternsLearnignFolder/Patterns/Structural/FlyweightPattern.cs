namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class FlyweightPattern
{
    internal static void Run()
    {
        var toppingFactory = new ToppingFactory();
        var order1Pepperoni = toppingFactory.GetTopping("Pepperoni");
        var order2Pepperoni = toppingFactory.GetTopping("Pepperoni");
        var order1Mushroom = toppingFactory.GetTopping("Mushrooms");
        Console.WriteLine($"Flyweight -> Shared Pepperoni instance: {ReferenceEquals(order1Pepperoni, order2Pepperoni)}");
        Console.WriteLine($"Flyweight -> Pepperoni != Mushrooms: {!ReferenceEquals(order1Pepperoni, order1Mushroom)}");
    }
}

internal sealed class Topping(string name) { public string Name { get; } = name; }
internal sealed class ToppingFactory
{
    private readonly Dictionary<string, Topping> _toppings = [];
    internal Topping GetTopping(string name)
    {
        if (!_toppings.TryGetValue(name, out var topping))
        {
            topping = new Topping(name);
            _toppings[name] = topping;
        }
        return topping;
    }
}
