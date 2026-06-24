namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class SingletonPattern
{
    internal static void Run()
    {
        var menuA = PizzaShopMenu.Instance;
        var menuB = PizzaShopMenu.Instance;
        menuA.SetPrice("Margherita", 12.99m);
        Console.WriteLine($"Singleton -> Same menu instance: {ReferenceEquals(menuA, menuB)}");
        Console.WriteLine($"Margherita price via other reference: {menuB.GetPrice("Margherita"):C}");
    }
}

internal sealed class PizzaShopMenu
{
    private static readonly Lazy<PizzaShopMenu> InstanceValue = new(() => new PizzaShopMenu());
    private readonly Dictionary<string, decimal> _prices = [];
    internal static PizzaShopMenu Instance => InstanceValue.Value;
    private PizzaShopMenu() { }
    internal void SetPrice(string pizzaName, decimal price) => _prices[pizzaName] = price;
    internal decimal GetPrice(string pizzaName) => _prices.TryGetValue(pizzaName, out var price) ? price : 0m;
}
