import { Component, Input, OnInit } from '@angular/core';
import { Category } from '../category';
import { Item } from '../item';
import items from '../items.json';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css'],
})
export class ProductListComponent implements OnInit {
  @Input() declare category: Category;
  items: Item[];
  constructor() {
    this.items = (items as any[]).map((item) => new Item(item));
  }

  ngOnInit(): void {}

  getItems(): Item[] {
    return this.items.filter((item) => item.categoryId === this.category.id);
  }

  onItemRemove(item: Item): void {
    this.items = this.items.filter((x) => x !== item);
  }
}
