namespace TaxCompliancePlatform.Application.Managers.Domino;

public sealed class DominoSalesTaxEstimator : IDominoSalesTaxEstimator
{
    public decimal EstimateSalesTax(decimal pretaxAmount, string marketRegion)
    {
        if (pretaxAmount <= 0)
        {
            return 0;
        }

        var region = marketRegion.Trim().ToUpperInvariant();
        var rate = region switch
        {
            var r when r.Contains("IL", StringComparison.Ordinal) => 0.1025m,
            var r when r.Contains("NY", StringComparison.Ordinal) => 0.08875m,
            var r when r.Contains("TX", StringComparison.Ordinal) => 0.0825m,
            _ => 0.08m
        };

        return Math.Round(pretaxAmount * rate, 2, MidpointRounding.AwayFromZero);
    }
}
