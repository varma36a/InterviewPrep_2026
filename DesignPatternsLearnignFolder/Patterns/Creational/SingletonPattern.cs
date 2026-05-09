namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class SingletonPattern
{
    internal static void Run()
    {
        var configA = AppConfig.Instance;
        var configB = AppConfig.Instance;
        configA.Set("Environment", "Production");
        Console.WriteLine($"Singleton -> Same instance: {ReferenceEquals(configA, configB)}");
        Console.WriteLine($"Read via other reference: {configB.Get("Environment")}");
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
