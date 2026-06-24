namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class StrategyPattern
{
    internal static void Run()
    {
        var checkout = new DeliveryCheckout(new StandardDeliveryStrategy());
        Console.WriteLine(checkout.CalculateFee(5.2m));
        checkout.SetStrategy(new ExpressDeliveryStrategy());
        Console.WriteLine(checkout.CalculateFee(5.2m));
    }
}

internal interface IDeliveryFeeStrategy { string Calculate(decimal distanceKm); }
internal sealed class StandardDeliveryStrategy : IDeliveryFeeStrategy
{
    public string Calculate(decimal distanceKm) => $"Strategy -> Standard delivery fee: {(2.99m + distanceKm * 0.50m):C}";
}
internal sealed class ExpressDeliveryStrategy : IDeliveryFeeStrategy
{
    public string Calculate(decimal distanceKm) => $"Strategy -> Express delivery fee: {(5.99m + distanceKm * 0.75m):C}";
}
internal sealed class DeliveryCheckout(IDeliveryFeeStrategy strategy)
{
    private IDeliveryFeeStrategy _strategy = strategy;
    internal void SetStrategy(IDeliveryFeeStrategy strategy) => _strategy = strategy;
    internal string CalculateFee(decimal distanceKm) => _strategy.Calculate(distanceKm);
}
