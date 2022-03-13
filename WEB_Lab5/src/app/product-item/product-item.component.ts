import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';
import { Item } from '../item';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css'],
})
export class ProductItemComponent implements OnInit {
  @Input() declare item: Item;
  @Output() remove = new EventEmitter();
  constructor() {}

  ngOnInit(): void {}

  getRating(): number {
    return Math.round(this.item.rating);
  }

  getShareLink(): string {
    return `https://t.me/share/url?url=${
      this.item.link
    }&text=${"Hi! Look what I've found on the Amazon."}`;
  }

  removeItem(): void {
    this.remove.emit(this.item);
  }

  addLike(): void {
    this.item.likes++;
  }
}
