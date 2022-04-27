import {Component, OnInit} from '@angular/core';
import {CompanyService} from "./services/company.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})




export class AppComponent implements OnInit {
  title = 'demo-front';
  logged = false;
  username = '';
  password = '';

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }

  constructor(private categoryService: CompanyService) {
  }

  login() {
    this.categoryService.login(this.username, this.password).subscribe((data) => {
    console.log(data)
      // @ts-ignore
      localStorage.setItem('token', data.access);

      this.logged = true;
      this.username = '';
      this.password = '';
    });
  }

  logout() {
    this.logged = false;
    localStorage.removeItem('token');
  }
}
