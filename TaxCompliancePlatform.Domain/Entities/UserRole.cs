using TaxCompliancePlatform.Domain.Common;

namespace TaxCompliancePlatform.Domain.Entities;

public sealed class UserRole : BaseEntity
{
    public Guid UserId { get; private set; }
    public string RoleName { get; private set; } = string.Empty;

    private UserRole()
    {
    }

    public UserRole(Guid userId, string roleName)
    {
        UserId = userId;
        RoleName = roleName;
    }
}
