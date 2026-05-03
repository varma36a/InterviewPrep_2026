using FluentValidation;

namespace TaxCompliancePlatform.Application.Handlers.Account.PatchCurrentUserEmail;

public sealed class PatchCurrentUserEmailCommandValidator : AbstractValidator<PatchCurrentUserEmailCommand>
{
    public PatchCurrentUserEmailCommandValidator()
    {
        RuleFor(x => x.Email).NotEmpty().EmailAddress().MaximumLength(150);
    }
}
