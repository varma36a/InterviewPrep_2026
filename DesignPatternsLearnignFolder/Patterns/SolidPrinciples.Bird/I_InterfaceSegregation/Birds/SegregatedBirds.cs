using SolidPrinciples.Bird.I_InterfaceSegregation;

namespace SolidPrinciples.Bird.I_InterfaceSegregation.Birds;

public sealed class Eagle(string name) : IFlyable, ICarnivorous
{
    public string Fly() => $"{name} soars at 10,000 ft scanning for prey.";
    public string Hunt() => $"{name} dives to catch fish with talons.";
}

public sealed class Duck(string name) : IFlyable, ISwimmable, IMigratory
{
    public string Fly() => $"{name} flies in V-formation.";
    public string Swim() => $"{name} paddles across the pond.";
    public string Migrate() => $"{name} flies south for winter.";
}

public sealed class Penguin(string name) : ISwimmable
{
    public string Swim() => $"{name} torpedoes through icy water at 15 mph.";
}
