namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class TemplateMethodPattern
{
    internal static void Run()
    {
        PizzaMakingProcess process = new ThinCrustPizzaProcess();
        process.MakePizza();
    }
}

internal abstract class PizzaMakingProcess
{
    internal void MakePizza()
    {
        PrepareDough();
        AddSauceAndToppings();
        Bake();
        Box();
    }
    protected abstract void PrepareDough();
    protected abstract void AddSauceAndToppings();
    protected abstract void Bake();
    protected virtual void Box() => Console.WriteLine("Template -> Boxed in standard pizza box");
}
internal sealed class ThinCrustPizzaProcess : PizzaMakingProcess
{
    protected override void PrepareDough() => Console.WriteLine("Template -> Rolled thin crust dough");
    protected override void AddSauceAndToppings() => Console.WriteLine("Template -> Added tomato sauce, mozzarella, basil");
    protected override void Bake() => Console.WriteLine("Template -> Baked at 450°F for 8 minutes");
}
