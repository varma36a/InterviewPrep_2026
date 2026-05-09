namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class VisitorPattern
{
    internal static void Run()
    {
        IAsset[] assets = [new ServerAsset("api-1"), new DatabaseAsset("tax-db")];
        var securityVisitor = new SecurityAuditVisitor();
        foreach (var asset in assets) asset.Accept(securityVisitor);
    }
}

internal interface IAssetVisitor { void Visit(ServerAsset server); void Visit(DatabaseAsset database); }
internal interface IAsset { void Accept(IAssetVisitor visitor); }
internal sealed class ServerAsset(string host) : IAsset
{
    internal string Host { get; } = host;
    public void Accept(IAssetVisitor visitor) => visitor.Visit(this);
}
internal sealed class DatabaseAsset(string name) : IAsset
{
    internal string Name { get; } = name;
    public void Accept(IAssetVisitor visitor) => visitor.Visit(this);
}
internal sealed class SecurityAuditVisitor : IAssetVisitor
{
    public void Visit(ServerAsset server) => Console.WriteLine($"Visitor -> Audited server {server.Host}");
    public void Visit(DatabaseAsset database) => Console.WriteLine($"Visitor -> Audited database {database.Name}");
}
