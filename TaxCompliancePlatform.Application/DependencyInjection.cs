using FluentValidation;
using MediatR;
using Microsoft.Extensions.DependencyInjection;
using TaxCompliancePlatform.Application.Managers.Auth;
using TaxCompliancePlatform.Application.Managers.Tenants;
using TaxCompliancePlatform.Application.Services.Auth;
using TaxCompliancePlatform.Application.Services.TaxProfiles;

namespace TaxCompliancePlatform.Application;

public static class DependencyInjection
{
    public static IServiceCollection AddApplication(this IServiceCollection services)
    {
        services.AddMediatR(cfg => cfg.RegisterServicesFromAssembly(typeof(DependencyInjection).Assembly));
        services.AddValidatorsFromAssembly(typeof(DependencyInjection).Assembly);

        services.AddScoped<IAuthService, AuthService>();
        services.AddScoped<ITaxProfileService, TaxProfileService>();
        services.AddScoped<ITenantRegistrationManager, TenantRegistrationManager>();
        services.AddScoped<ILoginAuthenticationManager, LoginAuthenticationManager>();

        return services;
    }
}
