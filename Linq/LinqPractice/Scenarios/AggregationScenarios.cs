using LinqPractice.Data;
using LinqPractice.Helpers;

namespace LinqPractice.Scenarios;

/// <summary>
/// Aggregation — Sum, Count, Average, Min, Max, Aggregate.
/// </summary>
public static class AggregationScenarios
{
    public static void RunAll()
    {
        ConsoleHelper.PrintSection("6. AGGREGATION (Sum, Count, Average, Min, Max, Aggregate)");

        // Q1: Total payroll
        ConsoleHelper.PrintQuery(
            "Total company payroll",
            "Employees.Sum(e => e.Salary)");
        var q1 = SampleData.Employees.Sum(e => e.Salary);
        ConsoleHelper.PrintScalar("Result", $"${q1:N0}");

        // Q2: Average product price in Electronics
        ConsoleHelper.PrintQuery(
            "Average price of Electronics products",
            "Products.Where(p => p.Category == \"Electronics\").Average(p => p.Price)");
        var q2 = SampleData.Products
            .Where(p => p.Category == "Electronics")
            .Average(p => p.Price);
        ConsoleHelper.PrintScalar("Result", $"${q2:F2}");

        // Q3: Completed order count and total revenue
        ConsoleHelper.PrintQuery(
            "Count and sum of Completed orders",
            "Orders.Where(o => o.Status == \"Completed\").Aggregate(...)");
        var completed = SampleData.Orders.Where(o => o.Status == "Completed").ToList();
        var q3Count = completed.Count;
        var q3Sum = completed.Sum(o => o.TotalAmount);
        ConsoleHelper.PrintScalar("Result", $"{q3Count} orders, ${q3Sum:N2} revenue");

        // Q4: Min/Max GPA among CS students
        ConsoleHelper.PrintQuery(
            "Min and max GPA for Computer Science majors",
            "Students.Where(...).Min/Max(s => s.Gpa)");
        var csGpas = SampleData.Students.Where(s => s.Major == "Computer Science").Select(s => s.Gpa);
        ConsoleHelper.PrintScalar("Result", $"Min: {csGpas.Min()}, Max: {csGpas.Max()}");

        // Q5: Product with highest stock
        ConsoleHelper.PrintQuery(
            "Product with highest stock count",
            "Products.OrderByDescending(p => p.Stock).First()");
        var q5 = SampleData.Products.OrderByDescending(p => p.Stock).First();
        ConsoleHelper.PrintScalar("Result", $"{q5.Name} ({q5.Stock} units)");

        // Q6: Custom aggregate — concatenate department names
        ConsoleHelper.PrintQuery(
            "Comma-separated distinct department names using Aggregate",
            "Employees.Select(e => e.Department).Distinct().Aggregate((a, b) => a + \", \" + b)");
        var q6 = SampleData.Employees
            .Select(e => e.Department)
            .Distinct()
            .OrderBy(d => d)
            .Aggregate((a, b) => $"{a}, {b}");
        ConsoleHelper.PrintScalar("Result", q6);

        // Q7: Total quantity sold per product
        ConsoleHelper.PrintQuery(
            "Total units sold per product",
            "OrderItems.GroupBy(oi => oi.ProductId).Select(g => new { ProductId = g.Key, Qty = g.Sum(x => x.Quantity) })");
        var q7 = SampleData.OrderItems
            .GroupBy(oi => oi.ProductId)
            .Join(SampleData.Products, g => g.Key, p => p.Id,
                (g, p) => $"{p.Name}: {g.Sum(x => x.Quantity)} sold")
            .ToList();
        ConsoleHelper.PrintResult("Result", q7);
    }
}
