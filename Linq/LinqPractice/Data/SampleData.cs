using LinqPractice.Models;

namespace LinqPractice.Data;

public static class SampleData
{
    public static IReadOnlyList<Department> Departments { get; } =
    [
        new(1, "Engineering", "Building A", 500000m),
        new(2, "Sales", "Building B", 300000m),
        new(3, "HR", "Building C", 150000m),
        new(4, "Marketing", "Building B", 200000m),
    ];

    public static IReadOnlyList<EmployeeEntity> EmployeeEntities { get; } =
    [
        new(1, "Alice Johnson", 1, 95000, new DateTime(2019, 3, 15), "Seattle", null),
        new(2, "Bob Smith", 1, 82000, new DateTime(2020, 7, 1), "Seattle", 1),
        new(3, "Carol White", 2, 72000, new DateTime(2018, 11, 20), "Chicago", null),
        new(4, "David Lee", 2, 68000, new DateTime(2021, 2, 10), "Chicago", 3),
        new(5, "Eve Martinez", 3, 65000, new DateTime(2017, 5, 5), "Austin", null),
        new(6, "Frank Brown", 1, 105000, new DateTime(2016, 9, 12), "Seattle", 1),
        new(7, "Grace Kim", 4, 71000, new DateTime(2022, 1, 18), "Austin", null),
        new(8, "Henry Davis", 1, 78000, new DateTime(2023, 6, 30), "Denver", 6),
        new(9, "Ivy Chen", 2, 75000, new DateTime(2019, 8, 22), "Chicago", 3),
        new(10, "Jack Wilson", 3, 62000, new DateTime(2020, 12, 1), "Austin", 5),
    ];

    public static IReadOnlyList<Employee> Employees { get; } =
    [
        new(1, "Alice Johnson", "Engineering", 95000, new DateTime(2019, 3, 15), "Seattle", null),
        new(2, "Bob Smith", "Engineering", 82000, new DateTime(2020, 7, 1), "Seattle", 1),
        new(3, "Carol White", "Sales", 72000, new DateTime(2018, 11, 20), "Chicago", null),
        new(4, "David Lee", "Sales", 68000, new DateTime(2021, 2, 10), "Chicago", 3),
        new(5, "Eve Martinez", "HR", 65000, new DateTime(2017, 5, 5), "Austin", null),
        new(6, "Frank Brown", "Engineering", 105000, new DateTime(2016, 9, 12), "Seattle", 1),
        new(7, "Grace Kim", "Marketing", 71000, new DateTime(2022, 1, 18), "Austin", null),
        new(8, "Henry Davis", "Engineering", 78000, new DateTime(2023, 6, 30), "Denver", 6),
        new(9, "Ivy Chen", "Sales", 75000, new DateTime(2019, 8, 22), "Chicago", 3),
        new(10, "Jack Wilson", "HR", 62000, new DateTime(2020, 12, 1), "Austin", 5),
    ];

    public static IReadOnlyList<Product> Products { get; } =
    [
        new(1, "Laptop Pro", "Electronics", 1299.99m, 45, true),
        new(2, "Wireless Mouse", "Electronics", 29.99m, 200, true),
        new(3, "Office Chair", "Furniture", 349.99m, 30, true),
        new(4, "Standing Desk", "Furniture", 599.99m, 15, true),
        new(5, "USB-C Hub", "Electronics", 49.99m, 0, true),
        new(6, "Monitor 27\"", "Electronics", 399.99m, 60, true),
        new(7, "Notebook Pack", "Stationery", 12.99m, 500, true),
        new(8, "Legacy Printer", "Electronics", 199.99m, 5, false),
        new(9, "Desk Lamp", "Furniture", 59.99m, 80, true),
        new(10, "Ergonomic Keyboard", "Electronics", 89.99m, 120, true),
    ];

    public static IReadOnlyList<Customer> Customers { get; } =
    [
        new(1, "Acme Corp", "billing@acme.com", "USA", new DateTime(2020, 1, 10)),
        new(2, "Globex Ltd", "orders@globex.com", "UK", new DateTime(2019, 6, 5)),
        new(3, "Initech", "ap@initech.com", "USA", new DateTime(2021, 3, 20)),
        new(4, "Umbrella Inc", "finance@umbrella.com", "Japan", new DateTime(2018, 11, 1)),
        new(5, "Stark Industries", "procurement@stark.com", "USA", new DateTime(2017, 8, 15)),
    ];

    public static IReadOnlyList<Order> Orders { get; } =
    [
        new(101, 1, new DateTime(2024, 1, 5), "Completed", 1349.98m),
        new(102, 2, new DateTime(2024, 1, 12), "Completed", 649.98m),
        new(103, 1, new DateTime(2024, 2, 3), "Completed", 89.99m),
        new(104, 3, new DateTime(2024, 2, 18), "Pending", 1299.99m),
        new(105, 4, new DateTime(2024, 3, 1), "Completed", 459.97m),
        new(106, 5, new DateTime(2024, 3, 10), "Cancelled", 599.99m),
        new(107, 2, new DateTime(2024, 3, 22), "Completed", 1699.97m),
        new(108, 1, new DateTime(2024, 4, 2), "Shipped", 399.99m),
        new(109, 3, new DateTime(2024, 4, 15), "Completed", 72.97m),
        new(110, 5, new DateTime(2024, 5, 1), "Completed", 949.98m),
    ];

    public static IReadOnlyList<OrderItem> OrderItems { get; } =
    [
        new(101, 1, 1, 1299.99m),
        new(101, 2, 1, 49.99m),
        new(102, 3, 1, 349.99m),
        new(102, 9, 5, 59.99m),
        new(103, 10, 1, 89.99m),
        new(104, 1, 1, 1299.99m),
        new(105, 6, 1, 399.99m),
        new(105, 7, 5, 12.99m),
        new(106, 4, 1, 599.99m),
        new(107, 1, 1, 1299.99m),
        new(107, 6, 1, 399.99m),
        new(108, 6, 1, 399.99m),
        new(109, 2, 2, 29.99m),
        new(109, 7, 1, 12.99m),
        new(110, 1, 1, 1299.99m),
        new(110, 3, 1, 349.99m),
        new(110, 10, 3, 89.99m),
    ];

    public static IReadOnlyList<Student> Students { get; } =
    [
        new(1, "Emma Thompson", 20, "Computer Science", 3.8),
        new(2, "Liam O'Brien", 22, "Mathematics", 3.5),
        new(3, "Sophia Garcia", 19, "Computer Science", 3.9),
        new(4, "Noah Patel", 21, "Physics", 3.2),
        new(5, "Olivia Nguyen", 20, "Computer Science", 3.7),
        new(6, "Ethan Brooks", 23, "Mathematics", 3.1),
    ];

    public static IReadOnlyList<Course> Courses { get; } =
    [
        new(1, "Data Structures", "Computer Science", 4),
        new(2, "Calculus II", "Mathematics", 4),
        new(3, "Algorithms", "Computer Science", 4),
        new(4, "Linear Algebra", "Mathematics", 3),
        new(5, "Database Systems", "Computer Science", 3),
        new(6, "Quantum Mechanics", "Physics", 4),
    ];

    public static IReadOnlyList<Enrollment> Enrollments { get; } =
    [
        new(1, 1, 92),
        new(1, 3, 88),
        new(1, 5, 95),
        new(2, 2, 78),
        new(2, 4, 82),
        new(3, 1, 97),
        new(3, 3, 94),
        new(3, 5, 91),
        new(4, 2, 70),
        new(4, 6, 75),
        new(5, 1, 85),
        new(5, 3, 89),
        new(6, 2, 65),
        new(6, 4, 68),
    ];

    public static IReadOnlyList<int> Numbers { get; } =
        Enumerable.Range(1, 20).ToList();

    public static IReadOnlyList<string> Words { get; } =
    [
        "apple", "banana", "apricot", "blueberry", "avocado",
        "cherry", "apricot", "date", "elderberry", "fig"
    ];
}
