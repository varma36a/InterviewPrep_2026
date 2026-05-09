namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class PrototypePattern
{
    internal static void Run()
    {
        var originalReport = new ReportTemplate("GST Monthly", "Standard Layout");
        var clonedReport = originalReport.Clone();
        clonedReport.Title = "GST Monthly - Client B";
        Console.WriteLine($"Prototype -> Original: {originalReport.Title}, Clone: {clonedReport.Title}");
    }
}

internal sealed class ReportTemplate
{
    public string Title { get; set; }
    public string Layout { get; }
    internal ReportTemplate(string title, string layout) { Title = title; Layout = layout; }
    internal ReportTemplate Clone() => new(Title, Layout);
}
