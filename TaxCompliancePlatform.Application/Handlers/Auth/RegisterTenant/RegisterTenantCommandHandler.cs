using MediatR;
using TaxCompliancePlatform.Application.Managers.Tenants;

namespace TaxCompliancePlatform.Application.Handlers.Auth.RegisterTenant;

public sealed class RegisterTenantCommandHandler(ITenantRegistrationManager tenantRegistrationManager)
    : IRequestHandler<RegisterTenantCommand, Guid>
{
    public Task<Guid> Handle(RegisterTenantCommand request, CancellationToken cancellationToken) =>
        tenantRegistrationManager.ProvisionNewTenantAsync(request, cancellationToken);
}
