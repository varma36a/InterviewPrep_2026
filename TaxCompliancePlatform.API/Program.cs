using Asp.Versioning;
using Microsoft.AspNetCore.Mvc.Authorization;
using Microsoft.AspNetCore.RateLimiting;
using Microsoft.OpenApi;
using Serilog;
using TaxCompliancePlatform.API.Correlation;
using TaxCompliancePlatform.API.Hosting;
using TaxCompliancePlatform.API.Middleware;
using TaxCompliancePlatform.API.Swagger;
using TaxCompliancePlatform.Application;
using TaxCompliancePlatform.Application.Providers.Correlation;
using TaxCompliancePlatform.Infrastructure;

var builder = WebApplication.CreateBuilder(args);

bool AuthorizationEnabled(IConfiguration cfg) =>
    bool.TryParse(cfg["Authorization:Enabled"], out var enabled) && enabled;

var authorizationEnabled = AuthorizationEnabled(builder.Configuration);

builder.Host.UseSerilog((context, loggerConfiguration) =>
{
    loggerConfiguration
        .ReadFrom.Configuration(context.Configuration)
        .Enrich.FromLogContext()
        .WriteTo.Console();
});

builder.Services.AddHttpContextAccessor();
builder.Services.AddScoped<ICorrelationContext, HttpCorrelationContext>();
builder.Services.AddApplication();
builder.Services.AddInfrastructure(builder.Configuration);
if (builder.Environment.IsDevelopment())
{
    builder.Services.AddHostedService<DevelopmentTenantBootstrapper>();
}

builder.Services.AddControllers(options =>
{
    if (!authorizationEnabled)
    {
        options.Filters.Add(new AllowAnonymousFilter());
    }
});
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddApiVersioning(options =>
    {
        options.DefaultApiVersion = new ApiVersion(1, 0);
        options.AssumeDefaultVersionWhenUnspecified = true;
        options.ReportApiVersions = true;
    })
    .AddApiExplorer(options =>
    {
        options.GroupNameFormat = "'v'VVV";
        options.SubstituteApiVersionInUrl = true;
    });
var oauth2Enabled = builder.Configuration.GetValue("OAuth2:Enabled", false);
builder.Services.AddSwaggerGen(options =>
{
    options.SwaggerDoc("v1", new OpenApiInfo { Title = "Tax Compliance Platform API", Version = "v1" });
    if (authorizationEnabled)
    {
        var bearerDescription = oauth2Enabled
            ? "Only required on endpoints that use [Authorize]. Get a first-party JWT from POST /api/v1/auth/login, or use an OAuth 2.0 / OIDC access token from your configured authority. Paste the token only (Swagger adds Bearer)."
            : "Only required on endpoints that use [Authorize]. Call POST /api/v1/auth/login first, then paste the accessToken value here (Swagger adds Bearer).";
        options.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
        {
            Name = "Authorization",
            Type = SecuritySchemeType.Http,
            Scheme = "Bearer",
            BearerFormat = "JWT",
            In = ParameterLocation.Header,
            Description = bearerDescription
        });
        options.OperationFilter<BearerAuthOperationFilter>();
    }
});

// Policies for [Authorize] when the authorization middleware is enabled below.
builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("TenantScopePolicy", policy => policy.RequireClaim("tenant_id"));
});

// Register JWT / OAuth2 schemes regardless of Authorization:Enabled so ChallengeAsync never hits a missing scheme.
// Only UseAuthentication/UseAuthorization are toggled by Authorization:Enabled.
builder.Services.AddPlatformAuthentication(builder.Configuration);

builder.Services.AddHealthChecks();
builder.Services.AddRateLimiter(options =>
{
    options.AddFixedWindowLimiter("api", limiter =>
    {
        limiter.PermitLimit = 100;
        limiter.Window = TimeSpan.FromMinutes(1);
        limiter.QueueLimit = 0;
    });
});

var app = builder.Build();

// If you see 401 + WWW-Authenticate: Bearer but appsettings shows false, env may override (Authorization__Enabled).
app.Logger.LogInformation(
    "Authorization:Enabled={AuthorizationEnabled} OAuth2:Enabled={OAuth2Enabled} (Authorization:Enabled raw '{AuthorizationRaw}'. When authorization is on, use first-party JWT from POST /api/v1/auth/login or an external OAuth2/OIDC access token when OAuth2:Enabled is true.)",
    authorizationEnabled,
    oauth2Enabled,
    app.Configuration["Authorization:Enabled"] ?? "<missing>");

app.UseMiddleware<CorrelationIdMiddleware>();
app.UseMiddleware<ExceptionHandlingMiddleware>();
app.UseMiddleware<RequestLoggingMiddleware>();
app.UseMiddleware<SecureHeadersMiddleware>();
app.UseMiddleware<TenantResolutionMiddleware>();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseRateLimiter();
if (authorizationEnabled)
{
    app.UseAuthentication();
    app.UseAuthorization();
}

app.MapHealthChecks("/health");
app.MapControllers().RequireRateLimiting("api");

app.Run();

public partial class Program;
