using FluentValidation;

namespace TaxCompliancePlatform.Application.Handlers.DominoFranchise.CreateDominoFranchiseSalesOrder;

public sealed class CreateDominoFranchiseSalesOrderCommandValidator : AbstractValidator<CreateDominoFranchiseSalesOrderCommand>
{
    public CreateDominoFranchiseSalesOrderCommandValidator()
    {
        RuleFor(x => x.CustomerOrderReference).NotEmpty().MaximumLength(40);
        RuleFor(x => x.PretaxAmount).GreaterThan(0);
    }
}
