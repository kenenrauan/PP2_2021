import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {AuthToken, Company} from "../models";
import {HttpClient, HttpClientModule} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class CompanyService {

  BASE_URl = 'http://localhost:8000';
  constructor(private http: HttpClient) { }

  getCompanies(): Observable<Company[]>{
    return this.http.get<Company[]>(`${this.BASE_URl}/api/companies`);
  }
  login(username: String, password: String): Observable<AuthToken> {
    return this.http.post<AuthToken>(`${this.BASE_URl}/api/login/`, {
      username,
      password
    });
  }

  getCompany(id: number) {
    return this.http.get<Company>(`${this.BASE_URl}/api/companies/${id}`);
  }
}
