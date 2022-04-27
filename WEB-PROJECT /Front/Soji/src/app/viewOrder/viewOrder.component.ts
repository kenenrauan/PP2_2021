import { Order } from './../order';
import { CartService } from './../cart.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-viewOrder',
  templateUrl: './viewOrder.component.html',
  styleUrls: ['./viewOrder.component.css']
})
export class ViewOrderComponent implements OnInit {

  orders: Order[] = [];

  constructor(private cartService: CartService,
    private route: ActivatedRoute,
    private location: Location) { }

  ngOnInit() {
    this.getMyOrders();
  }

  getMyOrders(){
    const id = parseInt(localStorage.getItem('userId'));
    this.cartService.getOrdersById(id).subscribe(orders => this.orders = orders);
  }

  deleteOrder(id){
    this.cartService.deleteOrder(id).subscribe();
    window.alert('You order is removed');
  }

}
