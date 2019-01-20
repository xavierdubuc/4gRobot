import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RectenvComponent } from './rectenv.component';

describe('RectenvComponent', () => {
  let component: RectenvComponent;
  let fixture: ComponentFixture<RectenvComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RectenvComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RectenvComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
