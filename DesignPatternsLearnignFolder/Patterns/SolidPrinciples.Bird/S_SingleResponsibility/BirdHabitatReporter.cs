using SolidPrinciples.Bird.Shared;

namespace SolidPrinciples.Bird.S_SingleResponsibility;

/// <summary>
/// S — Single Responsibility: habitat reporting only; not mixed with diet or locomotion.
/// </summary>
public sealed class BirdHabitatReporter
{
    public string DescribeHabitat(BirdProfile bird) =>
        bird.Species switch
        {
            "Eagle" => $"{bird.Name} nests on cliffs and tall trees.",
            "Robin" => $"{bird.Name} prefers gardens and woodland edges.",
            "Penguin" => $"{bird.Name} lives in coastal colonies in the Southern Hemisphere.",
            _ => $"{bird.Name} habitat varies by species."
        };
}
