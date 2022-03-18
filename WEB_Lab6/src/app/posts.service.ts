import {Injectable} from '@angular/core';
import {POSTS} from './fake-db';
import {Observable, of} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {Comment, Post} from './models';


@Injectable({
  providedIn: 'root'
})
export class PostsService {

  BASE_URL = 'https://jsonplaceholder.typicode.com';

  constructor(private client: HttpClient) {
  }

  // getPosts() {
  //   return of(POSTS);
  // }
  //
  // getPost(id: number) {
  //   const post = POSTS.find((x) => x.id === id);
  //   return of(post);
  // }


  getPosts(): Observable<Post[]> {
    return this.client.get<Post[]>(`${this.BASE_URL}/posts`);
  }

  getPost(id: number): Observable<Post> {
    return this.client.get<Post>(`${this.BASE_URL}/posts/${id}`);
  }

  addPost(post: Post): Observable<Post> {
    //@ts-ignore
    return this.client.post(`${this.BASE_URL}/posts`, post);
  }

  updatePost(post: Post): Observable<Post> {
    return this.client.put<Post>(`${this.BASE_URL}/posts/${post.id}`, post);
  }

  deletePost(id: number): Observable<any> {
    return this.client.delete(`${this.BASE_URL}/posts/${id}`);
  }

  getPostComments(id: number): Observable<Comment[]> {
    //@ts-ignore
    return this.client.get(`${this.BASE_URL}/posts/${id}/comments`);
  }
}