using MediatR;

namespace TaxCompliancePlatform.Application.Features.Auth.Commands.RegisterTenant;

public sealed record RegisterTenantCommand(
    string TenantName,
    string TenantSlug,
    string ContactEmail,
    string AdminFullName,
    string AdminEmail,
    string AdminPassword) : IRequest<Guid>;
