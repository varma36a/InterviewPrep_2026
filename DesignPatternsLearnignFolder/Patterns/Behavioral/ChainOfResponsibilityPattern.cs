namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class ChainOfResponsibilityPattern
{
    internal static void Run()
    {
        var cashier = new CashierHandler();
        var kitchen = new KitchenManagerHandler();
        var storeManager = new StoreManagerHandler();
        cashier.SetNext(kitchen).SetNext(storeManager);
        cashier.Handle(new OrderIssue("Wrong topping on pizza", 1));
        cashier.Handle(new OrderIssue("Pizza arrived cold", 2));
        cashier.Handle(new OrderIssue("Health complaint - foreign object", 3));
    }
}

internal sealed class OrderIssue(string description, int severity)
{
    internal string Description { get; } = description;
    internal int Severity { get; } = severity;
}
internal abstract class OrderIssueHandler
{
    private OrderIssueHandler? _next;
    internal OrderIssueHandler SetNext(OrderIssueHandler next) { _next = next; return next; }
    internal virtual void Handle(OrderIssue issue) => _next?.Handle(issue);
}
internal sealed class CashierHandler : OrderIssueHandler
{
    internal override void Handle(OrderIssue issue)
    {
        if (issue.Severity == 1) Console.WriteLine($"Chain -> Cashier resolved: {issue.Description}");
        else base.Handle(issue);
    }
}
internal sealed class KitchenManagerHandler : OrderIssueHandler
{
    internal override void Handle(OrderIssue issue)
    {
        if (issue.Severity == 2) Console.WriteLine($"Chain -> Kitchen manager resolved: {issue.Description}");
        else base.Handle(issue);
    }
}
internal sealed class StoreManagerHandler : OrderIssueHandler
{
    internal override void Handle(OrderIssue issue) => Console.WriteLine($"Chain -> Store manager resolved: {issue.Description}");
}
