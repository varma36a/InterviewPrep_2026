using TaxCompliancePlatform.Domain.Enums;

namespace TaxCompliancePlatform.Application.Providers.Execution;

/// <summary>
/// Per-request execution context built from HTTP headers, tenant resolution, and correlation middleware.
/// Handlers, services, and MediatR behaviors consume this for consistent audit and Domino's scenario metadata.
/// </summary>
public interface IRequestExecutionContext
{
    string CorrelationId { get; }

    Guid? TenantId { get; }

    bool HasTenant { get; }

    /// <summary>Franchise store identifier, e.g. US-60614-001.</summary>
    string DominoStoreCode { get; }

    /// <summary>Regional routing key, e.g. US-IL-CHICAGO.</summary>
    string DominoMarketRegion { get; }

    DominoFulfillmentChannel DominoFulfillmentChannel { get; }
}
