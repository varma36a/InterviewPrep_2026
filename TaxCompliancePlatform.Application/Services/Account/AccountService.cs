using MediatR;
using Microsoft.Extensions.Logging;
using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.Account.PatchCurrentUserEmail;
using TaxCompliancePlatform.Application.Providers.Execution;

namespace TaxCompliancePlatform.Application.Services.Account;

public sealed class AccountService(
    IMediator mediator,
    IRequestExecutionContext executionContext,
    ILogger<AccountService> logger) : IAccountService
{
    public async Task PatchCurrentUserEmailAsync(
        ApplicationServiceRequest<PatchCurrentUserEmailCommand> request,
        CancellationToken cancellationToken)
    {
        EnsureCorrelationMatchesAmbient(request.CorrelationId);
        using var scope = logger.BeginScope(new Dictionary<string, object?>
        {
            ["CorrelationId"] = request.CorrelationId,
            ["TenantId"] = executionContext.TenantId
        });
        logger.LogDebug("Orchestrating {Command}", nameof(PatchCurrentUserEmailCommand));
        await mediator.Send(request.Command, cancellationToken);
    }

    private void EnsureCorrelationMatchesAmbient(string requestCorrelationId)
    {
        var ambient = executionContext.CorrelationId;
        if (string.IsNullOrWhiteSpace(ambient) || string.IsNullOrWhiteSpace(requestCorrelationId))
        {
            return;
        }

        if (!string.Equals(ambient, requestCorrelationId, StringComparison.Ordinal))
        {
            throw new InvalidOperationException(
                "The correlation id on the service request does not match the ambient correlation context.");
        }
    }
}
