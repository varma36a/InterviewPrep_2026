namespace TaxCompliancePlatform.Application.Abstractions.CurrentUser;

/// <summary>
/// Authenticated user identity for the current request (from JWT when authorization is enabled).
/// </summary>
public interface ICurrentUserAccessor
{
    Guid? UserId { get; }
}
