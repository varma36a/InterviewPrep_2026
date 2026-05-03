namespace TaxCompliancePlatform.Application.Managers.Domino;

/// <summary>
/// Simplified regional sales-tax estimate for the Domino's franchise demo (not legal advice).
/// </summary>
public interface IDominoSalesTaxEstimator
{
    decimal EstimateSalesTax(decimal pretaxAmount, string marketRegion);
}
