namespace SolidPrinciples.Bird.L_LiskovSubstitution;

/// <summary>
/// Anti-pattern: forcing flight on birds that cannot fly breaks LSP.
/// A caller expecting FlyingBird.Fly() will crash when given Ostrich.
/// </summary>
public class FlyingBird
{
    public virtual string Fly() => "Flying through the air.";
}

public sealed class Ostrich : FlyingBird
{
    public override string Fly() =>
        throw new InvalidOperationException("Ostriches cannot fly — substituting Ostrich for FlyingBird violates LSP.");
}
