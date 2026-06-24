using LinqPractice.Data;
using LinqPractice.Helpers;

namespace LinqPractice.Scenarios;

/// <summary>
/// Joins — Inner, Left (GroupJoin), cross scenarios.
/// </summary>
public static class JoinScenarios
{
    public static void RunAll()
    {
        ConsoleHelper.PrintSection("5. JOINS (Join, GroupJoin, Left Join pattern)");

        // Q1: Inner join — orders with customer names
        ConsoleHelper.PrintQuery(
            "Orders with customer names (inner join)",
            "Orders.Join(Customers, o => o.CustomerId, c => c.Id, (o, c) => new { o.Id, c.Name, o.TotalAmount })");
        var q1 = SampleData.Orders
            .Join(SampleData.Customers, o => o.CustomerId, c => c.Id,
                (o, c) => $"Order {o.Id}: {c.Name} — ${o.TotalAmount}")
            .ToList();
        ConsoleHelper.PrintResult("Result", q1);

        // Q2: Join order items to product names with quantity
        ConsoleHelper.PrintQuery(
            "Order line items: product name × quantity",
            "OrderItems.Join(Products, oi => oi.ProductId, p => p.Id, (oi, p) => $\"{p.Name} x{oi.Quantity}\")");
        var q2 = SampleData.OrderItems
            .Join(SampleData.Products, oi => oi.ProductId, p => p.Id,
                (oi, p) => $"Order {oi.OrderId}: {p.Name} x{oi.Quantity}")
            .Take(8)
            .ToList();
        ConsoleHelper.PrintResult("Result (first 8)", q2);

        // Q3: Left join — all customers with order count (including 0)
        ConsoleHelper.PrintQuery(
            "All customers with order count (left join via GroupJoin + SelectMany)",
            "Customers.GroupJoin(Orders, c => c.Id, o => o.CustomerId, (c, orders) => new { c.Name, Count = orders.Count() })");
        var q3 = SampleData.Customers
            .GroupJoin(SampleData.Orders, c => c.Id, o => o.CustomerId,
                (c, orders) => $"{c.Name}: {orders.Count()} orders")
            .ToList();
        ConsoleHelper.PrintResult("Result", q3);

        // Q4: Left join with default — customers and their latest order date
        ConsoleHelper.PrintQuery(
            "Customer + latest order date (null if none)",
            "Customers.GroupJoin(...).Select(c => new { c.Name, Latest = orders.MaxBy(o => o.OrderDate)?.OrderDate })");
        var q4 = SampleData.Customers
            .GroupJoin(SampleData.Orders, c => c.Id, o => o.CustomerId,
                (c, orders) => new
                {
                    c.Name,
                    Latest = orders.MaxBy(o => o.OrderDate)?.OrderDate
                })
            .Select(x => x.Latest.HasValue
                ? $"{x.Name}: latest {x.Latest:yyyy-MM-dd}"
                : $"{x.Name}: no orders")
            .ToList();
        ConsoleHelper.PrintResult("Result", q4);

        // Q5: Student-course enrollment join
        ConsoleHelper.PrintQuery(
            "Student enrollments with course title and grade",
            "Enrollments.Join(Students,...).Join(Courses,...)");
        var q5 = SampleData.Enrollments
            .Join(SampleData.Students, e => e.StudentId, s => s.Id,
                (e, s) => new { e, s })
            .Join(SampleData.Courses, x => x.e.CourseId, c => c.Id,
                (x, c) => $"{x.s.Name} — {c.Title}: {x.e.Grade}%")
            .ToList();
        ConsoleHelper.PrintResult("Result", q5);

        // Q6: Self-join — employees with their manager name
        ConsoleHelper.PrintQuery(
            "Employees with manager names (self-join)",
            "Employees.GroupJoin(Employees, e => e.ManagerId, m => m.Id, (e, mgrs) => ...)");
        var q6 = SampleData.Employees
            .Where(e => e.ManagerId.HasValue)
            .Join(SampleData.Employees, e => e.ManagerId, m => m.Id,
                (e, m) => $"{e.Name} reports to {m.Name}")
            .ToList();
        ConsoleHelper.PrintResult("Result", q6);
    }
}
