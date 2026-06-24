using SolidPrinciples.Bird.Shared;

namespace SolidPrinciples.Bird.D_DependencyInversion;

public sealed class InMemoryBirdCatalogRepository : IBirdCatalogRepository
{
    private static readonly IReadOnlyList<BirdProfile> Residents =
    [
        new("Atlas", "Eagle"),
        new("Ruby", "Robin"),
        new("Pip", "Penguin")
    ];

    public Task<IReadOnlyList<BirdProfile>> GetResidentsAsync(CancellationToken cancellationToken) =>
        Task.FromResult(Residents);
}
