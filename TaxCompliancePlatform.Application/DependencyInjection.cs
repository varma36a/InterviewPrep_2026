using FluentValidation;
using MediatR;
using Microsoft.Extensions.DependencyInjection;
using TaxCompliancePlatform.Application.Managers.Auth;
using TaxCompliancePlatform.Application.Managers.Domino;
using TaxCompliancePlatform.Application.Managers.Tenants;
using TaxCompliancePlatform.Application.Pipeline;
using TaxCompliancePlatform.Application.Services.Auth;
using TaxCompliancePlatform.Application.Services.DominoFranchise;
using TaxCompliancePlatform.Application.Services.TaxProfiles;

namespace TaxCompliancePlatform.Application;

public static class DependencyInjection
{
    public static IServiceCollection AddApplication(this IServiceCollection services)
    {
        services.AddMediatR(cfg =>
        {
            cfg.RegisterServicesFromAssembly(typeof(DependencyInjection).Assembly);
            cfg.AddOpenBehavior(typeof(ExecutionContextLoggingBehavior<,>));
        });
        services.AddValidatorsFromAssembly(typeof(DependencyInjection).Assembly);

        services.AddScoped<IAuthService, AuthService>();
        services.AddScoped<ITaxProfileService, TaxProfileService>();
        services.AddScoped<IDominoFranchiseTaxService, DominoFranchiseTaxService>();
        services.AddScoped<ITenantRegistrationManager, TenantRegistrationManager>();
        services.AddScoped<ILoginAuthenticationManager, LoginAuthenticationManager>();
        services.AddScoped<IDominoSalesTaxEstimator, DominoSalesTaxEstimator>();

        return services;
    }
}
