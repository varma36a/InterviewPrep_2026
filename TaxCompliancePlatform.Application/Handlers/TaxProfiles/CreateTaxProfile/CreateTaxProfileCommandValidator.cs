using FluentValidation;

namespace TaxCompliancePlatform.Application.Handlers.TaxProfiles.CreateTaxProfile;

public sealed class CreateTaxProfileCommandValidator : AbstractValidator<CreateTaxProfileCommand>
{
    public CreateTaxProfileCommandValidator()
    {
        RuleFor(x => x.TaxIdentifier).NotEmpty().MaximumLength(50);
        RuleFor(x => x.CountryCode).NotEmpty().Length(2);
        RuleFor(x => x.AnnualTaxableIncome).GreaterThanOrEqualTo(0);
        RuleFor(x => x.Deductions).GreaterThanOrEqualTo(0);
        RuleFor(x => x.FiscalYear).InclusiveBetween(2000, 2100);
    }
}
