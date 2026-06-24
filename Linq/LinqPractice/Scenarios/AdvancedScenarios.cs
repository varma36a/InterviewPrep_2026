using LinqPractice.Data;
using LinqPractice.Helpers;

namespace LinqPractice.Scenarios;

/// <summary>
/// Advanced interview scenarios — nested queries, deferred execution, dictionaries.
/// </summary>
public static class AdvancedScenarios
{
    public static void RunAll()
    {
        ConsoleHelper.PrintSection("9. ADVANCED (Nested LINQ, ToDictionary, Complex Business Logic)");

        // Q1: Top-spending customer
        ConsoleHelper.PrintQuery(
            "Customer with highest total completed order amount",
            "Orders.Where(...).GroupBy(o => o.CustomerId).OrderByDescending(g => g.Sum(...)).First()");
        var q1 = SampleData.Orders
            .Where(o => o.Status == "Completed")
            .GroupBy(o => o.CustomerId)
            .Select(g => new { CustomerId = g.Key, Total = g.Sum(o => o.TotalAmount) })
            .OrderByDescending(x => x.Total)
            .First();
        var topCustomer = SampleData.Customers.First(c => c.Id == q1.CustomerId);
        ConsoleHelper.PrintScalar("Result", $"{topCustomer.Name} — ${q1.Total:N2}");

        // Q2: Employees earning more than their department average
        ConsoleHelper.PrintQuery(
            "Employees paid above their department average",
            "deptAvg join Employees where Salary > avg");
        var deptAvg = SampleData.Employees
            .GroupBy(e => e.Department)
            .ToDictionary(g => g.Key, g => g.Average(e => e.Salary));

        var q2 = SampleData.Employees
            .Where(e => e.Salary > deptAvg[e.Department])
            .Select(e => $"{e.Name} ({e.Department}): ${e.Salary} > avg ${deptAvg[e.Department]:F0}")
            .ToList();
        ConsoleHelper.PrintResult("Result", q2);

        // Q3: Products never ordered
        ConsoleHelper.PrintQuery(
            "Products that have never been ordered",
            "Products.Where(p => !OrderItems.Any(oi => oi.ProductId == p.Id))");
        var q3 = SampleData.Products
            .Where(p => !SampleData.OrderItems.Any(oi => oi.ProductId == p.Id))
            .Select(p => p.Name)
            .ToList();
        ConsoleHelper.PrintResult("Result", q3);

        // Q4: Running total of order amounts by date
        ConsoleHelper.PrintQuery(
            "Running total of order amounts (ordered by date)",
            "Orders.OrderBy(o => o.OrderDate).Select with running sum via Aggregate pattern");
        decimal running = 0;
        var q4 = SampleData.Orders
            .OrderBy(o => o.OrderDate)
            .Select(o =>
            {
                running += o.TotalAmount;
                return $"Order {o.Id} ({o.OrderDate:MM/dd}): +${o.TotalAmount} → running ${running:N2}";
            })
            .ToList();
        ConsoleHelper.PrintResult("Result", q4);

        // Q5: Student with most enrollments
        ConsoleHelper.PrintQuery(
            "Student enrolled in the most courses",
            "Enrollments.GroupBy(e => e.StudentId).OrderByDescending(g => g.Count()).First()");
        var topEnrollment = SampleData.Enrollments
            .GroupBy(e => e.StudentId)
            .OrderByDescending(g => g.Count())
            .First();
        var student = SampleData.Students.First(s => s.Id == topEnrollment.Key);
        ConsoleHelper.PrintScalar("Result", $"{student.Name} ({topEnrollment.Count()} courses)");

        // Q6: Average grade per course (only graded enrollments)
        ConsoleHelper.PrintQuery(
            "Average grade per course",
            "Enrollments.Where(e => e.Grade.HasValue).GroupBy(...).Join(Courses,...)");
        var q6 = SampleData.Enrollments
            .Where(e => e.Grade.HasValue)
            .GroupBy(e => e.CourseId)
            .Join(SampleData.Courses, g => g.Key, c => c.Id,
                (g, c) => $"{c.Title}: avg {g.Average(e => e.Grade!.Value):F1}%")
            .ToList();
        ConsoleHelper.PrintResult("Result", q6);

        // Q7: Deferred execution demo
        ConsoleHelper.PrintQuery(
            "Deferred execution: query not run until enumerated",
            "var query = Employees.Where(...); // no execution yet");
        var deferred = SampleData.Employees.Where(e => e.Salary > 90000);
        Console.WriteLine("  Query defined but not executed yet.");
        var q7 = deferred.Select(e => e.Name).ToList();
        ConsoleHelper.PrintResult("After .ToList()", q7);

        // Q8: Dictionary — product id to name for O(1) lookup
        ConsoleHelper.PrintQuery(
            "Build product Id → Name dictionary",
            "Products.ToDictionary(p => p.Id, p => p.Name)");
        var productDict = SampleData.Products.ToDictionary(p => p.Id, p => p.Name);
        ConsoleHelper.PrintScalar("Result", $"Product 6 = {productDict[6]}");
    }
}
