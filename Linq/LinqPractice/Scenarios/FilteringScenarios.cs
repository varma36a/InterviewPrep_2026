using LinqPractice.Data;
using LinqPractice.Helpers;

namespace LinqPractice.Scenarios;

/// <summary>
/// Filtering &amp; basic queries — very common in phone screens.
/// </summary>
public static class FilteringScenarios
{
    public static void RunAll()
    {
        ConsoleHelper.PrintSection("1. FILTERING (Where, OfType, Distinct)");

        // Q1: Employees in Engineering earning over 80k
        ConsoleHelper.PrintQuery(
            "Find Engineering employees with salary > 80,000",
            "Employees.Where(e => e.Department == \"Engineering\" && e.Salary > 80000)");
        var q1 = SampleData.Employees
            .Where(e => e.Department == "Engineering" && e.Salary > 80000)
            .Select(e => e.Name)
            .ToList();
        ConsoleHelper.PrintResult("Result", q1);

        // Q2: Products out of stock
        ConsoleHelper.PrintQuery(
            "Find products with zero stock",
            "Products.Where(p => p.Stock == 0)");
        var q2 = SampleData.Products
            .Where(p => p.Stock == 0)
            .Select(p => p.Name)
            .ToList();
        ConsoleHelper.PrintResult("Result", q2);

        // Q3: Active electronics under $100
        ConsoleHelper.PrintQuery(
            "Active electronics priced under $100",
            "Products.Where(p => p.IsActive && p.Category == \"Electronics\" && p.Price < 100)");
        var q3 = SampleData.Products
            .Where(p => p.IsActive && p.Category == "Electronics" && p.Price < 100)
            .Select(p => $"{p.Name} (${p.Price})")
            .ToList();
        ConsoleHelper.PrintResult("Result", q3);

        // Q4: Employees hired after 2020
        ConsoleHelper.PrintQuery(
            "Employees hired after Jan 1, 2020",
            "Employees.Where(e => e.HireDate > new DateTime(2020, 1, 1))");
        var q4 = SampleData.Employees
            .Where(e => e.HireDate > new DateTime(2020, 1, 1))
            .Select(e => $"{e.Name} ({e.HireDate:yyyy-MM-dd})")
            .ToList();
        ConsoleHelper.PrintResult("Result", q4);

        // Q5: Distinct cities where employees work
        ConsoleHelper.PrintQuery(
            "Distinct employee cities",
            "Employees.Select(e => e.City).Distinct()");
        var q5 = SampleData.Employees.Select(e => e.City).Distinct().OrderBy(c => c).ToList();
        ConsoleHelper.PrintResult("Result", q5);

        // Q6: Duplicate words in list
        ConsoleHelper.PrintQuery(
            "Words that appear more than once",
            "Words.GroupBy(w => w).Where(g => g.Count() > 1).Select(g => g.Key)");
        var q6 = SampleData.Words
            .GroupBy(w => w)
            .Where(g => g.Count() > 1)
            .Select(g => g.Key)
            .ToList();
        ConsoleHelper.PrintResult("Result", q6);

        // Q7: Even numbers divisible by 3
        ConsoleHelper.PrintQuery(
            "Numbers divisible by both 2 and 3",
            "Numbers.Where(n => n % 2 == 0 && n % 3 == 0)");
        var q7 = SampleData.Numbers.Where(n => n % 2 == 0 && n % 3 == 0).ToList();
        ConsoleHelper.PrintResult("Result", q7);
    }
}
