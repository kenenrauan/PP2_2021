import { Injectable } from '@angular/core';
import { Product} from './product';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import {LoginResponse} from './login-response';
import {User, UserId,UserReg} from './user';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private BASE_URL = 'http://127.0.0.1:8000';
  constructor( private http: HttpClient) { }

  registerNewUser(username,password):Observable<UserReg>{
    return this.http.post<UserReg>(`${this.BASE_URL}/core/users/`,{username,password});
  }

  getProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(`${this.BASE_URL}/core/products/`)
      .pipe(catchError(this.handleError<Product[]>('getProducts', []))
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
  getProduct(id: number): Observable<Product> {
    return this.http.get<Product>(`${this.BASE_URL}/core/products/${id}`).pipe(
      catchError(this.handleError<Product>(`getProduct id=${id}`))
    );
  }
  /* GET heroes whose name contains search term */
  searchProducts(term: string): Observable<Product[]> {
    if (!term.trim()) {
      // if not search term, return empty hero array.
      return of([]);
    }
    return this.http.get<Product[]>(`$api/products/?name=${term}`).pipe(
      catchError(this.handleError<Product[]>('searchProducts', []))
    );
  }
  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/core/auth/`, {
      username,
      password
    });

  }

  getUserId(username):Observable<UserId>{
    return this.http.get<UserId>(`http://127.0.0.1:8000/core/users/${username}/`);
  }
  }



