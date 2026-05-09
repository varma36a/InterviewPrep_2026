export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  accessToken?: string;
  refreshToken?: string;
  expiresAtUtc?: string;
  tokenType?: string;
  [key: string]: unknown;
}

export interface RegisterTenantRequest {
  tenantName: string;
  adminEmail: string;
  adminPassword: string;
  countryCode: string;
}

export interface TaxProfilesQuery {
  cursor?: string;
  limit?: number;
}

export interface SalesOrdersQuery {
  cursor?: string;
  limit?: number;
}
