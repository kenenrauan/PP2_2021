import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {ReactiveFormsModule} from '@angular/forms';
import {FormsModule} from '@angular/forms';
import { AppRoutingModule} from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductsComponent } from './products/products.component';
import { MainComponent } from './main/main.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { HttpClientModule } from '@angular/common/http';
import { ProductDetailComponent } from './product-detail/product-detail.component';
import { FeaturedprodComponent } from './featuredprod/featuredprod.component';
import { ProductSearchComponent } from './product-search/product-search.component';
import { CartComponent } from './cart/cart.component';
import { DeliveryComponent } from './delivery/delivery.component';
import { ServiceComponent } from './service/service.component';
import { ReviewsComponent } from './reviews/reviews.component';
import { LoginComponent } from './login/login.component';
import { AccountComponent } from './account/account.component';
import {HTTP_INTERCEPTORS} from '@angular/common/http';
import {AuthInterceptor} from './auth.interceptor';
import { ViewOrderComponent } from './viewOrder/viewOrder.component';

@NgModule({
   declarations: [
      AppComponent,
      ProductsComponent,
      MainComponent,
      TopBarComponent,
      ProductDetailComponent,
      FeaturedprodComponent,
      ProductSearchComponent,
      CartComponent,
      DeliveryComponent,
      ServiceComponent,
      ReviewsComponent,
      LoginComponent,
      AccountComponent,
      ViewOrderComponent
   ],
   imports: [
      FormsModule,
      BrowserModule,
      AppRoutingModule,
      HttpClientModule,
      ReactiveFormsModule
   ],
   providers: [
   ],
   bootstrap: [
      AppComponent
   ]
})
export class AppModule { }
