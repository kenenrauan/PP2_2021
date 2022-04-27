import { Component, OnInit } from '@angular/core';
import {Company, Vacancy} from "../models";
import {CompanyService} from "../services/company.service";
import {VacancyService} from "../services/vacancy.service";

@Component({
  selector: 'app-vacancy',
  templateUrl: './vacancy.component.html',
  styleUrls: ['./vacancy.component.css']
})
export class VacancyComponent implements OnInit {


  vacancies: Vacancy[] = []
  constructor(private service: VacancyService) { }

  ngOnInit(): void {
    this.getVacancies()
  }

  getVacancies(){
    this.service.getVacancies().subscribe(data =>{
      this.vacancies = data
    })
  }

}
