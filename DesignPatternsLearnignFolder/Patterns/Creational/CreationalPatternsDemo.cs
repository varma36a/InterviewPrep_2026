using DesignPatternsLearnignFolder.Patterns.Shared;

namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class CreationalPatternsDemo
{
    internal static void Run()
    {
        ConsoleSection.Print("CREATIONAL PATTERNS");

        var configA = AppConfig.Instance;
        var configB = AppConfig.Instance;
        configA.Set("Environment", "Production");
        Console.WriteLine($"Singleton -> Same instance: {ReferenceEquals(configA, configB)}");
        Console.WriteLine($"Read via other reference: {configB.Get("Environment")}");

        INotification email = NotificationFactory.Create("email");
        INotification sms = NotificationFactory.Create("sms");
        email.Send("Invoice generated");
        sms.Send("OTP: 483210");

        ITaxSuite indiaSuite = new IndiaTaxSuite();
        ITaxSuite usSuite = new USTaxSuite();
        Console.WriteLine(indiaSuite.CreateCalculator().CalculateTax(1000m));
        Console.WriteLine(usSuite.CreateCalculator().CalculateTax(1000m));

        var pipeline = new PipelineBuilder()
            .UseSourceControl("GitHub")
            .AddBuildStep("dotnet build")
            .AddTestStep("dotnet test")
            .AddDeployStep("Deploy to Azure")
            .Build();
        Console.WriteLine($"Builder -> {pipeline}");

        var originalReport = new ReportTemplate("GST Monthly", "Standard Layout");
        var clonedReport = originalReport.Clone();
        clonedReport.Title = "GST Monthly - Client B";
        Console.WriteLine($"Prototype -> Original: {originalReport.Title}, Clone: {clonedReport.Title}");
    }
}

internal sealed class AppConfig
{
    private static readonly Lazy<AppConfig> InstanceValue = new(() => new AppConfig());
    private readonly Dictionary<string, string> _settings = [];
    internal static AppConfig Instance => InstanceValue.Value;
    private AppConfig() { }
    internal void Set(string key, string value) => _settings[key] = value;
    internal string Get(string key) => _settings.TryGetValue(key, out var value) ? value : "N/A";
}

internal interface INotification { void Send(string message); }
internal sealed class EmailNotification : INotification { public void Send(string message) => Console.WriteLine($"Factory -> Email: {message}"); }
internal sealed class SmsNotification : INotification { public void Send(string message) => Console.WriteLine($"Factory -> SMS: {message}"); }

internal static class NotificationFactory
{
    internal static INotification Create(string type) => type.ToLowerInvariant() switch
    {
        "email" => new EmailNotification(),
        "sms" => new SmsNotification(),
        _ => throw new ArgumentException("Unsupported notification type.")
    };
}

internal interface ITaxCalculator { string CalculateTax(decimal amount); }
internal interface ITaxSuite { ITaxCalculator CreateCalculator(); }
internal sealed class IndiaTaxSuite : ITaxSuite { public ITaxCalculator CreateCalculator() => new IndiaTaxCalculator(); }
internal sealed class USTaxSuite : ITaxSuite { public ITaxCalculator CreateCalculator() => new USTaxCalculator(); }
internal sealed class IndiaTaxCalculator : ITaxCalculator { public string CalculateTax(decimal amount) => $"AbstractFactory -> India GST: {amount * 0.18m:C}"; }
internal sealed class USTaxCalculator : ITaxCalculator { public string CalculateTax(decimal amount) => $"AbstractFactory -> US Sales Tax: {amount * 0.07m:C}"; }

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

internal sealed class ReportTemplate
{
    public string Title { get; set; }
    public string Layout { get; }
    internal ReportTemplate(string title, string layout) { Title = title; Layout = layout; }
    internal ReportTemplate Clone() => new(Title, Layout);
}
