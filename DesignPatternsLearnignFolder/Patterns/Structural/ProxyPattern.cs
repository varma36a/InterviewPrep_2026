namespace DesignPatternsLearnignFolder.Patterns.Structural;

internal static class ProxyPattern
{
    internal static void Run()
    {
        IPremiumMenu premiumMenu = new PremiumMenuProxy("Customer");
        premiumMenu.ViewSpecials();
        premiumMenu = new PremiumMenuProxy("Manager");
        premiumMenu.ViewSpecials();
    }
}

internal interface IPremiumMenu { void ViewSpecials(); }
internal sealed class RealPremiumMenu : IPremiumMenu
{
    public void ViewSpecials() => Console.WriteLine("Proxy -> Truffle Pizza ($24.99), Lobster Pizza ($29.99)");
}
internal sealed class PremiumMenuProxy(string role) : IPremiumMenu
{
    private readonly RealPremiumMenu _realMenu = new();
    public void ViewSpecials()
    {
        if (role is "Manager" or "Staff")
            _realMenu.ViewSpecials();
        else
            Console.WriteLine("Proxy -> Premium menu access denied for customers");
    }
}
