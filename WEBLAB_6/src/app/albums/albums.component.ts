import { Component, OnInit } from '@angular/core';
import { Album } from '../album';
import { AlbumsService } from '../albums.service';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {
  // @ts-ignore: Object is possibly 'null'.
  newTitle: string;
  // @ts-ignore: Object is possibly 'null'.
  albums: Album[];
  // @ts-ignore: Object is possibly 'null'.
  loaded: boolean;
  constructor(private albumsService: AlbumsService) { }

  ngOnInit(): void {
    this.getAlbums();
  }

  getAlbums() {
    this.loaded = false;
    this.albumsService.getAlbums().subscribe(albums => {
      this.albums = albums;
      this.loaded = true;
    });
  }

  deleteAlbum(id: number) {
    this.loaded = false;
    this.albums = this.albums.filter(x => x.id !== id);
    this.albumsService.deleteAlbum(id).subscribe(albums =>{
      console.log("Deleted album #" + id);
      this.loaded = true;
    });
  }

  addAlbum() {
    this.newTitle = this.newTitle.trim();
    if (!this.newTitle) return;
    
    const album = {
      title: this.newTitle
    };
    this.newTitle = '';

    this.loaded = false;
    this.albumsService.addAlbum(album as Album).subscribe(album => {
      console.log(album);
      this.albums.push(album);
      this.loaded = true;
    });
  }

}