namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class AdapterPattern
{
    internal static void Run()
    {
        IPizzaCheckout checkout = new LegacyPosAdapter(new LegacyPosTerminal());
        checkout.Charge(24.99m, "Order #1042");
    }
}

internal interface IPizzaCheckout { void Charge(decimal amount, string orderId); }
internal sealed class LegacyPosTerminal
{
    public void SwipeCard(decimal total, string reference) =>
        Console.WriteLine($"Adapter -> Legacy POS charged {total:C} for {reference}");
}
internal sealed class LegacyPosAdapter : IPizzaCheckout
{
    private readonly LegacyPosTerminal _terminal;
    internal LegacyPosAdapter(LegacyPosTerminal terminal) => _terminal = terminal;
    public void Charge(decimal amount, string orderId) => _terminal.SwipeCard(amount, orderId);
}
