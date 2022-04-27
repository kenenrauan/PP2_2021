import { Injectable } from '@angular/core';
import {BehaviorSubject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StateService {
  // BehaviorSubject to store UserName
  private currentUserNameStore = new BehaviorSubject<string>("");

  // Make UserName store Observable
  public currentUserName$ = this.currentUserNameStore.asObservable();

  // Setter to update UserName
  setCurrentUserName(userName: string) {
    this.currentUserNameStore.next(userName);
  }
  constructor() { }
}

