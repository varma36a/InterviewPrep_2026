namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class FacadePattern
{
    internal static void Run()
    {
        var filingFacade = new TaxFilingFacade();
        filingFacade.FileReturn("Tenant-A");
    }
}

internal sealed class TaxValidationService { internal bool Validate(string tenant) { Console.WriteLine($"Facade -> Validation done for {tenant}"); return true; } }
internal sealed class TaxSubmissionService { internal void Submit(string tenant) => Console.WriteLine($"Facade -> Submitted return for {tenant}"); }
internal sealed class NotificationService { internal void Notify(string tenant) => Console.WriteLine($"Facade -> Notified {tenant}"); }

internal sealed class TaxFilingFacade
{
    private readonly TaxValidationService _validator = new();
    private readonly TaxSubmissionService _submitter = new();
    private readonly NotificationService _notifier = new();
    internal void FileReturn(string tenant)
    {
        if (_validator.Validate(tenant))
        {
            _submitter.Submit(tenant);
            _notifier.Notify(tenant);
        }
    }
}
