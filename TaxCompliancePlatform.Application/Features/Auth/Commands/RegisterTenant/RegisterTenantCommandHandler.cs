using MediatR;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Domain.Entities;
using TaxCompliancePlatform.Domain.Enums;

namespace TaxCompliancePlatform.Application.Features.Auth.Commands.RegisterTenant;

public sealed class RegisterTenantCommandHandler(IRepository<Tenant> tenantRepository, IRepository<User> userRepository, IRepository<UserRole> userRoleRepository, IUnitOfWork unitOfWork)
    : IRequestHandler<RegisterTenantCommand, Guid>
{
    public async Task<Guid> Handle(RegisterTenantCommand request, CancellationToken cancellationToken)
    {
        var tenant = new Tenant(request.TenantName.Trim(), request.TenantSlug.Trim().ToLowerInvariant(), request.ContactEmail.Trim().ToLowerInvariant());
        await tenantRepository.AddAsync(tenant, cancellationToken);

        var admin = new User(tenant.Id, request.AdminEmail.Trim().ToLowerInvariant(), request.AdminFullName.Trim(), BCrypt.Net.BCrypt.HashPassword(request.AdminPassword));
        await userRepository.AddAsync(admin, cancellationToken);

        var adminRole = new UserRole(admin.Id, SystemRoles.TenantAdmin);
        await userRoleRepository.AddAsync(adminRole, cancellationToken);

        await unitOfWork.SaveChangesAsync(cancellationToken);
        return tenant.Id;
    }
}
