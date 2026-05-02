using System.Net;
using System.Text.Json;

namespace TaxCompliancePlatform.API.Middleware;

public sealed class ExceptionHandlingMiddleware(RequestDelegate next, ILogger<ExceptionHandlingMiddleware> logger)
{
    public async Task Invoke(HttpContext context)
    {
        try
        {
            await next(context);
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "Unhandled exception occurred");
            context.Response.StatusCode = ex is UnauthorizedAccessException ? (int)HttpStatusCode.Unauthorized : (int)HttpStatusCode.InternalServerError;
            context.Response.ContentType = "application/json";

            var payload = new { success = false, error = ex.Message };
            await context.Response.WriteAsync(JsonSerializer.Serialize(payload));
        }
    }
}
