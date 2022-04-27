import {Component, Input, OnInit} from '@angular/core';
import {User} from '../user';
import { AccountService} from '../account.service';
import {Product} from '../product';
import {Order} from '../order';
import {ReviewsService} from '../reviews.service';
import  {ProductService} from '../product.service'; 
import {Location} from '@angular/common'

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent implements OnInit {
 
  confirmPassword;
  usera;
  constructor(private productService: ProductService, private location: Location ) { }

  ngOnInit(): void {
    this.usera = {
      username:'',
      password:''
  }
  this.confirmPassword='';
  }
  register(){
    if(this.confirmPassword==this.usera.password){
      this.productService.registerNewUser(this.usera.username,this.usera.password).subscribe(
        responce=>{
          alert('User '+this.usera.username+' has been created')
          this.location.back();
        },
        error => alert('User name exists')
    );
    }
    else
    alert('Passwords are not same');
  }
}

