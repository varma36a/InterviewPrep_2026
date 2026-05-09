namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class ChainOfResponsibilityPattern
{
    internal static void Run()
    {
        var l1 = new Level1Support();
        var l2 = new Level2Support();
        var manager = new SupportManager();
        l1.SetNext(l2).SetNext(manager);
        l1.Handle(new Ticket("Password reset", 1));
        l1.Handle(new Ticket("Data mismatch", 2));
        l1.Handle(new Ticket("Production outage", 3));
    }
}

internal sealed class Ticket(string issue, int severity)
{
    internal string Issue { get; } = issue;
    internal int Severity { get; } = severity;
}
internal abstract class SupportHandler
{
    private SupportHandler? _next;
    internal SupportHandler SetNext(SupportHandler next) { _next = next; return next; }
    internal virtual void Handle(Ticket ticket) => _next?.Handle(ticket);
}
internal sealed class Level1Support : SupportHandler
{
    internal override void Handle(Ticket ticket) { if (ticket.Severity == 1) Console.WriteLine($"Chain -> L1 handled: {ticket.Issue}"); else base.Handle(ticket); }
}
internal sealed class Level2Support : SupportHandler
{
    internal override void Handle(Ticket ticket) { if (ticket.Severity == 2) Console.WriteLine($"Chain -> L2 handled: {ticket.Issue}"); else base.Handle(ticket); }
}
internal sealed class SupportManager : SupportHandler { internal override void Handle(Ticket ticket) => Console.WriteLine($"Chain -> Manager handled: {ticket.Issue}"); }
