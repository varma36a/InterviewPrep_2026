using MediatR;

namespace TaxCompliancePlatform.Application.Handlers.TaxProfiles.GetTaxProfiles;

public sealed record GetTaxProfilesQuery(int PageNumber = 1, int PageSize = 20)
    : IRequest<IReadOnlyCollection<TaxProfileDto>>;

public sealed record TaxProfileDto(
    Guid Id,
    string TaxIdentifier,
    string CountryCode,
    decimal AnnualTaxableIncome,
    decimal Deductions,
    int FiscalYear);
