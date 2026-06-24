namespace SolidPrinciples.Bird.I_InterfaceSegregation;

/// <summary>
/// I — Interface Segregation: small, role-specific interfaces instead of one fat IBirdCapabilities.
/// </summary>
public interface IFlyable
{
    string Fly();
}

public interface ISwimmable
{
    string Swim();
}

public interface IMigratory
{
    string Migrate();
}

public interface ICarnivorous
{
    string Hunt();
}
