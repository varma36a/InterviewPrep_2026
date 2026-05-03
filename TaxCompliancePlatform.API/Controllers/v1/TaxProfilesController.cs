using Asp.Versioning;
using Microsoft.AspNetCore.Mvc;
using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.TaxProfiles.CreateTaxProfile;
using TaxCompliancePlatform.Application.Handlers.TaxProfiles.GetTaxProfiles;
using TaxCompliancePlatform.Application.Providers.Execution;
using TaxCompliancePlatform.Application.Services.TaxProfiles;

namespace TaxCompliancePlatform.API.Controllers.v1;

[ApiController]
[ApiVersion("1.0")]
[Route("api/v{version:apiVersion}/tax-profiles")]
//[Authorize(Policy = "TenantScopePolicy")]
public sealed class TaxProfilesController(ITaxProfileService taxProfileService, IRequestExecutionContext executionContext)
    : ControllerBase
{
    [HttpGet]
    public async Task<IActionResult> Get(int pageNumber = 1, int pageSize = 20, CancellationToken cancellationToken = default)
    {
        var items = await taxProfileService.GetTaxProfilesAsync(
            new ApplicationServiceRequest<GetTaxProfilesQuery>(
                executionContext.CorrelationId,
                new GetTaxProfilesQuery(pageNumber, pageSize)),
            cancellationToken);
        return Ok(items);
    }

    [HttpPost]
    //[Authorize(Roles = "TenantAdmin,FinanceManager")]
    public async Task<IActionResult> Create([FromBody] CreateTaxProfileCommand command, CancellationToken cancellationToken)
    {
        var id = await taxProfileService.CreateTaxProfileAsync(
            new ApplicationServiceRequest<CreateTaxProfileCommand>(executionContext.CorrelationId, command),
            cancellationToken);
        return CreatedAtAction(nameof(Create), new { id }, new { id });
    }
}
