import { Component, OnInit } from '@angular/core';
import {ProductService} from '../product.service';

@Component({
  selector: 'app-top-bar',
  templateUrl: './top-bar.component.html',
  styleUrls: ['./top-bar.component.css']
})
export class TopBarComponent implements OnInit {
  logged = false;
  userName: string;
  constructor(private productService: ProductService) { }
  current = 'Log in'

  ngOnInit(): void {
    this.getUsername()
  }
  getUsername(): void{
    this.userName = localStorage.getItem('username');
   if(this.userName){
     this.logged = true;
     this.current = this.userName;
   }
   else {
     this.logged = false;
     this.current = 'Log in';

   }
  }

}
