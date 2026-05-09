namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class BuilderPattern
{
    internal static void Run()
    {
        var pipeline = new PipelineBuilder()
            .UseSourceControl("GitHub")
            .AddBuildStep("dotnet build")
            .AddTestStep("dotnet test")
            .AddDeployStep("Deploy to Azure")
            .Build();
        Console.WriteLine($"Builder -> {pipeline}");
    }
}

internal sealed class DeploymentPipeline
{
    public string SourceControl { get; set; } = string.Empty;
    public List<string> Steps { get; init; } = [];
    public override string ToString() => $"Pipeline from {SourceControl}: {string.Join(" -> ", Steps)}";
}

internal sealed class PipelineBuilder
{
    private readonly DeploymentPipeline _pipeline = new();
    internal PipelineBuilder UseSourceControl(string source) { _pipeline.SourceControl = source; return this; }
    internal PipelineBuilder AddBuildStep(string step) { _pipeline.Steps.Add(step); return this; }
    internal PipelineBuilder AddTestStep(string step) { _pipeline.Steps.Add(step); return this; }
    internal PipelineBuilder AddDeployStep(string step) { _pipeline.Steps.Add(step); return this; }
    internal DeploymentPipeline Build() => _pipeline;
}
