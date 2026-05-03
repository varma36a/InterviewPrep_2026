namespace TaxCompliancePlatform.Domain.Enums;

/// <summary>
/// How the customer received their order — affects local use-tax nexus assumptions in the sample scenario.
/// </summary>
public enum DominoFulfillmentChannel
{
    Carryout = 0,
    Delivery = 1
}
