import { Component, OnInit } from '@angular/core';
import {CartService} from '../cart.service';
import {Product} from '../product';
import { FormBuilder } from '@angular/forms';
import {Order} from '../order';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {
  items: Product[] = [];
  productId: number[] = [];
  note: string;

  constructor( private cartService: CartService) {}

  ngOnInit(): void {
    this.items = this.cartService.getItems();
  }

  getProductIdes(): number[]{
    for (let i in this.items){
      this.productId.push(this.items[i].id);
    }
    return this.productId;
  }

  onSubmit(note: string) {
    let check = localStorage.getItem('token');
    if(check != null){
        console.log(this.getProductIdes());
        this.cartService.createOrder(parseInt(localStorage.getItem('userId')), this.getProductIdes(), note).subscribe();
        alert('You order is received');
        this.items.length = 0;
    }
    else{
      window.alert('Make a authorization');
    }
  }
}
