using Asp.Versioning;
using Microsoft.AspNetCore.Mvc;
using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.DominoFranchise.CreateDominoFranchiseSalesOrder;
using TaxCompliancePlatform.Application.Handlers.DominoFranchise.GetDominoFranchiseSalesOrders;
using TaxCompliancePlatform.Application.Providers.Execution;
using TaxCompliancePlatform.Application.Services.DominoFranchise;

namespace TaxCompliancePlatform.API.Controllers.v1;

/// <summary>
/// Domino's franchise scenario: record pizza sales for tax compliance and list prior submissions for the tenant.
/// Franchise context (store, market, carryout vs delivery) comes from ExecutionContextMiddleware headers or appsettings defaults.
/// </summary>
[ApiController]
[ApiVersion("1.0")]
[Route("api/v{version:apiVersion}/domino/franchise-tax")]
public sealed class DominoFranchiseTaxController(
    IDominoFranchiseTaxService dominoFranchiseTaxService,
    IRequestExecutionContext executionContext) : ControllerBase
{
    [HttpPost("sales-orders")]
    public async Task<IActionResult> RecordSalesOrder(
        [FromBody] CreateDominoFranchiseSalesOrderCommand command,
        CancellationToken cancellationToken)
    {
        var id = await dominoFranchiseTaxService.RecordSalesOrderAsync(
            new ApplicationServiceRequest<CreateDominoFranchiseSalesOrderCommand>(
                executionContext.CorrelationId,
                command),
            cancellationToken);
        return CreatedAtAction(nameof(RecordSalesOrder), new { id }, new { id });
    }

    [HttpGet("sales-orders")]
    public async Task<IActionResult> ListSalesOrders(
        int pageNumber = 1,
        int pageSize = 20,
        CancellationToken cancellationToken = default)
    {
        var items = await dominoFranchiseTaxService.GetSalesOrdersAsync(
            new ApplicationServiceRequest<GetDominoFranchiseSalesOrdersQuery>(
                executionContext.CorrelationId,
                new GetDominoFranchiseSalesOrdersQuery(pageNumber, pageSize)),
            cancellationToken);
        return Ok(items);
    }
}
