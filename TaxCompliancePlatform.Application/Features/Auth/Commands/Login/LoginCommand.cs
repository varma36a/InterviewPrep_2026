using MediatR;
using TaxCompliancePlatform.Application.Features.Auth.Common;

namespace TaxCompliancePlatform.Application.Features.Auth.Commands.Login;

public sealed record LoginCommand(string Email, string Password) : IRequest<AuthResponse>;
