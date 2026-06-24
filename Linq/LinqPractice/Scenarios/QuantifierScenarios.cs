using LinqPractice.Data;
using LinqPractice.Helpers;

namespace LinqPractice.Scenarios;

/// <summary>
/// Quantifiers &amp; element operations — Any, All, First, Single.
/// </summary>
public static class QuantifierScenarios
{
    public static void RunAll()
    {
        ConsoleHelper.PrintSection("7. QUANTIFIERS & ELEMENT OPS (Any, All, First, Single)");

        // Q1: Any employee in Denver?
        ConsoleHelper.PrintQuery(
            "Is there any employee in Denver?",
            "Employees.Any(e => e.City == \"Denver\")");
        var q1 = SampleData.Employees.Any(e => e.City == "Denver");
        ConsoleHelper.PrintScalar("Result", q1);

        // Q2: All products have positive price?
        ConsoleHelper.PrintQuery(
            "Do all products have price > 0?",
            "Products.All(p => p.Price > 0)");
        var q2 = SampleData.Products.All(p => p.Price > 0);
        ConsoleHelper.PrintScalar("Result", q2);

        // Q3: All CS students have GPA >= 3.0?
        ConsoleHelper.PrintQuery(
            "Do all CS students have GPA >= 3.0?",
            "Students.Where(s => s.Major == \"Computer Science\").All(s => s.Gpa >= 3.0)");
        var q3 = SampleData.Students
            .Where(s => s.Major == "Computer Science")
            .All(s => s.Gpa >= 3.0);
        ConsoleHelper.PrintScalar("Result", q3);

        // Q4: First employee named starting with 'A'
        ConsoleHelper.PrintQuery(
            "First employee whose name starts with 'A' (or default)",
            "Employees.FirstOrDefault(e => e.Name.StartsWith(\"A\"))");
        var q4 = SampleData.Employees.FirstOrDefault(e => e.Name.StartsWith("A"));
        ConsoleHelper.PrintScalar("Result", q4?.Name ?? "(none)");

        // Q5: Single department for employee id 8
        ConsoleHelper.PrintQuery(
            "Department of employee with Id = 8",
            "Employees.Where(e => e.Id == 8).Select(e => e.Department).Single()");
        var q5 = SampleData.Employees.Where(e => e.Id == 8).Select(e => e.Department).Single();
        ConsoleHelper.PrintScalar("Result", q5);

        // Q6: ElementAt — 5th number in sequence
        ConsoleHelper.PrintQuery(
            "5th number (0-based index 4)",
            "Numbers.ElementAt(4)");
        var q6 = SampleData.Numbers.ElementAt(4);
        ConsoleHelper.PrintScalar("Result", q6);

        // Q7: Any pending orders for customer Acme?
        ConsoleHelper.PrintQuery(
            "Does Acme Corp have any pending orders?",
            "Orders.Any(o => o.CustomerId == acmeId && o.Status == \"Pending\")");
        var acmeId = SampleData.Customers.First(c => c.Name == "Acme Corp").Id;
        var q7 = SampleData.Orders.Any(o => o.CustomerId == acmeId && o.Status == "Pending");
        ConsoleHelper.PrintScalar("Result", q7);
    }
}
