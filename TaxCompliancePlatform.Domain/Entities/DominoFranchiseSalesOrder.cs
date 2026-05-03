using TaxCompliancePlatform.Domain.Common;
using TaxCompliancePlatform.Domain.Enums;

namespace TaxCompliancePlatform.Domain.Entities;

/// <summary>
/// Sample compliance record: a Domino's franchise store reports taxable pizza sales for a tenant (franchisee / market office).
/// </summary>
public sealed class DominoFranchiseSalesOrder : BaseEntity
{
    public Guid TenantId { get; private set; }
    public string StoreCode { get; private set; } = string.Empty;
    public string MarketRegion { get; private set; } = string.Empty;
    public DominoFulfillmentChannel Channel { get; private set; }
    public string CustomerOrderReference { get; private set; } = string.Empty;
    public decimal PretaxAmount { get; private set; }
    public decimal EstimatedSalesTax { get; private set; }
    public string CorrelationId { get; private set; } = string.Empty;

    private DominoFranchiseSalesOrder()
    {
    }

    public DominoFranchiseSalesOrder(
        Guid tenantId,
        string storeCode,
        string marketRegion,
        DominoFulfillmentChannel channel,
        string customerOrderReference,
        decimal pretaxAmount,
        decimal estimatedSalesTax,
        string correlationId)
    {
        TenantId = tenantId;
        StoreCode = storeCode;
        MarketRegion = marketRegion;
        Channel = channel;
        CustomerOrderReference = customerOrderReference;
        PretaxAmount = pretaxAmount;
        EstimatedSalesTax = estimatedSalesTax;
        CorrelationId = correlationId;
    }
}
