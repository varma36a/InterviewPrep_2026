using LinqPractice.Data;
using LinqPractice.Helpers;

namespace LinqPractice.Scenarios;

/// <summary>
/// Grouping — GroupBy, ToLookup, aggregation per group.
/// </summary>
public static class GroupingScenarios
{
    public static void RunAll()
    {
        ConsoleHelper.PrintSection("4. GROUPING (GroupBy, ToLookup)");

        // Q1: Count employees per department
        ConsoleHelper.PrintQuery(
            "Employee count per department",
            "Employees.GroupBy(e => e.Department).Select(g => new { Dept = g.Key, Count = g.Count() })");
        var q1 = SampleData.Employees
            .GroupBy(e => e.Department)
            .Select(g => $"{g.Key}: {g.Count()} employees")
            .ToList();
        ConsoleHelper.PrintResult("Result", q1);

        // Q2: Average salary by department
        ConsoleHelper.PrintQuery(
            "Average salary per department",
            "Employees.GroupBy(e => e.Department).Select(g => new { g.Key, Avg = g.Average(e => e.Salary) })");
        var q2 = SampleData.Employees
            .GroupBy(e => e.Department)
            .Select(g => $"{g.Key}: avg ${g.Average(e => e.Salary):F0}")
            .ToList();
        ConsoleHelper.PrintResult("Result", q2);

        // Q3: Products grouped by category — max price each
        ConsoleHelper.PrintQuery(
            "Max product price per category",
            "Products.GroupBy(p => p.Category).Select(g => new { g.Key, MaxPrice = g.Max(p => p.Price) })");
        var q3 = SampleData.Products
            .GroupBy(p => p.Category)
            .Select(g => $"{g.Key}: max ${g.Max(p => p.Price)}")
            .ToList();
        ConsoleHelper.PrintResult("Result", q3);

        // Q4: Orders grouped by status — total revenue
        ConsoleHelper.PrintQuery(
            "Total revenue per order status",
            "Orders.GroupBy(o => o.Status).Select(g => new { g.Key, Revenue = g.Sum(o => o.TotalAmount) })");
        var q4 = SampleData.Orders
            .GroupBy(o => o.Status)
            .Select(g => $"{g.Key}: ${g.Sum(o => o.TotalAmount)}")
            .ToList();
        ConsoleHelper.PrintResult("Result", q4);

        // Q5: Group employees by city, list names
        ConsoleHelper.PrintQuery(
            "Employees grouped by city with names",
            "Employees.GroupBy(e => e.City).Select(g => new { City = g.Key, Names = g.Select(e => e.Name) })");
        var q5 = SampleData.Employees
            .GroupBy(e => e.City)
            .Select(g => $"{g.Key}: [{string.Join(", ", g.Select(e => e.Name))}]")
            .ToList();
        ConsoleHelper.PrintResult("Result", q5);

        // Q6: ToLookup — fast repeated lookups by department
        ConsoleHelper.PrintQuery(
            "Lookup: all employee names in Engineering via ToLookup",
            "Employees.ToLookup(e => e.Department)[\"Engineering\"].Select(e => e.Name)");
        var lookup = SampleData.Employees.ToLookup(e => e.Department);
        var q6 = lookup["Engineering"].Select(e => e.Name).ToList();
        ConsoleHelper.PrintResult("Result", q6);

        // Q7: GroupBy with having — departments with avg salary > 70k
        ConsoleHelper.PrintQuery(
            "Departments where average salary exceeds 70,000",
            "Employees.GroupBy(e => e.Department).Where(g => g.Average(e => e.Salary) > 70000).Select(g => g.Key)");
        var q7 = SampleData.Employees
            .GroupBy(e => e.Department)
            .Where(g => g.Average(e => e.Salary) > 70000)
            .Select(g => g.Key)
            .ToList();
        ConsoleHelper.PrintResult("Result", q7);
    }
}
