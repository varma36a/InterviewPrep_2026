namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class InterpreterPattern
{
    internal static void Run()
    {
        var promoRule = new AndExpression(
            new GreaterThanExpression("orderTotal", 25m),
            new EqualsExpression("loyaltyMember", "true"));
        var context = new OrderContext(new Dictionary<string, object>
        {
            ["orderTotal"] = 32.50m,
            ["loyaltyMember"] = "true"
        });
        Console.WriteLine($"Interpreter -> Free garlic bread eligible: {promoRule.Interpret(context)}");
    }
}

internal sealed class OrderContext(Dictionary<string, object> variables) { internal Dictionary<string, object> Variables { get; } = variables; }
internal interface IPromoRule { bool Interpret(OrderContext context); }
internal sealed class GreaterThanExpression(string key, decimal threshold) : IPromoRule
{
    public bool Interpret(OrderContext context) => Convert.ToDecimal(context.Variables[key]) > threshold;
}
internal sealed class EqualsExpression(string key, string expected) : IPromoRule
{
    public bool Interpret(OrderContext context) => context.Variables[key].ToString() == expected;
}
internal sealed class AndExpression(IPromoRule left, IPromoRule right) : IPromoRule
{
    public bool Interpret(OrderContext context) => left.Interpret(context) && right.Interpret(context);
}
