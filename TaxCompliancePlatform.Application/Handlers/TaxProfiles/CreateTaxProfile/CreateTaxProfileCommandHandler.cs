using MediatR;
using TaxCompliancePlatform.Application.Abstractions.CurrentUser;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Handlers.TaxProfiles.CreateTaxProfile;

public sealed class CreateTaxProfileCommandHandler(
    ICurrentTenantProvider currentTenantProvider,
    IRepository<TaxProfile> taxProfileRepository,
    IUnitOfWork unitOfWork)
    : IRequestHandler<CreateTaxProfileCommand, Guid>
{
    public async Task<Guid> Handle(CreateTaxProfileCommand request, CancellationToken cancellationToken)
    {
        if (!currentTenantProvider.HasTenant)
        {
            throw new ArgumentException(
                "Tenant context is missing. Send HTTP header X-Tenant-Id with your tenant UUID (from POST /api/v1/auth/tenants/register), or set TenantResolution:DefaultTenantId in appsettings.Development.json for local runs without that header.");
        }

        var profile = new TaxProfile(
            currentTenantProvider.TenantId,
            request.TaxIdentifier.Trim(),
            request.CountryCode.Trim().ToUpperInvariant(),
            request.AnnualTaxableIncome,
            request.Deductions,
            request.FiscalYear);

        await taxProfileRepository.AddAsync(profile, cancellationToken);
        await unitOfWork.SaveChangesAsync(cancellationToken);
        return profile.Id;
    }
}
