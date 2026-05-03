using MediatR;
using TaxCompliancePlatform.Application.Handlers.Auth.Common;

namespace TaxCompliancePlatform.Application.Handlers.Auth.Login;

public sealed record LoginCommand(string Email, string Password) : IRequest<AuthResponse>;
