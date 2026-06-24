using DesignPatternsLearnignFolder.Patterns.Behavioral;
using DesignPatternsLearnignFolder.Patterns.Creational;
using DesignPatternsLearnignFolder.Patterns.Structural;

namespace DesignPatternsLearnignFolder.Patterns.Shared;

internal static class PatternRunner
{
    private static readonly Dictionary<string, Action> Patterns = new(StringComparer.OrdinalIgnoreCase)
    {
        ["singleton"] = SingletonPattern.Run,
        ["factory"] = FactoryMethodPattern.Run,
        ["factorymethod"] = FactoryMethodPattern.Run,
        ["abstractfactory"] = AbstractFactoryPattern.Run,
        ["builder"] = BuilderPattern.Run,
        ["prototype"] = PrototypePattern.Run,
        ["creational"] = CreationalPatternsDemo.Run,

        ["adapter"] = AdapterPattern.Run,
        ["bridge"] = BridgePattern.Run,
        ["composite"] = CompositePattern.Run,
        ["decorator"] = DecoratorPattern.Run,
        ["facade"] = FacadePattern.Run,
        ["flyweight"] = FlyweightPattern.Run,
        ["proxy"] = ProxyPattern.Run,
        ["structural"] = StructuralPatternsDemo.Run,

        ["chain"] = ChainOfResponsibilityPattern.Run,
        ["chainofresponsibility"] = ChainOfResponsibilityPattern.Run,
        ["command"] = CommandPattern.Run,
        ["interpreter"] = InterpreterPattern.Run,
        ["iterator"] = IteratorPattern.Run,
        ["mediator"] = MediatorPattern.Run,
        ["memento"] = MementoPattern.Run,
        ["observer"] = ObserverPattern.Run,
        ["state"] = StatePattern.Run,
        ["strategy"] = StrategyPattern.Run,
        ["template"] = TemplateMethodPattern.Run,
        ["templatemethod"] = TemplateMethodPattern.Run,
        ["visitor"] = VisitorPattern.Run,
        ["behavioral"] = BehavioralPatternsDemo.Run,

        ["all"] = RunAll,
    };

    internal static void Run(string[] args)
    {
        if (args.Length == 0 || IsHelp(args[0]))
        {
            PrintUsage(runAll: args.Length == 0);
            if (args.Length == 0) RunAll();
            return;
        }

        foreach (var arg in args)
        {
            var key = Normalize(arg);
            if (!Patterns.TryGetValue(key, out var run))
            {
                Console.WriteLine($"Unknown pattern: '{arg}'");
                PrintUsage(runAll: false);
                return;
            }
            run();
        }
    }

    private static void RunAll()
    {
        CreationalPatternsDemo.Run();
        StructuralPatternsDemo.Run();
        BehavioralPatternsDemo.Run();
    }

    private static bool IsHelp(string arg) =>
        arg is "-h" or "--help" or "help" or "-?";

    private static string Normalize(string arg) =>
        arg.Replace("-", "", StringComparison.Ordinal).Replace("_", "", StringComparison.Ordinal);

    private static void PrintUsage(bool runAll)
    {
        if (runAll) return;

        Console.WriteLine();
        Console.WriteLine("Usage: dotnet run [-- <pattern> [pattern...]]");
        Console.WriteLine();
        Console.WriteLine("Examples:");
        Console.WriteLine("  dotnet run                    Run all patterns");
        Console.WriteLine("  dotnet run -- singleton       Run Singleton only");
        Console.WriteLine("  dotnet run -- creational        Run all creational patterns");
        Console.WriteLine("  dotnet run -- singleton builder  Run multiple patterns");
        Console.WriteLine();
        Console.WriteLine("Patterns:");
        Console.WriteLine("  Creational:  singleton, factory, abstractfactory, builder, prototype, creational");
        Console.WriteLine("  Structural:  adapter, bridge, composite, decorator, facade, flyweight, proxy, structural");
        Console.WriteLine("  Behavioral:  chain, command, interpreter, iterator, mediator, memento, observer,");
        Console.WriteLine("               state, strategy, template, visitor, behavioral");
    }
}
