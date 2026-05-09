namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class AbstractFactoryPattern
{
    internal static void Run()
    {
        ITaxSuite indiaSuite = new IndiaTaxSuite();
        ITaxSuite usSuite = new USTaxSuite();
        Console.WriteLine(indiaSuite.CreateCalculator().CalculateTax(1000m));
        Console.WriteLine(usSuite.CreateCalculator().CalculateTax(1000m));
    }
}

internal interface ITaxCalculator { string CalculateTax(decimal amount); }
internal interface ITaxSuite { ITaxCalculator CreateCalculator(); }
internal sealed class IndiaTaxSuite : ITaxSuite { public ITaxCalculator CreateCalculator() => new IndiaTaxCalculator(); }
internal sealed class USTaxSuite : ITaxSuite { public ITaxCalculator CreateCalculator() => new USTaxCalculator(); }
internal sealed class IndiaTaxCalculator : ITaxCalculator { public string CalculateTax(decimal amount) => $"AbstractFactory -> India GST: {amount * 0.18m:C}"; }
internal sealed class USTaxCalculator : ITaxCalculator { public string CalculateTax(decimal amount) => $"AbstractFactory -> US Sales Tax: {amount * 0.07m:C}"; }
