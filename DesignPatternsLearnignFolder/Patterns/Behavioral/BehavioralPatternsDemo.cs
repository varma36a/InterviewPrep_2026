using System.Collections;
using DesignPatternsLearnignFolder.Patterns.Shared;

namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class BehavioralPatternsDemo
{
    internal static void Run()
    {
        ConsoleSection.Print("BEHAVIORAL PATTERNS");

        var l1 = new Level1Support();
        var l2 = new Level2Support();
        var manager = new SupportManager();
        l1.SetNext(l2).SetNext(manager);
        l1.Handle(new Ticket("Password reset", 1));
        l1.Handle(new Ticket("Data mismatch", 2));
        l1.Handle(new Ticket("Production outage", 3));

        var vmService = new VmService();
        var invoker = new OperationInvoker();
        invoker.Enqueue(new StartVmCommand(vmService, "vm-prod-1"));
        invoker.Enqueue(new StopVmCommand(vmService, "vm-test-3"));
        invoker.RunAll();

        var expr = new AndExpression(new GreaterThanExpression("income", 50000), new EqualsExpression("country", "IN"));
        var context = new RuleContext(new Dictionary<string, object> { ["income"] = 75000, ["country"] = "IN" });
        Console.WriteLine($"Interpreter -> Eligible: {expr.Interpret(context)}");

        var customerDirectory = new CustomerDirectory(new[] { "Asha", "Ravi", "Mira" });
        foreach (var customer in customerDirectory) Console.WriteLine($"Iterator -> Customer: {customer}");

        var teamChat = new TeamChatMediator();
        var dev = new TeamMember("Dev", teamChat);
        var qa = new TeamMember("QA", teamChat);
        teamChat.Register(dev);
        teamChat.Register(qa);
        dev.Send("Build is ready for testing.");

        var editor = new DocumentEditor();
        editor.Content = "Draft v1";
        var history = new DraftHistory();
        history.Save(editor.Save());
        editor.Content = "Draft v2 with edits";
        editor.Restore(history.Undo());
        Console.WriteLine($"Memento -> Restored content: {editor.Content}");

        var stock = new Stock("TAX-ETF", 100m);
        stock.Attach(new Trader("Rohit"));
        stock.Attach(new Trader("Anya"));
        stock.Price = 106.5m;

        var order = new OrderContext();
        order.Next();
        order.Next();
        order.Next();

        var taxContext = new TaxComputationContext(new OldRegimeStrategy());
        Console.WriteLine(taxContext.Compute(1200000m));
        taxContext.SetStrategy(new NewRegimeStrategy());
        Console.WriteLine(taxContext.Compute(1200000m));

        DataImportPipeline pipeline = new CsvImportPipeline();
        pipeline.Run();

        IAsset[] assets = [new ServerAsset("api-1"), new DatabaseAsset("tax-db")];
        var securityVisitor = new SecurityAuditVisitor();
        foreach (var asset in assets) asset.Accept(securityVisitor);
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
    internal override void Handle(Ticket ticket)
    {
        if (ticket.Severity == 1) Console.WriteLine($"Chain -> L1 handled: {ticket.Issue}");
        else base.Handle(ticket);
    }
}

internal sealed class Level2Support : SupportHandler
{
    internal override void Handle(Ticket ticket)
    {
        if (ticket.Severity == 2) Console.WriteLine($"Chain -> L2 handled: {ticket.Issue}");
        else base.Handle(ticket);
    }
}

internal sealed class SupportManager : SupportHandler
{
    internal override void Handle(Ticket ticket) => Console.WriteLine($"Chain -> Manager handled: {ticket.Issue}");
}

internal interface ICommand { void Execute(); }

internal sealed class VmService
{
    internal void Start(string vm) => Console.WriteLine($"Command -> Started {vm}");
    internal void Stop(string vm) => Console.WriteLine($"Command -> Stopped {vm}");
}

internal sealed class StartVmCommand(VmService service, string vm) : ICommand { public void Execute() => service.Start(vm); }
internal sealed class StopVmCommand(VmService service, string vm) : ICommand { public void Execute() => service.Stop(vm); }

internal sealed class OperationInvoker
{
    private readonly Queue<ICommand> _commands = new();
    internal void Enqueue(ICommand command) => _commands.Enqueue(command);
    internal void RunAll() { while (_commands.TryDequeue(out var cmd)) cmd.Execute(); }
}

internal sealed class RuleContext(Dictionary<string, object> variables)
{
    internal Dictionary<string, object> Variables { get; } = variables;
}

internal interface IExpression { bool Interpret(RuleContext context); }
internal sealed class GreaterThanExpression(string key, decimal threshold) : IExpression
{
    public bool Interpret(RuleContext context) => Convert.ToDecimal(context.Variables[key]) > threshold;
}
internal sealed class EqualsExpression(string key, string expected) : IExpression
{
    public bool Interpret(RuleContext context) => context.Variables[key].ToString() == expected;
}
internal sealed class AndExpression(IExpression left, IExpression right) : IExpression
{
    public bool Interpret(RuleContext context) => left.Interpret(context) && right.Interpret(context);
}

internal sealed class CustomerDirectory : IEnumerable<string>
{
    private readonly List<string> _customers;
    internal CustomerDirectory(IEnumerable<string> customers) => _customers = [.. customers];
    public IEnumerator<string> GetEnumerator() => _customers.GetEnumerator();
    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
}

internal interface IChatMediator { void Send(string message, TeamMember sender); }

internal sealed class TeamChatMediator : IChatMediator
{
    private readonly List<TeamMember> _members = [];
    internal void Register(TeamMember member) => _members.Add(member);
    public void Send(string message, TeamMember sender)
    {
        foreach (var member in _members.Where(m => m != sender))
            member.Receive(message, sender.Name);
    }
}

internal sealed class TeamMember(string name, IChatMediator mediator)
{
    internal string Name { get; } = name;
    internal void Send(string message) => mediator.Send(message, this);
    internal void Receive(string message, string from) => Console.WriteLine($"Mediator -> {Name} got from {from}: {message}");
}

internal sealed class EditorMemento(string content) { internal string Content { get; } = content; }

internal sealed class DocumentEditor
{
    internal string Content { get; set; } = string.Empty;
    internal EditorMemento Save() => new(Content);
    internal void Restore(EditorMemento snapshot) => Content = snapshot.Content;
}

internal sealed class DraftHistory
{
    private readonly Stack<EditorMemento> _history = new();
    internal void Save(EditorMemento snapshot) => _history.Push(snapshot);
    internal EditorMemento Undo() => _history.Pop();
}

internal interface IInvestor { void Update(string symbol, decimal price); }

internal sealed class Stock(string symbol, decimal price)
{
    private readonly List<IInvestor> _investors = [];
    private decimal _price = price;
    internal string Symbol { get; } = symbol;
    internal decimal Price
    {
        get => _price;
        set
        {
            _price = value;
            foreach (var investor in _investors) investor.Update(Symbol, _price);
        }
    }
    internal void Attach(IInvestor investor) => _investors.Add(investor);
}

internal sealed class Trader(string name) : IInvestor
{
    public void Update(string symbol, decimal price) => Console.WriteLine($"Observer -> {name} notified: {symbol} at {price}");
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

internal sealed class CreatedState : IOrderState
{
    public string Name => "Created";
    public void Next(OrderContext context) => context.SetState(new PaidState());
}

internal sealed class PaidState : IOrderState
{
    public string Name => "Paid";
    public void Next(OrderContext context) => context.SetState(new ShippedState());
}

internal sealed class ShippedState : IOrderState
{
    public string Name => "Shipped";
    public void Next(OrderContext context) => context.SetState(new DeliveredState());
}

internal sealed class DeliveredState : IOrderState
{
    public string Name => "Delivered";
    public void Next(OrderContext context) => Console.WriteLine("State -> Order already delivered");
}

internal interface ITaxStrategy { string Calculate(decimal income); }
internal sealed class OldRegimeStrategy : ITaxStrategy
{
    public string Calculate(decimal income) => $"Strategy -> Old regime tax: {(income * 0.2m):C}";
}
internal sealed class NewRegimeStrategy : ITaxStrategy
{
    public string Calculate(decimal income) => $"Strategy -> New regime tax: {(income * 0.15m):C}";
}

internal sealed class TaxComputationContext(ITaxStrategy strategy)
{
    private ITaxStrategy _strategy = strategy;
    internal void SetStrategy(ITaxStrategy strategy) => _strategy = strategy;
    internal string Compute(decimal income) => _strategy.Calculate(income);
}

internal abstract class DataImportPipeline
{
    internal void Run()
    {
        Extract();
        Transform();
        Load();
    }
    protected abstract void Extract();
    protected abstract void Transform();
    protected abstract void Load();
}

internal sealed class CsvImportPipeline : DataImportPipeline
{
    protected override void Extract() => Console.WriteLine("Template -> Extract CSV");
    protected override void Transform() => Console.WriteLine("Template -> Transform records");
    protected override void Load() => Console.WriteLine("Template -> Load to DB");
}

internal interface IAssetVisitor
{
    void Visit(ServerAsset server);
    void Visit(DatabaseAsset database);
}

internal interface IAsset { void Accept(IAssetVisitor visitor); }

internal sealed class ServerAsset(string host) : IAsset
{
    internal string Host { get; } = host;
    public void Accept(IAssetVisitor visitor) => visitor.Visit(this);
}

internal sealed class DatabaseAsset(string name) : IAsset
{
    internal string Name { get; } = name;
    public void Accept(IAssetVisitor visitor) => visitor.Visit(this);
}

internal sealed class SecurityAuditVisitor : IAssetVisitor
{
    public void Visit(ServerAsset server) => Console.WriteLine($"Visitor -> Audited server {server.Host}");
    public void Visit(DatabaseAsset database) => Console.WriteLine($"Visitor -> Audited database {database.Name}");
}
