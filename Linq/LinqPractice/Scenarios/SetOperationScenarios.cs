using LinqPractice.Data;
using LinqPractice.Helpers;

namespace LinqPractice.Scenarios;

/// <summary>
/// Set operations — Union, Intersect, Except, Distinct.
/// </summary>
public static class SetOperationScenarios
{
    public static void RunAll()
    {
        ConsoleHelper.PrintSection("8. SET OPERATIONS (Union, Intersect, Except)");

        var engineeringCities = SampleData.Employees
            .Where(e => e.Department == "Engineering")
            .Select(e => e.City);
        var salesCities = SampleData.Employees
            .Where(e => e.Department == "Sales")
            .Select(e => e.City);

        // Q1: Union — cities with Engineering OR Sales
        ConsoleHelper.PrintQuery(
            "Cities with Engineering OR Sales employees",
            "engineeringCities.Union(salesCities)");
        var q1 = engineeringCities.Union(salesCities).OrderBy(c => c).ToList();
        ConsoleHelper.PrintResult("Result", q1);

        // Q2: Intersect — cities with both departments
        ConsoleHelper.PrintQuery(
            "Cities with BOTH Engineering AND Sales",
            "engineeringCities.Intersect(salesCities)");
        var q2 = engineeringCities.Intersect(salesCities).ToList();
        ConsoleHelper.PrintResult("Result", q2);

        // Q3: Except — Engineering cities not in Sales
        ConsoleHelper.PrintQuery(
            "Engineering cities excluding Sales cities",
            "engineeringCities.Except(salesCities)");
        var q3 = engineeringCities.Except(salesCities).ToList();
        ConsoleHelper.PrintResult("Result", q3);

        // Q4: Distinct product categories from active products
        ConsoleHelper.PrintQuery(
            "Distinct categories of active products",
            "Products.Where(p => p.IsActive).Select(p => p.Category).Distinct()");
        var q4 = SampleData.Products
            .Where(p => p.IsActive)
            .Select(p => p.Category)
            .Distinct()
            .OrderBy(c => c)
            .ToList();
        ConsoleHelper.PrintResult("Result", q4);

        // Q5: Customers who ordered in Q1 2024 vs Q2 2024
        var q1Customers = SampleData.Orders
            .Where(o => o.OrderDate >= new DateTime(2024, 1, 1) && o.OrderDate < new DateTime(2024, 4, 1))
            .Select(o => o.CustomerId);
        var q2Customers = SampleData.Orders
            .Where(o => o.OrderDate >= new DateTime(2024, 4, 1) && o.OrderDate < new DateTime(2024, 7, 1))
            .Select(o => o.CustomerId);

        ConsoleHelper.PrintQuery(
            "Customers who ordered in Q1 but NOT in Q2 2024",
            "q1Customers.Except(q2Customers) joined to customer names");
        var q5 = q1Customers
            .Except(q2Customers)
            .Join(SampleData.Customers, id => id, c => c.Id, (_, c) => c.Name)
            .ToList();
        ConsoleHelper.PrintResult("Result", q5);
    }
}
