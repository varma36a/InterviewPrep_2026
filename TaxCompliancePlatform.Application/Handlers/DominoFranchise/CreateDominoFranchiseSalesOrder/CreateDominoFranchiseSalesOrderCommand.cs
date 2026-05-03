using MediatR;

namespace TaxCompliancePlatform.Application.Handlers.DominoFranchise.CreateDominoFranchiseSalesOrder;

public sealed record CreateDominoFranchiseSalesOrderCommand(
    string CustomerOrderReference,
    decimal PretaxAmount) : IRequest<Guid>;
