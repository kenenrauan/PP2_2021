import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { VacancyComponent } from './vacancy/vacancy.component';
import { CompanyComponent } from './company/company.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import {FormsModule} from "@angular/forms";
import {AuthInterceptor} from "./AuthInterceptor";
import { CompanyDetailComponent } from './company-detail/company-detail.component';
import { VacancyDetailComponent } from './vacancy-detail/vacancy-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    VacancyComponent,
    CompanyComponent,
    CompanyDetailComponent,
    VacancyDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass:  AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
