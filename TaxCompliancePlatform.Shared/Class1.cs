namespace TaxCompliancePlatform.Shared;

public sealed record ApiResponse<T>(bool Success, T? Data, string? Error = null);
