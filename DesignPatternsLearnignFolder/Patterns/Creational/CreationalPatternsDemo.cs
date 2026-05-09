using DesignPatternsLearnignFolder.Patterns.Shared;

namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class CreationalPatternsDemo
{
    internal static void Run()
    {
        ConsoleSection.Print("CREATIONAL PATTERNS");
        SingletonPattern.Run();
        FactoryMethodPattern.Run();
        AbstractFactoryPattern.Run();
        BuilderPattern.Run();
        PrototypePattern.Run();
    }
}
