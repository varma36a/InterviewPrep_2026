using Serilog.Context;

namespace TaxCompliancePlatform.API.Middleware;

public sealed class RequestLoggingMiddleware(RequestDelegate next, ILogger<RequestLoggingMiddleware> logger)
{
    public async Task Invoke(HttpContext context)
    {
        var correlationId = context.Items.TryGetValue(CorrelationIdMiddleware.HeaderName, out var value)
            ? value?.ToString()
            : string.Empty;

        using (LogContext.PushProperty("CorrelationId", correlationId))
        using (LogContext.PushProperty("TenantId", context.Request.Headers[TenantResolutionMiddleware.TenantHeaderName].ToString()))
        {
            logger.LogInformation("Handling {Method} {Path}", context.Request.Method, context.Request.Path);
            await next(context);
            logger.LogInformation("Completed {Method} {Path} with status {StatusCode}", context.Request.Method, context.Request.Path, context.Response.StatusCode);
        }
    }
}
