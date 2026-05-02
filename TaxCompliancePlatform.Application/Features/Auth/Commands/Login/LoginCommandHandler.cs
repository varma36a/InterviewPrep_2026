using MediatR;
using Microsoft.EntityFrameworkCore;
using TaxCompliancePlatform.Application.Abstractions.Authentication;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Application.Features.Auth.Common;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Features.Auth.Commands.Login;

public sealed class LoginCommandHandler(IRepository<User> userRepository, IRepository<UserRole> roleRepository, IRepository<RefreshToken> refreshTokenRepository, IJwtTokenService jwtTokenService, IUnitOfWork unitOfWork)
    : IRequestHandler<LoginCommand, AuthResponse>
{
    public async Task<AuthResponse> Handle(LoginCommand request, CancellationToken cancellationToken)
    {
        var user = await userRepository.Query()
            .AsNoTracking()
            .FirstOrDefaultAsync(x => x.Email == request.Email.ToLowerInvariant(), cancellationToken)
            ?? throw new UnauthorizedAccessException("Invalid credentials.");

        if (!BCrypt.Net.BCrypt.Verify(request.Password, user.PasswordHash))
        {
            throw new UnauthorizedAccessException("Invalid credentials.");
        }

        var roles = await roleRepository.Query()
            .AsNoTracking()
            .Where(x => x.UserId == user.Id)
            .Select(x => x.RoleName)
            .ToListAsync(cancellationToken);

        var correlationId = Guid.NewGuid().ToString("N");
        var accessToken = jwtTokenService.GenerateAccessToken(user, roles, user.TenantId, correlationId);
        var refreshToken = jwtTokenService.GenerateRefreshToken();
        var refreshTokenEntity = new RefreshToken(user.Id, refreshToken, DateTime.UtcNow.AddDays(7));
        await refreshTokenRepository.AddAsync(refreshTokenEntity, cancellationToken);
        await unitOfWork.SaveChangesAsync(cancellationToken);

        return new AuthResponse(accessToken, refreshToken, DateTime.UtcNow.AddMinutes(30));
    }
}
