namespace LinqPractice.Models;

/// <summary>
/// Relational employee model (FK to Department). Used for N+1 demos.
/// </summary>
public record EmployeeEntity(
    int Id,
    string Name,
    int DepartmentId,
    decimal Salary,
    DateTime HireDate,
    string City,
    int? ManagerId);

public record EmployeeWithDepartment(
    int EmployeeId,
    string EmployeeName,
    decimal Salary,
    string City,
    string DepartmentName,
    string DepartmentLocation,
    decimal DepartmentBudget);
