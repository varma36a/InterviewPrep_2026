using Microsoft.AspNetCore.Http;
using TaxCompliancePlatform.API.Middleware;
using TaxCompliancePlatform.Application.Abstractions.CurrentUser;
using TaxCompliancePlatform.Application.Providers.Correlation;
using TaxCompliancePlatform.Application.Providers.Execution;
using TaxCompliancePlatform.Domain.Enums;

namespace TaxCompliancePlatform.API.Execution;

/// <summary>
/// Single HTTP-scoped provider for correlation, tenant, and Domino's scenario headers (populated by middleware).
/// </summary>
public sealed class HttpRequestExecutionContext(
    IHttpContextAccessor httpContextAccessor,
    ICurrentTenantProvider currentTenantProvider) : ICorrelationContext, IRequestExecutionContext
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

    public Guid? TenantId => currentTenantProvider.HasTenant ? currentTenantProvider.TenantId : null;

    public bool HasTenant => currentTenantProvider.HasTenant;

    public string DominoStoreCode => ReadDominoString(ExecutionContextHttpKeys.DominoStoreCode);

    public string DominoMarketRegion => ReadDominoString(ExecutionContextHttpKeys.DominoMarketRegion);

    public DominoFulfillmentChannel DominoFulfillmentChannel =>
        ReadDominoChannel(ExecutionContextHttpKeys.DominoFulfillmentChannel);

    private string ReadDominoString(string key)
    {
        var httpContext = httpContextAccessor.HttpContext;
        if (httpContext?.Items.TryGetValue(key, out var value) == true && value is string s && !string.IsNullOrWhiteSpace(s))
        {
            return s;
        }

        return string.Empty;
    }

    private DominoFulfillmentChannel ReadDominoChannel(string key)
    {
        var httpContext = httpContextAccessor.HttpContext;
        if (httpContext?.Items.TryGetValue(key, out var value) == true && value is DominoFulfillmentChannel ch)
        {
            return ch;
        }

        if (httpContext?.Items.TryGetValue(key, out value) == true &&
            value is string raw &&
            raw.Trim().Equals("Delivery", StringComparison.OrdinalIgnoreCase))
        {
            return DominoFulfillmentChannel.Delivery;
        }

        return DominoFulfillmentChannel.Carryout;
    }
}
