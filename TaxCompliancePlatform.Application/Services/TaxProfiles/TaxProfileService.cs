using MediatR;
using Microsoft.Extensions.Logging;
using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.TaxProfiles.CreateTaxProfile;
using TaxCompliancePlatform.Application.Handlers.TaxProfiles.GetTaxProfiles;
using TaxCompliancePlatform.Application.Providers.Execution;

namespace TaxCompliancePlatform.Application.Services.TaxProfiles;

public sealed class TaxProfileService(
    IMediator mediator,
    IRequestExecutionContext executionContext,
    ILogger<TaxProfileService> logger) : ITaxProfileService
{
    public async Task<CursorPagedResponse<TaxProfileDto>> GetTaxProfilesAsync(
        ApplicationServiceRequest<GetTaxProfilesQuery> request,
        CancellationToken cancellationToken)
    {
        EnsureCorrelationMatchesAmbient(request.CorrelationId);
        using var scope = logger.BeginScope(BuildScope(request.CorrelationId));
        logger.LogDebug("Orchestrating {Query}", nameof(GetTaxProfilesQuery));
        return await mediator.Send(request.Command, cancellationToken);
    }

    public async Task<Guid> CreateTaxProfileAsync(
        ApplicationServiceRequest<CreateTaxProfileCommand> request,
        CancellationToken cancellationToken)
    {
        EnsureCorrelationMatchesAmbient(request.CorrelationId);
        using var scope = logger.BeginScope(BuildScope(request.CorrelationId));
        logger.LogDebug("Orchestrating {Command}", nameof(CreateTaxProfileCommand));
        return await mediator.Send(request.Command, cancellationToken);
    }

    private Dictionary<string, object?> BuildScope(string correlationFromRequest) => new()
    {
        ["CorrelationId"] = correlationFromRequest,
        ["TenantId"] = executionContext.TenantId,
        ["DominoStoreCode"] = executionContext.DominoStoreCode,
        ["DominoMarketRegion"] = executionContext.DominoMarketRegion,
        ["DominoChannel"] = executionContext.DominoFulfillmentChannel.ToString()
    };

    private void EnsureCorrelationMatchesAmbient(string requestCorrelationId)
    {
        var ambient = executionContext.CorrelationId;
        if (string.IsNullOrWhiteSpace(ambient) || string.IsNullOrWhiteSpace(requestCorrelationId))
        {
            return;
        }

        if (!string.Equals(ambient, requestCorrelationId, StringComparison.Ordinal))
        {
            throw new InvalidOperationException(
                "The correlation id on the service request does not match the ambient correlation context.");
        }
    }
}
