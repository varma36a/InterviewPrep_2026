namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class CommandPattern
{
    internal static void Run()
    {
        var kitchen = new PizzaKitchen();
        var orderQueue = new OrderQueue();
        orderQueue.Enqueue(new PlaceOrderCommand(kitchen, "Large Margherita"));
        orderQueue.Enqueue(new CancelOrderCommand(kitchen, "Order #8821"));
        orderQueue.RunAll();
    }
}

internal interface IOrderCommand { void Execute(); }
internal sealed class PizzaKitchen
{
    internal void PlaceOrder(string pizza) => Console.WriteLine($"Command -> Placed order: {pizza}");
    internal void CancelOrder(string orderId) => Console.WriteLine($"Command -> Cancelled {orderId}");
}
internal sealed class PlaceOrderCommand(PizzaKitchen kitchen, string pizza) : IOrderCommand
{
    public void Execute() => kitchen.PlaceOrder(pizza);
}
internal sealed class CancelOrderCommand(PizzaKitchen kitchen, string orderId) : IOrderCommand
{
    public void Execute() => kitchen.CancelOrder(orderId);
}
internal sealed class OrderQueue
{
    private readonly Queue<IOrderCommand> _commands = new();
    internal void Enqueue(IOrderCommand command) => _commands.Enqueue(command);
    internal void RunAll() { while (_commands.TryDequeue(out var cmd)) cmd.Execute(); }
}
