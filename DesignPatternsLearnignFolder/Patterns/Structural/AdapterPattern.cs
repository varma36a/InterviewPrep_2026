namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class AdapterPattern
{
    internal static void Run()
    {
        ILegacyPaymentProcessor payment = new PaymentGatewayAdapter(new LegacyPaymentGateway());
        payment.Process(2499m);
    }
}

internal interface ILegacyPaymentProcessor { void Process(decimal amount); }
internal sealed class LegacyPaymentGateway { public void MakePayment(decimal amount) => Console.WriteLine($"Adapter -> Paid {amount:C} via legacy gateway"); }
internal sealed class PaymentGatewayAdapter : ILegacyPaymentProcessor
{
    private readonly LegacyPaymentGateway _gateway;
    internal PaymentGatewayAdapter(LegacyPaymentGateway gateway) => _gateway = gateway;
    public void Process(decimal amount) => _gateway.MakePayment(amount);
}
