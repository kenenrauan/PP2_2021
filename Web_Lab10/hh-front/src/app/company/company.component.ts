import { Component, OnInit } from '@angular/core';
import {Company} from "../models";
import {CompanyService} from "../services/company.service";

@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent implements OnInit {
  companies: Company[] = []
  constructor(private service: CompanyService) { }

  ngOnInit(): void {
    this.getCompanies()
  }

  getCompanies(){
    this.service.getCompanies().subscribe(data =>{
      this.companies = data
    })
  }

}
