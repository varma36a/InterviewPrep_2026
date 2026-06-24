namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class BuilderPattern
{
    internal static void Run()
    {
        var order = new PizzaOrderBuilder()
            .ForCustomer("Rohit")
            .WithSize("Large")
            .WithCrust("Thin")
            .AddTopping("Extra Cheese")
            .AddTopping("Mushrooms")
            .AddDeliveryInstructions("Ring doorbell twice")
            .Build();
        Console.WriteLine($"Builder -> {order}");
    }
}

internal sealed class PizzaOrder
{
    public string Customer { get; set; } = string.Empty;
    public string Size { get; set; } = string.Empty;
    public string Crust { get; set; } = string.Empty;
    public List<string> Toppings { get; init; } = [];
    public string DeliveryInstructions { get; set; } = string.Empty;
    public override string ToString() =>
        $"Order for {Customer}: {Size} {Crust} crust with [{string.Join(", ", Toppings)}] | Notes: {DeliveryInstructions}";
}

internal sealed class PizzaOrderBuilder
{
    private readonly PizzaOrder _order = new();
    internal PizzaOrderBuilder ForCustomer(string name) { _order.Customer = name; return this; }
    internal PizzaOrderBuilder WithSize(string size) { _order.Size = size; return this; }
    internal PizzaOrderBuilder WithCrust(string crust) { _order.Crust = crust; return this; }
    internal PizzaOrderBuilder AddTopping(string topping) { _order.Toppings.Add(topping); return this; }
    internal PizzaOrderBuilder AddDeliveryInstructions(string notes) { _order.DeliveryInstructions = notes; return this; }
    internal PizzaOrder Build() => _order;
}
