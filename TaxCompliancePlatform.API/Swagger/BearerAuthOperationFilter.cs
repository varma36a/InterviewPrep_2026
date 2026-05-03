using System.Reflection;
using Microsoft.AspNetCore.Authorization;
using Microsoft.OpenApi;
using Swashbuckle.AspNetCore.SwaggerGen;

namespace TaxCompliancePlatform.API.Swagger;

/// <summary>
/// Applies the Bearer security requirement only to endpoints that require authorization,
/// so Swagger does not prompt for an access token for login, register, or other anonymous APIs.
/// </summary>
public sealed class BearerAuthOperationFilter : IOperationFilter
{
    public void Apply(OpenApiOperation operation, OperationFilterContext context)
    {
        var methodInfo = context.MethodInfo;
        if (methodInfo is null)
        {
            return;
        }

        if (methodInfo.GetCustomAttribute<AllowAnonymousAttribute>(inherit: true) is not null)
        {
            return;
        }

        var declaringType = methodInfo.DeclaringType;
        if (declaringType?.GetCustomAttribute<AllowAnonymousAttribute>(inherit: true) is not null)
        {
            return;
        }

        var requiresAuth =
            methodInfo.GetCustomAttribute<AuthorizeAttribute>(inherit: true) is not null
            || declaringType?.GetCustomAttribute<AuthorizeAttribute>(inherit: true) is not null;

        if (!requiresAuth)
        {
            return;
        }

        operation.Security ??= new List<OpenApiSecurityRequirement>();
        operation.Security.Add(new OpenApiSecurityRequirement
        {
            [new OpenApiSecuritySchemeReference("Bearer", context.Document, string.Empty)] = []
        });
    }
}
