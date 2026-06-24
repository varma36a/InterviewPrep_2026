namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class PrototypePattern
{
    internal static void Run()
    {
        var houseSpecial = new SignaturePizza("House Special", "Thin", ["Pepperoni", "Olives", "Jalapeños"]);
        var customSpecial = houseSpecial.Clone();
        customSpecial.Name = "House Special - Extra Spicy";
        customSpecial.Toppings.Add("Extra Chili Flakes");
        Console.WriteLine($"Prototype -> Original: {houseSpecial.Name} [{string.Join(", ", houseSpecial.Toppings)}]");
        Console.WriteLine($"Prototype -> Clone:   {customSpecial.Name} [{string.Join(", ", customSpecial.Toppings)}]");
    }
}

internal sealed class SignaturePizza
{
    public string Name { get; set; }
    public string Crust { get; }
    public List<string> Toppings { get; }
    internal SignaturePizza(string name, string crust, List<string> toppings)
    {
        Name = name;
        Crust = crust;
        Toppings = [.. toppings];
    }
    internal SignaturePizza Clone() => new(Name, Crust, Toppings);
}
