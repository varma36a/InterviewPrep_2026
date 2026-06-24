namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class MediatorPattern
{
    internal static void Run()
    {
        var kitchenHub = new KitchenHub();
        var chef = new KitchenStaff("Chef", kitchenHub);
        var driver = new KitchenStaff("Driver", kitchenHub);
        kitchenHub.Register(chef);
        kitchenHub.Register(driver);
        chef.Send("Large Pepperoni is ready for pickup.");
    }
}

internal interface IKitchenMediator { void Send(string message, KitchenStaff sender); }
internal sealed class KitchenHub : IKitchenMediator
{
    private readonly List<KitchenStaff> _staff = [];
    internal void Register(KitchenStaff member) => _staff.Add(member);
    public void Send(string message, KitchenStaff sender)
    {
        foreach (var member in _staff.Where(m => m != sender)) member.Receive(message, sender.Name);
    }
}
internal sealed class KitchenStaff(string name, IKitchenMediator mediator)
{
    internal string Name { get; } = name;
    internal void Send(string message) => mediator.Send(message, this);
    internal void Receive(string message, string from) => Console.WriteLine($"Mediator -> {Name} got from {from}: {message}");
}
