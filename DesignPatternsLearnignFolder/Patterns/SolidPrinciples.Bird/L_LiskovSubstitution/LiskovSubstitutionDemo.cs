namespace SolidPrinciples.Bird.L_LiskovSubstitution;

public static class LiskovSubstitutionDemo
{
    public static void Run()
    {
        var guide = new BirdLocomotionGuide();
        Bird[] flock = [new Sparrow("Sky"), new Penguin("Pip")];

        foreach (var line in guide.GuideTour(flock))
        {
            Console.WriteLine($"  {line}");
        }

        Console.WriteLine("  Sparrow and Penguin are interchangeable as Bird — no thrown exceptions, no broken expectations.");

        try
        {
            FlyingBird bird = new Ostrich();
            _ = bird.Fly();
        }
        catch (InvalidOperationException ex)
        {
            Console.WriteLine($"  LSP violation: {ex.Message}");
        }
    }
}
