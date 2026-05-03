using MediatR;
using Microsoft.EntityFrameworkCore;
using TaxCompliancePlatform.Application.Abstractions.CurrentUser;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Handlers.DominoFranchise.GetDominoFranchiseSalesOrders;

public sealed class GetDominoFranchiseSalesOrdersQueryHandler(
    ICurrentTenantProvider currentTenantProvider,
    IRepository<DominoFranchiseSalesOrder> orderRepository)
    : IRequestHandler<GetDominoFranchiseSalesOrdersQuery, IReadOnlyCollection<DominoFranchiseSalesOrderDto>>
{
    public async Task<IReadOnlyCollection<DominoFranchiseSalesOrderDto>> Handle(
        GetDominoFranchiseSalesOrdersQuery request,
        CancellationToken cancellationToken)
    {
        if (!currentTenantProvider.HasTenant)
        {
            throw new ArgumentException(
                "Tenant context is missing. Send X-Tenant-Id or configure TenantResolution:DefaultTenantId for local runs.");
        }

        var skip = (Math.Max(request.PageNumber, 1) - 1) * Math.Clamp(request.PageSize, 1, 100);
        var take = Math.Clamp(request.PageSize, 1, 100);

        var items = await orderRepository.Query()
            .AsNoTracking()
            .Where(x => x.TenantId == currentTenantProvider.TenantId)
            .OrderByDescending(x => x.CreatedAtUtc)
            .Skip(skip)
            .Take(take)
            .Select(x => new DominoFranchiseSalesOrderDto(
                x.Id,
                x.StoreCode,
                x.MarketRegion,
                x.Channel.ToString(),
                x.CustomerOrderReference,
                x.PretaxAmount,
                x.EstimatedSalesTax,
                x.CorrelationId,
                x.CreatedAtUtc))
            .ToListAsync(cancellationToken);

        return items;
    }
}
