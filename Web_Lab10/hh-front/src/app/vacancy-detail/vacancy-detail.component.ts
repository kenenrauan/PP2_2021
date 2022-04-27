import { Component, OnInit } from '@angular/core';
import {Company, Vacancy} from "../models";
import {ActivatedRoute, Params, Router} from "@angular/router";
import {CompanyService} from "../services/company.service";
import {VacancyService} from "../services/vacancy.service";

@Component({
  selector: 'app-vacancy-detail',
  templateUrl: './vacancy-detail.component.html',
  styleUrls: ['./vacancy-detail.component.css']
})
export class VacancyDetailComponent implements OnInit {


  vacancy: Vacancy | undefined = undefined
  loaded: boolean = false
  constructor(private route: ActivatedRoute,
              private service: VacancyService,
              private router: Router) { }

  ngOnInit(): void {
    this.getVacancy()
  }

  getVacancy(){
    this.route.params.subscribe( (params: Params)=>{
        this.loaded = true
        this.service.getVacancy(+params['id']).subscribe(data =>{

          this.vacancy = data
        })
      }
    )
  }

}
