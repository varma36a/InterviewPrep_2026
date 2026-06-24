namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class CompositePattern
{
    internal static void Run()
    {
        var menu = new MenuCategory("Tony's Pizza Menu");
        var classics = new MenuCategory("Classic Pizzas");
        classics.Add(new MenuItem("Margherita", 10.99m));
        classics.Add(new MenuItem("Pepperoni", 12.99m));
        var combos = new MenuCategory("Combo Deals");
        combos.Add(new MenuItem("Garlic Bread", 4.99m));
        combos.Add(new MenuItem("Soft Drink", 2.49m));
        menu.Add(classics);
        menu.Add(combos);
        menu.Add(new MenuItem("Family Feast Combo", 29.99m));
        menu.Display();
    }
}

internal interface IMenuComponent { void Display(int depth = 0); }
internal sealed class MenuItem(string name, decimal price) : IMenuComponent
{
    public void Display(int depth = 0) => Console.WriteLine($"{new string(' ', depth)}- {name} ({price:C})");
}
internal sealed class MenuCategory(string name) : IMenuComponent
{
    private readonly List<IMenuComponent> _items = [];
    internal void Add(IMenuComponent item) => _items.Add(item);
    public void Display(int depth = 0)
    {
        Console.WriteLine($"{new string(' ', depth)}+ {name}");
        foreach (var item in _items) item.Display(depth + 2);
    }
}
