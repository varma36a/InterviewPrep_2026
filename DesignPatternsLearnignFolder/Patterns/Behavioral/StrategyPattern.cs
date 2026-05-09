namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class StrategyPattern
{
    internal static void Run()
    {
        var taxContext = new TaxComputationContext(new OldRegimeStrategy());
        Console.WriteLine(taxContext.Compute(1200000m));
        taxContext.SetStrategy(new NewRegimeStrategy());
        Console.WriteLine(taxContext.Compute(1200000m));
    }
}

internal interface ITaxStrategy { string Calculate(decimal income); }
internal sealed class OldRegimeStrategy : ITaxStrategy { public string Calculate(decimal income) => $"Strategy -> Old regime tax: {(income * 0.2m):C}"; }
internal sealed class NewRegimeStrategy : ITaxStrategy { public string Calculate(decimal income) => $"Strategy -> New regime tax: {(income * 0.15m):C}"; }
internal sealed class TaxComputationContext(ITaxStrategy strategy)
{
    private ITaxStrategy _strategy = strategy;
    internal void SetStrategy(ITaxStrategy strategy) => _strategy = strategy;
    internal string Compute(decimal income) => _strategy.Calculate(income);
}
