using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Hosting;
using TaxCompliancePlatform.Domain.Common;
using TaxCompliancePlatform.Domain.Entities;
using TaxCompliancePlatform.Infrastructure.Persistence;

namespace TaxCompliancePlatform.API.Hosting;

/// <summary>
/// Ensures <see cref="TenantResolutionMiddleware"/> default tenant id exists in MongoDB (Development only).
/// </summary>
public sealed class DevelopmentTenantBootstrapper(
    IHostEnvironment environment,
    IServiceScopeFactory scopeFactory,
    IConfiguration configuration,
    ILogger<DevelopmentTenantBootstrapper> logger) : IHostedService
{
    public async Task StartAsync(CancellationToken cancellationToken)
    {
        if (!environment.IsDevelopment())
        {
            return;
        }

        var raw = configuration["TenantResolution:DefaultTenantId"];
        if (string.IsNullOrWhiteSpace(raw) || !Guid.TryParse(raw.Trim(), out var tenantId))
        {
            return;
        }

        using var scope = scopeFactory.CreateScope();
        var db = scope.ServiceProvider.GetRequiredService<ApplicationDbContext>();

        if (await db.Tenants.AsNoTracking().AnyAsync(t => t.Id == tenantId, cancellationToken))
        {
            return;
        }

        var tenant = new Tenant("Development tenant", $"dev-{tenantId:N}", "dev-tenant@localhost");
        typeof(BaseEntity).GetProperty(nameof(BaseEntity.Id))!.SetValue(tenant, tenantId);

        await db.Tenants.AddAsync(tenant, cancellationToken);
        await db.SaveChangesAsync(cancellationToken);
        logger.LogInformation("Created development tenant {TenantId} for TenantResolution:DefaultTenantId.", tenantId);
    }

    public Task StopAsync(CancellationToken cancellationToken) => Task.CompletedTask;
}
