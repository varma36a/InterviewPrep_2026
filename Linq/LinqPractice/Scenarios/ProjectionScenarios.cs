using LinqPractice.Data;
using LinqPractice.Helpers;

namespace LinqPractice.Scenarios;

/// <summary>
/// Projection — Select, SelectMany, anonymous types.
/// </summary>
public static class ProjectionScenarios
{
    public static void RunAll()
    {
        ConsoleHelper.PrintSection("2. PROJECTION (Select, SelectMany, Anonymous Types)");

        // Q1: Employee name + salary projection
        ConsoleHelper.PrintQuery(
            "Project employees to \"Name earns $Salary\" strings",
            "Employees.Select(e => $\"{e.Name} earns ${e.Salary}\")");
        var q1 = SampleData.Employees
            .Select(e => $"{e.Name} earns ${e.Salary}")
            .ToList();
        ConsoleHelper.PrintResult("Result", q1);

        // Q2: Anonymous type with Id, Name, Department
        ConsoleHelper.PrintQuery(
            "Anonymous projection: Id, Name, Department",
            "Employees.Select(e => new { e.Id, e.Name, e.Department })");
        var q2 = SampleData.Employees
            .Select(e => new { e.Id, e.Name, e.Department })
            .Take(5)
            .Select(x => $"({x.Id}) {x.Name} - {x.Department}")
            .ToList();
        ConsoleHelper.PrintResult("Result (first 5)", q2);

        // Q3: SelectMany — flatten order items into product names
        ConsoleHelper.PrintQuery(
            "All product names from order line items (with duplicates)",
            "OrderItems.Join(Products, oi => oi.ProductId, p => p.Id, (oi, p) => p.Name)");
        var q3 = SampleData.OrderItems
            .Join(SampleData.Products, oi => oi.ProductId, p => p.Id, (_, p) => p.Name)
            .ToList();
        ConsoleHelper.PrintResult("Result", q3);

        // Q4: SelectMany — words starting with 'a' as char arrays flattened
        ConsoleHelper.PrintQuery(
            "All characters from words starting with 'a'",
            "Words.Where(w => w.StartsWith(\"a\")).SelectMany(w => w.ToCharArray())");
        var q4 = SampleData.Words
            .Where(w => w.StartsWith("a"))
            .SelectMany(w => w.ToCharArray())
            .Select(c => c.ToString())
            .ToList();
        ConsoleHelper.PrintResult("Result", q4);

        // Q5: Index in projection
        ConsoleHelper.PrintQuery(
            "Products with index: \"#0: Laptop Pro\"",
            "Products.Select((p, i) => $\"#{i}: {p.Name}\")");
        var q5 = SampleData.Products
            .Select((p, i) => $"#{i}: {p.Name}")
            .Take(5)
            .ToList();
        ConsoleHelper.PrintResult("Result (first 5)", q5);

        // Q6: Nested projection — customer order summaries
        ConsoleHelper.PrintQuery(
            "Customer name + list of their order totals",
            "Customers.Select(c => new { c.Name, Totals = Orders.Where(o => o.CustomerId == c.Id).Select(o => o.TotalAmount) })");
        var q6 = SampleData.Customers
            .Select(c => new
            {
                c.Name,
                Totals = SampleData.Orders
                    .Where(o => o.CustomerId == c.Id)
                    .Select(o => o.TotalAmount)
                    .ToList()
            })
            .Select(x => $"{x.Name}: [{string.Join(", ", x.Totals.Select(t => $"${t}"))}]")
            .ToList();
        ConsoleHelper.PrintResult("Result", q6);
    }
}
