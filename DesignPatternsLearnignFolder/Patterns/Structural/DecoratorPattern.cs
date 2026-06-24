namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class DecoratorPattern
{
    internal static void Run()
    {
        IPizzaOrder pizza = new BasePizza("Margherita", 10.99m);
        pizza = new ExtraCheeseDecorator(pizza);
        pizza = new ExtraPepperoniDecorator(pizza);
        pizza.Describe();
    }
}

internal interface IPizzaOrder { void Describe(); }
internal sealed class BasePizza(string name, decimal basePrice) : IPizzaOrder
{
    public void Describe() => Console.WriteLine($"Decorator -> {name} base price: {basePrice:C}");
}
internal abstract class PizzaToppingDecorator(IPizzaOrder pizza) : IPizzaOrder
{
    protected readonly IPizzaOrder Pizza = pizza;
    public virtual void Describe() => Pizza.Describe();
}
internal sealed class ExtraCheeseDecorator(IPizzaOrder pizza) : PizzaToppingDecorator(pizza)
{
    public override void Describe()
    {
        Pizza.Describe();
        Console.WriteLine("Decorator -> + Extra Cheese (+$1.50)");
    }
}
internal sealed class ExtraPepperoniDecorator(IPizzaOrder pizza) : PizzaToppingDecorator(pizza)
{
    public override void Describe()
    {
        Pizza.Describe();
        Console.WriteLine("Decorator -> + Extra Pepperoni (+$2.00)");
    }
}
