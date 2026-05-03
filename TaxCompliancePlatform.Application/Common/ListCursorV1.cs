using System.Text;
using System.Text.Json;

namespace TaxCompliancePlatform.Application.Common;

/// <summary>
/// Opaque cursor for keyset pagination ordered by <see cref="DateTime"/> (UTC) then <see cref="Guid"/> descending.
/// </summary>
public static class ListCursorV1
{
    private const string Version = "1";

    private sealed record Payload(string V, DateTime C, Guid I);

    public static string Encode(DateTime createdAtUtc, Guid id)
    {
        var json = JsonSerializer.Serialize(new Payload(Version, createdAtUtc, id));
        return Convert.ToBase64String(Encoding.UTF8.GetBytes(json));
    }

    /// <summary>Decodes a cursor from a previous response. Returns false if missing or invalid.</summary>
    public static bool TryDecode(string? cursor, out DateTime createdAtUtc, out Guid id)
    {
        createdAtUtc = default;
        id = default;
        if (string.IsNullOrWhiteSpace(cursor))
        {
            return false;
        }

        try
        {
            var padded = PadBase64(cursor.Trim());
            var json = Encoding.UTF8.GetString(Convert.FromBase64String(padded));
            var payload = JsonSerializer.Deserialize<Payload>(json);
            if (payload is null || payload.V != Version)
            {
                return false;
            }

            createdAtUtc = payload.C;
            id = payload.I;
            return true;
        }
        catch
        {
            return false;
        }
    }

    private static string PadBase64(string s)
    {
        var mod = s.Length % 4;
        return mod switch
        {
            0 => s,
            2 => s + "==",
            3 => s + "=",
            _ => s
        };
    }
}
