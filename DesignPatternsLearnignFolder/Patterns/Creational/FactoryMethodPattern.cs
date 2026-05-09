namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class FactoryMethodPattern
{
    internal static void Run()
    {
        INotification email = NotificationFactory.Create("email");
        INotification sms = NotificationFactory.Create("sms");
        email.Send("Invoice generated");
        sms.Send("OTP: 483210");
    }
}

internal interface INotification { void Send(string message); }
internal sealed class EmailNotification : INotification { public void Send(string message) => Console.WriteLine($"Factory -> Email: {message}"); }
internal sealed class SmsNotification : INotification { public void Send(string message) => Console.WriteLine($"Factory -> SMS: {message}"); }
internal static class NotificationFactory
{
    internal static INotification Create(string type) => type.ToLowerInvariant() switch
    {
        "email" => new EmailNotification(),
        "sms" => new SmsNotification(),
        _ => throw new ArgumentException("Unsupported notification type.")
    };
}
