using SolidPrinciples.Bird.I_InterfaceSegregation.Birds;

namespace SolidPrinciples.Bird.I_InterfaceSegregation;

/// <summary>
/// Depends only on ISwimmable — not forced to know about Fly() or Hunt().
/// </summary>
public sealed class AquaticBirdShow
{
    public IReadOnlyList<string> RunShow(IEnumerable<ISwimmable> swimmers) =>
        swimmers.Select(s => s.Swim()).ToList();
}

public sealed class MigrationTracker
{
    public IReadOnlyList<string> Track(IEnumerable<IMigratory> migratoryBirds) =>
        migratoryBirds.Select(m => m.Migrate()).ToList();
}

public static class InterfaceSegregationDemo
{
    public static void Run()
    {
        var aquaticShow = new AquaticBirdShow();
        ISwimmable[] swimmers = [new Duck("Donald"), new Penguin("Percy")];

        foreach (var act in aquaticShow.RunShow(swimmers))
        {
            Console.WriteLine($"  Aquatic show: {act}");
        }

        var tracker = new MigrationTracker();
        IMigratory[] migrants = [new Duck("Daisy")];

        foreach (var route in tracker.Track(migrants))
        {
            Console.WriteLine($"  Migration: {route}");
        }

        Console.WriteLine("  Penguin is not forced to implement Fly() or Hunt() — only what it actually does.");
    }
}
