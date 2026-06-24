namespace LinqPractice.Models;

public record Order(
    int Id,
    int CustomerId,
    DateTime OrderDate,
    string Status,
    decimal TotalAmount);

public record OrderItem(
    int OrderId,
    int ProductId,
    int Quantity,
    decimal UnitPrice);
