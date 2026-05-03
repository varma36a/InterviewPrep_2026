namespace TaxCompliancePlatform.Application.Common;

/// <summary>
/// Cursor-based page: pass <see cref="NextCursor"/> as the <c>cursor</c> query parameter on the next request when <see cref="HasMore"/> is true.
/// </summary>
public sealed record CursorPagedResponse<T>(IReadOnlyList<T> Items, string? NextCursor, bool HasMore);
