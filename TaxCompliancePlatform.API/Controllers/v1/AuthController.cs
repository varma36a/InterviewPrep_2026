using Asp.Versioning;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.Auth.Login;
using TaxCompliancePlatform.Application.Handlers.Auth.RegisterTenant;
using TaxCompliancePlatform.Application.Providers.Execution;
using TaxCompliancePlatform.Application.Services.Auth;

namespace TaxCompliancePlatform.API.Controllers.v1;

[ApiController]
[ApiVersion("1.0")]
[Route("api/v{version:apiVersion}/auth")]
[AllowAnonymous]
public sealed class AuthController(IAuthService authService, IRequestExecutionContext executionContext) : ControllerBase
{
    [HttpPost("tenants/register")]
    public async Task<IActionResult> RegisterTenant([FromBody] RegisterTenantCommand command, CancellationToken cancellationToken)
    {
        var tenantId = await authService.RegisterTenantAsync(
            new ApplicationServiceRequest<RegisterTenantCommand>(executionContext.CorrelationId, command),
            cancellationToken);
        return CreatedAtAction(nameof(RegisterTenant), new { tenantId }, new { tenantId });
    }

    [HttpPost("login")]
    public async Task<IActionResult> Login([FromBody] LoginCommand command, CancellationToken cancellationToken)
    {
        var result = await authService.LoginAsync(
            new ApplicationServiceRequest<LoginCommand>(executionContext.CorrelationId, command),
            cancellationToken);
        return Ok(result);
    }
}
