namespace SolidPrinciples.Bird.L_LiskovSubstitution;

/// <summary>
/// L — Liskov Substitution: any Bird can be passed to BirdLocomotionGuide without surprises.
/// Subtypes honour the base contract (Move returns a valid locomotion description).
/// </summary>
public abstract class Bird
{
    public string Name { get; }
    public string Species { get; }

    protected Bird(string name, string species)
    {
        Name = name;
        Species = species;
    }

    public abstract string Move();
}

public sealed class Sparrow(string name) : Bird(name, "Sparrow")
{
    public override string Move() => $"{Name} the Sparrow flaps its wings and flies.";
}

public sealed class Penguin(string name) : Bird(name, "Penguin")
{
    public override string Move() => $"{Name} the Penguin slides on its belly and swims.";
}

public sealed class BirdLocomotionGuide
{
    public IReadOnlyList<string> GuideTour(IEnumerable<Bird> birds) =>
        birds.Select(b => b.Move()).ToList();
}
