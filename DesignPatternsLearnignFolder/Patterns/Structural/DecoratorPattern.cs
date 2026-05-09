namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class DecoratorPattern
{
    internal static void Run()
    {
        IInvoiceService invoiceService = new InvoiceService();
        invoiceService = new AuditInvoiceDecorator(invoiceService);
        invoiceService.GenerateInvoice("INV-9001");
    }
}

internal interface IInvoiceService { void GenerateInvoice(string invoiceNumber); }
internal sealed class InvoiceService : IInvoiceService { public void GenerateInvoice(string invoiceNumber) => Console.WriteLine($"Decorator -> Generated invoice {invoiceNumber}"); }
internal abstract class InvoiceDecorator(IInvoiceService service) : IInvoiceService
{
    protected readonly IInvoiceService Service = service;
    public virtual void GenerateInvoice(string invoiceNumber) => Service.GenerateInvoice(invoiceNumber);
}
internal sealed class AuditInvoiceDecorator(IInvoiceService service) : InvoiceDecorator(service)
{
    public override void GenerateInvoice(string invoiceNumber)
    {
        Console.WriteLine($"Decorator -> Audit start for {invoiceNumber}");
        base.GenerateInvoice(invoiceNumber);
        Console.WriteLine($"Decorator -> Audit end for {invoiceNumber}");
    }
}
