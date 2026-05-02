namespace TaxCompliancePlatform.Application.Abstractions.CurrentUser;

public interface ICurrentTenantProvider
{
    Guid TenantId { get; }
    bool HasTenant { get; }
}
