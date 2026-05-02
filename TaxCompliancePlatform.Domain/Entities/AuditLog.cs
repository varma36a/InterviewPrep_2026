using TaxCompliancePlatform.Domain.Common;

namespace TaxCompliancePlatform.Domain.Entities;

public sealed class AuditLog : BaseEntity
{
    public Guid? TenantId { get; private set; }
    public Guid? UserId { get; private set; }
    public string Action { get; private set; } = string.Empty;
    public string Resource { get; private set; } = string.Empty;
    public string Details { get; private set; } = string.Empty;
    public string CorrelationId { get; private set; } = string.Empty;

    private AuditLog()
    {
    }

    public AuditLog(Guid? tenantId, Guid? userId, string action, string resource, string details, string correlationId)
    {
        TenantId = tenantId;
        UserId = userId;
        Action = action;
        Resource = resource;
        Details = details;
        CorrelationId = correlationId;
    }
}
