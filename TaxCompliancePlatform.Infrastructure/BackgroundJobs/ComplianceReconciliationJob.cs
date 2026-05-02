using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Infrastructure.BackgroundJobs;

public sealed class ComplianceReconciliationJob(IServiceScopeFactory scopeFactory, ILogger<ComplianceReconciliationJob> logger) : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        await Task.Delay(TimeSpan.FromMinutes(1), stoppingToken);

        while (!stoppingToken.IsCancellationRequested)
        {
            using var scope = scopeFactory.CreateScope();
            var auditRepository = scope.ServiceProvider.GetRequiredService<IRepository<AuditLog>>();
            var unitOfWork = scope.ServiceProvider.GetRequiredService<IUnitOfWork>();

            await auditRepository.AddAsync(
                new AuditLog(null, null, "BackgroundJob", "ComplianceReconciliation", "Periodic compliance reconciliation heartbeat", Guid.NewGuid().ToString("N")),
                stoppingToken);
            await unitOfWork.SaveChangesAsync(stoppingToken);

            logger.LogInformation("Compliance reconciliation heartbeat completed at {UtcNow}", DateTime.UtcNow);
            await Task.Delay(TimeSpan.FromMinutes(5), stoppingToken);
        }
    }
}
