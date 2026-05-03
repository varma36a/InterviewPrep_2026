using MediatR;

namespace TaxCompliancePlatform.Application.Handlers.DominoFranchise.GetDominoFranchiseSalesOrders;

public sealed record GetDominoFranchiseSalesOrdersQuery(int PageNumber = 1, int PageSize = 20)
    : IRequest<IReadOnlyCollection<DominoFranchiseSalesOrderDto>>;

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
