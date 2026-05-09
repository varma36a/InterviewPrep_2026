namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class CompositePattern
{
    internal static void Run()
    {
        var ceo = new EmployeeNode("CEO");
        var techLead = new EmployeeNode("Tech Lead");
        techLead.Add(new EmployeeLeaf("Backend Dev"));
        techLead.Add(new EmployeeLeaf("Frontend Dev"));
        ceo.Add(techLead);
        ceo.Add(new EmployeeLeaf("Finance Head"));
        ceo.Display();
    }
}

internal interface IOrgUnit { void Display(int depth = 0); }
internal sealed class EmployeeLeaf(string name) : IOrgUnit
{
    public void Display(int depth = 0) => Console.WriteLine($"{new string(' ', depth)}- {name}");
}
internal sealed class EmployeeNode(string name) : IOrgUnit
{
    private readonly List<IOrgUnit> _children = [];
    internal void Add(IOrgUnit unit) => _children.Add(unit);
    public void Display(int depth = 0)
    {
        Console.WriteLine($"{new string(' ', depth)}+ {name}");
        foreach (var child in _children) child.Display(depth + 2);
    }
}
