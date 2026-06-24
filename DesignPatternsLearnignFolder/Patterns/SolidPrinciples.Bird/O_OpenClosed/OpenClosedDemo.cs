namespace SolidPrinciples.Bird.O_OpenClosed;

public static class OpenClosedDemo
{
    public static void Run()
    {
        IBirdCallClassifier[] classifiers =
        [
            new RobinCallClassifier(),
            new CrowCallClassifier(),
            new OwlCallClassifier()
        ];

        var orchestrator = new BirdCallOrchestrator(classifiers);

        foreach (var sample in new[] { "cheer-up cheerily", "loud caw caw", "hoot hoot" })
        {
            Console.WriteLine($"  Sample '{sample}' → {orchestrator.Identify(sample)}");
        }

        Console.WriteLine("  OwlCallClassifier was added without editing BirdCallOrchestrator.");
    }
}
