import { ViewOrderComponent } from './viewOrder/viewOrder.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductsComponent} from './products/products.component';
import { MainComponent} from './main/main.component';
import { RouterModule, Routes } from '@angular/router';
import { ProductDetailComponent} from './product-detail/product-detail.component';
import {CartComponent} from './cart/cart.component';
import {DeliveryComponent} from './delivery/delivery.component';
import {ServiceComponent} from './service/service.component';
import {ReviewsComponent} from './reviews/reviews.component';
import {LoginComponent} from './login/login.component';
import {AccountComponent} from './account/account.component';

const routes: Routes = [
  { path: 'products', component: ProductsComponent },
  { path: '', component: MainComponent},
  { path: 'detail/:id', component: ProductDetailComponent },
  {path: 'cart', component: CartComponent},
  {path: 'delivery', component: DeliveryComponent},
  {path: 'services', component: ServiceComponent},
  {path: 'reviews', component: ReviewsComponent},
  {path: 'signin', component: LoginComponent},
  {path: 'account', component: AccountComponent},
  {path: 'vieworders', component: ViewOrderComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
