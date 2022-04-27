import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {Company, Vacancy} from "../models";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  BASE_URl = 'http://localhost:8000';
  constructor(private http: HttpClient) { }

  getVacancies(): Observable<Vacancy[]>{
    return this.http.get<Vacancy[]>(`${this.BASE_URl}/api/vacancies`);
  }
  getVacancy(id: number): Observable<Vacancy>{
    return this.http.get<Vacancy>(`${this.BASE_URl}/api/vacancies/${id}`);
  }
}
