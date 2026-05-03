using Serilog.Context;
using TaxCompliancePlatform.Application.Providers.Execution;

namespace TaxCompliancePlatform.API.Middleware;

public sealed class RequestLoggingMiddleware(RequestDelegate next, ILogger<RequestLoggingMiddleware> logger)
{
    public async Task Invoke(HttpContext context, IRequestExecutionContext executionContext)
    {
        using (LogContext.PushProperty("CorrelationId", executionContext.CorrelationId))
        using (LogContext.PushProperty("TenantId", executionContext.TenantId?.ToString() ?? string.Empty))
        using (LogContext.PushProperty("DominoStoreCode", executionContext.DominoStoreCode))
        using (LogContext.PushProperty("DominoMarketRegion", executionContext.DominoMarketRegion))
        using (LogContext.PushProperty("DominoChannel", executionContext.DominoFulfillmentChannel.ToString()))
        {
            logger.LogInformation("Handling {Method} {Path}", context.Request.Method, context.Request.Path);
            await next(context);
            logger.LogInformation(
                "Completed {Method} {Path} with status {StatusCode}",
                context.Request.Method,
                context.Request.Path,
                context.Response.StatusCode);
        }
    }
}
