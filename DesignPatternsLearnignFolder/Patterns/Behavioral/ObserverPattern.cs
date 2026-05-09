namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class ObserverPattern
{
    internal static void Run()
    {
        var stock = new Stock("TAX-ETF", 100m);
        stock.Attach(new Trader("Rohit"));
        stock.Attach(new Trader("Anya"));
        stock.Price = 106.5m;
    }
}

internal interface IInvestor { void Update(string symbol, decimal price); }
internal sealed class Stock(string symbol, decimal price)
{
    private readonly List<IInvestor> _investors = [];
    private decimal _price = price;
    internal string Symbol { get; } = symbol;
    internal decimal Price
    {
        get => _price;
        set
        {
            _price = value;
            foreach (var investor in _investors) investor.Update(Symbol, _price);
        }
    }
    internal void Attach(IInvestor investor) => _investors.Add(investor);
}
internal sealed class Trader(string name) : IInvestor { public void Update(string symbol, decimal price) => Console.WriteLine($"Observer -> {name} notified: {symbol} at {price}"); }
