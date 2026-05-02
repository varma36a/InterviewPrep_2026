using TaxCompliancePlatform.Application.Features.Auth.Commands.RegisterTenant;

namespace TaxCompliancePlatform.UnitTests;

public class RegisterTenantCommandValidatorTests
{
    [Fact]
    public void Should_Fail_When_Password_TooShort()
    {
        var validator = new RegisterTenantCommandValidator();
        var command = new RegisterTenantCommand("Acme Corp", "acme", "admin@acme.com", "Admin User", "admin@acme.com", "123");
        var result = validator.Validate(command);
        result.IsValid.Should().BeFalse();
    }
}