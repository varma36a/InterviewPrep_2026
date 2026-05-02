using Asp.Versioning;
using MediatR;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using TaxCompliancePlatform.Application.Features.TaxProfiles.Commands.CreateTaxProfile;
using TaxCompliancePlatform.Application.Features.TaxProfiles.Queries.GetTaxProfiles;

namespace TaxCompliancePlatform.API.Controllers.v1;

[ApiController]
[ApiVersion("1.0")]
[Route("api/v{version:apiVersion}/tax-profiles")]
[Authorize(Policy = "TenantScopePolicy")]
public sealed class TaxProfilesController(IMediator mediator) : ControllerBase
{
    [HttpGet]
    public async Task<IActionResult> Get(int pageNumber = 1, int pageSize = 20, CancellationToken cancellationToken = default)
    {
        var items = await mediator.Send(new GetTaxProfilesQuery(pageNumber, pageSize), cancellationToken);
        return Ok(items);
    }

    [HttpPost]
    [Authorize(Roles = "TenantAdmin,FinanceManager")]
    public async Task<IActionResult> Create([FromBody] CreateTaxProfileCommand command, CancellationToken cancellationToken)
    {
        var id = await mediator.Send(command, cancellationToken);
        return CreatedAtAction(nameof(Create), new { id }, new { id });
    }
}
