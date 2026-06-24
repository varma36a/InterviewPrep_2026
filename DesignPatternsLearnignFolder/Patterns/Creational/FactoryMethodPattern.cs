namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class FactoryMethodPattern
{
    internal static void Run()
    {
        IPizza margherita = PizzaFactory.Create("margherita");
        IPizza pepperoni = PizzaFactory.Create("pepperoni");
        margherita.Prepare();
        pepperoni.Prepare();
    }
}

internal interface IPizza { void Prepare(); }
internal sealed class MargheritaPizza : IPizza { public void Prepare() => Console.WriteLine("Factory -> Preparing Margherita: tomato, mozzarella, basil"); }
internal sealed class PepperoniPizza : IPizza { public void Prepare() => Console.WriteLine("Factory -> Preparing Pepperoni: tomato, mozzarella, pepperoni"); }
internal static class PizzaFactory
{
    internal static IPizza Create(string type) => type.ToLowerInvariant() switch
    {
        "margherita" => new MargheritaPizza(),
        "pepperoni" => new PepperoniPizza(),
        _ => throw new ArgumentException("Unsupported pizza type.")
    };
}
