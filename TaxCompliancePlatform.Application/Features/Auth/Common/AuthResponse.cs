namespace TaxCompliancePlatform.Application.Features.Auth.Common;

public sealed record AuthResponse(
    string AccessToken,
    string RefreshToken,
    DateTime AccessTokenExpiresAtUtc);
