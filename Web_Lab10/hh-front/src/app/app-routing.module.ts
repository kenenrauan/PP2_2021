import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {CompanyComponent} from "./company/company.component";
import {CompanyDetailComponent} from "./company-detail/company-detail.component";
import {VacancyService} from "./services/vacancy.service";
import {VacancyDetailComponent} from "./vacancy-detail/vacancy-detail.component";
import {VacancyComponent} from "./vacancy/vacancy.component";

const routes: Routes = [
  {path: 'comp', component: CompanyComponent},
  {path: 'comp/:id', component: CompanyDetailComponent},
  {path: 'vacancies', component: VacancyComponent},
  {path: 'vacancies/:id', component: VacancyDetailComponent},
  {path: '', redirectTo: 'comp', pathMatch: 'full'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
