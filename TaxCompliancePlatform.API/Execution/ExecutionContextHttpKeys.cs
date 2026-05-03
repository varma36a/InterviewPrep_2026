namespace TaxCompliancePlatform.API.Execution;

/// <summary>
/// HttpContext.Items keys populated by <see cref="Middleware.ExecutionContextMiddleware"/> for <see cref="HttpRequestExecutionContext"/>.
/// </summary>
public static class ExecutionContextHttpKeys
{
    public const string DominoStoreCode = "ExecutionContext.DominoStoreCode";
    public const string DominoMarketRegion = "ExecutionContext.DominoMarketRegion";
    public const string DominoFulfillmentChannel = "ExecutionContext.DominoFulfillmentChannel";
}
