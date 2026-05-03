using Asp.Versioning;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Mvc.Authorization;
using Microsoft.AspNetCore.RateLimiting;
using Microsoft.IdentityModel.Tokens;
using Microsoft.OpenApi;
using Serilog;
using System.Text;
using TaxCompliancePlatform.API.Correlation;
using TaxCompliancePlatform.API.Hosting;
using TaxCompliancePlatform.API.Middleware;
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
builder.Services.AddSwaggerGen(options =>
{
    options.SwaggerDoc("v1", new OpenApiInfo { Title = "Tax Compliance Platform API", Version = "v1" });
    if (authorizationEnabled)
    {
        options.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
        {
            Name = "Authorization",
            Type = SecuritySchemeType.Http,
            Scheme = "Bearer",
            BearerFormat = "JWT",
            In = ParameterLocation.Header,
            Description = "Paste the accessToken from POST /api/v1/auth/login (Swagger sends it as Bearer automatically)."
        });
        options.AddSecurityRequirement(document => new OpenApiSecurityRequirement
        {
            [new OpenApiSecuritySchemeReference("Bearer", document, string.Empty)] = []
        });
    }
});

// Policies for [Authorize] when the authorization middleware is enabled below.
builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("TenantScopePolicy", policy => policy.RequireClaim("tenant_id"));
});

// Register JWT schemes in DI regardless of Authorization:Enabled so ChallengeAsync never hits a missing DefaultChallengeScheme
// if anything in the pipeline still invokes authentication (ordering, hosting, or future middleware).
// Only UseAuthentication/UseAuthorization are toggled by Authorization:Enabled.
var jwtKey = builder.Configuration["Jwt:Key"] ?? throw new InvalidOperationException("JWT key is not configured.");
var bearerScheme = JwtBearerDefaults.AuthenticationScheme;
builder.Services.AddAuthentication(options =>
    {
        options.DefaultAuthenticateScheme = bearerScheme;
        options.DefaultChallengeScheme = bearerScheme;
        options.DefaultForbidScheme = bearerScheme;
    })
    .AddJwtBearer(bearerScheme, options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateIssuerSigningKey = true,
            ValidateLifetime = true,
            ValidIssuer = builder.Configuration["Jwt:Issuer"],
            ValidAudience = builder.Configuration["Jwt:Audience"],
            IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(jwtKey))
        };
    });

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
    "Authorization:Enabled computed={Computed} (Authorization:Enabled raw '{Raw}'. When true, protected routes need Bearer token from POST /api/v1/auth/login.)",
    authorizationEnabled,
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
