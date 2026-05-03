using MediatR;
using Microsoft.Extensions.Logging;
using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.Auth.Common;
using TaxCompliancePlatform.Application.Handlers.Auth.Login;
using TaxCompliancePlatform.Application.Handlers.Auth.RegisterTenant;
using TaxCompliancePlatform.Application.Providers.Execution;

namespace TaxCompliancePlatform.Application.Services.Auth;

public sealed class AuthService(
    IMediator mediator,
    IRequestExecutionContext executionContext,
    ILogger<AuthService> logger) : IAuthService
{
    public async Task<AuthResponse> LoginAsync(
        ApplicationServiceRequest<LoginCommand> request,
        CancellationToken cancellationToken)
    {
        EnsureCorrelationMatchesAmbient(request.CorrelationId);
        using var scope = logger.BeginScope(BuildScope(request.CorrelationId));
        logger.LogDebug("Orchestrating {Command}", nameof(LoginCommand));
        return await mediator.Send(request.Command, cancellationToken);
    }

    public async Task<Guid> RegisterTenantAsync(
        ApplicationServiceRequest<RegisterTenantCommand> request,
        CancellationToken cancellationToken)
    {
        EnsureCorrelationMatchesAmbient(request.CorrelationId);
        using var scope = logger.BeginScope(BuildScope(request.CorrelationId));
        logger.LogDebug("Orchestrating {Command}", nameof(RegisterTenantCommand));
        return await mediator.Send(request.Command, cancellationToken);
    }

    private Dictionary<string, object?> BuildScope(string correlationFromRequest) => new()
    {
        ["CorrelationId"] = correlationFromRequest,
        ["TenantId"] = executionContext.TenantId,
        ["DominoStoreCode"] = executionContext.DominoStoreCode,
        ["DominoMarketRegion"] = executionContext.DominoMarketRegion,
        ["DominoChannel"] = executionContext.DominoFulfillmentChannel.ToString()
    };

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
