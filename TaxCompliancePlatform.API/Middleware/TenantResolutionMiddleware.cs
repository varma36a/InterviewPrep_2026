using Microsoft.EntityFrameworkCore;
using TaxCompliancePlatform.Application.Abstractions.CurrentUser;
using TaxCompliancePlatform.Infrastructure.Persistence;
using TaxCompliancePlatform.Infrastructure.Tenancy;

namespace TaxCompliancePlatform.API.Middleware;

public sealed class TenantResolutionMiddleware(RequestDelegate next)
{
    public const string TenantHeaderName = "X-Tenant-Id";

    public async Task Invoke(HttpContext context, ICurrentTenantProvider currentTenantProvider, ApplicationDbContext dbContext)
    {
        if (context.Request.Headers.TryGetValue(TenantHeaderName, out var tenantHeader) &&
            Guid.TryParse(tenantHeader.ToString(), out var tenantId))
        {
            var exists = await dbContext.Tenants.AsNoTracking().AnyAsync(x => x.Id == tenantId, context.RequestAborted);
            if (exists)
            {
                if (currentTenantProvider is CurrentTenantProvider concreteProvider)
                {
                    concreteProvider.SetTenant(tenantId);
                }
            }
        }

        await next(context);
    }
}
