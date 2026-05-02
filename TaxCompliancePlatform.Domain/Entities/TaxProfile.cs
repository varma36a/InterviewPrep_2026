using TaxCompliancePlatform.Domain.Common;

namespace TaxCompliancePlatform.Domain.Entities;

public sealed class TaxProfile : BaseEntity
{
    public Guid TenantId { get; private set; }
    public string TaxIdentifier { get; private set; } = string.Empty;
    public string CountryCode { get; private set; } = string.Empty;
    public decimal AnnualTaxableIncome { get; private set; }
    public decimal Deductions { get; private set; }
    public int FiscalYear { get; private set; }

    private TaxProfile()
    {
    }

    public TaxProfile(Guid tenantId, string taxIdentifier, string countryCode, decimal annualTaxableIncome, decimal deductions, int fiscalYear)
    {
        TenantId = tenantId;
        TaxIdentifier = taxIdentifier;
        CountryCode = countryCode;
        AnnualTaxableIncome = annualTaxableIncome;
        Deductions = deductions;
        FiscalYear = fiscalYear;
    }
}
