using Microsoft.AspNetCore.Http;
using TaxCompliancePlatform.API.Middleware;
using TaxCompliancePlatform.Application.Providers.Correlation;

namespace TaxCompliancePlatform.API.Correlation;

/// <summary>
/// HTTP host binding for <see cref="ICorrelationContext"/> — keeps ASP.NET types out of Application/Infrastructure.
/// </summary>
public sealed class HttpCorrelationContext(IHttpContextAccessor httpContextAccessor) : ICorrelationContext
{
    public string CorrelationId
    {
        get
        {
            var httpContext = httpContextAccessor.HttpContext;
            if (httpContext?.Items.TryGetValue(CorrelationIdMiddleware.HeaderName, out var value) == true &&
                value is string s &&
                !string.IsNullOrWhiteSpace(s))
            {
                return s;
            }

            return string.Empty;
        }
    }
}
