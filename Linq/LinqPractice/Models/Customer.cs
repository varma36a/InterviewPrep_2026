namespace LinqPractice.Models;

public record Customer(
    int Id,
    string Name,
    string Email,
    string Country,
    DateTime RegisteredOn);
