namespace TaxCompliancePlatform.Application.Providers.Correlation;

/// <summary>
/// Ambient correlation identifier for the current logical request (populated by the host, e.g. HTTP middleware).
/// Application defines the contract; API/Infrastructure provide the implementation.
/// </summary>
public interface ICorrelationContext
{
    string CorrelationId { get; }
}
