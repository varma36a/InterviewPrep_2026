using Asp.Versioning;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.Account.PatchCurrentUserEmail;
using TaxCompliancePlatform.Application.Providers.Execution;
using TaxCompliancePlatform.Application.Services.Account;

namespace TaxCompliancePlatform.API.Controllers.v1;

/// <summary>
/// Authenticated account operations (partial updates).
/// </summary>
[ApiController]
[ApiVersion("1.0")]
[Authorize]
[Route("api/v{version:apiVersion}/account")]
public sealed class AccountController(IAccountService accountService, IRequestExecutionContext executionContext)
    : ControllerBase
{
    /// <summary>
    /// Partial update: change only the signed-in user's email. Send JSON body <c>{ "email": "new@example.com" }</c>.
    /// </summary>
    [HttpPatch("email")]
    public async Task<IActionResult> PatchEmail([FromBody] PatchEmailRequest body, CancellationToken cancellationToken)
    {
        await accountService.PatchCurrentUserEmailAsync(
            new ApplicationServiceRequest<PatchCurrentUserEmailCommand>(
                executionContext.CorrelationId,
                new PatchCurrentUserEmailCommand(body.Email)),
            cancellationToken);
        return NoContent();
    }
}

/// <summary>Merge-style body: only <see cref="Email"/> is applied; omitting other profile fields is expected.</summary>
public sealed record PatchEmailRequest(string Email);
