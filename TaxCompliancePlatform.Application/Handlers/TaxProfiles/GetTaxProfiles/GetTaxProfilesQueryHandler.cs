using MediatR;
using Microsoft.EntityFrameworkCore;
using TaxCompliancePlatform.Application.Abstractions.CurrentUser;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Handlers.TaxProfiles.GetTaxProfiles;

public sealed class GetTaxProfilesQueryHandler(
    ICurrentTenantProvider currentTenantProvider,
    IRepository<TaxProfile> taxProfileRepository)
    : IRequestHandler<GetTaxProfilesQuery, CursorPagedResponse<TaxProfileDto>>
{
    public async Task<CursorPagedResponse<TaxProfileDto>> Handle(GetTaxProfilesQuery request, CancellationToken cancellationToken)
    {
        if (!currentTenantProvider.HasTenant)
        {
            throw new ArgumentException(
                "Tenant context is missing. Send HTTP header X-Tenant-Id with your tenant UUID (from POST /api/v1/auth/tenants/register), or set TenantResolution:DefaultTenantId in appsettings.Development.json for local runs without that header.");
        }

        if (!string.IsNullOrWhiteSpace(request.Cursor) && !ListCursorV1.TryDecode(request.Cursor, out _, out _))
        {
            throw new ArgumentException(
                "Invalid cursor value. Use the nextCursor from the previous response, or omit cursor for the first page.");
        }

        var limit = Math.Clamp(request.Limit, 1, 100);

        var query = taxProfileRepository.Query()
            .AsNoTracking()
            .Where(x => x.TenantId == currentTenantProvider.TenantId);

        if (ListCursorV1.TryDecode(request.Cursor, out var cursorAt, out var cursorId))
        {
            query = query.Where(x =>
                x.CreatedAtUtc < cursorAt ||
                (x.CreatedAtUtc == cursorAt && x.Id < cursorId));
        }

        var raw = await query
            .OrderByDescending(x => x.CreatedAtUtc)
            .ThenByDescending(x => x.Id)
            .Take(limit + 1)
            .Select(x => new
            {
                x.Id,
                x.TaxIdentifier,
                x.CountryCode,
                x.AnnualTaxableIncome,
                x.Deductions,
                x.FiscalYear,
                x.CreatedAtUtc
            })
            .ToListAsync(cancellationToken);

        var hasMore = raw.Count > limit;
        var page = hasMore ? raw.Take(limit).ToList() : raw;

        var items = page
            .Select(x => new TaxProfileDto(
                x.Id,
                x.TaxIdentifier,
                x.CountryCode,
                x.AnnualTaxableIncome,
                x.Deductions,
                x.FiscalYear))
            .ToList();

        string? nextCursor = null;
        if (hasMore && page.Count > 0)
        {
            var last = page[^1];
            nextCursor = ListCursorV1.Encode(last.CreatedAtUtc, last.Id);
        }

        return new CursorPagedResponse<TaxProfileDto>(items, nextCursor, hasMore);
    }
}
