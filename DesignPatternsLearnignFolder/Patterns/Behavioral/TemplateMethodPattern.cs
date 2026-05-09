namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class TemplateMethodPattern
{
    internal static void Run()
    {
        DataImportPipeline pipeline = new CsvImportPipeline();
        pipeline.Run();
    }
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
