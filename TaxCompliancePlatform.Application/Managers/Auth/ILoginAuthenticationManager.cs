using TaxCompliancePlatform.Application.Handlers.Auth.Login;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Managers.Auth;

public interface ILoginAuthenticationManager
{
    Task<(User User, IReadOnlyList<string> Roles)> ValidateCredentialsAsync(
        LoginCommand command,
        CancellationToken cancellationToken);
}
