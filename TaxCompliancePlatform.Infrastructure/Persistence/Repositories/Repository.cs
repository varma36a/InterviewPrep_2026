using Microsoft.EntityFrameworkCore;
using TaxCompliancePlatform.Application.Abstractions.Persistence;
using TaxCompliancePlatform.Domain.Common;

namespace TaxCompliancePlatform.Infrastructure.Persistence.Repositories;

public sealed class Repository<T>(ApplicationDbContext dbContext) : IRepository<T> where T : BaseEntity
{
    public Task<T?> GetByIdAsync(Guid id, CancellationToken cancellationToken = default)
        => dbContext.Set<T>().FirstOrDefaultAsync(x => x.Id == id, cancellationToken);

    public IQueryable<T> Query() => dbContext.Set<T>().AsQueryable();

    public Task AddAsync(T entity, CancellationToken cancellationToken = default)
        => dbContext.Set<T>().AddAsync(entity, cancellationToken).AsTask();

    public void Update(T entity) => dbContext.Set<T>().Update(entity);

    public void Remove(T entity) => dbContext.Set<T>().Remove(entity);
}
