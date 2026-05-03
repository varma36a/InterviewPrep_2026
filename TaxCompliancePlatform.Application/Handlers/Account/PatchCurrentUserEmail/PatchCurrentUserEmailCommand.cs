using MediatR;

namespace TaxCompliancePlatform.Application.Handlers.Account.PatchCurrentUserEmail;

/// <summary>
/// Partial update: only the email address changes; other user fields are untouched.
/// </summary>
public sealed record PatchCurrentUserEmailCommand(string Email) : IRequest;
