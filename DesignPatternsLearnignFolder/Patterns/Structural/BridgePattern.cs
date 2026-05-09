namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class BridgePattern
{
    internal static void Run()
    {
        Report payrollPdf = new PayrollReport(new PdfExporter());
        Report taxExcel = new TaxReport(new ExcelExporter());
        payrollPdf.Export();
        taxExcel.Export();
    }
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
