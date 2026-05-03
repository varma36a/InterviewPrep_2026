using MediatR;
using Microsoft.Extensions.Logging;
using TaxCompliancePlatform.Application.Providers.Execution;

namespace TaxCompliancePlatform.Application.Pipeline;

/// <summary>
/// Ensures every MediatR handler run carries the current <see cref="IRequestExecutionContext"/> in logging scope.
/// </summary>
public sealed class ExecutionContextLoggingBehavior<TRequest, TResponse>(
    IRequestExecutionContext executionContext,
    ILogger<ExecutionContextLoggingBehavior<TRequest, TResponse>> logger) : IPipelineBehavior<TRequest, TResponse>
    where TRequest : notnull
{
    public async Task<TResponse> Handle(TRequest request, RequestHandlerDelegate<TResponse> next, CancellationToken _)
    {
        using var scope = logger.BeginScope(new Dictionary<string, object?>
        {
            ["CorrelationId"] = executionContext.CorrelationId,
            ["TenantId"] = executionContext.TenantId,
            ["DominoStoreCode"] = executionContext.DominoStoreCode,
            ["DominoMarketRegion"] = executionContext.DominoMarketRegion,
            ["DominoChannel"] = executionContext.DominoFulfillmentChannel.ToString()
        });

        logger.LogDebug("MediatR {RequestType}", typeof(TRequest).Name);
        return await next();
    }
}
