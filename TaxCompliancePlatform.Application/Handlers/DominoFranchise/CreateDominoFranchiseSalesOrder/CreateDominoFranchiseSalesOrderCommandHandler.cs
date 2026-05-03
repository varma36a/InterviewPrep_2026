using MediatR;
using TaxCompliancePlatform.Application.Abstractions.CurrentUser;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Application.Managers.Domino;
using TaxCompliancePlatform.Application.Providers.Execution;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Handlers.DominoFranchise.CreateDominoFranchiseSalesOrder;

public sealed class CreateDominoFranchiseSalesOrderCommandHandler(
    IRequestExecutionContext executionContext,
    ICurrentTenantProvider currentTenantProvider,
    IRepository<DominoFranchiseSalesOrder> orderRepository,
    IUnitOfWork unitOfWork,
    IDominoSalesTaxEstimator salesTaxEstimator) : IRequestHandler<CreateDominoFranchiseSalesOrderCommand, Guid>
{
    public async Task<Guid> Handle(CreateDominoFranchiseSalesOrderCommand request, CancellationToken cancellationToken)
    {
        if (!currentTenantProvider.HasTenant)
        {
            throw new ArgumentException(
                "Tenant context is missing. Send X-Tenant-Id or configure TenantResolution:DefaultTenantId for local runs.");
        }

        var storeCode = executionContext.DominoStoreCode;
        if (string.IsNullOrWhiteSpace(storeCode))
        {
            throw new ArgumentException(
                "Domino store context is missing. Send header X-Domino-Store-Code or configure DominoScenario:DefaultStoreCode.");
        }

        var market = executionContext.DominoMarketRegion;
        if (string.IsNullOrWhiteSpace(market))
        {
            throw new ArgumentException(
                "Domino market context is missing. Send header X-Domino-Market or configure DominoScenario:DefaultMarketRegion.");
        }

        var tax = salesTaxEstimator.EstimateSalesTax(request.PretaxAmount, market);
        var correlation = string.IsNullOrWhiteSpace(executionContext.CorrelationId)
            ? Guid.NewGuid().ToString("N")
            : executionContext.CorrelationId;

        var order = new DominoFranchiseSalesOrder(
            currentTenantProvider.TenantId,
            storeCode.Trim(),
            market.Trim(),
            executionContext.DominoFulfillmentChannel,
            request.CustomerOrderReference.Trim(),
            request.PretaxAmount,
            tax,
            correlation);

        await orderRepository.AddAsync(order, cancellationToken);
        await unitOfWork.SaveChangesAsync(cancellationToken);
        return order.Id;
    }
}
