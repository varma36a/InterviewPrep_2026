using TaxCompliancePlatform.Application.Abstractions.CurrentUser;

namespace TaxCompliancePlatform.Infrastructure.Tenancy;

public sealed class CurrentTenantProvider : ICurrentTenantProvider
{
    private Guid? _tenantId;

    public Guid TenantId => _tenantId ?? throw new InvalidOperationException("Tenant has not been resolved.");
    public bool HasTenant => _tenantId.HasValue;

    public void SetTenant(Guid tenantId) => _tenantId = tenantId;
}
