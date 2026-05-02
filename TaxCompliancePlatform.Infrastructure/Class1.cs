using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using TaxCompliancePlatform.Application.Abstractions.Authentication;
using TaxCompliancePlatform.Application.Abstractions.CurrentUser;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Infrastructure.Authentication;
using TaxCompliancePlatform.Infrastructure.BackgroundJobs;
using TaxCompliancePlatform.Infrastructure.Persistence;
using TaxCompliancePlatform.Infrastructure.Persistence.Repositories;
using TaxCompliancePlatform.Infrastructure.Tenancy;

namespace TaxCompliancePlatform.Infrastructure;

public static class DependencyInjection
{
    public static IServiceCollection AddInfrastructure(this IServiceCollection services, IConfiguration configuration)
    {
        services.AddDbContext<ApplicationDbContext>(options =>
            options.UseSqlServer(configuration.GetConnectionString("DefaultConnection")));

        services.AddScoped<IApplicationDbContext>(provider => provider.GetRequiredService<ApplicationDbContext>());
        services.AddScoped<IUnitOfWork>(provider => provider.GetRequiredService<ApplicationDbContext>());
        services.AddScoped(typeof(IRepository<>), typeof(Repository<>));
        services.AddScoped<ICurrentTenantProvider, CurrentTenantProvider>();
        services.AddScoped<IJwtTokenService, JwtTokenService>();

        services.AddHostedService<ComplianceReconciliationJob>();
        services.AddStackExchangeRedisCache(options =>
        {
            options.Configuration = configuration.GetConnectionString("Redis");
            options.InstanceName = "tax-compliance";
        });

        return services;
    }
}
