namespace TaxCompliancePlatform.Application.Strategy.Security;

/// <summary>
/// Pluggable password hashing strategy (implementation lives in Infrastructure).
/// </summary>
public interface IPasswordHasher
{
    string Hash(string password);
    bool Verify(string password, string passwordHash);
}
