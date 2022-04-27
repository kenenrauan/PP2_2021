import { Component, OnInit } from '@angular/core';
import {ProductService} from '../product.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  title = 'servicesGroup2';
  constructor(private productService: ProductService ) { }

  storedLogin:string;
  logged = false;

  username = '';
  password = '';


  ngOnInit(){
    let token = localStorage.getItem('token');
    if (token){
      this.logged = true;
      this.storedLogin = localStorage.getItem('username');
    }
  }

  login(){
    this.productService.login(this.username, this.password)
      .subscribe(res => {
        localStorage.setItem('token', res.token);
        this.productService.getUserId(this.username).subscribe(id=>
          {
            localStorage.setItem('userId', id.id.toString());
            localStorage.setItem('username',this.username);
          }
          );
        this.logged = true;

        this.username = '';
        this.password = '';
      })
  }

  logout(){
      localStorage.clear();
    this.logged = false;
  }
}
