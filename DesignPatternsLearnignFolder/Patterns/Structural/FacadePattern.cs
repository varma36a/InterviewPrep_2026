namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class FacadePattern
{
    internal static void Run()
    {
        var ordering = new PizzaOrderingFacade();
        ordering.PlaceOrder("Rohit", "Large Pepperoni");
    }
}

internal sealed class OrderValidator { internal bool Validate(string customer) { Console.WriteLine($"Facade -> Validated order for {customer}"); return true; } }
internal sealed class KitchenService { internal void Prepare(string pizza) => Console.WriteLine($"Facade -> Kitchen preparing {pizza}"); }
internal sealed class DeliveryDesk { internal void Dispatch(string customer) => Console.WriteLine($"Facade -> Delivery dispatched to {customer}"); }

internal sealed class PizzaOrderingFacade
{
    private readonly OrderValidator _validator = new();
    private readonly KitchenService _kitchen = new();
    private readonly DeliveryDesk _delivery = new();
    internal void PlaceOrder(string customer, string pizza)
    {
        if (_validator.Validate(customer))
        {
            _kitchen.Prepare(pizza);
            _delivery.Dispatch(customer);
        }
    }
}
