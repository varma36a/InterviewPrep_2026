using Microsoft.EntityFrameworkCore;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Application.Abstractions.Persistence;

public interface IApplicationDbContext
{
    DbSet<Tenant> Tenants { get; }
    DbSet<User> Users { get; }
    DbSet<UserRole> UserRoles { get; }
    DbSet<TaxProfile> TaxProfiles { get; }
    DbSet<TaxDocument> TaxDocuments { get; }
    DbSet<TaxComputation> TaxComputations { get; }
    DbSet<RefreshToken> RefreshTokens { get; }
    DbSet<AuditLog> AuditLogs { get; }
    Task<int> SaveChangesAsync(CancellationToken cancellationToken = default);
}
