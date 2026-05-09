namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class ProxyPattern
{
    internal static void Run()
    {
        IFinancialReport reportAccess = new FinancialReportProxy("Analyst");
        reportAccess.View();
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
