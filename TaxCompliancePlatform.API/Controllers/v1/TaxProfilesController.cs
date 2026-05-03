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
    /// <summary>Keyset pagination: omit <paramref name="cursor"/> for the first page; use <c>nextCursor</c> from the prior response for the next.</summary>
    [HttpGet]
    public async Task<IActionResult> Get(string? cursor = null, int limit = 20, CancellationToken cancellationToken = default)
    {
        var result = await taxProfileService.GetTaxProfilesAsync(
            new ApplicationServiceRequest<GetTaxProfilesQuery>(
                executionContext.CorrelationId,
                new GetTaxProfilesQuery(cursor, limit)),
            cancellationToken);
        return Ok(result);
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
