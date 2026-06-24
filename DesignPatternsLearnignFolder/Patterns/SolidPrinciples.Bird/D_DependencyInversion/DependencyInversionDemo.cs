namespace SolidPrinciples.Bird.D_DependencyInversion;

public static class DependencyInversionDemo
{
    public static async Task RunAsync()
    {
        IBirdCatalogRepository repository = new InMemoryBirdCatalogRepository();
        IBirdAlertNotifier notifier = new ConsoleBirdAlertNotifier();

        var sanctuary = new BirdSanctuaryService(repository, notifier);
        var count = await sanctuary.ConductHeadcountAsync(CancellationToken.None);

        Console.WriteLine($"  Headcount result: {count} residents.");
        Console.WriteLine("  Swap InMemoryBirdCatalogRepository for SqlBirdCatalogRepository without changing BirdSanctuaryService.");
    }
}
