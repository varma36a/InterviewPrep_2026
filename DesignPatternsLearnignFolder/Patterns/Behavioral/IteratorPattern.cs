using System.Collections;

namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class IteratorPattern
{
    internal static void Run()
    {
        var customerDirectory = new CustomerDirectory(new[] { "Asha", "Ravi", "Mira" });
        foreach (var customer in customerDirectory) Console.WriteLine($"Iterator -> Customer: {customer}");
    }
}

internal sealed class CustomerDirectory : IEnumerable<string>
{
    private readonly List<string> _customers;
    internal CustomerDirectory(IEnumerable<string> customers) => _customers = [.. customers];
    public IEnumerator<string> GetEnumerator() => _customers.GetEnumerator();
    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
}
