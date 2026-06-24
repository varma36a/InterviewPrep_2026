using SolidPrinciples.Bird.Shared;

namespace SolidPrinciples.Bird.S_SingleResponsibility;

/// <summary>
/// S — Single Responsibility: one reason to change (diet rules only).
/// </summary>
public sealed class BirdDietPlanner
{
    public string PlanDailyMeals(BirdProfile bird) =>
        bird.Species switch
        {
            "Eagle" => $"{bird.Name}: 400g fish + 150g small mammals",
            "Robin" => $"{bird.Name}: insects, berries, and mealworms",
            "Penguin" => $"{bird.Name}: krill and small fish",
            _ => $"{bird.Name}: standard seed mix"
        };
}
