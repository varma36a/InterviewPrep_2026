using LinqPractice.Data;
using LinqPractice.Helpers;
using LinqPractice.Models;

namespace LinqPractice.Scenarios;

/// <summary>
/// N+1 query problem — classic EF/LINQ interview topic with Employees + Departments.
/// </summary>
public static class NPlusOneScenarios
{
    public static void RunAll()
    {
        ConsoleHelper.PrintSection("11. N+1 PROBLEM (Employees + Departments)");

        var repo = new SimulatedEmployeeRepository(
            SampleData.EmployeeEntities,
            SampleData.Departments);

        DemonstrateNPlusOneProblem(repo);
        DemonstrateLookupFix(repo);
        DemonstrateJoinFix(repo);
        DemonstrateEagerLoadingPattern(repo);
        ShowInterviewTalkingPoints();
    }

    /// <summary>
    /// BAD: 1 query for employees + N queries for each employee's department = N+1
    /// </summary>
    private static void DemonstrateNPlusOneProblem(SimulatedEmployeeRepository repo)
    {
        Console.WriteLine();
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("❌ N+1 PROBLEM — Load employees, then fetch department inside loop");
        Console.ResetColor();
        ConsoleHelper.PrintQuery(
            "List each employee with department name and budget",
            "var emps = GetAllEmployees(); foreach (e in emps) { var dept = GetDepartmentById(e.DepartmentId); }");

        repo.ResetQueryCount();

        var employees = repo.GetAllEmployees();
        var results = new List<string>();

        foreach (var employee in employees)
        {
            // N additional queries — one per employee!
            var department = repo.GetDepartmentById(employee.DepartmentId);
            results.Add(
                $"{employee.Name} | {department?.Name} ({department?.Location}) | dept budget ${department?.Budget:N0}");
        }

        ConsoleHelper.PrintResult("Result", results);
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine($"  Total DB queries: {repo.QueryCount}  (= 1 + {employees.Count} employees = N+1)");
        Console.ResetColor();

        Console.WriteLine();
        Console.ForegroundColor = ConsoleColor.DarkGray;
        Console.WriteLine("  // Typical EF anti-pattern that causes this:");
        Console.WriteLine("  var employees = await _context.Employees.ToListAsync();  // 1 query");
        Console.WriteLine("  foreach (var e in employees)");
        Console.WriteLine("  {");
        Console.WriteLine("      var dept = await _context.Departments.FindAsync(e.DepartmentId);  // N queries");
        Console.WriteLine("  }");
        Console.ResetColor();
    }

    /// <summary>
    /// FIX 1: Load departments once into a dictionary — 2 queries total
    /// </summary>
    private static void DemonstrateLookupFix(SimulatedEmployeeRepository repo)
    {
        Console.WriteLine();
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("✅ FIX 1 — ToDictionary / lookup (2 queries: employees + all departments)");
        Console.ResetColor();
        ConsoleHelper.PrintQuery(
            "Pre-load departments into Dictionary, then join in memory",
            "var deptMap = GetAllDepartments().ToDictionary(d => d.Id); emps.Select(e => deptMap[e.DepartmentId])");

        repo.ResetQueryCount();

        var employees = repo.GetAllEmployees();
        var departmentMap = repo.GetAllDepartments().ToDictionary(d => d.Id);

        var results = employees
            .Select(e =>
            {
                var dept = departmentMap[e.DepartmentId];
                return $"{e.Name} | {dept.Name} ({dept.Location}) | dept budget ${dept.Budget:N0}";
            })
            .ToList();

        ConsoleHelper.PrintResult("Result", results);
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine($"  Total DB queries: {repo.QueryCount}  (constant — does NOT grow with employee count)");
        Console.ResetColor();
    }

    /// <summary>
    /// FIX 2: Single SQL JOIN — 1 query total
    /// </summary>
    private static void DemonstrateJoinFix(SimulatedEmployeeRepository repo)
    {
        Console.WriteLine();
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("✅ FIX 2 — Single JOIN query (best for relational DBs)");
        Console.ResetColor();
        ConsoleHelper.PrintQuery(
            "One query with INNER JOIN",
            "Employees.Join(Departments, e => e.DepartmentId, d => d.Id, (e, d) => ...)");

        repo.ResetQueryCount();

        var results = repo.GetEmployeesWithDepartmentsSingleQuery()
            .Select(x => $"{x.EmployeeName} | {x.DepartmentName} ({x.DepartmentLocation}) | dept budget ${x.DepartmentBudget:N0}")
            .ToList();

        ConsoleHelper.PrintResult("Result", results);
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine($"  Total DB queries: {repo.QueryCount}  (single round-trip)");
        Console.ResetColor();

        Console.WriteLine();
        Console.ForegroundColor = ConsoleColor.DarkGray;
        Console.WriteLine("  // EF Core equivalent:");
        Console.WriteLine("  var data = await _context.Employees");
        Console.WriteLine("      .Include(e => e.Department)   // eager load — 1 query with JOIN");
        Console.WriteLine("      .ToListAsync();");
        Console.ResetColor();
    }

    /// <summary>
    /// FIX 3: Projection in one query — only fetch columns you need
    /// </summary>
    private static void DemonstrateEagerLoadingPattern(SimulatedEmployeeRepository repo)
    {
        Console.WriteLine();
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("✅ FIX 3 — Project in one LINQ query (no loop, no N+1)");
        Console.ResetColor();
        ConsoleHelper.PrintQuery(
            "Departments with employee count — GroupJoin avoids N+1",
            "Departments.GroupJoin(Employees, d => d.Id, e => e.DepartmentId, ...)");

        repo.ResetQueryCount();

        repo.GetAllDepartments(); // simulate 1 query
        repo.GetAllEmployees();   // simulate 1 query — in EF this could be one query with GroupJoin

        var results = SampleData.Departments
            .GroupJoin(
                SampleData.EmployeeEntities,
                d => d.Id,
                e => e.DepartmentId,
                (d, emps) => new
                {
                    d.Name,
                    d.Budget,
                    Headcount = emps.Count(),
                    TotalPayroll = emps.Sum(e => e.Salary)
                })
            .Select(x => $"{x.Name}: {x.Headcount} employees, payroll ${x.TotalPayroll:N0} / budget ${x.Budget:N0}")
            .ToList();

        ConsoleHelper.PrintResult("Result", results);
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine($"  Total DB queries: {repo.QueryCount}  (2 queries — or 1 with proper GroupJoin SQL)");
        Console.ResetColor();
    }

    private static void ShowInterviewTalkingPoints()
    {
        Console.WriteLine();
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Interview talking points:");
        Console.ResetColor();
        Console.WriteLine("""
              • N+1 = 1 query for parent rows + N queries for related rows (one per item in a loop)
              • Symptom: page/API gets slower as data grows; SQL profiler shows repeated similar queries
              • Fixes: Include()/ThenInclude(), explicit Join, Select projection, or batch load + dictionary
              • EF Core: use .AsSplitQuery() carefully; prefer .Include() over lazy loading in loops
              • Detect: enable SQL logging, use MiniProfiler or EF Core logging in development
            """);
    }
}
