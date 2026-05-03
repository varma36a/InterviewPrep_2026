using MediatR;

namespace TaxCompliancePlatform.Application.Handlers.Auth.RegisterTenant;

public sealed record RegisterTenantCommand(
    string TenantName,
    string TenantSlug,
    string ContactEmail,
    string AdminFullName,
    string AdminEmail,
    string AdminPassword) : IRequest<Guid>;
