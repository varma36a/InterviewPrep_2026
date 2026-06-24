namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class ObserverPattern
{
    internal static void Run()
    {
        var orderTracker = new PizzaOrderTracker("Order #1042", "Preparing");
        orderTracker.Attach(new Customer("Rohit"));
        orderTracker.Attach(new Customer("Anya"));
        orderTracker.Status = "Out for Delivery";
    }
}

internal interface ICustomer { void Update(string orderId, string status); }
internal sealed class PizzaOrderTracker(string orderId, string status)
{
    private readonly List<ICustomer> _customers = [];
    private string _status = status;
    internal string OrderId { get; } = orderId;
    internal string Status
    {
        get => _status;
        set
        {
            _status = value;
            foreach (var customer in _customers) customer.Update(OrderId, _status);
        }
    }
    internal void Attach(ICustomer customer) => _customers.Add(customer);
}
internal sealed class Customer(string name) : ICustomer
{
    public void Update(string orderId, string status) => Console.WriteLine($"Observer -> {name} notified: {orderId} is now {status}");
}
