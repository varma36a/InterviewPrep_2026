namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class FlyweightPattern
{
    internal static void Run()
    {
        var docFactory = new DocumentTemplateFactory();
        var d1 = docFactory.GetTemplate("Invoice");
        var d2 = docFactory.GetTemplate("Invoice");
        Console.WriteLine($"Flyweight -> Shared template instance: {ReferenceEquals(d1, d2)}");
    }
}

internal sealed class DocumentTemplate(string name) { public string Name { get; } = name; }
internal sealed class DocumentTemplateFactory
{
    private readonly Dictionary<string, DocumentTemplate> _templates = [];
    internal DocumentTemplate GetTemplate(string name)
    {
        if (!_templates.TryGetValue(name, out var template))
        {
            template = new DocumentTemplate(name);
            _templates[name] = template;
        }
        return template;
    }
}
