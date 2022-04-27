import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Params, Router} from "@angular/router";
import {CompanyService} from "../services/company.service";
import {Company} from "../models";

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {

  company: Company |undefined = undefined
  loaded: boolean = false
  constructor(private route: ActivatedRoute,
              private service: CompanyService,
              private router: Router) { }

  ngOnInit(): void {
    this.getCompany()
  }

  getCompany(){
    this.route.params.subscribe( (params: Params)=>{
        this.loaded = true
        this.service.getCompany(+params['id']).subscribe(data =>{

          this.company = data
        })
      }
    )
  }


}
