namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class StatePattern
{
    internal static void Run()
    {
        var order = new PizzaOrderContext();
        order.Next();
        order.Next();
        order.Next();
    }
}

internal interface IPizzaOrderState { void Next(PizzaOrderContext context); string Name { get; } }
internal sealed class PizzaOrderContext
{
    private IPizzaOrderState _state = new PlacedState();
    internal void Next()
    {
        _state.Next(this);
        Console.WriteLine($"State -> Order status: {_state.Name}");
    }
    internal void SetState(IPizzaOrderState state) => _state = state;
}
internal sealed class PlacedState : IPizzaOrderState
{
    public string Name => "Placed";
    public void Next(PizzaOrderContext context) => context.SetState(new PreparingState());
}
internal sealed class PreparingState : IPizzaOrderState
{
    public string Name => "Preparing";
    public void Next(PizzaOrderContext context) => context.SetState(new OutForDeliveryState());
}
internal sealed class OutForDeliveryState : IPizzaOrderState
{
    public string Name => "Out for Delivery";
    public void Next(PizzaOrderContext context) => context.SetState(new DeliveredState());
}
internal sealed class DeliveredState : IPizzaOrderState
{
    public string Name => "Delivered";
    public void Next(PizzaOrderContext context) => Console.WriteLine("State -> Order already delivered");
}
