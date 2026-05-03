using TaxCompliancePlatform.Application.Common;
using TaxCompliancePlatform.Application.Handlers.Account.PatchCurrentUserEmail;

namespace TaxCompliancePlatform.Application.Services.Account;

public interface IAccountService
{
    Task PatchCurrentUserEmailAsync(
        ApplicationServiceRequest<PatchCurrentUserEmailCommand> request,
        CancellationToken cancellationToken);
}
