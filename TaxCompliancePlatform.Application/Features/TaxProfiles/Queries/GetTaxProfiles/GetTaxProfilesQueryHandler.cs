using MediatR;
using Microsoft.EntityFrameworkCore;
using TaxCompliancePlatform.Application.Abstractions.CurrentUser;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Features.TaxProfiles.Queries.GetTaxProfiles;

public sealed class GetTaxProfilesQueryHandler(ICurrentTenantProvider currentTenantProvider, IRepository<TaxProfile> taxProfileRepository)
    : IRequestHandler<GetTaxProfilesQuery, IReadOnlyCollection<TaxProfileDto>>
{
    public async Task<IReadOnlyCollection<TaxProfileDto>> Handle(GetTaxProfilesQuery request, CancellationToken cancellationToken)
    {
        if (!currentTenantProvider.HasTenant)
        {
            throw new UnauthorizedAccessException("Tenant context is missing.");
        }

        var skip = (Math.Max(request.PageNumber, 1) - 1) * Math.Clamp(request.PageSize, 1, 100);
        var take = Math.Clamp(request.PageSize, 1, 100);

        var profiles = await taxProfileRepository.Query()
            .AsNoTracking()
            .Where(x => x.TenantId == currentTenantProvider.TenantId)
            .OrderByDescending(x => x.CreatedAtUtc)
            .Skip(skip)
            .Take(take)
            .Select(x => new TaxProfileDto(x.Id, x.TaxIdentifier, x.CountryCode, x.AnnualTaxableIncome, x.Deductions, x.FiscalYear))
            .ToListAsync(cancellationToken);

        return profiles;
    }
}
