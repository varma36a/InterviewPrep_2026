using MediatR;
using Microsoft.EntityFrameworkCore;
using TaxCompliancePlatform.Application.Abstractions.CurrentUser;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Handlers.DominoFranchise.GetDominoFranchiseSalesOrders;

public sealed class GetDominoFranchiseSalesOrdersQueryHandler(
    ICurrentTenantProvider currentTenantProvider,
    IRepository<DominoFranchiseSalesOrder> orderRepository)
    : IRequestHandler<GetDominoFranchiseSalesOrdersQuery, CursorPagedResponse<DominoFranchiseSalesOrderDto>>
{
    public async Task<CursorPagedResponse<DominoFranchiseSalesOrderDto>> Handle(
        GetDominoFranchiseSalesOrdersQuery request,
        CancellationToken cancellationToken)
    {
        if (!currentTenantProvider.HasTenant)
        {
            throw new ArgumentException(
                "Tenant context is missing. Send X-Tenant-Id or configure TenantResolution:DefaultTenantId for local runs.");
        }

        if (!string.IsNullOrWhiteSpace(request.Cursor) && !ListCursorV1.TryDecode(request.Cursor, out _, out _))
        {
            throw new ArgumentException(
                "Invalid cursor value. Use the nextCursor from the previous response, or omit cursor for the first page.");
        }

        var limit = Math.Clamp(request.Limit, 1, 100);

        var query = orderRepository.Query()
            .AsNoTracking()
            .Where(x => x.TenantId == currentTenantProvider.TenantId);

        if (ListCursorV1.TryDecode(request.Cursor, out var cursorAt, out var cursorId))
        {
            query = query.Where(x =>
                x.CreatedAtUtc < cursorAt ||
                (x.CreatedAtUtc == cursorAt && x.Id < cursorId));
        }

        var raw = await query
            .OrderByDescending(x => x.CreatedAtUtc)
            .ThenByDescending(x => x.Id)
            .Take(limit + 1)
            .Select(x => new
            {
                x.Id,
                x.StoreCode,
                x.MarketRegion,
                Channel = x.Channel.ToString(),
                x.CustomerOrderReference,
                x.PretaxAmount,
                x.EstimatedSalesTax,
                x.CorrelationId,
                x.CreatedAtUtc
            })
            .ToListAsync(cancellationToken);

        var hasMore = raw.Count > limit;
        var page = hasMore ? raw.Take(limit).ToList() : raw;

        var items = page
            .Select(x => new DominoFranchiseSalesOrderDto(
                x.Id,
                x.StoreCode,
                x.MarketRegion,
                x.Channel,
                x.CustomerOrderReference,
                x.PretaxAmount,
                x.EstimatedSalesTax,
                x.CorrelationId,
                x.CreatedAtUtc))
            .ToList();

        string? nextCursor = null;
        if (hasMore && page.Count > 0)
        {
            var last = page[^1];
            nextCursor = ListCursorV1.Encode(last.CreatedAtUtc, last.Id);
        }

        return new CursorPagedResponse<DominoFranchiseSalesOrderDto>(items, nextCursor, hasMore);
    }
}
