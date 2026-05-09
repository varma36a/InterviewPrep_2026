namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class StatePattern
{
    internal static void Run()
    {
        var order = new OrderContext();
        order.Next();
        order.Next();
        order.Next();
    }
}

internal interface IOrderState { void Next(OrderContext context); string Name { get; } }
internal sealed class OrderContext
{
    private IOrderState _state = new CreatedState();
    internal void Next()
    {
        _state.Next(this);
        Console.WriteLine($"State -> Current: {_state.Name}");
    }
    internal void SetState(IOrderState state) => _state = state;
}
internal sealed class CreatedState : IOrderState { public string Name => "Created"; public void Next(OrderContext context) => context.SetState(new PaidState()); }
internal sealed class PaidState : IOrderState { public string Name => "Paid"; public void Next(OrderContext context) => context.SetState(new ShippedState()); }
internal sealed class ShippedState : IOrderState { public string Name => "Shipped"; public void Next(OrderContext context) => context.SetState(new DeliveredState()); }
internal sealed class DeliveredState : IOrderState { public string Name => "Delivered"; public void Next(OrderContext context) => Console.WriteLine("State -> Order already delivered"); }
