namespace DesignPatternsLearnignFolder.Patterns.Shared;

internal static class ConsoleSection
{
    internal static void Print(string title)
    {
        Console.WriteLine();
        Console.WriteLine(title);
        Console.WriteLine(new string('-', title.Length));
    }
}
