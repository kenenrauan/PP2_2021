import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Album } from '../album';
import { AlbumsService } from '../albums.service';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit {
  // @ts-ignore: Object is possibly 'null'.
  loaded: boolean;
  // @ts-ignore: Object is possibly 'null'.
  album: Album;
  constructor(private albumsService: AlbumsService,
              private route: ActivatedRoute,
              private location: Location) { }

  ngOnInit(): void {
    this.getAlbum();
  }

  getAlbum() {
    this.route.paramMap.subscribe(params => {
      const id = +(params.get('id') || '0');
      
      this.loaded = false;
      this.albumsService.getAlbum(id).subscribe(album => {
        this.album = album;
        this.loaded = true;
      });
    });
  }

  updateAlbum() {
    this.loaded = false;
    this.albumsService.updateAlbum(this.album).subscribe(album => {
      console.log(album);
      this.loaded = true;
    });
  }

  returnBack() {
    this.location.back();
  }

}