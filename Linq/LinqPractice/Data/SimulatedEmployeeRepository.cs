using LinqPractice.Models;

namespace LinqPractice.Data;

/// <summary>
/// Simulates a database/EF context. Each method call = 1 round-trip to the DB.
/// </summary>
public class SimulatedEmployeeRepository
{
    private readonly IReadOnlyList<EmployeeEntity> _employees;
    private readonly IReadOnlyList<Department> _departments;
    private int _queryCount;

    public SimulatedEmployeeRepository(
        IReadOnlyList<EmployeeEntity> employees,
        IReadOnlyList<Department> departments)
    {
        _employees = employees;
        _departments = departments;
    }

    public int QueryCount => _queryCount;

    public void ResetQueryCount() => _queryCount = 0;

    private void LogQuery(string sql)
    {
        _queryCount++;
        Console.ForegroundColor = ConsoleColor.DarkYellow;
        Console.WriteLine($"  [Query #{_queryCount}] {sql}");
        Console.ResetColor();
    }

    // --- Simulated DB calls (1 query each) ---

    public IReadOnlyList<EmployeeEntity> GetAllEmployees()
    {
        LogQuery("SELECT * FROM Employees");
        return _employees.ToList();
    }

    public Department? GetDepartmentById(int departmentId)
    {
        LogQuery($"SELECT * FROM Departments WHERE Id = {departmentId}");
        return _departments.FirstOrDefault(d => d.Id == departmentId);
    }

    public IReadOnlyList<Department> GetAllDepartments()
    {
        LogQuery("SELECT * FROM Departments");
        return _departments.ToList();
    }

    /// <summary>
    /// EF equivalent: .Include(e => e.Department) or explicit JOIN in one query.
    /// </summary>
    public IReadOnlyList<EmployeeWithDepartment> GetEmployeesWithDepartmentsSingleQuery()
    {
        LogQuery("""
            SELECT e.Id, e.Name, e.Salary, e.City, d.Name, d.Location, d.Budget
            FROM Employees e
            INNER JOIN Departments d ON e.DepartmentId = d.Id
            """);

        return _employees
            .Join(_departments,
                e => e.DepartmentId,
                d => d.Id,
                (e, d) => new EmployeeWithDepartment(
                    e.Id, e.Name, e.Salary, e.City, d.Name, d.Location, d.Budget))
            .ToList();
    }
}
