namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class InterpreterPattern
{
    internal static void Run()
    {
        var expr = new AndExpression(new GreaterThanExpression("income", 50000), new EqualsExpression("country", "IN"));
        var context = new RuleContext(new Dictionary<string, object> { ["income"] = 75000, ["country"] = "IN" });
        Console.WriteLine($"Interpreter -> Eligible: {expr.Interpret(context)}");
    }
}

internal sealed class RuleContext(Dictionary<string, object> variables) { internal Dictionary<string, object> Variables { get; } = variables; }
internal interface IExpression { bool Interpret(RuleContext context); }
internal sealed class GreaterThanExpression(string key, decimal threshold) : IExpression { public bool Interpret(RuleContext context) => Convert.ToDecimal(context.Variables[key]) > threshold; }
internal sealed class EqualsExpression(string key, string expected) : IExpression { public bool Interpret(RuleContext context) => context.Variables[key].ToString() == expected; }
internal sealed class AndExpression(IExpression left, IExpression right) : IExpression { public bool Interpret(RuleContext context) => left.Interpret(context) && right.Interpret(context); }
