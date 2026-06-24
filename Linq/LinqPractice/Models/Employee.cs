namespace LinqPractice.Models;

public record Employee(
    int Id,
    string Name,
    string Department,
    decimal Salary,
    DateTime HireDate,
    string City,
    int? ManagerId);
