using TaxCompliancePlatform.Application.Handlers.Auth.RegisterTenant;

namespace TaxCompliancePlatform.Application.Managers.Tenants;

public interface ITenantRegistrationManager
{
    Task<Guid> ProvisionNewTenantAsync(RegisterTenantCommand command, CancellationToken cancellationToken);
}
