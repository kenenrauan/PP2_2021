import {Component, OnInit} from '@angular/core';
import {Post} from '../models';
import {PostsService} from '../posts.service';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit {
  posts: Post[];
  loaded: boolean;
  newPost: string;

  constructor(private postsService: PostsService) {
    this.newPost = '';
  }

  ngOnInit(): void {
    this.getPosts();
  }

  getPosts() {
    this.loaded = false;
    this.postsService.getPosts().subscribe((posts) => {
      this.posts = posts;
      this.loaded = true;
    });
  }

  addPost() {
    const post = {
      title: this.newPost
    };
    this.loaded = false;
    this.postsService.addPost(post as Post).subscribe((post) => {
      this.posts.unshift(post);
      this.newPost = '';
      this.loaded = true;
    });
  }

  deletePost(id: number) {
    this.posts = this.posts.filter((x) => x.id !== id);
    this.postsService.deletePost(id).subscribe(() => {
      console.log('deleted', id);
    });
  }

}