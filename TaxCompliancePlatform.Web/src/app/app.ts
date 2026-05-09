import { Component, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { JsonPipe } from '@angular/common';
import { finalize } from 'rxjs';

import { ApiClientService } from './api-client.service';
import { LoginRequest, RegisterTenantRequest } from './api.models';

@Component({
  selector: 'app-root',
  imports: [FormsModule, JsonPipe],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = 'Tax Compliance Platform Frontend';
  protected readonly isLoading = signal(false);
  protected token = '';
  protected readonly lastResponse = signal<unknown>(null);
  protected readonly lastError = signal<string | null>(null);

  protected readonly registerTenantForm: RegisterTenantRequest = {
    tenantName: 'Contoso Tax LLC',
    adminEmail: 'admin@contoso.com',
    adminPassword: 'ChangeMe123!',
    countryCode: 'US'
  };

  protected readonly loginForm: LoginRequest = {
    email: 'admin@contoso.com',
    password: 'ChangeMe123!'
  };

  protected readonly patchEmailForm = {
    email: 'new-admin@contoso.com'
  };

  protected readonly taxProfile = {
  taxIdentifier: 'PAN1234567X',
  countryCode: 'US',
  annualTaxableIncome: 2250000,
  deductions: 1250000,
  fiscalYear: 2024
  };

  protected readonly salesOrder = {
    CustomerOrderReference: 'DOM-10021',
    PretaxAmount: 499.95
  };

  constructor(private readonly api: ApiClientService) {}

  protected registerTenant(): void {
    this.runRequest(this.api.registerTenant(this.registerTenantForm));
  }

  protected login(): void {
    this.runRequest(this.api.login(this.loginForm), (result) => {
      if (result && typeof result === 'object' && 'accessToken' in result) {
        const tokenValue = (result as { accessToken?: unknown }).accessToken;
        if (typeof tokenValue === 'string') {
          this.token = tokenValue;
        }
      }
    });
  }

  protected patchEmail(): void {
    this.runRequest(this.api.patchEmail(this.patchEmailForm.email, this.token.trim()));
  }

  protected getTaxProfiles(): void {
    this.runRequest(this.api.getTaxProfiles({ limit: 20 }, this.token.trim()));
  }

  protected createTaxProfile(): void {
    this.runRequest(this.api.createTaxProfile(this.taxProfile, this.token.trim()));
  }

  protected listSalesOrders(): void {
    this.runRequest(this.api.listSalesOrders({ limit: 20 }, this.token.trim()));
  }

  protected createSalesOrder(): void {
    this.runRequest(this.api.createSalesOrder(this.salesOrder, this.token.trim()));
  }

  private runRequest(
    request$: ReturnType<ApiClientService['registerTenant']>,
    onSuccess?: (result: unknown) => void
  ): void {
    this.isLoading.set(true);
    this.lastError.set(null);
    request$
      .pipe(finalize(() => this.isLoading.set(false)))
      .subscribe({
        next: (result) => {
          this.lastResponse.set(result ?? { status: 'success' });
          onSuccess?.(result);
        },
        error: (error) => {
          const message = typeof error?.message === 'string' ? error.message : 'Request failed.';
          this.lastError.set(message);
          this.lastResponse.set(error?.error ?? null);
        }
      });
  }
}
