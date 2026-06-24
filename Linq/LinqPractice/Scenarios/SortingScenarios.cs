using LinqPractice.Data;
using LinqPractice.Helpers;

namespace LinqPractice.Scenarios;

/// <summary>
/// Sorting &amp; partitioning — OrderBy, ThenBy, Take, Skip.
/// </summary>
public static class SortingScenarios
{
    public static void RunAll()
    {
        ConsoleHelper.PrintSection("3. SORTING & PARTITIONING (OrderBy, Take, Skip)");

        // Q1: Top 3 highest paid employees
        ConsoleHelper.PrintQuery(
            "Top 3 highest paid employees",
            "Employees.OrderByDescending(e => e.Salary).Take(3).Select(e => e.Name)");
        var q1 = SampleData.Employees
            .OrderByDescending(e => e.Salary)
            .Take(3)
            .Select(e => $"{e.Name} (${e.Salary})")
            .ToList();
        ConsoleHelper.PrintResult("Result", q1);

        // Q2: Products sorted by category then price
        ConsoleHelper.PrintQuery(
            "Products sorted by Category asc, Price desc",
            "Products.OrderBy(p => p.Category).ThenByDescending(p => p.Price)");
        var q2 = SampleData.Products
            .OrderBy(p => p.Category)
            .ThenByDescending(p => p.Price)
            .Select(p => $"{p.Category} | {p.Name} (${p.Price})")
            .ToList();
        ConsoleHelper.PrintResult("Result", q2);

        // Q3: Pagination — page 2, size 3
        ConsoleHelper.PrintQuery(
            "Employees page 2 (skip 3, take 3) sorted by name",
            "Employees.OrderBy(e => e.Name).Skip(3).Take(3)");
        var q3 = SampleData.Employees
            .OrderBy(e => e.Name)
            .Skip(3)
            .Take(3)
            .Select(e => e.Name)
            .ToList();
        ConsoleHelper.PrintResult("Result", q3);

        // Q4: Nth highest salary (2nd highest)
        ConsoleHelper.PrintQuery(
            "2nd highest salary value",
            "Employees.OrderByDescending(e => e.Salary).Skip(1).First().Salary");
        var q4 = SampleData.Employees
            .OrderByDescending(e => e.Salary)
            .Skip(1)
            .First()
            .Salary;
        ConsoleHelper.PrintScalar("Result", $"${q4}");

        // Q5: Latest 3 orders
        ConsoleHelper.PrintQuery(
            "3 most recent orders",
            "Orders.OrderByDescending(o => o.OrderDate).Take(3)");
        var q5 = SampleData.Orders
            .OrderByDescending(o => o.OrderDate)
            .Take(3)
            .Select(o => $"Order {o.Id} on {o.OrderDate:yyyy-MM-dd} (${o.TotalAmount})")
            .ToList();
        ConsoleHelper.PrintResult("Result", q5);

        // Q6: Students by GPA descending, then name
        ConsoleHelper.PrintQuery(
            "CS students sorted by GPA desc, then name asc",
            "Students.Where(s => s.Major == \"Computer Science\").OrderByDescending(s => s.Gpa).ThenBy(s => s.Name)");
        var q6 = SampleData.Students
            .Where(s => s.Major == "Computer Science")
            .OrderByDescending(s => s.Gpa)
            .ThenBy(s => s.Name)
            .Select(s => $"{s.Name} ({s.Gpa})")
            .ToList();
        ConsoleHelper.PrintResult("Result", q6);
    }
}
