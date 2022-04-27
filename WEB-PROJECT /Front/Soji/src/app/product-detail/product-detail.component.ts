import { Component, OnInit, Input} from '@angular/core';
import { Product} from '../product';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { CartService} from '../cart.service';
import { ProductService} from '../product.service';



@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit {
  product: Product;

  constructor(private route: ActivatedRoute,
              private productService: ProductService,
              private location: Location,
              private cartService: CartService
) { }
  ngOnInit(): void {
    this.getProduct();
  }

  getProduct(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProduct(id)
      .subscribe(product => this.product = product);
  }
  goBack(): void {
    this.location.back();
  }
  addToCart(product): void {
    this.cartService.addToCart(product);
}
}
