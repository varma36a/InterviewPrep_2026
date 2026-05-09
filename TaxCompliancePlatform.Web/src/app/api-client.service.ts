import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '../environments/environment';
import { LoginRequest, LoginResponse, RegisterTenantRequest, SalesOrdersQuery, TaxProfilesQuery } from './api.models';

@Injectable({
  providedIn: 'root'
})
export class ApiClientService {
  private readonly baseUrl = environment.apiBaseUrl;

  constructor(private readonly http: HttpClient) {}

  registerTenant(payload: RegisterTenantRequest): Observable<unknown> {
    return this.http.post(`${this.baseUrl}/auth/tenants/register`, payload);
  }

  login(payload: LoginRequest): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.baseUrl}/auth/login`, payload);
  }

  patchEmail(email: string, bearerToken: string): Observable<void> {
    return this.http.patch<void>(
      `${this.baseUrl}/account/email`,
      { email },
      { headers: this.authHeaders(bearerToken) }
    );
  }

  getTaxProfiles(query: TaxProfilesQuery = {}, bearerToken?: string): Observable<unknown> {
    let params = new HttpParams();
    if (query.cursor) {
      params = params.set('cursor', query.cursor);
    }
    if (query.limit) {
      params = params.set('limit', query.limit);
    }

    return this.http.get(`${this.baseUrl}/tax-profiles`, {
      params,
      headers: bearerToken ? this.authHeaders(bearerToken) : undefined
    });
  }

  createTaxProfile(payload: any, bearerToken?: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/tax-profiles`, payload, {
      headers: bearerToken ? this.authHeaders(bearerToken) : undefined
    });
  }

  listSalesOrders(query: SalesOrdersQuery = {}, bearerToken?: string): Observable<unknown> {
    let params = new HttpParams();
    if (query.cursor) {
      params = params.set('cursor', query.cursor);
    }
    if (query.limit) {
      params = params.set('limit', query.limit);
    }

    return this.http.get(`${this.baseUrl}/domino/franchise-tax/sales-orders`, {
      params,
      headers: bearerToken ? this.authHeaders(bearerToken) : undefined
    });
  }

  createSalesOrder(payload: unknown, bearerToken?: string): Observable<unknown> {
    return this.http.post(`${this.baseUrl}/domino/franchise-tax/sales-orders`, payload, {
      headers: bearerToken ? this.authHeaders(bearerToken) : undefined
    });
  }

  private authHeaders(bearerToken: string): HttpHeaders {
    return new HttpHeaders({
      Authorization: `Bearer ${bearerToken}`
    });
  }
}
