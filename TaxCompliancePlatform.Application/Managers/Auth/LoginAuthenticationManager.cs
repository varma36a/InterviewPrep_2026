using Microsoft.EntityFrameworkCore;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Application.Handlers.Auth.Login;
using TaxCompliancePlatform.Application.Strategy.Security;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Managers.Auth;

public sealed class LoginAuthenticationManager(
    IRepository<User> userRepository,
    IRepository<UserRole> roleRepository,
    IPasswordHasher passwordHasher) : ILoginAuthenticationManager
{
    public async Task<(User User, IReadOnlyList<string> Roles)> ValidateCredentialsAsync(
        LoginCommand command,
        CancellationToken cancellationToken)
    {
        var user = await userRepository.Query()
            .AsNoTracking()
            .FirstOrDefaultAsync(x => x.Email == command.Email.ToLowerInvariant(), cancellationToken)
            ?? throw new UnauthorizedAccessException("Invalid credentials.");

        if (!passwordHasher.Verify(command.Password, user.PasswordHash))
        {
            throw new UnauthorizedAccessException("Invalid credentials.");
        }

        var roles = await roleRepository.Query()
            .AsNoTracking()
            .Where(x => x.UserId == user.Id)
            .Select(x => x.RoleName)
            .ToListAsync(cancellationToken);

        return (user, roles);
    }
}
