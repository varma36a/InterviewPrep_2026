using MediatR;
using TaxCompliancePlatform.Application.Common;

namespace TaxCompliancePlatform.Application.Handlers.TaxProfiles.GetTaxProfiles;

public sealed record GetTaxProfilesQuery(string? Cursor, int Limit = 20)
    : IRequest<CursorPagedResponse<TaxProfileDto>>;

public sealed record TaxProfileDto(
    Guid Id,
    string TaxIdentifier,
    string CountryCode,
    decimal AnnualTaxableIncome,
    decimal Deductions,
    int FiscalYear);
