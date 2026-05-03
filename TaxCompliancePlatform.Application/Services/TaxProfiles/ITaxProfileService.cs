using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.TaxProfiles.CreateTaxProfile;
using TaxCompliancePlatform.Application.Handlers.TaxProfiles.GetTaxProfiles;

namespace TaxCompliancePlatform.Application.Services.TaxProfiles;

public interface ITaxProfileService
{
    Task<CursorPagedResponse<TaxProfileDto>> GetTaxProfilesAsync(
        ApplicationServiceRequest<GetTaxProfilesQuery> request,
        CancellationToken cancellationToken);

    Task<Guid> CreateTaxProfileAsync(
        ApplicationServiceRequest<CreateTaxProfileCommand> request,
        CancellationToken cancellationToken);
}
