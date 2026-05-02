using Asp.Versioning;
using MediatR;
using Microsoft.AspNetCore.Mvc;
using TaxCompliancePlatform.Application.Features.Auth.Commands.Login;
using TaxCompliancePlatform.Application.Features.Auth.Commands.RegisterTenant;

namespace TaxCompliancePlatform.API.Controllers.v1;

[ApiController]
[ApiVersion("1.0")]
[Route("api/v{version:apiVersion}/auth")]
public sealed class AuthController(IMediator mediator) : ControllerBase
{
    [HttpPost("tenants/register")]
    public async Task<IActionResult> RegisterTenant([FromBody] RegisterTenantCommand command, CancellationToken cancellationToken)
    {
        var tenantId = await mediator.Send(command, cancellationToken);
        return CreatedAtAction(nameof(RegisterTenant), new { tenantId }, new { tenantId });
    }

    [HttpPost("login")]
    public async Task<IActionResult> Login([FromBody] LoginCommand command, CancellationToken cancellationToken)
    {
        var result = await mediator.Send(command, cancellationToken);
        return Ok(result);
    }
}
