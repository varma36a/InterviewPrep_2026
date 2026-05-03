using MediatR;
using Microsoft.Extensions.Logging;
using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.Auth.Common;
using TaxCompliancePlatform.Application.Handlers.Auth.Login;
using TaxCompliancePlatform.Application.Handlers.Auth.RegisterTenant;
using TaxCompliancePlatform.Application.Providers.Correlation;

namespace TaxCompliancePlatform.Application.Services.Auth;

public sealed class AuthService(
    IMediator mediator,
    ICorrelationContext correlationContext,
    ILogger<AuthService> logger) : IAuthService
{
    public async Task<AuthResponse> LoginAsync(
        ApplicationServiceRequest<LoginCommand> request,
        CancellationToken cancellationToken)
    {
        EnsureCorrelationMatchesAmbient(request.CorrelationId);
        using var scope = logger.BeginScope(new Dictionary<string, object?>
        {
            ["CorrelationId"] = request.CorrelationId
        });
        logger.LogDebug("Orchestrating {Command}", nameof(LoginCommand));
        return await mediator.Send(request.Command, cancellationToken);
    }

    public async Task<Guid> RegisterTenantAsync(
        ApplicationServiceRequest<RegisterTenantCommand> request,
        CancellationToken cancellationToken)
    {
        EnsureCorrelationMatchesAmbient(request.CorrelationId);
        using var scope = logger.BeginScope(new Dictionary<string, object?>
        {
            ["CorrelationId"] = request.CorrelationId
        });
        logger.LogDebug("Orchestrating {Command}", nameof(RegisterTenantCommand));
        return await mediator.Send(request.Command, cancellationToken);
    }

    private void EnsureCorrelationMatchesAmbient(string requestCorrelationId)
    {
        var ambient = correlationContext.CorrelationId;
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
