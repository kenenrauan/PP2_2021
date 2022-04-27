import { Component, OnInit } from '@angular/core';
import {Product} from '../product';
import {ProductService} from '../product.service';

@Component({
  selector: 'app-featuredprod',
  templateUrl: './featuredprod.component.html',
  styleUrls: ['./featuredprod.component.css']
})
export class FeaturedprodComponent implements OnInit {
  products: Product[] = [];

  constructor(private productService: ProductService) { }

  ngOnInit(): void {
  this.getProducts();
  }
  getProducts(): void {
    this.productService.getProducts().subscribe(products => this.products = products.slice(0, 5));
  }
}
