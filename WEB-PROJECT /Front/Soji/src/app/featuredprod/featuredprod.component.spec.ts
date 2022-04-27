import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FeaturedprodComponent } from './featuredprod.component';

describe('FeaturedprodComponent', () => {
  let component: FeaturedprodComponent;
  let fixture: ComponentFixture<FeaturedprodComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FeaturedprodComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FeaturedprodComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
