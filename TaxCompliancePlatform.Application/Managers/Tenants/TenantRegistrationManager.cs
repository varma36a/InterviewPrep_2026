using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Application.Handlers.Auth.RegisterTenant;
using TaxCompliancePlatform.Application.Strategy.Security;
using TaxCompliancePlatform.Domain.Entities;
using TaxCompliancePlatform.Domain.Enums;

namespace TaxCompliancePlatform.Application.Managers.Tenants;

public sealed class TenantRegistrationManager(
    IRepository<Tenant> tenantRepository,
    IRepository<User> userRepository,
    IRepository<UserRole> userRoleRepository,
    IUnitOfWork unitOfWork,
    IPasswordHasher passwordHasher) : ITenantRegistrationManager
{
    public async Task<Guid> ProvisionNewTenantAsync(RegisterTenantCommand command, CancellationToken cancellationToken)
    {
        var tenant = new Tenant(
            command.TenantName.Trim(),
            command.TenantSlug.Trim().ToLowerInvariant(),
            command.ContactEmail.Trim().ToLowerInvariant());
        await tenantRepository.AddAsync(tenant, cancellationToken);

        var admin = new User(
            tenant.Id,
            command.AdminEmail.Trim().ToLowerInvariant(),
            command.AdminFullName.Trim(),
            passwordHasher.Hash(command.AdminPassword));
        await userRepository.AddAsync(admin, cancellationToken);

        var adminRole = new UserRole(admin.Id, SystemRoles.TenantAdmin);
        await userRoleRepository.AddAsync(adminRole, cancellationToken);

        await unitOfWork.SaveChangesAsync(cancellationToken);
        return tenant.Id;
    }
}
