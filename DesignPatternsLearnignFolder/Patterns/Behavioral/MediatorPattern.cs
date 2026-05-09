namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class MediatorPattern
{
    internal static void Run()
    {
        var teamChat = new TeamChatMediator();
        var dev = new TeamMember("Dev", teamChat);
        var qa = new TeamMember("QA", teamChat);
        teamChat.Register(dev);
        teamChat.Register(qa);
        dev.Send("Build is ready for testing.");
    }
}

internal interface IChatMediator { void Send(string message, TeamMember sender); }
internal sealed class TeamChatMediator : IChatMediator
{
    private readonly List<TeamMember> _members = [];
    internal void Register(TeamMember member) => _members.Add(member);
    public void Send(string message, TeamMember sender)
    {
        foreach (var member in _members.Where(m => m != sender)) member.Receive(message, sender.Name);
    }
}
internal sealed class TeamMember(string name, IChatMediator mediator)
{
    internal string Name { get; } = name;
    internal void Send(string message) => mediator.Send(message, this);
    internal void Receive(string message, string from) => Console.WriteLine($"Mediator -> {Name} got from {from}: {message}");
}
