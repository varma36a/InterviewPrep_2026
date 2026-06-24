namespace DesignPatternsLearnignFolder.Patterns.Creational;

internal static class AbstractFactoryPattern
{
    internal static void Run()
    {
        IPizzaStyleFactory nyStyle = new NewYorkStyleFactory();
        IPizzaStyleFactory chicagoStyle = new ChicagoStyleFactory();
        nyStyle.CreateCrust().Bake();
        nyStyle.CreateSauce().Spread();
        chicagoStyle.CreateCrust().Bake();
        chicagoStyle.CreateSauce().Spread();
    }
}

internal interface ICrust { void Bake(); }
internal interface ISauce { void Spread(); }
internal interface IPizzaStyleFactory { ICrust CreateCrust(); ISauce CreateSauce(); }

internal sealed class NewYorkStyleFactory : IPizzaStyleFactory
{
    public ICrust CreateCrust() => new ThinCrust();
    public ISauce CreateSauce() => new TomatoSauce();
}
internal sealed class ChicagoStyleFactory : IPizzaStyleFactory
{
    public ICrust CreateCrust() => new DeepDishCrust();
    public ISauce CreateSauce() => new ChunkyTomatoSauce();
}

internal sealed class ThinCrust : ICrust { public void Bake() => Console.WriteLine("AbstractFactory -> Baking thin NY-style crust"); }
internal sealed class DeepDishCrust : ICrust { public void Bake() => Console.WriteLine("AbstractFactory -> Baking deep-dish Chicago crust"); }
internal sealed class TomatoSauce : ISauce { public void Spread() => Console.WriteLine("AbstractFactory -> Spreading smooth tomato sauce"); }
internal sealed class ChunkyTomatoSauce : ISauce { public void Spread() => Console.WriteLine("AbstractFactory -> Spreading chunky tomato sauce"); }
