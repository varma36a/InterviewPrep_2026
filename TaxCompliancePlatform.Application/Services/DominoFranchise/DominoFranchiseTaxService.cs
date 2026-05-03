using MediatR;
using Microsoft.Extensions.Logging;
using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.DominoFranchise.CreateDominoFranchiseSalesOrder;
using TaxCompliancePlatform.Application.Handlers.DominoFranchise.GetDominoFranchiseSalesOrders;
using TaxCompliancePlatform.Application.Providers.Execution;

namespace TaxCompliancePlatform.Application.Services.DominoFranchise;

public sealed class DominoFranchiseTaxService(
    IMediator mediator,
    IRequestExecutionContext executionContext,
    ILogger<DominoFranchiseTaxService> logger) : IDominoFranchiseTaxService
{
    public async Task<Guid> RecordSalesOrderAsync(
        ApplicationServiceRequest<CreateDominoFranchiseSalesOrderCommand> request,
        CancellationToken cancellationToken)
    {
        EnsureCorrelationMatchesAmbient(request.CorrelationId);
        using var scope = logger.BeginScope(BuildScope());
        logger.LogInformation(
            "Orchestrating Domino franchise sales order for store {Store} market {Market}",
            executionContext.DominoStoreCode,
            executionContext.DominoMarketRegion);
        return await mediator.Send(request.Command, cancellationToken);
    }

    public async Task<CursorPagedResponse<DominoFranchiseSalesOrderDto>> GetSalesOrdersAsync(
        ApplicationServiceRequest<GetDominoFranchiseSalesOrdersQuery> request,
        CancellationToken cancellationToken)
    {
        EnsureCorrelationMatchesAmbient(request.CorrelationId);
        using var scope = logger.BeginScope(BuildScope());
        logger.LogInformation("Orchestrating Domino franchise sales order list");
        return await mediator.Send(request.Command, cancellationToken);
    }

    private Dictionary<string, object?> BuildScope() => new()
    {
        ["CorrelationId"] = executionContext.CorrelationId,
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
