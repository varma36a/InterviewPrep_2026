using SolidPrinciples.Bird.Shared;

namespace SolidPrinciples.Bird.D_DependencyInversion;

/// <summary>
/// D — Dependency Inversion: high-level BirdSanctuaryService depends on abstractions, not concrete storage or alerts.
/// </summary>
public interface IBirdCatalogRepository
{
    Task<IReadOnlyList<BirdProfile>> GetResidentsAsync(CancellationToken cancellationToken);
}

public interface IBirdAlertNotifier
{
    Task NotifyAsync(string message, CancellationToken cancellationToken);
}
