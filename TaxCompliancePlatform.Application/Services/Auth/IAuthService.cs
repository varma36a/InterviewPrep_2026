using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.Auth.Common;
using TaxCompliancePlatform.Application.Handlers.Auth.Login;
using TaxCompliancePlatform.Application.Handlers.Auth.RegisterTenant;

namespace TaxCompliancePlatform.Application.Services.Auth;

public interface IAuthService
{
    Task<AuthResponse> LoginAsync(ApplicationServiceRequest<LoginCommand> request, CancellationToken cancellationToken);

    Task<Guid> RegisterTenantAsync(
        ApplicationServiceRequest<RegisterTenantCommand> request,
        CancellationToken cancellationToken);
}
