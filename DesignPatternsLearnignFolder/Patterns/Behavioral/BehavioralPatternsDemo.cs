using DesignPatternsLearnignFolder.Patterns.Shared;

namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class BehavioralPatternsDemo
{
    internal static void Run()
    {
        ConsoleSection.Print("BEHAVIORAL PATTERNS");
        ChainOfResponsibilityPattern.Run();
        CommandPattern.Run();
        InterpreterPattern.Run();
        IteratorPattern.Run();
        MediatorPattern.Run();
        MementoPattern.Run();
        ObserverPattern.Run();
        StatePattern.Run();
        StrategyPattern.Run();
        TemplateMethodPattern.Run();
        VisitorPattern.Run();
    }
}
