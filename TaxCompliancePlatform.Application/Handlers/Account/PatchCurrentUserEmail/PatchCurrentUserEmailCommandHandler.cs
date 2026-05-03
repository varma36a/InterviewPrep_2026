using MediatR;
using Microsoft.EntityFrameworkCore;
using TaxCompliancePlatform.Application.Abstractions.CurrentUser;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Handlers.Account.PatchCurrentUserEmail;

public sealed class PatchCurrentUserEmailCommandHandler(
    ICurrentUserAccessor currentUserAccessor,
    ICurrentTenantProvider currentTenantProvider,
    IRepository<User> userRepository,
    IUnitOfWork unitOfWork) : IRequestHandler<PatchCurrentUserEmailCommand>
{
    public async Task Handle(PatchCurrentUserEmailCommand request, CancellationToken cancellationToken)
    {
        if (currentUserAccessor.UserId is not { } userId)
        {
            throw new UnauthorizedAccessException("A valid Bearer token is required to update your email.");
        }

        if (!currentTenantProvider.HasTenant)
        {
            throw new ArgumentException(
                "Tenant context is missing. Send X-Tenant-Id or configure TenantResolution:DefaultTenantId.");
        }

        var user = await userRepository.GetByIdAsync(userId, cancellationToken)
            ?? throw new UnauthorizedAccessException("User was not found.");

        if (user.TenantId != currentTenantProvider.TenantId)
        {
            throw new UnauthorizedAccessException("User does not belong to the resolved tenant.");
        }

        var normalized = request.Email.Trim().ToLowerInvariant();
        var duplicate = await userRepository.Query()
            .AsNoTracking()
            .AnyAsync(
                x => x.TenantId == user.TenantId && x.Email == normalized && x.Id != user.Id,
                cancellationToken);
        if (duplicate)
        {
            throw new ArgumentException("Another user in this tenant already uses that email address.");
        }

        user.UpdateEmail(request.Email);
        userRepository.Update(user);
        await unitOfWork.SaveChangesAsync(cancellationToken);
    }
}
