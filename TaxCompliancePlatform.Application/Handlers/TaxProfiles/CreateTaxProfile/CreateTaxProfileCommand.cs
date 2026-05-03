using MediatR;

namespace TaxCompliancePlatform.Application.Handlers.TaxProfiles.CreateTaxProfile;

public sealed record CreateTaxProfileCommand(
    string TaxIdentifier,
    string CountryCode,
    decimal AnnualTaxableIncome,
    decimal Deductions,
    int FiscalYear) : IRequest<Guid>;
