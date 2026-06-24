using LinqPractice.Scenarios;

Console.WriteLine("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║           LINQ Interview Practice — .NET 8 Console App           ║
    ╚══════════════════════════════════════════════════════════════════╝

    Run all solved examples:  dotnet run
    Practice mode (DIY):      dotnet run -- --practice
    Run one category:         dotnet run -- --category filtering

    Categories: filtering | projection | sorting | grouping | joins |
                aggregation | quantifiers | sets | advanced | nplus1 | querysyntax | practice
    """);

var cmdArgs = Environment.GetCommandLineArgs().Skip(1).ToArray();
var practiceMode = cmdArgs.Contains("--practice");
var categoryIndex = Array.IndexOf(cmdArgs, "--category");
var category = categoryIndex >= 0 && categoryIndex + 1 < cmdArgs.Length
    ? cmdArgs[categoryIndex + 1].ToLowerInvariant()
    : null;

if (practiceMode || category == "practice")
{
    PracticeExercises.RunAll();
}
else if (category is not null)
{
    RunCategory(category);
}
else
{
    RunAllScenarios();
}

static void RunAllScenarios()
{
    FilteringScenarios.RunAll();
    ProjectionScenarios.RunAll();
    SortingScenarios.RunAll();
    GroupingScenarios.RunAll();
    JoinScenarios.RunAll();
    AggregationScenarios.RunAll();
    QuantifierScenarios.RunAll();
    SetOperationScenarios.RunAll();
    AdvancedScenarios.RunAll();
    NPlusOneScenarios.RunAll();
    QuerySyntaxScenarios.RunAll();

    Console.WriteLine();
    Console.ForegroundColor = ConsoleColor.Cyan;
    Console.WriteLine("Tip: Run `dotnet run -- --practice` for hands-on exercises.");
    Console.WriteLine("     Open Scenarios/PracticeExercises.cs to implement them.");
    Console.ResetColor();
}

static void RunCategory(string category)
{
    switch (category)
    {
        case "filtering":
            FilteringScenarios.RunAll();
            break;
        case "projection":
            ProjectionScenarios.RunAll();
            break;
        case "sorting":
            SortingScenarios.RunAll();
            break;
        case "grouping":
            GroupingScenarios.RunAll();
            break;
        case "joins":
            JoinScenarios.RunAll();
            break;
        case "aggregation":
            AggregationScenarios.RunAll();
            break;
        case "quantifiers":
            QuantifierScenarios.RunAll();
            break;
        case "sets":
            SetOperationScenarios.RunAll();
            break;
        case "advanced":
            AdvancedScenarios.RunAll();
            break;
        case "nplus1":
            NPlusOneScenarios.RunAll();
            break;
        case "querysyntax":
        case "query":
            QuerySyntaxScenarios.RunAll();
            break;
        default:
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine($"Unknown category: {category}");
            Console.ResetColor();
            break;
    }
}
