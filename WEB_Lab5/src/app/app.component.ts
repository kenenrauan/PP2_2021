import { Component } from '@angular/core';
import categories from './categories.json'
import { Category } from './category'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'my-store';
  categories: Category[];
  selectedCategory: Category;

  constructor() {
    this.categories = categories;
    this.selectedCategory = categories[0];
  }

}