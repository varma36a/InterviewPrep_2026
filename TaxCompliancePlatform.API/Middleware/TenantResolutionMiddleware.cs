using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using TaxCompliancePlatform.Application.Abstractions.CurrentUser;
using TaxCompliancePlatform.Infrastructure.Persistence;
using TaxCompliancePlatform.Infrastructure.Tenancy;

namespace TaxCompliancePlatform.API.Middleware;

public sealed class TenantResolutionMiddleware(RequestDelegate next)
{
    public const string TenantHeaderName = "X-Tenant-Id";

    public async Task Invoke(
        HttpContext context,
        ICurrentTenantProvider currentTenantProvider,
        ApplicationDbContext dbContext,
        IConfiguration configuration)
    {
        if (currentTenantProvider is not CurrentTenantProvider concreteProvider)
        {
            await next(context);
            return;
        }

        if (context.Request.Headers.TryGetValue(TenantHeaderName, out var tenantHeader) &&
            Guid.TryParse(tenantHeader.ToString(), out var tenantId))
        {
            var exists = await dbContext.Tenants.AsNoTracking().AnyAsync(x => x.Id == tenantId, context.RequestAborted);
            if (exists)
            {
                concreteProvider.SetTenant(tenantId);
            }
        }

        if (!concreteProvider.HasTenant)
        {
            var defaultTenant = configuration["TenantResolution:DefaultTenantId"];
            if (!string.IsNullOrWhiteSpace(defaultTenant) &&
                Guid.TryParse(defaultTenant.Trim(), out var defaultTenantId))
            {
                var exists = await dbContext.Tenants.AsNoTracking().AnyAsync(x => x.Id == defaultTenantId, context.RequestAborted);
                if (exists)
                {
                    concreteProvider.SetTenant(defaultTenantId);
                }
            }
        }

        await next(context);
    }
}
