using TaxCompliancePlatform.Domain.Common;

namespace TaxCompliancePlatform.Domain.Entities;

public sealed class TaxComputation : BaseEntity
{
    public Guid TenantId { get; private set; }
    public Guid TaxProfileId { get; private set; }
    public decimal TaxableAmount { get; private set; }
    public decimal TaxRate { get; private set; }
    public decimal TaxLiability { get; private set; }
    public DateTime ComputedAtUtc { get; private set; } = DateTime.UtcNow;

    private TaxComputation()
    {
    }

    public TaxComputation(Guid tenantId, Guid taxProfileId, decimal taxableAmount, decimal taxRate, decimal taxLiability)
    {
        TenantId = tenantId;
        TaxProfileId = taxProfileId;
        TaxableAmount = taxableAmount;
        TaxRate = taxRate;
        TaxLiability = taxLiability;
    }
}
