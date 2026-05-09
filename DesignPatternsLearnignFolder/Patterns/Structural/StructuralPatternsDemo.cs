using DesignPatternsLearnignFolder.Patterns.Shared;

namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class StructuralPatternsDemo
{
    internal static void Run()
    {
        ConsoleSection.Print("STRUCTURAL PATTERNS");

        ILegacyPaymentProcessor payment = new PaymentGatewayAdapter(new LegacyPaymentGateway());
        payment.Process(2499m);

        Report payrollPdf = new PayrollReport(new PdfExporter());
        Report taxExcel = new TaxReport(new ExcelExporter());
        payrollPdf.Export();
        taxExcel.Export();

        var ceo = new EmployeeNode("CEO");
        var techLead = new EmployeeNode("Tech Lead");
        techLead.Add(new EmployeeLeaf("Backend Dev"));
        techLead.Add(new EmployeeLeaf("Frontend Dev"));
        ceo.Add(techLead);
        ceo.Add(new EmployeeLeaf("Finance Head"));
        ceo.Display();

        IInvoiceService invoiceService = new InvoiceService();
        invoiceService = new AuditInvoiceDecorator(invoiceService);
        invoiceService.GenerateInvoice("INV-9001");

        var filingFacade = new TaxFilingFacade();
        filingFacade.FileReturn("Tenant-A");

        var docFactory = new DocumentTemplateFactory();
        var d1 = docFactory.GetTemplate("Invoice");
        var d2 = docFactory.GetTemplate("Invoice");
        Console.WriteLine($"Flyweight -> Shared template instance: {ReferenceEquals(d1, d2)}");

        IFinancialReport reportAccess = new FinancialReportProxy("Analyst");
        reportAccess.View();
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

internal interface IExporter { void Export(string reportName); }
internal sealed class PdfExporter : IExporter { public void Export(string reportName) => Console.WriteLine($"Bridge -> Exported {reportName} as PDF"); }
internal sealed class ExcelExporter : IExporter { public void Export(string reportName) => Console.WriteLine($"Bridge -> Exported {reportName} as Excel"); }

internal abstract class Report
{
    private readonly IExporter _exporter;
    protected Report(IExporter exporter) => _exporter = exporter;
    protected abstract string Name { get; }
    public void Export() => _exporter.Export(Name);
}

internal sealed class PayrollReport(IExporter exporter) : Report(exporter) { protected override string Name => "Payroll Report"; }
internal sealed class TaxReport(IExporter exporter) : Report(exporter) { protected override string Name => "Tax Report"; }

internal interface IOrgUnit { void Display(int depth = 0); }
internal sealed class EmployeeLeaf(string name) : IOrgUnit
{
    public void Display(int depth = 0) => Console.WriteLine($"{new string(' ', depth)}- {name}");
}

internal sealed class EmployeeNode(string name) : IOrgUnit
{
    private readonly List<IOrgUnit> _children = [];
    internal void Add(IOrgUnit unit) => _children.Add(unit);

    public void Display(int depth = 0)
    {
        Console.WriteLine($"{new string(' ', depth)}+ {name}");
        foreach (var child in _children) child.Display(depth + 2);
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

internal sealed class DocumentTemplate(string name) { public string Name { get; } = name; }

internal sealed class DocumentTemplateFactory
{
    private readonly Dictionary<string, DocumentTemplate> _templates = [];

    internal DocumentTemplate GetTemplate(string name)
    {
        if (!_templates.TryGetValue(name, out var template))
        {
            template = new DocumentTemplate(name);
            _templates[name] = template;
        }

        return template;
    }
}

internal interface IFinancialReport { void View(); }
internal sealed class RealFinancialReport : IFinancialReport { public void View() => Console.WriteLine("Proxy -> Viewing financial report data"); }

internal sealed class FinancialReportProxy(string role) : IFinancialReport
{
    private readonly RealFinancialReport _real = new();

    public void View()
    {
        if (role is "Admin" or "Analyst") _real.View();
        else Console.WriteLine("Proxy -> Access denied");
    }
}
