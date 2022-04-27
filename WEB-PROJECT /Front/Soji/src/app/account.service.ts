import { Injectable } from '@angular/core';
import {User} from './user';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class AccountService {
  private userUrl = 'core/users';
  constructor( private http: HttpClient) { }
  getInfo(): Observable<User[]> {
    return this.http.get<User[]>(this.userUrl)
      .pipe(catchError(this.handleError<User[]>('getInfo', []))
      );
  }
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
