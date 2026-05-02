using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Abstractions.Authentication;

public interface IJwtTokenService
{
    string GenerateAccessToken(User user, IEnumerable<string> roles, Guid tenantId, string correlationId);
    string GenerateRefreshToken();
}
