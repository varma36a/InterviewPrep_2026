using Microsoft.EntityFrameworkCore;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Domain.Entities;

namespace TaxCompliancePlatform.Infrastructure.Persistence;

public sealed class ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : DbContext(options), IApplicationDbContext, IUnitOfWork
{
    public DbSet<Tenant> Tenants => Set<Tenant>();
    public DbSet<User> Users => Set<User>();
    public DbSet<UserRole> UserRoles => Set<UserRole>();
    public DbSet<TaxProfile> TaxProfiles => Set<TaxProfile>();
    public DbSet<TaxDocument> TaxDocuments => Set<TaxDocument>();
    public DbSet<TaxComputation> TaxComputations => Set<TaxComputation>();
    public DbSet<RefreshToken> RefreshTokens => Set<RefreshToken>();
    public DbSet<AuditLog> AuditLogs => Set<AuditLog>();
    public DbSet<DominoFranchiseSalesOrder> DominoFranchiseSalesOrders => Set<DominoFranchiseSalesOrder>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        modelBuilder.Entity<Tenant>(builder =>
        {
            builder.HasIndex(x => x.Slug).IsUnique();
            builder.Property(x => x.Name).HasMaxLength(150).IsRequired();
            builder.Property(x => x.Slug).HasMaxLength(80).IsRequired();
            builder.Property(x => x.ContactEmail).HasMaxLength(150).IsRequired();
        });

        modelBuilder.Entity<User>(builder =>
        {
            builder.HasIndex(x => new { x.TenantId, x.Email }).IsUnique();
            builder.Property(x => x.Email).HasMaxLength(150).IsRequired();
            builder.Property(x => x.FullName).HasMaxLength(120).IsRequired();
        });

        modelBuilder.Entity<UserRole>(builder =>
        {
            builder.HasIndex(x => new { x.UserId, x.RoleName }).IsUnique();
            builder.Property(x => x.RoleName).HasMaxLength(64).IsRequired();
        });

        modelBuilder.Entity<TaxProfile>(builder =>
        {
            builder.HasIndex(x => new { x.TenantId, x.TaxIdentifier, x.FiscalYear }).IsUnique();
            builder.Property(x => x.TaxIdentifier).HasMaxLength(50).IsRequired();
            builder.Property(x => x.CountryCode).HasMaxLength(2).IsRequired();
        });

        modelBuilder.Entity<TaxComputation>(builder =>
        {
            builder.HasIndex(x => new { x.TenantId, x.TaxProfileId, x.ComputedAtUtc });
        });

        modelBuilder.Entity<RefreshToken>(builder =>
        {
            builder.HasIndex(x => x.Token).IsUnique();
            builder.Property(x => x.Token).HasMaxLength(128).IsRequired();
            builder.HasIndex(x => new { x.UserId, x.ExpiresAtUtc });
        });

        modelBuilder.Entity<AuditLog>(builder =>
        {
            builder.Property(x => x.Action).HasMaxLength(100).IsRequired();
            builder.Property(x => x.Resource).HasMaxLength(200).IsRequired();
            builder.Property(x => x.CorrelationId).HasMaxLength(64).IsRequired();
            builder.HasIndex(x => new { x.TenantId, x.CreatedAtUtc });
        });

        modelBuilder.Entity<DominoFranchiseSalesOrder>(builder =>
        {
            builder.HasIndex(x => new { x.TenantId, x.StoreCode, x.CreatedAtUtc });
            builder.Property(x => x.StoreCode).HasMaxLength(32).IsRequired();
            builder.Property(x => x.MarketRegion).HasMaxLength(64).IsRequired();
            builder.Property(x => x.CustomerOrderReference).HasMaxLength(40).IsRequired();
            builder.Property(x => x.CorrelationId).HasMaxLength(64).IsRequired();
        });
    }
}
