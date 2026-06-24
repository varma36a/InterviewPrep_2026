namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class BridgePattern
{
    internal static void Run()
    {
        PizzaOrder pickup = new TakeawayOrder(new InStorePickup());
        PizzaOrder delivery = new TakeawayOrder(new HomeDelivery());
        pickup.Fulfill("Large Pepperoni");
        delivery.Fulfill("Medium Veggie");
    }
}

internal interface IFulfillmentChannel { void Deliver(string pizzaDescription); }
internal sealed class InStorePickup : IFulfillmentChannel
{
    public void Deliver(string pizzaDescription) => Console.WriteLine($"Bridge -> {pizzaDescription} ready for in-store pickup");
}
internal sealed class HomeDelivery : IFulfillmentChannel
{
    public void Deliver(string pizzaDescription) => Console.WriteLine($"Bridge -> {pizzaDescription} dispatched for home delivery");
}

internal abstract class PizzaOrder
{
    private readonly IFulfillmentChannel _channel;
    protected PizzaOrder(IFulfillmentChannel channel) => _channel = channel;
    public void Fulfill(string pizzaDescription) => _channel.Deliver(pizzaDescription);
}
internal sealed class TakeawayOrder(IFulfillmentChannel channel) : PizzaOrder(channel);
