using MediatR;
using TaxCompliancePlatform.Application.Abstractions.Authentication;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Application.Handlers.Auth.Common;
using TaxCompliancePlatform.Application.Managers.Auth;
using TaxCompliancePlatform.Application.Providers.Execution;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Handlers.Auth.Login;

public sealed class LoginCommandHandler(
    ILoginAuthenticationManager loginAuthenticationManager,
    IJwtTokenService jwtTokenService,
    IRepository<RefreshToken> refreshTokenRepository,
    IUnitOfWork unitOfWork,
    IRequestExecutionContext executionContext)
    : IRequestHandler<LoginCommand, AuthResponse>
{
    public async Task<AuthResponse> Handle(LoginCommand request, CancellationToken cancellationToken)
    {
        var (user, roles) = await loginAuthenticationManager.ValidateCredentialsAsync(request, cancellationToken);

        var correlationId = string.IsNullOrWhiteSpace(executionContext.CorrelationId)
            ? Guid.NewGuid().ToString("N")
            : executionContext.CorrelationId;

        var accessToken = jwtTokenService.GenerateAccessToken(user, roles, user.TenantId, correlationId);
        var refreshToken = jwtTokenService.GenerateRefreshToken();
        var refreshTokenEntity = new RefreshToken(user.Id, refreshToken, DateTime.UtcNow.AddDays(7));
        await refreshTokenRepository.AddAsync(refreshTokenEntity, cancellationToken);
        await unitOfWork.SaveChangesAsync(cancellationToken);

        return new AuthResponse(accessToken, refreshToken, DateTime.UtcNow.AddMinutes(30));
    }
}
