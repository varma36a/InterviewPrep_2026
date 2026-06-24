using LinqPractice.Data;
using LinqPractice.Helpers;

namespace LinqPractice.Scenarios;

/// <summary>
/// LINQ query syntax (from / where / select) — mirrors method syntax used elsewhere.
/// Every example shows the query-syntax form; method syntax equivalent in the hint.
/// </summary>
public static class QuerySyntaxScenarios
{
    public static void RunAll()
    {
        BasicFiltering();
        // ProjectionAndLet();
        // SortingAndPaging();
        // Joins();
        // GroupJoinAndLeftJoin();
        // Grouping();
        // MultipleFromSelectMany();
        // Subqueries();
        // EmployeeDepartmentExamples();
        // ShowSyntaxCheatSheet();
    }

    private static void BasicFiltering()
    {
        ConsoleHelper.PrintSection("QUERY SYNTAX — 1. Basic Filtering");

        ConsoleHelper.PrintQuery(
            "Engineering employees earning over 80k",
            "from e in Employees where e.Department == \"Engineering\" && e.Salary > 80000 select e.Name");

        var q1 =
            from e in SampleData.Employees
            where e.Department == "Engineering" && e.Salary > 80000
            select e.Name;
        ConsoleHelper.PrintResult("Result", q1);

        ConsoleHelper.PrintQuery(
            "Active products in Electronics or Furniture",
            "from p in Products where p.IsActive && (p.Category == \"Electronics\" || ...) select p.Name");

        var q2 =
            from p in SampleData.Products
            where p.IsActive && (p.Category == "Electronics" || p.Category == "Furniture")
            select p.Name;
        ConsoleHelper.PrintResult("Result", q2);

        ConsoleHelper.PrintQuery(
            "Orders in Q1 2024 (Jan–Mar)",
            "from o in Orders where o.OrderDate >= ... && o.OrderDate < ... select o.Id");

        var q3 =
            from o in SampleData.Orders
            where o.OrderDate >= new DateTime(2024, 1, 1)
               && o.OrderDate < new DateTime(2024, 4, 1)
            select $"Order {o.Id} ({o.OrderDate:yyyy-MM-dd})";
        ConsoleHelper.PrintResult("Result", q3);
    }

    private static void ProjectionAndLet()
    {
        ConsoleHelper.PrintSection("QUERY SYNTAX — 2. Projection & let");

        ConsoleHelper.PrintQuery(
            "Anonymous projection: name + annual bonus (10% of salary)",
            "from e in Employees let bonus = e.Salary * 0.10m select new { e.Name, bonus }");

        var q1 =
            from e in SampleData.Employees
            let bonus = e.Salary * 0.10m
            select new { e.Name, Bonus = bonus };
        ConsoleHelper.PrintResult("Result",
            q1.Select(x => $"{x.Name}: bonus ${x.Bonus:F0}"));

        ConsoleHelper.PrintQuery(
            "let — compute tax bracket label from salary",
            "from e in Employees let bracket = e.Salary >= 90000 ? \"High\" : \"Standard\" select ...");

        var q2 =
            from e in SampleData.Employees
            let bracket = e.Salary >= 90000 ? "High" : "Standard"
            select $"{e.Name} ({bracket})";
        ConsoleHelper.PrintResult("Result", q2);

        ConsoleHelper.PrintQuery(
            "Select into named type (tuple)",
            "from p in Products select (p.Name, p.Price, InStock: p.Stock > 0)");

        var q3 =
            from p in SampleData.Products
            where p.Category == "Electronics"
            select (p.Name, p.Price, InStock: p.Stock > 0);
        ConsoleHelper.PrintResult("Result",
            q3.Select(x => $"{x.Name} ${x.Price} [{(x.InStock ? "in stock" : "out")}]"));
    }

    private static void SortingAndPaging()
    {
        ConsoleHelper.PrintSection("QUERY SYNTAX — 3. Sorting & Paging");

        ConsoleHelper.PrintQuery(
            "Top 3 highest paid (orderby descending + Take)",
            "from e in Employees orderby e.Salary descending select e.Name");

        var q1 = (
            from e in SampleData.Employees
            orderby e.Salary descending
            select $"{e.Name} (${e.Salary})"
        ).Take(3);
        ConsoleHelper.PrintResult("Result", q1);

        ConsoleHelper.PrintQuery(
            "Multi-key sort: department asc, salary desc",
            "from e in Employees orderby e.Department, e.Salary descending select ...");

        var q2 =
            from e in SampleData.Employees
            orderby e.Department, e.Salary descending
            select $"{e.Department} | {e.Name} (${e.Salary})";
        ConsoleHelper.PrintResult("Result", q2);

        ConsoleHelper.PrintQuery(
            "Pagination: skip 3, take 3 (page 2)",
            "(from e in Employees orderby e.Name select e.Name).Skip(3).Take(3)");

        var q3 = (
            from e in SampleData.Employees
            orderby e.Name
            select e.Name
        ).Skip(3).Take(3);
        ConsoleHelper.PrintResult("Result", q3);
    }

    private static void Joins()
    {
        ConsoleHelper.PrintSection("QUERY SYNTAX — 4. Inner Join");

        ConsoleHelper.PrintQuery(
            "Orders with customer name (inner join)",
            "from o in Orders join c in Customers on o.CustomerId equals c.Id select ...");

        var q1 =
            from o in SampleData.Orders
            join c in SampleData.Customers on o.CustomerId equals c.Id
            select $"Order {o.Id}: {c.Name} — ${o.TotalAmount}";
        ConsoleHelper.PrintResult("Result", q1);

        ConsoleHelper.PrintQuery(
            "Three-way join: order items → product name + quantity",
            "from oi in OrderItems join p in Products on oi.ProductId equals p.Id select ...");

        var q2 =
            from oi in SampleData.OrderItems
            join p in SampleData.Products on oi.ProductId equals p.Id
            select $"Order {oi.OrderId}: {p.Name} x{oi.Quantity}";
        ConsoleHelper.PrintResult("Result", q2.Take(8));

        ConsoleHelper.PrintQuery(
            "Join with filter in where clause",
            "from o in Orders join c in Customers on ... where o.Status == \"Completed\" select ...");

        var q3 =
            from o in SampleData.Orders
            join c in SampleData.Customers on o.CustomerId equals c.Id
            where o.Status == "Completed"
            select $"{c.Name}: ${o.TotalAmount}";
        ConsoleHelper.PrintResult("Result", q3);

        ConsoleHelper.PrintQuery(
            "Self-join: employee → manager name",
            "from e in Employees join m in Employees on e.ManagerId equals m.Id select ...");

        var q4 =
            from e in SampleData.Employees
            join m in SampleData.Employees on e.ManagerId equals m.Id
            select $"{e.Name} → manager: {m.Name}";
        ConsoleHelper.PrintResult("Result", q4);
    }

    private static void GroupJoinAndLeftJoin()
    {
        ConsoleHelper.PrintSection("QUERY SYNTAX — 5. Group Join & Left Join (join … into)");

        ConsoleHelper.PrintQuery(
            "Group join: each customer with their orders",
            "from c in Customers join o in Orders on c.Id equals o.CustomerId into orderGroup select ...");

        var q1 =
            from c in SampleData.Customers
            join o in SampleData.Orders on c.Id equals o.CustomerId into orderGroup
            select new
            {
                c.Name,
                OrderCount = orderGroup.Count(),
                Total = orderGroup.Sum(x => x.TotalAmount)
            };
        ConsoleHelper.PrintResult("Result",
            q1.Select(x => $"{x.Name}: {x.OrderCount} orders, ${x.Total:N2}"));

        ConsoleHelper.PrintQuery(
            "Group join aggregate — revenue per customer (0 if no orders)",
            "from c in Customers join o in Orders ... into g select new { c.Name, Revenue = g.Sum(o => o.TotalAmount) }");

        var q2 =
            from c in SampleData.Customers
            join o in SampleData.Orders on c.Id equals o.CustomerId into orders
            select new
            {
                c.Name,
                Revenue = orders.Sum(x => x.TotalAmount)
            };
        ConsoleHelper.PrintResult("Result",
            q2.Select(x => $"{x.Name}: ${x.Revenue:N2}"));

        ConsoleHelper.PrintQuery(
            "Left join via DefaultIfEmpty — list each order row (null if customer has none)",
            "from c in Customers join o in Orders ... into g from o in g.DefaultIfEmpty() select new { c.Name, o?.TotalAmount }");

        var q2b =
            from c in SampleData.Customers
            join o in SampleData.Orders on c.Id equals o.CustomerId into orders
            from o in orders.DefaultIfEmpty()
            select new { c.Name, Amount = o?.TotalAmount };
        ConsoleHelper.PrintResult("Result (flattened rows)",
            q2b.Select(x => x.Amount is null ? $"{x.Name}: (no orders)" : $"{x.Name}: ${x.Amount}"));

        ConsoleHelper.PrintQuery(
            "Group join into + let — departments with employee names",
            "from d in Departments join e in EmployeeEntities on d.Id equals e.DepartmentId into emps select ...");

        var q3 =
            from d in SampleData.Departments
            join e in SampleData.EmployeeEntities on d.Id equals e.DepartmentId into emps
            let names = emps.Select(x => x.Name).ToList()
            select $"{d.Name}: [{string.Join(", ", names)}]";
        ConsoleHelper.PrintResult("Result", q3);
    }

    private static void Grouping()
    {
        ConsoleHelper.PrintSection("QUERY SYNTAX — 6. Group By");

        ConsoleHelper.PrintQuery(
            "Count employees per department",
            "from e in Employees group e by e.Department into g select new { Dept = g.Key, Count = g.Count() }");

        var q1 =
            from e in SampleData.Employees
            group e by e.Department into g
            select new { Dept = g.Key, Count = g.Count() };
        ConsoleHelper.PrintResult("Result",
            q1.Select(x => $"{x.Dept}: {x.Count}"));

        ConsoleHelper.PrintQuery(
            "Average salary per department",
            "from e in Employees group e by e.Department into g select new { g.Key, Avg = g.Average(e => e.Salary) }");

        var q2 =
            from e in SampleData.Employees
            group e by e.Department into g
            select new { g.Key, Avg = g.Average(e => e.Salary) };
        ConsoleHelper.PrintResult("Result",
            q2.Select(x => $"{x.Key}: avg ${x.Avg:F0}"));

        ConsoleHelper.PrintQuery(
            "Group with where (having) — departments avg salary > 70k",
            "from e in Employees group e by e.Department into g where g.Average(...) > 70000 select g.Key");

        var q3 =
            from e in SampleData.Employees
            group e by e.Department into g
            where g.Average(e => e.Salary) > 70000
            select g.Key;
        ConsoleHelper.PrintResult("Result", q3);

        ConsoleHelper.PrintQuery(
            "Nested group — city then department headcount",
            "from e in Employees group e by e.City into cityGroup from dept in cityGroup group dept by dept.Department select ...");

        var q4 =
            from e in SampleData.Employees
            group e by e.City into cityGroup
            from dept in cityGroup.GroupBy(x => x.Department)
            select $"{cityGroup.Key} / {dept.Key}: {dept.Count()}";
        ConsoleHelper.PrintResult("Result", q4);
    }

    private static void MultipleFromSelectMany()
    {
        ConsoleHelper.PrintSection("QUERY SYNTAX — 7. Multiple from (SelectMany / Cross Join)");

        ConsoleHelper.PrintQuery(
            "SelectMany — chars from words starting with 'a'",
            "from w in Words from c in w where w.StartsWith(\"a\") select c");

        var q1 =
            from w in SampleData.Words
            where w.StartsWith("a")
            from c in w
            select c;
        ConsoleHelper.PrintResult("Result", q1.Select(c => c.ToString()));

        ConsoleHelper.PrintQuery(
            "Cross join — every product paired with every customer (sample)",
            "from p in Products from c in Customers select new { p.Name, c.Name }");

        var q2 =
            from p in SampleData.Products.Take(3)
            from c in SampleData.Customers.Take(2)
            select $"{p.Name} → sold to {c.Name}";
        ConsoleHelper.PrintResult("Result", q2);

        ConsoleHelper.PrintQuery(
            "Multiple from with where — students enrolled in CS courses",
            "from en in Enrollments from s in Students from c in Courses where en.StudentId == s.Id && ... select ...");

        var q3 =
            from en in SampleData.Enrollments
            from s in SampleData.Students
            from c in SampleData.Courses
            where en.StudentId == s.Id
               && en.CourseId == c.Id
               && c.Department == "Computer Science"
            select $"{s.Name} took {c.Title} ({en.Grade}%)";
        ConsoleHelper.PrintResult("Result", q3);
    }

    private static void Subqueries()
    {
        ConsoleHelper.PrintSection("QUERY SYNTAX — 8. Subqueries in where & select");

        ConsoleHelper.PrintQuery(
            "where with subquery — employees earning above company average",
            "from e in Employees where e.Salary > (from x in Employees select x.Salary).Average() select e.Name");

        var avgSalary = SampleData.Employees.Average(e => e.Salary);
        var q1 =
            from e in SampleData.Employees
            where e.Salary > avgSalary
            select $"{e.Name} (${e.Salary})";
        ConsoleHelper.PrintResult("Result", q1);
        ConsoleHelper.PrintScalar("Company avg", $"${avgSalary:F0}");

        ConsoleHelper.PrintQuery(
            "where Any — customers who have a pending order",
            "from c in Customers where Orders.Any(o => o.CustomerId == c.Id && o.Status == \"Pending\") select c.Name");

        var q2 =
            from c in SampleData.Customers
            where SampleData.Orders.Any(o => o.CustomerId == c.Id && o.Status == "Pending")
            select c.Name;
        ConsoleHelper.PrintResult("Result", q2);

        ConsoleHelper.PrintQuery(
            "select with subquery — each product's total units sold",
            "from p in Products select new { p.Name, Sold = (from oi in OrderItems where oi.ProductId == p.Id select oi.Quantity).Sum() }");

        var q3 =
            from p in SampleData.Products
            select new
            {
                p.Name,
                Sold = (
                    from oi in SampleData.OrderItems
                    where oi.ProductId == p.Id
                    select oi.Quantity
                ).Sum()
            };
        ConsoleHelper.PrintResult("Result",
            q3.Select(x => $"{x.Name}: {x.Sold} sold"));

        ConsoleHelper.PrintQuery(
            "where Count — departments with more than 2 employees",
            "from d in Departments where EmployeeEntities.Count(e => e.DepartmentId == d.Id) > 2 select d.Name");

        var q4 =
            from d in SampleData.Departments
            where SampleData.EmployeeEntities.Count(e => e.DepartmentId == d.Id) > 2
            select d.Name;
        ConsoleHelper.PrintResult("Result", q4);
    }

    private static void EmployeeDepartmentExamples()
    {
        ConsoleHelper.PrintSection("QUERY SYNTAX — 9. Employee + Department (relational)");

        ConsoleHelper.PrintQuery(
            "Inner join — employees with department details",
            "from e in EmployeeEntities join d in Departments on e.DepartmentId equals d.Id select ...");

        var q1 =
            from e in SampleData.EmployeeEntities
            join d in SampleData.Departments on e.DepartmentId equals d.Id
            select $"{e.Name} | {d.Name} @ {d.Location} | budget ${d.Budget:N0}";
        ConsoleHelper.PrintResult("Result", q1);

        ConsoleHelper.PrintQuery(
            "Join + group — department payroll vs budget",
            "from e in EmployeeEntities join d in Departments ... group by d into g select ...");

        var q2 =
            from e in SampleData.EmployeeEntities
            join d in SampleData.Departments on e.DepartmentId equals d.Id
            group e by d into g
            select new
            {
                Dept = g.Key.Name,
                Payroll = g.Sum(x => x.Salary),
                g.Key.Budget
            };
        ConsoleHelper.PrintResult("Result",
            q2.Select(x => $"{x.Dept}: payroll ${x.Payroll:N0} / budget ${x.Budget:N0}"));

        ConsoleHelper.PrintQuery(
            "Left join — all departments even if no employees (Marketing has 1, add empty dept demo)",
            "from d in Departments join e in EmployeeEntities ... into emps from e in emps.DefaultIfEmpty() ...");

        var q3 =
            from d in SampleData.Departments
            join e in SampleData.EmployeeEntities on d.Id equals e.DepartmentId into emps
            select new
            {
                d.Name,
                Headcount = emps.Count()
            };
        ConsoleHelper.PrintResult("Result",
            q3.Select(x => $"{x.Name}: {x.Headcount} employees"));
    }

    private static void ShowSyntaxCheatSheet()
    {
        ConsoleHelper.PrintSection("QUERY SYNTAX — Cheat Sheet (method ↔ query)");

        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("""
            Operation          Query Syntax                          Method Syntax
            ─────────────────────────────────────────────────────────────────────────
            Filter             where condition                       .Where(x => ...)
            Project            select x                              .Select(x => ...)
            Sort               orderby x, y descending               .OrderBy().ThenByDescending()
            Take / Skip        (append).Take(n).Skip(n)              .Take(n).Skip(n)
            Join               join b in B on a.Id equals b.AId      .Join(B, a => a.Id, b => b.AId, ...)
            Left join          join ... into g from x in g.DefaultIfEmpty()   .GroupJoin(...).SelectMany(g => g.DefaultIfEmpty())
            Group              group x by x.Key into g               .GroupBy(x => x.Key)
            Flatten            from a in A from b in a.Items         .SelectMany(a => a.Items)
            Local variable     let total = x.Price * x.Qty           (inline or .Select with calc)
            Distinct           select ... (then .Distinct())         .Distinct()
            First/Any/Count    (query then).First() / use in where   .First() / .Any() / .Count()

            Notes:
            • Query syntax compiles to method syntax — they are equivalent
            • Use query syntax for joins & multiple from; method syntax for simple chains
            • Not all operators have query keywords (Take, Skip, Distinct, First → method at end)
            """);
        Console.ResetColor();
    }
}
