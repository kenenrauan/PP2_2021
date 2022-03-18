import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AlbumsService } from '../albums.service';
import { Location } from '@angular/common';
import { Photo } from '../photo';

@Component({
  selector: 'app-album-photos',
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css']
})
export class AlbumPhotosComponent implements OnInit {
  // @ts-ignore: Object is possibly 'null'.
  title: string;
  // @ts-ignore: Object is possibly 'null'.
  loaded: boolean;
  // @ts-ignore: Object is possibly 'null'.
  photos: Photo[];
  constructor(private albumsService: AlbumsService,
    private route: ActivatedRoute,
    private location: Location) { }

  ngOnInit(): void {
    this.getPhotos();
    this.getTitle();
  }

  getPhotos() {
    this.route.paramMap.subscribe(params => {
      const id = +(params.get('id') || '0');

      this.loaded = false;
      this.albumsService.getPhotos(id).subscribe(photos => {
        this.photos = photos;
        this.loaded = true;
      });
    });
  }

  getTitle() {
    this.route.paramMap.subscribe(params => {
      const id = +(params.get('id') || '0');

      this.loaded = false;
      this.albumsService.getAlbum(id).subscribe(album => {
        this.title = album.title;
        this.loaded = true;
      });
    });
  }

  returnBack() {
    this.location.back();
  }

}