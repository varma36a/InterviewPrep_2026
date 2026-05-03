using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;

namespace TaxCompliancePlatform.API.Hosting;

/// <summary>
/// Registers JWT Bearer for first-party tokens and, when enabled, OAuth 2.0 / OIDC access tokens
/// from an external authority (e.g. Microsoft Entra ID) using a single Authorization: Bearer header.
/// </summary>
public static class AuthenticationConfiguration
{
    public const string FirstPartyJwtScheme = "FirstPartyJwt";
    public const string ExternalOAuth2JwtScheme = "ExternalOAuth2Jwt";

    public static IServiceCollection AddPlatformAuthentication(this IServiceCollection services, IConfiguration configuration)
    {
        var jwtKey = configuration["Jwt:Key"] ?? throw new InvalidOperationException("JWT key is not configured.");
        var oauth2Enabled = configuration.GetValue("OAuth2:Enabled", false);

        if (oauth2Enabled)
        {
            var authority = configuration["OAuth2:Authority"]
                ?? throw new InvalidOperationException("OAuth2:Authority is required when OAuth2:Enabled is true.");
            var audience = configuration["OAuth2:Audience"]
                ?? throw new InvalidOperationException("OAuth2:Audience is required when OAuth2:Enabled is true.");

            services.AddAuthentication(options =>
                {
                    options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
                    options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
                    options.DefaultForbidScheme = JwtBearerDefaults.AuthenticationScheme;
                })
                .AddPolicyScheme(JwtBearerDefaults.AuthenticationScheme, "FirstPartyOrExternalOAuth2", policyOptions =>
                {
                    policyOptions.ForwardDefaultSelector = SelectJwtBearerScheme;
                })
                .AddJwtBearer(FirstPartyJwtScheme, options => ConfigureFirstPartyJwtBearer(options, configuration, jwtKey))
                .AddJwtBearer(ExternalOAuth2JwtScheme, options =>
                    ConfigureExternalOAuth2JwtBearer(options, configuration, authority, audience));
        }
        else
        {
            services.AddAuthentication(options =>
                {
                    options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
                    options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
                    options.DefaultForbidScheme = JwtBearerDefaults.AuthenticationScheme;
                })
                .AddJwtBearer(JwtBearerDefaults.AuthenticationScheme, options =>
                    ConfigureFirstPartyJwtBearer(options, configuration, jwtKey));
        }

        return services;
    }

    private static string SelectJwtBearerScheme(HttpContext context)
    {
        var configuration = context.RequestServices.GetRequiredService<IConfiguration>();
        var firstPartyIssuer = configuration["Jwt:Issuer"];
        var authorization = context.Request.Headers.Authorization.ToString();
        if (string.IsNullOrWhiteSpace(authorization) ||
            !authorization.StartsWith("Bearer ", StringComparison.OrdinalIgnoreCase))
        {
            return FirstPartyJwtScheme;
        }

        var token = authorization["Bearer ".Length..].Trim();
        var handler = new JwtSecurityTokenHandler();
        if (!handler.CanReadToken(token))
        {
            return FirstPartyJwtScheme;
        }

        var jwt = handler.ReadJwtToken(token);
        if (!string.IsNullOrEmpty(firstPartyIssuer) &&
            string.Equals(jwt.Issuer, firstPartyIssuer, StringComparison.Ordinal))
        {
            return FirstPartyJwtScheme;
        }

        return ExternalOAuth2JwtScheme;
    }

    private static void ConfigureFirstPartyJwtBearer(
        JwtBearerOptions options,
        IConfiguration configuration,
        string jwtKey)
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateIssuerSigningKey = true,
            ValidateLifetime = true,
            ValidIssuer = configuration["Jwt:Issuer"],
            ValidAudience = configuration["Jwt:Audience"],
            IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(jwtKey))
        };
    }

    private static void ConfigureExternalOAuth2JwtBearer(
        JwtBearerOptions options,
        IConfiguration configuration,
        string authority,
        string audience)
    {
        options.Authority = authority.TrimEnd('/');
        options.Audience = audience;
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true
        };

        var mapAzureTenant = configuration.GetValue("OAuth2:MapAzureTenantIdToTenantClaim", true);
        if (!mapAzureTenant)
        {
            return;
        }

        options.Events = new JwtBearerEvents
        {
            OnTokenValidated = context =>
            {
                var principal = context.Principal;
                if (principal?.Identity is not ClaimsIdentity identity)
                {
                    return Task.CompletedTask;
                }

                if (identity.FindFirst("tenant_id") is not null)
                {
                    return Task.CompletedTask;
                }

                var tid = principal.FindFirst("tid")?.Value
                    ?? principal.FindFirst("http://schemas.microsoft.com/identity/claims/tenantid")?.Value;
                if (!string.IsNullOrWhiteSpace(tid))
                {
                    identity.AddClaim(new Claim("tenant_id", tid));
                }

                return Task.CompletedTask;
            }
        };
    }
}
