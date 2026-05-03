using MediatR;
using TaxCompliancePlatform.Application.Common;

namespace TaxCompliancePlatform.Application.Handlers.DominoFranchise.GetDominoFranchiseSalesOrders;

public sealed record GetDominoFranchiseSalesOrdersQuery(string? Cursor, int Limit = 20)
    : IRequest<CursorPagedResponse<DominoFranchiseSalesOrderDto>>;

public sealed record DominoFranchiseSalesOrderDto(
    Guid Id,
    string StoreCode,
    string MarketRegion,
    string Channel,
    string CustomerOrderReference,
    decimal PretaxAmount,
    decimal EstimatedSalesTax,
    string CorrelationId,
    DateTime CreatedAtUtc);
