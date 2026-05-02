# Tax Compliance Platform (.NET 8)

Production-grade, multi-tenant Tax & Compliance Management Platform scaffold using Clean Architecture.

## Solution Structure

- `TaxCompliancePlatform.API`: HTTP API, middleware pipeline, authN/authZ, versioning, Swagger, health checks
- `TaxCompliancePlatform.Application`: CQRS (MediatR), validators, use-case orchestration, interfaces
- `TaxCompliancePlatform.Domain`: Entities, enums, and core business models
- `TaxCompliancePlatform.Infrastructure`: EF Core, SQL Server integration, repositories/UoW, JWT, Redis, background jobs
- `TaxCompliancePlatform.Shared`: shared response contracts
- `TaxCompliancePlatform.UnitTests`: validator and domain-focused tests
- `TaxCompliancePlatform.IntegrationTests`: API integration tests

## Implemented Foundations

- Multi-tenant model with tenant isolation metadata (`TenantId` everywhere)
- Tenant registration + onboarding flow
- JWT + refresh token primitives
- RBAC roles (`SuperAdmin`, `TenantAdmin`, `FinanceManager`, `Employee`)
- Policy-based authorization (`TenantScopePolicy`)
- Custom middleware:
  - Correlation ID
  - Global exception handling
  - Request logging
  - Tenant resolution
  - Secure headers
- CQRS with MediatR:
  - `RegisterTenantCommand`
  - `LoginCommand`
  - `CreateTaxProfileCommand`
  - `GetTaxProfilesQuery` with pagination
- FluentValidation for core commands
- EF Core SQL Server with indexing strategy for tenancy and reporting access paths
- Repository + Unit of Work
- Redis caching registration
- Serilog structured logging
- API versioning + Swagger + health checks + rate limiting
- Docker + Docker Compose bootstrap

## Step-by-Step Implementation Path

1. **Scaffold solution** and enforce project reference direction (`API -> Application/Infrastructure`, `Infrastructure -> Application/Domain`).
2. **Model domain** entities with explicit `TenantId` to guarantee tenant-aware data contracts.
3. **Define application abstractions** for auth, persistence, and tenant context.
4. **Implement CQRS handlers** for tenant onboarding, login, and tax profile operations.
5. **Add infrastructure** (`ApplicationDbContext`, generic repositories, JWT service, Redis, hosted jobs).
6. **Wire API bootstrap** with middleware chain, versioning, authorization, health checks, and Swagger.
7. **Containerize** with `Dockerfile` + `docker-compose.yml`.
8. **Harden for production**:
   - secret manager or Key Vault for JWT/connection strings
   - database migrations + CI policy checks
   - distributed tracing and centralized audit query APIs

## Run Locally

```bash
dotnet restore
dotnet build
dotnet test
dotnet run --project TaxCompliancePlatform.API
```

Or run containers:

```bash
docker compose up --build
```

## Architecture Decisions (Interview View)

- **Clean Architecture**: enforces dependency rule, keeps domain/business logic framework-agnostic.
- **CQRS + MediatR**: isolates use-cases and simplifies testing/extensibility for enterprise workflows.
- **Repository/UoW**: explicit transaction boundaries and test seams over EF Core while preserving LINQ flexibility.
- **Tenant header + token claim**: balances onboarding flexibility with strict per-request tenant context.
- **Middleware-first cross-cutting concerns**: centralized logging/correlation/error handling keeps controllers lean.
- **Versioned APIs from day one**: avoids contract drift and enables non-breaking enterprise rollout.

## Security Checklist (Bootstrap)

- HTTPS redirection enabled
- JWT bearer authentication configured
- Secure response headers middleware
- Parameterized queries via EF Core (SQL injection prevention)
- Correlation IDs for forensic traceability
- Config-driven secrets ready to move into secure secret stores