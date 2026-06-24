using SolidPrinciples.Bird.Shared;

namespace SolidPrinciples.Bird.S_SingleResponsibility;

public static class SingleResponsibilityDemo
{
    public static void Run()
    {
        var robin = new BirdProfile("Ruby", "Robin");
        var dietPlanner = new BirdDietPlanner();
        var habitatReporter = new BirdHabitatReporter();

        Console.WriteLine($"  Diet:    {dietPlanner.PlanDailyMeals(robin)}");
        Console.WriteLine($"  Habitat: {habitatReporter.DescribeHabitat(robin)}");
        Console.WriteLine("  Each class has exactly one job — change diet rules without touching habitat code.");
    }
}
