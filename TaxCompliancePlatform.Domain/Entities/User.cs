using TaxCompliancePlatform.Domain.Common;

namespace TaxCompliancePlatform.Domain.Entities;

public sealed class User : BaseEntity
{
    public Guid TenantId { get; private set; }
    public string Email { get; private set; } = string.Empty;
    public string FullName { get; private set; } = string.Empty;
    public string PasswordHash { get; private set; } = string.Empty;
    public bool IsActive { get; private set; } = true;

    private readonly List<UserRole> _roles = [];
    public IReadOnlyCollection<UserRole> Roles => _roles;

    private User()
    {
    }

    public User(Guid tenantId, string email, string fullName, string passwordHash)
    {
        TenantId = tenantId;
        Email = email;
        FullName = fullName;
        PasswordHash = passwordHash;
    }

    /// <summary>Partial update: email only (normalized to lower-case invariant).</summary>
    public void UpdateEmail(string email)
    {
        var normalized = email?.Trim().ToLowerInvariant()
            ?? throw new ArgumentException("Email is required.", nameof(email));
        if (string.IsNullOrWhiteSpace(normalized))
        {
            throw new ArgumentException("Email is required.", nameof(email));
        }

        Email = normalized;
        Touch();
    }
}
