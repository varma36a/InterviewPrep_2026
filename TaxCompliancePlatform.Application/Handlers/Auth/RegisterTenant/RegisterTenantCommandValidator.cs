using FluentValidation;

namespace TaxCompliancePlatform.Application.Handlers.Auth.RegisterTenant;

public sealed class RegisterTenantCommandValidator : AbstractValidator<RegisterTenantCommand>
{
    public RegisterTenantCommandValidator()
    {
        RuleFor(x => x.TenantName).NotEmpty().MaximumLength(150);
        RuleFor(x => x.TenantSlug).NotEmpty().MaximumLength(80);
        RuleFor(x => x.ContactEmail).NotEmpty().EmailAddress();
        RuleFor(x => x.AdminFullName).NotEmpty().MaximumLength(120);
        RuleFor(x => x.AdminEmail).NotEmpty().EmailAddress();
        RuleFor(x => x.AdminPassword).NotEmpty().MinimumLength(8);
    }
}
