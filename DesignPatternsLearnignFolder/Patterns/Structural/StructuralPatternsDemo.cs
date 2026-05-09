using DesignPatternsLearnignFolder.Patterns.Shared;

namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class StructuralPatternsDemo
{
    internal static void Run()
    {
        ConsoleSection.Print("STRUCTURAL PATTERNS");
        AdapterPattern.Run();
        BridgePattern.Run();
        CompositePattern.Run();
        DecoratorPattern.Run();
        FacadePattern.Run();
        FlyweightPattern.Run();
        ProxyPattern.Run();
    }
}
