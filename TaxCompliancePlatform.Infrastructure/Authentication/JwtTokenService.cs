using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Security.Cryptography;
using System.Text;
using Microsoft.Extensions.Configuration;
using Microsoft.IdentityModel.Tokens;
using TaxCompliancePlatform.Application.Abstractions.Authentication;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Infrastructure.Authentication;

public sealed class JwtTokenService(IConfiguration configuration) : IJwtTokenService
{
    public string GenerateAccessToken(User user, IEnumerable<string> roles, Guid tenantId, string correlationId)
    {
        var jwtConfig = configuration.GetSection("Jwt");
        var key = jwtConfig["Key"] ?? throw new InvalidOperationException("JWT key is missing.");
        var issuer = jwtConfig["Issuer"] ?? "TaxCompliancePlatform";
        var audience = jwtConfig["Audience"] ?? "TaxCompliancePlatform.Client";
        var expiryMinutes = int.TryParse(jwtConfig["AccessTokenExpiryMinutes"], out var configuredMinutes) ? configuredMinutes : 30;

        var claims = new List<Claim>
        {
            new(JwtRegisteredClaimNames.Sub, user.Id.ToString()),
            new(JwtRegisteredClaimNames.Email, user.Email),
            new("tenant_id", tenantId.ToString()),
            new("correlation_id", correlationId)
        };
        claims.AddRange(roles.Select(role => new Claim(ClaimTypes.Role, role)));

        var credentials = new SigningCredentials(new SymmetricSecurityKey(Encoding.UTF8.GetBytes(key)), SecurityAlgorithms.HmacSha256);
        var token = new JwtSecurityToken(
            issuer: issuer,
            audience: audience,
            claims: claims,
            expires: DateTime.UtcNow.AddMinutes(expiryMinutes),
            signingCredentials: credentials);

        return new JwtSecurityTokenHandler().WriteToken(token);
    }

    public string GenerateRefreshToken()
    {
        var bytes = RandomNumberGenerator.GetBytes(64);
        return Convert.ToBase64String(bytes);
    }
}
