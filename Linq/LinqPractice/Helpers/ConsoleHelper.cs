namespace LinqPractice.Helpers;

public static class ConsoleHelper
{
    public static void PrintSection(string title)
    {
        Console.WriteLine();
        Console.WriteLine(new string('=', 70));
        Console.WriteLine($"  {title}");
        Console.WriteLine(new string('=', 70));
    }

    public static void PrintQuery(string description, string queryHint)
    {
        Console.WriteLine();
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.WriteLine($"Problem: {description}");
        Console.ResetColor();
        Console.ForegroundColor = ConsoleColor.DarkGray;
        Console.WriteLine($"LINQ: {queryHint}");
        Console.ResetColor();
    }

    public static void PrintResult<T>(string label, IEnumerable<T> items, int maxItems = 10)
    {
        var list = items.ToList();
        Console.ForegroundColor = ConsoleColor.Green;
        Console.Write($"{label}: ");
        Console.ResetColor();

        if (list.Count == 0)
        {
            Console.WriteLine("(empty)");
            return;
        }

        var display = list.Take(maxItems).Select(x => x?.ToString() ?? "null");
        Console.WriteLine(string.Join(", ", display) + (list.Count > maxItems ? $"... (+{list.Count - maxItems} more)" : ""));
        Console.WriteLine($"  Count: {list.Count}");
    }

    public static void PrintScalar(string label, object value)
    {
        Console.ForegroundColor = ConsoleColor.Green;
        Console.Write($"{label}: ");
        Console.ResetColor();
        Console.WriteLine(value);
    }
}
