using MediatR;

namespace TaxCompliancePlatform.Application.Features.TaxProfiles.Commands.CreateTaxProfile;

public sealed record CreateTaxProfileCommand(
    string TaxIdentifier,
    string CountryCode,
    decimal AnnualTaxableIncome,
    decimal Deductions,
    int FiscalYear) : IRequest<Guid>;
