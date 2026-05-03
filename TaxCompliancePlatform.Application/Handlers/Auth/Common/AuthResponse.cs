namespace TaxCompliancePlatform.Application.Handlers.Auth.Common;

public sealed record AuthResponse(
    string AccessToken,
    string RefreshToken,
    DateTime AccessTokenExpiresAtUtc);
