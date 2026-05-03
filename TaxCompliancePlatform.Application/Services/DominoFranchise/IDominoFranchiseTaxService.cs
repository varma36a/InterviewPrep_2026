using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.DominoFranchise.CreateDominoFranchiseSalesOrder;
using TaxCompliancePlatform.Application.Handlers.DominoFranchise.GetDominoFranchiseSalesOrders;

namespace TaxCompliancePlatform.Application.Services.DominoFranchise;

public interface IDominoFranchiseTaxService
{
    Task<Guid> RecordSalesOrderAsync(
        ApplicationServiceRequest<CreateDominoFranchiseSalesOrderCommand> request,
        CancellationToken cancellationToken);

    Task<IReadOnlyCollection<DominoFranchiseSalesOrderDto>> GetSalesOrdersAsync(
        ApplicationServiceRequest<GetDominoFranchiseSalesOrdersQuery> request,
        CancellationToken cancellationToken);
}
