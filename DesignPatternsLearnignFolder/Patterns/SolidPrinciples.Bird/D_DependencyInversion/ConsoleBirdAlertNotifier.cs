namespace SolidPrinciples.Bird.D_DependencyInversion;

public sealed class ConsoleBirdAlertNotifier : IBirdAlertNotifier
{
    public Task NotifyAsync(string message, CancellationToken cancellationToken)
    {
        Console.WriteLine($"  [ALERT] {message}");
        return Task.CompletedTask;
    }
}
