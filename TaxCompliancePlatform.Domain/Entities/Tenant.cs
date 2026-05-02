using TaxCompliancePlatform.Domain.Common;

namespace TaxCompliancePlatform.Domain.Entities;

public sealed class Tenant : BaseEntity
{
    public string Name { get; private set; } = string.Empty;
    public string Slug { get; private set; } = string.Empty;
    public string ContactEmail { get; private set; } = string.Empty;
    public bool IsActive { get; private set; } = true;

    private readonly List<User> _users = [];
    public IReadOnlyCollection<User> Users => _users;

    private Tenant()
    {
    }

    public Tenant(string name, string slug, string contactEmail)
    {
        Name = name;
        Slug = slug;
        ContactEmail = contactEmail;
    }
}
