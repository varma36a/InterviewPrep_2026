using SolidPrinciples.Bird.Shared;

namespace SolidPrinciples.Bird.D_DependencyInversion;

public sealed class BirdSanctuaryService(
    IBirdCatalogRepository catalogRepository,
    IBirdAlertNotifier alertNotifier)
{
    public async Task<int> ConductHeadcountAsync(CancellationToken cancellationToken)
    {
        var residents = await catalogRepository.GetResidentsAsync(cancellationToken);
        var count = residents.Count;

        await alertNotifier.NotifyAsync(
            $"Sanctuary headcount complete: {count} birds ({string.Join(", ", residents.Select(r => r.Name))}).",
            cancellationToken);

        return count;
    }
}
