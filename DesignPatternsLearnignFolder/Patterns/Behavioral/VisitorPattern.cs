namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class VisitorPattern
{
    internal static void Run()
    {
        IMenuItem[] menu = [new PizzaItem("Margherita", 10.99m), new DrinkItem("Cola", 2.49m)];
        var priceAudit = new PriceAuditVisitor();
        foreach (var item in menu) item.Accept(priceAudit);
    }
}

internal interface IMenuVisitor { void Visit(PizzaItem pizza); void Visit(DrinkItem drink); }
internal interface IMenuItem { void Accept(IMenuVisitor visitor); }
internal sealed class PizzaItem(string name, decimal price) : IMenuItem
{
    internal string Name { get; } = name;
    internal decimal Price { get; } = price;
    public void Accept(IMenuVisitor visitor) => visitor.Visit(this);
}
internal sealed class DrinkItem(string name, decimal price) : IMenuItem
{
    internal string Name { get; } = name;
    internal decimal Price { get; } = price;
    public void Accept(IMenuVisitor visitor) => visitor.Visit(this);
}
internal sealed class PriceAuditVisitor : IMenuVisitor
{
    public void Visit(PizzaItem pizza) => Console.WriteLine($"Visitor -> Audited pizza '{pizza.Name}' at {pizza.Price:C}");
    public void Visit(DrinkItem drink) => Console.WriteLine($"Visitor -> Audited drink '{drink.Name}' at {drink.Price:C}");
}
