using LinqPractice.Data;
using LinqPractice.Helpers;

namespace LinqPractice.Scenarios;

/// <summary>
/// Practice exercises — try these yourself before peeking at solutions in Scenarios/.
/// Uncomment the query in each method and run: dotnet run -- --practice
/// </summary>
public static class PracticeExercises
{
    public static void RunAll()
    {
        ConsoleHelper.PrintSection("10. YOUR TURN — Practice Exercises (implement the LINQ yourself)");

        Console.WriteLine("""
            Instructions:
            1. Open Scenarios/PracticeExercises.cs
            2. Uncomment and implement each query in the Try* methods
            3. Run: dotnet run -- --practice

            """);

        //TryExercise1();
         //TryExercise2();
        TryExercise3();
        // TryExercise4();
        // TryExercise5();
        // TryExercise6();
        // TryExercise7();
        // TryExercise8();
    }

    // Exercise 1: Get names of employees in Seattle
    private static void TryExercise1()
    {
        ConsoleHelper.PrintQuery("Get names of all employees in Seattle", "YOUR QUERY HERE");
        var result = SampleData.Employees
            .Where(e => e.City == "Seattle")
            .Select(e => e.Name)
            .ToList();
        ConsoleHelper.PrintResult("Your result", result);
        Console.WriteLine("  (Uncomment the query above to solve)");
    }

    // Exercise 2: Count products per category
    private static void TryExercise2()
    {
        ConsoleHelper.PrintQuery("Count products in each category", "GroupBy + Count");
        var result = SampleData.Products
            .GroupBy(p => p.Category)
            .Select(g => $"{g.Key}: {g.Count()}")
            .ToList();
        ConsoleHelper.PrintResult("Your result", result);
        Console.WriteLine("  (Uncomment the query above to solve)");
    }

    // Exercise 3: Top 5 customers by total order amount
    private static void TryExercise3()
    {
        ConsoleHelper.PrintQuery("Top 5 customers by total order amount", "GroupBy + OrderByDescending + Take");
        var result = SampleData.Orders
            .GroupBy(o => o.CustomerId)
            .Select(g => new { CustomerId = g.Key, Total = g.Sum(o => o.TotalAmount) })
            .OrderByDescending(x => x.Total)
            //.Take(5)
            .Join(SampleData.Customers, x => x.CustomerId, c => c.Id,
                (x, c) => $"{c.Name}: ${x.Total}")
            .ToList();
        ConsoleHelper.PrintResult("Your result", result);
        Console.WriteLine("  (Uncomment the query above to solve)");
    }

    // Exercise 4: Find duplicate enrollments (same student + course)
    private static void TryExercise4()
    {
        ConsoleHelper.PrintQuery("This dataset has no dupes — find students taking 2+ CS courses", "Where + Count");
        // var result = SampleData.Enrollments
        //     .Join(SampleData.Courses, e => e.CourseId, c => c.Id, (e, c) => new { e.StudentId, c.Department })
        //     .Where(x => x.Department == "Computer Science")
        //     .GroupBy(x => x.StudentId)
        //     .Where(g => g.Count() >= 2)
        //     .Join(SampleData.Students, g => g.Key, s => s.Id, (_, s) => s.Name)
        //     .ToList();
        // ConsoleHelper.PrintResult("Your result", result);
        Console.WriteLine("  (Uncomment the query above to solve)");
    }

    // Exercise 5: Revenue by month in 2024
    private static void TryExercise5()
    {
        ConsoleHelper.PrintQuery("Total revenue by month for 2024 orders", "GroupBy OrderDate.Month + Sum");
        // var result = SampleData.Orders
        //     .Where(o => o.OrderDate.Year == 2024)
        //     .GroupBy(o => o.OrderDate.Month)
        //     .OrderBy(g => g.Key)
        //     .Select(g => $"Month {g.Key}: ${g.Sum(o => o.TotalAmount):N2}")
        //     .ToList();
        // ConsoleHelper.PrintResult("Your result", result);
        Console.WriteLine("  (Uncomment the query above to solve)");
    }

    // Exercise 6: Left join — list all products with total units sold (0 if none)
    private static void TryExercise6()
    {
        ConsoleHelper.PrintQuery("All products with total units sold (include 0)", "GroupJoin or DefaultIfEmpty pattern");
        // var result = SampleData.Products
        //     .GroupJoin(SampleData.OrderItems, p => p.Id, oi => oi.ProductId,
        //         (p, items) => new { p.Name, Sold = items.Sum(i => i.Quantity) })
        //     .Select(x => $"{x.Name}: {x.Sold} sold")
        //     .ToList();
        // ConsoleHelper.PrintResult("Your result", result);
        Console.WriteLine("  (Uncomment the query above to solve)");
    }

    // Exercise 7: Second highest distinct salary
    private static void TryExercise7()
    {
        ConsoleHelper.PrintQuery("Second highest distinct salary", "Distinct + OrderByDescending + Skip(1).First()");
        // var result = SampleData.Employees
        //     .Select(e => e.Salary)
        //     .Distinct()
        //     .OrderByDescending(s => s)
        //     .Skip(1)
        //     .First();
        // ConsoleHelper.PrintScalar("Your result", $"${result}");
        Console.WriteLine("  (Uncomment the query above to solve)");
    }

    // Exercise 8: Words grouped by first letter
    private static void TryExercise8()
    {
        ConsoleHelper.PrintQuery("Group words by first letter, show count per letter", "GroupBy w[0]");
        // var result = SampleData.Words
        //     .GroupBy(w => w[0])
        //     .OrderBy(g => g.Key)
        //     .Select(g => $"{g.Key}: {g.Count()} words")
        //     .ToList();
        // ConsoleHelper.PrintResult("Your result", result);
        Console.WriteLine("  (Uncomment the query above to solve)");
    }
}
